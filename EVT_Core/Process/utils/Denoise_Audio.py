import os
import torch
import traceback
import librosa
import soundfile
from pathlib import Path

from .uvr5.mdxnet import MDXNetDereverb
from .uvr5.vr import AudioPre, AudioPreDeEcho


def uvr(
    AudioData,
    SampleRate,
    ModelPath,
    Target,
    Agg
):
    try:
        if "onnx_dereverb_by_foxjoy" in ModelPath.lower() and Path(ModelPath).suffix == ".onnx":
            pre_fun = MDXNetDereverb(
                model_path = ModelPath,
                chunks = 15
            )
        else:
            device = "cuda" if torch.cuda.is_available() else "cpu"
            func = AudioPre if "DeEcho" not in Path(ModelPath).stem else AudioPreDeEcho
            pre_fun = func(
                agg = int(Agg),
                model_path = ModelPath,
                device = device,
                is_half = False,
            )
        tmp_path = Path(os.getcwd()).joinpath("tmp.wav").as_posix()
        AudioData = librosa.resample(AudioData, orig_sr = SampleRate, target_sr = 44100)
        soundfile.write(tmp_path, AudioData.T if len(AudioData.shape) > 1 else AudioData, 44100, subtype = 'PCM_16')
        data, samplerate = pre_fun._path_audio_(
            path = tmp_path,
            target = Target,
            is_hp3 = "hp3" in Path(ModelPath).stem.lower()
        )
    except:
        traceback.print_exc()
    finally:
        os.remove(tmp_path)
        if ModelPath == "onnx_dereverb_By_FoxJoy":
            del pre_fun.pred.model
            del pre_fun.pred.model_
        else:
            del pre_fun.model
            del pre_fun
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        return data.T if len(data.shape) > 1 else data, samplerate


def Denoiser(
    AudioData,
    SampleRate,
    ModelPath,
    Target = "voice", # 指定要保留人声还是背景音
    #Agg = 10 # 人声提取激进程度(0-20, step=1)
):
    '''
    ModelName_Map = {
        "不带和声": "HP3_all_vocals",
        "带和声": "HP5_only_main_vocal",
    }
    ModelName = ModelName_Map.get(AudioType, "HP3_all_vocals")
    '''
    return uvr(
        AudioData,
        SampleRate,
        ModelPath,
        Target = Target,
        Agg = 10
    )