import os
import PyEasyUtils as EasyUtils
from typing import Union, Optional

##############################################################################################################################

logPath = None


def logPath_set(setlogPath: str):
    global logPath
    logPath = setlogPath

##############################################################################################################################

def mkPyCommand(fileDir, *commands):
    return [
        'cd "%s"' % fileDir,
        'python -c "%s"' % ';'.join(EasyUtils.toIterable(commands))
    ]

##############################################################################################################################

class AudioProcessor:
    def __init__(self, toolDir):
        self.toolDir = toolDir

    def processAudio(self,
        **kwargs
    ):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.toolDir,
                'from AudioProcessor.process import Audio_Processing',
                f'AudioConvertandSlice = Audio_Processing({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
                'AudioConvertandSlice.processAudio()',
            ),
            env = os.environ
        )
        output, error, returnCode = self.spm.result(decodeResult = True, logPath = logPath)

    def terminate(self):
        for subprocess in self.spm.subprocesses:
            subprocess.terminate()


class VPR:
    def __init__(self, toolDir):
        self.toolDir = toolDir

    def infer(self,
        **kwargs
    ):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.toolDir,
                'from VPR.infer import Voice_Contrasting',
                f'AudioContrastInference = Voice_Contrasting({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
                'AudioContrastInference.getModel()',
                'AudioContrastInference.inference()',
            ),
            env = os.environ
        )
        output, error, returnCode = self.spm.result(decodeResult = True, logPath = logPath)

    def terminate(self):
        for subprocess in self.spm.subprocesses:
            subprocess.terminate()


class Whisper:
    def __init__(self, toolDir):
        self.toolDir = toolDir

    def infer(self,
        **kwargs
    ):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.toolDir,
                'from Whisper.transcribe import Voice_Transcribing',
                f'WAVtoSRT = Voice_Transcribing({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
                'WAVtoSRT.transcribe()',
            ),
            env = os.environ
        )
        output, error, returnCode = self.spm.result(decodeResult = True, logPath = logPath)

    def terminate(self):
        for subprocess in self.spm.subprocesses:
            subprocess.terminate()


class GPT_SoVITS:
    def __init__(self, toolDir):
        self.toolDir = toolDir

    def preprocess(self,
        **kwargs
    ):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.toolDir,
                'from GPT_SoVITS.preprocess import Dataset_Creating',
                f'SRTtoCSVandSplitAudio = Dataset_Creating({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
                'SRTtoCSVandSplitAudio.run()',
            ),
            env = os.environ
        )
        output, error, returnCode = self.spm.result(decodeResult = True, logPath = logPath)

    def train(self,
        **kwargs
    ):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.toolDir,
                'from GPT_SoVITS.train import train',
                f'train({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
            ),
            env = os.environ
        )
        output, error, returnCode = self.spm.result(decodeResult = True, logPath = logPath)

    def infer_webui(self,
        **kwargs
    ):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.toolDir,
                'from GPT_SoVITS.infer_webui import infer',
                f'infer({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
            ),
            env = os.environ
        )
        output, error, returnCode = self.spm.result(decodeResult = True, logPath = logPath)

    def terminate(self):
        for subprocess in self.spm.subprocesses:
            subprocess.terminate()

##############################################################################################################################