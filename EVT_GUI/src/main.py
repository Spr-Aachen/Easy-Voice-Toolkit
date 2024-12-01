import os
import sys
import time
import json
import hashlib
import argparse
import subprocess
from pathlib import Path
from glob import glob
from datetime import date, datetime
from concurrent.futures import ThreadPoolExecutor
from PySide6 import __file__ as PySide6_File
from PySide6.QtCore import Qt, QObject, Signal, Slot, QThread
from PySide6.QtCore import QCoreApplication as QCA
from PySide6.QtGui import QColor, QPixmap, QIcon, QTextCursor
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets import QTasks
from QEasyWidgets import ComponentsSignals, Theme, EasyTheme, Language, EasyLanguage, IconBase
from QEasyWidgets.Windows import MessageBoxBase

from windows.windows import *
from functions import *
from envConfigurator import *
from config import *

##############################################################################################################################

# Change working directory to current directory
os.chdir(currentDir)


# Parse path settings
parser = argparse.ArgumentParser()
parser.add_argument("--updater",      help = "path to updater",          default = Path(currentDir).joinpath('Updater.py' if isFileCompiled == False else 'Updater.exe'))
parser.add_argument("--core",         help = "dir of core files",        default = Path(resourceDir).joinpath('EVT_Core'))
parser.add_argument("--manifest",     help = "path to manifest.json",    default = Path(resourceDir).joinpath('manifest.json'))
parser.add_argument("--requirements", help = "path to requirements.txt", default = Path(resourceDir).joinpath('requirements.txt'))
parser.add_argument("--dependencies", help = "dir of dependencies",      default = Path(currentDir).joinpath(''))
parser.add_argument("--models",       help = "dir of models",            default = Path(currentDir).joinpath('Models'))
parser.add_argument("--output",       help = "dir of output",            default = Path(currentDir).joinpath(''))
parser.add_argument("--profile",      help = "dir of profile",           default = Path(currentDir).joinpath(''))
args = parser.parse_args()

UpdaterPath = args.updater
CoreDir = args.core
ManifestPath = args.manifest
RequirementsPath = args.requirements
DependencyDir = args.dependencies
ModelDir = args.models
OutputDir = args.output
ProfileDir = args.profile


# Set up client config
configDir = QFunc.normPath(Path(ProfileDir).joinpath('config'))
configPath = QFunc.normPath(Path(configDir).joinpath('config.ini'))
config = QFunc.configManager(configPath)
config.editConfig('Info', 'currentVersion', str(currentVersion))
config.editConfig('Info', 'executerName', str(QFunc.getFileInfo()[0]))


# Set up environment variables while python file is not compiled
if isFileCompiled == False:
    QFunc.setEnvVar( # Redirect PATH variable 'QT_QPA_PLATFORM_PLUGIN_PATH' to Pyside6 '/plugins/platforms' folder's path
        variable = 'QT_QPA_PLATFORM_PLUGIN_PATH',
        value = QFunc.normPath(Path(QFunc.getBaseDir(PySide6_File)).joinpath('plugins', 'platforms'))
    )
# Set up environment variables while environment is configured
if Path(DependencyDir).joinpath('Aria2').exists():
    QFunc.setEnvVar(
        variable = 'PATH',
        value = QFunc.normPath(Path(DependencyDir).joinpath('Aria2'))
    )
if Path(DependencyDir).joinpath('FFmpeg').exists():
    QFunc.setEnvVar(
        variable = 'PATH',
        value = QFunc.normPath(Path(DependencyDir).joinpath('FFmpeg', 'bin'))
    )
if Path(DependencyDir).joinpath('Python').exists():
    QFunc.setEnvVar(
        variable = 'PATH',
        value = QFunc.normPath(Path(DependencyDir).joinpath('Python'), trailingSlash = True)
    )
    QFunc.setEnvVar(
        variable = 'PATH',
        value = QFunc.normPath(Path(DependencyDir).joinpath('Python', 'Scripts'), trailingSlash = True)
    )

##############################################################################################################################

class Execute_Update_Checking(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    def Execute(self):
        Function_UpdateChecker(
            repoOwner = repoOwner,
            repoName = repoName,
            fileName = fileName,
            fileFormat = fileFormat,
            currentVersion = currentVersion
        )

        self.finished.emit()

##############################################################################################################################

# Tools: AudioProcessor
class Execute_Audio_Processing(QObject):
    '''
    Change media format to WAV (and denoise) and cut off the silent parts
    '''
    started = Signal()
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, params: tuple):
        self.started.emit()

        CMD = QFunc.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from AudioProcessor.Process import Audio_Processing; '
                f"AudioConvertandSlice = Audio_Processing{str(params)}; "
                'AudioConvertandSlice.Process_Audio()"'
            ]
        )
        Output, Error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = logPath
        )[:2]
        if 'error' in str(Error).lower():
            Error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            Error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            Error = None
        self.errChk.emit(str(Error))

        self.finished.emit()

    def Terminate(self):
        QFunc.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceIdentifier
class Execute_Voice_Identifying_VPR(QObject):
    '''
    Contrast the voice and filter out the similar ones
    '''
    started = Signal()
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, params: tuple):
        self.started.emit()

        CMD = QFunc.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from VPR.Identify import Voice_Identifying; '
                f"AudioContrastInference = Voice_Identifying{str(params)}; "
                'AudioContrastInference.GetModel(); '
                'AudioContrastInference.Inference()"'
            ]
        )
        Output, Error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = logPath
        )[:2]
        if 'error' in str(Error).lower():
            Error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            Error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            Error = None
        self.errChk.emit(str(Error))

        self.finished.emit()

    def Terminate(self):
        QFunc.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceTranscriber
class Execute_Voice_Transcribing_Whisper(QObject):
    '''
    Transcribe WAV content to SRT
    '''
    started = Signal()
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, params: tuple):
        self.started.emit()

        LANGUAGES = {
            "中":       "zh",
            "Chinese":  "zh",
            "英":       "en",
            "English":  "en",
            "日":       "ja",
            "japanese": "ja"
        }
        CMD = QFunc.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from Whisper.Transcribe import Voice_Transcribing; '
                f"WAVtoSRT = Voice_Transcribing{str(QFunc.itemReplacer(LANGUAGES, params))}; "
                'WAVtoSRT.Transcriber()"'
            ]
        )
        Output, Error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = logPath
        )[:2]
        if 'error' in str(Error).lower():
            Error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            Error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            Error = None
        self.errChk.emit(str(Error))

        self.finished.emit()

    def Terminate(self):
        QFunc.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: DatasetCreator
class Execute_Dataset_Creating_GPTSoVITS(QObject):
    '''
    Convert the whisper-generated SRT to CSV and split the WAV
    '''
    started = Signal()
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, params: tuple):
        self.started.emit()

        CMD = QFunc.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from GPT_SoVITS.Create import Dataset_Creating; '
                f"SRTtoCSVandSplitAudio = Dataset_Creating{str(params)}; "
                'SRTtoCSVandSplitAudio.CallingFunctions()"'
            ]
        )
        Output, Error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = logPath
        )[:2]
        if 'error' in str(Error).lower():
            Error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            Error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            Error = None
        self.errChk.emit(str(Error))

        self.finished.emit()

    def Terminate(self):
        QFunc.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


class Execute_Dataset_Creating_VITS(QObject):
    '''
    Convert the whisper-generated SRT to CSV and split the WAV
    '''
    started = Signal()
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, params: tuple):
        self.started.emit()

        CMD = QFunc.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from VITS.Create import Dataset_Creating; '
                f"SRTtoCSVandSplitAudio = Dataset_Creating{str(params)}; "
                'SRTtoCSVandSplitAudio.CallingFunctions()"'
            ]
        )
        Output, Error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = logPath
        )[:2]
        if 'error' in str(Error).lower():
            Error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            Error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            Error = None
        self.errChk.emit(str(Error))

        self.finished.emit()

    def Terminate(self):
        QFunc.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceTrainer
class Execute_Voice_Training_GPTSoVITS(QObject):
    '''
    Preprocess and then start training
    '''
    started = Signal()
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, params: tuple):
        self.started.emit()

        CMD = QFunc.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from GPT_SoVITS.Train import Train; '
                f'Train{str(params)}"'
            ]
        )
        Output, Error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = logPath
        )[:2]
        if 'error' in str(Error).lower():
            Error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            Error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            Error = None
        self.errChk.emit(str(Error))

        self.finished.emit()

    def Terminate(self):
        QFunc.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


class Execute_Voice_Training_VITS(QObject):
    '''
    Preprocess and then start training
    '''
    started = Signal()
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, params: tuple):
        self.started.emit()

        CMD = QFunc.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from VITS.Train import Train; '
                f'Train{str(params)}"'
            ]
        )
        Output, Error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = logPath
        )[:2]
        if 'error' in str(Error).lower():
            Error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            Error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            Error = None
        self.errChk.emit(str(Error))

        self.finished.emit()

    def Terminate(self):
        QFunc.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceConverter
class Execute_Voice_Converting_GPTSoVITS(QObject):
    '''
    Inference model
    '''
    started = Signal()
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, params: tuple):
        self.started.emit()

        CMD = QFunc.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from GPT_SoVITS.Convert import Convert; '
                f'Convert{str(params)}"'
            ]
        )
        Output, Error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = logPath
        )[:2]
        if 'error' in str(Error).lower():
            Error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            Error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            Error = None
        self.errChk.emit(str(Error))

        self.finished.emit()

    def Terminate(self):
        QFunc.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


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
    started = Signal()
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, params: tuple):
        self.started.emit()

        LANGUAGES = {
            "中":       "ZH",
            "Chinese":  "ZH",
            "英":       "EN",
            "English":  "EN",
            "日":       "JA",
            "Japanese": "JA"
        }
        CMD = QFunc.subprocessManager(communicateThroughConsole = True)
        self.Process = CMD.create(
            args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from VITS.Convert import Convert; '
                f'Convert{str(QFunc.itemReplacer(LANGUAGES, params))}"'
            ]
        )
        Output, Error = CMD.monitor(
            showProgress = True,
            decodeResult = True,
            logPath = logPath
        )[:2]
        if 'error' in str(Error).lower():
            Error += "（详情请见终端输出信息）"
        elif 'traceback' in str(Output).lower():
            Error = "执行完成，但疑似中途出错\n（详情请见终端输出信息）"
        else:
            Error = None
        self.errChk.emit(str(Error))

        self.finished.emit()

    def Terminate(self):
        QFunc.processTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# ClientFunc: GetModelsInfo
class CustomSignals_ModelView(QObject):
    '''
    Set up signals for model view
    '''
    Signal_Process_UVR = Signal(list)

    Signal_VPR_TDNN = Signal(list)

    Signal_ASR_Whisper = Signal(list)

    Signal_TTS_GPTSoVITS = Signal(list)

    Signal_TTS_VITS = Signal(list)

ModelViewSignals = CustomSignals_ModelView()

class Model_View(QObject):
    '''
    View model
    '''
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    def GetModelsInfo(self, ModelsDir: str, ModelsFormats: list):
        ModelsInfo = {}
        os.makedirs(ModelsDir, exist_ok = True)

        ModelDicts_Cloud = []
        Tags = [Path(ModelsDir).parts[-2], Path(ModelsDir).parts[-1]]
        if not Path(ManifestPath).exists():
            return []
        with open(QFunc.normPath(ManifestPath), 'r', encoding = 'utf-8') as File:
            param = json.load(File)
        for ModelDict in param["models"]:
            if ModelDict["tags"] == Tags:
                ModelDicts_Cloud.append(ModelDict)
        def GetModelInfo_Cloud(ModelDict):
            if isinstance(ModelDict["SHA"], dict):
                Name = ModelDict["name"]
                for Model, ModelSHA in ModelDict["SHA"].items():
                    ModelName = Model
                    ModelName, ModelType = ModelName.rsplit('.', 1)
                    ModelSize = ModelDict["size"][Model]
                    ModelDate = ModelDict["date"][Model]
                    ModelSHA = ModelSHA
                    ModelURL = ModelDict["downloadurl"][Model]
                    ModelDir = Path(ModelsDir).joinpath("Downloaded", Name)
                    DownloadParam = (ModelURL, ModelDir, ModelName, Path(ModelURL).suffix, ModelSHA)
                    ModelsInfo[ModelSHA] = [str(f"[{Name}]{ModelName}"), str(ModelType), str(ModelSize), str(ModelDate), tuple(DownloadParam)]
            else:
                ModelName = ModelDict["name"]
                ModelName, ModelType = ModelName.rsplit('.', 1)
                ModelSize = ModelDict["size"]
                ModelDate = ModelDict["date"]
                ModelSHA = ModelDict["SHA"]
                ModelURL = ModelDict["downloadurl"]
                ModelDir = Path(ModelsDir).joinpath("Downloaded")
                DownloadParam = (ModelURL, ModelDir, ModelName, Path(ModelURL).suffix, ModelSHA)
                ModelsInfo[ModelSHA] = [str(ModelName), str(ModelType), str(ModelSize), str(ModelDate), tuple(DownloadParam)]
        with ThreadPoolExecutor(max_workers = os.cpu_count()) as Executor:
            Executor.map(
                GetModelInfo_Cloud,
                ModelDicts_Cloud
            ) if ModelDicts_Cloud is not None else None

        ModelPaths_Local = []
        for ModelsFormat in ModelsFormats:
            ModelPaths_Local_Sep = QFunc.toIterable(QFunc.getPaths(ModelsDir, ModelsFormat))
            ModelPaths_Local_Sep = [ModelPath_Local_Sep for ModelPath_Local_Sep in ModelPaths_Local_Sep if ModelPath_Local_Sep is not None and ModelPath_Local_Sep.endswith(ModelsFormat)]
            ModelPaths_Local.extend(ModelPaths_Local_Sep) if ModelPaths_Local_Sep is not None else None
        ModelPaths_Local = list(set(ModelPaths_Local))
        def GetModelInfo_Local(ModelPath):
            Name = Path(ModelPath).parts[-2] if Path(ModelPath).parent.__str__() not in Path(ModelsDir).joinpath("Downloaded").__str__() else None
            ModelName = Path(ModelPath).name
            ModelName, ModelType = ModelName.rsplit('.', 1)
            ModelSize = round(Path(ModelPath).stat().st_size / (1024 ** 2), 1)
            ModelDate = datetime.fromtimestamp(Path(ModelPath).stat().st_mtime)
            with open(ModelPath, "rb") as m:
                ModelBytes = m.read()
            ModelSHA = hashlib.sha256(ModelBytes).hexdigest()
            ModelDir = Path(ModelPath).parent
            ModelsInfo[ModelSHA] = [str(f"[{Name}]{ModelName}" if Name is not None else ModelName), str(ModelType), str(ModelSize)+'MB', str(ModelDate), str(ModelDir)]
        with ThreadPoolExecutor(max_workers = os.cpu_count()) as Executor:
            Executor.map(
                GetModelInfo_Local,
                ModelPaths_Local
            ) if ModelPaths_Local is not None else None

        return list(ModelsInfo.values())

    @Slot()
    def Execute(self):
        ModelViewSignals.Signal_Process_UVR.emit(
            self.GetModelsInfo(
                QFunc.normPath(Path(ModelDir).joinpath('Process', 'UVR')),
                ['pth', 'onnx']
            )
        )
        ModelViewSignals.Signal_VPR_TDNN.emit(
            self.GetModelsInfo(
                QFunc.normPath(Path(ModelDir).joinpath('VPR', 'TDNN')),
                ['pth']
            )
        )
        ModelViewSignals.Signal_ASR_Whisper.emit(
            self.GetModelsInfo(
                QFunc.normPath(Path(ModelDir).joinpath('ASR', 'Whisper')),
                ['pt']
            )
        )
        ModelViewSignals.Signal_TTS_GPTSoVITS.emit(
            self.GetModelsInfo(
                QFunc.normPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS')),
                ['pth', 'ckpt', 'bin', 'json']
            )
        )
        ModelViewSignals.Signal_TTS_VITS.emit(
            self.GetModelsInfo(
                QFunc.normPath(Path(ModelDir).joinpath('TTS', 'VITS')),
                ['pth', 'json']
            )
        )
        self.finished.emit()


# ClientFunc: ModelDownloader
class Model_Downloader(QObject):
    '''
    Download model
    '''
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    def DownloadModel(self, DownloadParams: tuple):
        try:
            FilePath = QFunc.downloadFile(*DownloadParams, CreateNewConsole = True)[1]
            FileSuffix = Path(FilePath).suffix
            shutil.unpack_archive(FilePath, DownloadParams[1], FileSuffix) if FileSuffix in ('zip', 'tar', 'gztar', 'bztar') else None
            return None
        except Exception as e:
            return e

    @Slot(tuple)
    def Execute(self, params: tuple):
        Error = self.DownloadModel(params)
        self.errChk.emit(str(Error))

        self.finished.emit()


# ClientFunc: AddLocalModel
def AddLocalModel(ModelPath: str, Sector: list[str] = ['Tool', 'type']):
    MoveToDst = QFunc.normPath(Path(ModelDir).joinpath(*Sector))
    shutil.move(ModelPath, MoveToDst)


# ClientFunc: GetVPRResult
def VPRResult_Get(AudioSpeakersData_Path: str):
    AudioSpeakerSimList = []
    with open(AudioSpeakersData_Path, mode = 'r', encoding = 'utf-8') as AudioSpeakersData:
        AudioSpeakerSimLines = AudioSpeakersData.readlines()
    for AudioSpeakerSimLine in AudioSpeakerSimLines:
        AudioSpeakerSim = AudioSpeakerSimLine.strip().split('|')
        if len(AudioSpeakerSim) == 2:
            AudioSpeakerSim.append('')
        AudioSpeakerSimList.append(AudioSpeakerSim)
    return AudioSpeakerSimList


# ClientFunc: SaveVPRResult
def VPRResult_Save(AudioSpeakers: dict, AudioSpeakersData_Path: str, MoveAudio: bool, MoveToDst: Optional[str] = None):
    with open(AudioSpeakersData_Path, mode = 'w', encoding = 'utf-8') as AudioSpeakersData:
        Lines = []
        for Audio, Speaker in AudioSpeakers.items():
            Speaker = Speaker.strip()
            if Speaker == '':
                continue
            if MoveAudio:
                if MoveToDst is None:
                    raise Exception("Destination shouldn't be 'None'")
                MoveToDst_Sub = QFunc.normPath(Path(MoveToDst).joinpath(Speaker))
                os.makedirs(MoveToDst_Sub, exist_ok = True) if Path(MoveToDst_Sub).exists() == False else None
                Audio_Dst = QFunc.normPath(Path(MoveToDst_Sub).joinpath(Path(Audio).name).as_posix())
                shutil.copy(Audio, MoveToDst_Sub) if not Path(Audio_Dst).exists() else None
                Lines.append(f"{Audio_Dst}|{Speaker}\n")
            else:
                Lines.append(f"{Audio}|{Speaker}\n")
        AudioSpeakersData.writelines(Lines)


# ClientFunc: GetASRResult
def ASRResult_Get(SRTDir: str, AudioDir: str):
    ASRResult = {}
    for SRTFile in glob(QFunc.normPath(Path(SRTDir).joinpath('*.srt'))):
        AudioFiles = glob(QFunc.normPath(Path(AudioDir).joinpath('**', f'{Path(SRTFile).stem}.*')), recursive = True)
        if len(AudioFiles) == 0:
            continue
        with open(SRTFile, mode = 'r', encoding = 'utf-8') as SRT:
            SRTContent = SRT.read()
        ASRResult[AudioFiles[0]] = SRTContent
    return ASRResult


# ClientFunc: SaveASRResult
def ASRResult_Save(ASRResult: dict, SRTDir: str):
    for AudioFile in ASRResult.keys():
        SRTFiles = glob(QFunc.normPath(Path(SRTDir).joinpath(f'{Path(AudioFile).stem}.*')))
        if len(SRTFiles) == 0:
            continue
        with open(SRTFiles[0], mode = 'w', encoding = 'utf-8') as SRT:
            SRT.write(ASRResult[AudioFile])


# ClientFunc: GetDATResult
def DATResult_Get(DATPath: str):
    DATResult = {}
    with open(DATPath, mode = 'r', encoding = 'utf-8') as DAT:
        DATLines = DAT.readlines()
    for DATLine in DATLines:
        Audio = QFunc.normPath(Path(DATPath).parent.joinpath(DATLine.split('|')[0]))
        DATResult[Audio] = DATLine.strip()
    return DATResult


# ClientFunc: SaveDATResult
def DATResult_Save(DATResult: list, DATPath: str):
    with open(DATPath, mode = 'w', encoding = 'utf-8') as DAT:
        DATLines = '\n'.join(DATResult)
        DAT.write(DATLines)


# ClientFunc: IntegrityChecker
class Integrity_Checker(QObject):
    '''
    Check File integrity
    '''
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot()
    def Execute(self):
        Error = QFunc.runCMD(
            args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from AudioProcessor.Process import Audio_Processing; '
                'from VPR.Identify import Voice_Identifying; '
                'from Whisper.Transcribe import Voice_Transcribing; '
                'from GPT_SoVITS.Create import Dataset_Creating; '
                'from GPT_SoVITS.Train import Train; '
                'from GPT_SoVITS.Convert import Convert; '
                'from VITS.Create import Dataset_Creating; '
                'from VITS.Train import Train; '
                'from VITS.Convert import Convert"'
            ],
            communicateThroughConsole = True,
            decodeResult = True,
            logPath = logPath
        )[1]
        self.errChk.emit(str(Error))

        self.finished.emit()


# ClientFunc: TensorboardRunner
class Tensorboard_Runner(QObject):
    '''
    Check File integrity
    '''
    finished = Signal()

    errChk = Signal(str)

    def __init__(self):
        super().__init__()

    def RunTensorboard(self, LogDir):
        try:
            Error = None
            InitialWaitTime = 0
            MaximumWaitTime = 30
            while QFunc.getPaths(LogDir, 'events.out.tfevents') == None:
                time.sleep(3)
                InitialWaitTime += 3
                if InitialWaitTime >= MaximumWaitTime:
                    break
            subprocess.Popen(['python', '-m', 'tensorboard.main', '--logdir', LogDir], env = os.environ)
            time.sleep(9)
            QFunc.openURL('http://localhost:6006/')
        except Exception as e:
            Error = e
        finally:
            return Error

    @Slot(tuple)
    def Execute(self, params: tuple):
        Error = self.RunTensorboard(*params)
        self.errChk.emit(str(Error))

        self.finished.emit()

##############################################################################################################################

# Where to store custom signals
class CustomSignals_MainWindow(QObject):
    '''
    Set up signals for MainWindow
    '''
    Signal_MainWindowShown = Signal()

MainWindowSignals = CustomSignals_MainWindow()


# Show GUI
class MainWindow(Window_MainWindow):
    '''
    Show the user interface
    '''
    def __init__(self):
        super().__init__()

        self.MonitorUsage = QTasks.MonitorUsage()
        self.MonitorUsage.start()

    def closeEvent(self, event):
        config.editConfig('Info', 'executerName', '')
        FunctionSignals.Signal_TaskStatus.connect(lambda: QApplication.instance().exit())
        FunctionSignals.Signal_ForceQuit.emit()

    def showGuidance(self, windowTitle: str, Images: list, Texts: list):
        DialogBox = MessageBox_Stacked(self)
        DialogBox.setWindowTitle(windowTitle)
        DialogBox.SetContent(Images, Texts)
        DialogBox.exec()

    def appendModels(self):
        LineEdit_Models_Append = QLineEdit()
        DialogBox_Models_Append = MessageBox_Buttons(self)
        DialogBox_Models_Append.setText(QCA.translate('MainWindow', "请选择添加方式"))
        DialogBox_Models_Append.Button1.setText(QCA.translate('MainWindow', "模型文件目录（多文件）"))
        DialogBox_Models_Append.Button1.clicked.connect(
            lambda: (
                LineEdit_Models_Append.setText(
                    QFunc.getFileDialog(
                        mode = "SelectFolder"
                    )
                ),
                DialogBox_Models_Append.close(),
            )
        )
        DialogBox_Models_Append.Button2.setText(QCA.translate('MainWindow', "模型文件路径（单文件）"))
        DialogBox_Models_Append.Button2.clicked.connect(
            lambda: (
                LineEdit_Models_Append.setText(
                    QFunc.getFileDialog(
                        mode = "SelectFile",
                        fileType = "模型文件 (*.pt *.pth *.ckpt *.bin *.json')"
                    )
                ),
                DialogBox_Models_Append.close(),
            )
        )
        DialogBox_Models_Append.exec()
        ModelPath = LineEdit_Models_Append.text()
        if QFunc.normPath(ModelPath) is None:
            return
        ToolIndexList = ['Process', 'VPR', 'ASR', 'TTS']
        ToolIndex = self.ui.StackedWidget_Pages_Models.currentIndex()
        TabWidget = QFunc.findChildUI(self.ui.StackedWidget_Pages_Models.currentWidget(), QTabWidget)
        TypeIndex = TabWidget.currentIndex()
        Sector = [
            ToolIndexList[ToolIndex],
            TabWidget.tabText(TypeIndex).rsplit('（')[0],
        ]
        AddLocalModel(ModelPath, Sector)
        self.ui.Button_Models_Refresh.click()

    def setDirAlert(self, DirNameEdit: LineEditBase, RootEdit: LineEditBase, DirEdit: QLineEdit):
        def SetText_Dir():
            DirName = DirNameEdit.text()
            if len(DirName.strip()) == 0:
                alert = False
            else:
                DirText = Path(RootEdit.text()).joinpath(DirName).as_posix()
                alert = Path(DirText).exists() and list(Path(DirText).iterdir()) != []
                DirEdit.setText(DirText)
            DirNameEdit.alert(True if alert else False, "注意：目录已包含文件")
        DirNameEdit.interacted.connect(SetText_Dir)
        RootEdit.interacted.connect(SetText_Dir)

    def setPathAlert(self, FileNameEdit: LineEditBase, DirEdit: LineEditBase, suffix: str, FileEdit: QLineEdit):
        def SetText_File():
            fileName = FileNameEdit.text()
            if len(fileName.strip()) == 0:
                alert = False
            else:
                FileText = Path(DirEdit.text()).joinpath(fileName).as_posix() + suffix
                alert = Path(FileText).exists()
                FileEdit.setText(FileText)
            FileNameEdit.alert(True if alert else False, "注意：路径已存在")
        FileNameEdit.interacted.connect(SetText_File)
        DirEdit.interacted.connect(SetText_File)

    def setAudioSpeakersDataPath(self):
        DialogBox_AudioSpeakersDataPath = MessageBox_Buttons(self)
        DialogBox_AudioSpeakersDataPath.setText(QCA.translate('MainWindow', "请选择参数类型"))
        DialogBox_AudioSpeakersDataPath.Button1.setText(QCA.translate('MainWindow', "音频文件目录"))
        DialogBox_AudioSpeakersDataPath.Button1.clicked.connect(
            lambda: (
                self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.setText(
                    QFunc.getFileDialog(
                        mode = "SelectFolder",
                    )
                ),
                DialogBox_AudioSpeakersDataPath.close(),
            )
        )
        DialogBox_AudioSpeakersDataPath.Button2.setText(QCA.translate('MainWindow', "语音识别结果文本路径"))
        DialogBox_AudioSpeakersDataPath.Button2.clicked.connect(
            lambda: (
                self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.setText(
                    QFunc.getFileDialog(
                        mode = "SelectFile",
                        fileType = "txt类型 (*.txt)",
                        directory = Path(currentDir).joinpath('语音识别结果', 'VPR').as_posix()
                    )
                ),
                DialogBox_AudioSpeakersDataPath.close(),
            )
        )
        DialogBox_AudioSpeakersDataPath.exec()

    def showVPRResult(self, AudioSaveDir, AudioSpeakersData_Path, ComboItems):
        ChildWindow_VPR = Window_ChildWindow_VPR(self)

        ChildWindow_VPR.ui.Button_Close.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认放弃编辑？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_VPR.close()
                    )
                }
            )
        )
        ChildWindow_VPR.ui.Button_Maximize.clicked.connect(lambda: ChildWindow_VPR.showNormal() if ChildWindow_VPR.isMaximized() else ChildWindow_VPR.showMaximized())

        QFunc.setText(
            widget = ChildWindow_VPR.ui.Label_Title,
            text = QFunc.setRichText(
                QCA.translate('ChildWindow_VPR', "语音识别结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_VPR.ui.Label_Text,
            text = QFunc.setRichText(
                QCA.translate('ChildWindow_VPR', "这里记录了每个语音文件与其对应的人物名（留空表示无匹配人物且最终不会被保留）\n你可以对这些人物名进行更改并在表格下方设置音频的保存路径")
            )
        )

        ChildWindow_VPR.ui.Table.setHorizontalHeaderLabels(['音频路径', '人物姓名', '相似度', '播放', '操作'])

        ChildWindow_VPR.ui.CheckBox.setText(QCA.translate('ChildWindow_VPR', "结束编辑时将拥有匹配人物的音频保存到:"))
        ChildWindow_VPR.ui.CheckBox.setChecked(True)
        ChildWindow_VPR.ui.LineEdit.clearDefaultStyleSheet()
        ChildWindow_VPR.ui.LineEdit.setStyleSheet(ChildWindow_VPR.ui.LineEdit.styleSheet() + 'LineEditBase {border-width: 0px 0px 1px 0px; border-radius: 0px;}')
        ChildWindow_VPR.ui.LineEdit.setText(AudioSaveDir)
        ChildWindow_VPR.ui.LineEdit.setReadOnly(True)

        ChildWindow_VPR.ui.Button_Cancel.setText(QCA.translate('ChildWindow_VPR', "取消"))
        ChildWindow_VPR.ui.Button_Cancel.clicked.connect(ChildWindow_VPR.ui.Button_Close.click)
        ChildWindow_VPR.ui.Button_Save.setText(QCA.translate('ChildWindow_VPR', "保存"))
        ChildWindow_VPR.ui.Button_Save.clicked.connect(
            lambda: (
                VPRResult_Save(
                    ChildWindow_VPR.ui.Table.getValue(),
                    AudioSpeakersData_Path,
                    False
                ),
                MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "已保存当前结果。"
                )
            )
        )
        ChildWindow_VPR.ui.Button_Confirm.setText(QCA.translate('ChildWindow_VPR', "确认"))
        ChildWindow_VPR.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认结束并应用编辑？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        VPRResult_Save(
                            ChildWindow_VPR.ui.Table.getValue(),
                            AudioSpeakersData_Path,
                            ChildWindow_VPR.ui.CheckBox.isChecked(),
                            AudioSaveDir
                        ),
                        ChildWindow_VPR.close()
                    )
                }
            )
        )

        ChildWindow_VPR.ui.Table.setValue(
            VPRResult_Get(AudioSpeakersData_Path),
            ComboItems
        )
        ChildWindow_VPR.exec()

    def showASRResult(self, SRTDir, AudioDir):
        ChildWindow_ASR = Window_ChildWindow_ASR(self)

        ChildWindow_ASR.ui.Button_Close.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认放弃编辑？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_ASR.close()
                    )
                }
            )
        )
        ChildWindow_ASR.ui.Button_Maximize.clicked.connect(lambda: ChildWindow_ASR.showNormal() if ChildWindow_ASR.isMaximized() else ChildWindow_ASR.showMaximized())

        QFunc.setText(
            widget = ChildWindow_ASR.ui.Label_Title,
            text = QFunc.setRichText(
                QCA.translate('ChildWindow_ASR', "语音转录结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_ASR.ui.Label_Text,
            text = QFunc.setRichText(
                QCA.translate('ChildWindow_ASR', "这里记录了每个语音文件与其对应的字幕文本（包含了时间戳）\n你可以对这些文本进行更改，若启用了语种标注则小心不要误删")
            )
        )

        ChildWindow_ASR.ui.Table.setHorizontalHeaderLabels(['音频路径', '音频内容', '播放'])

        ChildWindow_ASR.ui.Button_Cancel.setText(QCA.translate('ChildWindow_ASR', "取消"))
        ChildWindow_ASR.ui.Button_Cancel.clicked.connect(ChildWindow_ASR.ui.Button_Close.click)
        ChildWindow_ASR.ui.Button_Confirm.setText(QCA.translate('ChildWindow_ASR', "确认"))
        ChildWindow_ASR.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认应用编辑？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ASRResult_Save(
                            ChildWindow_ASR.ui.Table.getValue(),
                            SRTDir
                        ),
                        ChildWindow_ASR.close()
                    )
                }
            )
        )

        ChildWindow_ASR.ui.Table.setValue(
            ASRResult_Get(SRTDir, AudioDir)
        )
        ChildWindow_ASR.exec()

    def showDATResult(self, DATPath_Training, DATPath_Validation):
        ChildWindow_DAT = Window_ChildWindow_DAT(self)

        ChildWindow_DAT.ui.Button_Close.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认放弃编辑？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_DAT.close()
                    )
                }
            )
        )
        ChildWindow_DAT.ui.Button_Maximize.clicked.connect(lambda: ChildWindow_DAT.showNormal() if ChildWindow_DAT.isMaximized() else ChildWindow_DAT.showMaximized())

        QFunc.setText(
            widget = ChildWindow_DAT.ui.Label_Title,
            text = QFunc.setRichText(
                QCA.translate('ChildWindow_DAT', "数据集制作结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_DAT.ui.Label_Text,
            text = QFunc.setRichText(
                QCA.translate('ChildWindow_DAT', "这里记录了每个语音文件与其对应的数据文本\n你可以对这些文本进行更改")
            )
        )

        ChildWindow_DAT.ui.Table_Train.setHorizontalHeaderLabels(['数据文本', '播放'])
        ChildWindow_DAT.ui.Table_Val.setHorizontalHeaderLabels(['数据文本', '播放'])

        ChildWindow_DAT.ui.Button_Cancel.setText(QCA.translate('ChildWindow_DAT', "取消"))
        ChildWindow_DAT.ui.Button_Cancel.clicked.connect(ChildWindow_DAT.ui.Button_Close.click)
        ChildWindow_DAT.ui.Button_Confirm.setText(QCA.translate('ChildWindow_DAT', "确认"))
        ChildWindow_DAT.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认应用编辑？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        DATResult_Save(
                            ChildWindow_DAT.ui.Table_Train.getValue(),
                            DATPath_Training
                        ),
                        DATResult_Save(
                            ChildWindow_DAT.ui.Table_Val.getValue(),
                            DATPath_Validation
                        ) if DATPath_Validation is not None else None,
                        ChildWindow_DAT.close()
                    )
                }
            )
        )

        ChildWindow_DAT.ui.Table_Train.setValue(
            DATResult_Get(DATPath_Training)
        )
        ChildWindow_DAT.ui.Table_Val.setValue(
            DATResult_Get(DATPath_Validation)
        ) if DATPath_Validation is not None else None
        ChildWindow_DAT.exec()

    def showTTSResult(self, MediaPath):
        ChildWindow_TTS = Window_ChildWindow_TTS(self)

        ChildWindow_TTS.ui.Button_Close.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认退出试听？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS.ui.widget.ReleaseMediaPlayer(),
                        ChildWindow_TTS.close()
                    )
                } 
            )
        )
        ChildWindow_TTS.ui.Button_Maximize.clicked.connect(lambda: ChildWindow_TTS.showNormal() if ChildWindow_TTS.isMaximized() else ChildWindow_TTS.showMaximized())

        QFunc.setText(
            widget = ChildWindow_TTS.ui.Label_Title,
            text = QFunc.setRichText(
                QCA.translate('ChildWindow_TTS', "语音合成结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_TTS.ui.Label_Text,
            text = QFunc.setRichText(
                QCA.translate('ChildWindow_TTS', "点击播放按钮以试听合成语音")
            )
        )

        ChildWindow_TTS.ui.Button_Cancel.setText(QCA.translate('ChildWindow_TTS', "丢弃"))
        ChildWindow_TTS.ui.Button_Cancel.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认丢弃音频？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS.ui.widget.ReleaseMediaPlayer(),
                        os.remove(MediaPath),
                        ChildWindow_TTS.close()
                    )
                }
            )
        )
        ChildWindow_TTS.ui.Button_Confirm.setText(QCA.translate('ChildWindow_TTS', "保留"))
        ChildWindow_TTS.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认保留音频？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS.ui.widget.ReleaseMediaPlayer(),
                        shutil.move(
                            MediaPath,
                            QFunc.getFileDialog(
                                mode = "SaveFile",
                                fileType = "wav类型 (*.wav)"
                            )
                        ),
                        ChildWindow_TTS.close()
                    )
                }
            )
        )

        ChildWindow_TTS.ui.widget.SetMediaPlayer(
            MediaPath
        )
        ChildWindow_TTS.exec()

    def chkUpdate(self):
        FunctionSignals.Signal_ReadyToUpdate.connect(
            lambda DownloadURL, VersionInfo: (
                MessageBoxBase.pop(None,
                    QMessageBox.Question, "Ask",
                    text = "检测到可用的新版本，是否更新？\nNew version available, wanna update?",
                    detailedText = VersionInfo,
                    buttons = QMessageBox.Yes|QMessageBox.No,
                    buttonEvents = {
                        QMessageBox.Yes: lambda: (
                            config.editConfig('Updater', 'Asked', 'True'),
                            subprocess.Popen(f'{"python" if isFileCompiled == False else ""} "{UpdaterPath}" --config "{configPath}"', shell = True, env = os.environ),
                            QApplication.instance().exit()
                        ),
                        QMessageBox.No: lambda: (
                            config.editConfig('Updater', 'Asked', 'False'),
                        )
                    }
                )
            )
        )

        Function_SetMethodExecutor(self,
            method = Execute_Update_Checking.Execute,
            params = ()
        )

    def main(self):
        '''
        Main funtion to orgnize all the subfunctions
        '''
        # Check for updates
        self.chkUpdate() if config.getValue('Settings', 'AutoUpdate', 'Enabled') == 'Enabled' else None

        # Logo
        self.setWindowIcon(QIcon(QFunc.normPath(Path(resourceDir).joinpath('assets/images/Logo.ico'))))

        #############################################################
        ########################## TitleBar #########################
        #############################################################

        # Theme toggler
        ComponentsSignals.Signal_SetTheme.connect(
            lambda: self.ui.CheckBox_SwitchTheme.setChecked(
                {Theme.Light: True, Theme.Dark: False}.get(EasyTheme.THEME)
            )
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_SwitchTheme,
            checkedEvents = [
                lambda: config.editConfig('Settings', 'Theme', Theme.Light),
                lambda: ComponentsSignals.Signal_SetTheme.emit(Theme.Light) if EasyTheme.THEME != Theme.Light else None
            ],
            uncheckedEvents = [
                lambda: config.editConfig('Settings', 'Theme', Theme.Dark),
                lambda: ComponentsSignals.Signal_SetTheme.emit(Theme.Dark) if EasyTheme.THEME != Theme.Dark else None
            ],
            takeEffect = False
        )

        # Window controling buttons
        self.ui.Button_Close_Window.clicked.connect(self.close)
        self.ui.Button_Close_Window.setBorderless(True)
        self.ui.Button_Close_Window.setTransparent(True)
        self.ui.Button_Close_Window.setHoverBackgroundColor(QColor(210, 123, 123, 210))
        self.ui.Button_Close_Window.setIcon(IconBase.X)

        self.ui.Button_Maximize_Window.clicked.connect(lambda: self.showNormal() if self.isMaximized() else self.showMaximized())
        self.ui.Button_Maximize_Window.setBorderless(True)
        self.ui.Button_Maximize_Window.setTransparent(True)
        self.ui.Button_Maximize_Window.setHoverBackgroundColor(QColor(123, 123, 123, 123))
        self.ui.Button_Maximize_Window.setIcon(IconBase.FullScreen)

        self.ui.Button_Minimize_Window.clicked.connect(self.showMinimized)
        self.ui.Button_Minimize_Window.setBorderless(True)
        self.ui.Button_Minimize_Window.setTransparent(True)
        self.ui.Button_Minimize_Window.setHoverBackgroundColor(QColor(123, 123, 123, 123))
        self.ui.Button_Minimize_Window.setIcon(IconBase.Dash)

        # Menu toggling button
        self.ui.Button_Toggle_Menu.clicked.connect(
            lambda: Function_AnimateFrame(
                frame = self.ui.Frame_Menu,
                minWidth = 48,
                maxWidth = 210
            )
        )
        self.ui.Button_Toggle_Menu.setChecked(False)
        self.ui.Button_Toggle_Menu.setToolTip(QCA.translate('MainWindow', "点击以展开/折叠菜单"))

        #############################################################
        ############################ Menu ###########################
        #############################################################

        self.ui.Button_Menu_Home.setText(QCA.translate('MainWindow', "主页"))
        self.ui.Button_Menu_Home.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 0
            )
        )
        self.ui.Button_Menu_Home.setChecked(True)
        self.ui.Button_Menu_Home.setToolTip(QCA.translate('MainWindow', "主页"))

        self.ui.Button_Menu_Env.setText(QCA.translate('MainWindow', "环境"))
        self.ui.Button_Menu_Env.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 1
            )
        )
        self.ui.Button_Menu_Env.setChecked(False)
        self.ui.Button_Menu_Env.setToolTip(QCA.translate('MainWindow', "环境配置"))

        self.ui.Button_Menu_Models.setText(QCA.translate('MainWindow', "模型"))
        self.ui.Button_Menu_Models.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 2
            )
        )
        self.ui.Button_Menu_Models.setChecked(False)
        self.ui.Button_Menu_Models.setToolTip(QCA.translate('MainWindow', "模型管理"))

        self.ui.Button_Menu_Process.setText(QCA.translate('MainWindow', "处理"))
        self.ui.Button_Menu_Process.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 3
            )
        )
        self.ui.Button_Menu_Process.setChecked(False)
        self.ui.Button_Menu_Process.setToolTip(QCA.translate('MainWindow', "工具：音频处理"))

        self.ui.Button_Menu_VPR.setText(QCA.translate('MainWindow', "识别"))
        self.ui.Button_Menu_VPR.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 4
            )
        )
        self.ui.Button_Menu_VPR.setChecked(False)
        self.ui.Button_Menu_VPR.setToolTip(QCA.translate('MainWindow', "工具：语音识别"))

        self.ui.Button_Menu_ASR.setText(QCA.translate('MainWindow', "转录"))
        self.ui.Button_Menu_ASR.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 5
            )
        )
        self.ui.Button_Menu_ASR.setChecked(False)
        self.ui.Button_Menu_ASR.setToolTip(QCA.translate('MainWindow', "工具：语音转文字"))

        self.ui.Button_Menu_Dataset.setText(QCA.translate('MainWindow', "数据"))
        self.ui.Button_Menu_Dataset.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 6
            )
        )
        self.ui.Button_Menu_Dataset.setChecked(False)
        self.ui.Button_Menu_Dataset.setToolTip(QCA.translate('MainWindow', "工具：数据集制作"))

        self.ui.Button_Menu_Train.setText(QCA.translate('MainWindow', "训练"))
        self.ui.Button_Menu_Train.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 7
            )
        )
        self.ui.Button_Menu_Train.setChecked(False)
        self.ui.Button_Menu_Train.setToolTip(QCA.translate('MainWindow', "工具：模型训练"))

        self.ui.Button_Menu_TTS.setText(QCA.translate('MainWindow', "合成"))
        self.ui.Button_Menu_TTS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 8
            )
        )
        self.ui.Button_Menu_TTS.setChecked(False)
        self.ui.Button_Menu_TTS.setToolTip(QCA.translate('MainWindow', "工具：语音合成"))

        self.ui.Button_Menu_Settings.setText(QCA.translate('MainWindow', "设置"))
        self.ui.Button_Menu_Settings.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 9
            )
        )
        self.ui.Button_Menu_Settings.setChecked(False)
        self.ui.Button_Menu_Settings.setToolTip(QCA.translate('MainWindow', "客户端设置"))

        self.ui.Button_Menu_Info.setText(QCA.translate('MainWindow', "关于"))
        self.ui.Button_Menu_Info.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 10
            )
        )
        self.ui.Button_Menu_Info.setChecked(False)
        self.ui.Button_Menu_Info.setToolTip(QCA.translate('MainWindow', "关于本软件"))

        #############################################################
        ####################### Content: Home #######################
        #############################################################

        self.ui.Label_Cover_Home.setPixmap(QPixmap(Path(resourceDir).joinpath('assets/images/others/Cover.png')))

        QFunc.setText(
            widget = self.ui.TextBrowser_Text_Home,
            text = QFunc.richTextManager().addTitle(
                text = QCA.translate('MainWindow', "介绍"),
                align = "left",
                size = 24,
                weight = 840,
            ).addBody(
                text = QCA.translate('MainWindow',
                    """
                    一个基于Whisper、VITS等项目实现的简易语音工具箱，提供了包括语音模型训练在内的多种自动化音频工具

                    工具箱目前包含以下功能：
                    音频处理
                    语音识别
                    语音转录
                    数据集制作
                    模型训练
                    语音合成

                    这些功能彼此之间相互独立，但又能无缝衔接地形成一套完整的工作流
                    用户可以根据自己的需求有选择性地使用，亦或者依次通过这些工具将未经处理的语音文件逐步变为理想的语音模型
                    """
                ),
                align = "left",
                size = 12,
                weight = 420,
                lineHeight = 27
            ).richText()
        )

        self.ui.Label_Demo_Text.setText(QCA.translate('MainWindow', "视频演示"))
        Function_SetURL(
            button = self.ui.Button_Demo,
            url = "https://www.bilibili.com/video/BV",
            buttonTooltip = "Click to view demo video"
        )
        self.ui.Label_Server_Text.setText(QCA.translate('MainWindow', "云端版本"))
        Function_SetURL(
            button = self.ui.Button_Server,
            url = "https://colab.research.google.com/github/Spr-Aachen/EVT-Reassets/images/others/blob/main/Easy_Voice_Toolkit_for_Colab.ipynb",
            buttonTooltip = "Click to run on server"
        )
        self.ui.Label_Repo_Text.setText(QCA.translate('MainWindow', "项目仓库"))
        Function_SetURL(
            button = self.ui.Button_Repo,
            url = "https://github.com/Spr-Aachen/Easy-Voice-Toolkit",
            buttonTooltip = "Click to view github repo"
        )
        self.ui.Label_Donate_Text.setText(QCA.translate('MainWindow', "赞助作者"))
        Function_SetURL(
            button = self.ui.Button_Donate,
            url = "https://ko-fi.com/spr_aachen",
            buttonTooltip = "Click to buy author a coffee"
        )

        #############################################################
        ##################### Content: Environ ######################
        #############################################################

        # EnvInstallation
        self.ui.Button_Env_Install_Title.setText(QCA.translate('MainWindow', "自动配置"))
        self.ui.Button_Env_Install_Title.setHorizontal(True)
        self.ui.Button_Env_Install_Title.setChecked(True)
        self.ui.Button_Env_Install_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Env,
                target = 0
            )
        )

        self.ui.Label_Env_Install_Aria2.setText(QCA.translate('MainWindow', "Aria2"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_Install_Aria2,
            progressBar = self.ui.ProgressBar_Env_Install_Aria2,
            method = Aria2_Installer.Execute,
            params = ()
        )
        MainWindowSignals.Signal_MainWindowShown.connect(
            self.ui.Button_Install_Aria2.click
        )
        self.ui.Button_Install_Aria2.setToolTip(QCA.translate('MainWindow', "重新检测安装"))
        EnvConfiguratorSignals.Signal_Aria2Undetected.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Information, "Tip",
                text = "未检测到Aria2，已开始下载",
                buttonEvents = {QMessageBox.Ok: lambda: self.ui.Button_Menu_Env.click()}
            )
        )
        EnvConfiguratorSignals.Signal_Aria2Installed.connect(#self.ui.Button_Install_Aria2.click)
            lambda: EnvConfiguratorSignals.Signal_Aria2Detected.emit()
        )
        EnvConfiguratorSignals.Signal_Aria2InstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = f"安装Aria2出错",
                detailedText = Exception
            )
        )
        EnvConfiguratorSignals.Signal_Aria2Detected.connect(
            lambda: self.ui.ProgressBar_Env_Install_Aria2.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_Aria2Status.connect(
            lambda Status: self.ui.Label_Env_Install_Aria2_Status.setText(Status)
        )

        self.ui.Label_Env_Install_FFmpeg.setText(QCA.translate('MainWindow', "FFmpeg"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_Install_FFmpeg,
            progressBar = self.ui.ProgressBar_Env_Install_FFmpeg,
            method = FFmpeg_Installer.Execute,
            params = ()
        )
        MainWindowSignals.Signal_MainWindowShown.connect(
            self.ui.Button_Install_FFmpeg.click
        )
        self.ui.Button_Install_FFmpeg.setToolTip(QCA.translate('MainWindow', "重新检测安装"))
        EnvConfiguratorSignals.Signal_FFmpegUndetected.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Information, "Tip",
                text = "未检测到FFmpeg，已开始下载",
                buttonEvents = {QMessageBox.Ok: lambda: self.ui.Button_Menu_Env.click()}
            )
        )
        EnvConfiguratorSignals.Signal_FFmpegInstalled.connect(#self.ui.Button_Install_FFmpeg.click)
            lambda: EnvConfiguratorSignals.Signal_FFmpegDetected.emit()
        )
        EnvConfiguratorSignals.Signal_FFmpegInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = f"安装FFmpeg出错",
                detailedText = Exception
            )
        )
        EnvConfiguratorSignals.Signal_FFmpegDetected.connect(
            lambda: self.ui.ProgressBar_Env_Install_FFmpeg.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_FFmpegStatus.connect(
            lambda Status: self.ui.Label_Env_Install_FFmpeg_Status.setText(Status)
        )

        self.ui.Label_Env_Install_Python.setText(QCA.translate('MainWindow', "Python"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_Install_Python,
            progressBar = self.ui.ProgressBar_Env_Install_Python,
            method = Python_Installer.Execute,
            params = ('3.9.0', )
        )
        MainWindowSignals.Signal_MainWindowShown.connect( #EnvConfiguratorSignals.Signal_CMakeDetected.connect(
            self.ui.Button_Install_Python.click
        )
        self.ui.Button_Install_Python.setToolTip(QCA.translate('MainWindow', "重新检测安装"))
        EnvConfiguratorSignals.Signal_PythonUndetected.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Information, "Tip",
                text = "未检测到3.8版本以上的Python，已开始下载",
                buttonEvents = {QMessageBox.Ok: lambda: self.ui.Button_Menu_Env.click()}
            )
        )
        EnvConfiguratorSignals.Signal_PythonInstalled.connect(#self.ui.Button_Install_Python.click)
            lambda: EnvConfiguratorSignals.Signal_PythonDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PythonInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = f"安装Python出错",
                detailedText = Exception
            )
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            lambda: self.ui.ProgressBar_Env_Install_Python.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PythonStatus.connect(
            lambda Status: self.ui.Label_Env_Install_Python_Status.setText(Status)
        )

        self.ui.Label_Env_Install_PyReqs.setText(QCA.translate('MainWindow', "Python Requirements"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_Install_PyReqs,
            progressBar = self.ui.ProgressBar_Env_Install_PyReqs,
            method = PyReqs_Installer.Execute,
            params = (QFunc.normPath(RequirementsPath), )
        ) if Path(RequirementsPath).exists() else None
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            self.ui.Button_Install_PyReqs.click
        )
        self.ui.Button_Install_PyReqs.setToolTip(QCA.translate('MainWindow', "重新检测安装"))
        EnvConfiguratorSignals.Signal_PyReqsUndetected.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Information, "Tip",
                text = "缺失Python依赖库，已开始下载",
                buttonEvents = {QMessageBox.Ok: lambda: self.ui.Button_Menu_Env.click()}
            )
        )
        EnvConfiguratorSignals.Signal_PyReqsInstalled.connect(#self.ui.Button_Install_PyReqs.click)
            lambda: EnvConfiguratorSignals.Signal_PyReqsDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PyReqsInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = f"安装Python依赖库出错",
                detailedText = Exception
            )
        )
        EnvConfiguratorSignals.Signal_PyReqsDetected.connect(
            lambda: self.ui.ProgressBar_Env_Install_PyReqs.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PyReqsStatus.connect(
            lambda Status: self.ui.Label_Env_Install_PyReqs_Status.setText(Status)
        )

        self.ui.Label_Env_Install_Pytorch.setText(QCA.translate('MainWindow', "Pytorch"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_Install_Pytorch,
            progressBar = self.ui.ProgressBar_Env_Install_Pytorch,
            method = Pytorch_Installer.Execute,
            params = ()
        )
        EnvConfiguratorSignals.Signal_PyReqsDetected.connect(
            self.ui.Button_Install_Pytorch.click
        )
        self.ui.Button_Install_Pytorch.setToolTip(QCA.translate('MainWindow', "重新检测安装"))
        EnvConfiguratorSignals.Signal_PytorchUndetected.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Information, "Tip",
                text = "缺失Pytorch相关库，已开始下载",
                buttonEvents = {QMessageBox.Ok: lambda: self.ui.Button_Menu_Env.click()}
            )
        )
        EnvConfiguratorSignals.Signal_PytorchInstalled.connect(#self.ui.Button_Install_Pytorch.click)
            lambda: EnvConfiguratorSignals.Signal_PytorchDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PytorchInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = f"安装Pytorch出错",
                detailedText = Exception
            )
        )
        EnvConfiguratorSignals.Signal_PytorchDetected.connect(
            lambda: self.ui.ProgressBar_Env_Install_Pytorch.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PytorchStatus.connect(
            lambda Status: self.ui.Label_Env_Install_Pytorch_Status.setText(Status)
        )

        # EnvManagement
        self.ui.Button_Env_Manage_Title.setText(QCA.translate('MainWindow', "安装管理"))
        self.ui.Button_Env_Manage_Title.setHorizontal(True)
        self.ui.Button_Env_Manage_Title.setChecked(False)
        self.ui.Button_Env_Manage_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Env,
                target = 1
            )
        )

        self.ui.ToolBox_Env_Manage_Pytorch.widget(0).setText(QCA.translate('MainWindow', "Pytorch"))
        self.ui.ToolBox_Env_Manage_Pytorch.widget(0).collapse()

        self.ui.Label_Env_Manage_Pytorch_Version.setText(QCA.translate('MainWindow', "选择Pytorch版本"))
        self.ui.ComboBox_Env_Manage_Pytorch_Version.addItems([ '2.0.1', '2.2.2'])

        self.ui.Button_Env_Manage_Pytorch_Install.setText(QCA.translate('MainWindow', "重装"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_Env_Manage_Pytorch_Install,
            method = Pytorch_Installer.Execute,
            paramsFrom = [
                self.ui.ComboBox_Env_Manage_Pytorch_Version,
                True
            ]
        )

        #############################################################
        ####################### Content: Models #####################
        #############################################################

        MainWindowSignals.Signal_MainWindowShown.connect(
            lambda: Function_SetMethodExecutor(self,
                method = Model_View.Execute
            )
        )

        self.ui.Button_Models_Process_Title.setText(QCA.translate('MainWindow', '基本处理'))
        self.ui.Button_Models_Process_Title.setHorizontal(True)
        self.ui.Button_Models_Process_Title.setChecked(True)
        self.ui.Button_Models_Process_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 0
            )
        )
        self.ui.Button_Models_Process_Title.setToolTip(QCA.translate('MainWindow', "基本处理模型"))

        self.ui.TabWidget_Models_Process.setTabText(0, 'UVR（人声分离）')
        self.ui.Table_Models_Process_UVR.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        ModelViewSignals.Signal_Process_UVR.connect(self.ui.Table_Models_Process_UVR.setValue)
        self.ui.Table_Models_Process_UVR.Download.connect(
            lambda params: Function_SetMethodExecutor(self,
                method = Model_Downloader.Execute,
                params = params
            )
        )

        self.ui.Button_Models_VPR_Title.setText(QCA.translate('MainWindow', 'VPR（识别）'))
        self.ui.Button_Models_VPR_Title.setHorizontal(True)
        self.ui.Button_Models_VPR_Title.setChecked(False)
        self.ui.Button_Models_VPR_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 1
            )
        )
        self.ui.Button_Models_VPR_Title.setToolTip(QCA.translate('MainWindow', "语音识别模型"))

        self.ui.TabWidget_Models_VPR.setTabText(0, 'VPR（声纹识别）')
        self.ui.Table_Models_VPR_TDNN.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        ModelViewSignals.Signal_VPR_TDNN.connect(self.ui.Table_Models_VPR_TDNN.setValue)
        self.ui.Table_Models_VPR_TDNN.Download.connect(
            lambda params: Function_SetMethodExecutor(self,
                method = Model_Downloader.Execute,
                params = params
            )
        )

        self.ui.Button_Models_ASR_Title.setText(QCA.translate('MainWindow', 'ASR（转录）'))
        self.ui.Button_Models_ASR_Title.setHorizontal(True)
        self.ui.Button_Models_ASR_Title.setChecked(False)
        self.ui.Button_Models_ASR_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 2
            )
        )
        self.ui.Button_Models_ASR_Title.setToolTip(QCA.translate('MainWindow', "语音转录模型"))

        self.ui.TabWidget_Models_ASR.setTabText(0, 'Whisper')
        self.ui.Table_Models_ASR_Whisper.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        ModelViewSignals.Signal_ASR_Whisper.connect(self.ui.Table_Models_ASR_Whisper.setValue)
        self.ui.Table_Models_ASR_Whisper.Download.connect(
            lambda params: Function_SetMethodExecutor(self,
                method = Model_Downloader.Execute,
                params = params
            )
        )

        self.ui.Button_Models_TTS_Title.setText(QCA.translate('MainWindow', 'TTS（合成）'))
        self.ui.Button_Models_TTS_Title.setHorizontal(True)
        self.ui.Button_Models_TTS_Title.setChecked(False)
        self.ui.Button_Models_TTS_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 3
            )
        )
        self.ui.Button_Models_TTS_Title.setToolTip(QCA.translate('MainWindow', "语音合成模型"))

        self.ui.TabWidget_Models_TTS.setTabText(0, 'GPT-SoVITS')
        self.ui.Table_Models_TTS_GPTSoVITS.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        ModelViewSignals.Signal_TTS_GPTSoVITS.connect(self.ui.Table_Models_TTS_GPTSoVITS.setValue)
        self.ui.Table_Models_TTS_GPTSoVITS.Download.connect(
            lambda params: Function_SetMethodExecutor(self,
                method = Model_Downloader.Execute,
                params = params
            )
        )

        self.ui.TabWidget_Models_TTS.setTabText(1, 'VITS')
        self.ui.Table_Models_TTS_VITS.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        ModelViewSignals.Signal_TTS_VITS.connect(self.ui.Table_Models_TTS_VITS.setValue)
        self.ui.Table_Models_TTS_VITS.Download.connect(
            lambda params: Function_SetMethodExecutor(self,
                method = Model_Downloader.Execute,
                params = params
            )
        )

        self.ui.Button_Models_Refresh.setText(QCA.translate('MainWindow', '刷新'))
        self.ui.Button_Models_Refresh.clicked.connect(
            lambda: Function_SetMethodExecutor(self,
                method = Model_View.Execute
            )
        )

        self.ui.Button_Models_Append.setText(QCA.translate('MainWindow', '添加'))
        self.ui.Button_Models_Append.clicked.connect(self.appendModels)

        #############################################################
        ###################### Content: Process #####################
        #############################################################

        # Guidance
        self.ui.Button_AudioProcessor_Help.clicked.connect(
            lambda: self.showGuidance(
                QCA.translate('MainWindow', "引导（仅出现一次）"),
                [
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Process.png')),
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                [
                    '欢迎来到音频处理工具界面\n该工具用于将媒体文件批量转换为音频文件并进行降噪、静音切除等操作',
                    '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
                ]
            )
        )

        self.ui.Button_Menu_Process.clicked.connect(
            lambda: (
                self.ui.Button_AudioProcessor_Help.click(),
                config.editConfig('Dialog', 'GuidanceShown_Process', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_Process', 'False')) is False else None
        )

        # ParamsManager
        Path_Config_Process = QFunc.normPath(Path(configDir).joinpath('Config_Process.ini'))
        ParamsManager_Process = ParamsManager(Path_Config_Process)

        # Top
        self.ui.Button_AudioProcessor_Title.setText(QCA.translate('MainWindow', '音频基本处理'))
        self.ui.Button_AudioProcessor_Title.setHorizontal(True)
        self.ui.Button_AudioProcessor_Title.setChecked(True)
        self.ui.Button_AudioProcessor_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Process,
                target = 0
            )
        )

        # Left
        self.ui.TreeWidget_Catalogue_Process.clear()
        self.ui.TreeWidget_Catalogue_Process.setHeaderHidden(True)

        # Middle
        self.ui.GroupBox_Process_InputParams.setTitle(QCA.translate('MainWindow', "输入参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_Process_InputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "输入参数")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_MediaDirInput,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "媒体输入目录\n需要处理的音频文件的所在目录。")
            )
        )
        ParamsManager_Process.SetParam(
            widget = self.ui.LineEdit_Process_MediaDirInput,
            section = 'Input params',
            option = 'Media_Dir_Input',
            defaultValue = '',
            setPlaceholderText = True
        )
        self.ui.LineEdit_Process_MediaDirInput.setFileDialog(
            mode = "SelectFolder"
        )
        self.ui.Button_Process_MediaDirInput_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.LineEdit_Process_MediaDirInput),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Process_MediaDirInput.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_MediaDirInput,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "媒体输入目录")
        )

        self.ui.GroupBox_Process_DenoiserParams.setTitle(QCA.translate('MainWindow', "降噪参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_Process_DenoiserParams,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "降噪参数")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_DenoiseAudio,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "启用杂音去除\n弱化音频中的非人声部分。")
            )
        )
        ParamsManager_Process.SetParam(
            widget = self.ui.CheckBox_Process_DenoiseAudio,
            section = 'Denoiser params',
            option = 'Denoise_Audio',
            defaultValue = True
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Process_DenoiseAudio,
            checkedText = "已启用",
            checkedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_Process_DenoiserParams_BasicSettings,
                    [
                        self.ui.Frame_Process_DenoiseModelPath,
                        self.ui.Frame_Process_DenoiseTarget,
                    ],
                    True
                )
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_Process_DenoiserParams_BasicSettings,
                    [
                        self.ui.Frame_Process_DenoiseModelPath,
                        self.ui.Frame_Process_DenoiseTarget,
                    ],
                    False
                )
            ],
            takeEffect = True
        )
        self.ui.Button_Process_DenoiseAudio_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.CheckBox_Process_DenoiseAudio)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_DenoiseAudio,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "降噪参数"),
            childItemText = QCA.translate('MainWindow', "启用杂音去除")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_DenoiseModelPath,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "uvr5模型路径\n用于uvr5降噪的模型文件的路径。")
            )
        )
        Process_DenoiseModelPath_Default = Path(ModelDir).joinpath('Process', 'UVR', 'Downloaded', 'HP5_only_main_vocal.pth').as_posix()
        ParamsManager_Process.SetParam(
            widget = self.ui.LineEdit_Process_DenoiseModelPath,
            section = 'Denoiser params',
            option = 'Denoise_Model_Path',
            defaultValue = Process_DenoiseModelPath_Default,
            setPlaceholderText = True
        )
        self.ui.LineEdit_Process_DenoiseModelPath.setFileDialog(
            mode = "SelectFile",
            fileType = "pth类型/onnx类型 (*.pth *.onnx)",
            directory = QFunc.normPath(Path(ModelDir).joinpath('Process', 'UVR', 'Downloaded'))
        )
        self.ui.Button_Process_DenoiseModelPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.LineEdit_Process_DenoiseModelPath),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Process_DenoiseModelPath.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_DenoiseModelPath,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "降噪参数"),
            childItemText = QCA.translate('MainWindow', "uvr5模型路径")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_DenoiseTarget,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "提取目标\n选择在降噪时要保留的声音对象。")
            )
        )
        self.ui.ComboBox_Process_DenoiseTarget.addItems([QCA.translate('MainWindow', '人声'), QCA.translate('MainWindow', '背景声')])
        ParamsManager_Process.SetParam(
            widget = self.ui.ComboBox_Process_DenoiseTarget,
            section = 'Denoiser params',
            option = 'Denoise_Target',
            defaultValue = '人声'
        )
        self.ui.Button_Process_DenoiseTarget_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.ComboBox_Process_DenoiseTarget)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_DenoiseTarget,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "降噪参数"),
            childItemText = QCA.translate('MainWindow', "提取目标")
        )

        self.ui.GroupBox_Process_SlicerParams.setTitle(QCA.translate('MainWindow', "静音切除参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_Process_SlicerParams,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "静音切除参数")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_SliceAudio,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "启用静音切除\n切除音频中的静音部分。")
            )
        )
        ParamsManager_Process.SetParam(
            widget = self.ui.CheckBox_Process_SliceAudio,
            section = 'Slicer params',
            option = 'Slice_Audio',
            defaultValue = True
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Process_SliceAudio,
            checkedText = "已启用",
            checkedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content,
                    [
                        self.ui.Frame_Process_RMSThreshold,
                        self.ui.Frame_Process_HopSize,
                        self.ui.Frame_Process_SilentIntervalMin,
                        self.ui.Frame_Process_SilenceKeptMax,
                        self.ui.Frame_Process_AudioLengthMin
                    ],
                    True,
                    True
                )
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content,
                    [
                        self.ui.Frame_Process_RMSThreshold,
                        self.ui.Frame_Process_HopSize,
                        self.ui.Frame_Process_SilentIntervalMin,
                        self.ui.Frame_Process_SilenceKeptMax,
                        self.ui.Frame_Process_AudioLengthMin
                    ],
                    False,
                    True
                )
            ],
            takeEffect = True
        )
        self.ui.Button_Process_SliceAudio_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.CheckBox_Process_SliceAudio)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_SliceAudio,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            childItemText = QCA.translate('MainWindow', "启用静音切除")
        )

        self.ui.ToolBox_Process_SlicerParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_Process_SlicerParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_Process_RMSThreshold,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "均方根阈值 (db)\n低于该阈值的片段将被视作静音进行处理，若有降噪需求可以增加该值。")
            )
        )
        self.ui.DoubleSpinBox_Process_RMSThreshold.setRange(-100, 0)
        #self.ui.DoubleSpinBox_Process_RMSThreshold.setSingleStep(0.01)
        ParamsManager_Process.SetParam(
            widget = self.ui.DoubleSpinBox_Process_RMSThreshold,
            section = 'Slicer params',
            option = 'RMS_Threshold',
            defaultValue = -34.
        )
        self.ui.Button_Process_RMSThreshold_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.DoubleSpinBox_Process_RMSThreshold)
            }
            
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_RMSThreshold,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            childItemText = QCA.translate('MainWindow', "均方根阈值")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_HopSize,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "跃点大小 (ms)\n每个RMS帧的长度，增加该值能够提高分割精度但会减慢进程。")
            )
        )
        self.ui.SpinBox_Process_HopSize.setRange(0, 100)
        self.ui.SpinBox_Process_HopSize.setSingleStep(1)
        ParamsManager_Process.SetParam(
            widget = self.ui.SpinBox_Process_HopSize,
            section = 'Slicer params',
            option = 'Hop_Size',
            defaultValue = 10
        )
        self.ui.Button_Process_HopSize_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.SpinBox_Process_HopSize)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_HopSize,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            childItemText = QCA.translate('MainWindow', "跃点大小")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_SilentIntervalMin,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "最小静音间隔 (ms)\n静音部分被分割成的最小长度，若音频只包含短暂中断可以减小该值。")
            )
        )
        self.ui.SpinBox_Process_SilentIntervalMin.setRange(0, 3000)
        self.ui.SpinBox_Process_SilentIntervalMin.setSingleStep(1)
        ParamsManager_Process.SetParam(
            widget = self.ui.SpinBox_Process_SilentIntervalMin,
            section = 'Slicer params',
            option = 'Silent_Interval_Min',
            defaultValue = 300
        )
        self.ui.SpinBox_Process_SilentIntervalMin.setToolTip(QCA.translate('MainWindow', "注意：这个值必须小于最小音频长度，大于跃点大小。"))
        self.ui.Button_Process_SilentIntervalMin_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.SpinBox_Process_SilentIntervalMin)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_SilentIntervalMin,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            childItemText = QCA.translate('MainWindow', "最小静音间隔")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_SilenceKeptMax,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "最大静音长度 (ms)\n被分割的音频周围保持静音的最大长度。")
            )
        )
        self.ui.SpinBox_Process_SilenceKeptMax.setRange(0, 10000)
        self.ui.SpinBox_Process_SilenceKeptMax.setSingleStep(1)
        ParamsManager_Process.SetParam(
            widget = self.ui.SpinBox_Process_SilenceKeptMax,
            section = 'Slicer params',
            option = 'Silence_Kept_Max',
            defaultValue = 500
        )
        self.ui.SpinBox_Process_SilenceKeptMax.setToolTip(QCA.translate('MainWindow', "注意：这个值无需完全对应被分割音频中的静音长度。算法将自行检索最佳的分割位置。"))
        self.ui.Button_Process_SilenceKeptMax_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.SpinBox_Process_SilenceKeptMax)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_SilenceKeptMax,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            childItemText = QCA.translate('MainWindow', "最大静音长度")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_AudioLengthMin,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "最小音频长度 (ms)\n每个被分割的音频片段所需的最小长度。")
            )
        )
        self.ui.SpinBox_Process_AudioLengthMin.setRange(300, 30000)
        self.ui.SpinBox_Process_AudioLengthMin.setSingleStep(1)
        ParamsManager_Process.SetParam(
            widget = self.ui.SpinBox_Process_AudioLengthMin,
            section = 'Slicer params',
            option = 'Audio_Length_Min',
            defaultValue = 4000
        )
        self.ui.Button_Process_AudioLengthMin_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.SpinBox_Process_AudioLengthMin)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_AudioLengthMin,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            childItemText = QCA.translate('MainWindow', "最小音频长度")
        )

        self.ui.GroupBox_Process_OutputParams.setTitle(QCA.translate('MainWindow', "输出参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_Process_OutputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "输出参数")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_MediaFormatOutput,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "媒体输出格式\n媒体文件输出为音频文件的格式，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Process_MediaFormatOutput.addItems(['flac', 'wav', 'mp3', 'aac', 'm4a', 'wma', 'aiff', 'au', 'ogg', 'None'])
        ParamsManager_Process.SetParam(
            widget = self.ui.ComboBox_Process_MediaFormatOutput,
            section = 'Output params',
            option = 'Media_Format_Output',
            defaultValue = 'wav'
        )
        self.ui.Button_Process_MediaFormatOutput_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.ComboBox_Process_MediaFormatOutput)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_AudioLengthMin,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "媒体输出格式")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_OutputDirName,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "输出目录名\n用于保存最后生成的音频文件的目录的名字。")
            )
        )
        Process_OutputDirName_Default = str(date.today())
        ParamsManager_Process.SetParam(
            widget = self.ui.LineEdit_Process_OutputDirName,
            section = 'Output params',
            option = 'Output_Dir_Name',
            defaultValue = '',
            setPlaceholderText = True,
            placeholderText = Process_OutputDirName_Default
        )
        self.ui.Button_Process_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.LineEdit_Process_OutputDirName),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Process_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_OutputDirName,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "输出目录名")
        )

        LineEdit_Process_OutputDir = LineEditBase()
        self.setDirAlert(
            DirNameEdit = self.ui.LineEdit_Process_OutputDirName,
            RootEdit = self.ui.LineEdit_Process_OutputRoot,
            DirEdit = LineEdit_Process_OutputDir
        )

        self.ui.ToolBox_Process_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_Process_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_Process_ToMono,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "合并声道\n将输出音频的声道合并为单声道。")
            )
        )
        ParamsManager_Process.SetParam(
            widget = self.ui.CheckBox_Process_ToMono,
            section = 'Output params',
            option = 'ToMono',
            defaultValue = False
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Process_ToMono,
            checkedText = "已启用",
            checkedEvents = [
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
            ],
            takeEffect = True
        )
        self.ui.Button_Process_ToMono_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.CheckBox_Process_ToMono)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_ToMono,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "合并声道")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_SampleRate,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "输出采样率\n输出音频所拥有的采样率，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Process_SampleRate.addItems(['22050', '44100', '48000', '96000', '192000', 'None'])
        ParamsManager_Process.SetParam(
            widget = self.ui.ComboBox_Process_SampleRate,
            section = 'Output params',
            option = 'SampleRate',
            defaultValue = None
        )
        self.ui.Button_Process_SampleRate_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.ComboBox_Process_SampleRate)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_SampleRate,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "输出采样率")
        )

        QFunc.setText(
            widget = self.ui.Label_Process_SampleWidth,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "输出采样位数\n输出音频所拥有的采样位数，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Process_SampleWidth.addItems(['8', '16', '24', '32', '32 (Float)', 'None'])
        ParamsManager_Process.SetParam(
            widget = self.ui.ComboBox_Process_SampleWidth,
            section = 'Output params',
            option = 'SampleWidth',
            defaultValue = None
        )
        self.ui.Button_Process_SampleWidth_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.ComboBox_Process_SampleWidth)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Process_SampleWidth,
            treeWidget = self.ui.TreeWidget_Catalogue_Process,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "输出采样位数")
        )

        # Right
        MonitorFile_Config_AudioProcessor = QTasks.MonitorFile(Path_Config_Process)
        MonitorFile_Config_AudioProcessor.start()
        MonitorFile_Config_AudioProcessor.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Process.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_Process.setText(QCA.translate('MainWindow', "全部重置"))
        self.ui.Button_ResetSettings_Process.clicked.connect(
            lambda: ParamsManager_Process.ResetSettings()
        )

        self.ui.Button_ImportSettings_Process.setText(QCA.translate('MainWindow', "导入配置"))
        self.ui.Button_ImportSettings_Process.clicked.connect(
            lambda: ParamsManager_Process.ImportSettings(
                QFunc.getFileDialog(
                    mode = "SelectFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_Process.setText(QCA.translate('MainWindow', "导出配置"))
        self.ui.Button_ExportSettings_Process.clicked.connect(
            lambda: ParamsManager_Process.ExportSettings(
                QFunc.getFileDialog(
                    mode = "SaveFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_CheckOutput_Process.setText(QCA.translate('MainWindow', "打开输出目录"))
        Function_SetURL(
            button = self.ui.Button_CheckOutput_Process,
            url = self.ui.LineEdit_Process_OutputRoot,
            buttonTooltip = "Click to open",
            createIfNotExist = True
        )

        # Bottom
        self.ui.Button_Process_Execute.setText(QCA.translate('MainWindow', "执行音频处理"))
        self.ui.Button_Process_Terminate.setText(QCA.translate('MainWindow', "终止音频处理"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_Process_Execute,
            terminateButton = self.ui.Button_Process_Terminate,
            progressBar = self.ui.ProgressBar_Process,
            consoleWidget = self.ui.Frame_Console,
            method = Execute_Audio_Processing.Execute,
            paramsFrom = [
                self.ui.LineEdit_Process_MediaDirInput,
                self.ui.ComboBox_Process_MediaFormatOutput,
                self.ui.ComboBox_Process_SampleRate,
                self.ui.ComboBox_Process_SampleWidth,
                self.ui.CheckBox_Process_ToMono,
                self.ui.CheckBox_Process_DenoiseAudio,
                self.ui.LineEdit_Process_DenoiseModelPath,
                self.ui.ComboBox_Process_DenoiseTarget,
                self.ui.CheckBox_Process_SliceAudio,
                self.ui.DoubleSpinBox_Process_RMSThreshold,
                self.ui.SpinBox_Process_AudioLengthMin,
                self.ui.SpinBox_Process_SilentIntervalMin,
                self.ui.SpinBox_Process_HopSize,
                self.ui.SpinBox_Process_SilenceKeptMax,
                self.ui.LineEdit_Process_OutputRoot,
                self.ui.LineEdit_Process_OutputDirName
            ],
            emptyAllowed = [
                self.ui.ComboBox_Process_MediaFormatOutput,
                self.ui.ComboBox_Process_SampleRate,
                self.ui.ComboBox_Process_SampleWidth
            ],
            successEvents = [
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        #############################################################
        ######################## Content: VPR #######################
        #############################################################

        # Guidance
        self.ui.Button_VoiceIdentifier_Help.clicked.connect(
            lambda: self.showGuidance(
                QCA.translate('MainWindow', "引导（仅出现一次）"),
                [
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_VPR.png')),
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                [
                    '欢迎来到语音识别工具界面\n该工具用于从不同说话人的音频中批量筛选出属于同一说话人的音频',
                    '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
                ]
            )
        )

        self.ui.Button_Menu_VPR.clicked.connect(
            lambda: (
                self.ui.Button_VoiceIdentifier_Help.click(),
                config.editConfig('Dialog', 'GuidanceShown_VPR', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_VPR', 'False')) is False else None
        )

        # ParamsManager
        Path_Config_VPR_TDNN = QFunc.normPath(Path(configDir).joinpath('Config_VPR_TDNN.ini'))
        ParamsManager_VPR_TDNN = ParamsManager(Path_Config_VPR_TDNN)

        # Top
        self.ui.Button_VoiceIdentifier_Title.setText(QCA.translate('MainWindow', "VPR（声纹识别）"))
        self.ui.Button_VoiceIdentifier_Title.setHorizontal(True)
        self.ui.Button_VoiceIdentifier_Title.setChecked(True)
        self.ui.Button_VoiceIdentifier_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_VPR,
                target = 0
            )
        )

        # Left
        self.ui.TreeWidget_Catalogue_VPR_TDNN.clear()
        self.ui.TreeWidget_Catalogue_VPR_TDNN.setHeaderHidden(True)

        # Middle
        self.ui.GroupBox_VPR_TDNN_InputParams.setTitle(QCA.translate('MainWindow', "输入参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_VPR_TDNN_InputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "输入参数")
        )

        QFunc.setText(
            widget = self.ui.Label_VPR_TDNN_AudioDirInput,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "音频输入目录\n需要进行语音识别筛选的音频文件的所在目录。")
            )
        )
        ParamsManager_VPR_TDNN.SetParam(
            widget = self.ui.LineEdit_VPR_TDNN_AudioDirInput,
            section = 'Input params',
            option = 'Audio_Dir_Input',
            defaultValue = '',
            setPlaceholderText = True
        )
        self.ui.LineEdit_VPR_TDNN_AudioDirInput.setFileDialog(
            mode = "SelectFolder",
            directory = Path(currentDir).joinpath('音频处理结果').as_posix()
        )
        self.ui.Button_VPR_TDNN_AudioDirInput_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_VPR_TDNN.ResetParam(self.ui.LineEdit_VPR_TDNN_AudioDirInput),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_VPR_TDNN_AudioDirInput.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_VPR_TDNN_AudioDirInput,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "音频输入目录")
        )

        QFunc.setText(
            widget = self.ui.Label_VPR_TDNN_StdAudioSpeaker,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "目标人物与音频\n目标人物的名字及其语音文件的路径。")
            )
        )
        self.ui.Table_VPR_TDNN_StdAudioSpeaker.setHorizontalHeaderLabels(['人物姓名', '音频路径', '增删'])
        ParamsManager_VPR_TDNN.SetParam(
            widget = self.ui.Table_VPR_TDNN_StdAudioSpeaker,
            section = 'Input params',
            option = 'StdAudioSpeaker',
            defaultValue = {"": ""}
        )
        self.ui.Table_VPR_TDNN_StdAudioSpeaker.setFileDialog(
            fileType = "音频类型 (*.flac *.wav *.mp3 *.aac *.m4a *.wma *.aiff *.au *.ogg)"
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_VPR_TDNN_StdAudioSpeaker,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "目标人物与音频")
        )

        self.ui.GroupBox_VPR_TDNN_VPRParams.setTitle(QCA.translate('MainWindow', "语音识别参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_VPR_TDNN_VPRParams,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "语音识别参数")
        )

        QFunc.setText(
            widget = self.ui.Label_VPR_TDNN_DecisionThreshold,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "判断阈值\n判断相似度的阈值，若参与比对的说话人声音相似度较高可以增加该值。")
            )
        )
        self.ui.DoubleSpinBox_VPR_TDNN_DecisionThreshold.setRange(0.5, 1)
        self.ui.DoubleSpinBox_VPR_TDNN_DecisionThreshold.setSingleStep(0.01)
        ParamsManager_VPR_TDNN.SetParam(
            widget = self.ui.DoubleSpinBox_VPR_TDNN_DecisionThreshold,
            section = 'VPR params',
            option = 'DecisionThreshold',
            defaultValue = 0.75
        )
        self.ui.Button_VPR_TDNN_DecisionThreshold_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_VPR_TDNN.ResetParam(self.ui.DoubleSpinBox_VPR_TDNN_DecisionThreshold)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_VPR_TDNN_DecisionThreshold,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "语音识别参数"),
            childItemText = QCA.translate('MainWindow', "判断阈值")
        )

        QFunc.setText(
            widget = self.ui.Label_VPR_TDNN_ModelPath,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "模型加载路径\n用于加载的声纹识别模型的路径。")
            )
        )
        VPR_TDNN_ModelPath_Default = Path(ModelDir).joinpath('VPR', 'TDNN', 'Downloaded', 'Ecapa-Tdnn_spectrogram.pth').as_posix()
        ParamsManager_VPR_TDNN.SetParam(
            widget = self.ui.LineEdit_VPR_TDNN_ModelPath,
            section = 'VPR params',
            option = 'Model_Path',
            defaultValue = VPR_TDNN_ModelPath_Default,
            setPlaceholderText = True,
            placeholderText = VPR_TDNN_ModelPath_Default
        )
        self.ui.LineEdit_VPR_TDNN_ModelPath.setFileDialog(
            mode = "SelectFile",
            fileType = "pth类型 (*.pth)",
            directory = QFunc.normPath(Path(ModelDir).joinpath('VPR', 'TDNN', 'Downloaded'))
        )
        self.ui.Button_VPR_TDNN_ModelPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_VPR_TDNN.ResetParam(self.ui.LineEdit_VPR_TDNN_ModelPath),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_VPR_TDNN_ModelPath.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_VPR_TDNN_ModelPath,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "语音识别参数"),
            childItemText = QCA.translate('MainWindow', "模型加载路径")
        )

        self.ui.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_VPR_TDNN_VPRParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_VPR_TDNN_ModelType,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "模型类型\n声纹识别模型的类型。")
            )
        )
        self.ui.ComboBox_VPR_TDNN_ModelType.addItems(['Ecapa-Tdnn'])
        ParamsManager_VPR_TDNN.SetParam(
            widget = self.ui.ComboBox_VPR_TDNN_ModelType,
            section = 'VPR params',
            option = 'Model_Type',
            defaultValue = 'Ecapa-Tdnn'
        )
        self.ui.Button_VPR_TDNN_ModelPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_VPR_TDNN.ResetParam(self.ui.ComboBox_VPR_TDNN_ModelType)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_VPR_TDNN_ModelType,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "语音识别参数"),
            childItemText = QCA.translate('MainWindow', "模型类型")
        )

        QFunc.setText(
            widget = self.ui.Label_VPR_TDNN_FeatureMethod,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "预处理方法\n音频的预处理方法。")
            )
        )
        self.ui.ComboBox_VPR_TDNN_FeatureMethod.addItems(['spectrogram', 'melspectrogram'])
        ParamsManager_VPR_TDNN.SetParam(
            widget = self.ui.ComboBox_VPR_TDNN_FeatureMethod,
            section = 'VPR params',
            option = 'Feature_Method',
            defaultValue = 'spectrogram'
        )
        self.ui.Button_VPR_TDNN_FeatureMethod_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_VPR_TDNN.ResetParam(self.ui.ComboBox_VPR_TDNN_FeatureMethod)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_VPR_TDNN_FeatureMethod,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "语音识别参数"),
            childItemText = QCA.translate('MainWindow', "预处理方法")
        )

        QFunc.setText(
            widget = self.ui.Label_VPR_TDNN_DurationOfAudio,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "音频长度\n用于预测的音频长度。")
            )
        )
        self.ui.DoubleSpinBox_VPR_TDNN_DurationOfAudio.setRange(0, 30)
        #self.ui.DoubleSpinBox_VPR_TDNN_DurationOfAudio.setSingleStep(0.01)
        ParamsManager_VPR_TDNN.SetParam(
            widget = self.ui.DoubleSpinBox_VPR_TDNN_DurationOfAudio,
            section = 'VPR params',
            option = 'Duration_of_Audio',
            defaultValue = 3.00
        )
        self.ui.Button_VPR_TDNN_DurationOfAudio_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_VPR_TDNN.ResetParam(self.ui.DoubleSpinBox_VPR_TDNN_DurationOfAudio)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_VPR_TDNN_DurationOfAudio,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "语音识别参数"),
            childItemText = QCA.translate('MainWindow', "音频长度")
        )

        self.ui.GroupBox_VPR_TDNN_OutputParams.setTitle(QCA.translate('MainWindow', "输出参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_VPR_TDNN_OutputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "输出参数")
        )

        QFunc.setText(
            widget = self.ui.Label_VPR_TDNN_OutputDirName,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "输出目录名\n用于保存最后生成的结果文件的目录的名字。")
            )
        )
        VPR_TDNN_OutputDirName_Default = str(date.today())
        ParamsManager_VPR_TDNN.SetParam(
            widget = self.ui.LineEdit_VPR_TDNN_OutputDirName,
            section = 'Output params',
            option = 'Audio_Dir_Output',
            defaultValue = '',
            setPlaceholderText = True,
            placeholderText = VPR_TDNN_OutputDirName_Default
        )
        self.ui.Button_VPR_TDNN_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_VPR_TDNN.ResetParam(self.ui.LineEdit_VPR_TDNN_OutputDirName),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_VPR_TDNN_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_VPR_TDNN_OutputDirName,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "输出目录名")
        )

        self.ui.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_VPR_TDNN_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_VPR_TDNN_AudioSpeakersDataName,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "识别结果文本名\n用于保存最后生成的记录音频文件与对应说话人的txt文件的名字。")
            )
        )
        VPR_TDNN_AudioSpeakersDataName_Default = "Recgonition_" + str(date.today())
        ParamsManager_VPR_TDNN.SetParam(
            widget = self.ui.LineEdit_VPR_TDNN_AudioSpeakersDataName,
            section = 'Output params',
            option = 'FileList_Name',
            defaultValue = VPR_TDNN_AudioSpeakersDataName_Default,
            setPlaceholderText = True,
            placeholderText = VPR_TDNN_AudioSpeakersDataName_Default
        )
        self.ui.Button_VPR_TDNN_AudioSpeakersDataName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_VPR_TDNN.ResetParam(self.ui.LineEdit_VPR_TDNN_AudioSpeakersDataName),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_VPR_TDNN_AudioSpeakersDataName.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_VPR_TDNN_AudioSpeakersDataName,
            treeWidget = self.ui.TreeWidget_Catalogue_VPR_TDNN,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "识别结果文本名")
        )

        LineEdit_VPR_TDNN_OutputDir = LineEditBase()
        self.setDirAlert(
            DirNameEdit = self.ui.LineEdit_VPR_TDNN_OutputDirName,
            RootEdit = self.ui.LineEdit_VPR_TDNN_OutputRoot,
            DirEdit = LineEdit_VPR_TDNN_OutputDir
        )

        LineEdit_VPR_TDNN_AudioSpeakersDataPath = LineEditBase()
        self.setPathAlert(
            FileNameEdit = self.ui.LineEdit_VPR_TDNN_AudioSpeakersDataName,
            DirEdit = LineEdit_VPR_TDNN_OutputDir,
            suffix = ".txt",
            FileEdit = LineEdit_VPR_TDNN_AudioSpeakersDataPath
        )

        # Right
        MonitorFile_Config_VoiceIdentifier = QTasks.MonitorFile(Path_Config_VPR_TDNN)
        MonitorFile_Config_VoiceIdentifier.start()
        MonitorFile_Config_VoiceIdentifier.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_VPR_TDNN.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_VPR_TDNN.setText(QCA.translate('MainWindow', "全部重置"))
        self.ui.Button_ResetSettings_VPR_TDNN.clicked.connect(
            lambda: ParamsManager_VPR_TDNN.ResetSettings()
        )

        self.ui.Button_ImportSettings_VPR_TDNN.setText(QCA.translate('MainWindow', "导入配置"))
        self.ui.Button_ImportSettings_VPR_TDNN.clicked.connect(
            lambda: ParamsManager_VPR_TDNN.ImportSettings(
                QFunc.getFileDialog(
                    mode = "SelectFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_VPR_TDNN.setText(QCA.translate('MainWindow', "导出配置"))
        self.ui.Button_ExportSettings_VPR_TDNN.clicked.connect(
            lambda: ParamsManager_VPR_TDNN.ExportSettings(
                QFunc.getFileDialog(
                    mode = "SaveFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_EditResult_VPR_TDNN.setText(QCA.translate('MainWindow', "编辑识别结果"))
        def EditVPRResult():
            VPRResultPath = QFunc.getFileDialog(
                mode = "SelectFile",
                fileType = "txt类型 (*.txt)",
                directory = Path(currentDir).joinpath('语音识别结果', 'VPR').as_posix()
            )
            if QFunc.normPath(VPRResultPath) is not None:
                self.showMask(True, "正在加载表单")
                self.showVPRResult(
                    LineEdit_VPR_TDNN_OutputDir.text(),
                    VPRResultPath,
                    None
                )
        self.ui.Button_EditResult_VPR_TDNN.clicked.connect(EditVPRResult)

        self.ui.Button_CheckOutput_VPR_TDNN.setText(QCA.translate('MainWindow', "打开输出目录"))
        Function_SetURL(
            button = self.ui.Button_CheckOutput_VPR_TDNN,
            url = self.ui.LineEdit_VPR_TDNN_OutputRoot,
            buttonTooltip = "Click to open",
            createIfNotExist = True
        )

        # Bottom
        self.ui.Button_VPR_TDNN_Execute.setText(QCA.translate('MainWindow', "执行语音识别"))
        self.ui.Button_VPR_TDNN_Terminate.setText(QCA.translate('MainWindow', "终止语音识别"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_VPR_TDNN_Execute,
            terminateButton = self.ui.Button_VPR_TDNN_Terminate,
            progressBar = self.ui.ProgressBar_VPR_TDNN,
            consoleWidget = self.ui.Frame_Console,
            method = Execute_Voice_Identifying_VPR.Execute,
            paramsFrom = [
                self.ui.Table_VPR_TDNN_StdAudioSpeaker,
                self.ui.LineEdit_VPR_TDNN_AudioDirInput,
                self.ui.LineEdit_VPR_TDNN_ModelPath,
                self.ui.ComboBox_VPR_TDNN_ModelType,
                self.ui.ComboBox_VPR_TDNN_FeatureMethod,
                self.ui.DoubleSpinBox_VPR_TDNN_DecisionThreshold,
                self.ui.DoubleSpinBox_VPR_TDNN_DurationOfAudio,
                self.ui.LineEdit_VPR_TDNN_OutputRoot,
                self.ui.LineEdit_VPR_TDNN_OutputDirName,
                self.ui.LineEdit_VPR_TDNN_AudioSpeakersDataName
            ],
            successEvents = [
                lambda: self.showMask(True, "正在加载表单"),
                lambda: self.showVPRResult(
                    LineEdit_VPR_TDNN_OutputDir.text(),
                    LineEdit_VPR_TDNN_AudioSpeakersDataPath.text(),
                    list(self.ui.Table_VPR_TDNN_StdAudioSpeaker.getValue().keys()) + ['']
                ),
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        #############################################################
        ######################## Content: ASR #######################
        #############################################################

        # Guidance
        self.ui.Button_VoiceTranscriber_Help.clicked.connect(
            lambda: self.showGuidance(
                QCA.translate('MainWindow', "引导（仅出现一次）"),
                [
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_ASR.png')),
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                [
                    '欢迎来到语音转录工具界面\n该工具用于将语音文件批量转换为字幕文件并进行语言标注等操作',
                    '顶部区域用于切换当前工具类型\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
                ]
            )
        )

        self.ui.Button_Menu_ASR.clicked.connect(
            lambda: (
                self.ui.Button_VoiceTranscriber_Help.click(),
                config.editConfig('Dialog', 'GuidanceShown_ASR', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_ASR', 'False')) is False else None
        )

        # ParamsManager
        Path_Config_ASR_Whisper = QFunc.normPath(Path(configDir).joinpath('Config_ASR_Whisper.ini'))
        ParamsManager_ASR_Whisper = ParamsManager(Path_Config_ASR_Whisper)

        # Top
        self.ui.Button_VoiceTranscriber_Title.setText(QCA.translate('MainWindow', "Whisper"))
        self.ui.Button_VoiceTranscriber_Title.setHorizontal(True)
        self.ui.Button_VoiceTranscriber_Title.setChecked(True)
        self.ui.Button_VoiceTranscriber_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_ASR,
                target = 0
            )
        )

        # Left
        self.ui.TreeWidget_Catalogue_ASR_Whisper.clear()
        self.ui.TreeWidget_Catalogue_ASR_Whisper.setHeaderHidden(True)

        # Middle
        self.ui.GroupBox_ASR_Whisper_InputParams.setTitle(QCA.translate('MainWindow', "输入参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_ASR_Whisper_InputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_ASR_Whisper,
            rootItemText = QCA.translate('MainWindow', "输入参数")
        )

        QFunc.setText(
            widget = self.ui.Label_ASR_Whisper_AudioDir,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "音频输入目录\n需要将语音内容转为文字的音频文件的所在目录。")
            )
        )
        ParamsManager_ASR_Whisper.SetParam(
            widget = self.ui.LineEdit_ASR_Whisper_AudioDir,
            section = 'Input params',
            option = 'Audio_Dir',
            defaultValue = '',
            setPlaceholderText = True
        )
        self.ui.LineEdit_ASR_Whisper_AudioDir.setFileDialog(
            mode = "SelectFolder"
        )
        self.ui.Button_ASR_Whisper_AudioDir_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_Whisper.ResetParam(self.ui.LineEdit_ASR_Whisper_AudioDir),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_ASR_Whisper_AudioDir.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_ASR_Whisper_AudioDir,
            treeWidget = self.ui.TreeWidget_Catalogue_ASR_Whisper,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "音频输入目录")
        )

        self.ui.GroupBox_ASR_Whisper_WhisperParams.setTitle(QCA.translate('MainWindow', "语音转录参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_ASR_Whisper_WhisperParams,
            treeWidget = self.ui.TreeWidget_Catalogue_ASR_Whisper,
            rootItemText = QCA.translate('MainWindow', "语音转录参数")
        )

        QFunc.setText(
            widget = self.ui.Label_ASR_Whisper_AddLanguageInfo,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "语种标注\n标注音频中说话人所使用的语言，若用于数据集制作则建议启用。")
            )
        )
        ParamsManager_ASR_Whisper.SetParam(
            widget = self.ui.CheckBox_ASR_Whisper_AddLanguageInfo,
            section = 'Whisper params',
            option = 'Add_LanguageInfo',
            defaultValue = True
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_ASR_Whisper_AddLanguageInfo,
            checkedText = "已启用",
            checkedEvents = [
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
            ],
            takeEffect = True
        )
        self.ui.Button_ASR_Whisper_AddLanguageInfo_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_Whisper.ResetParam(self.ui.CheckBox_ASR_Whisper_AddLanguageInfo)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_ASR_Whisper_AddLanguageInfo,
            treeWidget = self.ui.TreeWidget_Catalogue_ASR_Whisper,
            rootItemText = QCA.translate('MainWindow', "语音转录参数"),
            childItemText = QCA.translate('MainWindow', "语种标注")
        )

        QFunc.setText(
            widget = self.ui.Label_ASR_Whisper_ModelPath,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "模型加载路径\n用于加载的Whisper模型的路径。")
            )
        )
        ASR_Whisper_ModelPath_Default = Path(ModelDir).joinpath('ASR', 'Whisper', 'Downloaded', 'small.pt').as_posix()
        ParamsManager_ASR_Whisper.SetParam(
            widget = self.ui.LineEdit_ASR_Whisper_ModelPath,
            section = 'Whisper params',
            option = 'Model_Path',
            defaultValue = ASR_Whisper_ModelPath_Default,
            setPlaceholderText = True,
            placeholderText = ASR_Whisper_ModelPath_Default
        )
        self.ui.LineEdit_ASR_Whisper_ModelPath.setFileDialog(
            mode = "SelectFile",
            fileType = "pt类型 (*.pt)",
            directory = QFunc.normPath(Path(ModelDir).joinpath('ASR', 'Whisper', 'Downloaded'))
        )
        self.ui.Button_ASR_Whisper_ModelPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_Whisper.ResetParam(self.ui.LineEdit_ASR_Whisper_ModelPath),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_ASR_Whisper_ModelPath.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_ASR_Whisper_ModelPath,
            treeWidget = self.ui.TreeWidget_Catalogue_ASR_Whisper,
            rootItemText = QCA.translate('MainWindow', "语音转录参数"),
            childItemText = QCA.translate('MainWindow', "模型加载路径")
        )

        self.ui.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_ASR_Whisper_WhisperParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_ASR_Whisper_Verbose,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "显示转录内容\n启用该项后会在运行过程中显示转录的内容，否则只显示进度。")
            )
        )
        ParamsManager_ASR_Whisper.SetParam(
            widget = self.ui.CheckBox_ASR_Whisper_Verbose,
            section = 'Whisper params',
            option = 'Verbose',
            defaultValue = True
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_ASR_Whisper_Verbose,
            checkedText = "已启用",
            checkedEvents = [
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
            ],
            takeEffect = True
        )
        self.ui.Button_ASR_Whisper_Verbose_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_Whisper.ResetParam(self.ui.CheckBox_ASR_Whisper_Verbose)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_ASR_Whisper_Verbose,
            treeWidget = self.ui.TreeWidget_Catalogue_ASR_Whisper,
            rootItemText = QCA.translate('MainWindow', "语音转录参数"),
            childItemText = QCA.translate('MainWindow', "显示转录内容")
        )

        QFunc.setText(
            widget = self.ui.Label_ASR_Whisper_fp16,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "半精度计算\n主要使用半精度浮点数进行计算，若GPU不可用则忽略或禁用此项。")
            )
        )
        ParamsManager_ASR_Whisper.SetParam(
            widget = self.ui.CheckBox_ASR_Whisper_fp16,
            section = 'Whisper params',
            option = 'fp16',
            defaultValue = True
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_ASR_Whisper_fp16,
            checkedText = "已启用",
            checkedEvents = [
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
            ],
            takeEffect = True
        )
        self.ui.Button_ASR_Whisper_fp16_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_Whisper.ResetParam(self.ui.CheckBox_ASR_Whisper_fp16)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_ASR_Whisper_fp16,
            treeWidget = self.ui.TreeWidget_Catalogue_ASR_Whisper,
            rootItemText = QCA.translate('MainWindow', "语音转录参数"),
            childItemText = QCA.translate('MainWindow', "半精度计算")
        )

        QFunc.setText(
            widget = self.ui.Label_ASR_Whisper_ConditionOnPreviousText,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "关联上下文\n在音频之间的内容具有关联性时启用该项可以获得更好的效果。")
            )
        )
        ParamsManager_ASR_Whisper.SetParam(
            widget = self.ui.CheckBox_ASR_Whisper_ConditionOnPreviousText,
            section = 'Whisper params',
            option = 'Condition_on_Previous_Text',
            defaultValue = False
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_ASR_Whisper_ConditionOnPreviousText,
            checkedText = "已启用",
            checkedEvents = [
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
            ],
            takeEffect = True
        )
        self.ui.Button_ASR_Whisper_ConditionOnPreviousText_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_Whisper.ResetParam(self.ui.CheckBox_ASR_Whisper_ConditionOnPreviousText)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_ASR_Whisper_ConditionOnPreviousText,
            treeWidget = self.ui.TreeWidget_Catalogue_ASR_Whisper,
            rootItemText = QCA.translate('MainWindow', "语音转录参数"),
            childItemText = QCA.translate('MainWindow', "关联上下文")
        )

        self.ui.GroupBox_ASR_Whisper_OutputParams.setTitle(QCA.translate('MainWindow', "输出参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_ASR_Whisper_OutputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_ASR_Whisper,
            rootItemText = QCA.translate('MainWindow', "输出参数")
        )

        QFunc.setText(
            widget = self.ui.Label_ASR_Whisper_OutputDirName,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "输出目录名\n用于保存最后生成的字幕文件的目录的名字。")
            )
        )
        ASR_Whisper_OutputDirName_Default = str(date.today())
        ParamsManager_ASR_Whisper.SetParam(
            widget = self.ui.LineEdit_ASR_Whisper_OutputDirName,
            section = 'Output params',
            option = 'SRT_Dir_Name',
            defaultValue = '',
            setPlaceholderText = True,
            placeholderText = ASR_Whisper_OutputDirName_Default
        )
        self.ui.Button_ASR_Whisper_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_Whisper.ResetParam(self.ui.LineEdit_ASR_Whisper_OutputDirName),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_ASR_Whisper_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_ASR_Whisper_OutputDirName,
            treeWidget = self.ui.TreeWidget_Catalogue_ASR_Whisper,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "输出目录名")
        )

        LineEdit_ASR_Whisper_OutputDir = LineEditBase()
        self.setDirAlert(
            DirNameEdit = self.ui.LineEdit_ASR_Whisper_OutputDirName,
            RootEdit = self.ui.LineEdit_ASR_Whisper_OutputRoot,
            DirEdit = LineEdit_ASR_Whisper_OutputDir
        )

        # Right
        MonitorFile_Config_VoiceTranscriber = QTasks.MonitorFile(Path_Config_ASR_Whisper)
        MonitorFile_Config_VoiceTranscriber.start()
        MonitorFile_Config_VoiceTranscriber.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_ASR_Whisper.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_ASR_Whisper.setText(QCA.translate('MainWindow', "全部重置"))
        self.ui.Button_ResetSettings_ASR_Whisper.clicked.connect(
            lambda: ParamsManager_ASR_Whisper.ResetSettings()
        )

        self.ui.Button_ImportSettings_ASR_Whisper.setText(QCA.translate('MainWindow', "导入配置"))
        self.ui.Button_ImportSettings_ASR_Whisper.clicked.connect(
            lambda: ParamsManager_ASR_Whisper.ImportSettings(
                QFunc.getFileDialog(
                    mode = "SelectFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_ASR_Whisper.setText(QCA.translate('MainWindow', "导出配置"))
        self.ui.Button_ExportSettings_ASR_Whisper.clicked.connect(
            lambda: ParamsManager_ASR_Whisper.ExportSettings(
                QFunc.getFileDialog(
                    mode = "SaveFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_CheckOutput_ASR_Whisper.setText(QCA.translate('MainWindow', "打开输出目录"))
        Function_SetURL(
            button = self.ui.Button_CheckOutput_ASR_Whisper,
            url = self.ui.LineEdit_ASR_Whisper_OutputRoot,
            buttonTooltip = "Click to open",
            createIfNotExist = True
        )

        # Bottom
        self.ui.Button_ASR_Whisper_Execute.setText(QCA.translate('MainWindow', "执行语音转录"))
        self.ui.Button_ASR_Whisper_Terminate.setText(QCA.translate('MainWindow', "终止语音转录"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_ASR_Whisper_Execute,
            terminateButton = self.ui.Button_ASR_Whisper_Terminate,
            progressBar = self.ui.ProgressBar_ASR_Whisper,
            consoleWidget = self.ui.Frame_Console,
            method = Execute_Voice_Transcribing_Whisper.Execute,
            paramsFrom = [
                self.ui.LineEdit_ASR_Whisper_ModelPath,
                self.ui.LineEdit_ASR_Whisper_AudioDir,
                self.ui.CheckBox_ASR_Whisper_Verbose,
                self.ui.CheckBox_ASR_Whisper_AddLanguageInfo,
                self.ui.CheckBox_ASR_Whisper_ConditionOnPreviousText,
                self.ui.CheckBox_ASR_Whisper_fp16,
                self.ui.LineEdit_ASR_Whisper_OutputRoot,
                self.ui.LineEdit_ASR_Whisper_OutputDirName
            ],
            successEvents = [
                lambda: self.showMask(True, "正在加载表单"),
                lambda: self.showASRResult(
                    LineEdit_ASR_Whisper_OutputDir.text(), self.ui.LineEdit_ASR_Whisper_AudioDir.text()
                ),
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        #############################################################
        ###################### Content: Dataset #####################
        #############################################################

        # Guidance
        self.ui.Button_DatasetCreator_Help.clicked.connect(
            lambda: self.showGuidance(
                QCA.translate('MainWindow', "引导（仅出现一次）"),
                [
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Dataset.png')),
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                [
                    '欢迎来到数据集工具界面\n该工具用于生成适用于语音模型训练的数据集',
                    '顶部区域用于切换当前工具类型\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
                ]
            )
        )

        self.ui.Button_Menu_Dataset.clicked.connect(
            lambda: (
                self.ui.Button_DatasetCreator_Help.click(),
                config.editConfig('Dialog', 'GuidanceShown_Dataset', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_Dataset', 'False')) is False else None
        )

        # GPT-SoVITS - ParamsManager
        Path_Config_DAT_GPTSoVITS = QFunc.normPath(Path(configDir).joinpath('Config_DAT_GPT-SoVITS.ini'))
        ParamsManager_DAT_GPTSoVITS = ParamsManager(Path_Config_DAT_GPTSoVITS)

        # GPT-SoVITS - Top
        self.ui.Button_DatasetCreator_Title_GPTSoVITS.setText(QCA.translate('MainWindow', "GPT-SoVITS"))
        self.ui.Button_DatasetCreator_Title_GPTSoVITS.setHorizontal(True)
        self.ui.Button_DatasetCreator_Title_GPTSoVITS.setChecked(True)
        self.ui.Button_DatasetCreator_Title_GPTSoVITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Dataset,
                target = 0
            )
        )

        # GPT-SoVITS - Left
        self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS.clear()
        self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS.setHeaderHidden(True)

        # GPT-SoVITS - Middle
        self.ui.GroupBox_DAT_GPTSoVITS_InputParams.setTitle(QCA.translate('MainWindow', "输入参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_DAT_GPTSoVITS_InputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输入参数")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_GPTSoVITS_AudioSpeakersDataPath,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "音频文件目录/语音识别结果文本路径\n音频文件的所在目录，或者提供由语音识别得到的文本文件。")
            )
        )
        ParamsManager_DAT_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath,
            section = 'Input params',
            option = 'WAV_Dir',
            defaultValue = '',
            setPlaceholderText = True
        )
        self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.fileButton.clicked.connect(self.setAudioSpeakersDataPath)
        self.ui.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_GPTSoVITS_AudioSpeakersDataPath,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "音频文件目录")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_GPTSoVITS_SRTDir,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "字幕输入目录\n字幕文件的所在目录，字幕文件须与对应音频文件同名且在文本中注明所属语言。")
            )
        )
        ParamsManager_DAT_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_DAT_GPTSoVITS_SRTDir,
            section = 'Input params',
            option = 'SRT_Dir',
            defaultValue = '',
            setPlaceholderText = True
        )
        self.ui.LineEdit_DAT_GPTSoVITS_SRTDir.setFileDialog(
            mode = "SelectFolder",
            directory = Path(currentDir).joinpath('语音转录结果', 'Whisper').as_posix()
        )
        self.ui.Button_DAT_GPTSoVITS_SRTDir_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_SRTDir),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_GPTSoVITS_SRTDir.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_GPTSoVITS_SRTDir,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "字幕输入目录")
        )

        self.ui.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams.setTitle(QCA.translate('MainWindow', "数据集参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "数据集参数")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_GPTSoVITS_DataFormat,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "数据文本格式\n数据集的文本格式，默认使用GPT-SoVITS的标准。")
            )
        )
        DAT_GPTSoVITS_DataFormat_Default = '路径|人名|语言|文本'
        ParamsManager_DAT_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_DAT_GPTSoVITS_DataFormat,
            section = 'GPT-SoVITS params',
            option = 'DataFormat_Path',
            defaultValue = DAT_GPTSoVITS_DataFormat_Default,
            setPlaceholderText = True,
            placeholderText = DAT_GPTSoVITS_DataFormat_Default
        )
        self.ui.LineEdit_DAT_GPTSoVITS_DataFormat.textChanged.connect(
            lambda value: (
                MessageBoxBase.pop(self,
                    QMessageBox.Warning, "Warning",
                    "请保留关键词：'路径'，'人名'，'语言'，'文本'",
                ),
                ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_DataFormat),
            ) if not all(Keyword in value for Keyword in ['路径', '人名', '语言', '文本']) else None
        )
        self.ui.Button_DAT_GPTSoVITS_DataFormat_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_DataFormat),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_GPTSoVITS_DataFormat.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_GPTSoVITS_DataFormat,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            childItemText = QCA.translate('MainWindow', "数据文本格式")
        )

        self.ui.GroupBox_DAT_GPTSoVITS_OutputParams.setTitle(QCA.translate('MainWindow', "输出参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_DAT_GPTSoVITS_OutputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输出参数")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_GPTSoVITS_OutputDirName,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "输出目录名\n用于保存最后生成的数据集文件的目录的名字。")
            )
        )
        DAT_GPTSoVITS_OutputDirName_Default = str(date.today())
        ParamsManager_DAT_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName,
            section = 'Output params',
            option = 'Output_Dir_Name',
            defaultValue = '',
            setPlaceholderText = True,
            placeholderText = DAT_GPTSoVITS_OutputDirName_Default
        )
        self.ui.Button_DAT_GPTSoVITS_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_GPTSoVITS_OutputDirName,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "输出目录名")
        )

        self.ui.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_DAT_GPTSoVITS_FileListName,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "数据集文本名\n用于保存最后生成的数据集txt文件的名字。")
            )
        )
        DAT_GPTSoVITS_FileListName_Default = "Train_" + str(date.today())
        ParamsManager_DAT_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_DAT_GPTSoVITS_FileListName,
            section = 'Output params',
            option = 'FileList_Name',
            defaultValue = DAT_GPTSoVITS_FileListName_Default,
            setPlaceholderText = True,
            placeholderText = DAT_GPTSoVITS_FileListName_Default
        )
        self.ui.Button_DAT_GPTSoVITS_FileListName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_FileListName),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_GPTSoVITS_FileListName.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_GPTSoVITS_FileListName,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "数据集文本名")
        )

        LineEdit_DAT_GPTSoVITS_OutputDir = LineEditBase()
        self.setDirAlert(
            DirNameEdit = self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName,
            RootEdit = self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot,
            DirEdit = LineEdit_DAT_GPTSoVITS_OutputDir
        )

        LineEdit_DAT_GPTSoVITS_FileListPath = LineEditBase()
        self.setPathAlert(
            FileNameEdit = self.ui.LineEdit_DAT_GPTSoVITS_FileListName,
            DirEdit = LineEdit_DAT_GPTSoVITS_OutputDir,
            suffix = ".txt",
            FileEdit = LineEdit_DAT_GPTSoVITS_FileListPath,
        )

        # GPT-SoVITS - Right
        MonitorFile_Config_DatasetCreator_GPTSoVITS = QTasks.MonitorFile(Path_Config_DAT_GPTSoVITS)
        MonitorFile_Config_DatasetCreator_GPTSoVITS.start()
        MonitorFile_Config_DatasetCreator_GPTSoVITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_DAT_GPTSoVITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_DAT_GPTSoVITS.setText(QCA.translate('MainWindow', "全部重置"))
        self.ui.Button_ResetSettings_DAT_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_DAT_GPTSoVITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_DAT_GPTSoVITS.setText(QCA.translate('MainWindow', "导入配置"))
        self.ui.Button_ImportSettings_DAT_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_DAT_GPTSoVITS.ImportSettings(
                QFunc.getFileDialog(
                    mode = "SelectFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_DAT_GPTSoVITS.setText(QCA.translate('MainWindow', "导出配置"))
        self.ui.Button_ExportSettings_DAT_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_DAT_GPTSoVITS.ExportSettings(
                QFunc.getFileDialog(
                    mode = "SaveFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_CheckOutput_DAT_GPTSoVITS.setText(QCA.translate('MainWindow', "打开输出目录"))
        Function_SetURL(
            button = self.ui.Button_CheckOutput_DAT_GPTSoVITS,
            url = self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot,
            buttonTooltip = "Click to open",
            createIfNotExist = True
        )

        # GPT-SoVITS - Bottom
        self.ui.Button_DAT_GPTSoVITS_Execute.setText(QCA.translate('MainWindow', "执行数据集制作"))
        self.ui.Button_DAT_GPTSoVITS_Terminate.setText(QCA.translate('MainWindow', "终止数据集制作"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_DAT_GPTSoVITS_Execute,
            terminateButton = self.ui.Button_DAT_GPTSoVITS_Terminate,
            progressBar = self.ui.ProgressBar_DAT_GPTSoVITS,
            consoleWidget = self.ui.Frame_Console,
            method = Execute_Dataset_Creating_GPTSoVITS.Execute,
            paramsFrom = [
                self.ui.LineEdit_DAT_GPTSoVITS_SRTDir,
                self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath,
                self.ui.LineEdit_DAT_GPTSoVITS_DataFormat,
                self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot,
                self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName,
                self.ui.LineEdit_DAT_GPTSoVITS_FileListName
            ],
            emptyAllowed = [
            ],
            successEvents = [
                lambda: self.showMask(True, "正在加载表单"),
                lambda: self.showDATResult(
                    LineEdit_DAT_GPTSoVITS_FileListPath.text(),
                    None
                ),
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        # VITS - ParamsManager
        Path_Config_DAT_VITS = QFunc.normPath(Path(configDir).joinpath('Config_DAT_VITS.ini'))
        ParamsManager_DAT_VITS = ParamsManager(Path_Config_DAT_VITS)

        # VITS - Top
        self.ui.Button_DatasetCreator_Title_VITS.setText(QCA.translate('MainWindow', "VITS2"))
        self.ui.Button_DatasetCreator_Title_VITS.setHorizontal(True)
        self.ui.Button_DatasetCreator_Title_VITS.setChecked(False)
        self.ui.Button_DatasetCreator_Title_VITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Dataset,
                target = 1
            )
        )

        # VITS - Left
        self.ui.TreeWidget_Catalogue_DAT_VITS.clear()
        self.ui.TreeWidget_Catalogue_DAT_VITS.setHeaderHidden(True)

        # VITS - Middle
        self.ui.GroupBox_DAT_VITS_InputParams.setTitle(QCA.translate('MainWindow', "输入参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_DAT_VITS_InputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "输入参数")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_AudioSpeakersDataPath,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "音频文件目录/语音识别结果文本路径\n音频文件的所在目录（要求按说话人分类），或者提供由语音识别得到的文本文件。")
            )
        )
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath,
            section = 'Input params',
            option = 'WAV_Dir',
            defaultValue = '',
            setPlaceholderText = True
        )
        self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath.fileButton.clicked.connect(self.setAudioSpeakersDataPath)
        self.ui.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_AudioSpeakersDataPath,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "音频文件目录")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_SRTDir,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "字幕输入目录\n字幕文件的所在目录，字幕文件须与对应音频文件同名且在文本中注明所属语言。")
            )
        )
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.LineEdit_DAT_VITS_SRTDir,
            section = 'Input params',
            option = 'SRT_Dir',
            defaultValue = '',
            setPlaceholderText = True
        )
        self.ui.LineEdit_DAT_VITS_SRTDir.setFileDialog(
            mode = "SelectFolder",
            directory = Path(currentDir).joinpath('语音转录结果', 'Whisper').as_posix()
        )
        self.ui.Button_DAT_VITS_SRTDir_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_SRTDir),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_VITS_SRTDir.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_SRTDir,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "字幕输入目录")
        )

        self.ui.GroupBox_DAT_VITS_VITSParams.setTitle(QCA.translate('MainWindow', "数据集参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_DAT_VITS_VITSParams,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "数据集参数")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_DataFormat,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "数据文本格式\n数据集的文本格式，默认使用VITS的标准。")
            )
        )
        DAT_VITS_DataFormat_Default = '路径|人名|[语言]文本[语言]'
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.LineEdit_DAT_VITS_DataFormat,
            section = 'VITS params',
            option = 'DataFormat_Path',
            defaultValue = DAT_VITS_DataFormat_Default,
            setPlaceholderText = True,
            placeholderText = DAT_VITS_DataFormat_Default
        )
        self.ui.LineEdit_DAT_VITS_DataFormat.textChanged.connect(
            lambda value: (
                MessageBoxBase.pop(self,
                    QMessageBox.Warning, "Warning",
                    "请保留关键词：'路径'，'人名'，'语言'，'文本'",
                ),
                ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_DataFormat),
            ) if not all(Keyword in value for Keyword in ['路径', '人名', '语言', '文本']) else None
        )
        self.ui.Button_DAT_VITS_DataFormat_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_DataFormat),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_VITS_DataFormat.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_DataFormat,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            childItemText = QCA.translate('MainWindow', "数据文本格式")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_AddAuxiliaryData,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "添加辅助数据\n添加用以辅助训练的数据集，若当前语音数据的质量/数量较低则建议启用。")
            )
        )
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.CheckBox_DAT_VITS_AddAuxiliaryData,
            section = 'VITS params',
            option = 'Add_AuxiliaryData',
            defaultValue = False
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_DAT_VITS_AddAuxiliaryData,
            checkedText = "已启用",
            checkedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_DAT_VITS_VITSParams_BasicSettings,
                    [
                        self.ui.Frame_DAT_VITS_AuxiliaryDataPath
                    ],
                    True
                )
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_DAT_VITS_VITSParams_BasicSettings,
                    [
                        self.ui.Frame_DAT_VITS_AuxiliaryDataPath
                    ],
                    False
                )
            ],
            takeEffect = True
        )
        self.ui.Button_DAT_VITS_AddAuxiliaryData_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.CheckBox_DAT_VITS_AddAuxiliaryData)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_AddAuxiliaryData,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            childItemText = QCA.translate('MainWindow', "添加辅助数据")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_AuxiliaryDataPath,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "辅助数据文本路径\n辅助数据集的文本的路径。")
            )
        )
        DAT_VITS_AuxiliaryDataPath_Default = Path(currentDir).joinpath('AuxiliaryData', 'VITS', 'AuxiliaryData.txt').as_posix()
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath,
            section = 'VITS params',
            option = 'AuxiliaryData_Path',
            defaultValue = DAT_VITS_AuxiliaryDataPath_Default,
            setPlaceholderText = True,
            placeholderText = DAT_VITS_AuxiliaryDataPath_Default
        )
        self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath.setFileDialog(
            mode = "SelectFile",
            fileType = "文本类型 (*.csv *.txt)",
            directory = QFunc.normPath(Path(currentDir).joinpath('AuxiliaryData', 'VITS'))
        )
        self.ui.Button_DAT_VITS_AuxiliaryDataPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_AuxiliaryDataPath,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            childItemText = QCA.translate('MainWindow', "辅助数据文本路径")
        )

        self.ui.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_TrainRatio,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "训练集占比\n划分给训练集的数据在数据集中所占的比例。")
            )
        )
        self.ui.DoubleSpinBox_DAT_VITS_TrainRatio.setRange(0.5, 0.9)
        self.ui.DoubleSpinBox_DAT_VITS_TrainRatio.setSingleStep(0.1)
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.DoubleSpinBox_DAT_VITS_TrainRatio,
            section = 'VITS params',
            option = 'TrainRatio',
            defaultValue = 0.7
        )
        self.ui.Button_DAT_VITS_TrainRatio_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.DoubleSpinBox_DAT_VITS_TrainRatio)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_TrainRatio,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            childItemText = QCA.translate('MainWindow', "训练集占比")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_SampleRate,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "采样率 (HZ)\n数据集所要求的音频采样率，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_DAT_VITS_SampleRate.addItems(['22050', '44100', '48000', '96000', '192000', 'None'])
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.ComboBox_DAT_VITS_SampleRate,
            section = 'VITS params',
            option = 'SampleRate',
            defaultValue = 22050
        )
        self.ui.Button_DAT_VITS_SampleRate_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.ComboBox_DAT_VITS_SampleRate)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_SampleRate,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            childItemText = QCA.translate('MainWindow', "采样率")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_SampleWidth,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "采样位数\n数据集所要求的音频采样位数，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_DAT_VITS_SampleWidth.addItems(['8', '16', '24', '32', '32 (Float)', 'None'])
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.ComboBox_DAT_VITS_SampleWidth,
            section = 'VITS params',
            option = 'SampleWidth',
            defaultValue = 16
        )
        self.ui.Button_DAT_VITS_SampleWidth_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.ComboBox_DAT_VITS_SampleWidth)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_SampleWidth,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            childItemText = QCA.translate('MainWindow', "采样位数")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_ToMono,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "合并声道\n将数据集音频的声道合并为单声道。")
            )
        )
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.CheckBox_DAT_VITS_ToMono,
            section = 'VITS params',
            option = 'ToMono',
            defaultValue = True
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_DAT_VITS_ToMono,
            checkedText = "已启用",
            checkedEvents = [
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
            ],
            takeEffect = True
        )
        self.ui.Button_DAT_VITS_ToMono_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.CheckBox_DAT_VITS_ToMono)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_ToMono,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            childItemText = QCA.translate('MainWindow', "合并声道")
        )

        self.ui.GroupBox_DAT_VITS_OutputParams.setTitle(QCA.translate('MainWindow', "输出参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_DAT_VITS_OutputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "输出参数")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_OutputDirName,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "输出目录名\n用于保存最后生成的数据集文件的目录的名字。")
            )
        )
        DAT_VITS_OutputDirName_Default = str(date.today())
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.LineEdit_DAT_VITS_OutputDirName,
            section = 'Output params',
            option = 'Output_Dir_Name',
            defaultValue = '',
            setPlaceholderText = True,
            placeholderText = DAT_VITS_OutputDirName_Default
        )
        self.ui.Button_DAT_VITS_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_OutputDirName),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_VITS_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_OutputDirName,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "输出目录名")
        )

        self.ui.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_FileListNameTraining,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "训练集文本名\n用于保存最后生成的训练集txt文件的名字。")
            )
        )
        DAT_VITS_FileListNameTraining_Default = "Train_" + str(date.today())
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.LineEdit_DAT_VITS_FileListNameTraining,
            section = 'Output params',
            option = 'FileList_Name_Training',
            defaultValue = DAT_VITS_FileListNameTraining_Default,
            setPlaceholderText = True,
            placeholderText = DAT_VITS_FileListNameTraining_Default
        )
        self.ui.Button_DAT_VITS_FileListNameTraining_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_FileListNameTraining),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_VITS_FileListNameTraining.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_FileListNameTraining,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "训练集文本名")
        )

        QFunc.setText(
            widget = self.ui.Label_DAT_VITS_FileListNameValidation,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "验证集文本名\n用于保存最后生成的验证集txt文件的名字。")
            )
        )
        DAT_VITS_FileListNameValidation_Default = "Val_" + str(date.today())
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.LineEdit_DAT_VITS_FileListNameValidation,
            section = 'Output params',
            option = 'FileList_Name_Validation',
            defaultValue = DAT_VITS_FileListNameValidation_Default,
            setPlaceholderText = True,
            placeholderText = DAT_VITS_FileListNameValidation_Default
        )
        self.ui.Button_DAT_VITS_FileListNameValidation_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_FileListNameValidation),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_VITS_FileListNameValidation.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_DAT_VITS_FileListNameValidation,
            treeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "验证集文本名")
        )

        LineEdit_DAT_VITS_OutputDir = LineEditBase()
        self.setDirAlert(
            DirNameEdit = self.ui.LineEdit_DAT_VITS_OutputDirName,
            RootEdit = self.ui.LineEdit_DAT_VITS_OutputRoot,
            DirEdit = LineEdit_DAT_VITS_OutputDir
        )

        LineEdit_DAT_VITS_FileListPathTraining = LineEditBase()
        self.setPathAlert(
            FileNameEdit = self.ui.LineEdit_DAT_VITS_FileListNameTraining,
            DirEdit = LineEdit_DAT_VITS_OutputDir,
            suffix = ".txt",
            FileEdit = LineEdit_DAT_VITS_FileListPathTraining
        )

        LineEdit_DAT_VITS_FileListPathValidation = LineEditBase()
        self.setPathAlert(
            FileNameEdit = self.ui.LineEdit_DAT_VITS_FileListNameValidation,
            DirEdit = LineEdit_DAT_VITS_OutputDir,
            suffix = ".txt",
            FileEdit = LineEdit_DAT_VITS_FileListPathValidation
        )

        # VITS - Right
        MonitorFile_Config_DatasetCreator_VITS = QTasks.MonitorFile(Path_Config_DAT_VITS)
        MonitorFile_Config_DatasetCreator_VITS.start()
        MonitorFile_Config_DatasetCreator_VITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_DAT_VITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_DAT_VITS.setText(QCA.translate('MainWindow', "全部重置"))
        self.ui.Button_ResetSettings_DAT_VITS.clicked.connect(
            lambda: ParamsManager_DAT_VITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_DAT_VITS.setText(QCA.translate('MainWindow', "导入配置"))
        self.ui.Button_ImportSettings_DAT_VITS.clicked.connect(
            lambda: ParamsManager_DAT_VITS.ImportSettings(
                QFunc.getFileDialog(
                    mode = "SelectFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_DAT_VITS.setText(QCA.translate('MainWindow', "导出配置"))
        self.ui.Button_ExportSettings_DAT_VITS.clicked.connect(
            lambda: ParamsManager_DAT_VITS.ExportSettings(
                QFunc.getFileDialog(
                    mode = "SaveFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_CheckOutput_DAT_VITS.setText(QCA.translate('MainWindow', "打开输出目录"))
        Function_SetURL(
            button = self.ui.Button_CheckOutput_DAT_VITS,
            url = self.ui.LineEdit_DAT_VITS_OutputRoot,
            buttonTooltip = "Click to open",
            createIfNotExist = True
        )

        # VITS - Bottom
        self.ui.Button_DAT_VITS_Execute.setText(QCA.translate('MainWindow', "执行数据集制作"))
        self.ui.Button_DAT_VITS_Terminate.setText(QCA.translate('MainWindow', "终止数据集制作"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_DAT_VITS_Execute,
            terminateButton = self.ui.Button_DAT_VITS_Terminate,
            progressBar = self.ui.ProgressBar_DAT_VITS,
            consoleWidget = self.ui.Frame_Console,
            method = Execute_Dataset_Creating_VITS.Execute,
            paramsFrom = [
                self.ui.LineEdit_DAT_VITS_SRTDir,
                self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath,
                self.ui.ComboBox_DAT_VITS_SampleRate,
                self.ui.ComboBox_DAT_VITS_SampleWidth,
                self.ui.CheckBox_DAT_VITS_ToMono,
                self.ui.LineEdit_DAT_VITS_DataFormat,
                self.ui.CheckBox_DAT_VITS_AddAuxiliaryData,
                self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath,
                self.ui.DoubleSpinBox_DAT_VITS_TrainRatio,
                self.ui.LineEdit_DAT_VITS_OutputRoot,
                self.ui.LineEdit_DAT_VITS_OutputDirName,
                self.ui.LineEdit_DAT_VITS_FileListNameTraining,
                self.ui.LineEdit_DAT_VITS_FileListNameValidation
            ],
            emptyAllowed = [
                self.ui.ComboBox_DAT_VITS_SampleRate,
                self.ui.ComboBox_DAT_VITS_SampleWidth,
                self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath
            ],
            successEvents = [
                lambda: self.showMask(True, "正在加载表单"),
                lambda: self.showDATResult(
                    LineEdit_DAT_VITS_FileListPathTraining.text(),
                    LineEdit_DAT_VITS_FileListPathValidation.text()
                ),
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        #############################################################
        ####################### Content: Train ######################
        #############################################################

        # Guidance
        self.ui.Button_VoiceTrainer_Help.clicked.connect(
            lambda: self.showGuidance(
                QCA.translate('MainWindow', "引导（仅出现一次）"),
                [
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Train.png')),
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                [
                    '欢迎来到语音训练工具界面\n该工具用于训练出适用于语音合成的模型文件',
                    '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
                ]
            )
        )

        self.ui.Button_Menu_Train.clicked.connect(
            lambda: (
                self.ui.Button_VoiceTrainer_Help.click(),
                config.editConfig('Dialog', 'GuidanceShown_Train', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_Train', 'False')) is False else None
        )

        # GPT-SoVITS - ParamsManager
        Path_Config_Train_GPTSoVITS = QFunc.normPath(Path(configDir).joinpath('Config_Train_GPT-SoVITS.ini'))
        ParamsManager_Train_GPTSoVITS = ParamsManager(Path_Config_Train_GPTSoVITS)

        # GPT-SoVITS - Top
        self.ui.Button_VoiceTrainer_Title_GPTSoVITS.setText(QCA.translate('MainWindow', "GPT-SoVITS"))
        self.ui.Button_VoiceTrainer_Title_GPTSoVITS.setHorizontal(True)
        self.ui.Button_VoiceTrainer_Title_GPTSoVITS.setChecked(True)
        self.ui.Button_VoiceTrainer_Title_GPTSoVITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Train,
                target = 0
            )
        )

        # GPT-SoVITS - Left
        self.ui.TreeWidget_Catalogue_Train_GPTSoVITS.clear()
        self.ui.TreeWidget_Catalogue_Train_GPTSoVITS.setHeaderHidden(True)

        # GPT-SoVITS - Midlle
        self.ui.GroupBox_Train_GPTSoVITS_InputParams.setTitle(QCA.translate('MainWindow', "输入参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_Train_GPTSoVITS_InputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输入参数")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_GPTSoVITS_FileListPath,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "训练集文本路径\n用于提供训练集音频路径及其语音内容的训练集txt文件的路径。")
            )
        )
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_Train_GPTSoVITS_FileListPath,
            section = 'Input params',
            option = 'FileList_Path',
            defaultValue = '',
            setPlaceholderText = True
        )
        self.ui.LineEdit_Train_GPTSoVITS_FileListPath.setFileDialog(
            mode = "SelectFile",
            fileType = "txt类型 (*.txt)",
            directory = Path(currentDir).joinpath('数据集制作结果', 'GPT-SoVITS').as_posix()
        )
        self.ui.Button_Train_GPTSoVITS_FileListPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_FileListPath),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_GPTSoVITS_FileListPath.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_GPTSoVITS_FileListPath,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "训练集文本路径")
        )

        self.ui.GroupBox_Train_GPTSoVITS_GPTSoVITSParams.setTitle(QCA.translate('MainWindow', "训练参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_Train_GPTSoVITS_GPTSoVITSParams,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "训练参数")
        )

        '''
        QFunc.setText(
            widget = self.ui.Label_Train_GPTSoVITS_Epochs,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "s1迭代轮数\n将全部样本完整迭代一轮的次数。")
            )
        )
        self.ui.SpinBox_Train_GPTSoVITS_S1Epochs.setRange(1, 100)
        self.ui.SpinBox_Train_GPTSoVITS_S1Epochs.setSingleStep(1)
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.SpinBox_Train_GPTSoVITS_S1Epochs,
            section = 'GPT-SoVITS params',
            option = 'Epochs',
            defaultValue = 8
        )
        self.ui.Button_Train_GPTSoVITS_S1Epochs_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.SpinBox_Train_GPTSoVITS_S1Epochs)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_GPTSoVITS_Epochs,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "s1迭代轮数")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_GPTSoVITS_S2Epochs,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "s2迭代轮数\n将全部样本完整迭代一轮的次数。")
            )
        )
        self.ui.SpinBox_Train_GPTSoVITS_S2Epochs.setRange(1, 100)
        self.ui.SpinBox_Train_GPTSoVITS_S2Epochs.setSingleStep(1)
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.SpinBox_Train_GPTSoVITS_S2Epochs,
            section = 'GPT-SoVITS params',
            option = 'Epochs',
            defaultValue = 15
        )
        self.ui.Button_Train_GPTSoVITS_S2Epochs_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.SpinBox_Train_GPTSoVITS_S2Epochs)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_GPTSoVITS_S2Epochs,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "s2迭代轮数")
        )
        '''

        QFunc.setText(
            widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS1,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "预训练s1模型路径\n预训练s1模型的路径。")
            )
        )
        Train_GPTSoVITS_ModelPathPretrainedS1_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's1bert25hz-5kh-longer-epoch=12-step=369668.ckpt').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1,
            section = 'GPT-SoVITS params',
            option = 'Model_Path_Pretrained_s1',
            defaultValue = Train_GPTSoVITS_ModelPathPretrainedS1_Default,
            setPlaceholderText = True,
            placeholderText = Train_GPTSoVITS_ModelPathPretrainedS1_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1.setFileDialog(
            mode = "SelectFile",
            fileType = "ckpt类型 (*.ckpt)",
            directory = QFunc.normPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2'))
        )
        self.ui.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS1,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "预训练s1模型路径")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS2G,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "预训练s2G模型路径\n预训练s2G模型的路径。")
            )
        )
        Train_GPTSoVITS_ModelPathPretrainedS2G_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2G2333k.pth').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G,
            section = 'GPT-SoVITS params',
            option = 'Model_Path_Pretrained_s2G',
            defaultValue = Train_GPTSoVITS_ModelPathPretrainedS2G_Default,
            setPlaceholderText = True,
            placeholderText = Train_GPTSoVITS_ModelPathPretrainedS2G_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G.setFileDialog(
            mode = "SelectFile",
            fileType = "pth类型 (*.pth)",
            directory = QFunc.normPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2'))
        )
        self.ui.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS2G,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "预训练s2G模型路径")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS2D,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "预训练s2D模型路径\n预训练s2D模型的路径。")
            )
        )
        Train_GPTSoVITS_ModelPathPretrainedS2D_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2D2333k.pth').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D,
            section = 'GPT-SoVITS params',
            option = 'Model_Path_Pretrained_s2D',
            defaultValue = Train_GPTSoVITS_ModelPathPretrainedS2D_Default,
            setPlaceholderText = True,
            placeholderText = Train_GPTSoVITS_ModelPathPretrainedS2D_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D.setFileDialog(
            mode = "SelectFile",
            fileType = "pth类型 (*.pth)",
            directory = QFunc.normPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2'))
        )
        self.ui.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS2D,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "预训练s2D模型路径")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_GPTSoVITS_ModelDirPretrainedBert,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "预训练bert模型路径\n预训练bert模型（文件夹）的路径。")
            )
        )
        Train_GPTSoVITS_ModelDirPretrainedBert_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-roberta-wwm-ext-large').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert,
            section = 'GPT-SoVITS params',
            option = 'Model_Dir_Pretrained_bert',
            defaultValue = Train_GPTSoVITS_ModelDirPretrainedBert_Default,
            setPlaceholderText = True,
            placeholderText = Train_GPTSoVITS_ModelDirPretrainedBert_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded'))
        )
        self.ui.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_GPTSoVITS_ModelDirPretrainedBert,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "预训练bert模型路径")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_GPTSoVITS_ModelDirPretrainedSSL,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "预训练ssl模型路径\n预训练ssl模型（文件夹）的路径。")
            )
        )
        Train_GPTSoVITS_ModelDirPretrainedSSL_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-hubert-base').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL,
            section = 'GPT-SoVITS params',
            option = 'Model_Dir_Pretrained_ssl',
            defaultValue = Train_GPTSoVITS_ModelDirPretrainedSSL_Default,
            setPlaceholderText = True,
            placeholderText = Train_GPTSoVITS_ModelDirPretrainedSSL_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded'))
        )
        self.ui.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_GPTSoVITS_ModelDirPretrainedSSL,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "预训练ssl模型路径")
        )

        self.ui.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_Train_GPTSoVITS_FP16Run,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "半精度训练\n通过混合了float16精度的训练方式减小显存占用。")
            )
        )
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.CheckBox_Train_GPTSoVITS_FP16Run,
            section = 'GPT-SoVITS params',
            option = 'FP16_Run',
            defaultValue = False
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Train_GPTSoVITS_FP16Run,
            checkedText = "已启用",
            checkedEvents = [
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
            ],
            takeEffect = True
        )
        self.ui.Button_Train_GPTSoVITS_FP16Run_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.CheckBox_Train_GPTSoVITS_FP16Run)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_GPTSoVITS_FP16Run,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "半精度训练")
        )

        self.ui.GroupBox_Train_GPTSoVITS_OutputParams.setTitle(QCA.translate('MainWindow', "输出参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_Train_GPTSoVITS_OutputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输出参数")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_GPTSoVITS_OutputDirName,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "输出目录名\n存放训练所得模型的目录的名字。")
            )
        )
        Train_GPTSoVITS_OutputDirName_Default = str(date.today())
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_Train_GPTSoVITS_OutputDirName,
            section = 'Output params',
            option = 'Output_Dir_Name',
            defaultValue = '',
            setPlaceholderText = True,
            placeholderText = Train_GPTSoVITS_OutputDirName_Default
        )
        self.ui.Button_Train_GPTSoVITS_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_OutputDirName),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_GPTSoVITS_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.LineEdit_Train_GPTSoVITS_OutputDirName,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "输出目录名")
        )

        self.ui.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_Train_GPTSoVITS_LogDir,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "日志输出目录\n训练时生成的日志的存放目录。")
            )
        )
        Train_GPTSoVITS_LogDir_Default = Path(Path(currentDir).root).joinpath('EVT_TrainLog', 'GPT-SoVITS', str(date.today())).as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_Train_GPTSoVITS_LogDir,
            section = 'Output params',
            option = 'Output_LogDir',
            defaultValue = Train_GPTSoVITS_LogDir_Default,
            setPlaceholderText = True,
            placeholderText = Train_GPTSoVITS_LogDir_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_LogDir.textChanged.connect(
            lambda value: (
                MessageBoxBase.pop(self,
                    QMessageBox.Warning, "Warning",
                    "保存路径不支持非ASCII字符，请使用英文路径以避免训练报错",
                ),
                self.ui.LineEdit_Train_GPTSoVITS_LogDir.clear()
            ) if not all(Char.isascii() for Char in value) else None
        )
        self.ui.LineEdit_Train_GPTSoVITS_LogDir.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(Train_GPTSoVITS_LogDir_Default).parent)
        )
        self.ui.Button_Train_GPTSoVITS_LogDir_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_LogDir),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_GPTSoVITS_LogDir.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_GPTSoVITS_LogDir,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "日志输出目录")
        )

        LineEdit_Train_GPTSoVITS_OutputDir = LineEditBase()
        self.setDirAlert(
            DirNameEdit = self.ui.LineEdit_Train_GPTSoVITS_OutputDirName,
            RootEdit = self.ui.LineEdit_Train_GPTSoVITS_OutputRoot,
            DirEdit = LineEdit_Train_GPTSoVITS_OutputDir
        )

        # GPT-SoVITS - Right
        MonitorFile_Config_VoiceTrainer_GPTSoVITS = QTasks.MonitorFile(Path_Config_Train_GPTSoVITS)
        MonitorFile_Config_VoiceTrainer_GPTSoVITS.start()
        MonitorFile_Config_VoiceTrainer_GPTSoVITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Train_GPTSoVITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_Train_GPTSoVITS.setText(QCA.translate('MainWindow', "全部重置"))
        self.ui.Button_ResetSettings_Train_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_Train_GPTSoVITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_Train_GPTSoVITS.setText(QCA.translate('MainWindow', "导入配置"))
        self.ui.Button_ImportSettings_Train_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_Train_GPTSoVITS.ImportSettings(
                QFunc.getFileDialog(
                    mode = "SelectFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_Train_GPTSoVITS.setText(QCA.translate('MainWindow', "导出配置"))
        self.ui.Button_ExportSettings_Train_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_Train_GPTSoVITS.ExportSettings(
                QFunc.getFileDialog(
                    mode = "SaveFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_RunTensorboard_Train_GPTSoVITS.setText(QCA.translate('MainWindow', "启动Tensorboard"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_RunTensorboard_Train_GPTSoVITS,
            method = Tensorboard_Runner.Execute,
            paramsFrom = [
                self.ui.LineEdit_Train_GPTSoVITS_LogDir
            ]
        )

        self.ui.Button_CheckOutput_Train_GPTSoVITS.setText(QCA.translate('MainWindow', "打开输出目录"))
        Function_SetURL(
            button = self.ui.Button_CheckOutput_Train_GPTSoVITS,
            url = self.ui.LineEdit_Train_GPTSoVITS_OutputRoot,
            buttonTooltip = "Click to open",
            createIfNotExist = True
        )

        # GPT-SoVITS - Bottom
        self.ui.Button_Train_GPTSoVITS_Execute.setText(QCA.translate('MainWindow', "执行模型训练"))
        self.ui.Button_Train_GPTSoVITS_Terminate.setText(QCA.translate('MainWindow', "终止模型训练"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_Train_GPTSoVITS_Execute,
            terminateButton = self.ui.Button_Train_GPTSoVITS_Terminate,
            progressBar = self.ui.ProgressBar_Train_GPTSoVITS,
            consoleWidget = self.ui.Frame_Console,
            method = Execute_Voice_Training_GPTSoVITS.Execute,
            paramsFrom = [
                self.ui.LineEdit_Train_GPTSoVITS_FileListPath,
                #self.ui.SpinBox_Train_GPTSoVITS_S1Epochs,
                #self.ui.SpinBox_Train_GPTSoVITS_S1SaveInterval,
                #self.ui.SpinBox_Train_GPTSoVITS_S2Epochs,
                #self.ui.SpinBox_Train_GPTSoVITS_S2SaveInterval,
                #self.ui.SpinBox_Train_GPTSoVITS_BatchSize,
                self.ui.CheckBox_Train_GPTSoVITS_FP16Run,
                self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert,
                self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL,
                self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1,
                self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G,
                self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D,
                self.ui.LineEdit_Train_GPTSoVITS_OutputRoot,
                self.ui.LineEdit_Train_GPTSoVITS_OutputDirName,
                self.ui.LineEdit_Train_GPTSoVITS_LogDir
            ],
            successEvents = [
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )
        FunctionSignals.Signal_TaskStatus.connect(
            lambda Task, Status: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "是否稍后启用tensorboard？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {QMessageBox.Yes: lambda: self.ui.Button_RunTensorboard_Train_GPTSoVITS.click()}
            ) if Task == 'Execute_Voice_Training_GPTSoVITS.Execute' and Status == 'Started' else None
        )

        # VITS - ParamsManager
        Path_Config_Train_VITS = QFunc.normPath(Path(configDir).joinpath('Config_Train_VITS.ini'))
        ParamsManager_Train_VITS = ParamsManager(Path_Config_Train_VITS)

        # VITS - Top
        self.ui.Button_VoiceTrainer_Title_VITS.setText(QCA.translate('MainWindow', "VITS2"))
        self.ui.Button_VoiceTrainer_Title_VITS.setHorizontal(True)
        self.ui.Button_VoiceTrainer_Title_VITS.setChecked(False)
        self.ui.Button_VoiceTrainer_Title_VITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Train,
                target = 1
            )
        )

        # VITS - Left
        self.ui.TreeWidget_Catalogue_Train_VITS.clear()
        self.ui.TreeWidget_Catalogue_Train_VITS.setHeaderHidden(True)

        # VITS - Midlle
        self.ui.GroupBox_Train_VITS_InputParams.setTitle(QCA.translate('MainWindow', "输入参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_Train_VITS_InputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "输入参数")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_FileListPathTraining,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "训练集文本路径\n用于提供训练集音频路径及其语音内容的训练集txt文件的路径。")
            )
        )
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.LineEdit_Train_VITS_FileListPathTraining,
            section = 'Input params',
            option = 'FileList_Path_Training',
            defaultValue = '',
            setPlaceholderText = True
        )
        self.ui.LineEdit_Train_VITS_FileListPathTraining.setFileDialog(
            mode = "SelectFile",
            fileType = "txt类型 (*.txt)",
            directory = Path(currentDir).joinpath('数据集制作结果', 'VITS').as_posix()
        )
        self.ui.Button_Train_VITS_FileListPathTraining_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_FileListPathTraining),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_VITS_FileListPathTraining.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_FileListPathTraining,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "训练集文本路径")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_FileListPathValidation,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "验证集文本路径\n用于提供验证集音频路径及其语音内容的验证集txt文件的路径。")
            )
        )
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.LineEdit_Train_VITS_FileListPathValidation,
            section = 'Input params',
            option = 'FileList_Path_Validation',
            defaultValue = '',
            setPlaceholderText = True
        )
        self.ui.LineEdit_Train_VITS_FileListPathValidation.setFileDialog(
            mode = "SelectFile",
            fileType = "txt类型 (*.txt)",
            directory = Path(currentDir).joinpath('数据集制作结果', 'VITS').as_posix()
        )
        self.ui.Button_Train_VITS_FileListPathValidation_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_FileListPathValidation),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_VITS_FileListPathValidation.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_FileListPathValidation,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "验证集文本路径")
        )

        self.ui.GroupBox_Train_VITS_VITSParams.setTitle(QCA.translate('MainWindow', "训练参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_Train_VITS_VITSParams,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "训练参数")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_Epochs,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "迭代轮数\n将全部样本完整迭代一轮的次数。")
            )
        )
        self.ui.SpinBox_Train_VITS_Epochs.setRange(10, 100000)
        self.ui.SpinBox_Train_VITS_Epochs.setSingleStep(1)
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.SpinBox_Train_VITS_Epochs,
            section = 'VITS params',
            option = 'Epochs',
            defaultValue = 1000
        )
        self.ui.Button_Train_VITS_Epochs_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.SpinBox_Train_VITS_Epochs)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_Epochs,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "迭代轮数")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_BatchSize,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "批处理量\n每轮迭代中单位批次的样本数量，需根据GPU的性能调节该值。")
            )
        )
        self.ui.SpinBox_Train_VITS_BatchSize.setRange(2, 128)
        self.ui.SpinBox_Train_VITS_BatchSize.setSingleStep(1)
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.SpinBox_Train_VITS_BatchSize,
            section = 'VITS params',
            option = 'Batch_Size',
            defaultValue = 4
        )
        self.ui.SpinBox_Train_VITS_BatchSize.setToolTip(QCA.translate('MainWindow', "建议：2~4G: 2\n6~8G: 4\n10~12G: 8\n14~16G: 16"))
        self.ui.Button_Train_VITS_BatchSize_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.SpinBox_Train_VITS_BatchSize)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_BatchSize,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "批处理量")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_UsePretrainedModels,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "使用预训练模型\n使用预训练模型（底模），其载入优先级高于检查点。")
            )
        )
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.CheckBox_Train_VITS_UsePretrainedModels,
            section = 'VITS params',
            option = 'Use_PretrainedModels',
            defaultValue = True
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Train_VITS_UsePretrainedModels,
            checkedText = "已启用",
            checkedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_Train_VITS_VITSParams_BasicSettings,
                    [
                        self.ui.Frame_Train_VITS_ModelPathPretrainedG,
                        self.ui.Frame_Train_VITS_ModelPathPretrainedD,
                        self.ui.Frame_Train_VITS_KeepOriginalSpeakers,
                        self.ui.Frame_Train_VITS_ConfigPathLoad if self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers.isChecked() else None
                    ],
                    True
                )
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_Train_VITS_VITSParams_BasicSettings,
                    [
                        self.ui.Frame_Train_VITS_ModelPathPretrainedG,
                        self.ui.Frame_Train_VITS_ModelPathPretrainedD,
                        self.ui.Frame_Train_VITS_KeepOriginalSpeakers,
                        self.ui.Frame_Train_VITS_ConfigPathLoad
                    ],
                    False
                )
            ],
            takeEffect = True
        )
        self.ui.Button_Train_VITS_UsePretrainedModels_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.CheckBox_Train_VITS_UsePretrainedModels)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_UsePretrainedModels,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "使用预训练模型")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_ModelPathPretrainedG,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "预训练G模型路径\n预训练生成器（Generator）模型的路径。")
            )
        )
        Train_VITS_ModelPathPretrainedG_Default = Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_G.pth').as_posix()
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.LineEdit_Train_VITS_ModelPathPretrainedG,
            section = 'VITS params',
            option = 'Model_Path_Pretrained_G',
            defaultValue = Train_VITS_ModelPathPretrainedG_Default,
            setPlaceholderText = True,
            placeholderText = Train_VITS_ModelPathPretrainedG_Default
        )
        self.ui.LineEdit_Train_VITS_ModelPathPretrainedG.setFileDialog(
            mode = "SelectFile",
            fileType = "pth类型 (*.pth)",
            directory = QFunc.normPath(Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded'))
        )
        self.ui.Button_Train_VITS_ModelPathPretrainedG_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_ModelPathPretrainedG),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_VITS_ModelPathPretrainedG.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_ModelPathPretrainedG,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "预训练G模型路径")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_ModelPathPretrainedD,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "预训练D模型路径\n预训练判别器（Discriminator）模型的路径。")
            )
        )
        Train_VITS_ModelPathPretrainedD_Default = Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_D.pth').as_posix()
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.LineEdit_Train_VITS_ModelPathPretrainedD,
            section = 'VITS params',
            option = 'Model_Path_Pretrained_D',
            defaultValue = Train_VITS_ModelPathPretrainedD_Default,
            setPlaceholderText = True,
            placeholderText = Train_VITS_ModelPathPretrainedD_Default
        )
        self.ui.LineEdit_Train_VITS_ModelPathPretrainedD.setFileDialog(
            mode = "SelectFile",
            fileType = "pth类型 (*.pth)",
            directory = QFunc.normPath(Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded'))
        )
        self.ui.Button_Train_VITS_ModelPathPretrainedD_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_ModelPathPretrainedD),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_VITS_ModelPathPretrainedD.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_ModelPathPretrainedD,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "预训练D模型路径")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_KeepOriginalSpeakers,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "保留原说话人（实验性）\n保留预训练模型中原有的说话人。")
            )
        )
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers,
            section = 'VITS params',
            option = 'Keep_Original_Speakers',
            defaultValue = False
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers,
            checkedText = "已启用",
            checkedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_Train_VITS_VITSParams_BasicSettings,
                    [
                        self.ui.Frame_Train_VITS_ConfigPathLoad
                    ],
                    True
                )
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_Train_VITS_VITSParams_BasicSettings,
                    [
                        self.ui.Frame_Train_VITS_ConfigPathLoad
                    ],
                    False
                )
            ],
            takeEffect = True
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers,
            checkedEvents = [
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Question, "Tip",
                    text = """
                        开启该实验性功能需要注意以下几点：
                        1. 为防止老角色的音色在训练过程中被逐渐遗忘，请保证每个原角色至少有一两条音频参与训练。\n
                        2. 为防止老角色的顺序被重组（导致音色混乱），请在下方设置包含了底模角色信息的配置文件路径。
                    """,
                    buttons = QMessageBox.Yes|QMessageBox.No,
                    buttonEvents = {QMessageBox.No: lambda: self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers.setChecked(False)}
                )
            ],
            takeEffect = False
        )
        self.ui.Button_Train_VITS_KeepOriginalSpeakers_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_KeepOriginalSpeakers,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "保留原说话人")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_ConfigPathLoad,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "配置加载路径\n用于加载底模人物信息的配置文件的路径")
            )
        )
        Train_VITS_ConfigPathLoad_Default = Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_Config.json').as_posix()
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.LineEdit_Train_VITS_ConfigPathLoad,
            section = 'VITS params',
            option = 'Config_Path_Load',
            defaultValue = Train_VITS_ConfigPathLoad_Default,
            setPlaceholderText = True,
            placeholderText = Train_VITS_ConfigPathLoad_Default
        )
        self.ui.LineEdit_Train_VITS_ConfigPathLoad.setFileDialog(
            mode = "SelectFile",
            fileType = "json类型 (*.json)",
            directory = QFunc.normPath(Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded'))
        )
        self.ui.Button_Train_VITS_ConfigPathLoad_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_ConfigPathLoad),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_VITS_ConfigPathLoad.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_ConfigPathLoad,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "配置加载路径")
        )

        self.ui.ToolBox_Train_VITS_VITSParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_Train_VITS_VITSParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_NumWorkers,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "进程数量\n进行数据加载时可并行的进程数量，需根据CPU的性能调节该值。")
            )
        )
        self.ui.SpinBox_Train_VITS_NumWorkers.setRange(2, 128)
        self.ui.SpinBox_Train_VITS_NumWorkers.setSingleStep(2)
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.SpinBox_Train_VITS_NumWorkers,
            section = 'VITS params',
            option = 'Num_Workers',
            defaultValue = 4
        )
        self.ui.Button_Train_VITS_NumWorkers_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.SpinBox_Train_VITS_NumWorkers)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_NumWorkers,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "进程数量")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_FP16Run,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "半精度训练\n通过混合了float16精度的训练方式减小显存占用以支持更大的批处理量。")
            )
        )
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.CheckBox_Train_VITS_FP16Run,
            section = 'VITS params',
            option = 'FP16_Run',
            defaultValue = False
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Train_VITS_FP16Run,
            checkedText = "已启用",
            checkedEvents = [
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
            ],
            takeEffect = True
        )
        self.ui.Button_Train_VITS_FP16Run_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.CheckBox_Train_VITS_FP16Run)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_FP16Run,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            childItemText = QCA.translate('MainWindow', "半精度训练")
        )

        self.ui.GroupBox_Train_VITS_OutputParams.setTitle(QCA.translate('MainWindow', "输出参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_Train_VITS_OutputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "输出参数")
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_EvalInterval,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "保存间隔\n每次保存模型所间隔的步数。PS: 步数 ≈ 迭代轮次 * 训练样本数 / 批处理量")
            )
        )
        self.ui.SpinBox_Train_VITS_EvalInterval.setRange(10, 100000)
        self.ui.SpinBox_Train_VITS_EvalInterval.setSingleStep(1)
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.SpinBox_Train_VITS_EvalInterval,
            section = 'Output params',
            option = 'Eval_Interval',
            defaultValue = 1000
        )
        self.ui.SpinBox_Train_VITS_EvalInterval.setToolTip(QCA.translate('MainWindow', "提示：设置过小可能导致磁盘占用激增哦"))
        self.ui.Button_Train_VITS_EvalInterval_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.SpinBox_Train_VITS_EvalInterval)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_EvalInterval,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "保存间隔")
        )

        self.ui.ToolBox_Train_VITS_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_Train_VITS_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_OutputDirName,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "输出目录名\n存放训练所得模型的目录的名字，若目录中已存在模型则会将其视为检查点。")
            )
        )
        Train_VITS_OutputDirName_Default = str(date.today())
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.LineEdit_Train_VITS_OutputDirName,
            section = 'Output params',
            option = 'Output_Dir_Name',
            defaultValue = '',
            setPlaceholderText = True,
            placeholderText = Train_VITS_OutputDirName_Default
        )
        self.ui.Button_Train_VITS_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_OutputDirName),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_VITS_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_OutputDirName,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "输出目录名")
        )

        LineEdit_Train_VITS_OutputDir = LineEditBase()
        self.setDirAlert(
            DirNameEdit = self.ui.LineEdit_Train_VITS_OutputDirName,
            RootEdit = self.ui.LineEdit_Train_VITS_OutputRoot,
            DirEdit = LineEdit_Train_VITS_OutputDir
        )

        QFunc.setText(
            widget = self.ui.Label_Train_VITS_LogDir,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "日志输出目录\n训练时生成的日志的存放目录。")
            )
        )
        Train_VITS_LogDir_Default = Path(Path(currentDir).root).joinpath('EVT_TrainLog', 'VITS', str(date.today())).as_posix()
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.LineEdit_Train_VITS_LogDir,
            section = 'Output params',
            option = 'Output_LogDir',
            defaultValue = Train_VITS_LogDir_Default,
            setPlaceholderText = True,
            placeholderText = Train_VITS_LogDir_Default
        )
        self.ui.LineEdit_Train_VITS_LogDir.textChanged.connect(
            lambda value: (
                MessageBoxBase.pop(self,
                    QMessageBox.Warning, "Warning",
                    text = "保存路径不支持非ASCII字符，请使用英文路径以避免训练报错",
                ),
                self.ui.LineEdit_Train_VITS_LogDir.clear()
            ) if not all(Char.isascii() for Char in value) else None
        )
        self.ui.LineEdit_Train_VITS_LogDir.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(Train_VITS_LogDir_Default).parent)
        )
        self.ui.Button_Train_VITS_LogDir_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_LogDir),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_VITS_LogDir.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_Train_VITS_LogDir,
            treeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            childItemText = QCA.translate('MainWindow', "日志输出目录")
        )

        # VITS - Right
        MonitorFile_Config_VoiceTrainer_VITS = QTasks.MonitorFile(Path_Config_Train_VITS)
        MonitorFile_Config_VoiceTrainer_VITS.start()
        MonitorFile_Config_VoiceTrainer_VITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Train_VITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_Train_VITS.setText(QCA.translate('MainWindow', "全部重置"))
        self.ui.Button_ResetSettings_Train_VITS.clicked.connect(
            lambda: ParamsManager_Train_VITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_Train_VITS.setText(QCA.translate('MainWindow', "导入配置"))
        self.ui.Button_ImportSettings_Train_VITS.clicked.connect(
            lambda: ParamsManager_Train_VITS.ImportSettings(
                QFunc.getFileDialog(
                    mode = "SelectFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_Train_VITS.setText(QCA.translate('MainWindow', "导出配置"))
        self.ui.Button_ExportSettings_Train_VITS.clicked.connect(
            lambda: ParamsManager_Train_VITS.ExportSettings(
                QFunc.getFileDialog(
                    mode = "SaveFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_RunTensorboard_Train_VITS.setText(QCA.translate('MainWindow', "启动Tensorboard"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_RunTensorboard_Train_VITS,
            method = Tensorboard_Runner.Execute,
            paramsFrom = [
                self.ui.LineEdit_Train_VITS_LogDir
            ]
        )

        self.ui.Button_CheckOutput_Train_VITS.setText(QCA.translate('MainWindow', "打开输出目录"))
        Function_SetURL(
            button = self.ui.Button_CheckOutput_Train_VITS,
            url = self.ui.LineEdit_Train_VITS_OutputRoot,
            buttonTooltip = "Click to open",
            createIfNotExist = True
        )

        # VITS - Bottom
        self.ui.Button_Train_VITS_Execute.setText(QCA.translate('MainWindow', "执行模型训练"))
        self.ui.Button_Train_VITS_Terminate.setText(QCA.translate('MainWindow', "终止模型训练"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_Train_VITS_Execute,
            terminateButton = self.ui.Button_Train_VITS_Terminate,
            progressBar = self.ui.ProgressBar_Train_VITS,
            consoleWidget = self.ui.Frame_Console,
            method = Execute_Voice_Training_VITS.Execute,
            paramsFrom = [
                self.ui.LineEdit_Train_VITS_FileListPathTraining,
                self.ui.LineEdit_Train_VITS_FileListPathValidation,
                self.ui.SpinBox_Train_VITS_Epochs,
                self.ui.SpinBox_Train_VITS_EvalInterval,
                self.ui.SpinBox_Train_VITS_BatchSize,
                self.ui.CheckBox_Train_VITS_FP16Run,
                self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers,
                self.ui.LineEdit_Train_VITS_ConfigPathLoad,
                self.ui.SpinBox_Train_VITS_NumWorkers,
                self.ui.CheckBox_Train_VITS_UsePretrainedModels,
                self.ui.LineEdit_Train_VITS_ModelPathPretrainedG,
                self.ui.LineEdit_Train_VITS_ModelPathPretrainedD,
                self.ui.LineEdit_Train_VITS_OutputRoot,
                self.ui.LineEdit_Train_VITS_OutputDirName,
                'config.json',
                self.ui.LineEdit_Train_VITS_LogDir
            ],
            emptyAllowed = [
                self.ui.LineEdit_Train_VITS_ConfigPathLoad,
                self.ui.LineEdit_Train_VITS_ModelPathPretrainedG,
                self.ui.LineEdit_Train_VITS_ModelPathPretrainedD
            ],
            successEvents = [
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )
        FunctionSignals.Signal_TaskStatus.connect(
            lambda Task, Status: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "是否稍后启用tensorboard？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {QMessageBox.Yes: lambda: self.ui.Button_RunTensorboard_Train_VITS.click()}
            ) if Task == 'Execute_Voice_Training_VITS.Execute' and Status == 'Started' else None
        )

        #############################################################
        ######################## Content: TTS #######################
        #############################################################

        # Guidance
        self.ui.Button_VoiceConverter_Help.clicked.connect(
            lambda: self.showGuidance(
                QCA.translate('MainWindow', "引导（仅出现一次）"),
                [
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_TTS.png')),
                    QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                [
                    '欢迎来到语音合成工具界面\n该工具用于将文字转为语音，用户需要提供相应的模型和配置文件',
                    '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
                ]
            )
        )

        self.ui.Button_Menu_TTS.clicked.connect(
            lambda: (
                self.ui.Button_VoiceConverter_Help.click(),
                config.editConfig('Dialog', 'GuidanceShown_TTS', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_TTS', 'False')) is False else None
        )

        # GPT-SoVITS - ParamsManager
        Path_Config_TTS_GPTSoVITS = QFunc.normPath(Path(configDir).joinpath('Config_TTS_GPT-SoVITS.ini'))
        ParamsManager_TTS_GPTSoVITS = ParamsManager(Path_Config_TTS_GPTSoVITS)

        # GPT-SoVITS - Top
        self.ui.Button_VoiceConverter_Title_GPTSoVITS.setText(QCA.translate('MainWindow', "GPT-SoVITS"))
        self.ui.Button_VoiceConverter_Title_GPTSoVITS.setHorizontal(True)
        self.ui.Button_VoiceConverter_Title_GPTSoVITS.setChecked(True)
        self.ui.Button_VoiceConverter_Title_GPTSoVITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_TTS,
                target = 0
            )
        )

        # GPT-SoVITS - Left
        self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS.clear()
        self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS.setHeaderHidden(True)

        # GPT-SoVTIS - Middle
        self.ui.GroupBox_TTS_GPTSoVITS_InputParams.setTitle(QCA.translate('MainWindow', "输入参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_TTS_GPTSoVITS_InputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输入参数")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_GPTSoVITS_ModelPathLoadS1,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "s1模型加载路径\ns1模型的路径。")
            )
        )
        TTS_GPTSoVITS_ModelPathLoadS1_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's1bert25hz-5kh-longer-epoch=12-step=369668.ckpt').as_posix()
        ParamsManager_TTS_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1,
            section = 'Input params',
            option = 'Model_Path_Load_s1',
            defaultValue = TTS_GPTSoVITS_ModelPathLoadS1_Default,
            setPlaceholderText = True,
            placeholderText = TTS_GPTSoVITS_ModelPathLoadS1_Default
        )
        self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1.setFileDialog(
            mode = "SelectFile",
            fileType = "ckpt类型 (*.ckpt)",
            directory = Path(currentDir).joinpath('模型训练结果', 'GPT-SoVITS').as_posix()
        )
        self.ui.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_GPTSoVITS.ResetParam(self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_GPTSoVITS_ModelPathLoadS1,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "s1模型加载路径")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_GPTSoVITS_ModelPathLoadS2G,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "s2G模型加载路径\ns2G模型的路径。")
            )
        )
        TTS_GPTSoVITS_ModelPathLoadS2G_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2G2333k.pth').as_posix()
        ParamsManager_TTS_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G,
            section = 'Input params',
            option = 'Model_Path_Load_s2G',
            defaultValue = TTS_GPTSoVITS_ModelPathLoadS2G_Default,
            setPlaceholderText = True,
            placeholderText = TTS_GPTSoVITS_ModelPathLoadS2G_Default
        )
        self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G.setFileDialog(
            mode = "SelectFile",
            fileType = "pth类型 (*.pth)",
            directory = Path(currentDir).joinpath('模型训练结果', 'GPT-SoVITS').as_posix()
        )
        self.ui.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_GPTSoVITS.ResetParam(self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_GPTSoVITS_ModelPathLoadS2G,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "s2G模型加载路径")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_GPTSoVITS_ModelDirLoadBert,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "预训练bert模型加载路径\n预训练bert模型（文件夹）的路径。")
            )
        )
        TTS_GPTSoVITS_ModelDirLoadBert_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-roberta-wwm-ext-large').as_posix()
        ParamsManager_TTS_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert,
            section = 'Input params',
            option = 'Model_Dir_Load_bert',
            defaultValue = TTS_GPTSoVITS_ModelDirLoadBert_Default,
            setPlaceholderText = True,
            placeholderText = TTS_GPTSoVITS_ModelDirLoadBert_Default
        )
        self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded'))
        )
        self.ui.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_GPTSoVITS.ResetParam(self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_GPTSoVITS_ModelDirLoadBert,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "预训练bert模型加载路径")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_GPTSoVITS_ModelDirLoadSSL,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "预训练ssl模型加载路径\n预训练ssl模型的路径。")
            )
        )
        TTS_GPTSoVITS_ModelDirLoadSSL_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-hubert-base').as_posix()
        ParamsManager_TTS_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL,
            section = 'Input params',
            option = 'Model_Dir_Load_ssl',
            defaultValue = TTS_GPTSoVITS_ModelDirLoadSSL_Default,
            setPlaceholderText = True,
            placeholderText = TTS_GPTSoVITS_ModelDirLoadSSL_Default
        )
        self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded'))
        )
        self.ui.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_GPTSoVITS.ResetParam(self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_GPTSoVITS_ModelDirLoadSSL,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "预训练ssl模型加载路径")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_GPTSoVITS_UseWebUI,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "使用WebUI界面\n开启后会使用WebUI界面而非GUI窗口。")
            )
        )
        ParamsManager_TTS_GPTSoVITS.SetParam(
            widget = self.ui.CheckBox_TTS_GPTSoVITS_UseWebUI,
            section = 'Input params',
            option = 'Use_WebUI',
            defaultValue = True
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_TTS_GPTSoVITS_UseWebUI,
            checkedText = "已启用",
            checkedEvents = [
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
            ],
            takeEffect = True
        )
        self.ui.Button_TTS_GPTSoVITS_UseWebUI_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_GPTSoVITS.ResetParam(self.ui.CheckBox_TTS_GPTSoVITS_UseWebUI)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_GPTSoVITS_UseWebUI,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "使用WebUI界面")
        )

        # GPT-SoVITS - Right
        MonitorFile_Config_VoiceConverter_GPTSoVITS = QTasks.MonitorFile(Path_Config_TTS_GPTSoVITS)
        MonitorFile_Config_VoiceConverter_GPTSoVITS.start()
        MonitorFile_Config_VoiceConverter_GPTSoVITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_TTS_GPTSoVITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_TTS_GPTSoVITS.setText(QCA.translate('MainWindow', "全部重置"))
        self.ui.Button_ResetSettings_TTS_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_TTS_GPTSoVITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_TTS_GPTSoVITS.setText(QCA.translate('MainWindow', "导入配置"))
        self.ui.Button_ImportSettings_TTS_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_TTS_GPTSoVITS.ImportSettings(
                QFunc.getFileDialog(
                    mode = "SelectFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_TTS_GPTSoVITS.setText(QCA.translate('MainWindow', "导出配置"))
        self.ui.Button_ExportSettings_TTS_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_TTS_GPTSoVITS.ExportSettings(
                QFunc.getFileDialog(
                    mode = "SaveFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        # GPT-SoVITS - Bottom
        self.ui.Button_TTS_GPTSoVITS_Execute.setText(QCA.translate('MainWindow', "执行语音合成"))
        self.ui.Button_TTS_GPTSoVITS_Terminate.setText(QCA.translate('MainWindow', "终止语音合成"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_TTS_GPTSoVITS_Execute,
            terminateButton = self.ui.Button_TTS_GPTSoVITS_Terminate,
            progressBar = self.ui.ProgressBar_TTS_GPTSoVITS,
            consoleWidget = self.ui.Frame_Console,
            method = Execute_Voice_Converting_GPTSoVITS.Execute,
            paramsFrom = [
                self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1,
                self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G,
                self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert,
                self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL,
                False, # Set_FP16_Run
                False, # Enable_Batched_Infer
                self.ui.CheckBox_TTS_GPTSoVITS_UseWebUI,
            ],
            emptyAllowed = [
            ],
            successEvents = [
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        # VITS - ParamsManager
        Path_Config_TTS_VITS = QFunc.normPath(Path(configDir).joinpath('Config_TTS_VITS.ini'))
        ParamsManager_TTS_VITS = ParamsManager(Path_Config_TTS_VITS)

        # VITS - Top
        self.ui.Button_VoiceConverter_Title_VITS.setText(QCA.translate('MainWindow', "VITS2"))
        self.ui.Button_VoiceConverter_Title_VITS.setHorizontal(True)
        self.ui.Button_VoiceConverter_Title_VITS.setChecked(False)
        self.ui.Button_VoiceConverter_Title_VITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_TTS,
                target = 1
            )
        )

        # VITS - Left
        self.ui.TreeWidget_Catalogue_TTS_VITS.clear()
        self.ui.TreeWidget_Catalogue_TTS_VITS.setHeaderHidden(True)

        # VTIS - Middle
        self.ui.GroupBox_TTS_VITS_InputParams.setTitle(QCA.translate('MainWindow', "输入参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_TTS_VITS_InputParams,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            rootItemText = QCA.translate('MainWindow', "输入参数")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_VITS_ConfigPathLoad,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "配置加载路径\n用于推理的配置文件的路径。")
            )
        )
        TTS_VITS_ConfigPathLoad_Default = Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_Config.json').as_posix()
        ParamsManager_TTS_VITS.SetParam(
            widget = self.ui.LineEdit_TTS_VITS_ConfigPathLoad,
            section = 'Input params',
            option = 'Config_Path_Load',
            defaultValue = '',
            setPlaceholderText = True,
            placeholderText = TTS_VITS_ConfigPathLoad_Default
        )
        self.ui.LineEdit_TTS_VITS_ConfigPathLoad.textChanged.connect(
            lambda Path: (
                self.ui.ComboBox_TTS_VITS_Speaker.clear(),
                self.ui.ComboBox_TTS_VITS_Speaker.addItems(Get_Speakers(Path))
            )
        )
        self.ui.LineEdit_TTS_VITS_ConfigPathLoad.setFileDialog(
            mode = "SelectFile",
            fileType = "json类型 (*.json)",
            directory = Path(currentDir).joinpath('模型训练结果', 'VITS').as_posix()
        )
        self.ui.Button_TTS_VITS_ConfigPathLoad_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.LineEdit_TTS_VITS_ConfigPathLoad),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_TTS_VITS_ConfigPathLoad.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_VITS_ConfigPathLoad,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "配置加载路径")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_VITS_ModelPathLoad,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "G模型加载路径\n用于推理的生成器（Generator）模型的路径。")
            )
        )
        TTS_VITS_ModelPathLoad_Default = Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_G.pth').as_posix()
        ParamsManager_TTS_VITS.SetParam(
            widget = self.ui.LineEdit_TTS_VITS_ModelPathLoad,
            section = 'Input params',
            option = 'Model_Path_Load',
            defaultValue = '',
            setPlaceholderText = True,
            placeholderText = TTS_VITS_ModelPathLoad_Default
        )
        self.ui.LineEdit_TTS_VITS_ModelPathLoad.setFileDialog(
            mode = "SelectFile",
            fileType = "pth类型 (*.pth)",
            directory = Path(currentDir).joinpath('模型训练结果', 'VITS').as_posix()
        )
        self.ui.Button_TTS_VITS_ModelPathLoad_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.LineEdit_TTS_VITS_ModelPathLoad),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_TTS_VITS_ModelPathLoad.text())
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_VITS_ModelPathLoad,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            childItemText = QCA.translate('MainWindow', "G模型加载路径")
        )

        self.ui.GroupBox_TTS_VITS_VITSParams.setTitle(QCA.translate('MainWindow', "语音合成参数"))
        Function_AddToTreeWidget(
            widget = self.ui.GroupBox_TTS_VITS_VITSParams,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            rootItemText = QCA.translate('MainWindow', "语音合成参数")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_VITS_Text,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "输入文字\n输入的文字会作为说话人的语音内容。")
            )
        )
        ParamsManager_TTS_VITS.SetParam(
            widget = self.ui.PlainTextEdit_TTS_VITS_Text,
            section = 'VITS params',
            option = 'text',
            defaultValue = '',
            setPlaceholderText = True,
            placeholderText = '请输入语句'
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_VITS_Text,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            childItemText = QCA.translate('MainWindow', "输入文字")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_VITS_Language,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "所属语言\n文字所属的语言，若使用自动检测则保持'None'即可（有概率报错）。")
            )
        )
        self.ui.ComboBox_TTS_VITS_Language.addItems(['None', QCA.translate('MainWindow', '中'), QCA.translate('MainWindow', '英'), QCA.translate('MainWindow', '日')])
        ParamsManager_TTS_VITS.SetParam(
            widget = self.ui.ComboBox_TTS_VITS_Language,
            section = 'VITS params',
            option = 'Language',
            defaultValue = None
        )
        self.ui.Button_TTS_VITS_Language_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.ComboBox_TTS_VITS_Language)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_VITS_Language,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            childItemText = QCA.translate('MainWindow', "所属语言")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_VITS_Speaker,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "人物名字\n说话人物的名字。")
            )
        )
        self.ui.ComboBox_TTS_VITS_Speaker.addItems(
            Get_Speakers(self.ui.LineEdit_TTS_VITS_ConfigPathLoad.text())
        )
        ParamsManager_TTS_VITS.SetParam(
            widget = self.ui.ComboBox_TTS_VITS_Speaker,
            section = 'VITS params',
            option = 'Speaker',
            defaultValue = ''
        )
        self.ui.ComboBox_TTS_VITS_Speaker.setCurrentIndex(0)
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_VITS_Speaker,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            childItemText = QCA.translate('MainWindow', "人物名字")
        )

        self.ui.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.widget(0).setText(QCA.translate('MainWindow', "高级设置"))
        self.ui.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.widget(0).collapse()

        QFunc.setText(
            widget = self.ui.Label_TTS_VITS_EmotionStrength,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "情感强度\n情感的变化程度。")
            )
        )
        self.ui.HorizontalSlider_TTS_VITS_EmotionStrength.setRange(0, 1)
        self.ui.HorizontalSlider_TTS_VITS_EmotionStrength.setSingleStep(0.01)
        ParamsManager_TTS_VITS.SetParam(
            widget = self.ui.HorizontalSlider_TTS_VITS_EmotionStrength,
            section = 'VITS params',
            option = 'EmotionStrength',
            defaultValue = 0.67
        )
        self.ui.Button_TTS_VITS_EmotionStrength_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.HorizontalSlider_TTS_VITS_EmotionStrength)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_VITS_EmotionStrength,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            childItemText = QCA.translate('MainWindow', "情感强度")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_VITS_PhonemeDuration,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "音素音长\n音素的发音长度。")
            )
        )
        self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration.setRange(0, 1)
        self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration.setSingleStep(0.1)
        ParamsManager_TTS_VITS.SetParam(
            widget = self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration,
            section = 'VITS params',
            option = 'PhonemeDuration',
            defaultValue = 0.8
        )
        self.ui.Button_TTS_VITS_PhonemeDuration_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_VITS_PhonemeDuration,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            childItemText = QCA.translate('MainWindow', "音素音长")
        )

        QFunc.setText(
            widget = self.ui.Label_TTS_VITS_SpeechRate,
            text = QFunc.setRichText(
                QCA.translate('MainWindow', "整体语速\n整体的说话速度。")
            )
        )
        self.ui.HorizontalSlider_TTS_VITS_SpeechRate.setRange(0, 20)
        self.ui.HorizontalSlider_TTS_VITS_SpeechRate.setSingleStep(1)
        ParamsManager_TTS_VITS.SetParam(
            widget = self.ui.HorizontalSlider_TTS_VITS_SpeechRate,
            section = 'VITS params',
            option = 'SpeechRate',
            defaultValue = 1.
        )
        self.ui.Button_TTS_VITS_SpeechRate_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.HorizontalSlider_TTS_VITS_SpeechRate)
            }
        )
        Function_AddToTreeWidget(
            widget = self.ui.Label_TTS_VITS_SpeechRate,
            treeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            childItemText = QCA.translate('MainWindow', "整体语速")
        )

        TTS_VITS_AudioDirSave = Path(currentDir).joinpath('语音合成结果', 'VITS').as_posix()
        TTS_VITS_AudioPathSave = Path(TTS_VITS_AudioDirSave).joinpath("temp.wav").as_posix()
        os.makedirs(TTS_VITS_AudioDirSave) if not Path(TTS_VITS_AudioDirSave).exists() else None

        # VITS - Right
        MonitorFile_Config_VoiceConverter_VITS = QTasks.MonitorFile(Path_Config_TTS_VITS)
        MonitorFile_Config_VoiceConverter_VITS.start()
        MonitorFile_Config_VoiceConverter_VITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_TTS_VITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_TTS_VITS.setText(QCA.translate('MainWindow', "全部重置"))
        self.ui.Button_ResetSettings_TTS_VITS.clicked.connect(
            lambda: ParamsManager_TTS_VITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_TTS_VITS.setText(QCA.translate('MainWindow', "导入配置"))
        self.ui.Button_ImportSettings_TTS_VITS.clicked.connect(
            lambda: ParamsManager_TTS_VITS.ImportSettings(
                QFunc.getFileDialog(
                    mode = "SelectFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_TTS_VITS.setText(QCA.translate('MainWindow', "导出配置"))
        self.ui.Button_ExportSettings_TTS_VITS.clicked.connect(
            lambda: ParamsManager_TTS_VITS.ExportSettings(
                QFunc.getFileDialog(
                    mode = "SaveFile",
                    fileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_CheckOutput_TTS_VITS.setText(QCA.translate('MainWindow', "查看输出文件"))
        Function_SetURL(
            button = self.ui.Button_CheckOutput_TTS_VITS,
            url = TTS_VITS_AudioDirSave,
            buttonTooltip = "Click to open",
            createIfNotExist = True
        )

        # VITS - Bottom
        self.ui.Button_TTS_VITS_Execute.setText(QCA.translate('MainWindow', "执行语音合成"))
        self.ui.Button_TTS_VITS_Terminate.setText(QCA.translate('MainWindow', "终止语音合成"))
        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_TTS_VITS_Execute,
            terminateButton = self.ui.Button_TTS_VITS_Terminate,
            progressBar = self.ui.ProgressBar_TTS_VITS,
            consoleWidget = self.ui.Frame_Console,
            method = Execute_Voice_Converting_VITS.Execute,
            paramsFrom = [
                self.ui.LineEdit_TTS_VITS_ConfigPathLoad,
                self.ui.LineEdit_TTS_VITS_ModelPathLoad,
                self.ui.PlainTextEdit_TTS_VITS_Text,
                self.ui.ComboBox_TTS_VITS_Language,
                self.ui.ComboBox_TTS_VITS_Speaker,
                self.ui.HorizontalSlider_TTS_VITS_EmotionStrength,
                self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration,
                self.ui.HorizontalSlider_TTS_VITS_SpeechRate,
                TTS_VITS_AudioPathSave
            ],
            emptyAllowed = [
                self.ui.ComboBox_TTS_VITS_Language,
                self.ui.ComboBox_TTS_VITS_Speaker
            ],
            successEvents = [
                lambda: self.showMask(True, "正在加载播放器"),
                lambda: self.showTTSResult(
                    TTS_VITS_AudioPathSave
                ),
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        #############################################################
        ##################### Content: Settings #####################
        #############################################################

        # Client
        self.ui.Button_Settings_Title_Client.setText(QCA.translate('MainWindow', "系统选项"))
        self.ui.Button_Settings_Title_Client.setHorizontal(True)
        self.ui.Button_Settings_Title_Client.setChecked(True)
        self.ui.Button_Settings_Title_Client.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Settings,
                target = 0
            )
        )

        self.ui.GroupBox_Settings_Client_Outlook.setTitle(QCA.translate('MainWindow', "外观设置"))

        self.ui.Label_Setting_Theme.setText(QCA.translate('MainWindow', "主题"))
        self.ui.ComboBox_Setting_Theme.addItems([QCA.translate('MainWindow', '跟随系统'), QCA.translate('MainWindow', '亮色'), QCA.translate('MainWindow', '暗色')])
        ThemeDict = {
            '跟随系统': Theme.Auto,
            '亮色': Theme.Light,
            '暗色': Theme.Dark
        }
        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.ui.ComboBox_Setting_Theme.setCurrentText(
                QCA.translate('MainWindow', QFunc.findKey(ThemeDict, Theme))
            )
        )
        self.ui.ComboBox_Setting_Theme.currentIndexChanged.connect(
            lambda: (
                config.editConfig(
                    'Settings', 'Theme', ThemeDict.get(self.ui.ComboBox_Setting_Theme.currentText())
                ),
                ComponentsSignals.Signal_SetTheme.emit(
                    ThemeDict.get(self.ui.ComboBox_Setting_Theme.currentText())
                ) if EasyTheme.THEME != ThemeDict.get(self.ui.ComboBox_Setting_Theme.currentText()) else None
            )
        )

        self.ui.Label_Setting_Language.setText(QCA.translate('MainWindow', "语言"))
        self.ui.ComboBox_Setting_Language.addItems([QCA.translate('MainWindow', '跟随系统'), QCA.translate('MainWindow', '中文'), QCA.translate('MainWindow', '英文')])
        LanguageDict = {
            '跟随系统': Language.Auto,
            '中文': Language.ZH,
            '英文': Language.EN
        }
        ComponentsSignals.Signal_SetLanguage.connect(
            lambda Language: self.ui.ComboBox_Setting_Language.setCurrentText(
                QCA.translate('MainWindow', QFunc.findKey(LanguageDict, Language))
            )
        )
        self.ui.ComboBox_Setting_Language.currentIndexChanged.connect(
            lambda: (
                config.editConfig(
                    'Settings', 'Language', LanguageDict.get(self.ui.ComboBox_Setting_Language.currentText())
                ),
                ComponentsSignals.Signal_SetLanguage.emit(
                    LanguageDict.get(self.ui.ComboBox_Setting_Language.currentText())
                ) if EasyLanguage.LANG != LanguageDict.get(self.ui.ComboBox_Setting_Language.currentText()) else None
            )
        )

        self.ui.GroupBox_Settings_Client_Function.setTitle(QCA.translate('MainWindow', "功能设置"))

        self.ui.Label_Setting_AutoUpdate.setText(QCA.translate('MainWindow', "自动检查版本并更新"))
        self.ui.CheckBox_Setting_AutoUpdate.setChecked(
            {
                'Enabled': True,
                'Disabled': False
            }.get(config.getValue('Settings', 'AutoUpdate', 'Enabled'))
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Setting_AutoUpdate,
            checkedText = "已启用",
            checkedEvents = [
                lambda: config.editConfig('Settings', 'AutoUpdate', 'Enabled'),
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
                lambda: config.editConfig('Settings', 'AutoUpdate', 'Disabled')
            ],
            takeEffect = True
        )

        self.ui.GroupBox_Settings_Client_Operation.setTitle(QCA.translate('MainWindow', "操作"))

        Function_SetMethodExecutor(self,
            executeButton = self.ui.Button_Setting_IntegrityChecker,
            method = Integrity_Checker.Execute,
            params = ()
        )
        FunctionSignals.Signal_TaskStatus.connect(
            lambda Task, Status: self.ui.Button_Setting_IntegrityChecker.setCheckable(
                False if Status == 'Started' else True
            )
        )
        self.ui.Button_Setting_IntegrityChecker.setText(QCA.translate('MainWindow', "检查完整性"))
        self.ui.Button_Setting_IntegrityChecker.setToolTip(QCA.translate('MainWindow', "检查文件完整性"))

        # Tools
        self.ui.Button_Settings_Title_Tools.setText(QCA.translate('MainWindow', "工具选项"))
        self.ui.Button_Settings_Title_Tools.setHorizontal(True)
        self.ui.Button_Settings_Title_Tools.setChecked(False)
        self.ui.Button_Settings_Title_Tools.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Settings,
                target = 1
            )
        )

        self.ui.GroupBox_Settings_Tools_Function.setTitle(QCA.translate('MainWindow', "功能设置"))

        self.ui.Label_Setting_AutoReset.setText(QCA.translate('MainWindow', "启动时重置所有工具的参数设置"))
        self.ui.CheckBox_Setting_AutoReset.setChecked(
            {
                'Enabled': True,
                'Disabled': False
            }.get(config.getValue('Tools', 'AutoReset', 'Enabled'))
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Setting_AutoReset,
            checkedText = "已启用",
            checkedEvents = [
                lambda: config.editConfig('Tools', 'AutoReset', 'Enabled'),
                lambda: MainWindowSignals.Signal_MainWindowShown.connect(
                    lambda: (
                        ParamsManager_Process.ResetSettings(),
                        ParamsManager_VPR_TDNN.ResetSettings(),
                        ParamsManager_ASR_Whisper.ResetSettings(),
                        ParamsManager_DAT_GPTSoVITS.ResetSettings(),
                        ParamsManager_DAT_VITS.ResetSettings(),
                        ParamsManager_Train_GPTSoVITS.ResetSettings(),
                        ParamsManager_Train_VITS.ResetSettings(),
                        ParamsManager_TTS_GPTSoVITS.ResetSettings(),
                        ParamsManager_TTS_VITS.ResetSettings()
                    )
                )
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
                lambda: config.editConfig('Tools', 'AutoReset', 'Disabled'),
            ],
            takeEffect = True
        )

        self.ui.Label_Setting_Synchronizer.setText(QCA.translate('MainWindow', "自动关联前后工具的部分参数设置"))
        self.ui.CheckBox_Setting_Synchronizer.setChecked(
            {
                'Enabled': True,
                'Disabled': False
            }.get(config.getValue('Tools', 'Synchronizer', 'Enabled'))
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Setting_Synchronizer,
            checkedText = "已启用",
            checkedEvents = [
                lambda: config.editConfig('Tools', 'Synchronizer', 'Enabled'),
                lambda: Function_ParamsSynchronizer(
                    LineEdit_Process_OutputDir,
                    {LineEdit_Process_OutputDir: self.ui.LineEdit_VPR_TDNN_AudioDirInput}
                ),
                lambda: Function_ParamsSynchronizer(
                    LineEdit_VPR_TDNN_AudioSpeakersDataPath,
                    {LineEdit_VPR_TDNN_AudioSpeakersDataPath: [self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath, self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath]}
                ),
                lambda: Function_ParamsSynchronizer(
                    LineEdit_VPR_TDNN_OutputDir,
                    {LineEdit_VPR_TDNN_OutputDir: self.ui.LineEdit_ASR_Whisper_AudioDir}
                ),
                lambda: Function_ParamsSynchronizer(
                    LineEdit_ASR_Whisper_OutputDir,
                    {LineEdit_ASR_Whisper_OutputDir: [self.ui.LineEdit_DAT_GPTSoVITS_SRTDir, self.ui.LineEdit_DAT_VITS_SRTDir]}
                ),
                lambda: Function_ParamsSynchronizer(
                    LineEdit_DAT_GPTSoVITS_FileListPath,
                    {LineEdit_DAT_GPTSoVITS_FileListPath: self.ui.LineEdit_Train_GPTSoVITS_FileListPath}
                ),
                lambda: Function_ParamsSynchronizer(
                    [LineEdit_DAT_VITS_FileListPathTraining, LineEdit_DAT_VITS_FileListPathValidation],
                    {LineEdit_DAT_VITS_FileListPathTraining: self.ui.LineEdit_Train_VITS_FileListPathTraining, LineEdit_DAT_VITS_FileListPathValidation: self.ui.LineEdit_Train_VITS_FileListPathValidation}
                )
            ],
            uncheckedText = "未启用",
            uncheckedEvents = [
                lambda: config.editConfig('Tools', 'Synchronizer', 'Disabled'),
            ],
            takeEffect = True
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Setting_Synchronizer,
            uncheckedEvents = [
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "该设置将于重启之后生效"
                )
            ],
            takeEffect = False
        )

        self.ui.GroupBox_Settings_Tools_Path.setTitle(QCA.translate('MainWindow', "路径设置"))

        self.ui.Label_Process_OutputRoot.setText(QCA.translate('MainWindow', "音频处理输出目录"))
        Process_OutputRoot_Default = Path(OutputDir).joinpath('音频处理结果').as_posix()
        ParamsManager_Process.SetParam(
            widget = self.ui.LineEdit_Process_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = Process_OutputRoot_Default,
            setPlaceholderText = True,
            placeholderText = Process_OutputRoot_Default
        )
        self.ui.LineEdit_Process_OutputRoot.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(Process_OutputRoot_Default).parent)
        )
        self.ui.Button_Process_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.LineEdit_Process_OutputRoot)
            }
        )

        self.ui.Label_VPR_TDNN_OutputRoot.setText(QCA.translate('MainWindow', "声纹识别结果输出目录"))
        VPR_TDNN_AudioSpeakersDataRoot_Default = Path(currentDir).joinpath('语音识别结果', 'VPR').as_posix()
        ParamsManager_VPR_TDNN.SetParam(
            widget = self.ui.LineEdit_VPR_TDNN_OutputRoot,
            section = 'Output params',
            option = 'Audio_Root_Output',
            defaultValue = VPR_TDNN_AudioSpeakersDataRoot_Default,
            setPlaceholderText = True,
            placeholderText = VPR_TDNN_AudioSpeakersDataRoot_Default
        )
        self.ui.LineEdit_VPR_TDNN_OutputRoot.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(VPR_TDNN_AudioSpeakersDataRoot_Default).parent)
        )
        self.ui.Button_VPR_TDNN_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_VPR_TDNN.ResetParam(self.ui.LineEdit_VPR_TDNN_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_VPR_TDNN_OutputRoot.text())
            }
        )

        self.ui.Label_ASR_Whisper_OutputRoot.setText(QCA.translate('MainWindow', "Whisper转录输出目录"))
        ASR_Whisper_OutputRoot_Default = Path(OutputDir).joinpath('语音转录结果', 'Whisper').as_posix()
        ParamsManager_ASR_Whisper.SetParam(
            widget = self.ui.LineEdit_ASR_Whisper_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = ASR_Whisper_OutputRoot_Default,
            setPlaceholderText = True,
            placeholderText = ASR_Whisper_OutputRoot_Default
        )
        self.ui.LineEdit_ASR_Whisper_OutputRoot.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(ASR_Whisper_OutputRoot_Default).parent)
        )
        self.ui.Button_ASR_Whisper_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_Whisper.ResetParam(self.ui.LineEdit_ASR_Whisper_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_ASR_Whisper_OutputRoot.text())
            }
        )

        self.ui.Label_DAT_GPTSoVITS_OutputRoot.setText( QCA.translate('MainWindow', "GPTSoVITS数据集输出目录"))
        DAT_GPTSoVITS_OutputRoot_Default = Path(OutputDir).joinpath('数据集制作结果', 'GPT-SoVITS').as_posix()
        ParamsManager_DAT_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = DAT_GPTSoVITS_OutputRoot_Default,
            setPlaceholderText = True,
            placeholderText = DAT_GPTSoVITS_OutputRoot_Default
        )
        self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(DAT_GPTSoVITS_OutputRoot_Default).parent)
        )
        self.ui.Button_DAT_GPTSoVITS_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot.text())
            }
        )

        self.ui.Label_DAT_VITS_OutputRoot.setText(QCA.translate('MainWindow', "VITS数据集输出目录"))
        DAT_VITS_OutputRoot_Default = Path(OutputDir).joinpath('数据集制作结果', 'VITS').as_posix()
        ParamsManager_DAT_VITS.SetParam(
            widget = self.ui.LineEdit_DAT_VITS_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = DAT_VITS_OutputRoot_Default,
            setPlaceholderText = True,
            placeholderText = DAT_VITS_OutputRoot_Default
        )
        self.ui.LineEdit_DAT_VITS_OutputRoot.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(DAT_VITS_OutputRoot_Default).parent)
        )
        self.ui.Button_DAT_VITS_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_VITS_OutputRoot.text())
            }
        )

        self.ui.Label_Train_GPTSoVITS_OutputRoot.setText(QCA.translate('MainWindow', "GPTSoVITS训练输出目录"))
        Train_GPTSoVITS_OutputRoot_Default = Path(OutputDir).joinpath('模型训练结果', 'GPT-SoVITS').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            widget = self.ui.LineEdit_Train_GPTSoVITS_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = Train_GPTSoVITS_OutputRoot_Default,
            setPlaceholderText = True,
            placeholderText = Train_GPTSoVITS_OutputRoot_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_OutputRoot.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(Train_GPTSoVITS_OutputRoot_Default).parent)
        )
        self.ui.Button_Train_GPTSoVITS_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_GPTSoVITS_OutputRoot.text())
            }
        )

        self.ui.Label_Train_VITS_OutputRoot.setText(QCA.translate('MainWindow', "VITS训练输出目录"))
        Train_VITS_OutputRoot_Default = Path(OutputDir).joinpath('模型训练结果', 'VITS').as_posix()
        ParamsManager_Train_VITS.SetParam(
            widget = self.ui.LineEdit_Train_VITS_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = Train_VITS_OutputRoot_Default,
            setPlaceholderText = True,
            placeholderText = Train_VITS_OutputRoot_Default
        )
        self.ui.LineEdit_Train_VITS_OutputRoot.setFileDialog(
            mode = "SelectFolder",
            directory = QFunc.normPath(Path(Train_VITS_OutputRoot_Default).parent)
        )
        self.ui.Button_Train_VITS_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_VITS_OutputRoot.text())
            }
        )

        #############################################################
        ####################### Content: Info #######################
        #############################################################

        self.ui.Button_Info_Title.setText(QCA.translate('MainWindow', "用户须知"))

        QFunc.setText(
            widget = self.ui.TextBrowser_Text_Info,
            text = QFunc.richTextManager().addTitle(
                text = QCA.translate('MainWindow', "声明"),
                align = "left",
                size = 24,
                weight = 840
            ).addBody(
                text = QCA.translate('MainWindow',
                    """
                    请自行解决数据集的授权问题。对于使用未经授权的数据集进行训练所导致的任何问题，您将承担全部责任，并且该仓库及其维护者不承担任何后果！

                    您还需要服从以下条例：
                    0. 本项目仅用于学术交流目的，旨在促进沟通和学习。不适用于生产环境。
                    1. 基于 Easy Voice Toolkit 发布的任何视频必须在描述中明确指出它们用于变声，并指定声音或音频的输入源，例如使用他人发布的视频或音频，并将分离出的人声作为转换的输入源，必须提供清晰的原始视频链接。如果您使用自己的声音或其他商业语音合成软件生成的声音作为转换的输入源，也必须在描述中说明。
                    2. 您将对输入源引起的任何侵权问题负全部责任。当使用其他商业语音合成软件作为输入源时，请确保遵守该软件的使用条款。请注意，许多语音合成引擎在其使用条款中明确声明不能用于输入源转换。
                    3. 继续使用本项目被视为同意本仓库 README 中所述的相关条款。本仓库的 README 有义务进行劝导，但不承担可能出现的任何后续问题的责任。
                    4. 如果您分发此仓库的代码或将由此项目生成的任何结果公开发布（包括但不限于视频分享平台），请注明原始作者和代码来源（即此仓库）。
                    5. 如果您将此项目用于任何其他计划，请提前与本仓库的作者联系并告知。
                    """
                ),
                align = "left",
                size = 12,
                weight = 420,
                lineHeight = 27
            ).richText()
        )

        #############################################################
        ###################### Content: Console #####################
        #############################################################

        self.ui.Button_Console_Title.setText(QCA.translate('MainWindow', "终端"))

        MonitorLog = QTasks.MonitorLogFile(logPath)
        MonitorLog.start()
        MonitorLog.Signal_ConsoleInfo.connect(
            lambda Info: (
                self.ui.PlainTextEdit_Console.setPlainText(Info),
                self.ui.PlainTextEdit_Console.moveCursor(QTextCursor.End)
            )
        )

        self.ui.Button_Console_Copy.clicked.connect(
            lambda: (
                QApplication.clipboard().setText(self.ui.PlainTextEdit_Console.toPlainText()),
                MessageBoxBase.pop(self, windowTitle = "Tip", text = "已复制输出日志到剪切板")
            )
        )

        self.ui.Button_Console_Clear.clicked.connect(MonitorLog.clear)

        self.ui.Button_Console_Fold.clicked.connect(self.ui.Button_Toggle_Console.click)

        #############################################################
        ######################### StatusBar #########################
        #############################################################

        # Toggle Console
        self.ui.Button_Toggle_Console.setToolTip(QCA.translate('MainWindow', "点击以展开/折叠终端"))
        self.ui.Button_Toggle_Console.clicked.connect(
            lambda: Function_AnimateFrame(
                frame = self.ui.Frame_Console,
                minHeight = 0,
                maxHeight = 210,
                supportSplitter = True
            )
        )
        self.ui.Frame_Console.setFixedHeight(0)

        # Display ToolsStatus
        self.ui.Label_ToolsStatus.clear()
        FunctionSignals.Signal_TaskStatus.connect(
            lambda Task, Status: self.ui.Label_ToolsStatus.setText(
                f"工具状态：{'忙碌' if Status == 'Started' else '空闲'}"
            ) if Task in [
                'Execute_Audio_Processing.Execute',
                'Execute_Voice_Identifying_VPR.Execute',
                'Execute_Voice_Transcribing_Whisper.Execute',
                'Execute_Dataset_Creating_VITS.Execute',
                'Execute_Voice_Training_VITS.Execute',
                'Execute_Voice_Converting_VITS.Execute'
            ] else None
        )

        # Display Usage
        self.MonitorUsage.Signal_UsageInfo.connect(
            lambda Usage_CPU, Usage_GPU: (
                self.ui.Label_Usage_CPU.setText(f"CPU: {Usage_CPU}"),
                self.ui.Label_Usage_GPU.setText(f"GPU: {Usage_GPU}")
            )
        )

        # Display Version
        self.ui.Label_Version.setText(currentVersion)

        # Set Theme
        ComponentsSignals.Signal_SetTheme.emit(config.getValue('Settings', 'Theme', Theme.Auto))

        # Set Language
        ComponentsSignals.Signal_SetLanguage.emit(config.getValue('Settings', 'Language', Language.Auto))

        # Show MainWindow (and emit signal)
        self.show()
        MainWindowSignals.Signal_MainWindowShown.emit()

##############################################################################################################################

if __name__ == "__main__":
    App = QApplication(sys.argv)

    # Create&Show SplashScreen
    SC = QSplashScreen(QPixmap(QFunc.normPath(Path(resourceDir).joinpath('assets/images/others/SplashScreen.png'))))
    #SC.showMessage('Loading...', alignment = Qt.AlignmentFlag.AlignCenter)
    SC.show()

    # Init&Show MainWindow
    MW = MainWindow()
    MW.main()

    # Close SplashScreen
    SC.finish(MW) #SC.close()

    sys.exit(App.exec())

##############################################################################################################################