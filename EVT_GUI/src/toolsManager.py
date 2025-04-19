import os
import sys
import shutil
import json
import PyEasyUtils as EasyUtils
from glob import glob
from pathlib import Path
from typing import Optional
from PySide6.QtCore import QObject, Signal

##############################################################################################################################

# Tools: AudioProcessor
class Execute_Audio_Processing(QObject):
    '''
    Change media format to WAV (and denoise) and cut off the silent parts
    '''
    def __init__(self, coreDir, logPath):
        super().__init__()

        self.coreDir = coreDir
        self.logPath = logPath

    def execute(self, *params):
        CMD = EasyUtils.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{self.coreDir}"',
                'python -c "'
                'from AudioProcessor.process import Audio_Processing; '
                f"AudioConvertandSlice = Audio_Processing{str(params)}; "
                'AudioConvertandSlice.processAudio()"'
            ]
        )
        Output, error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        EasyUtils.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceIdentifier
class Execute_Voice_Identifying_VPR(QObject):
    '''
    Contrast the voice and filter out the similar ones
    '''
    def __init__(self, coreDir, logPath):
        super().__init__()

        self.coreDir = coreDir
        self.logPath = logPath

    def execute(self, *params):
        CMD = EasyUtils.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{self.coreDir}"',
                'python -c "'
                'from VPR.identify import Voice_Identifying; '
                f"AudioContrastInference = Voice_Identifying{str(params)}; "
                'AudioContrastInference.getModel(); '
                'AudioContrastInference.inference()"'
            ]
        )
        Output, error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        EasyUtils.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceTranscriber
class Execute_Voice_Transcribing_Whisper(QObject):
    '''
    Transcribe WAV content to SRT
    '''
    def __init__(self, coreDir, logPath):
        super().__init__()

        self.coreDir = coreDir
        self.logPath = logPath

    def execute(self, *params):
        LANGUAGES = {
            "中":       "zh",
            "Chinese":  "zh",
            "英":       "en",
            "English":  "en",
            "日":       "ja",
            "japanese": "ja"
        }
        CMD = EasyUtils.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{self.coreDir}"',
                'python -c "'
                'from Whisper.transcribe import Voice_Transcribing; '
                f"WAVtoSRT = Voice_Transcribing{str(EasyUtils.itemReplacer(LANGUAGES, params))}; "
                'WAVtoSRT.transcriber()"'
            ]
        )
        Output, error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        EasyUtils.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: DatasetCreator
class Execute_Dataset_Creating_GPTSoVITS(QObject):
    '''
    Convert the whisper-generated SRT to CSV and split the WAV
    '''
    def __init__(self, coreDir, logPath):
        super().__init__()

        self.coreDir = coreDir
        self.logPath = logPath

    def execute(self, *params):
        CMD = EasyUtils.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{self.coreDir}"',
                'python -c "'
                'from GPT_SoVITS.create import Dataset_Creating; '
                f"SRTtoCSVandSplitAudio = Dataset_Creating{str(params)}; "
                'SRTtoCSVandSplitAudio.run()"'
            ]
        )
        Output, error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        EasyUtils.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


class Execute_Dataset_Creating_VITS(QObject):
    '''
    Convert the whisper-generated SRT to CSV and split the WAV
    '''
    def __init__(self, coreDir, logPath):
        super().__init__()

        self.coreDir = coreDir
        self.logPath = logPath

    def execute(self, *params):
        CMD = EasyUtils.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{self.coreDir}"',
                'python -c "'
                'from VITS.create import Dataset_Creating; '
                f"SRTtoCSVandSplitAudio = Dataset_Creating{str(params)}; "
                'SRTtoCSVandSplitAudio.run()"'
            ]
        )
        Output, error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        EasyUtils.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceTrainer
class Execute_Voice_Training_GPTSoVITS(QObject):
    '''
    Preprocess and then start training
    '''
    def __init__(self, coreDir, logPath):
        super().__init__()

        self.coreDir = coreDir
        self.logPath = logPath

    def execute(self, *params):
        CMD = EasyUtils.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{self.coreDir}"',
                'python -c "'
                'from GPT_SoVITS.train import train; '
                f'train{str(params)}"'
            ]
        )
        Output, error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        EasyUtils.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


class Execute_Voice_Training_VITS(QObject):
    '''
    Preprocess and then start training
    '''
    def __init__(self, coreDir, logPath):
        super().__init__()

        self.coreDir = coreDir
        self.logPath = logPath

    def execute(self, *params):
        CMD = EasyUtils.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{self.coreDir}"',
                'python -c "'
                'from VITS.train import train; '
                f'train{str(params)}"'
            ]
        )
        Output, error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        EasyUtils.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceConverter
class Execute_Voice_Converting_GPTSoVITS(QObject):
    '''
    Inference model
    '''
    def __init__(self, coreDir, logPath):
        super().__init__()

        self.coreDir = coreDir
        self.logPath = logPath

    def execute(self, *params):
        CMD = EasyUtils.subprocessManager(communicateThroughConsole = True)
        self.process = CMD.create(
            args = [
                f'cd "{self.coreDir}"',
                'python -c "'
                'from GPT_SoVITS.convert_webui import convert; '
                f'convert{str(params)}"'
            ]
        )
        output, error = CMD.monitor(
            showProgress = True,
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
        EasyUtils.processTerminator(self.process.pid) if hasattr(self, 'process') else None


def Get_Speakers(Config_Path_Load):
    try:
        with open(Config_Path_Load, 'r', encoding = 'utf-8') as File:
            params = json.load(File)
        Speakers = params["speakers"]
        return Speakers
    except:
        return str()

class Execute_Voice_Converting_VITS(QObject):
    '''
    Inference model
    '''
    def __init__(self, coreDir, logPath):
        super().__init__()

        self.coreDir = coreDir
        self.logPath = logPath

    def execute(self, *params):
        LANGUAGES = {
            "中":       "ZH",
            "Chinese":  "ZH",
            "英":       "EN",
            "English":  "EN",
            "日":       "JA",
            "Japanese": "JA"
        }
        CMD = EasyUtils.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{self.coreDir}"',
                'python -c "'
                'from VITS.convert import convert; '
                f'convert{str(EasyUtils.itemReplacer(LANGUAGES, params))}"'
            ]
        )
        Output, error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = self.logPath
        )[:2]
        if 'error' in str(error).lower():
            error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            return
        raise Exception(error)

    def terminate(self):
        EasyUtils.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None

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