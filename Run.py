import os
import sys
import time #import asyncio
import json
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from PySide6 import __file__ as PySide6_File
from PySide6.QtCore import Qt, QObject, Signal, Slot, QThread
from PySide6.QtCore import QCoreApplication as QCA
from PySide6.QtWidgets import *

from EVT_GUI.QSimpleWidgets.Utils import *
from EVT_GUI.QSimpleWidgets.QTasks import *
from EVT_GUI.Window import *
from EVT_GUI.Functions import *
from EVT_GUI.EnvConfigurator import *

##############################################################################################################################

# Set current version
CurrentVersion = "v1.0.0"

##############################################################################################################################

# Check whether python file is compiled
FileName, IsFileCompiled = GetFileInfo()


# Set&Change working directory to current directory
CurrentDir = GetBaseDir(__file__ if IsFileCompiled == False else sys.executable)
os.chdir(CurrentDir)


# Set directory to store static dependencies
ResourceDir = CurrentDir if GetBaseDir(SearchMEIPASS = True) is None else GetBaseDir(SearchMEIPASS = True)


# Set directory to store models (and relevant config)
ModelsDir = NormPath(Path(CurrentDir).joinpath('Models'))


# Set directory to store client config
ConfigDir = NormPath(Path(CurrentDir).joinpath('Config'))


# Set up client config
ConfigPath = NormPath(Path(ConfigDir).joinpath('Config.ini'))
Config = ManageConfig(ConfigPath)
Config.EditConfig('Info', 'CurrentVersion', str(CurrentVersion))
Config.EditConfig('Info', 'ExecuterName', str(FileName))


# Set up environment variables while python file is not compiled
if IsFileCompiled == False:
    SetEnvVar( # Redirect PATH variable 'QT_QPA_PLATFORM_PLUGIN_PATH' to Pyside6 '/plugins/platforms' folder's path
        Variable = 'QT_QPA_PLATFORM_PLUGIN_PATH',
        Value = NormPath(Path(GetBaseDir(PySide6_File)).joinpath('plugins', 'platforms'))
    )
# Set up environment variables while environment is configured
if Path(CurrentDir).joinpath('Aria2').exists():
    SetEnvVar(
        Variable = 'PATH',
        Value = NormPath(Path(CurrentDir).joinpath('Aria2'))
    )
if Path(CurrentDir).joinpath('FFmpeg').exists():
    SetEnvVar(
        Variable = 'PATH',
        Value = NormPath(Path(CurrentDir).joinpath('FFmpeg', 'bin'))
    )
if Path(CurrentDir).joinpath('Python').exists():
    '''
    SetEnvVar(
        Variable = 'PYTHONPATH',
        Value = NormPath(Path(CurrentDir).joinpath('Python'))
    )
    '''
    SetEnvVar(
        Variable = 'PATH',
        Value = NormPath(Path(CurrentDir).joinpath('Python'), TrailingSlash = True)
    )
    SetEnvVar(
        Variable = 'PATH',
        Value = NormPath(Path(CurrentDir).joinpath('Python', 'Scripts'), TrailingSlash = True)
    )

##############################################################################################################################

def UpdaterExecuter():
    '''
    Execute updater
    '''
    if Config.GetValue('Settings', 'AutoUpdate', 'Enabled') == 'Enabled':
        if Config.GetValue('Updater', 'Status', 'Checking') != 'Executed':
            subprocess.Popen(['python.exe', NormPath(Path(CurrentDir).joinpath('Updater.py'))] if IsFileCompiled == False else [NormPath(Path(CurrentDir).joinpath('Updater.exe'))], env = os.environ)
            #Config.EditConfig('Updater', 'Status', 'Executed')
            sys.exit()
        else:
            Config.EditConfig('Updater', 'Status', 'Unexecuted')

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

        Error = RunCMD(
            Args = [
                f'cd "{ResourceDir}"',
                'python -c "'
                'from EVT_Core.Process.Process import Audio_Processing; '
                f"AudioConvertandSlice = Audio_Processing{str(Params)}; "
                'AudioConvertandSlice.Process_Audio()"'
            ],
            PathType = 'Posix',
            ShowProgress = True,
            CommunicateThroughConsole = True,
            DecodeResult = True
        )[1]
        Error = None if 'traceback' not in str(Error).lower() else Error

        self.finished.emit(str(Error))


# Tools: VoiceIdentifier
class Execute_Voice_Identifying(QObject):
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

        Error = RunCMD(
            Args = [
                f'cd "{ResourceDir}"',
                'python -c "'
                'from EVT_Core.ASR.VPR.Identify import Voice_Identifying; '
                f"AudioContrastInference = Voice_Identifying{str(Params)}; "
                'AudioContrastInference.GetModel(); '
                'AudioContrastInference.Inference()"'
            ],
            PathType = 'Posix',
            ShowProgress = True,
            CommunicateThroughConsole = True,
            DecodeResult = True
        )[1]
        Error = None if 'traceback' not in str(Error).lower() else Error

        self.finished.emit(str(Error))


# Tools: VoiceTranscriber
class Execute_Voice_Transcribing(QObject):
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
        Error = RunCMD(
            Args = [
                f'cd "{ResourceDir}"',
                'python -c "'
                'from EVT_Core.STT.Whisper.Transcribe import Voice_Transcribing; '
                f"WAVtoSRT = Voice_Transcribing{str(ItemReplacer(LANGUAGES, Params))}; "
                'WAVtoSRT.Transcriber()"'
            ],
            PathType = 'Posix',
            ShowProgress = True,
            CommunicateThroughConsole = True,
            DecodeResult = True
        )[1]
        Error = None if 'traceback' not in str(Error).lower() else Error

        self.finished.emit(str(Error))


# Tools: DatasetCreator
class Execute_Dataset_Creating(QObject):
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

        Error = RunCMD(
            Args = [
                f'cd "{ResourceDir}"',
                'python -c "'
                'from EVT_Core.DAT.VITS.Create import Dataset_Creating; '
                f"SRTtoCSVandSplitAudio = Dataset_Creating{str(Params)}; "
                'SRTtoCSVandSplitAudio.CallingFunctions()"'
            ],
            PathType = 'Posix',
            ShowProgress = True,
            CommunicateThroughConsole = True,
            DecodeResult = True
        )[1]
        Error = None if 'traceback' not in str(Error).lower() else Error

        self.finished.emit(str(Error))


# Tools: VoiceTrainer
class Execute_Voice_Training(QObject):
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

        Error = RunCMD(
            Args = [
                f'cd "{ResourceDir}"',
                'python -c "'
                'from EVT_Core.Train.VITS.Train import Voice_Training; '
                f"PreprocessandTrain = Voice_Training{str(Params)}; "
                'PreprocessandTrain.Preprocessing_and_Training()"'
            ],
            PathType = 'Posix',
            ShowProgress = True,
            CommunicateThroughConsole = True,
            DecodeResult = True
        )[1]
        if 'traceback' not in str(Error).lower():
            if "is not a directory" in str(Error).lower():
                Error = "请确保模型/配置保存路径中没有中文等特殊字符"
            if "specify the reduction dim" in str(Error).lower():
                Error = "请检查显存是否足够或者 batch size（批处理量）设置是否过高"
        else:
            Error = None 

        self.finished.emit(str(Error))


# Tools: VoiceConverter
def Get_Speakers(Config_Path_Load):
    try:
        with open(Config_Path_Load, 'r', encoding = 'utf-8') as File:
            Params = json.load(File)
        Speakers = Params["speakers"]
        return Speakers
    except:
        return str()

class Execute_Voice_Converting(QObject):
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
            "中":       "[ZH]",
            "Chinese":  "[ZH]",
            "英":       "[EN]",
            "English":  "[EN]",
            "日":       "[JA]",
            "Japanese": "[JA]"
        }
        Error = RunCMD(
            Args = [
                f'cd "{ResourceDir}"',
                'python -c "'
                'from EVT_Core.TTS.VITS.Convert import Voice_Converting; '
                f"TTS = Voice_Converting{str(ItemReplacer(LANGUAGES, Params))}; "
                'TTS.Converting()"'
            ],
            PathType = 'Posix',
            ShowProgress = True,
            CommunicateThroughConsole = True,
            DecodeResult = True
        )[1]
        Error = None if 'traceback' not in str(Error).lower() else Error

        self.finished.emit(str(Error))


# ClientFunc: GetModelsInfo
def GetModelsInfo(ModelsDir: str, ModelsFormats: list):
    '''
    '''
    ModelsInfo = {}
    os.makedirs(ModelsDir, exist_ok = True)

    ModelDicts_Cloud = []
    Tags = [Path(ModelsDir).parts[-2], Path(ModelsDir).parts[-1]]
    with open(Path(ResourceDir).joinpath('manifest.json'), 'r', encoding = 'utf-8') as File:
        Param = json.load(File)
    for ModelDict in Param["models"]:
        if ModelDict["tags"] == Tags:
            ModelDicts_Cloud.append(ModelDict)
    def GetModelInfo_Cloud(ModelDict):
        ModelName = ModelDict["name"]
        ModelSize = ModelDict["size"]
        ModelDate = ModelDict["date"]
        ModelSHA = ModelDict["SHA"]
        ModelURL = ModelDict["downloadurl"]
        DownloadParam = (ModelURL, Path(ModelsDir).joinpath("Downloaded"), ModelName, Path(ModelURL).suffix, ModelSHA)
        ModelsInfo[ModelSHA] = [str(ModelName), str(ModelSize), str(ModelDate), tuple(DownloadParam)]
    with ThreadPoolExecutor(max_workers = os.cpu_count()) as Executor:
        Executor.map(
            GetModelInfo_Cloud,
            ModelDicts_Cloud
        ) if ModelDicts_Cloud is not None else None

    ModelPaths_Local = []
    for ModelsFormat in ModelsFormats:
        ModelPaths_Local_Sep = GetPaths(ModelsDir, ModelsFormat)
        ModelPaths_Local.extend(ModelPaths_Local_Sep) if ModelPaths_Local_Sep is not None else None
    ModelPaths_Local = list(set(ModelPaths_Local))
    def GetModelInfo_Local(ModelPath):
        ModelName = Path(ModelPath).stem
        ModelSize = Path(ModelPath).stat().st_size
        ModelDate = datetime.fromtimestamp(Path(ModelPath).stat().st_mtime)
        with open(ModelPath, "rb") as m:
            ModelBytes = m.read()
        ModelSHA = hashlib.sha256(ModelBytes).hexdigest()
        ModelsInfo[ModelSHA] = [str(ModelName), str(ModelSize), str(ModelDate), str(ModelPath)]
    with ThreadPoolExecutor(max_workers = os.cpu_count()) as Executor:
        Executor.map(
            GetModelInfo_Local,
            ModelPaths_Local
        ) if ModelPaths_Local is not None else None

    return ModelsInfo.values()


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
            FilePath = DownloadFile(*DownloadParams)[1]
            FileSuffix = Path(FilePath).suffix
            shutil.unpack_archive(FilePath, DownloadParams[1], FileSuffix) if FileSuffix in ('zip', 'tar', 'gztar', 'bztar') else None
            return None
        except Exception as e:
            return e

    @Slot(tuple)
    def Execute(self, Params: tuple):
        Error = self.DownloadModel(Params)

        self.finished.emit(str(Error))


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

    @Slot(tuple)
    def Execute(self):
        if 'Undetected' not in [
            Config.GetValue('Env', 'FFmpeg'),
            Config.GetValue('Env', 'Python'),
            Config.GetValue('Env', 'PyReqs'),
            Config.GetValue('Env', 'Pytorch')
        ]:
            Error = RunCMD(
                Args = [
                    f'cd "{ResourceDir}"',
                    'python -c "'
                    'from EVT_Core.Process.Process import Audio_Processing; '
                    'from EVT_Core.ASR_VPR.Identify import Voice_Identifying; '
                    'from EVT_Core.STT_Whisper.Transcribe import Voice_Transcribing; '
                    'from EVT_Core.DAT_VITS.Create import Dataset_Creating; '
                    'from EVT_Core.Train_VITS.Train import Voice_Training; '
                    'from EVT_Core.TTS_VITS.Convert import Voice_Converting"'
                ],
                CommunicateThroughConsole = True,
                DecodeResult = True
            )[1]

        else:
            Error = 'Missing evironment dependencies!'

        self.finished.emit(str(Error))


# ClientFunc: TensorboardRunner
class Tensorboard_Runner(QObject):
    '''
    Check File integrity
    '''
    finished = Signal(str)

    def __init__(self):
        super().__init__()
    
    def RunTensorboard(self, LogDir): #async def RunTensorboard(self, LogDir):
        try:
            Error = None
            InitialWaitTime = 0
            MaximumWaitTime = 30
            while GetPaths(LogDir, 'events.out.tfevents') == None:
                time.sleep(3) #await asyncio.sleep(3)
                InitialWaitTime += 3
                if InitialWaitTime >= MaximumWaitTime:
                    break
            '''
            Output = RunCMD([['tensorboard', '--logdir', LogDir]], TimeOut = 9.)
            URL = FindURL(Output) #URL = Output[Output.find('http'):Output.find(' (', Output.find('http'))]
            Function_OpenURL(URL)
            '''
            subprocess.Popen(['tensorboard', '--logdir', LogDir], env = os.environ)
            time.sleep(9) #await asyncio.sleep(9)
            Function_OpenURL('http://localhost:6006/')
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

    # Run task
    Signal_ExecuteTask = Signal(tuple)

    # Monitor task
    Signal_TaskStatus = Signal(str, str)


MainWindowSignals = CustomSignals_MainWindow()


# Show GUI
class MainWindow(Window_Customizing):
    '''
    Show the user interface
    '''
    ui = Window_Customizing.ui

    def __init__(self, parent = None):
        super().__init__(parent)

        self.ConsoleInfo = ConsolOutputHandler()
        self.ConsoleInfo.start()

        self.MonitorUsage = MonitorUsage()
        self.MonitorUsage.start()

    def Function_SetMethodExecutor(self,
        ExecuteButton: Optional[QAbstractButton] = None,
        TerminateButton: Optional[QAbstractButton] = None,
        ProgressBar: Optional[QProgressBar] = None,
        ConsoleWidget: Optional[QWidget] = None,
        Method: object = ...,
        Params: Optional[tuple] = (),
        ParamsFrom: Optional[list] = [],
        EmptyAllowed: Optional[list] = [],
        #StartEventList: Optional[list] = None,
        #StartParamList: Optional[list[tuple]] = None,
        FinishEventList: Optional[list] = None,
        FinishParamList: Optional[list[tuple]] = None
    ):
        '''
        Function to execute outer class methods (through button)
        '''
        QualName = str(Method.__qualname__)
        ClassName =  QualName.split('.')[0]
        MethodName = QualName.split('.')[1]

        ClassInstance = globals()[ClassName]()
        ClassInstance.started.connect(lambda: MainWindowSignals.Signal_TaskStatus.emit(QualName, 'Started')) if hasattr(ClassInstance, 'started') else None
        #ClassInstance.started.connect(lambda: RunEvent(StartEventList, StartParamList)) if hasattr(ClassInstance, 'started') else None
        ClassInstance.finished.connect(lambda Error: MainWindowSignals.Signal_TaskStatus.emit(QualName, 'Finished') if Error == str(None) else None) if hasattr(ClassInstance, 'finished') else None
        ClassInstance.finished.connect(lambda Error: RunEvent(FinishEventList, FinishParamList) if Error == str(None) else None) if hasattr(ClassInstance, 'finished') else None
        ClassInstance.finished.connect(lambda Error: MainWindowSignals.Signal_TaskStatus.emit(QualName, 'Failed') if Error != str(None) else None) if hasattr(ClassInstance, 'finished') else None
        ClassInstance.finished.connect(lambda Error: Function_ShowMessageBox(QMessageBox.Warning, 'Failure', f'发生错误：\n{Error}') if Error != str(None) else None) if hasattr(ClassInstance, 'finished') else None

        if not isinstance(ClassInstance, QThread):
            WorkerThread = QThread()
            ClassInstance.moveToThread(WorkerThread)
            ClassInstance.finished.connect(WorkerThread.quit) if hasattr(ClassInstance, 'finished') else None
        else:
            WorkerThread = ClassInstance

        @Slot()
        def ExecuteMethod():
            '''
            Update the attributes for outer class methods and wait to execute with multithreading
            '''
            Args = Params#if Params != () else None
            if ParamsFrom not in ([], None):
                Args = Function_ParamsChecker(ParamsFrom, EmptyAllowed)
                if Args == "Abort":
                    return print("Aborted.")
                else:
                    pass #print("Continued.\n")

            MainWindowSignals = CustomSignals_MainWindow()
            MainWindowSignals.Signal_ExecuteTask.connect(getattr(ClassInstance, MethodName)) #MainWindowSignals.Signal_ExecuteTask.connect(lambda Args: getattr(ClassInstance, MethodName)(*Args))

            WorkerThread.started.connect(lambda: Function_AnimateFrame(ConsoleWidget, MinHeight = 0, MaxHeight = 210, Mode = "Extend")) if ConsoleWidget else None
            WorkerThread.started.connect(lambda: Function_AnimateProgressBar(ProgressBar, IsTaskAlive = True)) if ProgressBar else None
            WorkerThread.started.connect(lambda: Function_AnimateStackedWidget(Function_FindParentUI(ExecuteButton, QStackedWidget), TargetIndex = 1)) if TerminateButton else None
            WorkerThread.finished.connect(lambda: Function_AnimateFrame(ConsoleWidget, MinHeight = 0, MaxHeight = 210, Mode = "Reduce")) if ConsoleWidget else None
            WorkerThread.finished.connect(lambda: Function_AnimateProgressBar(ProgressBar, IsTaskAlive = False)) if ProgressBar else None
            WorkerThread.finished.connect(lambda: Function_AnimateStackedWidget(Function_FindParentUI(ExecuteButton, QStackedWidget), TargetIndex = 0)) if TerminateButton else None
            #WorkerThread.finished.connect(lambda: MainWindowSignals.Signal_ExecuteTask.disconnect(getattr(ClassInstance, MethodName)))

            MainWindowSignals.Signal_ExecuteTask.emit(Args)

            WorkerThread.start()

        if ExecuteButton is not None:
            ExecuteButton.clicked.connect(ExecuteMethod)
            ExecuteButton.setText("Execute 执行") if len(ExecuteButton.text().strip()) == 0 else None
        else:
            TempButton = QPushButton(self)
            TempButton.clicked.connect(ExecuteMethod)
            TempButton.click()
            WorkerThread.finished.connect(TempButton.deleteLater)

        @Slot()
        def TerminateMethod():
            '''
            Terminate the running thread
            '''
            if not WorkerThread.isFinished():
                try:
                    WorkerThread.terminate()
                except:
                    WorkerThread.quit()

            ProcessTerminator(
                Program = 'python.exe',
                SelfIgnored = True,
                SearchKeyword = True
            )

            ProgressBar.setValue(0)

        if TerminateButton is not None:
            TerminateButton.clicked.connect(
                lambda: Function_ShowMessageBox(
                    MessageType = QMessageBox.Question,
                    WindowTitle = "Ask",
                    Text = "当前任务仍在执行中，是否确认终止？",
                    Buttons = QMessageBox.Yes|QMessageBox.No,
                    EventButtons = [QMessageBox.Yes],
                    EventLists = [[TerminateMethod]],
                    ParamLists = [[()]]
                )
            )
            TerminateButton.setText("Terminate 终止") if len(TerminateButton.text().strip()) == 0 else None
        else:
            pass

    def Main(self):
        '''
        Main funtion to orgnize all the subfunctions
        '''
        self.setWindowIcon(QIcon(NormPath(Path(ResourceDir).joinpath('Icon.ico'))))

        #############################################################
        ########################## TitleBar #########################
        #############################################################

        # Title
        self.ui.Label_Title.setText("Easy Voice Toolkit - by Spr_Aachen")

        # Window controling buttons
        self.ui.Button_Close_Window.clicked.connect(self.close)
        self.ui.Button_Maximize_Window.clicked.connect(lambda: self.showNormal() if self.isMaximized() else self.showMaximized())
        self.ui.Button_Minimize_Window.clicked.connect(self.showMinimized)

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
        self.ui.Button_Menu_Download.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 1
            )
        )
        self.ui.Button_Menu_Download.setCheckable(True)
        self.ui.Button_Menu_Download.setChecked(False)
        self.ui.Button_Menu_Download.setAutoExclusive(True)
        self.ui.Button_Menu_Download.setToolTip(QCA.translate("ToolTip", "环境配置"))

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
        self.ui.Button_Menu_Process.setToolTip(QCA.translate("ToolTip", "音频处理"))

        self.ui.Label_Menu_ASR_Text.setText(QCA.translate("Label", "ASR"))
        self.ui.Button_Menu_ASR.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 4
            )
        )
        self.ui.Button_Menu_ASR.setCheckable(True)
        self.ui.Button_Menu_ASR.setChecked(False)
        self.ui.Button_Menu_ASR.setAutoExclusive(True)
        self.ui.Button_Menu_ASR.setToolTip(QCA.translate("ToolTip", "语音识别"))

        self.ui.Label_Menu_STT_Text.setText(QCA.translate("Label", "STT"))
        self.ui.Button_Menu_STT.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 5
            )
        )
        self.ui.Button_Menu_STT.setCheckable(True)
        self.ui.Button_Menu_STT.setChecked(False)
        self.ui.Button_Menu_STT.setAutoExclusive(True)
        self.ui.Button_Menu_STT.setToolTip(QCA.translate("ToolTip", "语音转文字"))

        self.ui.Label_Menu_Dataset_Text.setText(QCA.translate("Label", "DAT"))
        self.ui.Button_Menu_Dataset.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 6
            )
        )
        self.ui.Button_Menu_Dataset.setCheckable(True)
        self.ui.Button_Menu_Dataset.setChecked(False)
        self.ui.Button_Menu_Dataset.setAutoExclusive(True)
        self.ui.Button_Menu_Dataset.setToolTip(QCA.translate("ToolTip", "数据集生成"))

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
        self.ui.Button_Menu_Train.setToolTip(QCA.translate("ToolTip", "模型训练"))

        self.ui.Label_Menu_TTS_Text.setText(QCA.translate("Label", "TTS"))
        self.ui.Button_Menu_TTS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 8
            )
        )
        self.ui.Button_Menu_TTS.setCheckable(True)
        self.ui.Button_Menu_TTS.setChecked(False)
        self.ui.Button_Menu_TTS.setAutoExclusive(True)
        self.ui.Button_Menu_TTS.setToolTip(QCA.translate("ToolTip", "文字转语音"))

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

        self.ui.TextBrowser_Pic_Home.setStyleSheet(
            self.ui.TextBrowser_Pic_Home.styleSheet() +
            "QTextBrowser {"
            f"    background-image: url({NormPath(Path(ResourceDir).joinpath('Sources/Cover.png'), 'Posix')});"
            "    background-repeat: no-repeat;"
            "    background-position: center 0px;"
            "}"
        )

        Function_SetText(
            Widget = self.ui.TextBrowser_Text_Home,
            Text = SetRichText(
                Title = QCA.translate("TextBrowser", "介绍"),
                TitleAlign = "left",
                TitleSize = 24,
                TitleWeight = 840,
                Body = QCA.translate("TextBrowser",
                    "一个基于Whisper、VITS等项目实现的简易语音工具箱，提供了包括语音模型训练在内的多种自动化音频工具\n"
                    "\n"
                    "工具箱目前包含以下功能：\n"
                    "音频基本处理\n"
                    "语音识别和筛选\n"
                    "语音转文字字幕\n"
                    "语音数据集制作\n"
                    "语音模型训练\n"
                    "语音模型推理\n"
                    "\n"
                    "这些功能彼此之间相互独立，但又能无缝衔接地形成一套完整的工作流\n"
                    "用户可以根据自己的需求有选择性地使用，亦或者依次通过这些工具将未经处理的语音文件逐步变为理想的语音模型\n"
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
            URL = "https://colab.research.google.com/github/Spr-Aachen/EVT-Resources/blob/main/Easy_Voice_Toolkit_for_Colab.ipynb",
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
            URL = "https://",
            ButtonTooltip = "Click to buy him a coffee"
        )

        #############################################################
        ##################### Content: Environ ######################
        #############################################################

        self.ui.ToolButton_Env_Install_Title.setText(QCA.translate("Label", "依赖安装"))

        self.ui.Label_Env_Install_Aria2.setText("Aria2")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Install_Aria2,
            ProgressBar = self.ui.ProgressBar_Env_Install_Aria2,
            Method = Aria2_Installer.Execute,
            Params = ()
        )
        MainWindowSignals.Signal_MainWindowShown.connect(
            self.ui.Button_Install_Aria2.click #if Config.GetValue('Env', 'Aria2', 'Undetected') == 'Undetected' else EnvConfiguratorSignals.Signal_Aria2Detected.emit
        )
        self.ui.Button_Install_Aria2.setText('')
        self.ui.Button_Install_Aria2.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_Aria2Undetected.connect(
            lambda: Config.EditConfig('Env', 'Aria2', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_Aria2Undetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到Aria2，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [[self.ui.Button_Menu_Download.click]],
                ParamLists = [[()]]
            )
        )
        EnvConfiguratorSignals.Signal_Aria2Installed.connect(#self.ui.Button_Install_Aria2.click)
            lambda: EnvConfiguratorSignals.Signal_Aria2Detected.emit()
        )
        EnvConfiguratorSignals.Signal_Aria2InstallFailed.connect(
            lambda: Function_ShowMessageBox(
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = "安装Aria2出错",
                EventButtons = [QMessageBox.Ok]
            )
        )
        EnvConfiguratorSignals.Signal_Aria2Detected.connect(
            lambda: Config.EditConfig('Env', 'Aria2', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_Aria2Detected.connect(
            lambda: self.ui.ProgressBar_Env_Install_Aria2.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_Aria2Status.connect(
            lambda Status: self.ui.Label_Env_Install_Aria2_Status.setText(Status)
        )

        self.ui.Label_Env_Install_FFmpeg.setText("FFmpeg")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Install_FFmpeg,
            ProgressBar = self.ui.ProgressBar_Env_Install_FFmpeg,
            Method = FFmpeg_Installer.Execute,
            Params = ()
        )
        MainWindowSignals.Signal_MainWindowShown.connect(
            self.ui.Button_Install_FFmpeg.click #if Config.GetValue('Env', 'FFmpeg', 'Undetected') == 'Undetected' else EnvConfiguratorSignals.Signal_FFmpegDetected.emit
        )
        self.ui.Button_Install_FFmpeg.setText('')
        self.ui.Button_Install_FFmpeg.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_FFmpegUndetected.connect(
            lambda: Config.EditConfig('Env', 'FFmpeg', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_FFmpegUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到FFmpeg，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [[self.ui.Button_Menu_Download.click]],
                ParamLists = [[()]]
            )
        )
        EnvConfiguratorSignals.Signal_FFmpegInstalled.connect(#self.ui.Button_Install_FFmpeg.click)
            lambda: EnvConfiguratorSignals.Signal_FFmpegDetected.emit()
        )
        EnvConfiguratorSignals.Signal_FFmpegInstallFailed.connect(
            lambda: Function_ShowMessageBox(
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = "安装FFmpeg出错",
                EventButtons = [QMessageBox.Ok]
            )
        )
        EnvConfiguratorSignals.Signal_FFmpegDetected.connect(
            lambda: Config.EditConfig('Env', 'FFmpeg', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_FFmpegDetected.connect(
            lambda: self.ui.ProgressBar_Env_Install_FFmpeg.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_FFmpegStatus.connect(
            lambda Status: self.ui.Label_Env_Install_FFmpeg_Status.setText(Status)
        )

        self.ui.Label_Env_Install_Python.setText("Python")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Install_Python,
            ProgressBar = self.ui.ProgressBar_Env_Install_Python,
            Method = Python_Installer.Execute,
            Params = ('3.9', )
        )
        MainWindowSignals.Signal_MainWindowShown.connect( #EnvConfiguratorSignals.Signal_CMakeDetected.connect(
            self.ui.Button_Install_Python.click #if Config.GetValue('Env', 'Python', 'Undetected') == 'Undetected' else EnvConfiguratorSignals.Signal_PythonDetected.emit
        )
        self.ui.Button_Install_Python.setText('')
        self.ui.Button_Install_Python.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_PythonUndetected.connect(
            lambda: Config.EditConfig('Env', 'Python', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_PythonUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到Python，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [[self.ui.Button_Menu_Download.click]],
                ParamLists = [[()]]
            )
        )
        EnvConfiguratorSignals.Signal_PythonInstalled.connect(#self.ui.Button_Install_Python.click)
            lambda: EnvConfiguratorSignals.Signal_PythonDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PythonInstallFailed.connect(
            lambda: Function_ShowMessageBox(
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = "安装Python出错",
                EventButtons = [QMessageBox.Ok]
            )
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            lambda: Config.EditConfig('Env', 'Python', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            lambda: self.ui.ProgressBar_Env_Install_Python.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PythonStatus.connect(
            lambda Status: self.ui.Label_Env_Install_Python_Status.setText(Status)
        )

        self.ui.Label_Env_Install_PyReqs.setText("Python Requirements")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Install_PyReqs,
            ProgressBar = self.ui.ProgressBar_Env_Install_PyReqs,
            Method = PyReqs_Installer.Execute,
            Params = (NormPath(Path(ResourceDir).joinpath('requirements.txt')), )
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            self.ui.Button_Install_PyReqs.click #if Config.GetValue('Env', 'PyReqs', 'Undetected') == 'Undetected' else EnvConfiguratorSignals.Signal_PyReqsDetected.emit
        )
        self.ui.Button_Install_PyReqs.setText('')
        self.ui.Button_Install_PyReqs.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_PyReqsUndetected.connect(
            lambda: Config.EditConfig('Env', 'PyReqs', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_PyReqsUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到Python依赖库，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [[self.ui.Button_Menu_Download.click]],
                ParamLists = [[()]]
            )
        )
        EnvConfiguratorSignals.Signal_PyReqsInstalled.connect(#self.ui.Button_Install_PyReqs.click)
            lambda: EnvConfiguratorSignals.Signal_PyReqsDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PythonInstallFailed.connect(
            lambda: Function_ShowMessageBox(
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = "安装Python依赖库出错",
                EventButtons = [QMessageBox.Ok]
            )
        )
        EnvConfiguratorSignals.Signal_PyReqsDetected.connect(
            lambda: Config.EditConfig('Env', 'PyReqs', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PyReqsDetected.connect(
            lambda: self.ui.ProgressBar_Env_Install_PyReqs.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PyReqsStatus.connect(
            lambda Status: self.ui.Label_Env_Install_PyReqs_Status.setText(Status)
        )

        self.ui.Label_Env_Install_Pytorch.setText("Pytorch")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Install_Pytorch,
            ProgressBar = self.ui.ProgressBar_Env_Install_Pytorch,
            Method = Pytorch_Installer.Execute,
            Params = ()
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            self.ui.Button_Install_Pytorch.click #if Config.GetValue('Env', 'Pytorch', 'Undetected') == 'Undetected' else EnvConfiguratorSignals.Signal_PytorchDetected.emit
        )
        self.ui.Button_Install_Pytorch.setText('')
        self.ui.Button_Install_Pytorch.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_PytorchUndetected.connect(
            lambda: Config.EditConfig('Env', 'Pytorch', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_PytorchUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到Pytorch，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [[self.ui.Button_Menu_Download.click]],
                ParamLists = [[()]]
            )
        )
        EnvConfiguratorSignals.Signal_PytorchInstalled.connect(#self.ui.Button_Install_Pytorch.click)
            lambda: EnvConfiguratorSignals.Signal_PytorchDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PytorchInstallFailed.connect(
            lambda: Function_ShowMessageBox(
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = "安装Pytorch出错",
                EventButtons = [QMessageBox.Ok]
            )
        )
        EnvConfiguratorSignals.Signal_PytorchDetected.connect(
            lambda: Config.EditConfig('Env', 'Pytorch', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PytorchDetected.connect(
            lambda: self.ui.ProgressBar_Env_Install_Pytorch.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PytorchStatus.connect(
            lambda Status: self.ui.Label_Env_Install_Pytorch_Status.setText(Status)
        )

        #############################################################
        ####################### Content: Models #####################
        #############################################################

        self.ui.ToolButton_Models_ASR_Title.setText(QCA.translate("ToolButton", 'ASR'))
        self.ui.ToolButton_Models_ASR_Title.setChecked(True)
        self.ui.ToolButton_Models_ASR_Title.setAutoExclusive(True)
        self.ui.ToolButton_Models_ASR_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Models,
                TargetIndex = 0
            )
        )
        self.ui.ToolButton_Models_ASR_Title.setToolTip(
            "语音识别模型"
        )

        self.ui.TabWidget_Models_ASR.setTabText(0, 'VPR（声纹识别）')

        self.ui.Table_Models_ASR_VPR.SetHorizontalHeaders(['名字', '日期', '大小', '操作'])
        self.ui.Button_Menu_Models.clicked.connect(
            lambda: self.ui.Table_Models_ASR_VPR.SetValue(
                GetModelsInfo(
                    NormPath(Path(ModelsDir).joinpath('ASR', 'VPR')),
                    ['pth']
                )
            )
        )
        self.ui.Table_Models_ASR_VPR.Download.connect(
            lambda Params: self.Function_SetMethodExecutor(
                Method = Model_Downloader.Execute,
                Params = Params
            )
        )

        self.ui.ToolButton_Models_STT_Title.setText(QCA.translate("ToolButton", 'STT'))
        self.ui.ToolButton_Models_STT_Title.setChecked(False)
        self.ui.ToolButton_Models_STT_Title.setAutoExclusive(True)
        self.ui.ToolButton_Models_STT_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Models,
                TargetIndex = 1
            )
        )
        self.ui.ToolButton_Models_STT_Title.setToolTip(
            "语音转文字模型"
        )

        self.ui.TabWidget_Models_STT.setTabText(0, 'Whisper')

        self.ui.Table_Models_STT_Whisper.SetHorizontalHeaders(['名字', '日期', '大小', '操作'])
        self.ui.Button_Menu_Models.clicked.connect(
            lambda: self.ui.Table_Models_STT_Whisper.SetValue(
                GetModelsInfo(
                    NormPath(Path(ModelsDir).joinpath('STT', 'Whisper')),
                    ['pt']
                )
            )
        )
        self.ui.Table_Models_STT_Whisper.Download.connect(
            lambda Params: self.Function_SetMethodExecutor(
                Method = Model_Downloader.Execute,
                Params = Params
            )
        )

        self.ui.ToolButton_Models_TTS_Title.setText(QCA.translate("ToolButton", 'TTS'))
        self.ui.ToolButton_Models_TTS_Title.setChecked(False)
        self.ui.ToolButton_Models_TTS_Title.setAutoExclusive(True)
        self.ui.ToolButton_Models_TTS_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Models,
                TargetIndex = 2
            )
        )
        self.ui.ToolButton_Models_TTS_Title.setToolTip(
            "文字转语音模型"
        )

        self.ui.TabWidget_Models_TTS.setTabText(0, 'VITS')

        self.ui.Table_Models_TTS_VITS.SetHorizontalHeaders(['名字', '日期', '大小', '操作'])
        self.ui.Button_Menu_Models.clicked.connect(
            lambda: self.ui.Table_Models_TTS_VITS.SetValue(
                GetModelsInfo(
                    NormPath(Path(ModelsDir).joinpath('TTS', 'VITS')),
                    ['pt', 'json']
                )
            )
        )
        self.ui.Table_Models_TTS_VITS.Download.connect(
            lambda Params: self.Function_SetMethodExecutor(
                Method = Model_Downloader.Execute,
                Params = Params
            )
        )

        #############################################################
        ###################### Content: Process #####################
        #############################################################

        # Guidance
        DialogBox_Process = MessageBox_Stacked()
        DialogBox_Process.setWindowTitle('Guidance（该引导仅出现一次）')
        DialogBox_Process.SetContent(
            [
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_Process.png')),
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_Layout.png'))
            ],
            [
                '欢迎来到音频处理工具界面\n该工具会将媒体文件批量转换为音频文件，然后自动切除音频的静音部分',
                '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_Process.clicked.connect(
            lambda: DialogBox_Process.exec() if eval(Config.GetValue('Dialog', 'GuidanceShown_Process', 'False')) is False else None,
            type = Qt.QueuedConnection
        )
        self.ui.Button_Menu_Process.clicked.connect(
            lambda: Config.EditConfig('Dialog', 'GuidanceShown_Process', 'True'),
            type = Qt.QueuedConnection
        )

        # Config
        Path_Config_Process = NormPath(Path(ConfigDir).joinpath('Config_Process.ini'))
        Config_Process = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_Process',
                Path_Config_Process
            )
        )

        # Top
        self.ui.ToolButton_AudioProcessor_Title.setText(QCA.translate("ToolButton", '音频基本处理'))
        self.ui.ToolButton_AudioProcessor_Title.setChecked(True)
        self.ui.ToolButton_AudioProcessor_Title.setAutoExclusive(True)
        self.ui.ToolButton_AudioProcessor_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Process,
                TargetIndex = 0
            )
        )

        # Middle
        self.ui.GroupBox_Process_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))

        Function_SetText(
            Widget = self.ui.Label_Process_MediaDirInput,
            Text = SetRichText(
                Body = QCA.translate("Label", "媒体输入目录\n需要输出为音频文件的媒体文件的所在目录。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Process_MediaDirInput,
            Text = str(Config_Process.GetValue('AudioProcessor', 'Media_Dir_Input', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Process_MediaDirInput.textChanged.connect(
            lambda Value: Config_Process.EditConfig('AudioProcessor', 'Media_Dir_Input', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Process_MediaDirInput,
            LineEdit = self.ui.LineEdit_Process_MediaDirInput,
            Mode = "SelectDir"
        )
        self.ui.Button_Process_MediaDirInput_Undo.clicked.connect(
            lambda: self.ui.LineEdit_Process_MediaDirInput.setText('')
        )

        '''
        self.ui.GroupBox_Process_DenoiseParams.setTitle(QCA.translate("GroupBox", "降噪参数"))

        Function_SetText(
            Widget = self.ui.Label_Process_DenoiseAudio,
            Text = SetRichText(
                Body = QCA.translate("Label", "启用杂音去除\n弱化音频中的非人声部分。")
            )
        )
        self.ui.CheckBox_Process_DenoiseAudio.setChecked(
            eval(Config_Process.GetValue('AudioProcessor', 'Denoise_Audio', 'True'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Process_DenoiseAudio,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Process.EditConfig
            ],
            CheckedArgsList = [
                ('AudioProcessor', 'Denoise_Audio', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Process.EditConfig
            ],
            UncheckedArgsList = [
                ('AudioProcessor', 'Denoise_Audio', 'False')
            ],
            TakeEffect = True
        )
        self.ui.Button_Process_DenoiseAudio_Undo.clicked.connect(
            lambda: self.ui.CheckBox_Process_DenoiseAudio.setChecked(True)
        )
        '''

        self.ui.GroupBox_Process_AudioSlicerParams.setTitle(QCA.translate("GroupBox", "静音切除参数"))

        Function_SetText(
            Widget = self.ui.Label_Process_SliceAudio,
            Text = SetRichText(
                Body = QCA.translate("Label", "启用静音切除\n切除音频中的静音部分。")
            )
        )
        self.ui.CheckBox_Process_SliceAudio.setChecked(
            eval(Config_Process.GetValue('AudioProcessor', 'Slice_Audio', 'True'))
        )
        def CheckBox_Process_SliceAudio_HideWidgets(SetVisible):
            for Frame in (self.ui.Frame_Process_RMSThreshold,self.ui.Frame_Process_HopSize,self.ui.Frame_Process_SilentIntervalMin,self.ui.Frame_Process_SilenceKeptMax,self.ui.Frame_Process_AudioLengthMin):
                Frame.setVisible(SetVisible)
            if self.ui.CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings.isChecked():
                Function_AnimateFrame(
                    Frame = self.ui.Frame_Process_AudioSlicerParams_AdvanceSettings,
                    MinHeight = self.ui.Frame_Process_SampleRate.height()+self.ui.Frame_Process_SampleWidth.height()+self.ui.Frame_Process_ToMono.height(),
                    MaxHeight = self.ui.Frame_Process_AudioSlicerParams_AdvanceSettings.sizeHint().height() if SetVisible else (self.ui.Frame_Process_SampleRate.height()+self.ui.Frame_Process_SampleWidth.height()+self.ui.Frame_Process_ToMono.height()),
                    Duration = 210,
                    Mode = 'Extend' if SetVisible else 'Reduce'
                )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Process_SliceAudio,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Process.EditConfig,
                CheckBox_Process_SliceAudio_HideWidgets
            ],
            CheckedArgsList = [
                ('AudioProcessor', 'Slice_Audio', 'True'),
                (True)
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Process.EditConfig,
                CheckBox_Process_SliceAudio_HideWidgets
            ],
            UncheckedArgsList = [
                ('AudioProcessor', 'Slice_Audio', 'False'),
                (False)
            ],
            TakeEffect = True
        )
        self.ui.Button_Process_SliceAudio_Undo.clicked.connect(
            lambda: self.ui.CheckBox_Process_SliceAudio.setChecked(True)
        )

        self.ui.CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings.setChecked(
            False #eval(Config_Process.GetValue('AudioProcessor', 'Toggle_AdvanceSettings', ''))
        )
        def CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings_ExtendVisibleWidgets(Visualize):
            AlteredMaxHeight = self.ui.Frame_Process_SampleRate.height()+self.ui.Frame_Process_SampleWidth.height()+self.ui.Frame_Process_ToMono.height()
            Function_AnimateFrame(
                Frame = self.ui.Frame_Process_AudioSlicerParams_AdvanceSettings,
                MinHeight = 0,
                MaxHeight = self.ui.Frame_Process_AudioSlicerParams_AdvanceSettings.sizeHint().height() if self.ui.CheckBox_Process_SliceAudio.isChecked() else AlteredMaxHeight,
                Duration = 210,
                Mode = 'Extend' if Visualize else 'Reduce'
            )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings,
            CheckedText = "高级设置",
            CheckedEventList = [
                CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings_ExtendVisibleWidgets,
                #Config_Process.EditConfig
            ],
            CheckedArgsList = [
                (True),
                #('AudioProcessor', 'Toggle_AdvanceSettings', 'True')
            ],
            UncheckedText = "高级设置",
            UncheckedEventList = [
                CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings_ExtendVisibleWidgets,
                #Config_Process.EditConfig
            ],
            UncheckedArgsList = [
                (False),
                #('AudioProcessor', 'Toggle_AdvanceSettings', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Process_RMSThreshold,
            Text = SetRichText(
                Body = QCA.translate("Label", "均方根阈值 (db)\n低于该阈值的片段将被视作静音进行处理，若有降噪需求可以增加该值。")
            )
        )
        self.ui.DoubleSpinBox_Process_RMSThreshold.setRange(-100, 0)
        #self.ui.DoubleSpinBox_Process_RMSThreshold.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Process_RMSThreshold.setValue(
            float(Config_Process.GetValue('AudioProcessor', 'RMS_Threshold', '-40.'))
        )
        self.ui.DoubleSpinBox_Process_RMSThreshold.valueChanged.connect(
            lambda Value: Config_Process.EditConfig('AudioProcessor', 'RMS_Threshold', str(Value))
        )
        self.ui.Button_Process_RMSThreshold_Undo.clicked.connect(
            lambda: self.ui.DoubleSpinBox_Process_RMSThreshold.setValue(-40.)
        )

        Function_SetText(
            Widget = self.ui.Label_Process_HopSize,
            Text = SetRichText(
                Body = QCA.translate("Label", "跃点大小 (ms)\n每个RMS帧的长度，增加该值能够提高分割精度但会减慢进程。")
            )
        )
        self.ui.SpinBox_Process_HopSize.setRange(0, 100)
        self.ui.SpinBox_Process_HopSize.setSingleStep(1)
        self.ui.SpinBox_Process_HopSize.setValue(
            int(Config_Process.GetValue('AudioProcessor', 'Hop_Size', '10'))
        )
        self.ui.SpinBox_Process_HopSize.valueChanged.connect(
            lambda Value: Config_Process.EditConfig('AudioProcessor', 'Hop_Size', str(Value))
        )
        self.ui.Button_Process_HopSize_Undo.clicked.connect(
            lambda: self.ui.SpinBox_Process_HopSize.setValue(10)
        )

        Function_SetText(
            Widget = self.ui.Label_Process_SilentIntervalMin,
            Text = SetRichText(
                Body = QCA.translate("Label", "最小静音间隔 (ms)\n静音部分被分割成的最小长度，若音频只包含短暂中断可以减小该值。")
            )
        )
        self.ui.SpinBox_Process_SilentIntervalMin.setRange(0, 3000)
        self.ui.SpinBox_Process_SilentIntervalMin.setSingleStep(1)
        self.ui.SpinBox_Process_SilentIntervalMin.setValue(
            int(Config_Process.GetValue('AudioProcessor', 'Silent_Interval_Min', '300'))
        )
        self.ui.SpinBox_Process_SilentIntervalMin.valueChanged.connect(
            lambda Value: Config_Process.EditConfig('AudioProcessor', 'Silent_Interval_Min', str(Value))
        )
        self.ui.SpinBox_Process_SilentIntervalMin.setToolTip(QCA.translate("ToolTip", "注意：这个值必须小于最小音频长度，大于跃点大小。"))
        self.ui.Button_Process_SilentIntervalMin_Undo.clicked.connect(
            lambda: self.ui.SpinBox_Process_SilentIntervalMin.setValue(300)
        )

        Function_SetText(
            Widget = self.ui.Label_Process_SilenceKeptMax,
            Text = SetRichText(
                Body = QCA.translate("Label", "最大静音长度 (ms)\n被分割的音频周围保持静音的最大长度。")
            )
        )
        self.ui.SpinBox_Process_SilenceKeptMax.setRange(0, 10000)
        self.ui.SpinBox_Process_SilenceKeptMax.setSingleStep(1)
        self.ui.SpinBox_Process_SilenceKeptMax.setValue(
            int(Config_Process.GetValue('AudioProcessor', 'Silence_Kept_Max', '1000'))
        )
        self.ui.SpinBox_Process_SilenceKeptMax.valueChanged.connect(
            lambda Value: Config_Process.EditConfig('AudioProcessor', 'Silence_Kept_Max', str(Value))
        )
        self.ui.SpinBox_Process_SilenceKeptMax.setToolTip(QCA.translate("ToolTip", "注意：这个值无需完全对应被分割音频中的静音长度。算法将自行检索最佳的分割位置。"))
        self.ui.Button_Process_SilenceKeptMax_Undo.clicked.connect(
            lambda: self.ui.SpinBox_Process_SilenceKeptMax.setValue(1000)
        )

        Function_SetText(
            Widget = self.ui.Label_Process_AudioLengthMin,
            Text = SetRichText(
                Body = QCA.translate("Label", "最小音频长度 (ms)\n每个被分割的音频片段所需的最小长度。")
            )
        )
        self.ui.SpinBox_Process_AudioLengthMin.setRange(300, 30000)
        self.ui.SpinBox_Process_AudioLengthMin.setSingleStep(1)
        self.ui.SpinBox_Process_AudioLengthMin.setValue(
            int(Config_Process.GetValue('AudioProcessor', 'Audio_Length_Min', '3000'))
        )
        self.ui.SpinBox_Process_AudioLengthMin.valueChanged.connect(
            lambda Value: Config_Process.EditConfig('AudioProcessor', 'Audio_Length_Min', str(Value))
        )
        self.ui.Button_Process_AudioLengthMin_Undo.clicked.connect(
            lambda: self.ui.SpinBox_Process_AudioLengthMin.setValue(3000)
        )

        self.ui.GroupBox_Process_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))

        Function_SetText(
            Widget = self.ui.Label_Process_MediaFormatOutput,
            Text = SetRichText(
                Body = QCA.translate("Label", "媒体输出格式\n媒体文件输出为音频文件的格式，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Process_MediaFormatOutput.addItems(['flac', 'wav', 'mp3', 'aac', 'm4a', 'wma', 'aiff', 'au', 'ogg', 'None'])
        self.ui.ComboBox_Process_MediaFormatOutput.setCurrentText(
            str(Config_Process.GetValue('AudioProcessor', 'Media_Format_Output', 'wav'))
        )
        self.ui.ComboBox_Process_MediaFormatOutput.currentTextChanged.connect(
            lambda Value: Config_Process.EditConfig('AudioProcessor', 'Media_Format_Output', str(Value))
        )
        self.ui.Button_Process_MediaFormatOutput_Undo.clicked.connect(
            lambda: self.ui.ComboBox_Process_MediaFormatOutput.setCurrentText('wav')
        )

        Function_SetText(
            Widget = self.ui.Label_Process_MediaDirOutput,
            Text = SetRichText(
                Body = QCA.translate("Label", "媒体输出目录\n用于保存最后生成的音频文件的目录。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Process_MediaDirOutput,
            Text = str(Config_Process.GetValue('AudioProcessor', 'Media_Dir_Output', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Process_MediaDirOutput.textChanged.connect(
            lambda Value: Config_Process.EditConfig('AudioProcessor', 'Media_Dir_Output', str(Value))
        )
        '''
        self.ui.LineEdit_Process_MediaDirOutput.textChanged.connect(
            lambda Value: Function_ShowMessageBox(
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = "输出路径与输入路径相同"
            ) if Value == self.ui.LineEdit_Process_MediaDirInput.text() else None
        )
        '''
        Function_SetFileDialog(
            Button = self.ui.Button_Process_MediaDirOutput,
            LineEdit = self.ui.LineEdit_Process_MediaDirOutput,
            Mode = "SelectDir"
        )
        self.ui.Button_Process_MediaDirOutput_Undo.clicked.connect(
            lambda: self.ui.LineEdit_Process_MediaDirOutput.setText('')
        )

        self.ui.CheckBox_Process_OutputParams_Toggle_AdvanceSettings.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Process_OutputParams_Toggle_AdvanceSettings,
            CheckedText = "高级设置",
            CheckedEventList = [
                Function_AnimateFrame
            ],
            CheckedArgsList = [
                (
                    self.ui.Frame_Process_OutputParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_Process_OutputParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Extend'
                )
            ],
            UncheckedText = "高级设置",
            UncheckedEventList = [
                Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (
                    self.ui.Frame_Process_OutputParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_Process_OutputParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Reduce'
                )
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Process_ToMono,
            Text = SetRichText(
                Body = QCA.translate("Label", "合并声道\n将输出音频的声道合并为单声道。")
            )
        )
        self.ui.CheckBox_Process_ToMono.setChecked(
            eval(Config_Process.GetValue('AudioProcessor', 'ToMono', 'False'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Process_ToMono,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Process.EditConfig
            ],
            CheckedArgsList = [
                ('AudioProcessor', 'ToMono', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Process.EditConfig
            ],
            UncheckedArgsList = [
                ('AudioProcessor', 'ToMono', 'False')
            ],
            TakeEffect = True
        )
        self.ui.Button_Process_ToMono_Undo.clicked.connect(
            lambda: self.ui.CheckBox_Process_ToMono.setChecked(False)
        )

        Function_SetText(
            Widget = self.ui.Label_Process_SampleRate,
            Text = SetRichText(
                Body = QCA.translate("Label", "输出采样率\n输出音频所拥有的采样率，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Process_SampleRate.addItems(['22050', '44100', '48000', '96000', '192000', 'None'])
        self.ui.ComboBox_Process_SampleRate.setCurrentText(
            str(Config_Process.GetValue('AudioProcessor', 'SampleRate', 'None'))
        )
        self.ui.ComboBox_Process_SampleRate.currentTextChanged.connect(
            lambda Value: Config_Process.EditConfig('AudioProcessor', 'SampleRate', str(Value))
        )
        self.ui.Button_Process_SampleRate_Undo.clicked.connect(
            lambda: self.ui.ComboBox_Process_SampleRate.setCurrentText('None')
        )

        Function_SetText(
            Widget = self.ui.Label_Process_SampleWidth,
            Text = SetRichText(
                Body = QCA.translate("Label", "输出采样位数\n输出音频所拥有的采样位数，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Process_SampleWidth.addItems(['8', '16', '24', '32', '32 (Float)', 'None'])
        self.ui.ComboBox_Process_SampleWidth.setCurrentText(
            str(Config_Process.GetValue('AudioProcessor', 'SampleWidth', 'None'))
        )
        self.ui.ComboBox_Process_SampleWidth.currentTextChanged.connect(
            lambda Value: Config_Process.EditConfig('AudioProcessor', 'SampleWidth', str(Value))
        )
        self.ui.Button_Process_SampleWidth_Undo.clicked.connect(
            lambda: self.ui.ComboBox_Process_SampleWidth.setCurrentText('None')
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_Process,
            RootItemTexts = [
                self.ui.GroupBox_Process_InputParams.title(),
                self.ui.GroupBox_Process_AudioSlicerParams.title(),
                self.ui.GroupBox_Process_OutputParams.title()
            ],
            ChildItemTexts = [
                ("基础设置"),
                ("基础设置","高级设置"),
                ("基础设置","高级设置")
            ],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Process.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_Process_InputParams,
            ScrollArea = self.ui.ScrollArea_Middle_Process
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Process.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_Process_InputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_Process
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Process.topLevelItem(1),
            TargetWidget = self.ui.GroupBox_Process_AudioSlicerParams,
            ScrollArea = self.ui.ScrollArea_Middle_Process
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Process.topLevelItem(1).child(0),
            TargetWidget = self.ui.Frame_Process_AudioSlicerParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_Process
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Process.topLevelItem(1).child(1),
            TargetWidget = self.ui.Frame_Process_AudioSlicerParams_AdvanceSettings,
            ScrollArea = self.ui.ScrollArea_Middle_Process
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Process.topLevelItem(2),
            TargetWidget = self.ui.GroupBox_Process_OutputParams,
            ScrollArea = self.ui.ScrollArea_Middle_Process
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Process.topLevelItem(2).child(0),
            TargetWidget = self.ui.Frame_Process_OutputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_Process
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Process.topLevelItem(2).child(1),
            TargetWidget = self.ui.Frame_Process_OutputParams_AdvanceSettings,
            ScrollArea = self.ui.ScrollArea_Middle_Process
        )

        # Right
        MonitorFile_Config_AudioProcessor = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_Process')
        )
        MonitorFile_Config_AudioProcessor.start()
        MonitorFile_Config_AudioProcessor.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Process.setText(
                FileContent
            )
        )

        self.ui.Button_CheckOutput_Process.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Process,
            URL = self.ui.LineEdit_Process_MediaDirOutput,
            ButtonTooltip = "Click to open"
        )

        # Bottom
        self.ui.Button_Process_Execute.setToolTip(QCA.translate("ToolTip", "执行音频基本处理"))
        self.ui.Button_Process_Terminate.setToolTip(QCA.translate("ToolTip", "终止音频基本处理"))
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Process_Execute,
            TerminateButton = self.ui.Button_Process_Terminate,
            ProgressBar = self.ui.ProgressBar_Process,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Audio_Processing.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Process_MediaDirInput,
                self.ui.LineEdit_Process_MediaDirOutput,
                self.ui.ComboBox_Process_MediaFormatOutput,
                self.ui.ComboBox_Process_SampleRate,
                self.ui.ComboBox_Process_SampleWidth,
                self.ui.CheckBox_Process_ToMono,
                #self.ui.CheckBox_Process_DenoiseAudio,
                self.ui.CheckBox_Process_SliceAudio,
                self.ui.DoubleSpinBox_Process_RMSThreshold,
                self.ui.SpinBox_Process_AudioLengthMin,
                self.ui.SpinBox_Process_SilentIntervalMin,
                self.ui.SpinBox_Process_HopSize,
                self.ui.SpinBox_Process_SilenceKeptMax
            ],
            EmptyAllowed = [
                self.ui.ComboBox_Process_MediaFormatOutput,
                self.ui.ComboBox_Process_SampleRate,
                self.ui.ComboBox_Process_SampleWidth
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (
                    QMessageBox.Question, "Ask",
                    "当前任务已执行结束，是否跳转至下一工具界面？",
                    QMessageBox.Yes|QMessageBox.No, [QMessageBox.Yes],
                    [[self.ui.Button_Menu_ASR.click]], [[()]]
                )
            ]
        )

        #############################################################
        ######################## Content: ASR #######################
        #############################################################

        # Guidance
        DialogBox_ASR = MessageBox_Stacked()
        DialogBox_ASR.setWindowTitle('Guidance（该引导仅出现一次）')
        DialogBox_ASR.SetContent(
            [
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_ASR.png')),
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_Layout.png'))
            ],
            [
                '欢迎来到语音识别工具界面\n该工具会在不同说话人的音频中批量筛选出属于同一说话人的音频，用户需要提供一段目标说话人的语音',
                '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_ASR.clicked.connect(
            lambda: DialogBox_ASR.exec() if eval(Config.GetValue('Dialog', 'GuidanceShown_ASR', 'False')) is False else None,
            type = Qt.QueuedConnection
        )
        self.ui.Button_Menu_ASR.clicked.connect(
            lambda: Config.EditConfig('Dialog', 'GuidanceShown_ASR', 'True'),
            type = Qt.QueuedConnection
        )

        # Config
        Path_Config_ASR = NormPath(Path(ConfigDir).joinpath('Config_ASR.ini'))
        Config_ASR = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_ASR',
                Path_Config_ASR
            )
        )

        # Top
        self.ui.ToolButton_VoiceIdentifier_Title.setText(QCA.translate("ToolButton", "VPR"))
        self.ui.ToolButton_VoiceIdentifier_Title.setChecked(True)
        self.ui.ToolButton_VoiceIdentifier_Title.setAutoExclusive(True)
        self.ui.ToolButton_VoiceIdentifier_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_ASR,
                TargetIndex = 0
            )
        )

        # Middle
        self.ui.GroupBox_ASR_VPR_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))

        Function_SetText(
            Widget = self.ui.Label_ASR_VPR_AudioDirInput,
            Text = SetRichText(
                Body = QCA.translate("Label", "音频输入目录\n需要进行语音识别筛选的音频文件的所在目录。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_ASR_VPR_AudioDirInput,
            Text = str(Config_ASR.GetValue('VPR', 'Audio_Dir_Input', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_ASR_VPR_AudioDirInput.textChanged.connect(
            lambda Value: Config_ASR.EditConfig('VPR', 'Audio_Dir_Input', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_ASR_VPR_AudioDirInput,
            LineEdit = self.ui.LineEdit_ASR_VPR_AudioDirInput,
            Mode = "SelectDir"
        )
        self.ui.Button_ASR_VPR_AudioDirInput_Undo.clicked.connect(
            lambda: self.ui.LineEdit_ASR_VPR_AudioDirInput.setText('')
        )

        Function_SetText(
            Widget = self.ui.Label_ASR_VPR_StdAudioSpeaker,
            Text = SetRichText(
                Body = QCA.translate("Label", "目标人物与音频\n目标人物的名字及其语音文件的所在路径，音频中尽量不要混入杂音。")
            )
        )
        self.ui.Table_ASR_VPR_StdAudioSpeaker.SetHorizontalHeaders(['人物姓名', '音频路径', '增删'])
        self.ui.Table_ASR_VPR_StdAudioSpeaker.SetValue(
            eval(Config_ASR.GetValue('VPR', 'StdAudioSpeaker', '{"": ""}')),
            FileType = "音频类型 (*.mp3 *.aac *.wav *.flac)"
        )
        self.ui.Table_ASR_VPR_StdAudioSpeaker.ValueChanged.connect(
            lambda Value: Config_ASR.EditConfig('VPR', 'StdAudioSpeaker', str(Value))
        )

        self.ui.GroupBox_ASR_VPR_VPRParams.setTitle(QCA.translate("GroupBox", "声纹识别参数"))

        Function_SetText(
            Widget = self.ui.Label_ASR_VPR_DecisionThreshold,
            Text = SetRichText(
                Body = QCA.translate("Label", "判断阈值\n判断是否为同一人的阈值，若参与比对的说话人声音相识度较高可以增加该值。")
            )
        )
        self.ui.DoubleSpinBox_ASR_VPR_DecisionThreshold.setRange(0.5, 1)
        self.ui.DoubleSpinBox_ASR_VPR_DecisionThreshold.setSingleStep(0.01)
        self.ui.DoubleSpinBox_ASR_VPR_DecisionThreshold.setValue(
            float(Config_ASR.GetValue('VPR', 'DecisionThreshold', '0.75'))
        )
        self.ui.DoubleSpinBox_ASR_VPR_DecisionThreshold.valueChanged.connect(
            lambda Value: Config_ASR.EditConfig('VPR', 'DecisionThreshold', str(Value))
        )
        self.ui.Button_ASR_VPR_DecisionThreshold_Undo.clicked.connect(
            lambda: self.ui.DoubleSpinBox_ASR_VPR_DecisionThreshold.setValue(0.75)
        )

        self.ui.CheckBox_ASR_VPR_VPRParams_Toggle_AdvanceSettings.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_ASR_VPR_VPRParams_Toggle_AdvanceSettings,
            CheckedText = "高级设置",
            CheckedEventList = [
                Function_AnimateFrame
            ],
            CheckedArgsList = [
                (
                    self.ui.Frame_ASR_VPR_VPRParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_ASR_VPR_VPRParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Extend'
                )
            ],
            UncheckedText = "高级设置",
            UncheckedEventList = [
                Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (
                    self.ui.Frame_ASR_VPR_VPRParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_ASR_VPR_VPRParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Reduce'
                )
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_ASR_VPR_ModelPath,
            Text = SetRichText(
                Body = QCA.translate("Label", "模型加载路径\n用于加载的声纹识别模型的所在路径。")
            )
        )
        self.ui.LineEdit_ASR_VPR_ModelPath.setText(
            str(Config_ASR.GetValue('VPR', 'Model_Path', NormPath(Path(ModelsDir).joinpath('ASR', 'VPR', 'Downloaded', 'Ecapa-Tdnn_spectrogram.pth'), 'Posix')))
        )
        self.ui.LineEdit_ASR_VPR_ModelPath.textChanged.connect(
            lambda Value: Config_ASR.EditConfig('VPR', 'Model_Path', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_ASR_VPR_ModelPath,
            LineEdit = self.ui.LineEdit_ASR_VPR_ModelPath,
            Mode = "SelectDir",
            Directory = NormPath(Path(ModelsDir).joinpath('ASR', 'VPR'), 'Posix')
        )
        self.ui.Button_ASR_VPR_ModelPath_Undo.clicked.connect(
            lambda: self.ui.LineEdit_ASR_VPR_ModelPath.setText(NormPath(Path(ModelsDir).joinpath('ASR', 'VPR', 'Downloaded', 'Ecapa-Tdnn_spectrogram.pth'), 'Posix'))
        )

        Function_SetText(
            Widget = self.ui.Label_ASR_VPR_ModelType,
            Text = SetRichText(
                Body = QCA.translate("Label", "模型类型\n声纹识别模型的类型。")
            )
        )
        self.ui.ComboBox_ASR_VPR_ModelType.addItems(['Ecapa-Tdnn'])
        self.ui.ComboBox_ASR_VPR_ModelType.setCurrentText(
            str(Config_ASR.GetValue('VPR', 'Model_Type', 'Ecapa-Tdnn'))
        )
        self.ui.ComboBox_ASR_VPR_ModelType.currentTextChanged.connect(
            lambda Value: Config_ASR.EditConfig('VPR', 'Model_Type', str(Value))
        )
        self.ui.Button_ASR_VPR_ModelPath_Undo.clicked.connect(
            lambda: self.ui.ComboBox_ASR_VPR_ModelType.setCurrentText('Ecapa-Tdnn')
        )

        Function_SetText(
            Widget = self.ui.Label_ASR_VPR_FeatureMethod,
            Text = SetRichText(
                Body = QCA.translate("Label", "预处理方法\n音频的预处理方法。")
            )
        )
        self.ui.ComboBox_ASR_VPR_FeatureMethod.addItems(['spectrogram', 'melspectrogram'])
        self.ui.ComboBox_ASR_VPR_FeatureMethod.setCurrentText(
            str(Config_ASR.GetValue('VPR', 'Feature_Method', 'spectrogram'))
        )
        self.ui.ComboBox_ASR_VPR_FeatureMethod.currentTextChanged.connect(
            lambda Value: Config_ASR.EditConfig('VPR', 'Feature_Method', str(Value))
        )
        self.ui.Button_ASR_VPR_FeatureMethod_Undo.clicked.connect(
            lambda: self.ui.ComboBox_ASR_VPR_FeatureMethod.setCurrentText('spectrogram')
        )

        Function_SetText(
            Widget = self.ui.Label_ASR_VPR_DurationOfAudio,
            Text = SetRichText(
                Body = QCA.translate("Label", "音频长度\n用于预测的音频长度。")
            )
        )
        self.ui.DoubleSpinBox_ASR_VPR_DurationOfAudio.setRange(0, 30)
        #self.ui.DoubleSpinBox_ASR_VPR_DurationOfAudio.setSingleStep(0.01)
        self.ui.DoubleSpinBox_ASR_VPR_DurationOfAudio.setValue(
            float(Config_ASR.GetValue('VPR', 'Duration_of_Audio', '3.00'))
        )
        self.ui.DoubleSpinBox_ASR_VPR_DurationOfAudio.textChanged.connect(
            lambda Value: Config_ASR.EditConfig('VPR', 'Duration_of_Audio', str(Value))
        )
        self.ui.Button_ASR_VPR_DurationOfAudio_Undo.clicked.connect(
            lambda: self.ui.DoubleSpinBox_ASR_VPR_DurationOfAudio.setValue(3.00)
        )

        self.ui.GroupBox_ASR_VPR_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))

        Function_SetText(
            Widget = self.ui.Label_ASR_VPR_AudioSpeakersDataPath,
            Text = SetRichText(
                Body = QCA.translate("Label", "语音识别结果保存路径\n用于保存最后识别得到的音频文件与对应说话人的信息文件的路径。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_ASR_VPR_AudioSpeakersDataPath,
            Text = str(Config_ASR.GetValue('VPR', 'Audio_Dir_Output', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_ASR_VPR_AudioSpeakersDataPath.textChanged.connect(
            lambda Value: Config_ASR.EditConfig('VPR', 'Audio_Dir_Output', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_ASR_VPR_AudioSpeakersDataPath,
            LineEdit = self.ui.LineEdit_ASR_VPR_AudioSpeakersDataPath,
            Mode = "SaveFile",
            FileType = "txt类型 (*.txt)"
        )
        self.ui.Button_ASR_VPR_AudioSpeakersDataPath_Undo.clicked.connect(
            lambda: self.ui.LineEdit_ASR_VPR_AudioSpeakersDataPath.setText('')
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_ASR_VPR,
            RootItemTexts = [
                self.ui.GroupBox_ASR_VPR_InputParams.title(),
                self.ui.GroupBox_ASR_VPR_VPRParams.title(),
                self.ui.GroupBox_ASR_VPR_OutputParams.title()
            ],
            ChildItemTexts = [
                ("基础设置"),
                ("基础设置","高级设置"),
                ("基础设置")
            ],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_ASR_VPR.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_ASR_VPR_InputParams,
            ScrollArea = self.ui.ScrollArea_Middle_ASR_VPR
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_ASR_VPR.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_ASR_VPR_InputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_ASR_VPR
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_ASR_VPR.topLevelItem(1),
            TargetWidget = self.ui.GroupBox_ASR_VPR_VPRParams,
            ScrollArea = self.ui.ScrollArea_Middle_ASR_VPR
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_ASR_VPR.topLevelItem(1).child(0),
            TargetWidget = self.ui.Frame_ASR_VPR_VPRParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_ASR_VPR
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_ASR_VPR.topLevelItem(1).child(1),
            TargetWidget = self.ui.Frame_ASR_VPR_VPRParams_AdvanceSettings,
            ScrollArea = self.ui.ScrollArea_Middle_ASR_VPR
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_ASR_VPR.topLevelItem(2),
            TargetWidget = self.ui.GroupBox_ASR_VPR_OutputParams,
            ScrollArea = self.ui.ScrollArea_Middle_ASR_VPR
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_ASR_VPR.topLevelItem(2).child(0),
            TargetWidget = self.ui.Frame_ASR_VPR_OutputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_ASR_VPR
        )

        # Right
        MonitorFile_Config_VoiceIdentifier = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_ASR')
        )
        MonitorFile_Config_VoiceIdentifier.start()
        MonitorFile_Config_VoiceIdentifier.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_ASR_VPR.setText(
                FileContent
            )
        )

        self.ui.Button_SyncParams_ASR_VPR.setText(QCA.translate("Button", "关联参数设置"))
        Function_ParamsSynchronizer(
            Trigger = self.ui.Button_SyncParams_ASR_VPR,
            ParamsFrom = [
                self.ui.LineEdit_Process_MediaDirOutput
            ],
            ParamsTo = [
                self.ui.LineEdit_ASR_VPR_AudioDirInput
            ]
        )

        self.ui.Button_CheckOutput_ASR_VPR.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_ASR_VPR,
            URL = self.ui.LineEdit_ASR_VPR_AudioSpeakersDataPath,
            ButtonTooltip = "Click to open"
        )

        # Bottom
        self.ui.Button_ASR_VPR_Execute.setToolTip("执行语音识别和筛选")
        self.ui.Button_ASR_VPR_Terminate.setToolTip("终止语音识别和筛选")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_ASR_VPR_Execute,
            TerminateButton = self.ui.Button_ASR_VPR_Terminate,
            ProgressBar = self.ui.ProgressBar_ASR_VPR,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Voice_Identifying.Execute,
            ParamsFrom = [
                self.ui.Table_ASR_VPR_StdAudioSpeaker,
                self.ui.LineEdit_ASR_VPR_AudioDirInput,
                self.ui.LineEdit_ASR_VPR_AudioSpeakersDataPath,
                self.ui.LineEdit_ASR_VPR_ModelPath,
                self.ui.ComboBox_ASR_VPR_ModelType,
                self.ui.ComboBox_ASR_VPR_FeatureMethod,
                self.ui.DoubleSpinBox_ASR_VPR_DecisionThreshold,
                self.ui.DoubleSpinBox_ASR_VPR_DurationOfAudio
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (
                    QMessageBox.Question, "Ask",
                    "当前任务已执行结束，是否跳转至下一工具界面？",
                    QMessageBox.Yes|QMessageBox.No, [QMessageBox.Yes],
                    [[self.ui.Button_Menu_STT.click]], [[()]]
                )
            ]
        )

        #############################################################
        ######################## Content: STT #######################
        #############################################################

        # Guidance
        DialogBox_STT = MessageBox_Stacked()
        DialogBox_STT.setWindowTitle('Guidance（该引导仅出现一次）')
        DialogBox_STT.SetContent(
            [
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_STT.png')),
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_Layout.png'))
            ],
            [
                '欢迎来到语音转文字工具界面\n将语音文件的内容批量转换为带时间戳的文本并以字幕文件的形式保存',
                '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_STT.clicked.connect(
            lambda: DialogBox_STT.exec() if eval(Config.GetValue('Dialog', 'GuidanceShown_STT', 'False')) is False else None,
            type = Qt.QueuedConnection
        )
        self.ui.Button_Menu_STT.clicked.connect(
            lambda: Config.EditConfig('Dialog', 'GuidanceShown_STT', 'True'),
            type = Qt.QueuedConnection
        )

        # Config
        Path_Config_STT = NormPath(Path(ConfigDir).joinpath('Config_STT.ini'))
        Config_STT = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_STT',
                Path_Config_STT
            )
        )

        # Top
        self.ui.ToolButton_VoiceTranscriber_Title.setText(QCA.translate("ToolButton", "Whisper"))
        self.ui.ToolButton_VoiceTranscriber_Title.setChecked(True)
        self.ui.ToolButton_VoiceTranscriber_Title.setAutoExclusive(True)
        self.ui.ToolButton_VoiceTranscriber_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_STT,
                TargetIndex = 0
            )
        )

        # Middle
        self.ui.GroupBox_STT_Whisper_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))

        Function_SetText(
            Widget = self.ui.Label_STT_Whisper_WAVDir,
            Text = SetRichText(
                Body = QCA.translate("Label", "音频目录\n需要将语音内容转为文字的wav文件的所在目录。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_STT_Whisper_WAVDir,
            Text = str(Config_STT.GetValue('Whisper', 'WAV_Dir', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_STT_Whisper_WAVDir.textChanged.connect(
            lambda Value: Config_STT.EditConfig('Whisper', 'WAV_Dir', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_STT_Whisper_WAVDir,
            LineEdit = self.ui.LineEdit_STT_Whisper_WAVDir,
            Mode = "SelectDir"
        )
        self.ui.Button_STT_Whisper_WAVDir_Undo.clicked.connect(
            lambda: self.ui.LineEdit_STT_Whisper_WAVDir.setText('')
        )

        self.ui.GroupBox_STT_Whisper_WhisperParams.setTitle(QCA.translate("GroupBox", "语音转文字参数"))

        Function_SetText(
            Widget = self.ui.Label_STT_Whisper_ConditionOnPreviousText,
            Text = SetRichText(
                Body = QCA.translate("Label", "关联上下文\n在音频内容具有关联性时启用该项能获得更好的效果，但有概率令模型陷入失败循环。")
            )
        )
        self.ui.CheckBox_STT_Whisper_ConditionOnPreviousText.setChecked(
            eval(Config_STT.GetValue('Whisper', 'Condition_on_Previous_Text', 'False'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_STT_Whisper_ConditionOnPreviousText,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_STT.EditConfig
            ],
            CheckedArgsList = [
                ('Whisper', 'Condition_on_Previous_Text', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_STT.EditConfig
            ],
            UncheckedArgsList = [
                ('Whisper', 'Condition_on_Previous_Text', 'False')
            ],
            TakeEffect = True
        )
        self.ui.Button_STT_Whisper_ConditionOnPreviousText_Undo.clicked.connect(
            lambda: self.ui.CheckBox_STT_Whisper_ConditionOnPreviousText.setChecked(False)
        )

        self.ui.CheckBox_STT_Whisper_WhisperParams_Toggle_AdvanceSettings.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_STT_Whisper_WhisperParams_Toggle_AdvanceSettings,
            CheckedText = "高级设置",
            CheckedEventList = [
                Function_AnimateFrame
            ],
            CheckedArgsList = [
                (
                    self.ui.Frame_STT_Whisper_WhisperParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_STT_Whisper_WhisperParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Extend'
                )
            ],
            UncheckedText = "高级设置",
            UncheckedEventList = [
                Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (
                    self.ui.Frame_STT_Whisper_WhisperParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_STT_Whisper_WhisperParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Reduce'
                )
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_STT_Whisper_ModelPath,
            Text = SetRichText(
                Body = QCA.translate("Label", "模型加载路径\n用于加载的Whisper模型的所在路径。")
            )
        )
        self.ui.LineEdit_STT_Whisper_ModelPath.setText(
            str(Config_STT.GetValue('Whisper', 'Model_Path', NormPath(Path(ModelsDir).joinpath('STT', 'Whisper', 'Downloaded', 'small.pt'), 'Posix')))
        )
        self.ui.LineEdit_STT_Whisper_ModelPath.textChanged.connect(
            lambda Value: Config_STT.EditConfig('Whisper', 'Model_Path', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_STT_Whisper_ModelPath,
            LineEdit = self.ui.LineEdit_STT_Whisper_ModelPath,
            Mode = "SelectDir",
            Directory = NormPath(Path(ModelsDir).joinpath('STT', 'Whisper'), 'Posix')
        )
        self.ui.Button_STT_Whisper_ModelPath_Undo.clicked.connect(
            lambda: self.ui.LineEdit_STT_Whisper_ModelPath.setText(NormPath(Path(ModelsDir).joinpath('STT', 'Whisper', 'Downloaded', 'small.pt'), 'Posix'))
        )

        Function_SetText(
            Widget = self.ui.Label_STT_Whisper_Verbose,
            Text = SetRichText(
                Body = QCA.translate("Label", "启用输出日志\n输出debug日志。")
            )
        )
        self.ui.CheckBox_STT_Whisper_Verbose.setChecked(
            eval(Config_STT.GetValue('Whisper', 'Verbose', 'True'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_STT_Whisper_Verbose,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_STT.EditConfig
            ],
            CheckedArgsList = [
                ('Whisper', 'Verbose', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_STT.EditConfig
            ],
            UncheckedArgsList = [
                ('Whisper', 'Verbose', 'False')
            ],
            TakeEffect = True
        )
        self.ui.Button_STT_Whisper_Verbose_Undo.clicked.connect(
            lambda: self.ui.CheckBox_STT_Whisper_Verbose.setChecked(True)
        )

        Function_SetText(
            Widget = self.ui.Label_STT_Whisper_fp16,
            Text = SetRichText(
                Body = QCA.translate("Label", "半精度计算\n主要使用半精度浮点数进行计算，若GPU不可用则忽略或禁用此项。")
            )
        )
        self.ui.CheckBox_STT_Whisper_fp16.setChecked(
            eval(Config_STT.GetValue('Whisper', 'fp16', 'True'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_STT_Whisper_fp16,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_STT.EditConfig
            ],
            CheckedArgsList = [
                ('Whisper', 'fp16', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_STT.EditConfig
            ],
            UncheckedArgsList = [
                ('Whisper', 'fp16', 'False')
            ],
            TakeEffect = True
        )
        self.ui.Button_STT_Whisper_fp16_Undo.clicked.connect(
            lambda: self.ui.CheckBox_STT_Whisper_fp16.setChecked(True)
        )

        Function_SetText(
            Widget = self.ui.Label_STT_Whisper_Language,
            Text = SetRichText(
                Body = QCA.translate("Label", "所用语言\n音频中说话人所使用的语言，若自动检测则保持'None'即可。")
            )
        )
        self.ui.ComboBox_STT_Whisper_Language.addItems(['中', '英', '日', 'None'])
        self.ui.ComboBox_STT_Whisper_Language.setCurrentText(
            str(Config_STT.GetValue('Whisper', 'Language', 'None'))
        )
        self.ui.ComboBox_STT_Whisper_Language.currentTextChanged.connect(
            lambda Value: Config_STT.EditConfig('Whisper', 'Language', str(Value))
        )
        self.ui.Button_STT_Whisper_Language_Undo.clicked.connect(
            lambda: self.ui.ComboBox_STT_Whisper_Language.setCurrentText('None')
        )

        self.ui.GroupBox_STT_Whisper_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))

        Function_SetText(
            Widget = self.ui.Label_STT_Whisper_SRTDir,
            Text = SetRichText(
                Body = QCA.translate("Label", "字幕输出目录\n用于保存最后生成的字幕文件的目录。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_STT_Whisper_SRTDir,
            Text = str(Config_STT.GetValue('Whisper', 'SRT_Dir', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_STT_Whisper_SRTDir.textChanged.connect(
            lambda Value: Config_STT.EditConfig('Whisper', 'SRT_Dir', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_STT_Whisper_SRTDir,
            LineEdit = self.ui.LineEdit_STT_Whisper_SRTDir,
            Mode = "SelectDir"
        )
        self.ui.Button_STT_Whisper_SRTDir_Undo.clicked.connect(
            lambda: self.ui.LineEdit_STT_Whisper_SRTDir.setText('')
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_STT_Whisper,
            RootItemTexts = [
                self.ui.GroupBox_STT_Whisper_InputParams.title(),
                self.ui.GroupBox_STT_Whisper_WhisperParams.title(),
                self.ui.GroupBox_STT_Whisper_OutputParams.title()
            ],
            ChildItemTexts = [
                ("基础设置"),
                ("基础设置","高级设置"),
                ("基础设置")
            ],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_STT_Whisper.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_STT_Whisper_InputParams,
            ScrollArea = self.ui.ScrollArea_Middle_STT_Whisper
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_STT_Whisper.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_STT_Whisper_InputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_STT_Whisper
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_STT_Whisper.topLevelItem(1),
            TargetWidget = self.ui.GroupBox_STT_Whisper_WhisperParams,
            ScrollArea = self.ui.ScrollArea_Middle_STT_Whisper
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_STT_Whisper.topLevelItem(1).child(0),
            TargetWidget = self.ui.Frame_STT_Whisper_WhisperParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_STT_Whisper
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_STT_Whisper.topLevelItem(1).child(1),
            TargetWidget = self.ui.Frame_STT_Whisper_WhisperParams_AdvanceSettings,
            ScrollArea = self.ui.ScrollArea_Middle_STT_Whisper
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_STT_Whisper.topLevelItem(2),
            TargetWidget = self.ui.GroupBox_STT_Whisper_OutputParams,
            ScrollArea = self.ui.ScrollArea_Middle_STT_Whisper
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_STT_Whisper.topLevelItem(2).child(0),
            TargetWidget = self.ui.Frame_STT_Whisper_OutputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_STT_Whisper
        )

        # Right
        MonitorFile_Config_VoiceTranscriber = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_STT')
        )
        MonitorFile_Config_VoiceTranscriber.start()
        MonitorFile_Config_VoiceTranscriber.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_STT_Whisper.setText(
                FileContent
            )
        )

        self.ui.Button_SyncParams_STT_Whisper.setText(QCA.translate("Button", "关联参数设置"))
        '''
        Function_ParamsSynchronizer(
            Trigger = self.ui.Button_SyncParams_STT_Whisper,
            ParamsFrom = [
            ],
            ParamsTo = [
            ]
        )
        '''

        self.ui.Button_CheckOutput_STT_Whisper.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_STT_Whisper,
            URL = self.ui.LineEdit_STT_Whisper_SRTDir,
            ButtonTooltip = "Click to open"
        )

        # Bottom
        self.ui.Button_STT_Whisper_Execute.setToolTip("执行语音转文字字幕")
        self.ui.Button_STT_Whisper_Terminate.setToolTip("终止语音转文字字幕")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_STT_Whisper_Execute,
            TerminateButton = self.ui.Button_STT_Whisper_Terminate,
            ProgressBar = self.ui.ProgressBar_STT_Whisper,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Voice_Transcribing.Execute,
            ParamsFrom = [
                self.ui.LineEdit_STT_Whisper_ModelPath,
                self.ui.LineEdit_STT_Whisper_WAVDir,
                self.ui.LineEdit_STT_Whisper_SRTDir,
                self.ui.CheckBox_STT_Whisper_Verbose,
                'transcribe', #self.ui.ComboBox_STT_Whisper_Task
                self.ui.ComboBox_STT_Whisper_Language,
                self.ui.CheckBox_STT_Whisper_ConditionOnPreviousText,
                self.ui.CheckBox_STT_Whisper_fp16
            ],
            EmptyAllowed = [
                self.ui.ComboBox_STT_Whisper_Language
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (
                    QMessageBox.Question, "Ask",
                    "当前任务已执行结束，是否跳转至下一工具界面？",
                    QMessageBox.Yes|QMessageBox.No, [QMessageBox.Yes],
                    [[self.ui.Button_Menu_Dataset.click]], [[()]]
                )
            ]
        )

        #############################################################
        ###################### Content: Dataset #####################
        #############################################################

        # Guidance
        DialogBox_Dataset = MessageBox_Stacked()
        DialogBox_Dataset.setWindowTitle('Guidance（该引导仅出现一次）')
        DialogBox_Dataset.SetContent(
            [
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_Dataset.png')),
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_Layout.png'))
            ],
            [
                '欢迎来到数据集工具界面\n生成适用于语音模型训练的数据集。用户需要提供语音文件与对应的字幕文件',
                '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_Dataset.clicked.connect(
            lambda: DialogBox_Dataset.exec() if eval(Config.GetValue('Dialog', 'GuidanceShown_Dataset', 'False')) is False else None,
            type = Qt.QueuedConnection
        )
        self.ui.Button_Menu_Dataset.clicked.connect(
            lambda: Config.EditConfig('Dialog', 'GuidanceShown_Dataset', 'True'),
            type = Qt.QueuedConnection
        )

        # Config
        Path_Config_DAT = NormPath(Path(ConfigDir).joinpath('Config_DAT.ini'))
        Config_DAT = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_DAT',
                Path_Config_DAT
            )
        )

        # Top
        self.ui.ToolButton_DatasetCreator_Title.setText(QCA.translate("ToolButton", "VITS"))
        self.ui.ToolButton_DatasetCreator_Title.setChecked(True)
        self.ui.ToolButton_DatasetCreator_Title.setAutoExclusive(True)
        self.ui.ToolButton_DatasetCreator_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Dataset,
                TargetIndex = 0
            )
        )

        # Middle
        self.ui.GroupBox_DAT_VITS_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))

        Function_SetText(
            Widget = self.ui.Label_DAT_VITS_AudioSpeakersDataPath,
            Text = SetRichText(
                Body = QCA.translate("Label", "语音识别结果文件路径\n由语音识别得到的音频文件与对应说话人的信息文件的路径。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath,
            Text = str(Config_DAT.GetValue('VITS', 'WAV_Dir', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath.textChanged.connect(
            lambda Value: Config_DAT.EditConfig('VITS', 'WAV_Dir', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_DAT_VITS_AudioSpeakersDataPath,
            LineEdit = self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath,
            Mode = "SelectPath"
        )
        self.ui.Button_DAT_VITS_AudioSpeakersDataPath_Undo.clicked.connect(
            lambda: self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath.setText('')
        )

        Function_SetText(
            Widget = self.ui.Label_DAT_VITS_SRTDir,
            Text = SetRichText(
                Body = QCA.translate("Label", "字幕输入目录\n需要转为适用于模型训练的csv文件的srt文件的所在目录。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_DAT_VITS_SRTDir,
            Text = str(Config_DAT.GetValue('VITS', 'SRT_Dir', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_DAT_VITS_SRTDir.textChanged.connect(
            lambda Value: Config_DAT.EditConfig('VITS', 'SRT_Dir', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_DAT_VITS_SRTDir,
            LineEdit = self.ui.LineEdit_DAT_VITS_SRTDir,
            Mode = "SelectDir"
        )
        self.ui.Button_DAT_VITS_SRTDir_Undo.clicked.connect(
            lambda: self.ui.LineEdit_DAT_VITS_SRTDir.setText('')
        )

        self.ui.GroupBox_DAT_VITS_VITSParams.setTitle(QCA.translate("GroupBox", "数据集参数"))

        Function_SetText(
            Widget = self.ui.Label_DAT_VITS_AddAuxiliaryData,
            Text = SetRichText(
                Body = QCA.translate("Label", "添加辅助数据\n添加用以辅助训练的数据集，若当前语音数据的质量/数量较低则建议启用。")
            )
        )
        self.ui.CheckBox_DAT_VITS_AddAuxiliaryData.setChecked(
            eval(Config_DAT.GetValue('VITS', 'Add_AuxiliaryData', 'False'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_DAT_VITS_AddAuxiliaryData,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_DAT.EditConfig
            ],
            CheckedArgsList = [
                ('VITS', 'Add_AuxiliaryData', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_DAT.EditConfig
            ],
            UncheckedArgsList = [
                ('VITS', 'Add_AuxiliaryData', 'False')
            ],
            TakeEffect = True
        )
        self.ui.Button_DAT_VITS_AddAuxiliaryData_Undo.clicked.connect(
            lambda: self.ui.CheckBox_DAT_VITS_AddAuxiliaryData.setChecked(False)
        )

        self.ui.CheckBox_DAT_VITS_VITSParams_Toggle_AdvanceSettings.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_DAT_VITS_VITSParams_Toggle_AdvanceSettings,
            CheckedText = "高级设置",
            CheckedEventList = [
                Function_AnimateFrame
            ],
            CheckedArgsList = [
                (
                    self.ui.Frame_DAT_VITS_VITSParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_DAT_VITS_VITSParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Extend'
                )
            ],
            UncheckedText = "高级设置",
            UncheckedEventList = [
                Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (
                    self.ui.Frame_DAT_VITS_VITSParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_DAT_VITS_VITSParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Reduce'
                )
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_DAT_VITS_TrainRatio,
            Text = SetRichText(
                Body = QCA.translate("Label", "训练集占比\n划分给训练集的数据在数据集中所占的比例。")
            )
        )
        self.ui.DoubleSpinBox_DAT_VITS_TrainRatio.setRange(0.5, 0.9)
        self.ui.DoubleSpinBox_DAT_VITS_TrainRatio.setSingleStep(0.1)
        self.ui.DoubleSpinBox_DAT_VITS_TrainRatio.setValue(
            float(Config_DAT.GetValue('VITS', 'TrainRatio', '0.7'))
        )
        self.ui.DoubleSpinBox_DAT_VITS_TrainRatio.valueChanged.connect(
            lambda Value: Config_DAT.EditConfig('VITS', 'TrainRatio', str(Value))
        )
        self.ui.Button_DAT_VITS_TrainRatio_Undo.clicked.connect(
            lambda: self.ui.DoubleSpinBox_DAT_VITS_TrainRatio.setValue(0.7)
        )

        Function_SetText(
            Widget = self.ui.Label_DAT_VITS_SampleRate,
            Text = SetRichText(
                Body = QCA.translate("Label", "采样率 (HZ)\n数据集所要求的音频采样率，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_DAT_VITS_SampleRate.addItems(['22050', '44100', '48000', '96000', '192000', 'None'])
        self.ui.ComboBox_DAT_VITS_SampleRate.setCurrentText(
            str(Config_DAT.GetValue('VITS', 'SampleRate', '22050'))
        )
        self.ui.ComboBox_DAT_VITS_SampleRate.currentTextChanged.connect(
            lambda Value: Config_DAT.EditConfig('VITS', 'SampleRate', str(Value))
        )
        self.ui.Button_DAT_VITS_SampleRate_Undo.clicked.connect(
            lambda: self.ui.ComboBox_DAT_VITS_SampleRate.setCurrentText('22050')
        )

        Function_SetText(
            Widget = self.ui.Label_DAT_VITS_SampleWidth,
            Text = SetRichText(
                Body = QCA.translate("Label", "采样位数\n数据集所要求的音频采样位数，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_DAT_VITS_SampleWidth.addItems(['8', '16', '24', '32', '32 (Float)', 'None'])
        self.ui.ComboBox_DAT_VITS_SampleWidth.setCurrentText(
            str(Config_DAT.GetValue('VITS', 'SampleWidth', '16'))
        )
        self.ui.ComboBox_DAT_VITS_SampleWidth.currentTextChanged.connect(
            lambda Value: Config_DAT.EditConfig('VITS', 'SampleWidth', str(Value))
        )
        self.ui.Button_DAT_VITS_SampleWidth_Undo.clicked.connect(
            lambda: self.ui.ComboBox_DAT_VITS_SampleWidth.setCurrentText('16')
        )

        Function_SetText(
            Widget = self.ui.Label_DAT_VITS_ToMono,
            Text = SetRichText(
                Body = QCA.translate("Label", "合并声道\n将数据集音频的声道合并为单声道。")
            )
        )
        self.ui.CheckBox_DAT_VITS_ToMono.setChecked(
            eval(Config_DAT.GetValue('VITS', 'ToMono', 'True'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_DAT_VITS_ToMono,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_DAT.EditConfig
            ],
            CheckedArgsList = [
                ('VITS', 'ToMono', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_DAT.EditConfig
            ],
            UncheckedArgsList = [
                ('VITS', 'ToMono', 'False')
            ],
            TakeEffect = True
        )
        self.ui.Button_DAT_VITS_ToMono_Undo.clicked.connect(
            lambda: self.ui.CheckBox_DAT_VITS_ToMono.setChecked(True)
        )

        Function_SetText(
            Widget = self.ui.Label_DAT_VITS_AuxiliaryDataPath,
            Text = SetRichText(
                Body = QCA.translate("Label", "辅助数据文本路径\n辅助数据集的文本的所在路径。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath,
            Text = str(Config_DAT.GetValue('VITS', 'AuxiliaryData_Path', NormPath(Path(CurrentDir).joinpath('AuxiliaryData', 'AuxiliaryData.txt')) if Path(CurrentDir).joinpath('AuxiliaryData', 'AuxiliaryData.txt').exists() else '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath.textChanged.connect(
            lambda Value: Config_DAT.EditConfig('VITS', 'AuxiliaryData_Path', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_DAT_VITS_AuxiliaryDataPath,
            LineEdit = self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath,
            Mode = "SelectFile",
            FileType = "文本类型 (*.csv *.txt)"
        )
        self.ui.Button_DAT_VITS_AuxiliaryDataPath_Undo.clicked.connect(
            lambda: self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath.setText(NormPath(Path(CurrentDir).joinpath('AuxiliaryData', 'AuxiliaryData.txt')) if Path(CurrentDir).joinpath('AuxiliaryData', 'AuxiliaryData.txt').exists() else '')
        )

        self.ui.GroupBox_DAT_VITS_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))

        Function_SetText(
            Widget = self.ui.Label_DAT_VITS_WAVDirSplit,
            Text = SetRichText(
                Body = QCA.translate("Label", "音频输出目录\n用于保存最后处理完成的音频的目录。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_DAT_VITS_WAVDirSplit,
            Text = str(Config_DAT.GetValue('VITS', 'WAV_Dir_Split', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_DAT_VITS_WAVDirSplit.textChanged.connect(
            lambda Value: Config_DAT.EditConfig('VITS', 'WAV_Dir_Split', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_DAT_VITS_WAVDirSplit,
            LineEdit = self.ui.LineEdit_DAT_VITS_WAVDirSplit,
            Mode = "SelectDir"
        )
        self.ui.Button_DAT_VITS_WAVDirSplit_Undo.clicked.connect(
            lambda: self.ui.LineEdit_DAT_VITS_WAVDirSplit.setText('')
        )

        Function_SetText(
            Widget = self.ui.Label_DAT_VITS_FileListPathTraining,
            Text = SetRichText(
                Body = QCA.translate("Label", "训练集文本路径\n用于保存最后生成的训练集txt文件的路径。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_DAT_VITS_FileListPathTraining,
            Text = str(Config_DAT.GetValue('VITS', 'FileList_Path_Training', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_DAT_VITS_FileListPathTraining.textChanged.connect(
            lambda Value: Config_DAT.EditConfig('VITS', 'FileList_Path_Training', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_DAT_VITS_FileListPathTraining,
            LineEdit = self.ui.LineEdit_DAT_VITS_FileListPathTraining,
            Mode = "SaveFile",
            FileType = "txt类型 (*.txt)"
        )
        self.ui.Button_DAT_VITS_FileListPathTraining_Undo.clicked.connect(
            lambda: self.ui.LineEdit_DAT_VITS_FileListPathTraining.setText('')
        )

        Function_SetText(
            Widget = self.ui.Label_DAT_VITS_FileListPathValidation,
            Text = SetRichText(
                Body = QCA.translate("Label", "验证集文本路径\n用于保存最后生成的验证集txt文件的路径。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_DAT_VITS_FileListPathValidation,
            Text = str(Config_DAT.GetValue('VITS', 'FileList_Path_Validation', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_DAT_VITS_FileListPathValidation.textChanged.connect(
            lambda Value: Config_DAT.EditConfig('VITS', 'FileList_Path_Validation', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_DAT_VITS_FileListPathValidation,
            LineEdit = self.ui.LineEdit_DAT_VITS_FileListPathValidation,
            Mode = "SaveFile",
            FileType = "txt类型 (*.txt)"
        )
        self.ui.Button_DAT_VITS_FileListPathValidation_Undo.clicked.connect(
            lambda: self.ui.LineEdit_DAT_VITS_FileListPathValidation.setText('')
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_DAT_VITS,
            RootItemTexts = [
                self.ui.GroupBox_DAT_VITS_InputParams.title(),
                self.ui.GroupBox_DAT_VITS_VITSParams.title(),
                self.ui.GroupBox_DAT_VITS_OutputParams.title()
            ],
            ChildItemTexts = [
                ("基础设置"),
                ("基础设置","高级设置"),
                ("基础设置")
            ],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_DAT_VITS.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_DAT_VITS_InputParams,
            ScrollArea = self.ui.ScrollArea_Middle_DAT_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_DAT_VITS.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_DAT_VITS_InputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_DAT_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_DAT_VITS.topLevelItem(1),
            TargetWidget = self.ui.GroupBox_DAT_VITS_VITSParams,
            ScrollArea = self.ui.ScrollArea_Middle_DAT_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_DAT_VITS.topLevelItem(1).child(0),
            TargetWidget = self.ui.Frame_DAT_VITS_VITSParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_DAT_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_DAT_VITS.topLevelItem(1).child(1),
            TargetWidget = self.ui.Frame_DAT_VITS_VITSParams_AdvanceSettings,
            ScrollArea = self.ui.ScrollArea_Middle_DAT_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_DAT_VITS.topLevelItem(2),
            TargetWidget = self.ui.GroupBox_DAT_VITS_OutputParams,
            ScrollArea = self.ui.ScrollArea_Middle_DAT_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_DAT_VITS.topLevelItem(2).child(0),
            TargetWidget = self.ui.Frame_DAT_VITS_OutputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_DAT_VITS
        )

        # Right
        MonitorFile_Config_DatasetCreator = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_DAT')
        )
        MonitorFile_Config_DatasetCreator.start()
        MonitorFile_Config_DatasetCreator.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_DAT_VITS.setText(
                FileContent
            )
        )

        self.ui.Button_SyncParams_DAT_VITS.setText(QCA.translate("Button", "关联参数设置"))
        Function_ParamsSynchronizer(
            Trigger = self.ui.Button_SyncParams_DAT_VITS,
            ParamsFrom = [
                self.ui.LineEdit_ASR_VPR_AudioSpeakersDataPath,
                self.ui.LineEdit_STT_Whisper_SRTDir
            ],
            ParamsTo = [
                self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath,
                self.ui.LineEdit_DAT_VITS_SRTDir
            ]
        )

        self.ui.Button_CheckOutput_DAT_VITS.setText(QCA.translate("Button", "打开输出文件"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_DAT_VITS,
            URL = [
                self.ui.LineEdit_DAT_VITS_FileListPathTraining,
                self.ui.LineEdit_DAT_VITS_FileListPathValidation
            ],
            ButtonTooltip = "Click to open"
        )

        # Bottom
        self.ui.Button_DAT_VITS_Execute.setToolTip("执行语音数据集制作")
        self.ui.Button_DAT_VITS_Terminate.setToolTip("终止语音数据集制作")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_DAT_VITS_Execute,
            TerminateButton = self.ui.Button_DAT_VITS_Terminate,
            ProgressBar = self.ui.ProgressBar_DAT_VITS,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Dataset_Creating.Execute,
            ParamsFrom = [
                self.ui.LineEdit_DAT_VITS_SRTDir,
                self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath,
                self.ui.ComboBox_DAT_VITS_SampleRate,
                self.ui.ComboBox_DAT_VITS_SampleWidth,
                self.ui.CheckBox_DAT_VITS_ToMono,
                self.ui.LineEdit_DAT_VITS_WAVDirSplit,
                self.ui.CheckBox_DAT_VITS_AddAuxiliaryData,
                self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath,
                self.ui.DoubleSpinBox_DAT_VITS_TrainRatio,
                self.ui.LineEdit_DAT_VITS_FileListPathTraining,
                self.ui.LineEdit_DAT_VITS_FileListPathValidation
            ],
            EmptyAllowed = [
                self.ui.ComboBox_DAT_VITS_SampleRate,
                self.ui.ComboBox_DAT_VITS_SampleWidth,
                self.ui.LineEdit_DAT_VITS_AuxiliaryDataPath
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (
                    QMessageBox.Question, "Ask",
                    "当前任务已执行结束，是否跳转至下一工具界面？",
                    QMessageBox.Yes|QMessageBox.No, [QMessageBox.Yes],
                    [[self.ui.Button_Menu_Train.click]], [[()]]
                )
            ]
        )

        #############################################################
        ####################### Content: Train ######################
        #############################################################

        # Guidance
        DialogBox_Train = MessageBox_Stacked()
        DialogBox_Train.setWindowTitle('Guidance（该引导仅出现一次）')
        DialogBox_Train.SetContent(
            [
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_Train.png')),
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_Layout.png'))
            ],
            [
                '欢迎来到语音训练工具界面\n训练出适用于语音合成的模型文件。用户需要提供语音数据集',
                '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_Train.clicked.connect(
            lambda: DialogBox_Train.exec() if eval(Config.GetValue('Dialog', 'GuidanceShown_Train', 'False')) is False else None,
            type = Qt.QueuedConnection
        )
        self.ui.Button_Menu_Train.clicked.connect(
            lambda: Config.EditConfig('Dialog', 'GuidanceShown_Train', 'True'),
            type = Qt.QueuedConnection
        )

        # Config
        Path_Config_Train = NormPath(Path(ConfigDir).joinpath('Config_Train.ini'))
        Config_Train = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_Train',
                Path_Config_Train
            )
        )

        # Top
        self.ui.ToolButton_VoiceTrainer_Title.setText(QCA.translate("ToolButton", "VITS"))
        self.ui.ToolButton_VoiceTrainer_Title.setChecked(True)
        self.ui.ToolButton_VoiceTrainer_Title.setAutoExclusive(True)
        self.ui.ToolButton_VoiceTrainer_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Train,
                TargetIndex = 0
            )
        )

        # Midlle
        self.ui.GroupBox_Train_VITS_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))
        
        Function_SetText(
            Widget = self.ui.Label_Train_VITS_FileListPathTraining,
            Text = SetRichText(
                Body = QCA.translate("Label", "训练集文本路径\n用于提供训练集音频路径及其语音内容的训练集txt文件的所在路径。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Train_VITS_FileListPathTraining,
            Text = str(Config_Train.GetValue('VITS', 'FileList_Path_Training', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Train_VITS_FileListPathTraining.textChanged.connect(
            lambda Value: Config_Train.EditConfig('VITS', 'FileList_Path_Training', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Train_VITS_FileListPathTraining,
            LineEdit = self.ui.LineEdit_Train_VITS_FileListPathTraining,
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)"
        )
        self.ui.Button_Train_VITS_FileListPathTraining_Undo.clicked.connect(
            lambda: self.ui.LineEdit_Train_VITS_FileListPathTraining.setText('')
        )

        Function_SetText(
            Widget = self.ui.Label_Train_VITS_FileListPathValidation,
            Text = SetRichText(
                Body = QCA.translate("Label", "验证集文本路径\n用于提供验证集音频路径及其语音内容的验证集txt文件的所在路径。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Train_VITS_FileListPathValidation,
            Text = str(Config_Train.GetValue('VITS', 'FileList_Path_Validation', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Train_VITS_FileListPathValidation.textChanged.connect(
            lambda Value: Config_Train.EditConfig('VITS', 'FileList_Path_Validation', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Train_VITS_FileListPathValidation,
            LineEdit = self.ui.LineEdit_Train_VITS_FileListPathValidation,
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)"
        )
        self.ui.Button_Train_VITS_FileListPathValidation_Undo.clicked.connect(
            lambda: self.ui.LineEdit_Train_VITS_FileListPathValidation.setText('')
        )

        self.ui.GroupBox_Train_VITS_VITSParams.setTitle(QCA.translate("GroupBox", "训练参数"))

        Function_SetText(
            Widget = self.ui.Label_Train_VITS_Epochs,
            Text = SetRichText(
                Body = QCA.translate("Label", "迭代轮数\n将全部样本完整迭代一轮的次数。")
            )
        )
        self.ui.SpinBox_Train_VITS_Epochs.setRange(30, 300000)
        self.ui.SpinBox_Train_VITS_Epochs.setSingleStep(1)
        self.ui.SpinBox_Train_VITS_Epochs.setValue(
            int(Config_Train.GetValue('VITS', 'Epochs', '100'))
        )
        self.ui.SpinBox_Train_VITS_Epochs.valueChanged.connect(
            lambda Value: Config_Train.EditConfig('VITS', 'Epochs', str(Value))
        )
        self.ui.SpinBox_Train_VITS_Epochs.setToolTip("提示：在均没有预训练模型与辅助数据的情况下建议从一万轮次起步")
        self.ui.Button_Train_VITS_Epochs_Undo.clicked.connect(
            lambda: self.ui.SpinBox_Train_VITS_Epochs.setValue(100)
        )

        Function_SetText(
            Widget = self.ui.Label_Train_VITS_BatchSize,
            Text = SetRichText(
                Body = QCA.translate("Label", "批处理量\n每轮迭代中单位批次的样本数量，需根据GPU的性能调节该值。")
            )
        )
        self.ui.SpinBox_Train_VITS_BatchSize.setRange(2, 128)
        self.ui.SpinBox_Train_VITS_BatchSize.setSingleStep(1)
        self.ui.SpinBox_Train_VITS_BatchSize.setValue(
            int(Config_Train.GetValue('VITS', 'Batch_Size', '4'))
        )
        self.ui.SpinBox_Train_VITS_BatchSize.valueChanged.connect(
            lambda Value: Config_Train.EditConfig('VITS', 'Batch_Size', str(Value))
        )
        self.ui.SpinBox_Train_VITS_BatchSize.setToolTip("建议：4~6G: 2; 8~10G: 4; 12~14G: 8; ...")
        self.ui.Button_Train_VITS_BatchSize_Undo.clicked.connect(
            lambda: self.ui.SpinBox_Train_VITS_BatchSize.setValue(4)
        )

        Function_SetText(
            Widget = self.ui.Label_Train_VITS_UsePretrainedModels,
            Text = SetRichText(
                Body = QCA.translate("Label", "使用预训练模型\n使用预训练模型（底模），其载入优先级高于检查点。")
            )
        )
        self.ui.CheckBox_Train_VITS_UsePretrainedModels.setChecked(
            eval(Config_Train.GetValue('VITS', 'Use_PretrainedModels', 'True'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Train_VITS_UsePretrainedModels,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Train.EditConfig
            ],
            CheckedArgsList = [
                ('VITS', 'Use_PretrainedModels', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Train.EditConfig
            ],
            UncheckedArgsList = [
                ('VITS', 'Use_PretrainedModels', 'False')
            ],
            TakeEffect = True
        )
        self.ui.Button_Train_VITS_UsePretrainedModels_Undo.clicked.connect(
            lambda: self.ui.CheckBox_Train_VITS_UsePretrainedModels.setChecked(True)
        )

        '''
        Function_SetText(
            Widget = self.ui.Label_Train_VITS_OutputName,
            Text = SetRichText(
                Body = QCA.translate("Label", "输出名字\n训练所得模型与对应配置文件的名字。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Train_VITS_OutputName,
            Text = str(Config_Train.GetValue('VITS', 'Output_Name', str(datetime.today()))),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Train_VITS_OutputName.textChanged.connect(
            lambda Value: Config_Train.EditConfig('VITS', 'Output_Name', str(Value))
        )
        self.ui.Button_Train_VITS_OutputName_Undo.clicked.connect(
            lambda: self.ui.LineEdit_Train_VITS_OutputName.setText(str(datetime.today()))
        )
        '''

        self.ui.CheckBox_Train_VITS_VITSParams_Toggle_AdvanceSettings.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Train_VITS_VITSParams_Toggle_AdvanceSettings,
            CheckedText = "高级设置",
            CheckedEventList = [
                Function_AnimateFrame
            ],
            CheckedArgsList = [
                (
                    self.ui.Frame_Train_VITS_VITSParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_Train_VITS_VITSParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Extend'
                )
            ],
            UncheckedText = "高级设置",
            UncheckedEventList = [
                Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (
                    self.ui.Frame_Train_VITS_VITSParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_Train_VITS_VITSParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Reduce'
                )
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Train_VITS_NumWorkers,
            Text = SetRichText(
                Body = QCA.translate("Label", "进程数量\n进行数据加载时可并行的进程数量，需根据CPU的性能调节该值。")
            )
        )
        self.ui.SpinBox_Train_VITS_NumWorkers.setRange(2, 32)
        self.ui.SpinBox_Train_VITS_NumWorkers.setSingleStep(2)
        self.ui.SpinBox_Train_VITS_NumWorkers.setValue(
            int(Config_Train.GetValue('VITS', 'Num_Workers', '4'))
        )
        self.ui.SpinBox_Train_VITS_NumWorkers.valueChanged.connect(
            lambda Value: Config_Train.EditConfig('VITS', 'Num_Workers', str(Value))
        )
        self.ui.SpinBox_Train_VITS_NumWorkers.setToolTip("提示：如果配置属于低U高显的话不妨试试把数值降到2。")
        self.ui.Button_Train_VITS_NumWorkers_Undo.clicked.connect(
            lambda: self.ui.SpinBox_Train_VITS_NumWorkers.setValue(4)
        )

        Function_SetText(
            Widget = self.ui.Label_Train_VITS_FP16Run,
            Text = SetRichText(
                Body = QCA.translate("Label", "半精度训练\n通过混合了float16精度的训练方式减小显存占用以支持更大的批处理量。")
            )
        )
        self.ui.CheckBox_Train_VITS_FP16Run.setChecked(
            eval(Config_Train.GetValue('VITS', 'FP16_Run', 'True'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Train_VITS_FP16Run,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Train.EditConfig
            ],
            CheckedArgsList = [
                ('VITS', 'FP16_Run', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Train.EditConfig
            ],
            UncheckedArgsList = [
                ('VITS', 'FP16_Run', 'False')
            ],
            TakeEffect = True
        )
        self.ui.Button_Train_VITS_FP16Run_Undo.clicked.connect(
            lambda: self.ui.CheckBox_Train_VITS_FP16Run.setChecked(True)
        )

        Function_SetText(
            Widget = self.ui.Label_Train_VITS_ModelPathPretrainedG,
            Text = SetRichText(
                Body = QCA.translate("Label", "预训练G模型路径\n预训练生成器（Generator）模型的所在路径。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Train_VITS_ModelPathPretrainedG,
            Text = str(Config_Train.GetValue('VITS', 'Model_Path_Pretrained_G', NormPath(Path(ModelsDir).joinpath('TTS', 'VITS', 'Downloaded', 'Standard_G.pth'), 'Posix'))),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Train_VITS_ModelPathPretrainedG.textChanged.connect(
            lambda Value: Config_Train.EditConfig('VITS', 'Model_Path_Pretrained_G', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Train_VITS_ModelPathPretrainedG,
            LineEdit = self.ui.LineEdit_Train_VITS_ModelPathPretrainedG,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            Directory = NormPath(Path(ModelsDir).joinpath('TTS', 'VITS', 'Downloaded'), 'Posix')
        )
        self.ui.Button_Train_VITS_ModelPathPretrainedG_Undo.clicked.connect(
            lambda: self.ui.LineEdit_Train_VITS_ModelPathPretrainedG.setText(NormPath(Path(ModelsDir).joinpath('TTS', 'VITS', 'Downloaded', 'Standard_G.pth'), 'Posix'))
        )

        Function_SetText(
            Widget = self.ui.Label_Train_VITS_ModelPathPretrainedD,
            Text = SetRichText(
                Body = QCA.translate("Label", "预训练D模型路径\n预训练判别器（Discriminator）模型的所在路径。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Train_VITS_ModelPathPretrainedD,
            Text = str(Config_Train.GetValue('VITS', 'Model_Path_Pretrained_D', NormPath(Path(ModelsDir).joinpath('TTS', 'VITS', 'Downloaded', 'Standard_D.pth'), 'Posix'))),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Train_VITS_ModelPathPretrainedD.textChanged.connect(
            lambda Value: Config_Train.EditConfig('VITS', 'Model_Path_Pretrained_D', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Train_VITS_ModelPathPretrainedD,
            LineEdit = self.ui.LineEdit_Train_VITS_ModelPathPretrainedD,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            Directory = NormPath(Path(ModelsDir).joinpath('TTS', 'VITS', 'Pretrained'), 'Posix')
        )
        self.ui.Button_Train_VITS_ModelPathPretrainedD_Undo.clicked.connect(
            lambda: self.ui.LineEdit_Train_VITS_ModelPathPretrainedD.setText(NormPath(Path(ModelsDir).joinpath('TTS', 'VITS', 'Downloaded', 'Standard_D.pth'), 'Posix'))
        )

        Function_SetText(
            Widget = self.ui.Label_Train_VITS_KeepOriginalSpeakers,
            Text = SetRichText(
                Body = QCA.translate("Label", "保留原说话人（实验性）\n保留预训练模型中原有的说话人。")
            )
        )
        self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers.setChecked(
            eval(Config_Train.GetValue('VITS', 'Keep_Original_Speakers', 'False'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Train.EditConfig
            ],
            CheckedArgsList = [
                ('VITS', 'Keep_Original_Speakers', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Train.EditConfig
            ],
            UncheckedArgsList = [
                ('VITS', 'Keep_Original_Speakers', 'False')
            ],
            TakeEffect = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers,
            CheckedEventList = [
                Function_ShowMessageBox
            ],
            CheckedArgsList = [
                (
                    QMessageBox.Warning, "Tip",
                    "开启该实验性功能需要注意以下几点：\n"
                    "1. 为防止老角色的音色在训练过程中被逐渐遗忘，请保证每个原角色至少有一两条音频参与训练。\n"
                    "2. 为防止老角色的顺序被重组（导致音色混乱），请保证在'配置路径'选项中设置的配置文件包含了底模的角色信息。\n"
                    "3. 相对的，需要适当增加迭代轮数以保证训练效果且每轮迭代所的花费时间也会增加。"
                )
            ],
            TakeEffect = False
        )
        self.ui.Button_Train_VITS_KeepOriginalSpeakers_Undo.clicked.connect(
            lambda: self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers.setChecked(False)
        )

        self.ui.GroupBox_Train_VITS_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))

        Function_SetText(
            Widget = self.ui.Label_Train_VITS_EvalInterval,
            Text = SetRichText(
                Body = QCA.translate("Label", "保存间隔\n每次保存模型所间隔的步数。PS: 步数 ≈ 迭代轮次 * 训练样本数 / 批处理量")
            )
        )
        self.ui.SpinBox_Train_VITS_EvalInterval.setRange(300, 3000000)
        self.ui.SpinBox_Train_VITS_EvalInterval.setSingleStep(1)
        self.ui.SpinBox_Train_VITS_EvalInterval.setValue(
            int(Config_Train.GetValue('VITS', 'Eval_Interval', '1000'))
        )
        self.ui.SpinBox_Train_VITS_EvalInterval.valueChanged.connect(
            lambda Value: Config_Train.EditConfig('VITS', 'Eval_Interval', str(Value))
        )
        self.ui.SpinBox_Train_VITS_EvalInterval.setToolTip("提示：设置过小可能导致磁盘占用激增哦")
        self.ui.Button_Train_VITS_EvalInterval_Undo.clicked.connect(
            lambda: self.ui.SpinBox_Train_VITS_EvalInterval.setValue(1000)
        )

        Function_SetText(
            Widget = self.ui.Label_Train_VITS_OutputDir,
            Text = SetRichText(
                Body = QCA.translate("Label", "输出目录\n训练所得模型与对应配置文件的存放目录，若目录中已存在模型则会将其视为检查点。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Train_VITS_OutputDir,
            Text = str(Config_Train.GetValue('VITS', 'Output_Dir', NormPath(Path(ModelsDir).joinpath('TTS', 'VITS', str(datetime.today())), 'Posix'))),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Train_VITS_OutputDir.textChanged.connect(
            lambda Value: Config_Train.EditConfig('VITS', 'Output_Dir', str(Value))
        )
        self.ui.Label_Train_VITS_OutputDir.setToolTip("提示：当目录中存在多个模型时，编号最大的那个会被选为检查点。")
        Function_SetFileDialog(
            Button = self.ui.Button_Train_VITS_OutputDir,
            LineEdit = self.ui.LineEdit_Train_VITS_OutputDir,
            Mode = "SelectDir",
            Directory = NormPath(Path(ModelsDir).joinpath('TTS', 'VITS'), 'Posix')
        )
        self.ui.Button_Train_VITS_OutputDir_Undo.clicked.connect(
            lambda: self.ui.LineEdit_Train_VITS_OutputDir.setText(NormPath(Path(ModelsDir).joinpath('TTS', 'VITS', str(datetime.today())), 'Posix'))
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_Train_VITS,
            RootItemTexts = [
                self.ui.GroupBox_Train_VITS_InputParams.title(),
                self.ui.GroupBox_Train_VITS_VITSParams.title(),
                self.ui.GroupBox_Train_VITS_OutputParams.title()
            ],
            ChildItemTexts = [
                ("基础设置"),
                ("基础设置","高级设置"),
                ("基础设置")
            ],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Train_VITS.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_Train_VITS_InputParams,
            ScrollArea = self.ui.ScrollArea_Middle_Train_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Train_VITS.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_Train_VITS_InputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_Train_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Train_VITS.topLevelItem(1),
            TargetWidget = self.ui.GroupBox_Train_VITS_VITSParams,
            ScrollArea = self.ui.ScrollArea_Middle_Train_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Train_VITS.topLevelItem(1).child(0),
            TargetWidget = self.ui.Frame_Train_VITS_VITSParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_Train_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Train_VITS.topLevelItem(1).child(1),
            TargetWidget = self.ui.Frame_Train_VITS_VITSParams_AdvanceSettings,
            ScrollArea = self.ui.ScrollArea_Middle_Train_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Train_VITS.topLevelItem(2),
            TargetWidget = self.ui.GroupBox_Train_VITS_OutputParams,
            ScrollArea = self.ui.ScrollArea_Middle_Train_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Train_VITS.topLevelItem(2).child(0),
            TargetWidget = self.ui.Frame_Train_VITS_OutputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_Train_VITS
        )

        # Right
        MonitorFile_Config_VoiceTrainer = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_Train')
        )
        MonitorFile_Config_VoiceTrainer.start()
        MonitorFile_Config_VoiceTrainer.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Train_VITS.setText(
                FileContent
            )
        )

        self.ui.Button_RunTensorboard_Train_VITS.setText("启动Tensorboard")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_RunTensorboard_Train_VITS,
            Method = Tensorboard_Runner.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Train_VITS_OutputDir
            ]
        )

        self.ui.Button_SyncParams_Train_VITS.setText(QCA.translate("Button", "关联参数设置"))
        Function_ParamsSynchronizer(
            Trigger = self.ui.Button_SyncParams_Train_VITS,
            ParamsFrom = [
                self.ui.LineEdit_DAT_VITS_FileListPathTraining,
                self.ui.LineEdit_DAT_VITS_FileListPathValidation
            ],
            ParamsTo = [
                self.ui.LineEdit_Train_VITS_FileListPathTraining,
                self.ui.LineEdit_Train_VITS_FileListPathValidation
            ]
        )

        self.ui.Button_CheckOutput_Train_VITS.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Train_VITS,
            URL = self.ui.LineEdit_Train_VITS_OutputDir,
            ButtonTooltip = "Click to open"
        )

        # Bottom
        self.ui.Button_Train_VITS_Execute.setToolTip("执行语音模型训练")
        self.ui.Button_Train_VITS_Terminate.setToolTip("终止语音模型训练")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Train_VITS_Execute,
            TerminateButton = self.ui.Button_Train_VITS_Terminate,
            ProgressBar = self.ui.ProgressBar_Train_VITS,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Voice_Training.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Train_VITS_FileListPathTraining,
                self.ui.LineEdit_Train_VITS_FileListPathValidation,
                self.ui.SpinBox_Train_VITS_EvalInterval,
                self.ui.SpinBox_Train_VITS_Epochs,
                self.ui.SpinBox_Train_VITS_BatchSize,
                self.ui.CheckBox_Train_VITS_FP16Run,
                self.ui.CheckBox_Train_VITS_KeepOriginalSpeakers,
                self.ui.SpinBox_Train_VITS_NumWorkers,
                self.ui.CheckBox_Train_VITS_UsePretrainedModels,
                self.ui.LineEdit_Train_VITS_ModelPathPretrainedG,
                self.ui.LineEdit_Train_VITS_ModelPathPretrainedD,
                self.ui.LineEdit_Train_VITS_OutputDir
            ],
            EmptyAllowed = [
                self.ui.LineEdit_Train_VITS_ModelPathPretrainedG,
                self.ui.LineEdit_Train_VITS_ModelPathPretrainedD
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (
                    QMessageBox.Question, "Ask",
                    "当前任务已执行结束，是否跳转至下一工具界面？",
                    QMessageBox.Yes|QMessageBox.No, [QMessageBox.Yes],
                    [[self.ui.Button_Menu_TTS.click]], [[()]]
                )
            ]
        )
        MainWindowSignals.Signal_TaskStatus.connect(
            lambda Task, Status: Function_ShowMessageBox(
                MessageType = QMessageBox.Question,
                WindowTitle = "Ask",
                Text = "是否稍后启用tensorboard？",
                Buttons = QMessageBox.Yes|QMessageBox.No,
                EventButtons = [QMessageBox.Yes],
                EventLists = [[self.ui.Button_RunTensorboard_Train_VITS.click]],
                ParamLists = [[()]]
            ) if Task == 'Execute_Voice_Training.Execute' and Status == 'Started' else None
        )

        #############################################################
        ######################## Content: TTS #######################
        #############################################################

        # Guidance
        DialogBox_TTS = MessageBox_Stacked()
        DialogBox_TTS.setWindowTitle('Guidance（该引导仅出现一次）')
        DialogBox_TTS.SetContent(
            [
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_TTS.png')),
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance_Layout.png'))
            ],
            [
                '欢迎来到文字转语音工具界面\n将文字转为语音并生成音频文件，用户需要提供相应的模型和配置文件',
                '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
            ]
        )
        self.ui.Button_Menu_TTS.clicked.connect(
            lambda: DialogBox_TTS.exec() if eval(Config.GetValue('Dialog', 'GuidanceShown_TTS', 'False')) is False else None,
            type = Qt.QueuedConnection
        )
        self.ui.Button_Menu_TTS.clicked.connect(
            lambda: Config.EditConfig('Dialog', 'GuidanceShown_TTS', 'True'),
            type = Qt.QueuedConnection
        )

        # Config
        Path_Config_TTS = NormPath(Path(ConfigDir).joinpath('Config_TTS.ini'))
        Config_TTS = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_TTS',
                Path_Config_TTS
            )
        )

        # Top
        self.ui.ToolButton_VoiceConverter_Title.setText(QCA.translate("ToolButton", "VITS"))
        self.ui.ToolButton_VoiceConverter_Title.setChecked(True)
        self.ui.ToolButton_VoiceConverter_Title.setAutoExclusive(True)
        self.ui.ToolButton_VoiceConverter_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_TTS,
                TargetIndex = 0
            )
        )

        # Middle
        self.ui.GroupBox_TTS_VITS_InputParams.setTitle(QCA.translate("GroupBox", "输入参数"))

        Function_SetText(
            Widget = self.ui.Label_TTS_VITS_ConfigPathLoad,
            Text = SetRichText(
                Body = QCA.translate("Label", "配置加载路径\n用于推理的配置文件的所在路径。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_TTS_VITS_ConfigPathLoad,
            Text = str(Config_TTS.GetValue('VITS', 'Config_Path_Load', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_TTS_VITS_ConfigPathLoad.textChanged.connect(
            lambda Value: Config_TTS.EditConfig('VITS', 'Config_Path_Load', str(Value))
        )
        self.ui.LineEdit_TTS_VITS_ConfigPathLoad.textChanged.connect(
            lambda: self.ui.ComboBox_TTS_VITS_Speaker.clear(),
            type = Qt.QueuedConnection
        )
        self.ui.LineEdit_TTS_VITS_ConfigPathLoad.textChanged.connect(
            lambda Path: self.ui.ComboBox_TTS_VITS_Speaker.addItems(
                Get_Speakers(Path)
            ),
            type = Qt.QueuedConnection
        )
        Function_SetFileDialog(
            Button = self.ui.Button_TTS_VITS_ConfigPathLoad,
            LineEdit = self.ui.LineEdit_TTS_VITS_ConfigPathLoad,
            Mode = "SelectFile",
            FileType = "json类型 (*.json)"
        )
        self.ui.Button_TTS_VITS_ConfigPathLoad_Undo.clicked.connect(
            lambda: self.ui.LineEdit_TTS_VITS_ConfigPathLoad.setText('')
        )

        Function_SetText(
            Widget = self.ui.Label_TTS_VITS_ModelPathLoad,
            Text = SetRichText(
                Body = QCA.translate("Label", "G模型加载路径\n用于推理的生成器（Generator）模型的所在路径。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_TTS_VITS_ModelPathLoad,
            Text = str(Config_TTS.GetValue('VITS', 'Model_Path_Load', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_TTS_VITS_ModelPathLoad.textChanged.connect(
            lambda Value: Config_TTS.EditConfig('VITS', 'Model_Path_Load', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_TTS_VITS_ModelPathLoad,
            LineEdit = self.ui.LineEdit_TTS_VITS_ModelPathLoad,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)"
        )
        self.ui.Button_TTS_VITS_ModelPathLoad_Undo.clicked.connect(
            lambda: self.ui.LineEdit_TTS_VITS_ModelPathLoad.setText('')
        )

        self.ui.GroupBox_TTS_VITS_VITSParams.setTitle(QCA.translate("GroupBox", "文字转语音参数"))

        Function_SetText(
            Widget = self.ui.Label_TTS_VITS_Text,
            Text = SetRichText(
                Body = QCA.translate("Label", "输入文字\n输入的文字会作为说话人的语音内容。")
            )
        )
        Function_SetText(
            Widget = self.ui.PlainTextEdit_TTS_VITS_Text,
            Text = str(Config_TTS.GetValue('VITS', 'Text', '')),
            SetPlaceholderText = True,
            PlaceholderText = '请输入语句'
        )
        self.ui.PlainTextEdit_TTS_VITS_Text.textChanged.connect(
            lambda: Config_TTS.EditConfig('VITS', 'Text', self.ui.PlainTextEdit_TTS_VITS_Text.toPlainText())
        )

        Function_SetText(
            Widget = self.ui.Label_TTS_VITS_Language,
            Text = SetRichText(
                Body = QCA.translate("Label", "所用语言\n说话人/文字所使用的语言。")
            )
        )
        self.ui.ComboBox_TTS_VITS_Language.addItems(['中', '英', '日'])
        self.ui.ComboBox_TTS_VITS_Language.setCurrentText(
            str(Config_TTS.GetValue('VITS', 'Language', '中'))
        )
        self.ui.ComboBox_TTS_VITS_Language.currentTextChanged.connect(
            lambda Value: Config_TTS.EditConfig('VITS', 'Language', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_TTS_VITS_Speaker,
            Text = SetRichText(
                Body = QCA.translate("Label", "人物名字\n说话人物的名字。")
            )
        )
        self.ui.ComboBox_TTS_VITS_Speaker.addItems(
            Get_Speakers(str(Config_TTS.GetValue('VITS', 'Config_Path_Load', 'None')))
        )
        self.ui.ComboBox_TTS_VITS_Speaker.setCurrentText(
            str(Config_TTS.GetValue('VITS', 'Speaker', '')) if str(Config_TTS.GetValue('VITS', 'Speaker', '')) in Get_Speakers(str(Config_TTS.GetValue('VITS', 'Config_Path_Load', 'None')))
            else (Get_Speakers(str(Config_TTS.GetValue('VITS', 'Config_Path_Load', 'None')))[0] if Get_Speakers(str(Config_TTS.GetValue('VITS', 'Config_Path_Load', 'None'))) != '' else '')
        )
        self.ui.ComboBox_TTS_VITS_Speaker.currentTextChanged.connect(
            lambda Value: Config_TTS.EditConfig('VITS', 'Speaker', str(Value))
        )

        self.ui.CheckBox_TTS_VITS_VITSParams_Toggle_AdvanceSettings.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_TTS_VITS_VITSParams_Toggle_AdvanceSettings,
            CheckedText = "高级设置",
            CheckedEventList = [
                Function_AnimateFrame
            ],
            CheckedArgsList = [
                (
                    self.ui.Frame_TTS_VITS_VITSParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_TTS_VITS_VITSParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Extend'
                )
            ],
            UncheckedText = "高级设置",
            UncheckedEventList = [
                Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (
                    self.ui.Frame_TTS_VITS_VITSParams_AdvanceSettings,
                    None, None,
                    0, self.ui.Frame_TTS_VITS_VITSParams_AdvanceSettings.sizeHint().height(),
                    210,
                    'Reduce'
                )
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_TTS_VITS_EmotionStrength,
            Text = SetRichText(
                Body = QCA.translate("Label", "情感强度\n情感的变化程度。")
            )
        )
        self.ui.HorizontalSlider_TTS_VITS_EmotionStrength.setMinimum(0)
        self.ui.HorizontalSlider_TTS_VITS_EmotionStrength.setMaximum(100)
        self.ui.HorizontalSlider_TTS_VITS_EmotionStrength.setTickInterval(1)
        self.ui.HorizontalSlider_TTS_VITS_EmotionStrength.setValue(
            int(float(Config_TTS.GetValue('VITS', 'EmotionStrength', '0.67')) * 100)
        )
        self.ui.HorizontalSlider_TTS_VITS_EmotionStrength.valueChanged.connect(
            lambda Value: Config_TTS.EditConfig('VITS', 'EmotionStrength', str(Value * 0.01))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.HorizontalSlider_TTS_VITS_EmotionStrength,
            ParamsFrom = [
                self.ui.HorizontalSlider_TTS_VITS_EmotionStrength
            ],
            Times = 0.01,
            ParamsTo = [
                self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength
            ]
        )
        self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength.setRange(0, 1)
        self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength.setSingleStep(0.01)
        self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength.setValue(
            float(Config_TTS.GetValue('VITS', 'EmotionStrength', '0.67'))
        )
        self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength.valueChanged.connect(
            lambda Value: Config_TTS.EditConfig('VITS', 'EmotionStrength', str(Value))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength,
            ParamsFrom = [
                self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength
            ],
            Times = 100,
            ParamsTo = [
                self.ui.HorizontalSlider_TTS_VITS_EmotionStrength
            ]
        )
        self.ui.Button_TTS_VITS_EmotionStrength_Undo.clicked.connect(
            lambda: self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength.setValue(0.67)
        )

        Function_SetText(
            Widget = self.ui.Label_TTS_VITS_PhonemeDuration,
            Text = SetRichText(
                Body = QCA.translate("Label", "音素音长\n音素的发音长度。")
            )
        )
        self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration.setMinimum(0)
        self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration.setMaximum(10)
        self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration.setTickInterval(1)
        self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration.setValue(
            int(float(Config_TTS.GetValue('VITS', 'PhonemeDuration', '0.8')) * 10)
        )
        self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration.valueChanged.connect(
            lambda Value: Config_TTS.EditConfig('VITS', 'PhonemeDuration', str(Value * 0.1))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration,
            ParamsFrom = [
                self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration
            ],
            Times = 0.1,
            ParamsTo = [
                self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration
            ]
        )
        self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration.setRange(0, 1)
        self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration.setSingleStep(0.1)
        self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration.setValue(
            float(Config_TTS.GetValue('VITS', 'PhonemeDuration', '0.8'))
        )
        self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration.valueChanged.connect(
            lambda Value: Config_TTS.EditConfig('VITS', 'PhonemeDuration', str(Value))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration,
            ParamsFrom = [
                self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration
            ],
            Times = 10,
            ParamsTo = [
                self.ui.HorizontalSlider_TTS_VITS_PhonemeDuration
            ]
        )
        self.ui.Button_TTS_VITS_PhonemeDuration_Undo.clicked.connect(
            lambda: self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration.setValue(0.8)
        )

        Function_SetText(
            Widget = self.ui.Label_TTS_VITS_SpeechRate,
            Text = SetRichText(
                Body = QCA.translate("Label", "整体语速\n整体的说话速度。")
            )
        )
        self.ui.HorizontalSlider_TTS_VITS_SpeechRate.setMinimum(0)
        self.ui.HorizontalSlider_TTS_VITS_SpeechRate.setMaximum(20)
        self.ui.HorizontalSlider_TTS_VITS_SpeechRate.setTickInterval(1)
        self.ui.HorizontalSlider_TTS_VITS_SpeechRate.setValue(
            int(float(Config_TTS.GetValue('VITS', 'SpeechRate', '1.')) * 10)
        )
        self.ui.HorizontalSlider_TTS_VITS_SpeechRate.valueChanged.connect(
            lambda Value: Config_TTS.EditConfig('VITS', 'SpeechRate', str(Value * 0.1))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.HorizontalSlider_TTS_VITS_SpeechRate,
            ParamsFrom = [
                self.ui.HorizontalSlider_TTS_VITS_SpeechRate
            ],
            Times = 0.1,
            ParamsTo = [
                self.ui.DoubleSpinBox_TTS_VITS_SpeechRate
            ]
        )
        self.ui.DoubleSpinBox_TTS_VITS_SpeechRate.setRange(0, 2)
        self.ui.DoubleSpinBox_TTS_VITS_SpeechRate.setSingleStep(0.1)
        self.ui.DoubleSpinBox_TTS_VITS_SpeechRate.setValue(
            float(Config_TTS.GetValue('VITS', 'SpeechRate', '1.'))
        )
        self.ui.DoubleSpinBox_TTS_VITS_SpeechRate.valueChanged.connect(
            lambda Value: Config_TTS.EditConfig('VITS', 'SpeechRate', str(Value))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.DoubleSpinBox_TTS_VITS_SpeechRate,
            ParamsFrom = [
                self.ui.DoubleSpinBox_TTS_VITS_SpeechRate
            ],
            Times = 10,
            ParamsTo = [
                self.ui.HorizontalSlider_TTS_VITS_SpeechRate
            ]
        )
        self.ui.Button_TTS_VITS_SpeechRate_Undo.clicked.connect(
            lambda: self.ui.DoubleSpinBox_TTS_VITS_SpeechRate.setValue(1.)
        )

        self.ui.GroupBox_TTS_VITS_OutputParams.setTitle(QCA.translate("GroupBox", "输出参数"))

        Function_SetText(
            Widget = self.ui.Label_TTS_VITS_AudioDirSave,
            Text = SetRichText(
                Body = QCA.translate("Label", "音频保存目录\n用于保存推理得到的音频的目录。")
            )
        )
        Function_SetText(
            Widget = self.ui.LineEdit_TTS_VITS_AudioDirSave,
            Text = str(Config_TTS.GetValue('VITS', 'Audio_Dir_Save', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_TTS_VITS_AudioDirSave.textChanged.connect(
            lambda Value: Config_TTS.EditConfig('VITS', 'Audio_Dir_Save', str(Value))
        )
        Function_SetFileDialog(
            Button = self.ui.Button_TTS_VITS_AudioDirSave,
            LineEdit = self.ui.LineEdit_TTS_VITS_AudioDirSave,
            Mode = "SelectDir"
        )
        self.ui.Button_TTS_VITS_ModelPathLoad_Undo.clicked.connect(
            lambda: self.ui.LineEdit_TTS_VITS_ModelPathLoad.setText('')
        )

        # Right
        MonitorFile_Config_VoiceConverter = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_TTS')
        )
        MonitorFile_Config_VoiceConverter.start()
        MonitorFile_Config_VoiceConverter.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_TTS_VITS.setText(
                FileContent
            )
        )

        self.ui.Button_CheckOutput_TTS_VITS.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_TTS_VITS,
            URL = self.ui.LineEdit_TTS_VITS_AudioDirSave,
            ButtonTooltip = "Click to open"
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_TTS_VITS,
            RootItemTexts = [
                self.ui.GroupBox_TTS_VITS_InputParams.title(),
                self.ui.GroupBox_TTS_VITS_VITSParams.title(),
                self.ui.GroupBox_TTS_VITS_OutputParams.title()
            ],
            ChildItemTexts = [
                ("基础设置"),
                ("基础设置","高级设置"),
                ("基础设置")
            ],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_TTS_VITS.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_TTS_VITS_InputParams,
            ScrollArea = self.ui.ScrollArea_Middle_TTS_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_TTS_VITS.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_TTS_VITS_InputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_TTS_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_TTS_VITS.topLevelItem(1),
            TargetWidget = self.ui.GroupBox_TTS_VITS_VITSParams,
            ScrollArea = self.ui.ScrollArea_Middle_TTS_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_TTS_VITS.topLevelItem(1).child(0),
            TargetWidget = self.ui.Frame_TTS_VITS_VITSParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_TTS_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_TTS_VITS.topLevelItem(1).child(1),
            TargetWidget = self.ui.Frame_TTS_VITS_VITSParams_AdvanceSettings,
            ScrollArea = self.ui.ScrollArea_Middle_TTS_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_TTS_VITS.topLevelItem(1),
            TargetWidget = self.ui.GroupBox_TTS_VITS_OutputParams,
            ScrollArea = self.ui.ScrollArea_Middle_TTS_VITS
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_TTS_VITS.topLevelItem(1).child(0),
            TargetWidget = self.ui.Frame_TTS_VITS_OutputParams_BasicSettings,
            ScrollArea = self.ui.ScrollArea_Middle_TTS_VITS
        )

        # Bottom
        self.ui.Button_TTS_VITS_Execute.setToolTip("执行语音模型推理")
        self.ui.Button_TTS_VITS_Terminate.setToolTip("终止语音模型推理")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_TTS_VITS_Execute,
            TerminateButton = self.ui.Button_TTS_VITS_Terminate,
            ProgressBar = self.ui.ProgressBar_TTS_VITS,
            ConsoleWidget = self.ui.Frame_Console,
            Method = Execute_Voice_Converting.Execute,
            ParamsFrom = [
                self.ui.LineEdit_TTS_VITS_ConfigPathLoad,
                self.ui.LineEdit_TTS_VITS_ModelPathLoad,
                self.ui.PlainTextEdit_TTS_VITS_Text,
                self.ui.ComboBox_TTS_VITS_Language,
                self.ui.ComboBox_TTS_VITS_Speaker,
                self.ui.DoubleSpinBox_TTS_VITS_EmotionStrength,
                self.ui.DoubleSpinBox_TTS_VITS_PhonemeDuration,
                self.ui.DoubleSpinBox_TTS_VITS_SpeechRate,
                self.ui.LineEdit_TTS_VITS_AudioDirSave
            ],
            EmptyAllowed = [
                self.ui.ComboBox_TTS_VITS_Speaker
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束！",
                    QMessageBox.Ok
                )
            ]
        )

        #############################################################
        ##################### Content: Settings #####################
        #############################################################

        self.ui.ToolButton_Settings_Title.setText(QCA.translate("Label", "系统选项"))

        self.ui.Label_Setting_Language.setText(QCA.translate("Label", "语言"))
        self.ui.ComboBox_Setting_Language.addItems(['中文'])
        self.ui.ComboBox_Setting_Language.setCurrentText(
            {
                'Chinese': '中文'
            }.get(Config.GetValue('Settings', 'Language', 'Chinese'))
        )
        self.ui.ComboBox_Setting_Language.currentIndexChanged.connect(
            lambda: Config.EditConfig(
                'Settings',
                'Language',
                {
                    '中文': 'Chinese'
                }.get(self.ui.ComboBox_Setting_Language.currentText())
            )
        )

        self.ui.Button_Setting_ClientRebooter.clicked.connect(ClientRebooter)
        self.ui.Button_Setting_ClientRebooter.setText(QCA.translate("Button", "重启客户端"))
        self.ui.Button_Setting_ClientRebooter.setToolTip(QCA.translate("ToolTip", "重启EVT客户端"))

        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Setting_IntegrityChecker,
            Method = Integrity_Checker.Execute,
            Params = ()
        )
        MainWindowSignals.Signal_TaskStatus.connect(
            lambda Task, Status: self.ui.Button_Setting_IntegrityChecker.setCheckable(
                False if Status == 'Started' else True
            )
        )
        self.ui.Button_Setting_IntegrityChecker.setText(QCA.translate("Button", "检查完整性"))
        self.ui.Button_Setting_IntegrityChecker.setToolTip(QCA.translate("ToolTip", "检查文件完整性"))

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
            CheckedEventList = [
                Config.EditConfig,
                #Updater
            ],
            CheckedArgsList = [
                ('Settings', 'AutoUpdate', 'Enabled'),
                #(CurrentVersion, IsFileCompiled, CurrentDir, f'Easy Voice Toolkit {CurrentVersion}', CurrentDir)
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config.EditConfig
            ],
            UncheckedArgsList = [
                ('Settings', 'AutoUpdate', 'Disabled')
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
            CheckedEventList = [
                Config.EditConfig,
                Function_ParamsSynchronizer,
                Function_ParamsSynchronizer,
                Function_ParamsSynchronizer,
                Function_ParamsSynchronizer
            ],
            CheckedArgsList = [
                ('Tools', 'Synchronizer', 'Enabled'),
                (self.ui.LineEdit_Process_MediaDirOutput,[self.ui.LineEdit_Process_MediaDirOutput],None,[self.ui.LineEdit_ASR_VPR_AudioDirInput]),
                (self.ui.LineEdit_ASR_VPR_AudioSpeakersDataPath,[self.ui.LineEdit_ASR_VPR_AudioSpeakersDataPath],None,[self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath]),
                (self.ui.LineEdit_STT_Whisper_SRTDir,[self.ui.LineEdit_STT_Whisper_SRTDir],None,[self.ui.LineEdit_DAT_VITS_SRTDir]),
                ([self.ui.LineEdit_DAT_VITS_FileListPathTraining,self.ui.LineEdit_DAT_VITS_FileListPathValidation],[self.ui.LineEdit_DAT_VITS_FileListPathTraining,self.ui.LineEdit_DAT_VITS_FileListPathValidation],None,[self.ui.LineEdit_Train_VITS_FileListPathTraining,self.ui.LineEdit_Train_VITS_FileListPathValidation]),
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config.EditConfig,
                #Function_ParamsSynchronizer,
                #Function_ParamsSynchronizer,
                #Function_ParamsSynchronizer,
                #Function_ParamsSynchronizer
            ],
            UncheckedArgsList = [
                ('Tools', 'Synchronizer', 'Disabled'),
                #(self.ui.LineEdit_Process_MediaDirOutput,[self.ui.LineEdit_Process_MediaDirOutput],None,[self.ui.LineEdit_ASR_VPR_AudioDirInput],"Disconnect"),
                #(self.ui.LineEdit_ASR_VPR_AudioSpeakersDataPath,[self.ui.LineEdit_ASR_VPR_AudioSpeakersDataPath],None,[self.ui.LineEdit_DAT_VITS_AudioSpeakersDataPath],"Disconnect"),
                #(self.ui.LineEdit_STT_Whisper_SRTDir,[self.ui.LineEdit_STT_Whisper_SRTDir],None,[self.ui.LineEdit_DAT_VITS_SRTDir],"Disconnect"),
                #([self.ui.LineEdit_DAT_VITS_FileListPathTraining,self.ui.LineEdit_DAT_VITS_FileListPathValidation],[self.ui.LineEdit_DAT_VITS_FileListPathTraining,self.ui.LineEdit_DAT_VITS_FileListPathValidation],None,[self.ui.LineEdit_Train_VITS_FileListPathTraining,self.ui.LineEdit_Train_VITS_FileListPathValidation],"Disconnect")
            ],
            TakeEffect = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Setting_Synchronizer,
            UncheckedEventList = [
                Function_ShowMessageBox
            ],
            UncheckedArgsList = [
                (
                    QMessageBox.Information, "Tip",
                    "该设置将于重启之后生效"
                )
            ],
            TakeEffect = False
        )

        #############################################################
        ####################### Content: Info #######################
        #############################################################

        self.ui.ToolButton_Info_Title.setText(QCA.translate("Label", "用户须知"))

        Function_SetText(
            Widget = self.ui.TextBrowser_Text_Info,
            Text = SetRichText(
                Title = QCA.translate("TextBrowser", "声明"),
                TitleAlign = "left",
                TitleSize = 24,
                TitleWeight = 840,
                Body = QCA.translate("TextBrowser",
                    "请自行解决数据集的授权问题。对于使用未经授权的数据集进行训练所导致的任何问题，您将承担全部责任，并且该仓库及其维护者不承担任何后果！\n"
                    "\n"
                    "您还需要服从以下条例：\n"
                    "0. 本项目仅用于学术交流目的，旨在促进沟通和学习。不适用于生产环境。\n"
                    "1. 基于 Easy Voice Toolkit 发布的任何视频必须在描述中明确指出它们用于变声，并指定声音或音频的输入源，例如使用他人发布的视频或音频，并将分离出的人声作为转换的输入源，必须提供清晰的原始视频链接。如果您使用自己的声音或其他商业语音合成软件生成的声音作为转换的输入源，也必须在描述中说明。\n"
                    "2. 您将对输入源引起的任何侵权问题负全部责任。当使用其他商业语音合成软件作为输入源时，请确保遵守该软件的使用条款。请注意，许多语音合成引擎在其使用条款中明确声明不能用于输入源转换。\n"
                    "3. 继续使用本项目被视为同意本仓库 README 中所述的相关条款。本仓库的 README 有义务进行劝导，但不承担可能出现的任何后续问题的责任。\n"
                    "4. 如果您分发此仓库的代码或将由此项目生成的任何结果公开发布（包括但不限于视频分享平台），请注明原始作者和代码来源（即此仓库）。\n"
                    "5. 如果您将此项目用于任何其他计划，请提前与本仓库的作者联系并告知。\n"
                ),
                BodyAlign = "left",
                BodySize = 12,
                BodyWeight = 420,
                BodyLineHeight = 27
            )
        )

        #############################################################
        ######################### StatusBar #########################
        #############################################################

        # Toggle Console
        self.ui.Button_Toggle_Console.setChecked(False)
        self.ui.Button_Toggle_Console.setAutoExclusive(False)
        self.ui.Button_Toggle_Console.setToolTip("Click to toggle console")
        self.ui.Button_Toggle_Console.clicked.connect(
            lambda: Function_AnimateFrame(
                Frame = self.ui.Frame_Console,
                MinHeight = 0,
                MaxHeight = 210
            )
        )

        # Print ConsoleInfo
        self.ConsoleInfo.Signal_ConsoleInfo.connect(
            lambda Info: self.ui.PlainTextEdit_Console.setPlainText(Info)
        )

        # Display ToolsStatus
        self.ui.Label_ToolsStatus.clear()
        MainWindowSignals.Signal_TaskStatus.connect(
            lambda Task, Status: self.ui.Label_ToolsStatus.setText(
                f"工具状态：{'忙碌' if Status == 'Started' else '空闲'}"
            ) if Task in [
                'Execute_Audio_Processing.Execute',
                'Execute_Voice_Identifying.Execute',
                'Execute_Voice_Transcribing.Execute',
                'Execute_Dataset_Creating.Execute',
                'Execute_Voice_Training.Execute',
                'Execute_Voice_Converting.Execute'
            ] else None
        )

        # Display Usage
        self.MonitorUsage.Signal_UsageInfo.connect(
            lambda Usage_CPU, Usage_GPU: self.ui.Label_Usage_CPU.setText(
                f"CPU: {Usage_CPU}"
            )
        )
        self.MonitorUsage.Signal_UsageInfo.connect(
            lambda Usage_CPU, Usage_GPU: self.ui.Label_Usage_GPU.setText(
                f"GPU: {Usage_GPU}"
            )
        )

        # Display Version
        self.ui.Label_Version.setText(CurrentVersion)

        # Show MainWindow (and emit signal)
        self.show()
        MainWindowSignals.Signal_MainWindowShown.emit()

##############################################################################################################################

if __name__ == "__main__":
    UpdaterExecuter()

    App = QApplication(sys.argv)

    Window = MainWindow()
    Window.Main()
    
    sys.exit(App.exec())

##############################################################################################################################