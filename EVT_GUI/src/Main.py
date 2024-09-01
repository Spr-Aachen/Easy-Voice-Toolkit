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
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets import QTasks
from QEasyWidgets import ComponentsSignals, Theme, EasyTheme, Language, EasyLanguage, TranslationBase, IconBase

from windows.Windows import *
from Functions import *
from EnvConfigurator import *
from Config import *

##############################################################################################################################

# Change working directory to current directory
os.chdir(CurrentDir)


# Parse path settings
parser = argparse.ArgumentParser()
parser.add_argument("--core",         help = "dir of core files",        default = Path(ResourceDir).joinpath('EVT_Core'))
parser.add_argument("--manifest",     help = "path to manifest.json",    default = Path(ResourceDir).joinpath('manifest.json'))
parser.add_argument("--requirements", help = "path to requirements.txt", default = Path(ResourceDir).joinpath('requirements.txt'))
parser.add_argument("--dependencies", help = "dir of dependencies",      default = Path(CurrentDir).joinpath(''))
parser.add_argument("--models",       help = "dir of models",            default = Path(CurrentDir).joinpath('Models'))
parser.add_argument("--output",       help = "dir of output",            default = Path(CurrentDir).joinpath(''))
args = parser.parse_args()

CoreDir = args.core
ManifestPath = args.manifest
RequirementsPath = args.requirements
DependencyDir = args.dependencies
ModelDir = args.models
OutputDir = args.output


# Set up client config
Config = QFunc.ManageConfig(ConfigPath)
Config.EditConfig('Info', 'CurrentVersion', str(CurrentVersion))
Config.EditConfig('Info', 'ExecuterName', str(QFunc.GetFileInfo()[0]))


# Set up environment variables while python file is not compiled
if IsFileCompiled == False:
    QFunc.SetEnvVar( # Redirect PATH variable 'QT_QPA_PLATFORM_PLUGIN_PATH' to Pyside6 '/plugins/platforms' folder's path
        Variable = 'QT_QPA_PLATFORM_PLUGIN_PATH',
        Value = QFunc.NormPath(Path(QFunc.GetBaseDir(PySide6_File)).joinpath('plugins', 'platforms'))
    )
# Set up environment variables while environment is configured
if Path(DependencyDir).joinpath('Aria2').exists():
    QFunc.SetEnvVar(
        Variable = 'PATH',
        Value = QFunc.NormPath(Path(DependencyDir).joinpath('Aria2'))
    )
if Path(DependencyDir).joinpath('FFmpeg').exists():
    QFunc.SetEnvVar(
        Variable = 'PATH',
        Value = QFunc.NormPath(Path(DependencyDir).joinpath('FFmpeg', 'bin'))
    )
if Path(DependencyDir).joinpath('Python').exists():
    QFunc.SetEnvVar(
        Variable = 'PATH',
        Value = QFunc.NormPath(Path(DependencyDir).joinpath('Python'), TrailingSlash = True)
    )
    QFunc.SetEnvVar(
        Variable = 'PATH',
        Value = QFunc.NormPath(Path(DependencyDir).joinpath('Python', 'Scripts'), TrailingSlash = True)
    )

##############################################################################################################################

def UpdaterExecuter():
    '''
    Execute updater
    '''
    if Config.GetValue('Settings', 'AutoUpdate', 'Enabled') == 'Enabled':
        subprocess.Popen(['python.exe', QFunc.NormPath(Path(CurrentDir).joinpath('Updater.py'))] if IsFileCompiled == False else [QFunc.NormPath(Path(CurrentDir).joinpath('Updater.exe'))], env = os.environ)
        QApplication.exit()
        os._exit(0) if IsFileCompiled == True else None

##############################################################################################################################

# Tools: AudioProcessor
class Execute_Audio_Processing(QObject):
    '''
    Change media format to WAV (and denoise) and cut off the silent parts
    '''
    started = Signal()
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        CMD = QFunc.SubprocessManager(CommunicateThroughConsole = True)
        self.Process = CMD.create(
            Args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from Process.Process import Audio_Processing; '
                f"AudioConvertandSlice = Audio_Processing{str(Params)}; "
                'AudioConvertandSlice.Process_Audio()"'
            ]
        )
        Output, Error = CMD.monitor(
            ShowProgress = True,
            DecodeResult = True,
            LogPath = LogPath
        )[:2]
        if 'error' in str(Error).lower():
            pass
        elif 'traceback' in str(Output).lower():
            Error = "出错了，详情请见终端输出信息"
        else:
            Error = None

        self.finished.emit(str(Error))

    def Terminate(self):
        QFunc.ProcessTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceIdentifier
class Execute_Voice_Identifying_VPR(QObject):
    '''
    Contrast the voice and filter out the similar ones
    '''
    started = Signal()
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        CMD = QFunc.SubprocessManager(CommunicateThroughConsole = True)
        self.Process = CMD.create(
            Args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from ASR.VPR.Identify import Voice_Identifying; '
                f"AudioContrastInference = Voice_Identifying{str(Params)}; "
                'AudioContrastInference.GetModel(); '
                'AudioContrastInference.Inference()"'
            ]
        )
        Output, Error = CMD.monitor(
            ShowProgress = True,
            DecodeResult = True,
            LogPath = LogPath
        )[:2]
        if 'error' in str(Error).lower():
            pass
        elif 'traceback' in str(Output).lower():
            Error = "出错了，详情请见终端输出信息"
        else:
            Error = None

        self.finished.emit(str(Error))

    def Terminate(self):
        QFunc.ProcessTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceTranscriber
class Execute_Voice_Transcribing_Whisper(QObject):
    '''
    Transcribe WAV content to SRT
    '''
    started = Signal()
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        LANGUAGES = {
            "中":       "zh",
            "Chinese":  "zh",
            "英":       "en",
            "English":  "en",
            "日":       "ja",
            "japanese": "ja"
        }
        CMD = QFunc.SubprocessManager(CommunicateThroughConsole = True)
        self.Process = CMD.create(
            Args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from STT.Whisper.Transcribe import Voice_Transcribing; '
                f"WAVtoSRT = Voice_Transcribing{str(QFunc.ItemReplacer(LANGUAGES, Params))}; "
                'WAVtoSRT.Transcriber()"'
            ]
        )
        Output, Error = CMD.monitor(
            ShowProgress = True,
            DecodeResult = True,
            LogPath = LogPath
        )[:2]
        if 'error' in str(Error).lower():
            pass
        elif 'traceback' in str(Output).lower():
            Error = "出错了，详情请见终端输出信息"
        else:
            Error = None

        self.finished.emit(str(Error))

    def Terminate(self):
        QFunc.ProcessTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: DatasetCreator
class Execute_Dataset_Creating_GPTSoVITS(QObject):
    '''
    Convert the whisper-generated SRT to CSV and split the WAV
    '''
    started = Signal()
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        CMD = QFunc.SubprocessManager(CommunicateThroughConsole = True)
        self.Process = CMD.create(
            Args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from Dataset.GPT_SoVITS.Create import Dataset_Creating; '
                f"SRTtoCSVandSplitAudio = Dataset_Creating{str(Params)}; "
                'SRTtoCSVandSplitAudio.CallingFunctions()"'
            ]
        )
        Output, Error = CMD.monitor(
            ShowProgress = True,
            DecodeResult = True,
            LogPath = LogPath
        )[:2]
        if 'error' in str(Error).lower():
            pass
        elif 'traceback' in str(Output).lower():
            Error = "出错了，详情请见终端输出信息"
        else:
            Error = None

        self.finished.emit(str(Error))

    def Terminate(self):
        QFunc.ProcessTerminator(self.Process.pid) if hasattr(self, 'Process') else None


class Execute_Dataset_Creating_VITS(QObject):
    '''
    Convert the whisper-generated SRT to CSV and split the WAV
    '''
    started = Signal()
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        CMD = QFunc.SubprocessManager(CommunicateThroughConsole = True)
        self.Process = CMD.create(
            Args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from Dataset.VITS.Create import Dataset_Creating; '
                f"SRTtoCSVandSplitAudio = Dataset_Creating{str(Params)}; "
                'SRTtoCSVandSplitAudio.CallingFunctions()"'
            ]
        )
        Output, Error = CMD.monitor(
            ShowProgress = True,
            DecodeResult = True,
            LogPath = LogPath
        )[:2]
        if 'error' in str(Error).lower():
            pass
        elif 'traceback' in str(Output).lower():
            Error = "出错了，详情请见终端输出信息"
        else:
            Error = None

        self.finished.emit(str(Error))

    def Terminate(self):
        QFunc.ProcessTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceTrainer
class Execute_Voice_Training_GPTSoVITS(QObject):
    '''
    Preprocess and then start training
    '''
    started = Signal()
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        CMD = QFunc.SubprocessManager(CommunicateThroughConsole = True)
        self.Process = CMD.create(
            Args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from Train.GPT_SoVITS.Train import Train; '
                f'Train{str(Params)}"'
            ]
        )
        Output, Error = CMD.monitor(
            ShowProgress = True,
            DecodeResult = True,
            LogPath = LogPath
        )[:2]
        if 'error' in str(Error).lower():
            pass
        elif 'traceback' in str(Output).lower():
            Error = "出错了，详情请见终端输出信息"
        else:
            Error = None

        self.finished.emit(str(Error))

    def Terminate(self):
        QFunc.ProcessTerminator(self.Process.pid) if hasattr(self, 'Process') else None


class Execute_Voice_Training_VITS(QObject):
    '''
    Preprocess and then start training
    '''
    started = Signal()
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        CMD = QFunc.SubprocessManager(CommunicateThroughConsole = True)
        self.Process = CMD.create(
            Args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from Train.VITS.Train import Train; '
                f'Train{str(Params)}"'
            ]
        )
        Output, Error = CMD.monitor(
            ShowProgress = True,
            DecodeResult = True,
            LogPath = LogPath
        )[:2]
        if 'error' in str(Error).lower():
            pass
        elif 'traceback' in str(Output).lower():
            Error = "出错了，详情请见终端输出信息"
        else:
            Error = None

        self.finished.emit(str(Error))

    def Terminate(self):
        QFunc.ProcessTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# Tools: VoiceConverter
class Execute_Voice_Converting_GPTSoVITS(QObject):
    '''
    Inference model
    '''
    started = Signal()
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        CMD = QFunc.SubprocessManager(CommunicateThroughConsole = True)
        self.Process = CMD.create(
            Args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from TTS.GPT_SoVITS.Convert import Convert; '
                f'Convert{str(Params)}"'
            ]
        )
        Output, Error = CMD.monitor(
            ShowProgress = True,
            DecodeResult = True,
            LogPath = LogPath
        )[:2]
        if 'error' in str(Error).lower():
            pass
        elif 'traceback' in str(Output).lower():
            Error = "出错了，详情请见终端输出信息"
        else:
            Error = None

        self.finished.emit(str(Error))

    def Terminate(self):
        QFunc.ProcessTerminator(self.Process.pid) if hasattr(self, 'Process') else None


def Get_Speakers(Config_Path_Load):
    try:
        with open(Config_Path_Load, 'r', encoding = 'utf-8') as File:
            Params = json.load(File)
        Speakers = Params["speakers"]
        return Speakers
    except:
        return str()

class Execute_Voice_Converting_VITS(QObject):
    '''
    Inference model
    '''
    started = Signal()
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        LANGUAGES = {
            "中":       "ZH",
            "Chinese":  "ZH",
            "英":       "EN",
            "English":  "EN",
            "日":       "JA",
            "Japanese": "JA"
        }
        CMD = QFunc.SubprocessManager(CommunicateThroughConsole = True)
        self.Process = CMD.create(
            Args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from TTS.VITS.Convert import Convert; '
                f'Convert{str(QFunc.ItemReplacer(LANGUAGES, Params))}"'
            ]
        )
        Output, Error = CMD.monitor(
            ShowProgress = True,
            DecodeResult = True,
            LogPath = LogPath
        )[:2]
        if 'error' in str(Error).lower():
            pass
        elif 'traceback' in str(Output).lower():
            Error = "出错了，详情请见终端输出信息"
        else:
            Error = None

        self.finished.emit(str(Error))

    def Terminate(self):
        QFunc.ProcessTerminator(self.Process.pid) if hasattr(self, 'Process') else None


# ClientFunc: GetModelsInfo
class CustomSignals_ModelView(QObject):
    '''
    Set up signals for model view
    '''
    Signal_Process_UVR = Signal(list)

    Signal_ASR_VPR = Signal(list)

    Signal_STT_Whisper = Signal(list)

    Signal_TTS_GPTSoVITS = Signal(list)

    Signal_TTS_VITS = Signal(list)

ModelViewSignals = CustomSignals_ModelView()

class Model_View(QObject):
    '''
    View model
    '''
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    def GetModelsInfo(self, ModelsDir: str, ModelsFormats: list):
        ModelsInfo = {}
        os.makedirs(ModelsDir, exist_ok = True)

        ModelDicts_Cloud = []
        Tags = [Path(ModelsDir).parts[-2], Path(ModelsDir).parts[-1]]
        with open(QFunc.NormPath(ManifestPath), 'r', encoding = 'utf-8') as File:
            Param = json.load(File)
        for ModelDict in Param["models"]:
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
            ModelPaths_Local_Sep = QFunc.ToIterable(QFunc.GetPaths(ModelsDir, ModelsFormat))
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
                QFunc.NormPath(Path(ModelDir).joinpath('Process', 'UVR')),
                ['pth', 'onnx']
            )
        )
        ModelViewSignals.Signal_ASR_VPR.emit(
            self.GetModelsInfo(
                QFunc.NormPath(Path(ModelDir).joinpath('ASR', 'VPR')),
                ['pth']
            )
        )
        ModelViewSignals.Signal_STT_Whisper.emit(
            self.GetModelsInfo(
                QFunc.NormPath(Path(ModelDir).joinpath('STT', 'Whisper')),
                ['pt']
            )
        )
        ModelViewSignals.Signal_TTS_GPTSoVITS.emit(
            self.GetModelsInfo(
                QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS')),
                ['pth', 'ckpt', 'bin', 'json']
            )
        )
        ModelViewSignals.Signal_TTS_VITS.emit(
            self.GetModelsInfo(
                QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'VITS')),
                ['pth', 'json']
            )
        )
        self.finished.emit(str(None))


# ClientFunc: ModelDownloader
class Model_Downloader(QObject):
    '''
    Download model
    '''
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    def DownloadModel(self, DownloadParams: tuple):
        try:
            FilePath = QFunc.DownloadFile(*DownloadParams, CreateNewConsole = True)[1]
            FileSuffix = Path(FilePath).suffix
            shutil.unpack_archive(FilePath, DownloadParams[1], FileSuffix) if FileSuffix in ('zip', 'tar', 'gztar', 'bztar') else None
            return None
        except Exception as e:
            return e

    @Slot(tuple)
    def Execute(self, Params: tuple):
        Error = self.DownloadModel(Params)

        self.finished.emit(str(Error))


# ClientFunc: AddLocalModel
def AddLocalModel(ModelPath: str, Sector: list[str] = ['Tool', 'Type']):
    MoveToDst = QFunc.NormPath(Path(ModelDir).joinpath(*Sector))
    shutil.move(ModelPath, MoveToDst)


# ClientFunc: GetASRResult
def ASRResult_Get(AudioSpeakersData_Path: str):
    AudioSpeakerSimList = []
    with open(AudioSpeakersData_Path, mode = 'r', encoding = 'utf-8') as AudioSpeakersData:
        AudioSpeakerSimLines = AudioSpeakersData.readlines()
    for AudioSpeakerSimLine in AudioSpeakerSimLines:
        AudioSpeakerSim = AudioSpeakerSimLine.strip().split('|')
        if len(AudioSpeakerSim) == 2:
            AudioSpeakerSim.append('')
        AudioSpeakerSimList.append(AudioSpeakerSim)
    return AudioSpeakerSimList


# ClientFunc: SaveASRResult
def ASRResult_Save(AudioSpeakers: dict, AudioSpeakersData_Path: str, MoveAudio: bool, MoveToDst: Optional[str] = None):
    with open(AudioSpeakersData_Path, mode = 'w', encoding = 'utf-8') as AudioSpeakersData:
        Lines = []
        for Audio, Speaker in AudioSpeakers.items():
            Speaker = Speaker.strip()
            if Speaker == '':
                continue
            if MoveAudio:
                if MoveToDst is None:
                    raise Exception("Destination shouldn't be 'None'")
                MoveToDst_Sub = QFunc.NormPath(Path(MoveToDst).joinpath(Speaker))
                os.makedirs(MoveToDst_Sub, exist_ok = True) if Path(MoveToDst_Sub).exists() == False else None
                Audio_Dst = QFunc.NormPath(Path(MoveToDst_Sub).joinpath(Path(Audio).name).as_posix())
                shutil.copy(Audio, MoveToDst_Sub) if not Path(Audio_Dst).exists() else None
                Lines.append(f"{Audio_Dst}|{Speaker}\n")
            else:
                Lines.append(f"{Audio}|{Speaker}\n")
        AudioSpeakersData.writelines(Lines)


# ClientFunc: GetSTTResult
def STTResult_Get(SRTDir: str, AudioDir: str):
    STTResult = {}
    for SRTFile in glob(QFunc.NormPath(Path(SRTDir).joinpath('*.srt'))):
        AudioFiles = glob(QFunc.NormPath(Path(AudioDir).joinpath('**', f'{Path(SRTFile).stem}.*')), recursive = True)
        if len(AudioFiles) == 0:
            continue
        with open(SRTFile, mode = 'r', encoding = 'utf-8') as SRT:
            SRTContent = SRT.read()
        STTResult[AudioFiles[0]] = SRTContent
    return STTResult


# ClientFunc: SaveSTTResult
def STTResult_Save(STTResult: dict, SRTDir: str):
    for AudioFile in STTResult.keys():
        SRTFiles = glob(QFunc.NormPath(Path(SRTDir).joinpath(f'{Path(AudioFile).stem}.*')))
        if len(SRTFiles) == 0:
            continue
        with open(SRTFiles[0], mode = 'w', encoding = 'utf-8') as SRT:
            SRT.write(STTResult[AudioFile])


# ClientFunc: GetDATResult
def DATResult_Get(DATPath: str):
    DATResult = {}
    with open(DATPath, mode = 'r', encoding = 'utf-8') as DAT:
        DATLines = DAT.readlines()
    for DATLine in DATLines:
        Audio = QFunc.NormPath(Path(DATPath).parent.joinpath(DATLine.split('|')[0]))
        DATResult[Audio] = DATLine.strip()
    return DATResult


# ClientFunc: SaveDATResult
def DATResult_Save(DATResult: list, DATPath: str):
    with open(DATPath, mode = 'w', encoding = 'utf-8') as DAT:
        DATLines = '\n'.join(DATResult)
        DAT.write(DATLines)


# ClientFunc: ClientRebooter
def ClientRebooter():
    '''
    Reboot EVT client
    '''
    UpdaterExecuter() #os.execl(sys.executable, 'python', __file__, *sys.argv[1:]) else os.execl(sys.executable, sys.executable, *sys.argv)


# ClientFunc: IntegrityChecker
class Integrity_Checker(QObject):
    '''
    Check File integrity
    '''
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot()
    def Execute(self):
        Error = QFunc.RunCMD(
            Args = [
                f'cd "{CoreDir}"',
                'python -c "'
                'from Process.Process import Audio_Processing; '
                'from ASR.VPR.Identify import Voice_Identifying; '
                'from STT.Whisper.Transcribe import Voice_Transcribing; '
                'from Dataset.VITS.Create import Dataset_Creating; '
                'from Train.VITS.Train import Voice_Training; '
                'from TTS.VITS.Convert import Voice_Converting"'
            ],
            CommunicateThroughConsole = True,
            DecodeResult = True,
            LogPath = LogPath
        )[1]

        self.finished.emit(str(Error))


# ClientFunc: TensorboardRunner
class Tensorboard_Runner(QObject):
    '''
    Check File integrity
    '''
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    def RunTensorboard(self, LogDir):
        try:
            Error = None
            InitialWaitTime = 0
            MaximumWaitTime = 30
            while QFunc.GetPaths(LogDir, 'events.out.tfevents') == None:
                time.sleep(3)
                InitialWaitTime += 3
                if InitialWaitTime >= MaximumWaitTime:
                    break
            subprocess.Popen(['python', '-m', 'tensorboard.main', '--logdir', LogDir], env = os.environ)
            time.sleep(9)
            QFunc.Function_OpenURL('http://localhost:6006/')
        except Exception as e:
            Error = e
        finally:
            return Error

    @Slot(tuple)
    def Execute(self, Params: tuple):
        Error = self.RunTensorboard(*Params)

        self.finished.emit(str(Error))

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

        self.Clipboard = QApplication.clipboard()

        self.MonitorUsage = QTasks.MonitorUsage()
        self.MonitorUsage.start()

    def Main(self):
        '''
        Main funtion to orgnize all the subfunctions
        '''
        # Logo
        self.setWindowIcon(QIcon(QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/Logo.ico'))))

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
            CheckBox = self.ui.CheckBox_SwitchTheme,
            CheckedEvents = [
                lambda: Config.EditConfig('Settings', 'Theme', Theme.Light),
                lambda: ComponentsSignals.Signal_SetTheme.emit(Theme.Light) if EasyTheme.THEME != Theme.Light else None
            ],
            UncheckedEvents = [
                lambda: Config.EditConfig('Settings', 'Theme', Theme.Dark),
                lambda: ComponentsSignals.Signal_SetTheme.emit(Theme.Dark) if EasyTheme.THEME != Theme.Dark else None
            ],
            TakeEffect = False
        )

        # Window controling buttons
        self.closed.connect(
            lambda: (
                FunctionSignals.Signal_ForceQuit.emit(),
                FunctionSignals.Signal_TaskStatus.connect(QApplication.exit),
                #os._exit(0)
            )
        )
        self.ui.Button_Close_Window.clicked.connect(self.close)
        self.ui.Button_Close_Window.ClearDefaultStyleSheet()
        self.ui.Button_Close_Window.setStyleSheet(
            "ButtonBase {background-color: transparent; border: none;}"
            "ButtonBase:hover {background-color: rgba(210, 123, 123, 210);}"
        )
        self.ui.Button_Close_Window.setIcon(IconBase.X)

        self.ui.Button_Maximize_Window.clicked.connect(lambda: self.showNormal() if self.isMaximized() else self.showMaximized())
        self.ui.Button_Maximize_Window.ClearDefaultStyleSheet()
        self.ui.Button_Maximize_Window.setStyleSheet(
            "ButtonBase {background-color: transparent; border: none;}"
            "ButtonBase:hover {background-color: rgba(123, 123, 123, 123);}"
        )
        self.ui.Button_Maximize_Window.setIcon(IconBase.FullScreen)

        self.ui.Button_Minimize_Window.clicked.connect(self.showMinimized)
        self.ui.Button_Minimize_Window.ClearDefaultStyleSheet()
        self.ui.Button_Minimize_Window.setStyleSheet(
            "ButtonBase {background-color: transparent; border: none;}"
            "ButtonBase:hover {background-color: rgba(123, 123, 123, 123);}"
        )
        self.ui.Button_Minimize_Window.setIcon(IconBase.Dash)

        # Menu toggling button
        self.ui.Button_Toggle_Menu.clicked.connect(
            lambda: Function_AnimateFrame(
                Frame = self.ui.Frame_Menu,
                MinWidth = 48,
                MaxWidth = 210
            )
        )
        self.ui.Button_Toggle_Menu.setCheckable(True)
        self.ui.Button_Toggle_Menu.setChecked(False)
        self.ui.Button_Toggle_Menu.setAutoExclusive(False)
        self.ui.Button_Toggle_Menu.setToolTip(QCA.translate("ToolTip", "点击以展开/折叠菜单"))

        #############################################################
        ############################ Menu ###########################
        #############################################################

        self.ui.Label_Menu_Home_Text.setText(QCA.translate("Label", "主页"))
        self.ui.Button_Menu_Home.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 0
            )
        )
        self.ui.Button_Menu_Home.setCheckable(True)
        self.ui.Button_Menu_Home.setChecked(True)
        self.ui.Button_Menu_Home.setAutoExclusive(True)
        self.ui.Button_Menu_Home.setToolTip(QCA.translate("ToolTip", "主页"))

        self.ui.Label_Menu_Env_Install_Text.setText(QCA.translate("Label", "环境"))
        self.ui.Button_Menu_Env.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 1
            )
        )
        self.ui.Button_Menu_Env.setCheckable(True)
        self.ui.Button_Menu_Env.setChecked(False)
        self.ui.Button_Menu_Env.setAutoExclusive(True)
        self.ui.Button_Menu_Env.setToolTip(QCA.translate("ToolTip", "环境配置"))

        self.ui.Label_Menu_Models_Text.setText(QCA.translate("Label", "模型"))
        self.ui.Button_Menu_Models.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 2
            )
        )
        self.ui.Button_Menu_Models.setCheckable(True)
        self.ui.Button_Menu_Models.setChecked(False)
        self.ui.Button_Menu_Models.setAutoExclusive(True)
        self.ui.Button_Menu_Models.setToolTip(QCA.translate("ToolTip", "模型管理"))

        self.ui.Label_Menu_Process_Text.setText(QCA.translate("Label", "处理"))
        self.ui.Button_Menu_Process.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 3
            )
        )
        self.ui.Button_Menu_Process.setCheckable(True)
        self.ui.Button_Menu_Process.setChecked(False)
        self.ui.Button_Menu_Process.setAutoExclusive(True)
        self.ui.Button_Menu_Process.setToolTip(QCA.translate("ToolTip", "工具：音频处理"))

        self.ui.Label_Menu_ASR_Text.setText(QCA.translate("Label", "识别"))
        self.ui.Button_Menu_ASR.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 4
            )
        )
        self.ui.Button_Menu_ASR.setCheckable(True)
        self.ui.Button_Menu_ASR.setChecked(False)
        self.ui.Button_Menu_ASR.setAutoExclusive(True)
        self.ui.Button_Menu_ASR.setToolTip(QCA.translate("ToolTip", "工具：语音识别"))

        self.ui.Label_Menu_STT_Text.setText(QCA.translate("Label", "转录"))
        self.ui.Button_Menu_STT.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 5
            )
        )
        self.ui.Button_Menu_STT.setCheckable(True)
        self.ui.Button_Menu_STT.setChecked(False)
        self.ui.Button_Menu_STT.setAutoExclusive(True)
        self.ui.Button_Menu_STT.setToolTip(QCA.translate("ToolTip", "工具：语音转文字"))

        self.ui.Label_Menu_Dataset_Text.setText(QCA.translate("Label", "数据"))
        self.ui.Button_Menu_Dataset.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 6
            )
        )
        self.ui.Button_Menu_Dataset.setCheckable(True)
        self.ui.Button_Menu_Dataset.setChecked(False)
        self.ui.Button_Menu_Dataset.setAutoExclusive(True)
        self.ui.Button_Menu_Dataset.setToolTip(QCA.translate("ToolTip", "工具：数据集制作"))

        self.ui.Label_Menu_Train_Text.setText(QCA.translate("Label", "训练"))
        self.ui.Button_Menu_Train.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 7
            )
        )
        self.ui.Button_Menu_Train.setCheckable(True)
        self.ui.Button_Menu_Train.setChecked(False)
        self.ui.Button_Menu_Train.setAutoExclusive(True)
        self.ui.Button_Menu_Train.setToolTip(QCA.translate("ToolTip", "工具：模型训练"))

        self.ui.Label_Menu_TTS_Text.setText(QCA.translate("Label", "合成"))
        self.ui.Button_Menu_TTS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 8
            )
        )
        self.ui.Button_Menu_TTS.setCheckable(True)
        self.ui.Button_Menu_TTS.setChecked(False)
        self.ui.Button_Menu_TTS.setAutoExclusive(True)
        self.ui.Button_Menu_TTS.setToolTip(QCA.translate("ToolTip", "工具：语音合成"))

        self.ui.Label_Menu_Settings_Text.setText(QCA.translate("Label", "设置"))
        self.ui.Button_Menu_Settings.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 9
            )
        )
        self.ui.Button_Menu_Settings.setCheckable(True)
        self.ui.Button_Menu_Settings.setChecked(False)
        self.ui.Button_Menu_Settings.setAutoExclusive(True)
        self.ui.Button_Menu_Settings.setToolTip(QCA.translate("ToolTip", "客户端设置"))

        self.ui.Label_Menu_Info_Text.setText(QCA.translate("Label", "关于"))
        self.ui.Button_Menu_Info.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 10
            )
        )
        self.ui.Button_Menu_Info.setCheckable(True)
        self.ui.Button_Menu_Info.setChecked(False)
        self.ui.Button_Menu_Info.setAutoExclusive(True)
        self.ui.Button_Menu_Info.setToolTip(QCA.translate("ToolTip", "关于本软件"))

        #############################################################
        ####################### Content: Home #######################
        #############################################################

        #self.ui.ToolButton_Home_Title.setText(QCA.translate("Label", "主页"))
        Function_SetImage(
            Widget = self.ui.Label_Cover_Home,
            ImagePath = Path(ResourceDir).joinpath('assets/images/others/Cover.png')
        )

        QFunc.Function_SetText(
            Widget = self.ui.TextBrowser_Text_Home,
            Text = QFunc.SetRichText(
                Title = QCA.translate("TextBrowser", "介绍"),
                TitleAlign = "left",
                TitleSize = 24,
                TitleWeight = 840,
                Body = QCA.translate("TextBrowser",
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
                BodyAlign = "left",
                BodySize = 12,
                BodyWeight = 420,
                BodyLineHeight = 27
            )
        )

        self.ui.Label_Demo_Text.setText(QCA.translate("Button", "视频演示"))
        Function_SetURL(
            Button = self.ui.Button_Demo,
            URL = "https://www.bilibili.com/video/BV",
            ButtonTooltip = "Click to view demo video"
        )
        self.ui.Label_Server_Text.setText(QCA.translate("Button", "云端版本"))
        Function_SetURL(
            Button = self.ui.Button_Server,
            URL = "https://colab.research.google.com/github/Spr-Aachen/EVT-Reassets/images/others/blob/main/Easy_Voice_Toolkit_for_Colab.ipynb",
            ButtonTooltip = "Click to run on server"
        )
        self.ui.Label_Repo_Text.setText(QCA.translate("Button", "项目仓库"))
        Function_SetURL(
            Button = self.ui.Button_Repo,
            URL = "https://github.com/Spr-Aachen/Easy-Voice-Toolkit",
            ButtonTooltip = "Click to view github repo"
        )
        self.ui.Label_Donate_Text.setText(QCA.translate("Button", "赞助作者"))
        Function_SetURL(
            Button = self.ui.Button_Donate,
            URL = "https://ko-fi.com/spr_aachen",
            ButtonTooltip = "Click to buy author a coffee"
        )

        #############################################################
        ##################### Content: Environ ######################
        #############################################################

        # EnvInstallation
        self.ui.ToolButton_Env_Install_Title.setText(QCA.translate("Label", "自动配置"))
        self.ui.ToolButton_Env_Install_Title.setCheckable(True)
        self.ui.ToolButton_Env_Install_Title.setChecked(True)
        self.ui.ToolButton_Env_Install_Title.setAutoExclusive(True)
        self.ui.ToolButton_Env_Install_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Env,
                TargetIndex = 0
            )
        )

        self.ui.Label_Env_Install_Aria2.setText(QCA.translate("Label", "Aria2"))
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_Install_Aria2,
            ProgressBar = self.ui.ProgressBar_Env_Install_Aria2,
            Method = Aria2_Installer.Execute,
            Params = ()
        )
        MainWindowSignals.Signal_MainWindowShown.connect(
            self.ui.Button_Install_Aria2.click
        )
        self.ui.Button_Install_Aria2.setText('')
        self.ui.Button_Install_Aria2.setToolTip(QCA.translate("ToolTip", "重新检测安装"))
        EnvConfiguratorSignals.Signal_Aria2Undetected.connect(
            lambda: Function_ShowMessageBox(self,
                WindowTitle = "Tip",
                Text = "未检测到Aria2，已开始下载",
                ButtonEvents = {QMessageBox.Ok: lambda: self.ui.Button_Menu_Env.click()}
            )
        )
        EnvConfiguratorSignals.Signal_Aria2Installed.connect(#self.ui.Button_Install_Aria2.click)
            lambda: EnvConfiguratorSignals.Signal_Aria2Detected.emit()
        )
        EnvConfiguratorSignals.Signal_Aria2InstallFailed.connect(
            lambda Exception: Function_ShowMessageBox(self,
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = f"安装Aria2出错：\n{Exception}",
            )
        )
        EnvConfiguratorSignals.Signal_Aria2Detected.connect(
            lambda: self.ui.ProgressBar_Env_Install_Aria2.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_Aria2Status.connect(
            lambda Status: self.ui.Label_Env_Install_Aria2_Status.setText(Status)
        )

        self.ui.Label_Env_Install_FFmpeg.setText(QCA.translate("Label", "FFmpeg"))
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_Install_FFmpeg,
            ProgressBar = self.ui.ProgressBar_Env_Install_FFmpeg,
            Method = FFmpeg_Installer.Execute,
            Params = ()
        )
        MainWindowSignals.Signal_MainWindowShown.connect(
            self.ui.Button_Install_FFmpeg.click
        )
        self.ui.Button_Install_FFmpeg.setText('')
        self.ui.Button_Install_FFmpeg.setToolTip(QCA.translate("ToolTip", "重新检测安装"))
        EnvConfiguratorSignals.Signal_FFmpegUndetected.connect(
            lambda: Function_ShowMessageBox(self,
                WindowTitle = "Tip",
                Text = "未检测到FFmpeg，已开始下载",
                ButtonEvents = {QMessageBox.Ok: lambda: self.ui.Button_Menu_Env.click()}
            )
        )
        EnvConfiguratorSignals.Signal_FFmpegInstalled.connect(#self.ui.Button_Install_FFmpeg.click)
            lambda: EnvConfiguratorSignals.Signal_FFmpegDetected.emit()
        )
        EnvConfiguratorSignals.Signal_FFmpegInstallFailed.connect(
            lambda Exception: Function_ShowMessageBox(self,
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = f"安装FFmpeg出错：\n{Exception}",
            )
        )
        EnvConfiguratorSignals.Signal_FFmpegDetected.connect(
            lambda: self.ui.ProgressBar_Env_Install_FFmpeg.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_FFmpegStatus.connect(
            lambda Status: self.ui.Label_Env_Install_FFmpeg_Status.setText(Status)
        )

        self.ui.Label_Env_Install_Python.setText(QCA.translate("Label", "Python"))
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_Install_Python,
            ProgressBar = self.ui.ProgressBar_Env_Install_Python,
            Method = Python_Installer.Execute,
            Params = ('3.9.0', )
        )
        MainWindowSignals.Signal_MainWindowShown.connect( #EnvConfiguratorSignals.Signal_CMakeDetected.connect(
            self.ui.Button_Install_Python.click
        )
        self.ui.Button_Install_Python.setText('')
        self.ui.Button_Install_Python.setToolTip(QCA.translate("ToolTip", "重新检测安装"))
        EnvConfiguratorSignals.Signal_PythonUndetected.connect(
            lambda: Function_ShowMessageBox(self,
                WindowTitle = "Tip",
                Text = "未检测到3.8版本以上的Python，已开始下载",
                ButtonEvents = {QMessageBox.Ok: lambda: self.ui.Button_Menu_Env.click()}
            )
        )
        EnvConfiguratorSignals.Signal_PythonInstalled.connect(#self.ui.Button_Install_Python.click)
            lambda: EnvConfiguratorSignals.Signal_PythonDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PythonInstallFailed.connect(
            lambda Exception: Function_ShowMessageBox(self,
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = f"安装Python出错：\n{Exception}",
            )
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            lambda: self.ui.ProgressBar_Env_Install_Python.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PythonStatus.connect(
            lambda Status: self.ui.Label_Env_Install_Python_Status.setText(Status)
        )

        self.ui.Label_Env_Install_PyReqs.setText(QCA.translate("Label", "Python Requirements"))
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_Install_PyReqs,
            ProgressBar = self.ui.ProgressBar_Env_Install_PyReqs,
            Method = PyReqs_Installer.Execute,
            Params = (QFunc.NormPath(RequirementsPath), )
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            self.ui.Button_Install_PyReqs.click
        )
        self.ui.Button_Install_PyReqs.setText('')
        self.ui.Button_Install_PyReqs.setToolTip(QCA.translate("ToolTip", "重新检测安装"))
        EnvConfiguratorSignals.Signal_PyReqsUndetected.connect(
            lambda: Function_ShowMessageBox(self,
                WindowTitle = "Tip",
                Text = "缺失Python依赖库，已开始下载",
                ButtonEvents = {QMessageBox.Ok: lambda: self.ui.Button_Menu_Env.click()}
            )
        )
        EnvConfiguratorSignals.Signal_PyReqsInstalled.connect(#self.ui.Button_Install_PyReqs.click)
            lambda: EnvConfiguratorSignals.Signal_PyReqsDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PythonInstallFailed.connect(
            lambda Exception: Function_ShowMessageBox(self,
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = f"安装Python依赖库出错：\n{Exception}"
            )
        )
        EnvConfiguratorSignals.Signal_PyReqsDetected.connect(
            lambda: self.ui.ProgressBar_Env_Install_PyReqs.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PyReqsStatus.connect(
            lambda Status: self.ui.Label_Env_Install_PyReqs_Status.setText(Status)
        )

        self.ui.Label_Env_Install_Pytorch.setText(QCA.translate("Label", "Pytorch"))
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_Install_Pytorch,
            ProgressBar = self.ui.ProgressBar_Env_Install_Pytorch,
            Method = Pytorch_Installer.Execute,
            Params = ()
        )
        EnvConfiguratorSignals.Signal_PyReqsDetected.connect(
            self.ui.Button_Install_Pytorch.click
        )
        self.ui.Button_Install_Pytorch.setText('')
        self.ui.Button_Install_Pytorch.setToolTip(QCA.translate("ToolTip", "重新检测安装"))
        EnvConfiguratorSignals.Signal_PytorchUndetected.connect(
            lambda: Function_ShowMessageBox(self,
                WindowTitle = "Tip",
                Text = "缺失Pytorch相关库，已开始下载",
                ButtonEvents = {QMessageBox.Ok: lambda: self.ui.Button_Menu_Env.click()}
            )
        )
        EnvConfiguratorSignals.Signal_PytorchInstalled.connect(#self.ui.Button_Install_Pytorch.click)
            lambda: EnvConfiguratorSignals.Signal_PytorchDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PytorchInstallFailed.connect(
            lambda Exception: Function_ShowMessageBox(self,
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = f"安装Pytorch出错：\n{Exception}",
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
        self.ui.ToolButton_Env_Manage_Title.setText(QCA.translate("ToolButton", "安装管理"))
        self.ui.ToolButton_Env_Manage_Title.setCheckable(True)
        self.ui.ToolButton_Env_Manage_Title.setChecked(False)
        self.ui.ToolButton_Env_Manage_Title.setAutoExclusive(True)
        self.ui.ToolButton_Env_Manage_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Env,
                TargetIndex = 1
            )
        )

        self.ui.ToolBox_Env_Manage_Pytorch.widget(0).setText(QCA.translate("ToolBox", "Pytorch"))
        self.ui.ToolBox_Env_Manage_Pytorch.widget(0).collapse()

        self.ui.Label_Env_Manage_Pytorch_Version.setText(QCA.translate("Label", "选择Pytorch版本"))
        self.ui.ComboBox_Env_Manage_Pytorch_Version.addItems([ '2.0.1', '2.2.2'])

        self.ui.Button_Env_Manage_Pytorch_Install.setText(QCA.translate("Button", "重装"))
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_Env_Manage_Pytorch_Install,
            Method = Pytorch_Installer.Execute,
            ParamsFrom = [
                self.ui.ComboBox_Env_Manage_Pytorch_Version,
                True
            ]
        )

        #############################################################
        ####################### Content: Models #####################
        #############################################################

        MainWindowSignals.Signal_MainWindowShown.connect(
            lambda: Function_SetMethodExecutor(self,
                Method = Model_View.Execute
            )
        )

        self.ui.ToolButton_Models_Process_Title.setText(QCA.translate("ToolButton", '基本处理'))
        self.ui.ToolButton_Models_Process_Title.setCheckable(True)
        self.ui.ToolButton_Models_Process_Title.setChecked(True)
        self.ui.ToolButton_Models_Process_Title.setAutoExclusive(True)
        self.ui.ToolButton_Models_Process_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Models,
                TargetIndex = 0
            )
        )
        self.ui.ToolButton_Models_Process_Title.setToolTip(
            "基本处理模型"
        )

        self.ui.TabWidget_Models_Process.setTabText(0, 'UVR（人声分离）')
        self.ui.Table_Models_Process_UVR.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        ModelViewSignals.Signal_Process_UVR.connect(self.ui.Table_Models_Process_UVR.SetValue)
        self.ui.Table_Models_Process_UVR.Download.connect(
            lambda Params: Function_SetMethodExecutor(self,
                Method = Model_Downloader.Execute,
                Params = Params
            )
        )

        self.ui.ToolButton_Models_ASR_Title.setText(QCA.translate("ToolButton", 'ASR（识别）'))
        self.ui.ToolButton_Models_ASR_Title.setCheckable(True)
        self.ui.ToolButton_Models_ASR_Title.setChecked(False)
        self.ui.ToolButton_Models_ASR_Title.setAutoExclusive(True)
        self.ui.ToolButton_Models_ASR_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Models,
                TargetIndex = 1
            )
        )
        self.ui.ToolButton_Models_ASR_Title.setToolTip(
            "语音识别模型"
        )

        self.ui.TabWidget_Models_ASR.setTabText(0, 'VPR（声纹识别）')
        self.ui.Table_Models_ASR_VPR.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        ModelViewSignals.Signal_ASR_VPR.connect(self.ui.Table_Models_ASR_VPR.SetValue)
        self.ui.Table_Models_ASR_VPR.Download.connect(
            lambda Params: Function_SetMethodExecutor(self,
                Method = Model_Downloader.Execute,
                Params = Params
            )
        )

        self.ui.ToolButton_Models_STT_Title.setText(QCA.translate("ToolButton", 'STT（转录）'))
        self.ui.ToolButton_Models_STT_Title.setCheckable(True)
        self.ui.ToolButton_Models_STT_Title.setChecked(False)
        self.ui.ToolButton_Models_STT_Title.setAutoExclusive(True)
        self.ui.ToolButton_Models_STT_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Models,
                TargetIndex = 2
            )
        )
        self.ui.ToolButton_Models_STT_Title.setToolTip(
            "语音转录模型"
        )

        self.ui.TabWidget_Models_STT.setTabText(0, 'Whisper')
        self.ui.Table_Models_STT_Whisper.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        ModelViewSignals.Signal_STT_Whisper.connect(self.ui.Table_Models_STT_Whisper.SetValue)
        self.ui.Table_Models_STT_Whisper.Download.connect(
            lambda Params: Function_SetMethodExecutor(self,
                Method = Model_Downloader.Execute,
                Params = Params
            )
        )

        self.ui.ToolButton_Models_TTS_Title.setText(QCA.translate("ToolButton", 'TTS（合成）'))
        self.ui.ToolButton_Models_TTS_Title.setCheckable(True)
        self.ui.ToolButton_Models_TTS_Title.setChecked(False)
        self.ui.ToolButton_Models_TTS_Title.setAutoExclusive(True)
        self.ui.ToolButton_Models_TTS_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Models,
                TargetIndex = 3
            )
        )
        self.ui.ToolButton_Models_TTS_Title.setToolTip(
            "语音合成模型"
        )

        self.ui.TabWidget_Models_TTS.setTabText(0, 'GPT-SoVITS')
        self.ui.Table_Models_TTS_GPTSoVITS.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        ModelViewSignals.Signal_TTS_GPTSoVITS.connect(self.ui.Table_Models_TTS_GPTSoVITS.SetValue)
        self.ui.Table_Models_TTS_GPTSoVITS.Download.connect(
            lambda Params: Function_SetMethodExecutor(self,
                Method = Model_Downloader.Execute,
                Params = Params
            )
        )

        self.ui.TabWidget_Models_TTS.setTabText(1, 'VITS')
        self.ui.Table_Models_TTS_VITS.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        ModelViewSignals.Signal_TTS_VITS.connect(self.ui.Table_Models_TTS_VITS.SetValue)
        self.ui.Table_Models_TTS_VITS.Download.connect(
            lambda Params: Function_SetMethodExecutor(self,
                Method = Model_Downloader.Execute,
                Params = Params
            )
        )

        self.ui.Button_Models_Refresh.setText(QCA.translate("ToolButton", '刷新'))
        self.ui.Button_Models_Refresh.clicked.connect(
            lambda: Function_SetMethodExecutor(self,
                Method = Model_View.Execute
            )
        )

        self.ui.Button_Models_Append.setText(QCA.translate("ToolButton", '添加'))
        LineEdit_Models_Append = QLineEdit()
        DialogBox_Models_Append = MessageBox_Buttons(self)
        DialogBox_Models_Append.setText(QCA.translate("MsgBox", "请选择添加方式"))
        DialogBox_Models_Append.Button1.setText(QCA.translate("Button", "模型文件目录（多文件）"))
        DialogBox_Models_Append.Button1.clicked.connect(
            lambda: (
                LineEdit_Models_Append.setText(
                    QFunc.Function_GetFileDialog(
                        Mode = "SelectFolder"
                    )
                ),
                DialogBox_Models_Append.close(),
            )
        )
        DialogBox_Models_Append.Button2.setText(QCA.translate("Button", "模型文件路径（单文件）"))
        DialogBox_Models_Append.Button2.clicked.connect(
            lambda: (
                LineEdit_Models_Append.setText(
                    QFunc.Function_GetFileDialog(
                        Mode = "SelectFile",
                        FileType = "模型文件 (*.pt *.pth *.ckpt *.bin *.json')"
                    )
                ),
                DialogBox_Models_Append.close(),
            )
        )
        def AppendModel():
            DialogBox_Models_Append.exec()
            ModelPath = LineEdit_Models_Append.text()
            if QFunc.NormPath(ModelPath) is None:
                return
            ToolIndexList = ['Process', 'ASR', 'STT', 'TTS']
            ToolIndex = self.ui.StackedWidget_Pages_Models.currentIndex()
            TabWidget = QFunc.Function_FindChildUI(self.ui.StackedWidget_Pages_Models.currentWidget(), QTabWidget)
            TypeIndex = TabWidget.currentIndex()
            Sector = [
                ToolIndexList[ToolIndex],
                TabWidget.tabText(TypeIndex).rsplit('（')[0],
            ]
            AddLocalModel(ModelPath, Sector)
            self.ui.Button_Models_Refresh.click()
        self.ui.Button_Models_Append.clicked.connect(AppendModel)

        #############################################################
        ###################### Content: Process #####################
        #############################################################

        # Guidance
        DialogBox_Process = MessageBox_Stacked(self)
        DialogBox_Process.setWindowTitle(QCA.translate("MsgBox", "引导（仅出现一次）"))
        DialogBox_Process.SetContent(
            [
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_Process.png')),
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
            ],
            [
                '欢迎来到音频处理工具界面\n该工具用于将媒体文件批量转换为音频文件并进行降噪、静音切除等操作',
                '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_Process.clicked.connect(
            lambda: (
                DialogBox_Process.exec(),
                Config.EditConfig('Dialog', 'GuidanceShown_Process', 'True')
            ) if eval(Config.GetValue('Dialog', 'GuidanceShown_Process', 'False')) is False else None
        )

        self.ui.Button_AudioProcessor_Help.clicked.connect(
            lambda: DialogBox_Process.exec()
        )

        # ParamsManager
        Path_Config_Process = QFunc.NormPath(Path(ConfigDir).joinpath('Config_Process.ini'))
        ParamsManager_Process = ParamsManager(Path_Config_Process)

        # Top
        self.ui.ToolButton_AudioProcessor_Title.setText(QCA.translate("ToolButton", '音频基本处理'))
        self.ui.ToolButton_AudioProcessor_Title.setCheckable(True)
        self.ui.ToolButton_AudioProcessor_Title.setChecked(True)
        self.ui.ToolButton_AudioProcessor_Title.setAutoExclusive(True)
        self.ui.ToolButton_AudioProcessor_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Process,
                TargetIndex = 0
            )
        )

        # Left
        self.ui.TreeWidget_Catalogue_Process.clear()
        self.ui.TreeWidget_Catalogue_Process.setHeaderHidden(True)

        # Middle
        self.ui.GroupBox_Process_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_Process_InputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "输入参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_MediaDirInput,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "媒体输入目录\n需要处理的音频文件的所在目录。")
            )
        )
        ParamsManager_Process.SetParam(
            Widget = self.ui.LineEdit_Process_MediaDirInput,
            Section = 'Input Params',
            Option = 'Media_Dir_Input',
            DefaultValue = '',
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Process_MediaDirInput.SetFileDialog(
            Mode = "SelectFolder"
        )
        self.ui.Button_Process_MediaDirInput_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.LineEdit_Process_MediaDirInput),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Process_MediaDirInput.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_MediaDirInput,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "媒体输入目录")
        )

        self.ui.GroupBox_Process_DenoiserParams.setTitle(QCA.translate("GroupBox", "降噪参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_Process_DenoiserParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "降噪参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_DenoiseAudio,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "启用杂音去除\n弱化音频中的非人声部分。")
            )
        )
        ParamsManager_Process.SetParam(
            Widget = self.ui.CheckBox_Process_DenoiseAudio,
            Section = 'Denoiser Params',
            Option = 'Denoise_Audio',
            DefaultValue = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Process_DenoiseAudio,
            CheckedText = "已启用",
            CheckedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_Process_DenoiserParams_BasicSettings,
                    [
                        self.ui.Frame_Process_DenoiseModelPath,
                        self.ui.Frame_Process_DenoiseTarget,
                    ],
                    True
                )
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_Process_DenoiserParams_BasicSettings,
                    [
                        self.ui.Frame_Process_DenoiseModelPath,
                        self.ui.Frame_Process_DenoiseTarget,
                    ],
                    False
                )
            ],
            TakeEffect = True
        )
        self.ui.Button_Process_DenoiseAudio_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.CheckBox_Process_DenoiseAudio)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_DenoiseAudio,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "降噪参数"),
            ChildItemText = QCA.translate("Tree", "启用杂音去除")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_DenoiseModelPath,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "uvr5模型路径\n用于uvr5降噪的模型文件的路径。")
            )
        )
        Process_DenoiseModelPath_Default = Path(ModelDir).joinpath('Process', 'UVR', 'Downloaded', 'HP5_only_main_vocal.pth').as_posix()
        ParamsManager_Process.SetParam(
            Widget = self.ui.LineEdit_Process_DenoiseModelPath,
            Section = 'Denoiser Params',
            Option = 'Denoise_Model_Path',
            DefaultValue = Process_DenoiseModelPath_Default,
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Process_DenoiseModelPath.SetFileDialog(
            Mode = "SelectFile",
            FileType = "pth类型/onnx类型 (*.pth *.onnx)",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('Process', 'UVR', 'Downloaded'))
        )
        self.ui.Button_Process_DenoiseModelPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.LineEdit_Process_DenoiseModelPath),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Process_DenoiseModelPath.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_DenoiseModelPath,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "降噪参数"),
            ChildItemText = QCA.translate("Tree", "uvr5模型路径")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_DenoiseTarget,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "提取目标\n选择在降噪时要保留的声音对象。")
            )
        )
        self.ui.ComboBox_Process_DenoiseTarget.addItems([QCA.translate("ComboBox", '人声'), QCA.translate("ComboBox", '背景声')])
        ParamsManager_Process.SetParam(
            Widget = self.ui.ComboBox_Process_DenoiseTarget,
            Section = 'Denoiser Params',
            Option = 'Denoise_Target',
            DefaultValue = '人声'
        )
        self.ui.Button_Process_DenoiseTarget_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.ComboBox_Process_DenoiseTarget)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_DenoiseTarget,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "降噪参数"),
            ChildItemText = QCA.translate("Tree", "提取目标")
        )

        self.ui.GroupBox_Process_SlicerParams.setTitle(QCA.translate("GroupBox", "静音切除参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_Process_SlicerParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "静音切除参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_SliceAudio,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "启用静音切除\n切除音频中的静音部分。")
            )
        )
        ParamsManager_Process.SetParam(
            Widget = self.ui.CheckBox_Process_SliceAudio,
            Section = 'Slicer Params',
            Option = 'Slice_Audio',
            DefaultValue = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Process_SliceAudio,
            CheckedText = "已启用",
            CheckedEvents = [
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
            UncheckedText = "未启用",
            UncheckedEvents = [
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
            TakeEffect = True
        )
        self.ui.Button_Process_SliceAudio_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.CheckBox_Process_SliceAudio)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_SliceAudio,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "静音切除参数"),
            ChildItemText = QCA.translate("Tree", "启用静音切除")
        )

        self.ui.ToolBox_Process_SlicerParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_Process_SlicerParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_RMSThreshold,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "均方根阈值 (db)\n低于该阈值的片段将被视作静音进行处理，若有降噪需求可以增加该值。")
            )
        )
        self.ui.DoubleSpinBox_Process_RMSThreshold.setRange(-100, 0)
        #self.ui.DoubleSpinBox_Process_RMSThreshold.setSingleStep(0.01)
        ParamsManager_Process.SetParam(
            Widget = self.ui.DoubleSpinBox_Process_RMSThreshold,
            Section = 'Slicer Params',
            Option = 'RMS_Threshold',
            DefaultValue = -34.
        )
        self.ui.Button_Process_RMSThreshold_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.DoubleSpinBox_Process_RMSThreshold)
            }
            
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_RMSThreshold,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "静音切除参数"),
            ChildItemText = QCA.translate("Tree", "均方根阈值")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_HopSize,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "跃点大小 (ms)\n每个RMS帧的长度，增加该值能够提高分割精度但会减慢进程。")
            )
        )
        self.ui.SpinBox_Process_HopSize.setRange(0, 100)
        self.ui.SpinBox_Process_HopSize.setSingleStep(1)
        ParamsManager_Process.SetParam(
            Widget = self.ui.SpinBox_Process_HopSize,
            Section = 'Slicer Params',
            Option = 'Hop_Size',
            DefaultValue = 10
        )
        self.ui.Button_Process_HopSize_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.SpinBox_Process_HopSize)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_HopSize,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "静音切除参数"),
            ChildItemText = QCA.translate("Tree", "跃点大小")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_SilentIntervalMin,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "最小静音间隔 (ms)\n静音部分被分割成的最小长度，若音频只包含短暂中断可以减小该值。")
            )
        )
        self.ui.SpinBox_Process_SilentIntervalMin.setRange(0, 3000)
        self.ui.SpinBox_Process_SilentIntervalMin.setSingleStep(1)
        ParamsManager_Process.SetParam(
            Widget = self.ui.SpinBox_Process_SilentIntervalMin,
            Section = 'Slicer Params',
            Option = 'Silent_Interval_Min',
            DefaultValue = 300
        )
        self.ui.SpinBox_Process_SilentIntervalMin.setToolTip(QCA.translate("ToolTip", "注意：这个值必须小于最小音频长度，大于跃点大小。"))
        self.ui.Button_Process_SilentIntervalMin_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.SpinBox_Process_SilentIntervalMin)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_SilentIntervalMin,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "静音切除参数"),
            ChildItemText = QCA.translate("Tree", "最小静音间隔")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_SilenceKeptMax,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "最大静音长度 (ms)\n被分割的音频周围保持静音的最大长度。")
            )
        )
        self.ui.SpinBox_Process_SilenceKeptMax.setRange(0, 10000)
        self.ui.SpinBox_Process_SilenceKeptMax.setSingleStep(1)
        ParamsManager_Process.SetParam(
            Widget = self.ui.SpinBox_Process_SilenceKeptMax,
            Section = 'Slicer Params',
            Option = 'Silence_Kept_Max',
            DefaultValue = 500
        )
        self.ui.SpinBox_Process_SilenceKeptMax.setToolTip(QCA.translate("ToolTip", "注意：这个值无需完全对应被分割音频中的静音长度。算法将自行检索最佳的分割位置。"))
        self.ui.Button_Process_SilenceKeptMax_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.SpinBox_Process_SilenceKeptMax)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_SilenceKeptMax,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "静音切除参数"),
            ChildItemText = QCA.translate("Tree", "最大静音长度")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_AudioLengthMin,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "最小音频长度 (ms)\n每个被分割的音频片段所需的最小长度。")
            )
        )
        self.ui.SpinBox_Process_AudioLengthMin.setRange(300, 30000)
        self.ui.SpinBox_Process_AudioLengthMin.setSingleStep(1)
        ParamsManager_Process.SetParam(
            Widget = self.ui.SpinBox_Process_AudioLengthMin,
            Section = 'Slicer Params',
            Option = 'Audio_Length_Min',
            DefaultValue = 4000
        )
        self.ui.Button_Process_AudioLengthMin_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.SpinBox_Process_AudioLengthMin)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_AudioLengthMin,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "静音切除参数"),
            ChildItemText = QCA.translate("Tree", "最小音频长度")
        )

        self.ui.GroupBox_Process_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_Process_OutputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "输出参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_MediaFormatOutput,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "媒体输出格式\n媒体文件输出为音频文件的格式，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Process_MediaFormatOutput.addItems(['flac', 'wav', 'mp3', 'aac', 'm4a', 'wma', 'aiff', 'au', 'ogg', 'None'])
        ParamsManager_Process.SetParam(
            Widget = self.ui.ComboBox_Process_MediaFormatOutput,
            Section = 'Output Params',
            Option = 'Media_Format_Output',
            DefaultValue = 'wav'
        )
        self.ui.Button_Process_MediaFormatOutput_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.ComboBox_Process_MediaFormatOutput)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_AudioLengthMin,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "媒体输出格式")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_OutputDirName,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "输出目录名\n用于保存最后生成的音频文件的目录的名字。")
            )
        )
        Process_OutputDirName_Default = str(date.today())
        ParamsManager_Process.SetParam(
            Widget = self.ui.LineEdit_Process_OutputDirName,
            Section = 'Output Params',
            Option = 'Output_Dir_Name',
            DefaultValue = '',
            SetPlaceholderText = True,
            PlaceholderText = Process_OutputDirName_Default
        )
        self.ui.LineEdit_Process_OutputDirName.RemoveFileDialogButton()
        self.ui.Button_Process_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.LineEdit_Process_OutputDirName),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Process_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_OutputDirName,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "输出目录名")
        )

        LineEdit_Process_OutputDir = QLineEdit()
        def SetText_LineEdit_Process_OutputDir():
            DirName = self.ui.LineEdit_Process_OutputDirName.text()
            if len(DirName.strip()) == 0:
                Alert = False
            else:
                DirText = Path(self.ui.LineEdit_Process_OutputRoot.text()).joinpath(DirName).as_posix()
                LineEdit_Process_OutputDir.setText(DirText)
                Alert = Path(DirText).exists() and list(Path(DirText).iterdir()) != []
            self.ui.LineEdit_Process_OutputDirName.Alert(True if Alert else False, "注意：目录已包含文件")
        self.ui.LineEdit_Process_OutputDirName.interacted.connect(SetText_LineEdit_Process_OutputDir)
        self.ui.LineEdit_Process_OutputRoot.interacted.connect(SetText_LineEdit_Process_OutputDir)
        #SetText_LineEdit_Process_OutputDir()

        self.ui.ToolBox_Process_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_Process_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_ToMono,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "合并声道\n将输出音频的声道合并为单声道。")
            )
        )
        ParamsManager_Process.SetParam(
            Widget = self.ui.CheckBox_Process_ToMono,
            Section = 'Output Params',
            Option = 'ToMono',
            DefaultValue = False
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Process_ToMono,
            CheckedText = "已启用",
            CheckedEvents = [
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
            ],
            TakeEffect = True
        )
        self.ui.Button_Process_ToMono_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.CheckBox_Process_ToMono)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_ToMono,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "合并声道")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_SampleRate,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "输出采样率\n输出音频所拥有的采样率，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Process_SampleRate.addItems(['22050', '44100', '48000', '96000', '192000', 'None'])
        ParamsManager_Process.SetParam(
            Widget = self.ui.ComboBox_Process_SampleRate,
            Section = 'Output Params',
            Option = 'SampleRate',
            DefaultValue = None
        )
        self.ui.Button_Process_SampleRate_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.ComboBox_Process_SampleRate)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_SampleRate,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "输出采样率")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Process_SampleWidth,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "输出采样位数\n输出音频所拥有的采样位数，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Process_SampleWidth.addItems(['8', '16', '24', '32', '32 (Float)', 'None'])
        ParamsManager_Process.SetParam(
            Widget = self.ui.ComboBox_Process_SampleWidth,
            Section = 'Output Params',
            Option = 'SampleWidth',
            DefaultValue = None
        )
        self.ui.Button_Process_SampleWidth_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.ComboBox_Process_SampleWidth)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Process_SampleWidth,
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "输出采样位数")
        )

        # Right
        MonitorFile_Config_AudioProcessor = QTasks.MonitorFile(Path_Config_Process)
        MonitorFile_Config_AudioProcessor.start()
        MonitorFile_Config_AudioProcessor.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Process.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_Process.setText(QCA.translate("Button", "全部重置"))
        self.ui.Button_ResetSettings_Process.clicked.connect(
            lambda: ParamsManager_Process.ResetSettings()
        )

        self.ui.Button_ImportSettings_Process.setText(QCA.translate("Button", "导入配置"))
        self.ui.Button_ImportSettings_Process.clicked.connect(
            lambda: ParamsManager_Process.ImportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SelectFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_Process.setText(QCA.translate("Button", "导出配置"))
        self.ui.Button_ExportSettings_Process.clicked.connect(
            lambda: ParamsManager_Process.ExportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SaveFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_CheckOutput_Process.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Process,
            URL = self.ui.LineEdit_Process_OutputRoot,
            ButtonTooltip = "Click to open",
            CreateIfNotExist = True
        )

        # Bottom
        self.ui.Button_Process_Execute.setToolTip(QCA.translate("ToolTip", "执行音频处理"))
        self.ui.Button_Process_Terminate.setToolTip(QCA.translate("ToolTip", "终止音频处理"))
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_Process_Execute,
            TerminateButton = self.ui.Button_Process_Terminate,
            ProgressBar = self.ui.ProgressBar_Process,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Audio_Processing.Execute,
            ParamsFrom = [
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
            EmptyAllowed = [
                self.ui.ComboBox_Process_MediaFormatOutput,
                self.ui.ComboBox_Process_SampleRate,
                self.ui.ComboBox_Process_SampleWidth
            ],
            FinishEvents = [
                lambda: Function_ShowMessageBox(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        #############################################################
        ######################## Content: ASR #######################
        #############################################################

        # Guidance
        DialogBox_ASR = MessageBox_Stacked(self)
        DialogBox_ASR.setWindowTitle(QCA.translate("MsgBox", "引导（仅出现一次）"))
        DialogBox_ASR.SetContent(
            [
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_ASR.png')),
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
            ],
            [
                '欢迎来到语音识别工具界面\n该工具用于从不同说话人的音频中批量筛选出属于同一说话人的音频',
                '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_ASR.clicked.connect(
            lambda: (
                DialogBox_ASR.exec(),
                Config.EditConfig('Dialog', 'GuidanceShown_ASR', 'True')
            ) if eval(Config.GetValue('Dialog', 'GuidanceShown_ASR', 'False')) is False else None
        )

        self.ui.Button_VoiceIdentifier_Help.clicked.connect(
            lambda: DialogBox_ASR.exec()
        )

        # ParamsManager
        Path_Config_ASR_VPR = QFunc.NormPath(Path(ConfigDir).joinpath('Config_ASR_VPR.ini'))
        ParamsManager_ASR_VPR = ParamsManager(Path_Config_ASR_VPR)

        # Top
        self.ui.ToolButton_VoiceIdentifier_Title.setText(QCA.translate("ToolButton", "VPR（声纹识别）"))
        self.ui.ToolButton_VoiceIdentifier_Title.setCheckable(True)
        self.ui.ToolButton_VoiceIdentifier_Title.setChecked(True)
        self.ui.ToolButton_VoiceIdentifier_Title.setAutoExclusive(True)
        self.ui.ToolButton_VoiceIdentifier_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_ASR,
                TargetIndex = 0
            )
        )

        # Left
        self.ui.TreeWidget_Catalogue_ASR_VPR.clear()
        self.ui.TreeWidget_Catalogue_ASR_VPR.setHeaderHidden(True)

        # Middle
        self.ui.GroupBox_ASR_VPR_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_ASR_VPR_InputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "输入参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_ASR_VPR_AudioDirInput,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "音频输入目录\n需要进行语音识别筛选的音频文件的所在目录。")
            )
        )
        ParamsManager_ASR_VPR.SetParam(
            Widget = self.ui.LineEdit_ASR_VPR_AudioDirInput,
            Section = 'Input Params',
            Option = 'Audio_Dir_Input',
            DefaultValue = '',
            SetPlaceholderText = True
        )
        self.ui.LineEdit_ASR_VPR_AudioDirInput.SetFileDialog(
            Mode = "SelectFolder",
            Directory = Path(CurrentDir).joinpath('音频处理结果').as_posix()
        )
        self.ui.Button_ASR_VPR_AudioDirInput_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_VPR.ResetParam(self.ui.LineEdit_ASR_VPR_AudioDirInput),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_ASR_VPR_AudioDirInput.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_ASR_VPR_AudioDirInput,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "音频输入目录")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_ASR_VPR_StdAudioSpeaker,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "目标人物与音频\n目标人物的名字及其语音文件的路径。")
            )
        )
        self.ui.Table_ASR_VPR_StdAudioSpeaker.setHorizontalHeaderLabels(['人物姓名', '音频路径', '增删'])
        ParamsManager_ASR_VPR.SetParam(
            Widget = self.ui.Table_ASR_VPR_StdAudioSpeaker,
            Section = 'Input Params',
            Option = 'StdAudioSpeaker',
            DefaultValue = {"": ""}
        )
        self.ui.Table_ASR_VPR_StdAudioSpeaker.SetFileDialog(
            FileType = "音频类型 (*.flac *.wav *.mp3 *.aac *.m4a *.wma *.aiff *.au *.ogg)"
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_ASR_VPR_StdAudioSpeaker,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "目标人物与音频")
        )

        self.ui.GroupBox_ASR_VPR_VPRParams.setTitle(QCA.translate("GroupBox", "语音识别参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_ASR_VPR_VPRParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "语音识别参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_ASR_VPR_DecisionThreshold,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "判断阈值\n判断相似度的阈值，若参与比对的说话人声音相似度较高可以增加该值。")
            )
        )
        self.ui.DoubleSpinBox_ASR_VPR_DecisionThreshold.setRange(0.5, 1)
        self.ui.DoubleSpinBox_ASR_VPR_DecisionThreshold.setSingleStep(0.01)
        ParamsManager_ASR_VPR.SetParam(
            Widget = self.ui.DoubleSpinBox_ASR_VPR_DecisionThreshold,
            Section = 'VPR Params',
            Option = 'DecisionThreshold',
            DefaultValue = 0.75
        )
        self.ui.Button_ASR_VPR_DecisionThreshold_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_VPR.ResetParam(self.ui.DoubleSpinBox_ASR_VPR_DecisionThreshold)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_ASR_VPR_DecisionThreshold,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "语音识别参数"),
            ChildItemText = QCA.translate("Tree", "判断阈值")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_ASR_VPR_ModelPath,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "模型加载路径\n用于加载的声纹识别模型的路径。")
            )
        )
        ASR_VPR_ModelPath_Default = Path(ModelDir).joinpath('ASR', 'VPR', 'Downloaded', 'Ecapa-Tdnn_spectrogram.pth').as_posix()
        ParamsManager_ASR_VPR.SetParam(
            Widget = self.ui.LineEdit_ASR_VPR_ModelPath,
            Section = 'VPR Params',
            Option = 'Model_Path',
            DefaultValue = ASR_VPR_ModelPath_Default,
            SetPlaceholderText = True,
            PlaceholderText = ASR_VPR_ModelPath_Default
        )
        self.ui.LineEdit_ASR_VPR_ModelPath.SetFileDialog(
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('ASR', 'VPR', 'Downloaded'))
        )
        self.ui.Button_ASR_VPR_ModelPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_VPR.ResetParam(self.ui.LineEdit_ASR_VPR_ModelPath),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_ASR_VPR_ModelPath.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_ASR_VPR_ModelPath,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "语音识别参数"),
            ChildItemText = QCA.translate("Tree", "模型加载路径")
        )

        self.ui.ToolBox_ASR_VPR_VPRParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_ASR_VPR_VPRParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_ASR_VPR_ModelType,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "模型类型\n声纹识别模型的类型。")
            )
        )
        self.ui.ComboBox_ASR_VPR_ModelType.addItems(['Ecapa-Tdnn'])
        ParamsManager_ASR_VPR.SetParam(
            Widget = self.ui.ComboBox_ASR_VPR_ModelType,
            Section = 'VPR Params',
            Option = 'Model_Type',
            DefaultValue = 'Ecapa-Tdnn'
        )
        self.ui.Button_ASR_VPR_ModelPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_VPR.ResetParam(self.ui.ComboBox_ASR_VPR_ModelType)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_ASR_VPR_ModelType,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "语音识别参数"),
            ChildItemText = QCA.translate("Tree", "模型类型")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_ASR_VPR_FeatureMethod,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "预处理方法\n音频的预处理方法。")
            )
        )
        self.ui.ComboBox_ASR_VPR_FeatureMethod.addItems(['spectrogram', 'melspectrogram'])
        ParamsManager_ASR_VPR.SetParam(
            Widget = self.ui.ComboBox_ASR_VPR_FeatureMethod,
            Section = 'VPR Params',
            Option = 'Feature_Method',
            DefaultValue = 'spectrogram'
        )
        self.ui.Button_ASR_VPR_FeatureMethod_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_VPR.ResetParam(self.ui.ComboBox_ASR_VPR_FeatureMethod)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_ASR_VPR_FeatureMethod,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "语音识别参数"),
            ChildItemText = QCA.translate("Tree", "预处理方法")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_ASR_VPR_DurationOfAudio,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "音频长度\n用于预测的音频长度。")
            )
        )
        self.ui.DoubleSpinBox_ASR_VPR_DurationOfAudio.setRange(0, 30)
        #self.ui.DoubleSpinBox_ASR_VPR_DurationOfAudio.setSingleStep(0.01)
        ParamsManager_ASR_VPR.SetParam(
            Widget = self.ui.DoubleSpinBox_ASR_VPR_DurationOfAudio,
            Section = 'VPR Params',
            Option = 'Duration_of_Audio',
            DefaultValue = 3.00
        )
        self.ui.Button_ASR_VPR_DurationOfAudio_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_VPR.ResetParam(self.ui.DoubleSpinBox_ASR_VPR_DurationOfAudio)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_ASR_VPR_DurationOfAudio,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "语音识别参数"),
            ChildItemText = QCA.translate("Tree", "音频长度")
        )

        self.ui.GroupBox_ASR_VPR_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_ASR_VPR_OutputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "输出参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_ASR_VPR_OutputDirName,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "输出目录名\n用于保存最后生成的结果文件的目录的名字。")
            )
        )
        ASR_VPR_OutputDirName_Default = str(date.today())
        ParamsManager_ASR_VPR.SetParam(
            Widget = self.ui.LineEdit_ASR_VPR_OutputDirName,
            Section = 'Output Params',
            Option = 'Audio_Dir_Output',
            DefaultValue = '',
            SetPlaceholderText = True,
            PlaceholderText = ASR_VPR_OutputDirName_Default
        )
        self.ui.LineEdit_ASR_VPR_OutputDirName.RemoveFileDialogButton()
        self.ui.Button_ASR_VPR_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_VPR.ResetParam(self.ui.LineEdit_ASR_VPR_OutputDirName),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_ASR_VPR_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_ASR_VPR_OutputDirName,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "输出目录名")
        )

        self.ui.ToolBox_ASR_VPR_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_ASR_VPR_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_ASR_VPR_AudioSpeakersDataName,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "识别结果文本名\n用于保存最后生成的记录音频文件与对应说话人的txt文件的名字。")
            )
        )
        ASR_VPR_AudioSpeakersDataName_Default = "Recgonition_" + str(date.today())
        ParamsManager_ASR_VPR.SetParam(
            Widget = self.ui.LineEdit_ASR_VPR_AudioSpeakersDataName,
            Section = 'Output Params',
            Option = 'FileList_Name',
            DefaultValue = ASR_VPR_AudioSpeakersDataName_Default,
            SetPlaceholderText = True,
            PlaceholderText = ASR_VPR_AudioSpeakersDataName_Default
        )
        self.ui.LineEdit_ASR_VPR_AudioSpeakersDataName.RemoveFileDialogButton()
        self.ui.Button_ASR_VPR_AudioSpeakersDataName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_VPR.ResetParam(self.ui.LineEdit_ASR_VPR_AudioSpeakersDataName),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_ASR_VPR_AudioSpeakersDataName.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_ASR_VPR_AudioSpeakersDataName,
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "识别结果文本名")
        )

        LineEdit_ASR_VPR_OutputDir = QLineEdit()
        def SetText_LineEdit_ASR_VPR_OutputDir():
            DirName = self.ui.LineEdit_ASR_VPR_OutputDirName.text()
            if len(DirName.strip()) == 0:
                Alert = False
            else:
                DirText = Path(self.ui.LineEdit_ASR_VPR_OutputRoot.text()).joinpath(DirName).as_posix()
                LineEdit_ASR_VPR_OutputDir.setText(DirText)
                Alert = Path(DirText).exists() and list(Path(DirText).iterdir()) != []
            self.ui.LineEdit_ASR_VPR_OutputDirName.Alert(True if Alert else False, "注意：目录已包含文件")
        self.ui.LineEdit_ASR_VPR_OutputDirName.interacted.connect(SetText_LineEdit_ASR_VPR_OutputDir)
        self.ui.LineEdit_ASR_VPR_OutputRoot.interacted.connect(SetText_LineEdit_ASR_VPR_OutputDir)
        #SetText_LineEdit_ASR_VPR_OutputDir()

        LineEdit_ASR_VPR_AudioSpeakersDataPath = QLineEdit()
        def SetText_LineEdit_ASR_VPR_AudioSpeakersDataPath():
            FileName = self.ui.LineEdit_ASR_VPR_AudioSpeakersDataName.text()
            if len(FileName.strip()) == 0:
                Alert = False
            else:
                PathText = Path(LineEdit_ASR_VPR_OutputDir.text()).joinpath(FileName).as_posix() + ".txt"
                LineEdit_ASR_VPR_AudioSpeakersDataPath.setText(PathText)
                Alert = Path(PathText).exists()
            self.ui.LineEdit_ASR_VPR_AudioSpeakersDataName.Alert(True if Alert else False, "注意：路径已存在")
        self.ui.LineEdit_ASR_VPR_AudioSpeakersDataName.interacted.connect(SetText_LineEdit_ASR_VPR_AudioSpeakersDataPath)
        LineEdit_ASR_VPR_OutputDir.textChanged.connect(SetText_LineEdit_ASR_VPR_AudioSpeakersDataPath)
        #SetText_LineEdit_ASR_VPR_AudioSpeakersDataPath()

        # ChildWindow
        ChildWindow_ASR = Window_ChildWindow_ASR(self)

        ChildWindow_ASR.ui.Button_Close.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                QMessageBox.Question, "Ask",
                "确认放弃编辑？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_ASR.close()
                    )
                }
            )
        )
        ChildWindow_ASR.ui.Button_Maximize.clicked.connect(lambda: ChildWindow_ASR.showNormal() if ChildWindow_ASR.isMaximized() else ChildWindow_ASR.showMaximized())

        QFunc.Function_SetText(
            Widget = ChildWindow_ASR.ui.Label_Title,
            Text = QFunc.SetRichText(
                Title = QCA.translate("Label", "语音识别结果")
            )
        )
        QFunc.Function_SetText(
            Widget = ChildWindow_ASR.ui.Label_Text,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "这里记录了每个语音文件与其对应的人物名（留空表示无匹配人物且最终不会被保留）\n你可以对这些人物名进行更改并在表格下方设置音频的保存路径")
            )
        )

        ChildWindow_ASR.ui.Table.setHorizontalHeaderLabels(['音频路径', '人物姓名', '相似度', '播放', '操作'])

        ChildWindow_ASR.ui.CheckBox.setText(QCA.translate("CheckBox", "结束编辑时将拥有匹配人物的音频保存到:"))
        ChildWindow_ASR.ui.CheckBox.setChecked(True)
        ChildWindow_ASR.ui.LineEdit.ClearDefaultStyleSheet()
        ChildWindow_ASR.ui.LineEdit.setStyleSheet(ChildWindow_ASR.ui.LineEdit.styleSheet() + 'LineEditBase {border-width: 0px 0px 1px 0px; border-radius: 0px;}')
        LineEdit_ASR_VPR_OutputDir.textChanged.connect(ChildWindow_ASR.ui.LineEdit.setText)
        ChildWindow_ASR.ui.LineEdit.RemoveFileDialogButton()
        ChildWindow_ASR.ui.LineEdit.setReadOnly(True)

        ChildWindow_ASR.ui.Button_Cancel.setText(QCA.translate("Button", "取消"))
        ChildWindow_ASR.ui.Button_Cancel.clicked.connect(ChildWindow_ASR.ui.Button_Close.click)
        ChildWindow_ASR.ui.Button_Save.setText(QCA.translate("Button", "保存"))
        ChildWindow_ASR.ui.Button_Save.clicked.connect(
            lambda: (
                ASRResult_Save(
                    ChildWindow_ASR.ui.Table.GetValue(),
                    LineEdit_ASR_VPR_AudioSpeakersDataPath.text(),
                    False
                ),
                Function_ShowMessageBox(self,
                    QMessageBox.Information, "Tip",
                    "已保存当前结果。"
                )
            )
        )
        ChildWindow_ASR.ui.Button_Confirm.setText(QCA.translate("Button", "确认"))
        ChildWindow_ASR.ui.Button_Confirm.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                QMessageBox.Question, "Ask",
                "确认结束并应用编辑？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        ASRResult_Save(
                            ChildWindow_ASR.ui.Table.GetValue(),
                            LineEdit_ASR_VPR_AudioSpeakersDataPath.text(),
                            ChildWindow_ASR.ui.CheckBox.isChecked(),
                            ChildWindow_ASR.ui.LineEdit.text()
                        ),
                        ChildWindow_ASR.close()
                    )
                }
            )
        )

        # Right
        MonitorFile_Config_VoiceIdentifier = QTasks.MonitorFile(Path_Config_ASR_VPR)
        MonitorFile_Config_VoiceIdentifier.start()
        MonitorFile_Config_VoiceIdentifier.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_ASR_VPR.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_ASR_VPR.setText(QCA.translate("Button", "全部重置"))
        self.ui.Button_ResetSettings_ASR_VPR.clicked.connect(
            lambda: ParamsManager_ASR_VPR.ResetSettings()
        )

        self.ui.Button_ImportSettings_ASR_VPR.setText(QCA.translate("Button", "导入配置"))
        self.ui.Button_ImportSettings_ASR_VPR.clicked.connect(
            lambda: ParamsManager_ASR_VPR.ImportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SelectFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_ASR_VPR.setText(QCA.translate("Button", "导出配置"))
        self.ui.Button_ExportSettings_ASR_VPR.clicked.connect(
            lambda: ParamsManager_ASR_VPR.ExportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SaveFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_EditResult_ASR_VPR.setText(QCA.translate("Button", "编辑识别结果"))
        def EditASRResult():
            ASRResultPath = QFunc.Function_GetFileDialog(
                Mode = "SelectFile",
                FileType = "txt类型 (*.txt)",
                Directory = Path(CurrentDir).joinpath('语音识别结果', 'VPR').as_posix()
            )
            if QFunc.NormPath(ASRResultPath) is not None:
                self.ShowMask(True, "正在加载表单")
                ChildWindow_ASR.ui.Table.SetValue(
                    ASRResult_Get(ASRResultPath),
                    None
                )
                ChildWindow_ASR.exec()
        self.ui.Button_EditResult_ASR_VPR.clicked.connect(EditASRResult)

        self.ui.Button_CheckOutput_ASR_VPR.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_ASR_VPR,
            URL = self.ui.LineEdit_ASR_VPR_OutputRoot,
            ButtonTooltip = "Click to open",
            CreateIfNotExist = True
        )

        # Bottom
        self.ui.Button_ASR_VPR_Execute.setToolTip("执行语音识别")
        self.ui.Button_ASR_VPR_Terminate.setToolTip("终止语音识别")
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_ASR_VPR_Execute,
            TerminateButton = self.ui.Button_ASR_VPR_Terminate,
            ProgressBar = self.ui.ProgressBar_ASR_VPR,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Voice_Identifying_VPR.Execute,
            ParamsFrom = [
                self.ui.Table_ASR_VPR_StdAudioSpeaker,
                self.ui.LineEdit_ASR_VPR_AudioDirInput,
                self.ui.LineEdit_ASR_VPR_ModelPath,
                self.ui.ComboBox_ASR_VPR_ModelType,
                self.ui.ComboBox_ASR_VPR_FeatureMethod,
                self.ui.DoubleSpinBox_ASR_VPR_DecisionThreshold,
                self.ui.DoubleSpinBox_ASR_VPR_DurationOfAudio,
                self.ui.LineEdit_ASR_VPR_OutputRoot,
                self.ui.LineEdit_ASR_VPR_OutputDirName,
                self.ui.LineEdit_ASR_VPR_AudioSpeakersDataName
            ],
            FinishEvents = [
                lambda: self.ShowMask(True, "正在加载表单"),
                lambda: ChildWindow_ASR.ui.Table.SetValue(
                    ASRResult_Get(LineEdit_ASR_VPR_AudioSpeakersDataPath.text()),
                    list(self.ui.Table_ASR_VPR_StdAudioSpeaker.GetValue().keys()) + ['']
                ),
                ChildWindow_ASR.exec,
                lambda: Function_ShowMessageBox(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        #############################################################
        ######################## Content: STT #######################
        #############################################################

        # Guidance
        DialogBox_STT = MessageBox_Stacked(self)
        DialogBox_STT.setWindowTitle(QCA.translate("MsgBox", "引导（仅出现一次）"))
        DialogBox_STT.SetContent(
            [
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_STT.png')),
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
            ],
            [
                '欢迎来到语音转录工具界面\n该工具用于将语音文件批量转换为字幕文件并进行语言标注等操作',
                '顶部区域用于切换当前工具类型\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_STT.clicked.connect(
            lambda: (
                DialogBox_STT.exec(),
                Config.EditConfig('Dialog', 'GuidanceShown_STT', 'True')
            ) if eval(Config.GetValue('Dialog', 'GuidanceShown_STT', 'False')) is False else None
        )

        self.ui.Button_VoiceTranscriber_Help.clicked.connect(
            lambda: DialogBox_STT.exec()
        )

        # ParamsManager
        Path_Config_STT_Whisper = QFunc.NormPath(Path(ConfigDir).joinpath('Config_STT_Whisper.ini'))
        ParamsManager_STT_Whisper = ParamsManager(Path_Config_STT_Whisper)

        # Top
        self.ui.ToolButton_VoiceTranscriber_Title.setText(QCA.translate("ToolButton", "Whisper"))
        self.ui.ToolButton_VoiceTranscriber_Title.setCheckable(True)
        self.ui.ToolButton_VoiceTranscriber_Title.setChecked(True)
        self.ui.ToolButton_VoiceTranscriber_Title.setAutoExclusive(True)
        self.ui.ToolButton_VoiceTranscriber_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_STT,
                TargetIndex = 0
            )
        )

        # Left
        self.ui.TreeWidget_Catalogue_STT_Whisper.clear()
        self.ui.TreeWidget_Catalogue_STT_Whisper.setHeaderHidden(True)

        # Middle
        self.ui.GroupBox_STT_Whisper_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_STT_Whisper_InputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_STT_Whisper,
            RootItemText = QCA.translate("Tree", "输入参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_STT_Whisper_AudioDir,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "音频输入目录\n需要将语音内容转为文字的音频文件的所在目录。")
            )
        )
        ParamsManager_STT_Whisper.SetParam(
            Widget = self.ui.LineEdit_STT_Whisper_AudioDir,
            Section = 'Input Params',
            Option = 'Audio_Dir',
            DefaultValue = '',
            SetPlaceholderText = True
        )
        self.ui.LineEdit_STT_Whisper_AudioDir.SetFileDialog(
            Mode = "SelectFolder"
        )
        self.ui.Button_STT_Whisper_AudioDir_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_STT_Whisper.ResetParam(self.ui.LineEdit_STT_Whisper_AudioDir),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_STT_Whisper_AudioDir.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_STT_Whisper_AudioDir,
            TreeWidget = self.ui.TreeWidget_Catalogue_STT_Whisper,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "音频输入目录")
        )

        self.ui.GroupBox_STT_Whisper_WhisperParams.setTitle(QCA.translate("GroupBox", "语音转录参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_STT_Whisper_WhisperParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_STT_Whisper,
            RootItemText = QCA.translate("Tree", "语音转录参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_STT_Whisper_AddLanguageInfo,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "语种标注\n标注音频中说话人所使用的语言，若用于数据集制作则建议启用。")
            )
        )
        ParamsManager_STT_Whisper.SetParam(
            Widget = self.ui.CheckBox_STT_Whisper_AddLanguageInfo,
            Section = 'Whisper Params',
            Option = 'Add_LanguageInfo',
            DefaultValue = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_STT_Whisper_AddLanguageInfo,
            CheckedText = "已启用",
            CheckedEvents = [
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
            ],
            TakeEffect = True
        )
        self.ui.Button_STT_Whisper_AddLanguageInfo_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_STT_Whisper.ResetParam(self.ui.CheckBox_STT_Whisper_AddLanguageInfo)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_STT_Whisper_AddLanguageInfo,
            TreeWidget = self.ui.TreeWidget_Catalogue_STT_Whisper,
            RootItemText = QCA.translate("Tree", "语音转录参数"),
            ChildItemText = QCA.translate("Tree", "语种标注")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_STT_Whisper_ModelPath,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "模型加载路径\n用于加载的Whisper模型的路径。")
            )
        )
        STT_Whisper_ModelPath_Default = Path(ModelDir).joinpath('STT', 'Whisper', 'Downloaded', 'small.pt').as_posix()
        ParamsManager_STT_Whisper.SetParam(
            Widget = self.ui.LineEdit_STT_Whisper_ModelPath,
            Section = 'Whisper Params',
            Option = 'Model_Path',
            DefaultValue = STT_Whisper_ModelPath_Default,
            SetPlaceholderText = True,
            PlaceholderText = STT_Whisper_ModelPath_Default
        )
        self.ui.LineEdit_STT_Whisper_ModelPath.SetFileDialog(
            Mode = "SelectFile",
            FileType = "pt类型 (*.pt)",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('STT', 'Whisper', 'Downloaded'))
        )
        self.ui.Button_STT_Whisper_ModelPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_STT_Whisper.ResetParam(self.ui.LineEdit_STT_Whisper_ModelPath),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_STT_Whisper_ModelPath.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_STT_Whisper_ModelPath,
            TreeWidget = self.ui.TreeWidget_Catalogue_STT_Whisper,
            RootItemText = QCA.translate("Tree", "语音转录参数"),
            ChildItemText = QCA.translate("Tree", "模型加载路径")
        )

        self.ui.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_STT_Whisper_Verbose,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "显示转录内容\n启用该项后会在运行过程中显示转录的内容，否则只显示进度。")
            )
        )
        ParamsManager_STT_Whisper.SetParam(
            Widget = self.ui.CheckBox_STT_Whisper_Verbose,
            Section = 'Whisper Params',
            Option = 'Verbose',
            DefaultValue = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_STT_Whisper_Verbose,
            CheckedText = "已启用",
            CheckedEvents = [
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
            ],
            TakeEffect = True
        )
        self.ui.Button_STT_Whisper_Verbose_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_STT_Whisper.ResetParam(self.ui.CheckBox_STT_Whisper_Verbose)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_STT_Whisper_Verbose,
            TreeWidget = self.ui.TreeWidget_Catalogue_STT_Whisper,
            RootItemText = QCA.translate("Tree", "语音转录参数"),
            ChildItemText = QCA.translate("Tree", "显示转录内容")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_STT_Whisper_fp16,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "半精度计算\n主要使用半精度浮点数进行计算，若GPU不可用则忽略或禁用此项。")
            )
        )
        ParamsManager_STT_Whisper.SetParam(
            Widget = self.ui.CheckBox_STT_Whisper_fp16,
            Section = 'Whisper Params',
            Option = 'fp16',
            DefaultValue = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_STT_Whisper_fp16,
            CheckedText = "已启用",
            CheckedEvents = [
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
            ],
            TakeEffect = True
        )
        self.ui.Button_STT_Whisper_fp16_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_STT_Whisper.ResetParam(self.ui.CheckBox_STT_Whisper_fp16)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_STT_Whisper_fp16,
            TreeWidget = self.ui.TreeWidget_Catalogue_STT_Whisper,
            RootItemText = QCA.translate("Tree", "语音转录参数"),
            ChildItemText = QCA.translate("Tree", "半精度计算")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_STT_Whisper_ConditionOnPreviousText,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "关联上下文\n在音频之间的内容具有关联性时启用该项可以获得更好的效果。")
            )
        )
        ParamsManager_STT_Whisper.SetParam(
            Widget = self.ui.CheckBox_STT_Whisper_ConditionOnPreviousText,
            Section = 'Whisper Params',
            Option = 'Condition_on_Previous_Text',
            DefaultValue = False
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_STT_Whisper_ConditionOnPreviousText,
            CheckedText = "已启用",
            CheckedEvents = [
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
            ],
            TakeEffect = True
        )
        self.ui.Button_STT_Whisper_ConditionOnPreviousText_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_STT_Whisper.ResetParam(self.ui.CheckBox_STT_Whisper_ConditionOnPreviousText)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_STT_Whisper_ConditionOnPreviousText,
            TreeWidget = self.ui.TreeWidget_Catalogue_STT_Whisper,
            RootItemText = QCA.translate("Tree", "语音转录参数"),
            ChildItemText = QCA.translate("Tree", "关联上下文")
        )

        self.ui.GroupBox_STT_Whisper_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_STT_Whisper_OutputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_STT_Whisper,
            RootItemText = QCA.translate("Tree", "输出参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_STT_Whisper_OutputDirName,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "输出目录名\n用于保存最后生成的字幕文件的目录的名字。")
            )
        )
        STT_Whisper_OutputDirName_Default = str(date.today())
        ParamsManager_STT_Whisper.SetParam(
            Widget = self.ui.LineEdit_STT_Whisper_OutputDirName,
            Section = 'Output Params',
            Option = 'SRT_Dir_Name',
            DefaultValue = '',
            SetPlaceholderText = True,
            PlaceholderText = STT_Whisper_OutputDirName_Default
        )
        self.ui.LineEdit_STT_Whisper_OutputDirName.RemoveFileDialogButton()
        self.ui.Button_STT_Whisper_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_STT_Whisper.ResetParam(self.ui.LineEdit_STT_Whisper_OutputDirName),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_STT_Whisper_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_STT_Whisper_OutputDirName,
            TreeWidget = self.ui.TreeWidget_Catalogue_STT_Whisper,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "输出目录名")
        )

        LineEdit_STT_Whisper_OutputDir = QLineEdit()
        def SetText_LineEdit_STT_Whisper_OutputDir():
            DirName = self.ui.LineEdit_STT_Whisper_OutputDirName.text()
            if len(DirName.strip()) == 0:
                Alert = False
            else:
                DirText = Path(self.ui.LineEdit_STT_Whisper_OutputRoot.text()).joinpath(DirName).as_posix()
                LineEdit_STT_Whisper_OutputDir.setText(DirText)
                Alert = Path(DirText).exists() and list(Path(DirText).iterdir()) != []
            self.ui.LineEdit_STT_Whisper_OutputDirName.Alert(True if Alert else False, "注意：目录已包含文件")
        self.ui.LineEdit_STT_Whisper_OutputDirName.interacted.connect(SetText_LineEdit_STT_Whisper_OutputDir)
        self.ui.LineEdit_STT_Whisper_OutputRoot.interacted.connect(SetText_LineEdit_STT_Whisper_OutputDir)
        #SetText_LineEdit_STT_Whisper_OutputDir()

        # ChildWindow
        ChildWindow_STT = Window_ChildWindow_STT(self)

        ChildWindow_STT.ui.Button_Close.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                QMessageBox.Question, "Ask",
                "确认放弃编辑？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_STT.close()
                    )
                }
            )
        )
        ChildWindow_STT.ui.Button_Maximize.clicked.connect(lambda: ChildWindow_STT.showNormal() if ChildWindow_STT.isMaximized() else ChildWindow_STT.showMaximized())

        QFunc.Function_SetText(
            Widget = ChildWindow_STT.ui.Label_Title,
            Text = QFunc.SetRichText(
                Title = QCA.translate("Label", "语音转录结果")
            )
        )
        QFunc.Function_SetText(
            Widget = ChildWindow_STT.ui.Label_Text,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "这里记录了每个语音文件与其对应的字幕文本（包含了时间戳）\n你可以对这些文本进行更改，若启用了语种标注则小心不要误删")
            )
        )

        ChildWindow_STT.ui.Table.setHorizontalHeaderLabels(['音频路径', '音频内容', '播放'])

        ChildWindow_STT.ui.Button_Cancel.setText(QCA.translate("Button", "取消"))
        ChildWindow_STT.ui.Button_Cancel.clicked.connect(ChildWindow_STT.ui.Button_Close.click)
        ChildWindow_STT.ui.Button_Confirm.setText(QCA.translate("Button", "确认"))
        ChildWindow_STT.ui.Button_Confirm.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                QMessageBox.Question, "Ask",
                "确认应用编辑？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        STTResult_Save(
                            ChildWindow_STT.ui.Table.GetValue(),
                            LineEdit_STT_Whisper_OutputDir.text()
                        ),
                        ChildWindow_STT.close()
                    )
                }
            )
        )

        # Right
        MonitorFile_Config_VoiceTranscriber = QTasks.MonitorFile(Path_Config_STT_Whisper)
        MonitorFile_Config_VoiceTranscriber.start()
        MonitorFile_Config_VoiceTranscriber.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_STT_Whisper.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_STT_Whisper.setText(QCA.translate("Button", "全部重置"))
        self.ui.Button_ResetSettings_STT_Whisper.clicked.connect(
            lambda: ParamsManager_STT_Whisper.ResetSettings()
        )

        self.ui.Button_ImportSettings_STT_Whisper.setText(QCA.translate("Button", "导入配置"))
        self.ui.Button_ImportSettings_STT_Whisper.clicked.connect(
            lambda: ParamsManager_STT_Whisper.ImportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SelectFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_STT_Whisper.setText(QCA.translate("Button", "导出配置"))
        self.ui.Button_ExportSettings_STT_Whisper.clicked.connect(
            lambda: ParamsManager_STT_Whisper.ExportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SaveFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_CheckOutput_STT_Whisper.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_STT_Whisper,
            URL = self.ui.LineEdit_STT_Whisper_OutputRoot,
            ButtonTooltip = "Click to open",
            CreateIfNotExist = True
        )

        # Bottom
        self.ui.Button_STT_Whisper_Execute.setToolTip("执行语音转录")
        self.ui.Button_STT_Whisper_Terminate.setToolTip("终止语音转录")
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_STT_Whisper_Execute,
            TerminateButton = self.ui.Button_STT_Whisper_Terminate,
            ProgressBar = self.ui.ProgressBar_STT_Whisper,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Voice_Transcribing_Whisper.Execute,
            ParamsFrom = [
                self.ui.LineEdit_STT_Whisper_ModelPath,
                self.ui.LineEdit_STT_Whisper_AudioDir,
                self.ui.CheckBox_STT_Whisper_Verbose,
                self.ui.CheckBox_STT_Whisper_AddLanguageInfo,
                self.ui.CheckBox_STT_Whisper_ConditionOnPreviousText,
                self.ui.CheckBox_STT_Whisper_fp16,
                self.ui.LineEdit_STT_Whisper_OutputRoot,
                self.ui.LineEdit_STT_Whisper_OutputDirName
            ],
            FinishEvents = [
                lambda: self.ShowMask(True, "正在加载表单"),
                lambda: ChildWindow_STT.ui.Table.SetValue(
                    STTResult_Get(LineEdit_STT_Whisper_OutputDir.text(), self.ui.LineEdit_STT_Whisper_AudioDir.text())
                ),
                ChildWindow_STT.exec,
                lambda: Function_ShowMessageBox(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        #############################################################
        ###################### Content: Dataset #####################
        #############################################################

        # Guidance
        DialogBox_Dataset = MessageBox_Stacked(self)
        DialogBox_Dataset.setWindowTitle(QCA.translate("MsgBox", "引导（仅出现一次）"))
        DialogBox_Dataset.SetContent(
            [
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_Dataset.png')),
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
            ],
            [
                '欢迎来到数据集工具界面\n该工具用于生成适用于语音模型训练的数据集',
                '顶部区域用于切换当前工具类型\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_Dataset.clicked.connect(
            lambda: (
                DialogBox_Dataset.exec(),
                Config.EditConfig('Dialog', 'GuidanceShown_Dataset', 'True')
            ) if eval(Config.GetValue('Dialog', 'GuidanceShown_Dataset', 'False')) is False else None
        )

        self.ui.Button_DatasetCreator_Help.clicked.connect(
            lambda: DialogBox_Dataset.exec()
        )

        # GPT-SoVITS - ParamsManager
        Path_Config_DAT_GPTSoVITS = QFunc.NormPath(Path(ConfigDir).joinpath('Config_DAT_GPT-SoVITS.ini'))
        ParamsManager_DAT_GPTSoVITS = ParamsManager(Path_Config_DAT_GPTSoVITS)

        # GPT-SoVITS - Top
        self.ui.ToolButton_DatasetCreator_Title_GPTSoVITS.setText(QCA.translate("ToolButton", "GPT-SoVITS"))
        self.ui.ToolButton_DatasetCreator_Title_GPTSoVITS.setCheckable(True)
        self.ui.ToolButton_DatasetCreator_Title_GPTSoVITS.setChecked(True)
        self.ui.ToolButton_DatasetCreator_Title_GPTSoVITS.setAutoExclusive(True)
        self.ui.ToolButton_DatasetCreator_Title_GPTSoVITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Dataset,
                TargetIndex = 0
            )
        )

        # GPT-SoVITS - Left
        self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS.clear()
        self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS.setHeaderHidden(True)

        # GPT-SoVITS - Middle
        self.ui.GroupBox_DAT_GPTSoVITS_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_DAT_GPTSoVITS_InputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输入参数")
        )

        DialogBox_GPTSoVITS_AudioSpeakersDataPath = MessageBox_Buttons(self)
        DialogBox_GPTSoVITS_AudioSpeakersDataPath.setText(QCA.translate("MsgBox", "请选择参数类型"))
        DialogBox_GPTSoVITS_AudioSpeakersDataPath.Button1.setText(QCA.translate("Button", "音频文件目录"))
        DialogBox_GPTSoVITS_AudioSpeakersDataPath.Button1.clicked.connect(
            lambda: (
                self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.setText(
                    QFunc.Function_GetFileDialog(
                        Mode = "SelectFolder",
                        Directory = QFunc.NormPath(Path(ChildWindow_ASR.ui.LineEdit.text()))
                    )
                ),
                DialogBox_GPTSoVITS_AudioSpeakersDataPath.close(),
            )
        )
        DialogBox_GPTSoVITS_AudioSpeakersDataPath.Button2.setText(QCA.translate("Button", "语音识别结果文本路径"))
        DialogBox_GPTSoVITS_AudioSpeakersDataPath.Button2.clicked.connect(
            lambda: (
                self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.setText(
                    QFunc.Function_GetFileDialog(
                        Mode = "SelectFile",
                        FileType = "txt类型 (*.txt)",
                        Directory = Path(CurrentDir).joinpath('语音识别结果', 'VPR').as_posix()
                    )
                ),
                DialogBox_GPTSoVITS_AudioSpeakersDataPath.close(),
            )
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_GPTSoVITS_AudioSpeakersDataPath,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "音频文件目录/语音识别结果文本路径\n音频文件的所在目录，或者提供由语音识别得到的文本文件。")
            )
        )
        ParamsManager_DAT_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath,
            Section = 'Input Params',
            Option = 'WAV_Dir',
            DefaultValue = '',
            SetPlaceholderText = True
        )
        self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.Button.clicked.connect(
            lambda: DialogBox_GPTSoVITS_AudioSpeakersDataPath.exec()
        )
        self.ui.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_GPTSoVITS_AudioSpeakersDataPath,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "音频文件目录")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_GPTSoVITS_SRTDir,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "字幕输入目录\n字幕文件的所在目录，字幕文件须与对应音频文件同名且在文本中注明所属语言。")
            )
        )
        ParamsManager_DAT_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_DAT_GPTSoVITS_SRTDir,
            Section = 'Input Params',
            Option = 'SRT_Dir',
            DefaultValue = '',
            SetPlaceholderText = True
        )
        self.ui.LineEdit_DAT_GPTSoVITS_SRTDir.SetFileDialog(
            Mode = "SelectFolder",
            Directory = Path(CurrentDir).joinpath('语音转录结果', 'Whisper').as_posix()
        )
        self.ui.Button_DAT_GPTSoVITS_SRTDir_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_SRTDir),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_GPTSoVITS_SRTDir.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_GPTSoVITS_SRTDir,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "字幕输入目录")
        )

        self.ui.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams.setTitle(QCA.translate("GroupBox", "数据集参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "数据集参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_GPTSoVITS_DataFormat,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "数据文本格式\n数据集的文本格式，默认使用GPT-SoVITS的标准。")
            )
        )
        DAT_GPTSoVITS_DataFormat_Default = '路径|人名|语言|文本'
        ParamsManager_DAT_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_DAT_GPTSoVITS_DataFormat,
            Section = 'GPT-SoVITS Params',
            Option = 'DataFormat_Path',
            DefaultValue = DAT_GPTSoVITS_DataFormat_Default,
            SetPlaceholderText = True,
            PlaceholderText = DAT_GPTSoVITS_DataFormat_Default
        )
        self.ui.LineEdit_DAT_GPTSoVITS_DataFormat.textChanged.connect(
            lambda Value: (
                Function_ShowMessageBox(self,
                    MessageType = QMessageBox.Warning,
                    WindowTitle = "Warning",
                    Text = "请保留关键词：'路径'，'人名'，'语言'，'文本'",
                ),
                ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_DataFormat),
            ) if not all(Keyword in Value for Keyword in ['路径', '人名', '语言', '文本']) else None
        )
        self.ui.LineEdit_DAT_GPTSoVITS_DataFormat.RemoveFileDialogButton()
        self.ui.Button_DAT_GPTSoVITS_DataFormat_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_DataFormat),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_GPTSoVITS_DataFormat.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_GPTSoVITS_DataFormat,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "数据集参数"),
            ChildItemText = QCA.translate("Tree", "数据文本格式")
        )

        self.ui.GroupBox_DAT_GPTSoVITS_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_DAT_GPTSoVITS_OutputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输出参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_GPTSoVITS_OutputDirName,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "输出目录名\n用于保存最后生成的数据集文件的目录的名字。")
            )
        )
        DAT_GPTSoVITS_OutputDirName_Default = str(date.today())
        ParamsManager_DAT_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName,
            Section = 'Output Params',
            Option = 'Output_Dir_Name',
            DefaultValue = '',
            SetPlaceholderText = True,
            PlaceholderText = DAT_GPTSoVITS_OutputDirName_Default
        )
        self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName.RemoveFileDialogButton()
        self.ui.Button_DAT_GPTSoVITS_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_GPTSoVITS_OutputDirName,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "输出目录名")
        )

        self.ui.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_GPTSoVITS_FileListName,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "数据集文本名\n用于保存最后生成的数据集txt文件的名字。")
            )
        )
        DAT_GPTSoVITS_FileListName_Default = "Train_" + str(date.today())
        ParamsManager_DAT_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_DAT_GPTSoVITS_FileListName,
            Section = 'Output Params',
            Option = 'FileList_Name',
            DefaultValue = DAT_GPTSoVITS_FileListName_Default,
            SetPlaceholderText = True,
            PlaceholderText = DAT_GPTSoVITS_FileListName_Default
        )
        self.ui.LineEdit_DAT_GPTSoVITS_FileListName.RemoveFileDialogButton()
        self.ui.Button_DAT_GPTSoVITS_FileListName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_FileListName),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_GPTSoVITS_FileListName.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_GPTSoVITS_FileListName,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "数据集文本名")
        )

        LineEdit_DAT_GPTSoVITS_OutputDir = QLineEdit()
        def SetText_LineEdit_DAT_GPTSoVITS_OutputDir():
            DirName = self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName.text()
            if len(DirName.strip()) == 0:
                Alert = False
            else:
                DirText = Path(self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot.text()).joinpath(DirName).as_posix()
                LineEdit_DAT_GPTSoVITS_OutputDir.setText(DirText)
                Alert = Path(DirText).exists() and list(Path(DirText).iterdir()) != []
            self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName.Alert(True if Alert else False, "注意：目录已包含文件")
        self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName.interacted.connect(SetText_LineEdit_DAT_GPTSoVITS_OutputDir)
        self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot.interacted.connect(SetText_LineEdit_DAT_GPTSoVITS_OutputDir)
        #SetText_LineEdit_DAT_GPTSoVITS_OutputDir()

        LineEdit_DAT_GPTSoVITS_FileListPath = QLineEdit()
        def SetText_LineEdit_DAT_GPTSoVITS_FileListPath():
            FileName = self.ui.LineEdit_DAT_GPTSoVITS_FileListName.text()
            if len(FileName.strip()) == 0:
                Alert = False
            else:
                PathText = Path(LineEdit_DAT_GPTSoVITS_OutputDir.text()).joinpath(FileName).as_posix() + ".txt"
                LineEdit_DAT_GPTSoVITS_FileListPath.setText(PathText)
                Alert = Path(PathText).exists()
            self.ui.LineEdit_DAT_GPTSoVITS_FileListName.Alert(True if Alert else False, "注意：路径已存在")
        self.ui.LineEdit_DAT_GPTSoVITS_FileListName.interacted.connect(SetText_LineEdit_DAT_GPTSoVITS_FileListPath)
        LineEdit_DAT_GPTSoVITS_OutputDir.textChanged.connect(SetText_LineEdit_DAT_GPTSoVITS_FileListPath)
        #SetText_LineEdit_DAT_GPTSoVITS_FileListPath()

        # ChildWindow
        ChildWindow_DAT_GPTSoVITS = Window_ChildWindow_DAT_GPTSoVITS(self)

        ChildWindow_DAT_GPTSoVITS.ui.Button_Close.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                QMessageBox.Question, "Ask",
                "确认放弃编辑？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_DAT_GPTSoVITS.close()
                    )
                }
            )
        )
        ChildWindow_DAT_GPTSoVITS.ui.Button_Maximize.clicked.connect(lambda: ChildWindow_DAT_GPTSoVITS.showNormal() if ChildWindow_DAT_GPTSoVITS.isMaximized() else ChildWindow_DAT_GPTSoVITS.showMaximized())

        QFunc.Function_SetText(
            Widget = ChildWindow_DAT_GPTSoVITS.ui.Label_Title,
            Text = QFunc.SetRichText(
                Title = QCA.translate("Label", "数据集制作结果")
            )
        )
        QFunc.Function_SetText(
            Widget = ChildWindow_DAT_GPTSoVITS.ui.Label_Text,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "这里记录了每个语音文件与其对应的数据文本\n你可以对这些文本进行更改")
            )
        )

        ChildWindow_DAT_GPTSoVITS.ui.Table.setHorizontalHeaderLabels(['数据文本', '播放'])

        ChildWindow_DAT_GPTSoVITS.ui.Button_Cancel.setText(QCA.translate("Button", "取消"))
        ChildWindow_DAT_GPTSoVITS.ui.Button_Cancel.clicked.connect(ChildWindow_DAT_GPTSoVITS.ui.Button_Close.click)
        ChildWindow_DAT_GPTSoVITS.ui.Button_Confirm.setText(QCA.translate("Button", "确认"))
        ChildWindow_DAT_GPTSoVITS.ui.Button_Confirm.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                QMessageBox.Question, "Ask",
                "确认应用编辑？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        DATResult_Save(
                            ChildWindow_DAT_GPTSoVITS.ui.Table.GetValue(),
                            LineEdit_DAT_GPTSoVITS_FileListPath.text()
                        ),
                        ChildWindow_DAT_GPTSoVITS.close()
                    )
                }
            )
        )

        # GPT-SoVITS - Right
        MonitorFile_Config_DatasetCreator_GPTSoVITS = QTasks.MonitorFile(Path_Config_DAT_GPTSoVITS)
        MonitorFile_Config_DatasetCreator_GPTSoVITS.start()
        MonitorFile_Config_DatasetCreator_GPTSoVITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_DAT_GPTSoVITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_DAT_GPTSoVITS.setText(QCA.translate("Button", "全部重置"))
        self.ui.Button_ResetSettings_DAT_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_DAT_GPTSoVITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_DAT_GPTSoVITS.setText(QCA.translate("Button", "导入配置"))
        self.ui.Button_ImportSettings_DAT_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_DAT_GPTSoVITS.ImportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SelectFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_DAT_GPTSoVITS.setText(QCA.translate("Button", "导出配置"))
        self.ui.Button_ExportSettings_DAT_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_DAT_GPTSoVITS.ExportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SaveFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_CheckOutput_DAT_GPTSoVITS.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_DAT_GPTSoVITS,
            URL = self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot,
            ButtonTooltip = "Click to open",
            CreateIfNotExist = True
        )

        # GPT-SoVITS - Bottom
        self.ui.Button_DAT_GPTSoVITS_Execute.setToolTip("执行数据集制作")
        self.ui.Button_DAT_GPTSoVITS_Terminate.setToolTip("终止数据集制作")
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_DAT_GPTSoVITS_Execute,
            TerminateButton = self.ui.Button_DAT_GPTSoVITS_Terminate,
            ProgressBar = self.ui.ProgressBar_DAT_GPTSoVITS,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Dataset_Creating_GPTSoVITS.Execute,
            ParamsFrom = [
                self.ui.LineEdit_DAT_GPTSoVITS_SRTDir,
                self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath,
                self.ui.LineEdit_DAT_GPTSoVITS_DataFormat,
                self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot,
                self.ui.LineEdit_DAT_GPTSoVITS_OutputDirName,
                self.ui.LineEdit_DAT_GPTSoVITS_FileListName
            ],
            EmptyAllowed = [
            ],
            FinishEvents = [
                lambda: self.ShowMask(True, "正在加载表单"),
                lambda: ChildWindow_DAT_GPTSoVITS.ui.Table.SetValue(
                    DATResult_Get(LineEdit_DAT_GPTSoVITS_FileListPath.text())
                ),
                ChildWindow_DAT_GPTSoVITS.exec,
                lambda: Function_ShowMessageBox(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        # VITS - ParamsManager
        Path_Config_DAT_VITS = QFunc.NormPath(Path(ConfigDir).joinpath('Config_DAT_VITS.ini'))
        ParamsManager_DAT_VITS = ParamsManager(Path_Config_DAT_VITS)

        # VITS - Top
        self.ui.ToolButton_DatasetCreator_Title_VITS.setText(QCA.translate("ToolButton", "VITS2"))
        self.ui.ToolButton_DatasetCreator_Title_VITS.setCheckable(True)
        self.ui.ToolButton_DatasetCreator_Title_VITS.setChecked(False)
        self.ui.ToolButton_DatasetCreator_Title_VITS.setAutoExclusive(True)
        self.ui.ToolButton_DatasetCreator_Title_VITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Dataset,
                TargetIndex = 1
            )
        )

        # VITS - Left
        self.ui.TreeWidget_Catalogue_DAT_VITS.clear()
        self.ui.TreeWidget_Catalogue_DAT_VITS.setHeaderHidden(True)

        # VITS - Middle
        self.ui.GroupBox_DAT_VITS_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_DAT_VITS_InputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "输入参数")
        )

        DialogBox_VITS_AudioSpeakersDataPath = MessageBox_Buttons(self)
        DialogBox_VITS_AudioSpeakersDataPath.setText(QCA.translate("MsgBox", "请选择参数类型"))
        DialogBox_VITS_AudioSpeakersDataPath.Button1.setText(QCA.translate("Button", "音频文件目录"))
        DialogBox_VITS_AudioSpeakersDataPath.Button1.clicked.connect(
            lambda: (
                self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath.setText(
                    QFunc.Function_GetFileDialog(
                        Mode = "SelectFolder",
                        Directory = QFunc.NormPath(Path(ChildWindow_ASR.ui.LineEdit.text()))
                    )
                ),
                DialogBox_VITS_AudioSpeakersDataPath.close(),
            )
        )
        DialogBox_VITS_AudioSpeakersDataPath.Button2.setText(QCA.translate("Button", "语音识别结果文本路径"))
        DialogBox_VITS_AudioSpeakersDataPath.Button2.clicked.connect(
            lambda: (
                self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath.setText(
                    QFunc.Function_GetFileDialog(
                        Mode = "SelectFile",
                        FileType = "txt类型 (*.txt)",
                        Directory = Path(CurrentDir).joinpath('语音识别结果', 'VPR').as_posix()
                    )
                ),
                DialogBox_VITS_AudioSpeakersDataPath.close(),
            )
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_AudioSpeakersDataPath,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "音频文件目录/语音识别结果文本路径\n音频文件的所在目录（要求按说话人分类），或者提供由语音识别得到的文本文件。")
            )
        )
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath,
            Section = 'Input Params',
            Option = 'WAV_Dir',
            DefaultValue = '',
            SetPlaceholderText = True
        )
        self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath.Button.clicked.connect(
            lambda: DialogBox_VITS_AudioSpeakersDataPath.exec()
        )
        self.ui.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_AudioSpeakersDataPath,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "音频文件目录")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_SRTDir,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "字幕输入目录\n字幕文件的所在目录，字幕文件须与对应音频文件同名且在文本中注明所属语言。")
            )
        )
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.LineEdit_DAT_VITS_SRTDir,
            Section = 'Input Params',
            Option = 'SRT_Dir',
            DefaultValue = '',
            SetPlaceholderText = True
        )
        self.ui.LineEdit_DAT_VITS_SRTDir.SetFileDialog(
            Mode = "SelectFolder",
            Directory = Path(CurrentDir).joinpath('语音转录结果', 'Whisper').as_posix()
        )
        self.ui.Button_DAT_VITS_SRTDir_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_SRTDir),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_VITS_SRTDir.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_SRTDir,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "字幕输入目录")
        )

        self.ui.GroupBox_DAT_VITS_VITSParams.setTitle(QCA.translate("GroupBox", "数据集参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_DAT_VITS_VITSParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "数据集参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_DataFormat,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "数据文本格式\n数据集的文本格式，默认使用VITS的标准。")
            )
        )
        DAT_VITS_DataFormat_Default = '路径|人名|[语言]文本[语言]'
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.LineEdit_DAT_VITS_DataFormat,
            Section = 'VITS Params',
            Option = 'DataFormat_Path',
            DefaultValue = DAT_VITS_DataFormat_Default,
            SetPlaceholderText = True,
            PlaceholderText = DAT_VITS_DataFormat_Default
        )
        self.ui.LineEdit_DAT_VITS_DataFormat.textChanged.connect(
            lambda Value: (
                Function_ShowMessageBox(self,
                    MessageType = QMessageBox.Warning,
                    WindowTitle = "Warning",
                    Text = "请保留关键词：'路径'，'人名'，'语言'，'文本'",
                ),
                ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_DataFormat),
            ) if not all(Keyword in Value for Keyword in ['路径', '人名', '语言', '文本']) else None
        )
        self.ui.LineEdit_DAT_VITS_DataFormat.RemoveFileDialogButton()
        self.ui.Button_DAT_VITS_DataFormat_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_DataFormat),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_VITS_DataFormat.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_DataFormat,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "数据集参数"),
            ChildItemText = QCA.translate("Tree", "数据文本格式")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_AddAuxiliaryData,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "添加辅助数据\n添加用以辅助训练的数据集，若当前语音数据的质量/数量较低则建议启用。")
            )
        )
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.CheckBox_DAT_VITS_AddAuxiliaryData,
            Section = 'VITS Params',
            Option = 'Add_AuxiliaryData',
            DefaultValue = False
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_DAT_VITS_AddAuxiliaryData,
            CheckedText = "已启用",
            CheckedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_DAT_VITS_VITSParams_BasicSettings,
                    [
                        self.ui.Frame_DAT_VITS_AuxiliaryDataPath
                    ],
                    True
                )
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_DAT_VITS_VITSParams_BasicSettings,
                    [
                        self.ui.Frame_DAT_VITS_AuxiliaryDataPath
                    ],
                    False
                )
            ],
            TakeEffect = True
        )
        self.ui.Button_DAT_VITS_AddAuxiliaryData_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.CheckBox_DAT_VITS_AddAuxiliaryData)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_AddAuxiliaryData,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "数据集参数"),
            ChildItemText = QCA.translate("Tree", "添加辅助数据")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_AuxiliaryDataPath,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "辅助数据文本路径\n辅助数据集的文本的路径。")
            )
        )
        DAT_VITS_AuxiliaryDataPath_Default = Path(CurrentDir).joinpath('AuxiliaryData', 'VITS', 'AuxiliaryData.txt').as_posix()
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath,
            Section = 'VITS Params',
            Option = 'AuxiliaryData_Path',
            DefaultValue = DAT_VITS_AuxiliaryDataPath_Default,
            SetPlaceholderText = True,
            PlaceholderText = DAT_VITS_AuxiliaryDataPath_Default
        )
        self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath.SetFileDialog(
            Mode = "SelectFile",
            FileType = "文本类型 (*.csv *.txt)",
            Directory = QFunc.NormPath(Path(CurrentDir).joinpath('AuxiliaryData', 'VITS'))
        )
        self.ui.Button_DAT_VITS_AuxiliaryDataPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_AuxiliaryDataPath,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "数据集参数"),
            ChildItemText = QCA.translate("Tree", "辅助数据文本路径")
        )

        self.ui.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_TrainRatio,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "训练集占比\n划分给训练集的数据在数据集中所占的比例。")
            )
        )
        self.ui.DoubleSpinBox_DAT_VITS_TrainRatio.setRange(0.5, 0.9)
        self.ui.DoubleSpinBox_DAT_VITS_TrainRatio.setSingleStep(0.1)
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.DoubleSpinBox_DAT_VITS_TrainRatio,
            Section = 'VITS Params',
            Option = 'TrainRatio',
            DefaultValue = 0.7
        )
        self.ui.Button_DAT_VITS_TrainRatio_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.DoubleSpinBox_DAT_VITS_TrainRatio)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_TrainRatio,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "数据集参数"),
            ChildItemText = QCA.translate("Tree", "训练集占比")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_SampleRate,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "采样率 (HZ)\n数据集所要求的音频采样率，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_DAT_VITS_SampleRate.addItems(['22050', '44100', '48000', '96000', '192000', 'None'])
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.ComboBox_DAT_VITS_SampleRate,
            Section = 'VITS Params',
            Option = 'SampleRate',
            DefaultValue = 22050
        )
        self.ui.Button_DAT_VITS_SampleRate_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.ComboBox_DAT_VITS_SampleRate)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_SampleRate,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "数据集参数"),
            ChildItemText = QCA.translate("Tree", "采样率")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_SampleWidth,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "采样位数\n数据集所要求的音频采样位数，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_DAT_VITS_SampleWidth.addItems(['8', '16', '24', '32', '32 (Float)', 'None'])
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.ComboBox_DAT_VITS_SampleWidth,
            Section = 'VITS Params',
            Option = 'SampleWidth',
            DefaultValue = 16
        )
        self.ui.Button_DAT_VITS_SampleWidth_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.ComboBox_DAT_VITS_SampleWidth)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_SampleWidth,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "数据集参数"),
            ChildItemText = QCA.translate("Tree", "采样位数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_ToMono,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "合并声道\n将数据集音频的声道合并为单声道。")
            )
        )
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.CheckBox_DAT_VITS_ToMono,
            Section = 'VITS Params',
            Option = 'ToMono',
            DefaultValue = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_DAT_VITS_ToMono,
            CheckedText = "已启用",
            CheckedEvents = [
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
            ],
            TakeEffect = True
        )
        self.ui.Button_DAT_VITS_ToMono_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.CheckBox_DAT_VITS_ToMono)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_ToMono,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "数据集参数"),
            ChildItemText = QCA.translate("Tree", "合并声道")
        )

        self.ui.GroupBox_DAT_VITS_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_DAT_VITS_OutputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "输出参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_OutputDirName,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "输出目录名\n用于保存最后生成的数据集文件的目录的名字。")
            )
        )
        DAT_VITS_OutputDirName_Default = str(date.today())
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.LineEdit_DAT_VITS_OutputDirName,
            Section = 'Output Params',
            Option = 'Output_Dir_Name',
            DefaultValue = '',
            SetPlaceholderText = True,
            PlaceholderText = DAT_VITS_OutputDirName_Default
        )
        self.ui.LineEdit_DAT_VITS_OutputDirName.RemoveFileDialogButton()
        self.ui.Button_DAT_VITS_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_OutputDirName),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_VITS_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_OutputDirName,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "输出目录名")
        )

        self.ui.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_FileListNameTraining,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "训练集文本名\n用于保存最后生成的训练集txt文件的名字。")
            )
        )
        DAT_VITS_FileListNameTraining_Default = "Train_" + str(date.today())
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.LineEdit_DAT_VITS_FileListNameTraining,
            Section = 'Output Params',
            Option = 'FileList_Name_Training',
            DefaultValue = DAT_VITS_FileListNameTraining_Default,
            SetPlaceholderText = True,
            PlaceholderText = DAT_VITS_FileListNameTraining_Default
        )
        self.ui.LineEdit_DAT_VITS_FileListNameTraining.RemoveFileDialogButton()
        self.ui.Button_DAT_VITS_FileListNameTraining_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_FileListNameTraining),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_VITS_FileListNameTraining.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_FileListNameTraining,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "训练集文本名")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_DAT_VITS_FileListNameValidation,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "验证集文本名\n用于保存最后生成的验证集txt文件的名字。")
            )
        )
        DAT_VITS_FileListNameValidation_Default = "Val_" + str(date.today())
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.LineEdit_DAT_VITS_FileListNameValidation,
            Section = 'Output Params',
            Option = 'FileList_Name_Validation',
            DefaultValue = DAT_VITS_FileListNameValidation_Default,
            SetPlaceholderText = True,
            PlaceholderText = DAT_VITS_FileListNameValidation_Default
        )
        self.ui.LineEdit_DAT_VITS_FileListNameValidation.RemoveFileDialogButton()
        self.ui.Button_DAT_VITS_FileListNameValidation_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_FileListNameValidation),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_VITS_FileListNameValidation.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_DAT_VITS_FileListNameValidation,
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "验证集文本名")
        )

        LineEdit_DAT_VITS_OutputDir = QLineEdit()
        def SetText_LineEdit_DAT_VITS_OutputDir():
            DirName = self.ui.LineEdit_DAT_VITS_OutputDirName.text()
            if len(DirName.strip()) == 0:
                Alert = False
            else:
                DirText = Path(self.ui.LineEdit_DAT_VITS_OutputRoot.text()).joinpath(DirName).as_posix()
                LineEdit_DAT_VITS_OutputDir.setText(DirText)
                Alert = Path(DirText).exists() and list(Path(DirText).iterdir()) != []
            self.ui.LineEdit_DAT_VITS_OutputDirName.Alert(True if Alert else False, "注意：目录已包含文件")
        self.ui.LineEdit_DAT_VITS_OutputDirName.interacted.connect(SetText_LineEdit_DAT_VITS_OutputDir)
        self.ui.LineEdit_DAT_VITS_OutputRoot.interacted.connect(SetText_LineEdit_DAT_VITS_OutputDir)
        #SetText_LineEdit_DAT_VITS_OutputDir()

        LineEdit_DAT_VITS_FileListPathTraining = QLineEdit()
        def SetText_LineEdit_DAT_VITS_FileListPathTraining():
            FileName = self.ui.LineEdit_DAT_VITS_FileListNameTraining.text()
            if len(FileName.strip()) == 0:
                Alert = False
            else:
                PathText = Path(LineEdit_DAT_VITS_OutputDir.text()).joinpath(FileName).as_posix() + ".txt"
                LineEdit_DAT_VITS_FileListPathTraining.setText(PathText)
                Alert = Path(PathText).exists()
            self.ui.LineEdit_DAT_VITS_FileListNameTraining.Alert(True if Alert else False, "注意：路径已存在")
        self.ui.LineEdit_DAT_VITS_FileListNameTraining.interacted.connect(SetText_LineEdit_DAT_VITS_FileListPathTraining)
        LineEdit_DAT_VITS_OutputDir.textChanged.connect(SetText_LineEdit_DAT_VITS_FileListPathTraining)
        #SetText_LineEdit_DAT_VITS_FileListPathTraining()

        LineEdit_DAT_VITS_FileListPathValidation = QLineEdit()
        def SetText_LineEdit_DAT_VITS_FileListPathValidation():
            FileName = self.ui.LineEdit_DAT_VITS_FileListNameValidation.text()
            if len(FileName.strip()) == 0:
                Alert = False
            else:
                PathText = Path(LineEdit_DAT_VITS_OutputDir.text()).joinpath(FileName).as_posix() + ".txt"
                LineEdit_DAT_VITS_FileListPathValidation.setText(PathText)
                Alert = Path(PathText).exists()
            self.ui.LineEdit_DAT_VITS_FileListNameValidation.Alert(True if Alert else False, "注意：路径已存在")
        self.ui.LineEdit_DAT_VITS_FileListNameValidation.interacted.connect(SetText_LineEdit_DAT_VITS_FileListPathValidation)
        LineEdit_DAT_VITS_OutputDir.textChanged.connect(SetText_LineEdit_DAT_VITS_FileListPathValidation)
        #SetText_LineEdit_DAT_VITS_FileListPathValidation()

        # ChildWindow
        ChildWindow_DAT_VITS = Window_ChildWindow_DAT_VITS(self)

        ChildWindow_DAT_VITS.ui.Button_Close.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                QMessageBox.Question, "Ask",
                "确认放弃编辑？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_DAT_VITS.close()
                    )
                }
            )
        )
        ChildWindow_DAT_VITS.ui.Button_Maximize.clicked.connect(lambda: ChildWindow_DAT_VITS.showNormal() if ChildWindow_DAT_VITS.isMaximized() else ChildWindow_DAT_VITS.showMaximized())

        QFunc.Function_SetText(
            Widget = ChildWindow_DAT_VITS.ui.Label_Title,
            Text = QFunc.SetRichText(
                Title = QCA.translate("Label", "数据集制作结果")
            )
        )
        QFunc.Function_SetText(
            Widget = ChildWindow_DAT_VITS.ui.Label_Text,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "这里记录了每个语音文件与其对应的数据文本\n你可以对这些文本进行更改")
            )
        )

        ChildWindow_DAT_VITS.ui.Table_Train.setHorizontalHeaderLabels(['数据文本', '播放'])
        ChildWindow_DAT_VITS.ui.Table_Val.setHorizontalHeaderLabels(['数据文本', '播放'])

        ChildWindow_DAT_VITS.ui.Button_Cancel.setText(QCA.translate("Button", "取消"))
        ChildWindow_DAT_VITS.ui.Button_Cancel.clicked.connect(ChildWindow_DAT_VITS.ui.Button_Close.click)
        ChildWindow_DAT_VITS.ui.Button_Confirm.setText(QCA.translate("Button", "确认"))
        ChildWindow_DAT_VITS.ui.Button_Confirm.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                QMessageBox.Question, "Ask",
                "确认应用编辑？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        DATResult_Save(
                            ChildWindow_DAT_VITS.ui.Table_Train.GetValue(),
                            LineEdit_DAT_VITS_FileListPathTraining.text()
                        ),
                        DATResult_Save(
                            ChildWindow_DAT_VITS.ui.Table_Val.GetValue(),
                            LineEdit_DAT_VITS_FileListPathValidation.text()
                        ),
                        ChildWindow_DAT_VITS.close()
                    )
                }
            )
        )

        # VITS - Right
        MonitorFile_Config_DatasetCreator_VITS = QTasks.MonitorFile(Path_Config_DAT_VITS)
        MonitorFile_Config_DatasetCreator_VITS.start()
        MonitorFile_Config_DatasetCreator_VITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_DAT_VITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_DAT_VITS.setText(QCA.translate("Button", "全部重置"))
        self.ui.Button_ResetSettings_DAT_VITS.clicked.connect(
            lambda: ParamsManager_DAT_VITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_DAT_VITS.setText(QCA.translate("Button", "导入配置"))
        self.ui.Button_ImportSettings_DAT_VITS.clicked.connect(
            lambda: ParamsManager_DAT_VITS.ImportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SelectFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_DAT_VITS.setText(QCA.translate("Button", "导出配置"))
        self.ui.Button_ExportSettings_DAT_VITS.clicked.connect(
            lambda: ParamsManager_DAT_VITS.ExportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SaveFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_CheckOutput_DAT_VITS.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_DAT_VITS,
            URL = self.ui.LineEdit_DAT_VITS_OutputRoot,
            ButtonTooltip = "Click to open",
            CreateIfNotExist = True
        )

        # VITS - Bottom
        self.ui.Button_DAT_VITS_Execute.setToolTip("执行数据集制作")
        self.ui.Button_DAT_VITS_Terminate.setToolTip("终止数据集制作")
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_DAT_VITS_Execute,
            TerminateButton = self.ui.Button_DAT_VITS_Terminate,
            ProgressBar = self.ui.ProgressBar_DAT_VITS,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Dataset_Creating_VITS.Execute,
            ParamsFrom = [
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
            EmptyAllowed = [
                self.ui.ComboBox_DAT_VITS_SampleRate,
                self.ui.ComboBox_DAT_VITS_SampleWidth,
                self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath
            ],
            FinishEvents = [
                lambda: self.ShowMask(True, "正在加载表单"),
                lambda: ChildWindow_DAT_VITS.ui.Table_Train.SetValue(
                    DATResult_Get(LineEdit_DAT_VITS_FileListPathTraining.text())
                ),
                lambda: ChildWindow_DAT_VITS.ui.Table_Val.SetValue(
                    DATResult_Get(LineEdit_DAT_VITS_FileListPathValidation.text())
                ),
                ChildWindow_DAT_VITS.exec,
                lambda: Function_ShowMessageBox(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        #############################################################
        ####################### Content: Train ######################
        #############################################################

        # Guidance
        DialogBox_Train = MessageBox_Stacked(self)
        DialogBox_Train.setWindowTitle(QCA.translate("MsgBox", "引导（仅出现一次）"))
        DialogBox_Train.SetContent(
            [
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_Train.png')),
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
            ],
            [
                '欢迎来到语音训练工具界面\n该工具用于训练出适用于语音合成的模型文件',
                '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_Train.clicked.connect(
            lambda: (
                DialogBox_Train.exec(),
                Config.EditConfig('Dialog', 'GuidanceShown_Train', 'True')
            ) if eval(Config.GetValue('Dialog', 'GuidanceShown_Train', 'False')) is False else None
        )

        self.ui.Button_VoiceTrainer_Help.clicked.connect(
            lambda: DialogBox_Train.exec()
        )

        # GPT-SoVITS - ParamsManager
        Path_Config_Train_GPTSoVITS = QFunc.NormPath(Path(ConfigDir).joinpath('Config_Train_GPT-SoVITS.ini'))
        ParamsManager_Train_GPTSoVITS = ParamsManager(Path_Config_Train_GPTSoVITS)

        # GPT-SoVITS - Top
        self.ui.ToolButton_VoiceTrainer_Title_GPTSoVITS.setText(QCA.translate("ToolButton", "GPT-SoVITS"))
        self.ui.ToolButton_VoiceTrainer_Title_GPTSoVITS.setCheckable(True)
        self.ui.ToolButton_VoiceTrainer_Title_GPTSoVITS.setChecked(True)
        self.ui.ToolButton_VoiceTrainer_Title_GPTSoVITS.setAutoExclusive(True)
        self.ui.ToolButton_VoiceTrainer_Title_GPTSoVITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Train,
                TargetIndex = 0
            )
        )

        # GPT-SoVITS - Left
        self.ui.TreeWidget_Catalogue_Train_GPTSoVITS.clear()
        self.ui.TreeWidget_Catalogue_Train_GPTSoVITS.setHeaderHidden(True)

        # GPT-SoVITS - Midlle
        self.ui.GroupBox_Train_GPTSoVITS_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_Train_GPTSoVITS_InputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输入参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_GPTSoVITS_FileListPath,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "训练集文本路径\n用于提供训练集音频路径及其语音内容的训练集txt文件的路径。")
            )
        )
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_Train_GPTSoVITS_FileListPath,
            Section = 'Input Params',
            Option = 'FileList_Path',
            DefaultValue = '',
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Train_GPTSoVITS_FileListPath.SetFileDialog(
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)",
            Directory = Path(CurrentDir).joinpath('数据集制作结果', 'GPT-SoVITS').as_posix()
        )
        self.ui.Button_Train_GPTSoVITS_FileListPath_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_FileListPath),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_GPTSoVITS_FileListPath.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_GPTSoVITS_FileListPath,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "训练集文本路径")
        )

        self.ui.GroupBox_Train_GPTSoVITS_GPTSoVITSParams.setTitle(QCA.translate("GroupBox", "训练参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_Train_GPTSoVITS_GPTSoVITSParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "训练参数")
        )

        '''
        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_GPTSoVITS_Epochs,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "s1迭代轮数\n将全部样本完整迭代一轮的次数。")
            )
        )
        self.ui.SpinBox_Train_GPTSoVITS_S1Epochs.setRange(1, 100)
        self.ui.SpinBox_Train_GPTSoVITS_S1Epochs.setSingleStep(1)
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.SpinBox_Train_GPTSoVITS_S1Epochs,
            Section = 'GPT-SoVITS Params',
            Option = 'Epochs',
            DefaultValue = 8
        )
        self.ui.Button_Train_GPTSoVITS_S1Epochs_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.SpinBox_Train_GPTSoVITS_S1Epochs)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_GPTSoVITS_Epochs,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "s1迭代轮数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_GPTSoVITS_S2Epochs,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "s2迭代轮数\n将全部样本完整迭代一轮的次数。")
            )
        )
        self.ui.SpinBox_Train_GPTSoVITS_S2Epochs.setRange(1, 100)
        self.ui.SpinBox_Train_GPTSoVITS_S2Epochs.setSingleStep(1)
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.SpinBox_Train_GPTSoVITS_S2Epochs,
            Section = 'GPT-SoVITS Params',
            Option = 'Epochs',
            DefaultValue = 15
        )
        self.ui.Button_Train_GPTSoVITS_S2Epochs_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.SpinBox_Train_GPTSoVITS_S2Epochs)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_GPTSoVITS_S2Epochs,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "s2迭代轮数")
        )
        '''

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS1,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "预训练s1模型路径\n预训练s1模型的路径。")
            )
        )
        Train_GPTSoVITS_ModelPathPretrainedS1_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's1bert25hz-2kh-longer-epoch=68e-step=50232.ckpt').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1,
            Section = 'GPT-SoVITS Params',
            Option = 'Model_Path_Pretrained_s1',
            DefaultValue = Train_GPTSoVITS_ModelPathPretrainedS1_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_GPTSoVITS_ModelPathPretrainedS1_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1.SetFileDialog(
            Mode = "SelectFile",
            FileType = "ckpt类型 (*.ckpt)",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2'))
        )
        self.ui.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS1,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "预训练s1模型路径")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS2G,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "预训练s2G模型路径\n预训练s2G模型的路径。")
            )
        )
        Train_GPTSoVITS_ModelPathPretrainedS2G_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2G488k.pth').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G,
            Section = 'GPT-SoVITS Params',
            Option = 'Model_Path_Pretrained_s2G',
            DefaultValue = Train_GPTSoVITS_ModelPathPretrainedS2G_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_GPTSoVITS_ModelPathPretrainedS2G_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G.SetFileDialog(
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2'))
        )
        self.ui.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS2G,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "预训练s2G模型路径")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS2D,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "预训练s2D模型路径\n预训练s2D模型的路径。")
            )
        )
        Train_GPTSoVITS_ModelPathPretrainedS2D_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2D488k.pth').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D,
            Section = 'GPT-SoVITS Params',
            Option = 'Model_Path_Pretrained_s2D',
            DefaultValue = Train_GPTSoVITS_ModelPathPretrainedS2D_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_GPTSoVITS_ModelPathPretrainedS2D_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D.SetFileDialog(
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2'))
        )
        self.ui.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_GPTSoVITS_ModelPathPretrainedS2D,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "预训练s2D模型路径")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_GPTSoVITS_ModelDirPretrainedBert,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "预训练bert模型路径\n预训练bert模型（文件夹）的路径。")
            )
        )
        Train_GPTSoVITS_ModelDirPretrainedBert_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-roberta-wwm-ext-large').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert,
            Section = 'GPT-SoVITS Params',
            Option = 'Model_Dir_Pretrained_bert',
            DefaultValue = Train_GPTSoVITS_ModelDirPretrainedBert_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_GPTSoVITS_ModelDirPretrainedBert_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded'))
        )
        self.ui.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_GPTSoVITS_ModelDirPretrainedBert,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "预训练bert模型路径")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_GPTSoVITS_ModelDirPretrainedSSL,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "预训练ssl模型路径\n预训练ssl模型（文件夹）的路径。")
            )
        )
        Train_GPTSoVITS_ModelDirPretrainedSSL_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-hubert-base').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL,
            Section = 'GPT-SoVITS Params',
            Option = 'Model_Dir_Pretrained_ssl',
            DefaultValue = Train_GPTSoVITS_ModelDirPretrainedSSL_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_GPTSoVITS_ModelDirPretrainedSSL_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded'))
        )
        self.ui.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_GPTSoVITS_ModelDirPretrainedSSL,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "预训练ssl模型路径")
        )

        self.ui.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_GPTSoVITS_FP16Run,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "半精度训练\n通过混合了float16精度的训练方式减小显存占用。")
            )
        )
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.CheckBox_Train_GPTSoVITS_FP16Run,
            Section = 'GPT-SoVITS Params',
            Option = 'FP16_Run',
            DefaultValue = False
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Train_GPTSoVITS_FP16Run,
            CheckedText = "已启用",
            CheckedEvents = [
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
            ],
            TakeEffect = True
        )
        self.ui.Button_Train_GPTSoVITS_FP16Run_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.CheckBox_Train_GPTSoVITS_FP16Run)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_GPTSoVITS_FP16Run,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "半精度训练")
        )

        self.ui.GroupBox_Train_GPTSoVITS_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_Train_GPTSoVITS_OutputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输出参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_GPTSoVITS_OutputDirName,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "输出目录名\n存放训练所得模型的目录的名字。")
            )
        )
        Train_GPTSoVITS_OutputDirName_Default = str(date.today())
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_Train_GPTSoVITS_OutputDirName,
            Section = 'Output Params',
            Option = 'Output_Dir_Name',
            DefaultValue = '',
            SetPlaceholderText = True,
            PlaceholderText = Train_GPTSoVITS_OutputDirName_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_OutputDirName.RemoveFileDialogButton()
        self.ui.Button_Train_GPTSoVITS_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_OutputDirName),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_GPTSoVITS_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.LineEdit_Train_GPTSoVITS_OutputDirName,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "输出目录名")
        )

        self.ui.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_GPTSoVITS_LogDir,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "日志输出目录\n训练时生成的日志的存放目录。")
            )
        )
        Train_GPTSoVITS_LogDir_Default = Path(Path(CurrentDir).root).joinpath('EVT_TrainLog', 'GPT-SoVITS', str(date.today())).as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_Train_GPTSoVITS_LogDir,
            Section = 'Output Params',
            Option = 'Output_LogDir',
            DefaultValue = Train_GPTSoVITS_LogDir_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_GPTSoVITS_LogDir_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_LogDir.textChanged.connect(
            lambda Value: (
                Function_ShowMessageBox(self,
                    MessageType = QMessageBox.Warning,
                    WindowTitle = "Warning",
                    Text = "保存路径不支持非ASCII字符，请使用英文路径以避免训练报错",
                ),
                self.ui.LineEdit_Train_GPTSoVITS_LogDir.clear()
            ) if not all(Char.isascii() for Char in Value) else None
        )
        self.ui.LineEdit_Train_GPTSoVITS_LogDir.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(Train_GPTSoVITS_LogDir_Default).parent)
        )
        self.ui.Button_Train_GPTSoVITS_LogDir_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_LogDir),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_GPTSoVITS_LogDir.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_GPTSoVITS_LogDir,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "日志输出目录")
        )

        LineEdit_Train_GPTSoVITS_OutputDir = QLineEdit()
        def SetText_LineEdit_Train_GPTSoVITS_OutputDir():
            DirName = self.ui.LineEdit_Train_GPTSoVITS_OutputDirName.text()
            if len(DirName.strip()) == 0:
                Alert = False
            else:
                DirText = Path(self.ui.LineEdit_Train_GPTSoVITS_OutputRoot.text()).joinpath(DirName).as_posix()
                LineEdit_Train_GPTSoVITS_OutputDir.setText(DirText)
                Alert = Path(DirText).exists() and list(Path(DirText).iterdir()) != []
            self.ui.LineEdit_Train_GPTSoVITS_OutputDirName.Alert(True if Alert else False, "注意：目录已包含文件")
        self.ui.LineEdit_Train_GPTSoVITS_OutputDirName.interacted.connect(SetText_LineEdit_Train_GPTSoVITS_OutputDir)
        self.ui.LineEdit_Train_GPTSoVITS_OutputRoot.interacted.connect(SetText_LineEdit_Train_GPTSoVITS_OutputDir)
        #SetText_LineEdit_Train_GPTSoVITS_OutputDir()

        # GPT-SoVITS - Right
        MonitorFile_Config_VoiceTrainer_GPTSoVITS = QTasks.MonitorFile(Path_Config_Train_GPTSoVITS)
        MonitorFile_Config_VoiceTrainer_GPTSoVITS.start()
        MonitorFile_Config_VoiceTrainer_GPTSoVITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Train_GPTSoVITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_Train_GPTSoVITS.setText(QCA.translate("Button", "全部重置"))
        self.ui.Button_ResetSettings_Train_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_Train_GPTSoVITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_Train_GPTSoVITS.setText(QCA.translate("Button", "导入配置"))
        self.ui.Button_ImportSettings_Train_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_Train_GPTSoVITS.ImportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SelectFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_Train_GPTSoVITS.setText(QCA.translate("Button", "导出配置"))
        self.ui.Button_ExportSettings_Train_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_Train_GPTSoVITS.ExportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SaveFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_RunTensorboard_Train_GPTSoVITS.setText(QCA.translate("Button", "启动Tensorboard"))
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_RunTensorboard_Train_GPTSoVITS,
            Method = Tensorboard_Runner.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Train_GPTSoVITS_LogDir
            ]
        )

        self.ui.Button_CheckOutput_Train_GPTSoVITS.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Train_GPTSoVITS,
            URL = self.ui.LineEdit_Train_GPTSoVITS_OutputRoot,
            ButtonTooltip = "Click to open",
            CreateIfNotExist = True
        )

        # GPT-SoVITS - Bottom
        self.ui.Button_Train_GPTSoVITS_Execute.setToolTip("执行模型训练")
        self.ui.Button_Train_GPTSoVITS_Terminate.setToolTip("终止模型训练")
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_Train_GPTSoVITS_Execute,
            TerminateButton = self.ui.Button_Train_GPTSoVITS_Terminate,
            ProgressBar = self.ui.ProgressBar_Train_GPTSoVITS,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Voice_Training_GPTSoVITS.Execute,
            ParamsFrom = [
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
            FinishEvents = [
                lambda: Function_ShowMessageBox(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )
        FunctionSignals.Signal_TaskStatus.connect(
            lambda Task, Status: Function_ShowMessageBox(self,
                MessageType = QMessageBox.Question,
                WindowTitle = "Ask",
                Text = "是否稍后启用tensorboard？",
                Buttons = QMessageBox.Yes|QMessageBox.No,
                ButtonEvents = {QMessageBox.Yes: lambda: self.ui.Button_RunTensorboard_Train_GPTSoVITS.click()}
            ) if Task == 'Execute_Voice_Training_GPTSoVITS.Execute' and Status == 'Started' else None
        )

        # VITS - ParamsManager
        Path_Config_Train_VITS = QFunc.NormPath(Path(ConfigDir).joinpath('Config_Train_VITS.ini'))
        ParamsManager_Train_VITS = ParamsManager(Path_Config_Train_VITS)

        # VITS - Top
        self.ui.ToolButton_VoiceTrainer_Title_VITS.setText(QCA.translate("ToolButton", "VITS2"))
        self.ui.ToolButton_VoiceTrainer_Title_VITS.setCheckable(True)
        self.ui.ToolButton_VoiceTrainer_Title_VITS.setChecked(False)
        self.ui.ToolButton_VoiceTrainer_Title_VITS.setAutoExclusive(True)
        self.ui.ToolButton_VoiceTrainer_Title_VITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Train,
                TargetIndex = 1
            )
        )

        # VITS - Left
        self.ui.TreeWidget_Catalogue_Train_VITS.clear()
        self.ui.TreeWidget_Catalogue_Train_VITS.setHeaderHidden(True)

        # VITS - Midlle
        self.ui.GroupBox_Train_VITS_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_Train_VITS_InputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "输入参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_FileListPathTraining,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "训练集文本路径\n用于提供训练集音频路径及其语音内容的训练集txt文件的路径。")
            )
        )
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.LineEdit_Train_VITS_FileListPathTraining,
            Section = 'Input Params',
            Option = 'FileList_Path_Training',
            DefaultValue = '',
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Train_VITS_FileListPathTraining.SetFileDialog(
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)",
            Directory = Path(CurrentDir).joinpath('数据集制作结果', 'VITS').as_posix()
        )
        self.ui.Button_Train_VITS_FileListPathTraining_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_FileListPathTraining),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_VITS_FileListPathTraining.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_FileListPathTraining,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "训练集文本路径")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_FileListPathValidation,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "验证集文本路径\n用于提供验证集音频路径及其语音内容的验证集txt文件的路径。")
            )
        )
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.LineEdit_Train_VITS_FileListPathValidation,
            Section = 'Input Params',
            Option = 'FileList_Path_Validation',
            DefaultValue = '',
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Train_VITS_FileListPathValidation.SetFileDialog(
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)",
            Directory = Path(CurrentDir).joinpath('数据集制作结果', 'VITS').as_posix()
        )
        self.ui.Button_Train_VITS_FileListPathValidation_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_FileListPathValidation),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_VITS_FileListPathValidation.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_FileListPathValidation,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "验证集文本路径")
        )

        self.ui.GroupBox_Train_VITS_VITSParams.setTitle(QCA.translate("GroupBox", "训练参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_Train_VITS_VITSParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "训练参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_Epochs,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "迭代轮数\n将全部样本完整迭代一轮的次数。")
            )
        )
        self.ui.SpinBox_Train_VITS_Epochs.setRange(10, 100000)
        self.ui.SpinBox_Train_VITS_Epochs.setSingleStep(1)
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.SpinBox_Train_VITS_Epochs,
            Section = 'VITS Params',
            Option = 'Epochs',
            DefaultValue = 1000
        )
        self.ui.Button_Train_VITS_Epochs_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.SpinBox_Train_VITS_Epochs)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_Epochs,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "迭代轮数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_BatchSize,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "批处理量\n每轮迭代中单位批次的样本数量，需根据GPU的性能调节该值。")
            )
        )
        self.ui.SpinBox_Train_VITS_BatchSize.setRange(2, 128)
        self.ui.SpinBox_Train_VITS_BatchSize.setSingleStep(1)
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.SpinBox_Train_VITS_BatchSize,
            Section = 'VITS Params',
            Option = 'Batch_Size',
            DefaultValue = 4
        )
        self.ui.SpinBox_Train_VITS_BatchSize.setToolTip("建议：2~4G: 2\n6~8G: 4\n10~12G: 8\n14~16G: 16")
        self.ui.Button_Train_VITS_BatchSize_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.SpinBox_Train_VITS_BatchSize)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_BatchSize,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "批处理量")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_UsePretrainedModels,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "使用预训练模型\n使用预训练模型（底模），其载入优先级高于检查点。")
            )
        )
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.CheckBox_Train_VITS_UsePretrainedModels,
            Section = 'VITS Params',
            Option = 'Use_PretrainedModels',
            DefaultValue = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Train_VITS_UsePretrainedModels,
            CheckedText = "已启用",
            CheckedEvents = [
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
            UncheckedText = "未启用",
            UncheckedEvents = [
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
            TakeEffect = True
        )
        self.ui.Button_Train_VITS_UsePretrainedModels_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.CheckBox_Train_VITS_UsePretrainedModels)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_UsePretrainedModels,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "使用预训练模型")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_ModelPathPretrainedG,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "预训练G模型路径\n预训练生成器（Generator）模型的路径。")
            )
        )
        Train_VITS_ModelPathPretrainedG_Default = Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_G.pth').as_posix()
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.LineEdit_Train_VITS_ModelPathPretrainedG,
            Section = 'VITS Params',
            Option = 'Model_Path_Pretrained_G',
            DefaultValue = Train_VITS_ModelPathPretrainedG_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_VITS_ModelPathPretrainedG_Default
        )
        self.ui.LineEdit_Train_VITS_ModelPathPretrainedG.SetFileDialog(
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded'))
        )
        self.ui.Button_Train_VITS_ModelPathPretrainedG_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_ModelPathPretrainedG),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_VITS_ModelPathPretrainedG.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_ModelPathPretrainedG,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "预训练G模型路径")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_ModelPathPretrainedD,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "预训练D模型路径\n预训练判别器（Discriminator）模型的路径。")
            )
        )
        Train_VITS_ModelPathPretrainedD_Default = Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_D.pth').as_posix()
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.LineEdit_Train_VITS_ModelPathPretrainedD,
            Section = 'VITS Params',
            Option = 'Model_Path_Pretrained_D',
            DefaultValue = Train_VITS_ModelPathPretrainedD_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_VITS_ModelPathPretrainedD_Default
        )
        self.ui.LineEdit_Train_VITS_ModelPathPretrainedD.SetFileDialog(
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded'))
        )
        self.ui.Button_Train_VITS_ModelPathPretrainedD_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_ModelPathPretrainedD),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_VITS_ModelPathPretrainedD.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_ModelPathPretrainedD,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "预训练D模型路径")
        )

        DialogBox_KeepOriginalSpeakers = MessageBox_LineEdit(self)
        DialogBox_KeepOriginalSpeakers.setWindowTitle('Tip')
        DialogBox_KeepOriginalSpeakers.SetContent(
            Title = "开启该实验性功能需要注意以下几点：",
            Body = """
                1. 为防止老角色的音色在训练过程中被逐渐遗忘，请保证每个原角色至少有一两条音频参与训练。\n
                2. 为防止老角色的顺序被重组（导致音色混乱），请在下方设置包含了底模角色信息的配置文件路径。
            """
        )
        DialogBox_KeepOriginalSpeakers.LineEdit.SetFileDialog(
            Mode = "SelectFile", 
            FileType = "json类型 (*.json)",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded'))
        )
        Function_ParamsSynchronizer(
            Trigger = DialogBox_KeepOriginalSpeakers.LineEdit,
            FromTo = {DialogBox_KeepOriginalSpeakers.LineEdit: self.ui.LineEdit_Train_VITS_ConfigPathLoad}
        )
        DialogBox_KeepOriginalSpeakers.Button_Confirm.setText(QCA.translate("Button", "确认"))
        DialogBox_KeepOriginalSpeakers.Button_Confirm.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = "配置文件路径不存在！",
            ) if Path(DialogBox_KeepOriginalSpeakers.LineEdit.text()).is_file() == False else DialogBox_KeepOriginalSpeakers.close()
        )
        DialogBox_KeepOriginalSpeakers.Button_Cancel.setText(QCA.translate("Button", "取消"))
        DialogBox_KeepOriginalSpeakers.Button_Cancel.clicked.connect(
            lambda: (
                self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers.setChecked(False),
                DialogBox_KeepOriginalSpeakers.close()
            )
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_KeepOriginalSpeakers,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "保留原说话人（实验性）\n保留预训练模型中原有的说话人。")
            )
        )
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers,
            Section = 'VITS Params',
            Option = 'Keep_Original_Speakers',
            DefaultValue = False
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers,
            CheckedText = "已启用",
            CheckedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_Train_VITS_VITSParams_BasicSettings,
                    [
                        self.ui.Frame_Train_VITS_ConfigPathLoad
                    ],
                    True
                )
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
                lambda: Function_SetChildWidgetsVisibility(
                    self.ui.Frame_Train_VITS_VITSParams_BasicSettings,
                    [
                        self.ui.Frame_Train_VITS_ConfigPathLoad
                    ],
                    False
                )
            ],
            TakeEffect = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers,
            CheckedEvents = [
                lambda: DialogBox_KeepOriginalSpeakers.exec()
            ],
            TakeEffect = False
        )
        self.ui.Button_Train_VITS_KeepOriginalSpeakers_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_KeepOriginalSpeakers,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "保留原说话人")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_ConfigPathLoad,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "配置加载路径\n用于加载底模人物信息的配置文件的路径")
            )
        )
        Train_VITS_ConfigPathLoad_Default = Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_Config.json').as_posix()
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.LineEdit_Train_VITS_ConfigPathLoad,
            Section = 'VITS Params',
            Option = 'Config_Path_Load',
            DefaultValue = Train_VITS_ConfigPathLoad_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_VITS_ConfigPathLoad_Default
        )
        self.ui.LineEdit_Train_VITS_ConfigPathLoad.SetFileDialog(
            Mode = "SelectFile",
            FileType = "json类型 (*.json)",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded'))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.LineEdit_Train_VITS_ConfigPathLoad,
            FromTo = {self.ui.LineEdit_Train_VITS_ConfigPathLoad: DialogBox_KeepOriginalSpeakers.LineEdit}
        )
        self.ui.Button_Train_VITS_ConfigPathLoad_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_ConfigPathLoad),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_VITS_ConfigPathLoad.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_ConfigPathLoad,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "配置加载路径")
        )

        self.ui.ToolBox_Train_VITS_VITSParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_Train_VITS_VITSParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_NumWorkers,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "进程数量\n进行数据加载时可并行的进程数量，需根据CPU的性能调节该值。")
            )
        )
        self.ui.SpinBox_Train_VITS_NumWorkers.setRange(2, 128)
        self.ui.SpinBox_Train_VITS_NumWorkers.setSingleStep(2)
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.SpinBox_Train_VITS_NumWorkers,
            Section = 'VITS Params',
            Option = 'Num_Workers',
            DefaultValue = 4
        )
        self.ui.Button_Train_VITS_NumWorkers_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.SpinBox_Train_VITS_NumWorkers)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_NumWorkers,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "进程数量")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_FP16Run,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "半精度训练\n通过混合了float16精度的训练方式减小显存占用以支持更大的批处理量。")
            )
        )
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.CheckBox_Train_VITS_FP16Run,
            Section = 'VITS Params',
            Option = 'FP16_Run',
            DefaultValue = False
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Train_VITS_FP16Run,
            CheckedText = "已启用",
            CheckedEvents = [
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
            ],
            TakeEffect = True
        )
        self.ui.Button_Train_VITS_FP16Run_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.CheckBox_Train_VITS_FP16Run)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_FP16Run,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "训练参数"),
            ChildItemText = QCA.translate("Tree", "半精度训练")
        )

        self.ui.GroupBox_Train_VITS_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_Train_VITS_OutputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "输出参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_EvalInterval,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "保存间隔\n每次保存模型所间隔的步数。PS: 步数 ≈ 迭代轮次 * 训练样本数 / 批处理量")
            )
        )
        self.ui.SpinBox_Train_VITS_EvalInterval.setRange(10, 100000)
        self.ui.SpinBox_Train_VITS_EvalInterval.setSingleStep(1)
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.SpinBox_Train_VITS_EvalInterval,
            Section = 'Output Params',
            Option = 'Eval_Interval',
            DefaultValue = 1000
        )
        self.ui.SpinBox_Train_VITS_EvalInterval.setToolTip("提示：设置过小可能导致磁盘占用激增哦")
        self.ui.Button_Train_VITS_EvalInterval_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.SpinBox_Train_VITS_EvalInterval)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_EvalInterval,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "保存间隔")
        )

        self.ui.ToolBox_Train_VITS_OutputParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_Train_VITS_OutputParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_OutputDirName,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "输出目录名\n存放训练所得模型的目录的名字，若目录中已存在模型则会将其视为检查点。")
            )
        )
        Train_VITS_OutputDirName_Default = str(date.today())
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.LineEdit_Train_VITS_OutputDirName,
            Section = 'Output Params',
            Option = 'Output_Dir_Name',
            DefaultValue = '',
            SetPlaceholderText = True,
            PlaceholderText = Train_VITS_OutputDirName_Default
        )
        self.ui.LineEdit_Train_VITS_OutputDirName.RemoveFileDialogButton()
        self.ui.Button_Train_VITS_OutputDirName_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_OutputDirName),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_VITS_OutputDirName.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_OutputDirName,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "输出目录名")
        )

        LineEdit_Train_VITS_OutputDir = QLineEdit()
        def SetText_LineEdit_Train_VITS_OutputDir():
            DirName = self.ui.LineEdit_Train_VITS_OutputDirName.text()
            if len(DirName.strip()) == 0:
                Alert = False
            else:
                DirText = Path(self.ui.LineEdit_Train_VITS_OutputRoot.text()).joinpath(DirName).as_posix()
                LineEdit_Train_VITS_OutputDir.setText(DirText)
                Alert = Path(DirText).exists() and list(Path(DirText).iterdir()) != []
            self.ui.LineEdit_Train_VITS_OutputDirName.Alert(True if Alert else False, "注意：目录已包含文件")
        self.ui.LineEdit_Train_VITS_OutputDirName.interacted.connect(SetText_LineEdit_Train_VITS_OutputDir)
        self.ui.LineEdit_Train_VITS_OutputRoot.interacted.connect(SetText_LineEdit_Train_VITS_OutputDir)
        #SetText_LineEdit_Train_VITS_OutputDir()

        QFunc.Function_SetText(
            Widget = self.ui.Label_Train_VITS_LogDir,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "日志输出目录\n训练时生成的日志的存放目录。")
            )
        )
        Train_VITS_LogDir_Default = Path(Path(CurrentDir).root).joinpath('EVT_TrainLog', 'VITS', str(date.today())).as_posix()
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.LineEdit_Train_VITS_LogDir,
            Section = 'Output Params',
            Option = 'Output_LogDir',
            DefaultValue = Train_VITS_LogDir_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_VITS_LogDir_Default
        )
        self.ui.LineEdit_Train_VITS_LogDir.textChanged.connect(
            lambda Value: (
                Function_ShowMessageBox(self,
                    MessageType = QMessageBox.Warning,
                    WindowTitle = "Warning",
                    Text = "保存路径不支持非ASCII字符，请使用英文路径以避免训练报错",
                ),
                self.ui.LineEdit_Train_VITS_LogDir.clear()
            ) if not all(Char.isascii() for Char in Value) else None
        )
        self.ui.LineEdit_Train_VITS_LogDir.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(Train_VITS_LogDir_Default).parent)
        )
        self.ui.Button_Train_VITS_LogDir_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_LogDir),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_VITS_LogDir.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_Train_VITS_LogDir,
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemText = QCA.translate("Tree", "输出参数"),
            ChildItemText = QCA.translate("Tree", "日志输出目录")
        )

        # VITS - Right
        MonitorFile_Config_VoiceTrainer_VITS = QTasks.MonitorFile(Path_Config_Train_VITS)
        MonitorFile_Config_VoiceTrainer_VITS.start()
        MonitorFile_Config_VoiceTrainer_VITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Train_VITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_Train_VITS.setText(QCA.translate("Button", "全部重置"))
        self.ui.Button_ResetSettings_Train_VITS.clicked.connect(
            lambda: ParamsManager_Train_VITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_Train_VITS.setText(QCA.translate("Button", "导入配置"))
        self.ui.Button_ImportSettings_Train_VITS.clicked.connect(
            lambda: ParamsManager_Train_VITS.ImportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SelectFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_Train_VITS.setText(QCA.translate("Button", "导出配置"))
        self.ui.Button_ExportSettings_Train_VITS.clicked.connect(
            lambda: ParamsManager_Train_VITS.ExportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SaveFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_RunTensorboard_Train_VITS.setText(QCA.translate("Button", "启动Tensorboard"))
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_RunTensorboard_Train_VITS,
            Method = Tensorboard_Runner.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Train_VITS_LogDir
            ]
        )

        self.ui.Button_CheckOutput_Train_VITS.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Train_VITS,
            URL = self.ui.LineEdit_Train_VITS_OutputRoot,
            ButtonTooltip = "Click to open",
            CreateIfNotExist = True
        )

        # VITS - Bottom
        self.ui.Button_Train_VITS_Execute.setToolTip("执行模型训练")
        self.ui.Button_Train_VITS_Terminate.setToolTip("终止模型训练")
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_Train_VITS_Execute,
            TerminateButton = self.ui.Button_Train_VITS_Terminate,
            ProgressBar = self.ui.ProgressBar_Train_VITS,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Voice_Training_VITS.Execute,
            ParamsFrom = [
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
                'Config.json',
                self.ui.LineEdit_Train_VITS_LogDir
            ],
            EmptyAllowed = [
                self.ui.LineEdit_Train_VITS_ConfigPathLoad,
                self.ui.LineEdit_Train_VITS_ModelPathPretrainedG,
                self.ui.LineEdit_Train_VITS_ModelPathPretrainedD
            ],
            FinishEvents = [
                lambda: Function_ShowMessageBox(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )
        FunctionSignals.Signal_TaskStatus.connect(
            lambda Task, Status: Function_ShowMessageBox(self,
                MessageType = QMessageBox.Question,
                WindowTitle = "Ask",
                Text = "是否稍后启用tensorboard？",
                Buttons = QMessageBox.Yes|QMessageBox.No,
                ButtonEvents = {QMessageBox.Yes: lambda: self.ui.Button_RunTensorboard_Train_VITS.click()}
            ) if Task == 'Execute_Voice_Training_VITS.Execute' and Status == 'Started' else None
        )

        #############################################################
        ######################## Content: TTS #######################
        #############################################################

        # Guidance
        DialogBox_TTS = MessageBox_Stacked(self)
        DialogBox_TTS.setWindowTitle(QCA.translate("MsgBox", "引导（仅出现一次）"))
        DialogBox_TTS.SetContent(
            [
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_TTS.png')),
                QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
            ],
            [
                '欢迎来到语音合成工具界面\n该工具用于将文字转为语音，用户需要提供相应的模型和配置文件',
                '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_TTS.clicked.connect(
            lambda: (
                DialogBox_TTS.exec(),
                Config.EditConfig('Dialog', 'GuidanceShown_TTS', 'True')
            ) if eval(Config.GetValue('Dialog', 'GuidanceShown_TTS', 'False')) is False else None
        )

        self.ui.Button_VoiceConverter_Help.clicked.connect(
            lambda: DialogBox_TTS.exec()
        )

        # GPT-SoVITS - ParamsManager
        Path_Config_TTS_GPTSoVITS = QFunc.NormPath(Path(ConfigDir).joinpath('Config_TTS_GPT-SoVITS.ini'))
        ParamsManager_TTS_GPTSoVITS = ParamsManager(Path_Config_TTS_GPTSoVITS)

        # GPT-SoVITS - Top
        self.ui.ToolButton_VoiceConverter_Title_GPTSoVITS.setText(QCA.translate("ToolButton", "GPT-SoVITS"))
        self.ui.ToolButton_VoiceConverter_Title_GPTSoVITS.setCheckable(True)
        self.ui.ToolButton_VoiceConverter_Title_GPTSoVITS.setChecked(True)
        self.ui.ToolButton_VoiceConverter_Title_GPTSoVITS.setAutoExclusive(True)
        self.ui.ToolButton_VoiceConverter_Title_GPTSoVITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_TTS,
                TargetIndex = 0
            )
        )

        # GPT-SoVITS - Left
        self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS.clear()
        self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS.setHeaderHidden(True)

        # GPT-SoVTIS - Middle
        self.ui.GroupBox_TTS_GPTSoVITS_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_TTS_GPTSoVITS_InputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输入参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_GPTSoVITS_ModelPathLoadS1,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "s1模型加载路径\ns1模型的路径。")
            )
        )
        TTS_GPTSoVITS_ModelPathLoadS1_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's1bert25hz-2kh-longer-epoch=68e-step=50232.ckpt').as_posix()
        ParamsManager_TTS_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1,
            Section = 'Input Params',
            Option = 'Model_Path_Load_s1',
            DefaultValue = TTS_GPTSoVITS_ModelPathLoadS1_Default,
            SetPlaceholderText = True,
            PlaceholderText = TTS_GPTSoVITS_ModelPathLoadS1_Default
        )
        self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1.SetFileDialog(
            Mode = "SelectFile",
            FileType = "ckpt类型 (*.ckpt)",
            Directory = Path(CurrentDir).joinpath('模型训练结果', 'GPT-SoVITS').as_posix()
        )
        self.ui.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_GPTSoVITS.ResetParam(self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_GPTSoVITS_ModelPathLoadS1,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "s1模型加载路径")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_GPTSoVITS_ModelPathLoadS2G,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "s2G模型加载路径\ns2G模型的路径。")
            )
        )
        TTS_GPTSoVITS_ModelPathLoadS2G_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2G488k.pth').as_posix()
        ParamsManager_TTS_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G,
            Section = 'Input Params',
            Option = 'Model_Path_Load_s2G',
            DefaultValue = TTS_GPTSoVITS_ModelPathLoadS2G_Default,
            SetPlaceholderText = True,
            PlaceholderText = TTS_GPTSoVITS_ModelPathLoadS2G_Default
        )
        self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G.SetFileDialog(
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            Directory = Path(CurrentDir).joinpath('模型训练结果', 'GPT-SoVITS').as_posix()
        )
        self.ui.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_GPTSoVITS.ResetParam(self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_GPTSoVITS_ModelPathLoadS2G,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "s2G模型加载路径")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_GPTSoVITS_ModelDirLoadBert,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "预训练bert模型加载路径\n预训练bert模型（文件夹）的路径。")
            )
        )
        TTS_GPTSoVITS_ModelDirLoadBert_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-roberta-wwm-ext-large').as_posix()
        ParamsManager_TTS_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert,
            Section = 'Input Params',
            Option = 'Model_Dir_Load_bert',
            DefaultValue = TTS_GPTSoVITS_ModelDirLoadBert_Default,
            SetPlaceholderText = True,
            PlaceholderText = TTS_GPTSoVITS_ModelDirLoadBert_Default
        )
        self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded'))
        )
        self.ui.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_GPTSoVITS.ResetParam(self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_GPTSoVITS_ModelDirLoadBert,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "预训练bert模型加载路径")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_GPTSoVITS_ModelDirLoadSSL,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "预训练ssl模型加载路径\n预训练ssl模型的路径。")
            )
        )
        TTS_GPTSoVITS_ModelDirLoadSSL_Default = Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-hubert-base').as_posix()
        ParamsManager_TTS_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL,
            Section = 'Input Params',
            Option = 'Model_Dir_Load_ssl',
            DefaultValue = TTS_GPTSoVITS_ModelDirLoadSSL_Default,
            SetPlaceholderText = True,
            PlaceholderText = TTS_GPTSoVITS_ModelDirLoadSSL_Default
        )
        self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(ModelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded'))
        )
        self.ui.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_GPTSoVITS.ResetParam(self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_GPTSoVITS_ModelDirLoadSSL,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_GPTSoVITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "预训练ssl模型加载路径")
        )

        # GPT-SoVITS - Right
        MonitorFile_Config_VoiceConverter_GPTSoVITS = QTasks.MonitorFile(Path_Config_TTS_GPTSoVITS)
        MonitorFile_Config_VoiceConverter_GPTSoVITS.start()
        MonitorFile_Config_VoiceConverter_GPTSoVITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_TTS_GPTSoVITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_TTS_GPTSoVITS.setText(QCA.translate("Button", "全部重置"))
        self.ui.Button_ResetSettings_TTS_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_TTS_GPTSoVITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_TTS_GPTSoVITS.setText(QCA.translate("Button", "导入配置"))
        self.ui.Button_ImportSettings_TTS_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_TTS_GPTSoVITS.ImportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SelectFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_TTS_GPTSoVITS.setText(QCA.translate("Button", "导出配置"))
        self.ui.Button_ExportSettings_TTS_GPTSoVITS.clicked.connect(
            lambda: ParamsManager_TTS_GPTSoVITS.ExportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SaveFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        # GPT-SoVITS - Bottom
        self.ui.Button_TTS_GPTSoVITS_Execute.setToolTip("执行语音合成")
        self.ui.Button_TTS_GPTSoVITS_Terminate.setToolTip("终止语音合成")
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_TTS_GPTSoVITS_Execute,
            TerminateButton = self.ui.Button_TTS_GPTSoVITS_Terminate,
            ProgressBar = self.ui.ProgressBar_TTS_GPTSoVITS,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Voice_Converting_GPTSoVITS.Execute,
            ParamsFrom = [
                self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1,
                self.ui.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G,
                self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert,
                self.ui.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL,
            ],
            EmptyAllowed = [
            ],
            FinishEvents = [
                lambda: Function_ShowMessageBox(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        # VITS - ParamsManager
        Path_Config_TTS_VITS = QFunc.NormPath(Path(ConfigDir).joinpath('Config_TTS_VITS.ini'))
        ParamsManager_TTS_VITS = ParamsManager(Path_Config_TTS_VITS)

        # VITS - Top
        self.ui.ToolButton_VoiceConverter_Title_VITS.setText(QCA.translate("ToolButton", "VITS2"))
        self.ui.ToolButton_VoiceConverter_Title_VITS.setCheckable(True)
        self.ui.ToolButton_VoiceConverter_Title_VITS.setChecked(False)
        self.ui.ToolButton_VoiceConverter_Title_VITS.setAutoExclusive(True)
        self.ui.ToolButton_VoiceConverter_Title_VITS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_TTS,
                TargetIndex = 1
            )
        )

        # VITS - Left
        self.ui.TreeWidget_Catalogue_TTS_VITS.clear()
        self.ui.TreeWidget_Catalogue_TTS_VITS.setHeaderHidden(True)

        # VTIS - Middle
        self.ui.GroupBox_TTS_VITS_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_TTS_VITS_InputParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            RootItemText = QCA.translate("Tree", "输入参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_VITS_ConfigPathLoad,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "配置加载路径\n用于推理的配置文件的路径。")
            )
        )
        TTS_VITS_ConfigPathLoad_Default = Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_Config.json').as_posix()
        ParamsManager_TTS_VITS.SetParam(
            Widget = self.ui.LineEdit_TTS_VITS_ConfigPathLoad,
            Section = 'Input Params',
            Option = 'Config_Path_Load',
            DefaultValue = '',
            SetPlaceholderText = True,
            PlaceholderText = TTS_VITS_ConfigPathLoad_Default
        )
        self.ui.LineEdit_TTS_VITS_ConfigPathLoad.textChanged.connect(
            lambda Path: (
                self.ui.ComboBox_TTS_VITS_Speaker.clear(),
                self.ui.ComboBox_TTS_VITS_Speaker.addItems(Get_Speakers(Path))
            )
        )
        self.ui.LineEdit_TTS_VITS_ConfigPathLoad.SetFileDialog(
            Mode = "SelectFile",
            FileType = "json类型 (*.json)",
            Directory = Path(CurrentDir).joinpath('模型训练结果', 'VITS').as_posix()
        )
        self.ui.Button_TTS_VITS_ConfigPathLoad_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.LineEdit_TTS_VITS_ConfigPathLoad),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_TTS_VITS_ConfigPathLoad.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_VITS_ConfigPathLoad,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "配置加载路径")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_VITS_ModelPathLoad,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "G模型加载路径\n用于推理的生成器（Generator）模型的路径。")
            )
        )
        TTS_VITS_ModelPathLoad_Default = Path(ModelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_G.pth').as_posix()
        ParamsManager_TTS_VITS.SetParam(
            Widget = self.ui.LineEdit_TTS_VITS_ModelPathLoad,
            Section = 'Input Params',
            Option = 'Model_Path_Load',
            DefaultValue = '',
            SetPlaceholderText = True,
            PlaceholderText = TTS_VITS_ModelPathLoad_Default
        )
        self.ui.LineEdit_TTS_VITS_ModelPathLoad.SetFileDialog(
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            Directory = Path(CurrentDir).joinpath('模型训练结果', 'VITS').as_posix()
        )
        self.ui.Button_TTS_VITS_ModelPathLoad_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.LineEdit_TTS_VITS_ModelPathLoad),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_TTS_VITS_ModelPathLoad.text())
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_VITS_ModelPathLoad,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            RootItemText = QCA.translate("Tree", "输入参数"),
            ChildItemText = QCA.translate("Tree", "G模型加载路径")
        )

        self.ui.GroupBox_TTS_VITS_VITSParams.setTitle(QCA.translate("GroupBox", "语音合成参数"))
        Function_AddToTreeWidget(
            Widget = self.ui.GroupBox_TTS_VITS_VITSParams,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            RootItemText = QCA.translate("Tree", "语音合成参数")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_VITS_Text,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "输入文字\n输入的文字会作为说话人的语音内容。")
            )
        )
        ParamsManager_TTS_VITS.SetParam(
            Widget = self.ui.PlainTextEdit_TTS_VITS_Text,
            Section = 'VITS Params',
            Option = 'Text',
            DefaultValue = '',
            SetPlaceholderText = True,
            PlaceholderText = '请输入语句'
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_VITS_Text,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            RootItemText = QCA.translate("Tree", "语音合成参数"),
            ChildItemText = QCA.translate("Tree", "输入文字")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_VITS_Language,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "所属语言\n文字所属的语言，若使用自动检测则保持'None'即可（有概率报错）。")
            )
        )
        self.ui.ComboBox_TTS_VITS_Language.addItems(['None', QCA.translate("ComboBox", '中'), QCA.translate("ComboBox", '英'), QCA.translate("ComboBox", '日')])
        ParamsManager_TTS_VITS.SetParam(
            Widget = self.ui.ComboBox_TTS_VITS_Language,
            Section = 'VITS Params',
            Option = 'Language',
            DefaultValue = None
        )
        self.ui.Button_TTS_VITS_Language_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.ComboBox_TTS_VITS_Language)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_VITS_Language,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            RootItemText = QCA.translate("Tree", "语音合成参数"),
            ChildItemText = QCA.translate("Tree", "所属语言")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_VITS_Speaker,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "人物名字\n说话人物的名字。")
            )
        )
        self.ui.ComboBox_TTS_VITS_Speaker.addItems(
            Get_Speakers(self.ui.LineEdit_TTS_VITS_ConfigPathLoad.text())
        )
        '''
        ParamsManager_TTS_VITS.SetParam(
            Widget = self.ui.ComboBox_TTS_VITS_Speaker,
            Section = 'VITS Params',
            Option = 'Speaker',
            DefaultValue = ''
        )
        '''
        self.ui.ComboBox_TTS_VITS_Speaker.setCurrentIndex(0)
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_VITS_Speaker,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            RootItemText = QCA.translate("Tree", "语音合成参数"),
            ChildItemText = QCA.translate("Tree", "人物名字")
        )

        self.ui.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.widget(0).setText(QCA.translate("ToolBox", "高级设置"))
        self.ui.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.widget(0).collapse()

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_VITS_EmotionStrength,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "情感强度\n情感的变化程度。")
            )
        )
        self.ui.HorizontalSlider_TTS_VITS_EmotionStrength.setMinimum(0)
        self.ui.HorizontalSlider_TTS_VITS_EmotionStrength.setMaximum(100)
        self.ui.HorizontalSlider_TTS_VITS_EmotionStrength.setTickInterval(1)
        ParamsManager_TTS_VITS.SetParam(
            Widget = self.ui.HorizontalSlider_TTS_VITS_EmotionStrength,
            Section = 'VITS Params',
            Option = 'EmotionStrength',
            DefaultValue = 0.67,
            Times = 100
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.HorizontalSlider_TTS_VITS_EmotionStrength,
            FromTo = {
                self.ui.HorizontalSlider_TTS_VITS_EmotionStrength: self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength
            },
            Times = 0.01
        )
        self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength.setRange(0, 1)
        self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength.setSingleStep(0.01)
        ParamsManager_TTS_VITS.SetParam(
            Widget = self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength,
            Section = 'VITS Params',
            Option = 'EmotionStrength',
            DefaultValue = 0.67
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength,
            FromTo = {
                self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength: self.ui.HorizontalSlider_TTS_VITS_EmotionStrength
            },
            Times = 100
        )
        self.ui.Button_TTS_VITS_EmotionStrength_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_VITS_EmotionStrength,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            RootItemText = QCA.translate("Tree", "语音合成参数"),
            ChildItemText = QCA.translate("Tree", "情感强度")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_VITS_PhonemeDuration,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "音素音长\n音素的发音长度。")
            )
        )
        self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration.setMinimum(0)
        self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration.setMaximum(10)
        self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration.setTickInterval(1)
        ParamsManager_TTS_VITS.SetParam(
            Widget = self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration,
            Section = 'VITS Params',
            Option = 'PhonemeDuration',
            DefaultValue = 0.8,
            Times = 10
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration,
            FromTo = {
                self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration: self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration
            },
            Times = 0.1
        )
        self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration.setRange(0, 1)
        self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration.setSingleStep(0.1)
        ParamsManager_TTS_VITS.SetParam(
            Widget = self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration,
            Section = 'VITS Params',
            Option = 'PhonemeDuration',
            DefaultValue = 0.8
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration,
            FromTo = {
                self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration: self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration
            },
            Times = 10
        )
        self.ui.Button_TTS_VITS_PhonemeDuration_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_VITS_PhonemeDuration,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            RootItemText = QCA.translate("Tree", "语音合成参数"),
            ChildItemText = QCA.translate("Tree", "音素音长")
        )

        QFunc.Function_SetText(
            Widget = self.ui.Label_TTS_VITS_SpeechRate,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "整体语速\n整体的说话速度。")
            )
        )
        self.ui.HorizontalSlider_TTS_VITS_SpeechRate.setMinimum(0)
        self.ui.HorizontalSlider_TTS_VITS_SpeechRate.setMaximum(20)
        self.ui.HorizontalSlider_TTS_VITS_SpeechRate.setTickInterval(1)
        ParamsManager_TTS_VITS.SetParam(
            Widget = self.ui.HorizontalSlider_TTS_VITS_SpeechRate,
            Section = 'VITS Params',
            Option = 'SpeechRate',
            DefaultValue = 1.,
            Times = 10
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.HorizontalSlider_TTS_VITS_SpeechRate,
            FromTo = {
                self.ui.HorizontalSlider_TTS_VITS_SpeechRate: self.ui.DoubleSpinBox_TTS_VITS_SpeechRate
            },
            Times = 0.1
        )
        self.ui.DoubleSpinBox_TTS_VITS_SpeechRate.setRange(0, 2)
        self.ui.DoubleSpinBox_TTS_VITS_SpeechRate.setSingleStep(0.1)
        ParamsManager_TTS_VITS.SetParam(
            Widget = self.ui.DoubleSpinBox_TTS_VITS_SpeechRate,
            Section = 'VITS Params',
            Option = 'SpeechRate',
            DefaultValue = 1.
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.DoubleSpinBox_TTS_VITS_SpeechRate,
            FromTo = {
                self.ui.DoubleSpinBox_TTS_VITS_SpeechRate: self.ui.HorizontalSlider_TTS_VITS_SpeechRate
            },
            Times = 10
        )
        self.ui.Button_TTS_VITS_SpeechRate_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_TTS_VITS.ResetParam(self.ui.DoubleSpinBox_TTS_VITS_SpeechRate)
            }
        )
        Function_AddToTreeWidget(
            Widget = self.ui.Label_TTS_VITS_SpeechRate,
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            RootItemText = QCA.translate("Tree", "语音合成参数"),
            ChildItemText = QCA.translate("Tree", "整体语速")
        )

        TTS_VITS_AudioDirSave = Path(CurrentDir).joinpath('语音合成结果', 'VITS').as_posix()
        TTS_VITS_AudioPathSave = Path(TTS_VITS_AudioDirSave).joinpath("temp.wav").as_posix()
        os.makedirs(TTS_VITS_AudioDirSave) if not Path(TTS_VITS_AudioDirSave).exists() else None

        # ChildWindow
        ChildWindow_TTS_VITS = Window_ChildWindow_TTS_VITS(self)

        ChildWindow_TTS_VITS.ui.Button_Close.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                QMessageBox.Question, "Ask",
                "确认退出试听？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS_VITS.ui.Widget.ReleaseMediaPlayer(),
                        ChildWindow_TTS_VITS.close()
                    )
                } 
            )
        )
        ChildWindow_TTS_VITS.ui.Button_Maximize.clicked.connect(lambda: ChildWindow_TTS_VITS.showNormal() if ChildWindow_TTS_VITS.isMaximized() else ChildWindow_TTS_VITS.showMaximized())

        QFunc.Function_SetText(
            Widget = ChildWindow_TTS_VITS.ui.Label_Title,
            Text = QFunc.SetRichText(
                Title = QCA.translate("Label", "语音合成结果")
            )
        )
        QFunc.Function_SetText(
            Widget = ChildWindow_TTS_VITS.ui.Label_Text,
            Text = QFunc.SetRichText(
                Body = QCA.translate("Label", "点击播放按钮以试听合成语音")
            )
        )

        ChildWindow_TTS_VITS.ui.Button_Cancel.setText(QCA.translate("Button", "丢弃"))
        ChildWindow_TTS_VITS.ui.Button_Cancel.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                QMessageBox.Question, "Ask",
                "确认丢弃音频？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS_VITS.ui.Widget.ReleaseMediaPlayer(),
                        os.remove(TTS_VITS_AudioPathSave),
                        ChildWindow_TTS_VITS.close()
                    )
                }
            )
        )
        ChildWindow_TTS_VITS.ui.Button_Confirm.setText(QCA.translate("Button", "保留"))
        ChildWindow_TTS_VITS.ui.Button_Confirm.clicked.connect(
            lambda: Function_ShowMessageBox(self,
                QMessageBox.Question, "Ask",
                "确认保留音频？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS_VITS.ui.Widget.ReleaseMediaPlayer(),
                        shutil.move(
                            TTS_VITS_AudioPathSave,
                            QFunc.Function_GetFileDialog(
                                Mode = "SaveFile",
                                FileType = "wav类型 (*.wav)"
                            )
                        ),
                        ChildWindow_TTS_VITS.close()
                    )
                }
            )
        )

        # VITS - Right
        MonitorFile_Config_VoiceConverter_VITS = QTasks.MonitorFile(Path_Config_TTS_VITS)
        MonitorFile_Config_VoiceConverter_VITS.start()
        MonitorFile_Config_VoiceConverter_VITS.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_TTS_VITS.setText(
                FileContent
            )
        )

        self.ui.Button_ResetSettings_TTS_VITS.setText(QCA.translate("Button", "全部重置"))
        self.ui.Button_ResetSettings_TTS_VITS.clicked.connect(
            lambda: ParamsManager_TTS_VITS.ResetSettings()
        )

        self.ui.Button_ImportSettings_TTS_VITS.setText(QCA.translate("Button", "导入配置"))
        self.ui.Button_ImportSettings_TTS_VITS.clicked.connect(
            lambda: ParamsManager_TTS_VITS.ImportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SelectFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_ExportSettings_TTS_VITS.setText(QCA.translate("Button", "导出配置"))
        self.ui.Button_ExportSettings_TTS_VITS.clicked.connect(
            lambda: ParamsManager_TTS_VITS.ExportSettings(
                QFunc.Function_GetFileDialog(
                    Mode = "SaveFile",
                    FileType = "ini类型 (*.ini)"
                )
            )
        )

        self.ui.Button_CheckOutput_TTS_VITS.setText(QCA.translate("Button", "查看输出文件"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_TTS_VITS,
            URL = TTS_VITS_AudioDirSave,
            ButtonTooltip = "Click to open",
            CreateIfNotExist = True
        )

        # VITS - Bottom
        self.ui.Button_TTS_VITS_Execute.setToolTip("执行语音合成")
        self.ui.Button_TTS_VITS_Terminate.setToolTip("终止语音合成")
        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_TTS_VITS_Execute,
            TerminateButton = self.ui.Button_TTS_VITS_Terminate,
            ProgressBar = self.ui.ProgressBar_TTS_VITS,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Voice_Converting_VITS.Execute,
            ParamsFrom = [
                self.ui.LineEdit_TTS_VITS_ConfigPathLoad,
                self.ui.LineEdit_TTS_VITS_ModelPathLoad,
                self.ui.PlainTextEdit_TTS_VITS_Text,
                self.ui.ComboBox_TTS_VITS_Language,
                self.ui.ComboBox_TTS_VITS_Speaker,
                self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength,
                self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration,
                self.ui.DoubleSpinBox_TTS_VITS_SpeechRate,
                TTS_VITS_AudioPathSave
            ],
            EmptyAllowed = [
                self.ui.ComboBox_TTS_VITS_Language,
                self.ui.ComboBox_TTS_VITS_Speaker
            ],
            FinishEvents = [
                lambda: self.ShowMask(True, "正在加载播放器"),
                lambda: ChildWindow_TTS_VITS.ui.Widget.SetMediaPlayer(
                    TTS_VITS_AudioPathSave
                ),
                ChildWindow_TTS_VITS.exec,
                lambda: Function_ShowMessageBox(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                )
            ]
        )

        #############################################################
        ##################### Content: Settings #####################
        #############################################################

        # Client
        self.ui.ToolButton_Settings_Title_Client.setText(QCA.translate("Label", "系统选项"))
        self.ui.ToolButton_Settings_Title_Client.setCheckable(True)
        self.ui.ToolButton_Settings_Title_Client.setChecked(True)
        self.ui.ToolButton_Settings_Title_Client.setAutoExclusive(True)
        self.ui.ToolButton_Settings_Title_Client.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Settings,
                TargetIndex = 0
            )
        )

        self.ui.GroupBox_Settings_Client_Outlook.setTitle(QCA.translate("GroupBox", "外观设置"))

        self.ui.Label_Setting_Theme.setText(QCA.translate("Label", "主题"))
        self.ui.ComboBox_Setting_Theme.addItems([QCA.translate("ComboBox", '跟随系统'), QCA.translate("ComboBox", '亮色'), QCA.translate("ComboBox", '暗色')])
        ThemeDict = {
            '跟随系统': Theme.Auto,
            '亮色': Theme.Light,
            '暗色': Theme.Dark
        }
        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.ui.ComboBox_Setting_Theme.setCurrentText(
                QCA.translate("ComboBox", QFunc.FindKey(ThemeDict, Theme))
            )
        )
        self.ui.ComboBox_Setting_Theme.currentIndexChanged.connect(
            lambda: (
                Config.EditConfig(
                    'Settings', 'Theme', ThemeDict.get(self.ui.ComboBox_Setting_Theme.currentText())
                ),
                ComponentsSignals.Signal_SetTheme.emit(
                    ThemeDict.get(self.ui.ComboBox_Setting_Theme.currentText())
                ) if EasyTheme.THEME != ThemeDict.get(self.ui.ComboBox_Setting_Theme.currentText()) else None
            )
        )

        self.ui.Label_Setting_Language.setText(QCA.translate("Label", "语言"))
        self.ui.ComboBox_Setting_Language.addItems([QCA.translate("ComboBox", '跟随系统')])
        LanguageDict = {
            '跟随系统': Language.Auto,
            #'中文': Language.ZH,
            #'英文': Language.EN
        }
        ComponentsSignals.Signal_SetLanguage.connect(
            lambda Language: self.ui.ComboBox_Setting_Language.setCurrentText(
                QCA.translate("ComboBox", QFunc.FindKey(LanguageDict, Language))
            )
        )

        self.ui.GroupBox_Settings_Client_Function.setTitle(QCA.translate("GroupBox", "功能设置"))

        self.ui.Label_Setting_AutoUpdate.setText(QCA.translate("Label", "自动检查版本并更新"))
        self.ui.CheckBox_Setting_AutoUpdate.setChecked(
            {
                'Enabled': True,
                'Disabled': False
            }.get(Config.GetValue('Settings', 'AutoUpdate', 'Enabled'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Setting_AutoUpdate,
            CheckedText = "已启用",
            CheckedEvents = [
                lambda: Config.EditConfig('Settings', 'AutoUpdate', 'Enabled'),
                #lambda: Updater(CurrentVersion, IsFileCompiled, CurrentDir, f'Easy Voice Toolkit {CurrentVersion}', CurrentDir)
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
                lambda: Config.EditConfig('Settings', 'AutoUpdate', 'Disabled')
            ],
            TakeEffect = True
        )

        self.ui.GroupBox_Settings_Client_Operation.setTitle(QCA.translate("GroupBox", "操作"))

        self.ui.Button_Setting_ClientRebooter.clicked.connect(ClientRebooter)
        self.ui.Button_Setting_ClientRebooter.setText(QCA.translate("Button", "重启客户端"))
        self.ui.Button_Setting_ClientRebooter.setToolTip(QCA.translate("ToolTip", "重启EVT客户端"))

        Function_SetMethodExecutor(self,
            ExecuteButton = self.ui.Button_Setting_IntegrityChecker,
            Method = Integrity_Checker.Execute,
            Params = ()
        )
        FunctionSignals.Signal_TaskStatus.connect(
            lambda Task, Status: self.ui.Button_Setting_IntegrityChecker.setCheckable(
                False if Status == 'Started' else True
            )
        )
        self.ui.Button_Setting_IntegrityChecker.setText(QCA.translate("Button", "检查完整性"))
        self.ui.Button_Setting_IntegrityChecker.setToolTip(QCA.translate("ToolTip", "检查文件完整性"))

        # Tools
        self.ui.ToolButton_Settings_Title_Tools.setText(QCA.translate("Label", "工具选项"))
        self.ui.ToolButton_Settings_Title_Tools.setCheckable(True)
        self.ui.ToolButton_Settings_Title_Tools.setChecked(False)
        self.ui.ToolButton_Settings_Title_Tools.setAutoExclusive(True)
        self.ui.ToolButton_Settings_Title_Tools.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Settings,
                TargetIndex = 1
            )
        )

        self.ui.GroupBox_Settings_Tools_Function.setTitle(QCA.translate("GroupBox", "功能设置"))

        self.ui.Label_Setting_AutoReset.setText(QCA.translate("Label", "启动时重置所有工具的参数设置"))
        self.ui.CheckBox_Setting_AutoReset.setChecked(
            {
                'Enabled': True,
                'Disabled': False
            }.get(Config.GetValue('Tools', 'AutoReset', 'Enabled'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Setting_AutoReset,
            CheckedText = "已启用",
            CheckedEvents = [
                lambda: Config.EditConfig('Tools', 'AutoReset', 'Enabled'),
                lambda: MainWindowSignals.Signal_MainWindowShown.connect(
                    lambda: (
                        ParamsManager_Process.ResetSettings(),
                        ParamsManager_ASR_VPR.ResetSettings(),
                        ParamsManager_STT_Whisper.ResetSettings(),
                        ParamsManager_DAT_GPTSoVITS.ResetSettings(),
                        ParamsManager_DAT_VITS.ResetSettings(),
                        ParamsManager_Train_GPTSoVITS.ResetSettings(),
                        ParamsManager_Train_VITS.ResetSettings(),
                        ParamsManager_TTS_GPTSoVITS.ResetSettings(),
                        ParamsManager_TTS_VITS.ResetSettings()
                    )
                )
            ],
            UncheckedText = "未启用",
            UncheckedEvents = [
                lambda: Config.EditConfig('Tools', 'AutoReset', 'Disabled'),
            ],
            TakeEffect = True
        )

        self.ui.Label_Setting_Synchronizer.setText(QCA.translate("Label", "自动关联前后工具的部分参数设置"))
        self.ui.CheckBox_Setting_Synchronizer.setChecked(
            {
                'Enabled': True,
                'Disabled': False
            }.get(Config.GetValue('Tools', 'Synchronizer', 'Enabled'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Setting_Synchronizer,
            CheckedText = "已启用",
            CheckedEvents = [
                lambda: Config.EditConfig('Tools', 'Synchronizer', 'Enabled'),
                lambda: Function_ParamsSynchronizer(
                    LineEdit_Process_OutputDir,
                    {LineEdit_Process_OutputDir: self.ui.LineEdit_ASR_VPR_AudioDirInput}
                ),
                lambda: Function_ParamsSynchronizer(
                    LineEdit_ASR_VPR_AudioSpeakersDataPath,
                    {LineEdit_ASR_VPR_AudioSpeakersDataPath: [self.ui.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath, self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath]}
                ),
                lambda: Function_ParamsSynchronizer(
                    ChildWindow_ASR.ui.LineEdit,
                    {ChildWindow_ASR.ui.LineEdit: self.ui.LineEdit_STT_Whisper_AudioDir}
                ),
                lambda: Function_ParamsSynchronizer(
                    LineEdit_STT_Whisper_OutputDir,
                    {LineEdit_STT_Whisper_OutputDir: [self.ui.LineEdit_DAT_GPTSoVITS_SRTDir, self.ui.LineEdit_DAT_VITS_SRTDir]}
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
            UncheckedText = "未启用",
            UncheckedEvents = [
                lambda: Config.EditConfig('Tools', 'Synchronizer', 'Disabled'),
            ],
            TakeEffect = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Setting_Synchronizer,
            UncheckedEvents = [
                lambda: Function_ShowMessageBox(self,
                    QMessageBox.Information, "Tip",
                    "该设置将于重启之后生效"
                )
            ],
            TakeEffect = False
        )

        self.ui.GroupBox_Settings_Tools_Path.setTitle(QCA.translate("GroupBox", "路径设置"))

        self.ui.Label_Process_OutputRoot.setText(QCA.translate("Label", "音频处理输出目录"))
        Process_OutputRoot_Default = Path(OutputDir).joinpath('音频处理结果').as_posix()
        ParamsManager_Process.SetParam(
            Widget = self.ui.LineEdit_Process_OutputRoot,
            Section = 'Output Params',
            Option = 'Output_Root',
            DefaultValue = Process_OutputRoot_Default,
            SetPlaceholderText = True,
            PlaceholderText = Process_OutputRoot_Default
        )
        self.ui.LineEdit_Process_OutputRoot.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(Process_OutputRoot_Default).parent)
        )
        self.ui.Button_Process_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Process.ResetParam(self.ui.LineEdit_Process_OutputRoot)
            }
        )

        self.ui.Label_ASR_VPR_OutputRoot.setText(QCA.translate("Label", "声纹识别结果输出目录"))
        ASR_VPR_AudioSpeakersDataRoot_Default = Path(CurrentDir).joinpath('语音识别结果', 'VPR').as_posix()
        ParamsManager_ASR_VPR.SetParam(
            Widget = self.ui.LineEdit_ASR_VPR_OutputRoot,
            Section = 'Output Params',
            Option = 'Audio_Root_Output',
            DefaultValue = ASR_VPR_AudioSpeakersDataRoot_Default,
            SetPlaceholderText = True,
            PlaceholderText = ASR_VPR_AudioSpeakersDataRoot_Default
        )
        self.ui.LineEdit_ASR_VPR_OutputRoot.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(ASR_VPR_AudioSpeakersDataRoot_Default).parent)
        )
        self.ui.Button_ASR_VPR_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_ASR_VPR.ResetParam(self.ui.LineEdit_ASR_VPR_OutputRoot),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_ASR_VPR_OutputRoot.text())
            }
        )

        self.ui.Label_STT_Whisper_OutputRoot.setText(QCA.translate("Label", "Whisper转录输出目录"))
        STT_Whisper_OutputRoot_Default = Path(OutputDir).joinpath('语音转录结果', 'Whisper').as_posix()
        ParamsManager_STT_Whisper.SetParam(
            Widget = self.ui.LineEdit_STT_Whisper_OutputRoot,
            Section = 'Output Params',
            Option = 'Output_Root',
            DefaultValue = STT_Whisper_OutputRoot_Default,
            SetPlaceholderText = True,
            PlaceholderText = STT_Whisper_OutputRoot_Default
        )
        self.ui.LineEdit_STT_Whisper_OutputRoot.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(STT_Whisper_OutputRoot_Default).parent)
        )
        self.ui.Button_STT_Whisper_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_STT_Whisper.ResetParam(self.ui.LineEdit_STT_Whisper_OutputRoot),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_STT_Whisper_OutputRoot.text())
            }
        )

        self.ui.Label_DAT_GPTSoVITS_OutputRoot.setText( QCA.translate("Label", "GPTSoVITS数据集输出目录"))
        DAT_GPTSoVITS_OutputRoot_Default = Path(OutputDir).joinpath('数据集制作结果', 'GPT-SoVITS').as_posix()
        ParamsManager_DAT_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot,
            Section = 'Output Params',
            Option = 'Output_Root',
            DefaultValue = DAT_GPTSoVITS_OutputRoot_Default,
            SetPlaceholderText = True,
            PlaceholderText = DAT_GPTSoVITS_OutputRoot_Default
        )
        self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(DAT_GPTSoVITS_OutputRoot_Default).parent)
        )
        self.ui.Button_DAT_GPTSoVITS_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_GPTSoVITS.ResetParam(self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot.text())
            }
        )

        self.ui.Label_DAT_VITS_OutputRoot.setText(QCA.translate("Label", "VITS数据集输出目录"))
        DAT_VITS_OutputRoot_Default = Path(OutputDir).joinpath('数据集制作结果', 'VITS').as_posix()
        ParamsManager_DAT_VITS.SetParam(
            Widget = self.ui.LineEdit_DAT_VITS_OutputRoot,
            Section = 'Output Params',
            Option = 'Output_Root',
            DefaultValue = DAT_VITS_OutputRoot_Default,
            SetPlaceholderText = True,
            PlaceholderText = DAT_VITS_OutputRoot_Default
        )
        self.ui.LineEdit_DAT_VITS_OutputRoot.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(DAT_VITS_OutputRoot_Default).parent)
        )
        self.ui.Button_DAT_VITS_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_DAT_VITS.ResetParam(self.ui.LineEdit_DAT_VITS_OutputRoot),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_DAT_VITS_OutputRoot.text())
            }
        )

        self.ui.Label_Train_GPTSoVITS_OutputRoot.setText(QCA.translate("Label", "GPTSoVITS训练输出目录"))
        Train_GPTSoVITS_OutputRoot_Default = Path(OutputDir).joinpath('模型训练结果', 'GPT-SoVITS').as_posix()
        ParamsManager_Train_GPTSoVITS.SetParam(
            Widget = self.ui.LineEdit_Train_GPTSoVITS_OutputRoot,
            Section = 'Output Params',
            Option = 'Output_Root',
            DefaultValue = Train_GPTSoVITS_OutputRoot_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_GPTSoVITS_OutputRoot_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_OutputRoot.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(Train_GPTSoVITS_OutputRoot_Default).parent)
        )
        self.ui.Button_Train_GPTSoVITS_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_GPTSoVITS.ResetParam(self.ui.LineEdit_Train_GPTSoVITS_OutputRoot),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_GPTSoVITS_OutputRoot.text())
            }
        )

        self.ui.Label_Train_VITS_OutputRoot.setText(QCA.translate("Label", "VITS训练输出目录"))
        Train_VITS_OutputRoot_Default = Path(OutputDir).joinpath('模型训练结果', 'VITS').as_posix()
        ParamsManager_Train_VITS.SetParam(
            Widget = self.ui.LineEdit_Train_VITS_OutputRoot,
            Section = 'Output Params',
            Option = 'Output_Root',
            DefaultValue = Train_VITS_OutputRoot_Default,
            SetPlaceholderText = True,
            PlaceholderText = Train_VITS_OutputRoot_Default
        )
        self.ui.LineEdit_Train_VITS_OutputRoot.SetFileDialog(
            Mode = "SelectFolder",
            Directory = QFunc.NormPath(Path(Train_VITS_OutputRoot_Default).parent)
        )
        self.ui.Button_Train_VITS_OutputRoot_MoreActions.SetMenu(
            ActionEvents = {
                "重置": lambda: ParamsManager_Train_VITS.ResetParam(self.ui.LineEdit_Train_VITS_OutputRoot),
                "复制": lambda: self.Clipboard.setText(self.ui.LineEdit_Train_VITS_OutputRoot.text())
            }
        )

        #############################################################
        ####################### Content: Info #######################
        #############################################################

        self.ui.ToolButton_Info_Title.setText(QCA.translate("Label", "用户须知"))

        QFunc.Function_SetText(
            Widget = self.ui.TextBrowser_Text_Info,
            Text = QFunc.SetRichText(
                Title = QCA.translate("TextBrowser", "声明"),
                TitleAlign = "left",
                TitleSize = 24,
                TitleWeight = 840,
                Body = QCA.translate("TextBrowser",
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
                BodyAlign = "left",
                BodySize = 12,
                BodyWeight = 420,
                BodyLineHeight = 27
            )
        )

        #############################################################
        ###################### Content: Console #####################
        #############################################################

        self.ui.Button_Console_Title.setText(QCA.translate("Button", "终端"))

        MonitorLog = QTasks.MonitorLogFile(LogPath)
        MonitorLog.start()
        MonitorLog.Signal_ConsoleInfo.connect(
            lambda Info: (
                self.ui.PlainTextEdit_Console.setPlainText(Info),
                self.ui.PlainTextEdit_Console.moveCursor(QTextCursor.End)
            )
        )

        self.ui.Button_Console_Copy.clicked.connect(
            lambda: (
                self.Clipboard.setText(self.ui.PlainTextEdit_Console.toPlainText()),
                Function_ShowMessageBox(self, WindowTitle = "Tip", Text = "已复制输出日志到剪切板")
            )
        )

        self.ui.Button_Console_Clear.clicked.connect(MonitorLog.clear)

        self.ui.Button_Console_Fold.clicked.connect(self.ui.Button_Toggle_Console.click)

        #############################################################
        ######################### StatusBar #########################
        #############################################################

        # Toggle Console
        self.ui.Button_Toggle_Console.setChecked(False)
        self.ui.Button_Toggle_Console.setAutoExclusive(False)
        self.ui.Button_Toggle_Console.setToolTip("点击以展开/折叠终端")
        self.ui.Button_Toggle_Console.clicked.connect(
            lambda: Function_AnimateFrame(
                Frame = self.ui.Frame_Console,
                MinHeight = 0,
                MaxHeight = 210,
                SupportSplitter = True
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
        self.ui.Label_Version.setText(CurrentVersion)

        # Set Theme
        ComponentsSignals.Signal_SetTheme.emit(Config.GetValue('Settings', 'Theme', Theme.Auto))

        # Show MainWindow (and emit signal)
        self.show()
        MainWindowSignals.Signal_MainWindowShown.emit()

##############################################################################################################################

if __name__ == "__main__":
    # Check for updates
    UpdaterExecuter()

    App = QApplication(sys.argv)

    # Create&Show SplashScreen
    SC = QSplashScreen(QPixmap(QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/others/SplashScreen.png'))))
    #SC.showMessage('Loading...', alignment = Qt.AlignmentFlag.AlignCenter)
    SC.show()

    # Set Language
    Translator = TranslationBase()
    Translator.load(Language.Auto)
    App.installTranslator(Translator)

    # Init&Show MainWindow
    MW = MainWindow()
    MW.Main()

    # Close SplashScreen
    SC.finish(MW) #SC.close()

    sys.exit(App.exec())

##############################################################################################################################