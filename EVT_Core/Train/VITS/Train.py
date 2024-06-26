from typing import Optional
from pathlib import Path
from datetime import datetime
import os
import sys
import re
import json
import platform
import logging
logging.basicConfig(stream = sys.stdout, encoding = 'utf-8')
logging.getLogger('numba').setLevel(logging.WARNING)
import torchaudio
import torch
from torch.nn import functional as F
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
import torch.multiprocessing as mp
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.cuda.amp import autocast, GradScaler
torch.backends.cudnn.benchmark = True
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

from .vits.Data_Utils import (
    TextAudioSpeakerLoader,
    TextAudioSpeakerCollate,
    DistributedBucketSampler
)
from .vits.Models import (
    AVAILABLE_FLOW_TYPES,
    AVAILABLE_DURATION_DISCRIMINATOR_TYPES,
    SynthesizerTrn,
    MultiPeriodDiscriminator,
    DurationDiscriminatorV1,
    DurationDiscriminatorV2
)
from .vits.Mel_Processing import (
    mel_spectrogram_torch,
    spec_to_mel_torch
)
from .vits.Commons import (
    slice_segments,
    clip_grad_value_
)
from .vits.Losses import (
    generator_loss,
    discriminator_loss,
    feature_loss,
    kl_loss
)
from .vits.Utils import (
    load_audiopaths_sid_text,
    plot_spectrogram_to_numpy,
    summarize,
    plot_alignment_to_numpy,
    save_checkpoint,
    get_logger,
    add_elements,
    #check_git_hash,
    load_checkpoint,
    remove_old_checkpoints,
    latest_checkpoint_path,
    get_hparams
)
from .vits.text import (
    _clean_text,
    #symbols
)
from .vits.text.symbols import symbols


global_step = 0


class Preprocessing:
    '''
    Preprocess
    '''
    def __init__(self,
        FileList_Path_Training: str,
        FileList_Path_Validation: str,
        Config_Dir_Save: str = './',
        Set_Eval_Interval: int = 1000,
        Set_Epochs: int = 10000,
        Set_Batch_Size: int = 16,
        Set_FP16_Run: bool = True,
        Keep_Original_Speakers: bool = False,
        Config_Path_Load: Optional[str] = None
    ):
        self.FileList_Path_Training = FileList_Path_Training
        self.FileList_Path_Validation = FileList_Path_Validation
        self.Config_Dir_Save = Config_Dir_Save
        self.Set_Eval_Interval = Set_Eval_Interval
        self.Set_Epochs = Set_Epochs
        self.Set_Batch_Size = Set_Batch_Size
        self.Set_FP16_Run = Set_FP16_Run
        self.Keep_Original_Speakers = Keep_Original_Speakers
        self.Config_Path_Load = Config_Path_Load if Keep_Original_Speakers else None

        os.makedirs(self.Config_Dir_Save, exist_ok = True)
        self.Config_Path_Edited = Path(Config_Dir_Save).joinpath(f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json").__str__()
        self.FileList_Path_Training_Updated = Path(self.Config_Path_Edited).parent.joinpath(Path(self.FileList_Path_Training).name).__str__()
        self.FileList_Path_Validation_Updated = Path(self.Config_Path_Edited).parent.joinpath(Path(self.FileList_Path_Validation).name).__str__()
        self.Out_Extension = "cleaned"

    def Configurator(self):
        '''
        Edit JSON file
        '''
        def Get_Languages(Text_Path_Training, Text_Path_Validation):
            Languages = []
            for Text_Path in [Text_Path_Training, Text_Path_Validation]:
                with open(file = Text_Path, mode = 'r', encoding = 'utf-8') as File:
                    Lines = File.readlines()
                for _, Line in enumerate(Lines):
                    Line_Text = Line.split('|', maxsplit = 2)[2]
                    Language = re.split(r'[\[\]]', Line_Text)[1]
                    Languages.append(Language) if Language not in Languages else None
            if set(Languages).issubset({'ZH', 'EN', 'JA'}):
                if set(Languages) == {'ZH'}:
                    return "mandarin"
                else:
                    return "mandarin_english_japanese"
            else:
                raise Exception('Unsupported language!')

        def Get_NewSpeakers(Text_Path_Training, Text_Path_Validation):
            Speakers = []
            for Text_Path in [Text_Path_Training, Text_Path_Validation]:
                with open(file = Text_Path, mode = 'r', encoding = 'utf-8') as File:
                    Lines = File.readlines()
                for _, Line in enumerate(Lines):
                    Speaker = Line.split('|', maxsplit = 2)[1]
                    Speakers.append(Speaker) if Speaker not in Speakers else None
            return Speakers

        def Get_OldSpeakers(Config_Path_Load):
            if Config_Path_Load is not None and Path(Config_Path_Load).exists():
                with open(file = Config_Path_Load, mode = 'rb') as ConfigFile_Extra:
                    OldSpeakers = json.load(ConfigFile_Extra)["speakers"]
            else:
                OldSpeakers = []
            return OldSpeakers

        Language = Get_Languages(self.FileList_Path_Training, self.FileList_Path_Validation)
        NewSpeakers = Get_NewSpeakers(self.FileList_Path_Training, self.FileList_Path_Validation)
        OldSpeakers = Get_OldSpeakers(self.Config_Path_Load) if self.Keep_Original_Speakers else []

        with open(file = Path(__file__).parent.joinpath('./configs', f'{Language}_base.json').__str__(), mode = 'rb') as ConfigFile_Default:
            Params = json.load(ConfigFile_Default)
        try:
            Params_Old = Params
            Params_Old["train"]["eval_interval"]   = self.Set_Eval_Interval
            Params_Old["train"]["epochs"]          = self.Set_Epochs
            Params_Old["train"]["batch_size"]      = self.Set_Batch_Size
            Params_Old["train"]["fp16_run"]        = self.Set_FP16_Run
            Params_Old["data"]["training_files"]   = f'{self.FileList_Path_Training_Updated}.{self.Out_Extension}'
            Params_Old["data"]["validation_files"] = f'{self.FileList_Path_Validation_Updated}.{self.Out_Extension}'
            Params_Old["data"]["text_cleaners"]    = [(Language + "_cleaners").lower()]
            Params_Old["data"]["n_speakers"]       = add_elements(OldSpeakers, NewSpeakers).__len__()
            Params_Old["speakers"]                 = add_elements(OldSpeakers, NewSpeakers)
            Params_New = Params_Old
        except:
            raise Exception("Please check if params exist")
        with open(self.Config_Path_Edited, 'w', encoding = 'utf-8') as File_New:
            json.dump(Params_New, File_New, indent = 4)
        print(f"Config created in {self.Config_Dir_Save}")

    def Cleaner(self):
        '''
        Convert natural language text to symbols
        '''
        def Update_SID(Config_Path, Text_Path, Save_Path):
            with open(file = Config_Path, mode = 'rb') as ConfigFile:
                NewSpeakers = json.load(ConfigFile)["speakers"]
            with open(file = Text_Path, mode = 'r', encoding = 'utf-8') as TextFile:
                Lines = TextFile.readlines()
            for Index, Line in enumerate(Lines):
                Line_Path = Line.split('|', maxsplit = 1)[0]
                Line_Path = Path(Text_Path).parent.joinpath(Line_Path).as_posix() if not Path(Line_Path).is_absolute() else Line_Path
                Speaker = Line.split('|', maxsplit = 2)[1]
                SpeakerID = NewSpeakers.index(Speaker)
                Line_Text = Line.split('|', maxsplit = 2)[2]
                Line = f"{Line_Path}|{SpeakerID}|{Line_Text}"
                Lines[Index] = Line
            with open(file = Save_Path, mode = 'w', encoding = 'utf-8') as TextFile:
                TextFile.writelines(Lines)

        def Get_Cleaners(Config_Path):
            with open(file = Config_Path, mode = 'rb') as ConfigFile:
                NewCleaners = json.load(ConfigFile)["data"]["text_cleaners"]
            return NewCleaners

        for Index, FileList in enumerate([self.FileList_Path_Training, self.FileList_Path_Validation]):
            print("START:", FileList)
            FileList_Updated = [self.FileList_Path_Training_Updated, self.FileList_Path_Validation_Updated][Index]
            Update_SID(self.Config_Path_Edited, FileList, FileList_Updated)
            Path_SID_Text = load_audiopaths_sid_text(FileList_Updated)
            for i in range(len(Path_SID_Text)):
                Path_SID_Text[i][2] = _clean_text(Path_SID_Text[i][2], Get_Cleaners(self.Config_Path_Edited))
            Filelist_Cleaned = FileList_Updated + "." + self.Out_Extension
            with open(Filelist_Cleaned, 'w', encoding = 'utf-8') as f:
                f.writelines(["|".join(x) + "\n" for x in Path_SID_Text])

    def Resampler(self):
        '''
        Resample dataset audio to fit the sampling rate setting in config
        '''
        def Get_Resample_List(Config_Path, Text_Path):
            ResampleList = []
            with open(file = Config_Path, mode = 'rb') as ConfigFile:
                SampleRate_New = json.load(ConfigFile)['data']['sampling_rate']
            with open(file = Text_Path, mode = 'r', encoding = 'utf-8') as TextFile:
                Lines = TextFile.readlines()
            for Line in Lines:
                Line_Path = Line.split('|', maxsplit = 1)[0]
                ResampleList.append((Line_Path, SampleRate_New))
            return ResampleList

        def Resample(Audio_Path, SampleRate_New):
            AudioData_Old, SampleRate_Old = torchaudio.load(Audio_Path)
            AudioData_New = torchaudio.transforms.Resample(orig_freq = SampleRate_Old, new_freq = SampleRate_New)(AudioData_Old)
            torchaudio.save(Audio_Path, src = AudioData_New, sample_rate = SampleRate_New)

        for FileList in (self.FileList_Path_Validation, self.FileList_Path_Training):
            print("Resampling audio according to", FileList)
            with ThreadPoolExecutor(max_workers = os.cpu_count()) as Executor:
                Executor.map(
                    Resample,
                    *zip(*Get_Resample_List(self.Config_Path_Edited, FileList))
                )


class Training:
    '''
    Train
    '''
    def __init__(self,
        Num_Workers: int = 4,
        Model_Path_Pretrained_G: Optional[str] = None,
        Model_Path_Pretrained_D: Optional[str] = None,
        Keep_Original_Speakers: bool = False,
        Log_Dir: str = "./"
    ):
        self.Num_Workers = Num_Workers
        self.Model_Path_Pretrained_G = Model_Path_Pretrained_G
        self.Model_Path_Pretrained_D = Model_Path_Pretrained_D
        self.Keep_Original_Speakers = Keep_Original_Speakers
        self.Log_Dir = Log_Dir

        self.UsePretrainedModel = False if None in (self.Model_Path_Pretrained_G, self.Model_Path_Pretrained_D) else True

    def evaluate(self,
        hps, generator, eval_loader, writer_eval
    ):
        generator.eval()
        with torch.no_grad():
            for batch_idx, (x, x_lengths, spec, spec_lengths, y, y_lengths, speakers) in enumerate(eval_loader):
                x, x_lengths = x.cuda(0), x_lengths.cuda(0)
                spec, spec_lengths = spec.cuda(0), spec_lengths.cuda(0)
                y, y_lengths = y.cuda(0), y_lengths.cuda(0)
                speakers = speakers.cuda(0)

                # remove else
                x = x[:1]
                x_lengths = x_lengths[:1]
                spec = spec[:1]
                spec_lengths = spec_lengths[:1]
                y = y[:1]
                y_lengths = y_lengths[:1]
                speakers = speakers[:1]
                break
            y_hat, attn, mask, *_ = generator.module.infer(x, x_lengths, speakers, max_len=1000)
            y_hat_lengths = mask.sum([1, 2]).long() * hps.data.hop_length

            mel = spec_to_mel_torch(
                spec,
                hps.data.filter_length,
                hps.data.n_mel_channels,
                hps.data.sampling_rate,
                hps.data.mel_fmin,
                hps.data.mel_fmax
            ) if not (hps.model.use_mel_posterior_encoder or hps.data.use_mel_posterior_encoder) else spec
            y_hat_mel = mel_spectrogram_torch(
                y_hat.squeeze(1).float(),
                hps.data.filter_length,
                hps.data.n_mel_channels,
                hps.data.sampling_rate,
                hps.data.hop_length,
                hps.data.win_length,
                hps.data.mel_fmin,
                hps.data.mel_fmax
            )
        image_dict = {"gen/mel": plot_spectrogram_to_numpy(y_hat_mel[0].cpu().numpy())}
        audio_dict = {"gen/audio": y_hat[0, :, :y_hat_lengths[0]]}
        if global_step == 0:
            image_dict.update({"gt/mel": plot_spectrogram_to_numpy(mel[0].cpu().numpy())})
            audio_dict.update({"gt/audio": y[0, :, :y_lengths[0]]})

        summarize(
            writer=writer_eval,
            global_step=global_step,
            images=image_dict,
            audios=audio_dict,
            audio_sampling_rate=hps.data.sampling_rate
        )
        generator.train()

    def train_and_evaluate(self,
        rank, epoch, hps, nets, optims, schedulers, scaler, loaders, logger, writers
    ):
        net_g, net_d, net_dur_disc = nets
        optim_g, optim_d, optim_dur_disc = optims
        scheduler_g, scheduler_d, scheduler_dur_disc = schedulers
        train_loader, eval_loader = loaders
        if writers is not None:
            writer, writer_eval = writers

        train_loader.batch_sampler.set_epoch(epoch)
        global global_step

        net_g.train()
        net_d.train()
        net_dur_disc.train() if net_dur_disc is not None else None

        if rank == 0:
            loader = tqdm(train_loader, desc='Loading train data')
        else:
            loader = train_loader

        for batch_idx, (x, x_lengths, spec, spec_lengths, y, y_lengths, speakers) in enumerate(loader):
            if net_g.module.use_noise_scaled_mas:
                current_mas_noise_scale = net_g.module.mas_noise_scale_initial - net_g.module.noise_scale_delta * global_step
                net_g.module.current_mas_noise_scale = max(current_mas_noise_scale, 0.0)
            x, x_lengths = x.cuda(rank, non_blocking=True), x_lengths.cuda(rank, non_blocking=True)
            spec, spec_lengths = spec.cuda(rank, non_blocking=True), spec_lengths.cuda(rank, non_blocking=True)
            y, y_lengths = y.cuda(rank, non_blocking=True), y_lengths.cuda(rank, non_blocking=True)
            speakers = speakers.cuda(rank, non_blocking=True)

            with autocast(enabled=hps.train.fp16_run):
                y_hat, l_length, attn, ids_slice, x_mask, z_mask, (z, z_p, m_p, logs_p, m_q, logs_q), (hidden_x, logw, logw_) = net_g(x, x_lengths, spec, spec_lengths, speakers)

                mel = spec_to_mel_torch(
                    spec.float(),
                    hps.data.filter_length,
                    hps.data.n_mel_channels,
                    hps.data.sampling_rate,
                    hps.data.mel_fmin,
                    hps.data.mel_fmax
                ) if not (hps.model.use_mel_posterior_encoder or hps.data.use_mel_posterior_encoder) else spec
                y_mel = slice_segments(mel, ids_slice, hps.train.segment_size // hps.data.hop_length)
                y_hat_mel = mel_spectrogram_torch(
                    y_hat.squeeze(1),
                    hps.data.filter_length,
                    hps.data.n_mel_channels,
                    hps.data.sampling_rate,
                    hps.data.hop_length,
                    hps.data.win_length,
                    hps.data.mel_fmin,
                    hps.data.mel_fmax
                )
                y = slice_segments(y, ids_slice * hps.data.hop_length, hps.train.segment_size) # slice

                # Discriminator
                y_d_hat_r, y_d_hat_g, _, _ = net_d(y, y_hat.detach())
                with autocast(enabled=False):
                    loss_disc, losses_disc_r, losses_disc_g = discriminator_loss(y_d_hat_r, y_d_hat_g)
                    loss_disc_all = loss_disc

                # Duration Discriminator
                if net_dur_disc is not None:
                    y_dur_hat_r, y_dur_hat_g = net_dur_disc(hidden_x.detach(), x_mask.detach(), logw_.detach(), logw.detach())
                    with autocast(enabled=False):
                        # TODO: I think need to mean using the mask, but for now, just mean all
                        loss_dur_disc, losses_dur_disc_r, losses_dur_disc_g = discriminator_loss(y_dur_hat_r, y_dur_hat_g)
                        loss_dur_disc_all = loss_dur_disc
                    optim_dur_disc.zero_grad()
                    scaler.scale(loss_dur_disc_all).backward()
                    scaler.unscale_(optim_dur_disc)
                    grad_norm_dur_disc = clip_grad_value_(net_dur_disc.parameters(), None)
                    scaler.step(optim_dur_disc)

            optim_d.zero_grad()
            scaler.scale(loss_disc_all).backward()
            scaler.unscale_(optim_d)
            grad_norm_d = clip_grad_value_(net_d.parameters(), None)
            scaler.step(optim_d)

            with autocast(enabled=hps.train.fp16_run):
                # Generator
                y_d_hat_r, y_d_hat_g, fmap_r, fmap_g = net_d(y, y_hat)
                if net_dur_disc is not None:
                    y_dur_hat_r, y_dur_hat_g = net_dur_disc(hidden_x, x_mask, logw_, logw)
                with autocast(enabled=False):
                    loss_dur = torch.sum(l_length.float())
                    loss_mel = F.l1_loss(y_mel, y_hat_mel) * hps.train.c_mel
                    loss_kl = kl_loss(z_p, logs_q, m_p, logs_p, z_mask) * hps.train.c_kl

                    loss_fm = feature_loss(fmap_r, fmap_g)
                    loss_gen, losses_gen = generator_loss(y_d_hat_g)
                    loss_gen_all = loss_gen + loss_fm + loss_mel + loss_dur + loss_kl
                    if net_dur_disc is not None:
                        loss_dur_gen, losses_dur_gen = generator_loss(y_dur_hat_g)
                        loss_gen_all += loss_dur_gen

            optim_g.zero_grad()
            scaler.scale(loss_gen_all).backward()
            scaler.unscale_(optim_g)
            grad_norm_g = clip_grad_value_(net_g.parameters(), None)
            scaler.step(optim_g)
            scaler.update()

            if rank == 0:
                if global_step % hps.train.log_interval == 0:
                    lr = optim_g.param_groups[0]['lr']
                    losses = [loss_disc, loss_gen, loss_fm, loss_mel, loss_dur, loss_kl]
                    logger.info('Train Epoch: {} [{:.0f}%]'.format(epoch, 100. * batch_idx / len(train_loader)))
                    logger.info([x.item() for x in losses] + [global_step, lr])

                    scalar_dict = {"loss/g/total": loss_gen_all, "loss/d/total": loss_disc_all, "learning_rate": lr, "grad_norm_d": grad_norm_d, "grad_norm_g": grad_norm_g}
                    scalar_dict.update({"loss/dur_disc/total": loss_dur_disc_all, "grad_norm_dur_disc": grad_norm_dur_disc}) if net_dur_disc is not None else None
                    scalar_dict.update({"loss/g/fm": loss_fm, "loss/g/mel": loss_mel, "loss/g/dur": loss_dur, "loss/g/kl": loss_kl})

                    scalar_dict.update({"loss/g/{}".format(i): v for i, v in enumerate(losses_gen)})
                    scalar_dict.update({"loss/d_r/{}".format(i): v for i, v in enumerate(losses_disc_r)})
                    scalar_dict.update({"loss/d_g/{}".format(i): v for i, v in enumerate(losses_disc_g)})

                # if net_dur_disc is not None:
                #   scalar_dict.update({"loss/dur_disc_r" : f"{losses_dur_disc_r}"})
                #   scalar_dict.update({"loss/dur_disc_g" : f"{losses_dur_disc_g}"})
                #   scalar_dict.update({"loss/dur_gen" : f"{loss_dur_gen}"})

                    image_dict = {
                        "slice/mel_org": plot_spectrogram_to_numpy(y_mel[0].data.cpu().numpy()),
                        "slice/mel_gen": plot_spectrogram_to_numpy(y_hat_mel[0].data.cpu().numpy()),
                        "all/mel": plot_spectrogram_to_numpy(mel[0].data.cpu().numpy()),
                        "all/attn": plot_alignment_to_numpy(attn[0,0].data.cpu().numpy())
                    }
                    summarize(
                        writer=writer,
                        global_step=global_step,
                        images=image_dict,
                        scalars=scalar_dict)

                if global_step % hps.train.eval_interval == 0:
                    self.evaluate(hps, net_g, eval_loader, writer_eval)
                    save_checkpoint(net_g, optim_g, hps.train.learning_rate, epoch, Path(hps.model_dir).joinpath("G_{}.pth".format(global_step)).__str__())
                    save_checkpoint(net_d, optim_d, hps.train.learning_rate, epoch, Path(hps.model_dir).joinpath("D_{}.pth".format(global_step)).__str__())
                    save_checkpoint(net_dur_disc, optim_dur_disc, hps.train.learning_rate, epoch, os.path.join(hps.model_dir, "DUR_{}.pth".format(global_step))) if net_dur_disc is not None else None

                    remove_old_checkpoints(hps.model_dir, prefixes=["G_*.pth", "D_*.pth", "DUR_*.pth"])
            global_step += 1

        if rank == 0:
            logger.info('====> Epoch: {}'.format(epoch))

    def run(self, rank, n_gpus, hps):
        global global_step
        net_dur_disc = None
        if rank == 0:
            logger = get_logger(hps.model_dir)
            #logger.info(hps)
            #check_git_hash(hps.model_dir)
            writer = SummaryWriter(log_dir = self.Log_Dir)
            writer_eval = SummaryWriter(log_dir = Path(self.Log_Dir).joinpath("eval").__str__())

        dist.init_process_group(
            backend = 'gloo' if platform.system() == 'Windows' else 'nccl', # Windows不支持NCCL backend，故使用GLOO
            init_method = 'env://',
            world_size = n_gpus,
            rank = rank
        )

        torch.manual_seed(hps.train.seed)
        torch.cuda.set_device(rank)

        if "use_mel_posterior_encoder" in hps.model.keys() and hps.model.use_mel_posterior_encoder == True:
            print("Using mel posterior encoder for VITS2")
            posterior_channels = 80  # vits2
            hps.data.use_mel_posterior_encoder = True
        else:
            print("Using lin posterior encoder for VITS1")
            posterior_channels = hps.data.filter_length // 2 + 1
            hps.data.use_mel_posterior_encoder = False

        train_dataset = TextAudioSpeakerLoader(hps.data.training_files, hps.data)
        train_sampler = DistributedBucketSampler(
            train_dataset,
            hps.train.batch_size,
            [32,300,400,500,600,700,800,900,1000],
            num_replicas=n_gpus,
            rank=rank,
            shuffle=True
        )
        collate_fn = TextAudioSpeakerCollate()
        train_loader = DataLoader(
            train_dataset,
            num_workers=self.Num_Workers,
            shuffle=False,
            pin_memory=True,
            collate_fn=collate_fn,
            batch_sampler=train_sampler
        )
        if rank == 0:
            eval_dataset = TextAudioSpeakerLoader(hps.data.validation_files, hps.data)
            eval_loader = DataLoader(
                eval_dataset,
                num_workers=0,
                shuffle=False,
                batch_size=hps.train.batch_size,
                pin_memory=True,
                drop_last=False,
                collate_fn=collate_fn
            )

        # some of these flags are not being used in the code and directly set in hps json file.
        # they are kept here for reference and prototyping.
        if "use_transformer_flows" in hps.model.keys() and hps.model.use_transformer_flows == True:
            use_transformer_flows = True
            transformer_flow_type = hps.model.transformer_flow_type
            print(f"Using transformer flows {transformer_flow_type} for VITS2")
            assert transformer_flow_type in AVAILABLE_FLOW_TYPES, f"transformer_flow_type must be one of {AVAILABLE_FLOW_TYPES}"
        else:
            print("Using normal flows for VITS1")
            use_transformer_flows = False

        if "use_spk_conditioned_encoder" in hps.model.keys() and hps.model.use_spk_conditioned_encoder == True:
            if hps.data.n_speakers == 0:
                raise ValueError("n_speakers must be > 0 when using spk conditioned encoder to train multi-speaker model")
            use_spk_conditioned_encoder = True
        else:
            print("Using normal encoder for VITS1")
            use_spk_conditioned_encoder = False

        if "use_noise_scaled_mas" in hps.model.keys() and hps.model.use_noise_scaled_mas == True:
            print("Using noise scaled MAS for VITS2")
            use_noise_scaled_mas = True
            mas_noise_scale_initial = 0.01
            noise_scale_delta = 2e-6
        else:
            print("Using normal MAS for VITS1")
            use_noise_scaled_mas = False
            mas_noise_scale_initial = 0.0
            noise_scale_delta = 0.0

        # Initialize VITS models and move to GPU
        net_g = SynthesizerTrn(
            len(symbols),
            posterior_channels,
            hps.train.segment_size // hps.data.hop_length,
            n_speakers=hps.data.n_speakers,
            mas_noise_scale_initial=mas_noise_scale_initial,
            noise_scale_delta=noise_scale_delta,
            **hps.model
        ).cuda(rank)
        net_d = MultiPeriodDiscriminator(
            hps.model.use_spectral_norm
        ).cuda(rank)
        if "use_duration_discriminator" in hps.model.keys() and hps.model.use_duration_discriminator == True:
            use_duration_discriminator = True

            # add duration discriminator type here
            duration_discriminator_type = getattr(hps.model, "duration_discriminator_type", "dur_disc_1")
            print(f"Using duration_discriminator {duration_discriminator_type} for VITS2")
            assert duration_discriminator_type in AVAILABLE_DURATION_DISCRIMINATOR_TYPES, f"duration_discriminator_type must be one of {AVAILABLE_DURATION_DISCRIMINATOR_TYPES}"
            duration_discriminator_type = AVAILABLE_DURATION_DISCRIMINATOR_TYPES
            if duration_discriminator_type == "dur_disc_1":
                net_dur_disc = DurationDiscriminatorV1(
                    hps.model.hidden_channels,
                    hps.model.hidden_channels,
                    3,
                    0.1,
                    gin_channels=hps.model.gin_channels if hps.data.n_speakers != 0 else 0,
                ).cuda(rank)
            elif duration_discriminator_type == "dur_disc_2":
                net_dur_disc = DurationDiscriminatorV2(
                    hps.model.hidden_channels,
                    hps.model.hidden_channels,
                    3,
                    0.1,
                    gin_channels=hps.model.gin_channels if hps.data.n_speakers != 0 else 0,
                ).cuda(rank) 
        else:
            print("NOT using any duration discriminator like VITS1")
            net_dur_disc = None
            use_duration_discriminator = False

        # Build optimizers for the initialized VITS models
        optim_g = torch.optim.AdamW(
            filter(lambda net_g_params: net_g_params.requires_grad, net_g.parameters()), # Filter out params which don't require gradient
            hps.train.learning_rate,
            betas=hps.train.betas,
            eps=hps.train.eps
        )
        optim_d = torch.optim.AdamW(
            net_d.parameters(),
            hps.train.learning_rate,
            betas=hps.train.betas,
            eps=hps.train.eps
        )
        optim_dur_disc = torch.optim.AdamW(
            net_dur_disc.parameters(),
            hps.train.learning_rate,
            betas=hps.train.betas,
            eps=hps.train.eps
        ) if net_dur_disc is not None else None

        # Build DDP models for the initialized VITS models
        net_g = DDP(net_g, device_ids = [rank], find_unused_parameters = True)
        net_d = DDP(net_d, device_ids = [rank], find_unused_parameters = False)
        net_dur_disc = DDP(net_dur_disc, device_ids=[rank]) if net_dur_disc is not None else None

        # Load state dict from checkpoint for the initialized VITS models and get the optimizer, learning rate and iteration
        try:
            _, optim_g, lr_g, epoch_str = load_checkpoint(
                self.Model_Path_Pretrained_G if self.UsePretrainedModel else latest_checkpoint_path(hps.model_dir, "G_*.pth"),
                net_g,
                optim_g,
                self.Keep_Original_Speakers if self.UsePretrainedModel else True
            )
            _, optim_d, lr_d, epoch_str = load_checkpoint(
                self.Model_Path_Pretrained_D if self.UsePretrainedModel else latest_checkpoint_path(hps.model_dir, "D_*.pth"),
                net_d,
                optim_d,
                self.Keep_Original_Speakers if self.UsePretrainedModel else True
            )
            _, _, _, epoch_str = load_checkpoint(
                latest_checkpoint_path(hps.model_dir, "DUR_*.pth"),
                net_dur_disc,
                optim_dur_disc
            ) if net_dur_disc is not None else (_, _, _, epoch_str)

            # To prevent KeyError: "param 'initial_lr' is not specified in param_groups[0] when resuming an optimizer"
            if optim_g.param_groups[0].get('initial_lr') is None:
                optim_g.param_groups[0]['initial_lr'] = lr_g
            if optim_d.param_groups[0].get('initial_lr') is None:
                optim_d.param_groups[0]['initial_lr'] = lr_d

            global_step = (epoch_str - 1) * len(train_loader) # > 0
            print(f"Continue from step {global_step}")

        except Exception as e:
            epoch_str = 1
            global_step = 0
            print(f"Got Exception: {e}. Start from step 0")

        # Build learning rate schedulers for optimizers
        scheduler_g = torch.optim.lr_scheduler.ExponentialLR(optim_g, gamma = hps.train.lr_decay, last_epoch = epoch_str - 2)
        scheduler_d = torch.optim.lr_scheduler.ExponentialLR(optim_d, gamma = hps.train.lr_decay, last_epoch = epoch_str - 2)
        scheduler_dur_disc = torch.optim.lr_scheduler.ExponentialLR(optim_dur_disc, gamma=hps.train.lr_decay, last_epoch=epoch_str - 2) if net_dur_disc is not None else None

        # Build gradient scaler
        scaler = GradScaler(enabled = hps.train.fp16_run)

        # Start training (and evaluating)
        for epoch in range(epoch_str, hps.train.epochs + 1):
            if rank == 0:
                self.train_and_evaluate(
                    rank, epoch, hps, [net_g, net_d, net_dur_disc], [optim_g, optim_d, optim_dur_disc], [scheduler_g, scheduler_d, scheduler_dur_disc], scaler,
                    [train_loader, eval_loader], logger, [writer, writer_eval]
                )
            else:
                self.train_and_evaluate(
                    rank, epoch, hps, [net_g, net_d, net_dur_disc], [optim_g, optim_d, optim_dur_disc], [scheduler_g, scheduler_d, scheduler_dur_disc], scaler,
                    [train_loader, None], None, None
                )
            scheduler_g.step()
            scheduler_d.step()
            scheduler_dur_disc.step() if net_dur_disc is not None else None


class Voice_Training(Preprocessing, Training):
    '''
    1. Preprocess
    2. Train & Evaluate
    '''
    def __init__(self,
        FileList_Path_Training: str,
        FileList_Path_Validation: str,
        Set_Epochs: int = 10000,
        Set_Eval_Interval: int = 1000,
        Set_Batch_Size: int = 16,
        Set_FP16_Run: bool = True,
        Keep_Original_Speakers: bool = False,
        Config_Path_Load: Optional[str] = None,
        Num_Workers: int = 4,
        Use_PretrainedModels: bool = True,
        Model_Path_Pretrained_G: Optional[str] = None,
        Model_Path_Pretrained_D: Optional[str] = None,
        Output_Root: str = "./",
        Output_Dir_Name: str = "",
        Output_LogDir: str = ""
    ):
        Dir_Output = Path(Output_Root).joinpath(Output_Dir_Name).as_posix()
        Preprocessing.__init__(self, FileList_Path_Training, FileList_Path_Validation, Dir_Output, Set_Eval_Interval, Set_Epochs, Set_Batch_Size, Set_FP16_Run, Keep_Original_Speakers, Config_Path_Load)
        Training.__init__(self, Num_Workers, Model_Path_Pretrained_G if Use_PretrainedModels else None, Model_Path_Pretrained_D if Use_PretrainedModels else None, Keep_Original_Speakers, Output_LogDir)
        self.Model_Dir_Save = Dir_Output

    def Preprocessing_and_Training(self):
        # Preprocess
        self.Configurator()
        self.Cleaner()
        self.Resampler()

        # Train & Evaluate
        """Assume Single Node Multi GPUs Training Only"""
        assert torch.cuda.is_available(), "CPU training is not allowed."

        n_gpus = torch.cuda.device_count()
        os.environ['MASTER_ADDR'] = 'localhost'
        os.environ['MASTER_PORT'] = '8000'

        hps = get_hparams(
            Config_Path = self.Config_Path_Edited,
            Model_Dir = self.Model_Dir_Save
        )
        mp.spawn(super().run, args = (n_gpus, hps,), nprocs = n_gpus)