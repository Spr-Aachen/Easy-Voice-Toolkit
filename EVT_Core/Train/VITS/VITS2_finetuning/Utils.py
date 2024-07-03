import os
import re
import glob
import sys
import shutil
import logging
logging.basicConfig(stream = sys.stdout, encoding = 'utf-8')
logger = logging
import json
import subprocess
import matplotlib
import matplotlib.pylab as plt
import numpy as np
import torch
from typing import Optional
from pathlib import Path


MATPLOTLIB_FLAG = False


def load_checkpoint(checkpoint_path, model, optimizer, keep_speaker_emb: bool = False):
    assert os.path.isfile(checkpoint_path)
    checkpoint_dict = torch.load(checkpoint_path, map_location='cpu')
    iteration = checkpoint_dict['iteration']
    learning_rate = checkpoint_dict['learning_rate']
    optimizer.load_state_dict(checkpoint_dict['optimizer']) if optimizer is not None else None
    def get_new_state_dict(state_dict, saved_state_dict, keep_speaker_emb):
        new_state_dict = {}
        for layer_param, tensor in state_dict.items():
            try: # Assign tensor of layer param from saved state dict to new state dict while layer param is not embedding's weight, otherwise use the current tensor
                if layer_param == 'emb_g.weight':
                    if keep_speaker_emb: # Keep the original speaker embedding, otherwise drop it
                        tensor[:saved_state_dict[layer_param].shape[0], :] = saved_state_dict[layer_param]
                    new_state_dict[layer_param] = tensor
                else:
                    new_state_dict[layer_param] = saved_state_dict[layer_param]
            except:
                logger.info("%s is not in the checkpoint" % layer_param)
                new_state_dict[layer_param] = tensor
        return new_state_dict
    if hasattr(model, 'module'):
        model.module.load_state_dict(get_new_state_dict(model.module.state_dict(), checkpoint_dict['model'], keep_speaker_emb))
    else:
        model.load_state_dict(get_new_state_dict(model.state_dict(), checkpoint_dict['model'], keep_speaker_emb))
    logger.info(f"Loaded checkpoint '{checkpoint_path}' (iteration {iteration})")
    return model, optimizer, learning_rate, iteration


def save_checkpoint(model, optimizer, learning_rate, iteration, checkpoint_path): # fix issue: torch.save doesn't support chinese path
    logger.info(f"Saving model and optimizer state at iteration {iteration} to {checkpoint_path}")
    if hasattr(model, 'module'):
        state_dict = model.module.state_dict()
    else:
        state_dict = model.state_dict()
    checkpoint_path_tmp = Path(Path(checkpoint_path).root).joinpath("checkpoint_tmp").as_posix()
    torch.save(
        {
            'model': state_dict,
            'iteration': iteration,
            'optimizer': optimizer.state_dict(),
            'learning_rate': learning_rate
        },
        checkpoint_path_tmp
    )
    shutil.move(checkpoint_path_tmp, Path(checkpoint_path).parent.as_posix())


def summarize(writer, global_step, scalars={}, histograms={}, images={}, audios={}, audio_sampling_rate=22050):
    for k, v in scalars.items():
        writer.add_scalar(k, v, global_step)
    for k, v in histograms.items():
        writer.add_histogram(k, v, global_step)
    for k, v in images.items():
        writer.add_image(k, v, global_step, dataformats='HWC')
    for k, v in audios.items():
        writer.add_audio(k, v, global_step, audio_sampling_rate)


def latest_checkpoint_path(dir_path, regex="G_*.pth"):
    f_list = glob.glob(os.path.normpath(os.path.join(dir_path, regex)))
    f_list.sort(key=lambda f: int("".join(filter(str.isdigit, f))))
    x = f_list[-1]
    print(x)
    return x


def remove_old_checkpoints(cp_dir, prefixes=['G_*.pth', 'D_*.pth', 'DUR_*.pth']):
    def scan_checkpoint(dir_path, regex):
        f_list = glob.glob(os.path.join(dir_path, regex))
        f_list.sort(key=lambda f: int("".join(filter(str.isdigit, f))))
        if len(f_list) == 0:
            return None
        return f_list
    for prefix in prefixes:
        sorted_ckpts = scan_checkpoint(cp_dir, prefix)
        if sorted_ckpts and len(sorted_ckpts) > 3:
            for ckpt_path in sorted_ckpts[:-3]:
                os.remove(ckpt_path)
                print("removed {}".format(ckpt_path))


def plot_spectrogram_to_numpy(spectrogram):
    global MATPLOTLIB_FLAG
    if not MATPLOTLIB_FLAG:
        matplotlib.use("Agg")
        MATPLOTLIB_FLAG = True
        mpl_logger = logging.getLogger('matplotlib')
        mpl_logger.setLevel(logging.WARNING)

    fig, ax = plt.subplots(figsize=(10,2))
    im = ax.imshow(spectrogram, aspect="auto", origin="lower", interpolation='none')
    plt.colorbar(im, ax=ax)
    plt.xlabel("Frames")
    plt.ylabel("Channels")
    plt.tight_layout()

    fig.canvas.draw()
    data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close()
    return data


def plot_alignment_to_numpy(alignment, info=None):
    global MATPLOTLIB_FLAG
    if not MATPLOTLIB_FLAG:
        matplotlib.use("Agg")
        MATPLOTLIB_FLAG = True
        mpl_logger = logging.getLogger('matplotlib')
        mpl_logger.setLevel(logging.WARNING)

    fig, ax = plt.subplots(figsize=(6, 4))
    im = ax.imshow(alignment.transpose(), aspect='auto', origin='lower', interpolation='none')
    fig.colorbar(im, ax=ax)
    xlabel = 'Decoder timestep'
    if info is not None:
            xlabel += '\n\n' + info
    plt.xlabel(xlabel)
    plt.ylabel('Encoder timestep')
    plt.tight_layout()

    fig.canvas.draw()
    data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close()
    return data


def load_audiopaths_sid_text(filename, split = "|"):
    with open(filename, 'r', encoding = 'utf-8') as f:
        audiopaths_sid_text = [line.strip().split(split) for line in f]
    return audiopaths_sid_text


def add_elements(
    Iterable1,
    Iterable2
):
    '''
    Add unique elements form Iterable2 to Iterable1
    '''
    def GetDictKeys(Iterable):
        return sorted(Iterable.keys(), key = lambda Key: Iterable[Key]) if isinstance(Iterable, dict) else Iterable
    Iterable1, Iterable2 = GetDictKeys(Iterable1), GetDictKeys(Iterable2)
    for Element in Iterable2:
        Iterable1.append(Element) if Element not in Iterable1 else None
    return Iterable1


def check_git_hash(model_dir):
    source_dir = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(os.path.normpath(os.path.join(source_dir, ".git"))):
        logger.warn(f"{source_dir} is not a git repository, therefore hash value comparison will be ignored.")
        return

    cur_hash = subprocess.getoutput("git rev-parse HEAD")

    path = os.path.normpath(os.path.join(model_dir, "githash"))
    if os.path.exists(path):
        saved_hash = open(path).read()
        if saved_hash != cur_hash:
            logger.warn("git hash values are different. {}(saved) != {}(current)".format(saved_hash[:8], cur_hash[:8]))
    else:
        open(path, "w").write(cur_hash)


def get_logger(model_dir, filename="train.log"):
    global logger
    logger = logging.getLogger(os.path.basename(model_dir))
    logger.setLevel(logging.DEBUG)

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    handler = logging.FileHandler(os.path.normpath(os.path.join(model_dir, filename)))
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter("%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s"))
    logger.addHandler(handler)
    return logger


class HParams():
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if type(v) == dict:
                v = HParams(**v)
            self[k] = v

    def keys(self):
        return self.__dict__.keys()

    def items(self):
        return self.__dict__.items()

    def values(self):
        return self.__dict__.values()

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __contains__(self, key):
        return key in self.__dict__

    def __repr__(self):
        return self.__dict__.__repr__()


def get_hparams(
    Config_Path: str,
    Model_Dir: Optional[str] = None
):
    with open(Config_Path, 'r', encoding = 'utf-8') as f:
        data = f.read()
    config = json.loads(data)
    hparams = HParams(**config)

    if Model_Dir is not None:
        os.makedirs(Model_Dir) if not Path(Model_Dir).exists() else None
        hparams.model_dir = Model_Dir

    return hparams


def Get_Config_Path(ConfigPath):
    if Path(ConfigPath).is_dir():
        ConfigPaths = [File for File in os.listdir(ConfigPath) if Path(File).suffix == '.json']
        ConfigPath = sorted(ConfigPaths, key = lambda ConfigPath: re.sub(r'[A-Za-z]+', '', Path(ConfigPath).name))[-1]
    return ConfigPath


def Get_Model_Path(ModelPath):
    if Path(ModelPath).is_dir():
        ModelPaths = [File for File in os.listdir(ModelPath) if Path(File).suffix == '.pth' and 'G_' in File]
        ModelPath = sorted(ModelPaths, key = lambda ModelPath: re.sub(r'G_[A-Za-z]+', '', Path(ModelPath).name))[-1]
    return ModelPath