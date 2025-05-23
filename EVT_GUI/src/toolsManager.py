import os
import sys
import shutil
import json
import PyEasyUtils as EasyUtils
from glob import glob
from pathlib import Path
from typing import Union, Optional
from PySide6.QtCore import QObject, Signal

##############################################################################################################################

def mkPyCommand(fileDir, *commands):
    return [
        'cd "%s"' % fileDir,
        'python -c "%s"' % ';'.join(EasyUtils.toIterable(commands))
    ]

##############################################################################################################################

class Tool_AudioProcessor(QObject):
    '''
    Start audio processing
    '''
    def __init__(self, fileDir, logPath):
        super().__init__()

        self.fileDir = fileDir
        self.logPath = logPath

    def processAudio(self, *params):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.fileDir,
                'from AudioProcessor.process import Audio_Processing',
                f'AudioConvertandSlice = Audio_Processing{str(params)}',
                'AudioConvertandSlice.processAudio()',
            )
        )
        output, error = self.spm.result(
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        if not hasattr(self, 'spm'):
            return
        for subprocess in self.spm.subprocesses:
            EasyUtils.terminateProcess(subprocess.pid)


class Tool_VPR(QObject):
    '''
    Start VPR inferencing
    '''
    def __init__(self, fileDir, logPath):
        super().__init__()

        self.fileDir = fileDir
        self.logPath = logPath

    def infer(self, *params):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.fileDir,
                'from VPR.infer import Voice_Contrasting',
                f'AudioContrastInference = Voice_Contrasting{str(params)}',
                'AudioContrastInference.getModel()',
                'AudioContrastInference.inference()',
            )
        )
        output, error = self.spm.result(
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        if not hasattr(self, 'spm'):
            return
        for subprocess in self.spm.subprocesses:
            EasyUtils.terminateProcess(subprocess.pid)


class Tool_Whisper(QObject):
    '''
    Start Whisper transcribing
    '''
    def __init__(self, fileDir, logPath):
        super().__init__()

        self.fileDir = fileDir
        self.logPath = logPath

    def infer(self, *params):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.fileDir,
                'from Whisper.transcribe import Voice_Transcribing',
                f'WAVtoSRT = Voice_Transcribing{str(params)}',
                'WAVtoSRT.transcribe()',
            )
        )
        output, error = self.spm.result(
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        if not hasattr(self, 'spm'):
            return
        for subprocess in self.spm.subprocesses:
            EasyUtils.terminateProcess(subprocess.pid)


class Tool_GPTSoVITS(QObject):
    '''
    Start GPTSoVITS preprocessing
    '''
    def __init__(self, fileDir, logPath):
        super().__init__()

        self.fileDir = fileDir
        self.logPath = logPath

    def preprocess(self, *params):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.fileDir,
                'from GPT_SoVITS.preprocess import Dataset_Creating',
                f'SRTtoCSVandSplitAudio = Dataset_Creating{str(params)}',
                'SRTtoCSVandSplitAudio.run()',
            )
        )
        output, error = self.spm.result(
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def train(self, *params):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.fileDir,
                'from GPT_SoVITS.train import train',
                f'train{str(params)}',
            )
        )
        output, error = self.spm.result(
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def infer(self, *params):
        self.spm = EasyUtils.subprocessManager(shell = True)
        self.spm.create(
            args = mkPyCommand(
                self.fileDir,
                'from GPT_SoVITS.infer_webui import infer',
                f'infer{str(params)}',
            )
        )
        output, error = self.spm.result(
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        if not hasattr(self, 'spm'):
            return
        for subprocess in self.spm.subprocesses:
            EasyUtils.terminateProcess(subprocess.pid)

##############################################################################################################################

def VPRResult_Get(audioSpeakersData_path: str):
    """
    GetVPRResult
    """
    AudioSpeakerSimList = []
    with open(audioSpeakersData_path, mode = 'r', encoding = 'utf-8') as AudioSpeakersData:
        AudioSpeakerSimLines = AudioSpeakersData.readlines()
    for AudioSpeakerSimLine in AudioSpeakerSimLines:
        AudioSpeakerSim = AudioSpeakerSimLine.strip().split('|')
        if len(AudioSpeakerSim) == 2:
            AudioSpeakerSim.append('')
        AudioSpeakerSimList.append(AudioSpeakerSim)
    return AudioSpeakerSimList


def VPRResult_Save(audioSpeakers: dict, audioSpeakersData_path: str, moveAudio: bool, moveToDst: Optional[str] = None):
    """
    SaveVPRResult
    """
    with open(audioSpeakersData_path, mode = 'w', encoding = 'utf-8') as AudioSpeakersData:
        Lines = []
        for Audio, Speaker in audioSpeakers.items():
            Speaker = Speaker.strip()
            if Speaker == '':
                continue
            if moveAudio:
                if moveToDst is None:
                    raise Exception("Destination shouldn't be 'None'")
                MoveToDst_Sub = EasyUtils.normPath(Path(moveToDst).joinpath(Speaker))
                os.makedirs(MoveToDst_Sub, exist_ok = True) if Path(MoveToDst_Sub).exists() == False else None
                Audio_Dst = EasyUtils.normPath(Path(MoveToDst_Sub).joinpath(Path(Audio).name).as_posix())
                shutil.copy(Audio, MoveToDst_Sub) if not Path(Audio_Dst).exists() else None
                Lines.append(f"{Audio_Dst}|{Speaker}\n")
            else:
                Lines.append(f"{Audio}|{Speaker}\n")
        AudioSpeakersData.writelines(Lines)


def ASRResult_Get(srtDir: str, audioDir: str):
    """
    GetASRResult
    """
    asrResult = {}
    for SRTFile in glob(EasyUtils.normPath(Path(srtDir).joinpath('*.srt'))):
        AudioFiles = glob(EasyUtils.normPath(Path(audioDir).joinpath('**', f'{Path(SRTFile).stem}.*')), recursive = True)
        if len(AudioFiles) == 0:
            continue
        with open(SRTFile, mode = 'r', encoding = 'utf-8') as SRT:
            SRTContent = SRT.read()
        asrResult[AudioFiles[0]] = SRTContent
    return asrResult


def ASRResult_Save(asrResult: dict, srtDir: str):
    """
    SaveASRResult
    """
    for AudioFile in asrResult.keys():
        SRTFiles = glob(EasyUtils.normPath(Path(srtDir).joinpath(f'{Path(AudioFile).stem}.*')))
        if len(SRTFiles) == 0:
            continue
        with open(SRTFiles[0], mode = 'w', encoding = 'utf-8') as SRT:
            SRT.write(asrResult[AudioFile])


def DATResult_Get(datPath: str):
    """
    GetDATResult
    """
    datResult = {}
    with open(datPath, mode = 'r', encoding = 'utf-8') as DAT:
        DATLines = DAT.readlines()
    for DATLine in DATLines:
        Audio = EasyUtils.normPath(Path(datPath).parent.joinpath(DATLine.split('|')[0]))
        datResult[Audio] = DATLine.strip()
    return datResult


def DATResult_Save(datResult: list, datPath: str):
    """
    SaveDATResult
    """
    with open(datPath, mode = 'w', encoding = 'utf-8') as DAT:
        DATLines = '\n'.join(datResult)
        DAT.write(DATLines)

##############################################################################################################################