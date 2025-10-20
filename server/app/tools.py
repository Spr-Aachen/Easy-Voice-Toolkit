import os, sys
import PyEasyUtils as EasyUtils
from pathlib import Path

##############################################################################################################################

currentDir = Path(sys.argv[0]).parent.as_posix()

toolDir = Path(currentDir).joinpath("modules").as_posix()


def mkPyCommand(fileDir, *commands):
    return [
        'cd "%s"' % fileDir,
        'python -c "%s"' % ';'.join(EasyUtils.toIterable(commands))
    ]

##############################################################################################################################

class AudioProcessor:
    def __init__(self):
        self.spm_processAudio = None

    async def processAudio(self,
        **kwargs
    ):
        self.spm_processAudio = EasyUtils.asyncSubprocessManager(shell = True)
        await self.spm_processAudio.create(
            args = mkPyCommand(
                toolDir,
                'from AudioProcessor.process import Audio_Processing',
                f'AudioConvertandSlice = Audio_Processing({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
                'AudioConvertandSlice.processAudio()',
            ),
            env = os.environ
        )
        subprocessMonitor = self.spm_processAudio.monitor()
        async for outputLine, errorLine in subprocessMonitor:
            yield outputLine

    def terminate_processAudio(self):
        for subprocess in self.spm_processAudio.subprocesses:
            EasyUtils.terminateProcess(subprocess.pid)


class VPR:
    def __init__(self):
        self.spm_processAudio = None

    async def infer(self,
        **kwargs
    ):
        self.spm_infer = EasyUtils.asyncSubprocessManager(shell = True)
        await self.spm_infer.create(
            args = mkPyCommand(
                toolDir,
                'from VPR.infer import Voice_Contrasting',
                f'AudioContrastInference = Voice_Contrasting({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
                'AudioContrastInference.getModel()',
                'AudioContrastInference.inference()',
            ),
            env = os.environ
        )
        subprocessMonitor = self.spm_infer.monitor()
        async for outputLine, errorLine in subprocessMonitor:
            yield outputLine

    def terminate_infer(self):
        for subprocess in self.spm_infer.subprocesses:
            EasyUtils.terminateProcess(subprocess.pid)


class Whisper:
    def __init__(self):
        self.spm_processAudio = None

    async def infer(self,
        **kwargs
    ):
        self.spm_infer = EasyUtils.asyncSubprocessManager(shell = True)
        await self.spm_infer.create(
            args = mkPyCommand(
                toolDir,
                'from Whisper.transcribe import Voice_Transcribing',
                f'WAVtoSRT = Voice_Transcribing({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
                'WAVtoSRT.transcribe()',
            ),
            env = os.environ
        )
        subprocessMonitor = self.spm_infer.monitor()
        async for outputLine, errorLine in subprocessMonitor:
            yield outputLine

    def terminate_infer(self):
        for subprocess in self.spm_infer.subprocesses:
            EasyUtils.terminateProcess(subprocess.pid)


class GPT_SoVITS:
    def __init__(self):
        self.spm_processAudio = None

    async def preprocess(self,
        **kwargs
    ):
        self.spm_preprocess = EasyUtils.asyncSubprocessManager(shell = True)
        await self.spm_preprocess.create(
            args = mkPyCommand(
                toolDir,
                'from GPT_SoVITS.preprocess import Dataset_Creating',
                f'SRTtoCSVandSplitAudio = Dataset_Creating({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
                'SRTtoCSVandSplitAudio.run()',
            ),
            env = os.environ
        )
        subprocessMonitor = self.spm_preprocess.monitor()
        async for outputLine, errorLine in subprocessMonitor:
            yield outputLine

    def terminate_preprocess(self):
        for subprocess in self.spm_preprocess.subprocesses:
            EasyUtils.terminateProcess(subprocess.pid)

    async def train(self,
        **kwargs
    ):
        self.spm_train = EasyUtils.asyncSubprocessManager(shell = True)
        await self.spm_train.create(
            args = mkPyCommand(
                toolDir,
                'from GPT_SoVITS.train import train',
                f'train({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
            ),
            env = os.environ
        )
        subprocessMonitor = self.spm_train.monitor()
        async for outputLine, errorLine in subprocessMonitor:
            yield outputLine

    def terminate_train(self):
        for subprocess in self.spm_train.subprocesses:
            EasyUtils.terminateProcess(subprocess.pid)

    async def infer_webui(self,
        **kwargs
    ):
        self.spm_infer_webui = EasyUtils.asyncSubprocessManager(shell = True)
        await self.spm_infer_webui.create(
            args = mkPyCommand(
                toolDir,
                'from GPT_SoVITS.infer_webui import infer',
                f'infer({",".join(f"{k}={v!r}" for k, v in kwargs.items())})',
            ),
            env = os.environ
        )
        subprocessMonitor = self.spm_infer_webui.monitor()
        async for outputLine, errorLine in subprocessMonitor:
            yield outputLine

    def terminate_infer_webui(self):
        for subprocess in self.spm_infer_webui.subprocesses:
            EasyUtils.terminateProcess(subprocess.pid)

##############################################################################################################################