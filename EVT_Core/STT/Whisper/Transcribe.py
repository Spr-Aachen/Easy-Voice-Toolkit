import hashlib
import io
import os
import glob
import urllib
import warnings
import torch
import numpy as np
from tqdm import tqdm
from typing import List, Optional, Union
from pathlib import Path

from .whisper.Transcribe import transcribe
from .whisper.Utils import optional_int, optional_float, str2bool, get_writer
from .whisper.Model import ModelDimensions, Whisper


_MODELS = {
    "tiny.en": "https://openaipublic.azureedge.net/main/whisper/models/d3dd57d32accea0b295c96e26691aa14d8822fac7d9d27d5dc00b4ca2826dd03/tiny.en.pt",
    "tiny": "https://openaipublic.azureedge.net/main/whisper/models/65147644a518d12f04e32d6f3b26facc3f8dd46e5390956a9424a650c0ce22b9/tiny.pt",
    "base.en": "https://openaipublic.azureedge.net/main/whisper/models/25a8566e1d0c1e2231d1c762132cd20e0f96a85d16145c3a00adf5d1ac670ead/base.en.pt",
    "base": "https://openaipublic.azureedge.net/main/whisper/models/ed3a0b6b1c0edf879ad9b11b1af5a0e6ab5db9205f891f668f8b0e6c6326e34e/base.pt",
    "small.en": "https://openaipublic.azureedge.net/main/whisper/models/f953ad0fd29cacd07d5a9eda5624af0f6bcf2258be67c92b79389873d91e0872/small.en.pt",
    "small": "https://openaipublic.azureedge.net/main/whisper/models/9ecf779972d90ba49c06d968637d720dd632c55bbf19d441fb42bf17a411e794/small.pt",
    "medium.en": "https://openaipublic.azureedge.net/main/whisper/models/d7440d1dc186f76616474e0ff0b3b6b879abc9d1a4926b7adfa41db2d497ab4f/medium.en.pt",
    "medium": "https://openaipublic.azureedge.net/main/whisper/models/345ae4da62f9b3d59415adc60127b97c714f32e89e936602e85993674d08dcb1/medium.pt",
    "large-v1": "https://openaipublic.azureedge.net/main/whisper/models/e4b87e7e0bf463eb8e6956e646f1e277e901512310def2c24bf0e11bd3c28e9a/large-v1.pt",
    "large-v2": "https://openaipublic.azureedge.net/main/whisper/models/81f7c96c852ee8fc832187b0132e569d6c3065a3252ed18e56effd0b6a73e524/large-v2.pt",
    "large": "https://openaipublic.azureedge.net/main/whisper/models/81f7c96c852ee8fc832187b0132e569d6c3065a3252ed18e56effd0b6a73e524/large-v2.pt",
}


def _download(url: str, root: str, in_memory: bool) -> Union[bytes, str]:
    os.makedirs(root, exist_ok=True)

    expected_sha256 = url.split("/")[-2]
    download_target = os.path.join(root, os.path.basename(url))

    if os.path.exists(download_target) and not os.path.isfile(download_target):
        raise RuntimeError(f"{download_target} exists and is not a regular file")

    if os.path.isfile(download_target):
        with open(download_target, "rb") as f:
            model_bytes = f.read()
        if hashlib.sha256(model_bytes).hexdigest() == expected_sha256:
            return model_bytes if in_memory else download_target
        else:
            warnings.warn(f"{download_target} exists, but the SHA256 checksum does not match; re-downloading the file")

    with urllib.request.urlopen(url) as source, open(download_target, "wb") as output:
        with tqdm(total=int(source.info().get("Content-Length")), ncols=80, unit='iB', unit_scale=True, unit_divisor=1024) as loop:
            while True:
                buffer = source.read(8192)
                if not buffer:
                    break

                output.write(buffer)
                loop.update(len(buffer))

    model_bytes = open(download_target, "rb").read()
    if hashlib.sha256(model_bytes).hexdigest() != expected_sha256:
        raise RuntimeError("Model has been downloaded but the SHA256 checksum does not not match. Please retry loading the model.")

    return model_bytes if in_memory else download_target


def available_models() -> List[str]:
    """Returns the names of available models"""
    return list(_MODELS.keys())


def load_model(name: str, device: Optional[Union[str, torch.device]] = None, download_root: str = None, in_memory: bool = False) -> Whisper:
    """
    Load a Whisper ASR model

    Parameters
    ----------
    name : str
        one of the official model names listed by `whisper.available_models()`, or
        path to a model checkpoint containing the model dimensions and the model state_dict.
    device : Union[str, torch.device]
        the PyTorch device to put the model into
    download_root: str
        path to download the model files; by default, it uses "~/.cache/whisper"
    in_memory: bool
        whether to preload the model weights into host memory

    Returns
    -------
    model : Whisper
        The Whisper ASR model instance
    """

    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    if download_root is None:
        download_root = os.path.join(
            os.getenv(
                "XDG_CACHE_HOME",
                os.path.join(
                    os.path.expanduser("~"), ".cache"
                )
            ),
            "whisper"
        )

    if name in _MODELS:
        checkpoint_file = _download(_MODELS[name], download_root, in_memory)
    elif os.path.isfile(name):
        checkpoint_file = open(name, "rb").read() if in_memory else name
    else:
        raise RuntimeError(f"Model {name} not found; available models = {available_models()}")

    with (io.BytesIO(checkpoint_file) if in_memory else open(checkpoint_file, "rb")) as fp:
        checkpoint = torch.load(fp, map_location=device)
    del checkpoint_file

    dims = ModelDimensions(**checkpoint["dims"])
    model = Whisper(dims)
    model.load_state_dict(checkpoint["model_state_dict"])

    return model.to(device)


class Voice_Transcribing:
    '''
    Transcribe WAV files to text and save as SRT files
    '''
    def __init__(self,
        Model_Path: str = './Models/.pt',
        Audio_Dir: str = './WAV_Files',
        Verbose: str2bool = True,
        Add_LanguageInfo: bool = True,
        Condition_on_Previous_Text: str2bool = False,
        fp16: str2bool = True,
        Output_Root: str = './',
        Output_Name: str = 'SRT_Files'
    ):
        self.Model_Name = Path(Model_Path).stem.__str__() # name of the Whisper model to use    choices = available_models()
        self.Model_Dir = Path(Model_Path).parent.__str__() # the path to save model files; uses ~/.cache/whisper by default
        self.Device: str = "cuda" if torch.cuda.is_available() else "cpu" # device to use for PyTorch inference
        self.Audio_Dir = Audio_Dir # the path to save audio files
        self.SRT_Dir = Path(Output_Root).joinpath(Output_Name).as_posix() # help = "directory to save the outputs
        self.Verbose = Verbose # whether to print out the progress and debug messages
        self.Task = 'transcribe' # whether to perform X->X speech recognition ('transcribe') or X->English translation ('translate')
        self.Language = None # language spoken in the audio, specify None to perform language detection
        self.Add_LanguageInfo = Add_LanguageInfo # add language info to the transcription
        self.Temperature: float = 0 # temperature to use for sampling
        self.Best_of: optional_int = 5 # number of candidates when sampling with non-zero temperature
        self.Beam_Size: optional_int = 5 # number of beams in beam search, only applicable when temperature is zero
        self.Patience: float = None # optional patience value to use in beam decoding, as in https://arxiv.org/abs/2204.05424, the default (1.0) is equivalent to conventional beam search
        self.Length_Penalty: float = None # optional token length penalty coefficient (alpha) as in https://arxiv.org/abs/1609.08144, uses simple length normalization by default
        self.Initial_Prompt: str = None # optional text to provide as a prompt for the first window
        self.Suppress_Tokens: str = "-1" # comma-separated list of token ids to suppress during sampling; '-1' will suppress most special characters except common punctuations
        self.Condition_on_Previous_Text = Condition_on_Previous_Text # if True, provide the previous output of the model as a prompt for the next window; disabling may make the text inconsistent across windows, but the model becomes less prone to getting stuck in a failure loop
        self.fp16 = fp16 # whether to perform inference in fp16; True by default
        self.Temperature_Increment_on_Fallback: optional_float = 0.2 # temperature to increase when falling back when the decoding fails to meet either of the thresholds below
        self.Compression_Ratio_Threshold: optional_float = 2.4 # if the gzip compression ratio is higher than this value, treat the decoding as failed
        self.Logprob_Threshold: optional_float = -1.0 # if the average log probability is lower than this value, treat the decoding as failed
        self.No_Speech_Threshold: optional_float = 0.6 # if the probability of the <|nospeech|> token is higher than this value AND the decoding has failed due to `logprob_threshold`, consider the segment as silence
        self.Threads: optional_int = 0 # number of threads used by torch for CPU inference; supercedes MKL_NUM_THREADS/OMP_NUM_THREADS
    
    def Transcriber(self):
        os.makedirs(self.Audio_Dir, exist_ok = True)
        os.makedirs(self.SRT_Dir, exist_ok = True)

        if self.Model_Name.endswith(".en") and self.Language not in {"en", "English"}:
            if self.Language is not None:
                warnings.warn(f"{self.Model_Name} is an English-only model but receipted '{self.Language}'; using English instead.")
            self.Language = "en"

        if (increment := self.Temperature_Increment_on_Fallback) is not None:
            Temperature = tuple(np.arange(self.Temperature, 1.0 + 1e-6, increment))
        else:
            Temperature = [self.Temperature]

        if (threads := self.Threads) > 0:
            torch.set_num_threads(threads)

        Model = load_model(
            name = self.Model_Name,
            device = self.Device,
            download_root = self.Model_Dir
        )

        # Filter out the audio files and get their paths
        PathList = []
        for Dir_Path, Folder_Names, File_Names in os.walk(self.Audio_Dir):
            for Index, File_Name in enumerate(File_Names):
                for extension in ['.flac', '.wav', '.mp3', '.aac', '.m4a', '.wma', '.aiff', '.au', '.ogg']:
                    if File_Name.endswith(extension):
                        File_Path = Path(Dir_Path).joinpath(File_Name).as_posix()
                        PathList.append(File_Path)

        Writer = get_writer("srt", self.SRT_Dir)

        for Audio_Path in PathList:
            try:
                Writer(
                    transcribe(
                        model = Model,
                        audio = Audio_Path,
                        verbose = self.Verbose,
                        temperature = Temperature,
                        compression_ratio_threshold = self.Compression_Ratio_Threshold,
                        logprob_threshold = self.Logprob_Threshold,
                        no_speech_threshold = self.No_Speech_Threshold,
                        condition_on_previous_text = self.Condition_on_Previous_Text,
                        initial_prompt = self.Initial_Prompt,
                        #decode_options = {"language": self.Language}
                    ),
                    Audio_Path,
                    self.Add_LanguageInfo
                )
            except: # To avoid encountering the ValueError (https://github.com/openai/whisper/discussions/1068)
                Writer(
                    transcribe(
                        model = Model,
                        audio = Audio_Path,
                        verbose = self.Verbose,
                        temperature = [self.Temperature], # This means setting 'Temperature_Increment_on_Fallback' to None
                        compression_ratio_threshold = self.Compression_Ratio_Threshold,
                        logprob_threshold = self.Logprob_Threshold,
                        no_speech_threshold = self.No_Speech_Threshold,
                        condition_on_previous_text = self.Condition_on_Previous_Text,
                        initial_prompt = self.Initial_Prompt,
                        #decode_options = {"language": self.Language}
                    ),
                    Audio_Path,
                    self.Add_LanguageInfo
                )