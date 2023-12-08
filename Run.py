import os
import sys
import time #import asyncio
import json
from pathlib import Path
from PySide6 import __file__ as PySide6_File
from PySide6.QtCore import Qt, QObject, Signal, Slot, QThread, QPropertyAnimation, QParallelAnimationGroup
from PySide6.QtCore import QCoreApplication as QCA
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import *

from EVT_GUI.QSimpleWidgets.Utils import *
from EVT_GUI.QSimpleWidgets.QTasks import *
from EVT_GUI.Window import Window_Customizing
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


# Set up environment variables while python file is not compiled
if IsFileCompiled == False:
    SetEnvVar( # Redirect PATH variable 'QT_QPA_PLATFORM_PLUGIN_PATH' to Pyside6 '/plugins/platforms' folder's path
        Variable = 'QT_QPA_PLATFORM_PLUGIN_PATH',
        Value = NormPath(Path(GetBaseDir(PySide6_File)).joinpath('plugins', 'platforms'))
    )
# Set up environment variables while environment is configured
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


# Set up config
ConfigPath = NormPath(Path(CurrentDir).joinpath('Config', 'Config.ini'))
Config = ManageConfig(ConfigPath)
Config.EditConfig('Info', 'CurrentVersion', str(CurrentVersion))
Config.EditConfig('Info', 'ExecuterName', str(FileName))

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

# ClientFunc1
def ClientRebooter():
    '''
    Reboot EVT client
    '''
    UpdaterExecuter() #os.execl(sys.executable, 'python', __file__, *sys.argv[1:]) else os.execl(sys.executable, sys.executable, *sys.argv)


# ClientFunc2
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
            #Config.GetValue('Env', 'GCC'),
            #Config.GetValue('Env', 'CMake'),
            Config.GetValue('Env', 'Python'),
            Config.GetValue('Env', 'PyReqs'),
            Config.GetValue('Env', 'Pytorch')
        ]:
            Error = RunCMD(
                Args = [
                    f'cd "{ResourceDir}"',
                    'python -c "'
                    'from EVT_Core.Tool_AudioProcessor.Process import Audio_Processing; '
                    'from EVT_Core.Tool_VoiceIdentifier.Identify import Voice_Identifying; '
                    'from EVT_Core.Tool_VoiceTranscriber.Transcribe import Voice_Transcribing; '
                    'from EVT_Core.Tool_DatasetCreator.Create import Dataset_Creating; '
                    'from EVT_Core.Tool_VoiceTrainer.Train import Voice_Training; '
                    'from EVT_Core.Tool_VoiceConverter.Convert import Voice_Converting"'
                ],
                CommunicateThroughConsole = True,
                DecodeResult = True
            )[1]

        else:
            Error = 'Missing evironment dependencies!'

        self.finished.emit(str(Error))


# ClientFunc3
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
            while GetPath(LogDir, 'events.out.tfevents') == False:
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

# Tool1: AudioProcessor
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
                'from EVT_Core.Tool_AudioProcessor.Process import Audio_Processing; '
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


# Tool2: VoiceIdentifier
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
                'from EVT_Core.Tool_VoiceIdentifier.Identify import Voice_Identifying; '
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


# Tool3: VoiceTranscriber
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
                'from EVT_Core.Tool_VoiceTranscriber.Transcribe import Voice_Transcribing; '
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


# Tool4: DatasetCreator
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
                'from EVT_Core.Tool_DatasetCreator.Create import Dataset_Creating; '
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


# Tool5: VoiceTrainer
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
                'from EVT_Core.Tool_VoiceTrainer.Train import Voice_Training; '
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


# Tool6: VoiceConverter
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
                'from EVT_Core.Tool_VoiceConverter.Convert import Voice_Converting; '
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

##############################################################################################################################

# Where to store custom signals
class CustomSignals_MainWindow(QObject):
    '''
    Set up signals for MainWindow
    '''
    Signal_MainWindowShown = Signal()

    # Monitor frame
    Signal_FrameStatus = Signal(str)

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

    def __init__(self):
        super().__init__()

        self.ConsoleInfo = ConsolOutputHandler()
        self.ConsoleInfo.start()

        self.MonitorUsage = MonitorUsage()
        self.MonitorUsage.start()

    def Function_AnimateStackedWidget(self,
        StackedWidget: QStackedWidget,
        TargetIndex: int = 0,
        Duration: int = 0
    ):
        '''
        Function to animate stackedwidget
        '''
        Widget_Original = StackedWidget.currentWidget()
        Geometry_Original = Widget_Original.geometry()

        self.WidgetAnimation = QPropertyAnimation(Widget_Original, b"geometry")

        def AnimateStackedWidget(Index_Altered):
            self.WidgetAnimation = Function_SetAnimation(self.WidgetAnimation, Geometry_Original, Geometry_Original.setY(0), Duration)
            self.WidgetAnimation.finished.connect(
                lambda: StackedWidget.setCurrentIndex(Index_Altered),
                type = Qt.QueuedConnection
            )
            self.WidgetAnimation.finished.connect(
                lambda: Widget_Original.setGeometry(Geometry_Original),
                type = Qt.QueuedConnection
            )
            self.WidgetAnimation.start()

        AnimateStackedWidget(TargetIndex)

    def Function_AnimateFrame(self,
        Frame: QWidget,
        MinWidth: int = ...,
        MaxWidth: int = ...,
        MinHeight: int = ...,
        MaxHeight: int = ...,
        Duration: int = 210,
        Mode: str = "Toggle"
    ):
        '''
        Function to animate frame
        '''
        Width_Current = Frame.width()
        Height_Current = Frame.height()

        self.FrameAnimationMinWidth = QPropertyAnimation(Frame, b"minimumWidth")
        self.FrameAnimationMaxWidth = QPropertyAnimation(Frame, b"maximumWidth")
        self.FrameAnimationMinHeight = QPropertyAnimation(Frame, b"minimumHeight")
        self.FrameAnimationMaxHeight = QPropertyAnimation(Frame, b"maximumHeight")

        self.AnimationGroup = QParallelAnimationGroup()

        def AnimateFrameWidth(Width_Altered):
            self.AnimationGroup.addAnimation(Function_SetAnimation(self.FrameAnimationMinWidth, Width_Current, Width_Altered, Duration))
            self.AnimationGroup.addAnimation(Function_SetAnimation(self.FrameAnimationMaxWidth, Width_Current, Width_Altered, Duration))
            self.AnimationGroup.start()

        def AnimateFrameHeight(Height_Altered):
            self.AnimationGroup.addAnimation(Function_SetAnimation(self.FrameAnimationMinHeight, Height_Current, Height_Altered, Duration))
            self.AnimationGroup.addAnimation(Function_SetAnimation(self.FrameAnimationMaxHeight, Height_Current, Height_Altered, Duration))
            self.AnimationGroup.start()

        if Mode == "Extend":
            if MaxWidth != ...:
                AnimateFrameWidth(MaxWidth)
            if MaxHeight != ...:
                AnimateFrameHeight(MaxHeight)
            MainWindowSignals.Signal_FrameStatus.emit(f"{Frame.objectName()}Extended")
        if Mode == "Reduce":
            if MinWidth != ...:
                AnimateFrameWidth(MinWidth)
            if MinHeight != ...:
                AnimateFrameHeight(MinHeight)
            MainWindowSignals.Signal_FrameStatus.emit(f"{Frame.objectName()}Reduced")
        if Mode == "Toggle":
            if Width_Current == MinWidth or Height_Current == MinHeight:
                if MaxWidth != ...:
                    AnimateFrameWidth(MaxWidth)
                if MaxHeight != ...:
                    AnimateFrameHeight(MaxHeight)
                MainWindowSignals.Signal_FrameStatus.emit(f"{Frame.objectName()}Extended")
            else:
                if MinWidth != ...:
                    AnimateFrameWidth(MinWidth)
                if MinHeight != ...:
                    AnimateFrameHeight(MinHeight)
                MainWindowSignals.Signal_FrameStatus.emit(f"{Frame.objectName()}Reduced")

    @Slot(str)
    def Function_PrintText(self,
        Panel: QObject,
        Frame: Optional[QFrame] = None,
        FrameStatus: str = ...,
        Text: str = ...,
        ShowCursor: Optional[bool] = None
    ):
        '''
        Function to print text on panel while its parent frame is extended
        '''
        if isinstance(Panel, (QLabel, QComboBox, QCheckBox, QTextBrowser)):
            Panel.setText(Text)
        if isinstance(Panel, (QLineEdit, QTextEdit, QPlainTextEdit)):
            TextCursor = Panel.textCursor()
            TextCursor.movePosition(QTextCursor.End)
            TextCursor.insertText(Text)
            Panel.setTextCursor(TextCursor)
            Panel.ensureCursorVisible() if ShowCursor else None

        Frame = Function_FindParentUI(
            ChildUI = Panel,
            ParentType = QFrame
        ) if Frame == None else Frame

        if FrameStatus == f"{Frame.objectName()}Extended":
            Panel.setVisible(True)
        if FrameStatus == f"{Frame.objectName()}Reduced":
            Panel.setVisible(False)

    def Function_SetMethodExecutor(self,
        ExecuteButton: QPushButton,
        TerminateButton: Optional[QPushButton] = None,
        ProgressBar: Optional[QProgressBar] = None,
        ConsoleFrame: Optional[QFrame] = None,
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

            WorkerThread.started.connect(lambda: self.Function_AnimateFrame(ConsoleFrame, MinHeight = 0, MaxHeight = 210, Mode = "Extend")) if ConsoleFrame else None
            WorkerThread.started.connect(lambda: Function_AnimateProgressBar(ProgressBar, IsTaskAlive = True)) if ProgressBar else None
            WorkerThread.started.connect(lambda: self.Function_AnimateStackedWidget(Function_FindParentUI(ExecuteButton, QStackedWidget), TargetIndex = 1)) if TerminateButton else None
            WorkerThread.finished.connect(lambda: self.Function_AnimateFrame(ConsoleFrame, MinHeight = 0, MaxHeight = 210, Mode = "Reduce")) if ConsoleFrame else None
            WorkerThread.finished.connect(lambda: Function_AnimateProgressBar(ProgressBar, IsTaskAlive = False)) if ProgressBar else None
            WorkerThread.finished.connect(lambda: self.Function_AnimateStackedWidget(Function_FindParentUI(ExecuteButton, QStackedWidget), TargetIndex = 0)) if TerminateButton else None
            #WorkerThread.finished.connect(lambda: MainWindowSignals.Signal_ExecuteTask.disconnect(getattr(ClassInstance, MethodName)))

            MainWindowSignals.Signal_ExecuteTask.emit(Args)

            WorkerThread.start()

        ExecuteButton.clicked.connect(ExecuteMethod)#if ExecuteButton else ExecuteMethod()
        ExecuteButton.setText("Execute 执行") if ExecuteButton != None and ExecuteButton.text() == "" else None

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
        ) if TerminateButton else None
        TerminateButton.setText("Terminate 终止") if TerminateButton != None and TerminateButton.text() == "" else None

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
            lambda: self.Function_AnimateFrame(
                Frame = self.ui.Frame_Menu,
                MinWidth = 48,
                MaxWidth = 210
            )
        )
        self.ui.Button_Toggle_Menu.setCheckable(True)
        self.ui.Button_Toggle_Menu.setChecked(False)
        self.ui.Button_Toggle_Menu.setAutoExclusive(False)
        self.ui.Button_Toggle_Menu.setToolTipDuration(-1)
        self.ui.Button_Toggle_Menu.setToolTip(QCA.translate("ToolTip", "点击以展开/折叠菜单"))

        #############################################################
        ############################ Menu ###########################
        #############################################################

        MainWindowSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: self.Function_PrintText(
                Panel = self.ui.Label_Menu_Home_Text,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Label", "主页")
            )
        )
        self.ui.Button_Menu_Home.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 0
            )
        )
        self.ui.Button_Menu_Home.setCheckable(True)
        self.ui.Button_Menu_Home.setChecked(True)
        self.ui.Button_Menu_Home.setAutoExclusive(True)
        self.ui.Button_Menu_Home.setToolTipDuration(-1)
        self.ui.Button_Menu_Home.setToolTip(QCA.translate("ToolTip", "主页"))

        MainWindowSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: self.Function_PrintText(
                Panel = self.ui.Label_Menu_Download_Text,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Label", "下载")
            )
        )
        self.ui.Button_Menu_Download.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 1
            )
        )
        self.ui.Button_Menu_Download.setCheckable(True)
        self.ui.Button_Menu_Download.setChecked(False)
        self.ui.Button_Menu_Download.setAutoExclusive(True)
        self.ui.Button_Menu_Download.setToolTipDuration(-1)
        self.ui.Button_Menu_Download.setToolTip(QCA.translate("ToolTip", "下载"))

        MainWindowSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: self.Function_PrintText(
                Panel = self.ui.Label_Menu_Tools_Text,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Label", "工具")
            )
        )
        self.ui.Button_Menu_Tools.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 2
            )
        )
        self.ui.Button_Menu_Tools.setCheckable(True)
        self.ui.Button_Menu_Tools.setChecked(False)
        self.ui.Button_Menu_Tools.setAutoExclusive(True)
        self.ui.Button_Menu_Tools.setToolTipDuration(-1)
        self.ui.Button_Menu_Tools.setToolTip(QCA.translate("ToolTip", "工具"))

        MainWindowSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: self.Function_PrintText(
                Panel = self.ui.Label_Menu_Settings_Text,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Label", "设置")
            )
        )
        self.ui.Button_Menu_Settings.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 3
            )
        )
        self.ui.Button_Menu_Settings.setCheckable(True)
        self.ui.Button_Menu_Settings.setChecked(False)
        self.ui.Button_Menu_Settings.setAutoExclusive(True)
        self.ui.Button_Menu_Settings.setToolTipDuration(-1)
        self.ui.Button_Menu_Settings.setToolTip(QCA.translate("ToolTip", "设置"))

        MainWindowSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: self.Function_PrintText(
                Panel = self.ui.Label_Menu_Info_Text,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Label", "关于")
            )
        )
        self.ui.Button_Menu_Info.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 4
            )
        )
        self.ui.Button_Menu_Info.setCheckable(True)
        self.ui.Button_Menu_Info.setChecked(False)
        self.ui.Button_Menu_Info.setAutoExclusive(True)
        self.ui.Button_Menu_Info.setToolTipDuration(-1)
        self.ui.Button_Menu_Info.setToolTip(QCA.translate("ToolTip", "关于"))

        #########################################################
        ##################### Content: Home #####################
        #########################################################

        #self.ui.ToolButton_Home_Title.setText(QCA.translate("Label", "主页"))

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
        ##################### Content: Download #####################
        #############################################################

        self.ui.ToolButton_Download_Title.setText(QCA.translate("Label", "环境依赖"))

        self.ui.Label_Download_FFmpeg.setText("FFmpeg")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Install_FFmpeg,
            ProgressBar = self.ui.ProgressBar_Download_FFmpeg,
            Method = FFmpeg_Installer.Execute,
            Params = ()
        )
        MainWindowSignals.Signal_MainWindowShown.connect(
            self.ui.Button_Install_FFmpeg.click #if Config.GetValue('Env', 'FFmpeg', 'Undetected') == 'Undetected' else EnvConfiguratorSignals.Signal_FFmpegDetected.emit
        )
        self.ui.Button_Install_FFmpeg.setText('')
        self.ui.Button_Install_FFmpeg.setCheckable(True)
        self.ui.Button_Install_FFmpeg.setToolTipDuration(-1)
        self.ui.Button_Install_FFmpeg.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_FFmpegUndetected.connect(
            lambda: Config.EditConfig('Env', 'FFmpeg', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_FFmpegUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到FFmpeg，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_FFmpegInstalled.connect(#self.ui.Button_Install_FFmpeg.click)
            lambda: EnvConfiguratorSignals.Signal_FFmpegDetected.emit()
        )
        EnvConfiguratorSignals.Signal_FFmpegInstallFailed.connect(
            lambda: Function_ShowMessageBox(
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
            lambda: self.ui.ProgressBar_Download_FFmpeg.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_FFmpegStatus.connect(
            lambda Status: self.ui.Label_Download_FFmpeg_Status.setText(Status)
        )

        '''
        self.ui.Label_Download_GCC.setText("GCC")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Install_GCC,
            ProgressBar = self.ui.ProgressBar_Download_GCC,
            Method = GCC_Installer.Execute,
            Params = ()
        )
        MainWindowSignals.Signal_MainWindowShown.connect(
            self.ui.Button_Install_GCC.click #if Config.GetValue('Env', 'GCC', 'Undetected') == 'Undetected' else EnvConfiguratorSignals.Signal_GCCDetected.emit
        )
        self.ui.Button_Install_GCC.setText('')
        self.ui.Button_Install_GCC.setCheckable(True)
        self.ui.Button_Install_GCC.setToolTipDuration(-1)
        self.ui.Button_Install_GCC.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_GCCUndetected.connect(
            lambda: Config.EditConfig('Env', 'GCC', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_GCCUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到GCC，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_GCCInstalled.connect(#self.ui.Button_Install_GCC.click)
            lambda: EnvConfiguratorSignals.Signal_GCCDetected.emit()
        )
        EnvConfiguratorSignals.Signal_GCCInstallFailed.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Warning",
                Text = "安装GCC出错",
                EventButtons = [QMessageBox.Ok]
            )
        )
        EnvConfiguratorSignals.Signal_GCCDetected.connect(
            lambda: Config.EditConfig('Env', 'GCC', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_GCCDetected.connect(
            lambda: self.ui.ProgressBar_Download_GCC.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_GCCStatus.connect(
            lambda Status: self.ui.Label_Download_GCC_Status.setText(Status)
        )

        self.ui.Label_Download_CMake.setText("CMake")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Install_CMake,
            ProgressBar = self.ui.ProgressBar_Download_CMake,
            Method = CMake_Installer.Execute,
            Params = ()
        )
        EnvConfiguratorSignals.Signal_GCCDetected.connect(
            self.ui.Button_Install_CMake.click #if Config.GetValue('Env', 'CMake', 'Undetected') == 'Undetected' else EnvConfiguratorSignals.Signal_CMakeDetected.emit
        )
        self.ui.Button_Install_CMake.setText('')
        self.ui.Button_Install_CMake.setCheckable(True)
        self.ui.Button_Install_CMake.setToolTipDuration(-1)
        self.ui.Button_Install_CMake.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_CMakeUndetected.connect(
            lambda: Config.EditConfig('Env', 'CMake', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_CMakeUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到CMake，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_CMakeInstalled.connect(#self.ui.Button_Install_CMake.click)
            lambda: EnvConfiguratorSignals.Signal_CMakeDetected.emit()
        )
        EnvConfiguratorSignals.Signal_CMakeInstallFailed.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Warning",
                Text = "安装CMake出错",
                EventButtons = [QMessageBox.Ok]
            )
        )
        EnvConfiguratorSignals.Signal_CMakeDetected.connect(
            lambda: Config.EditConfig('Env', 'CMake', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_CMakeDetected.connect(
            lambda: self.ui.ProgressBar_Download_CMake.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_CMakeStatus.connect(
            lambda Status: self.ui.Label_Download_CMake_Status.setText(Status)
        )
        '''

        self.ui.Label_Download_Python.setText("Python")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Install_Python,
            ProgressBar = self.ui.ProgressBar_Download_Python,
            Method = Python_Installer.Execute,
            Params = ('3.9', )
        )
        MainWindowSignals.Signal_MainWindowShown.connect( #EnvConfiguratorSignals.Signal_CMakeDetected.connect(
            self.ui.Button_Install_Python.click #if Config.GetValue('Env', 'Python', 'Undetected') == 'Undetected' else EnvConfiguratorSignals.Signal_PythonDetected.emit
        )
        self.ui.Button_Install_Python.setText('')
        self.ui.Button_Install_Python.setCheckable(True)
        self.ui.Button_Install_Python.setToolTipDuration(-1)
        self.ui.Button_Install_Python.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_PythonUndetected.connect(
            lambda: Config.EditConfig('Env', 'Python', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_PythonUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到Python，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_PythonInstalled.connect(#self.ui.Button_Install_Python.click)
            lambda: EnvConfiguratorSignals.Signal_PythonDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PythonInstallFailed.connect(
            lambda: Function_ShowMessageBox(
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
            lambda: self.ui.ProgressBar_Download_Python.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PythonStatus.connect(
            lambda Status: self.ui.Label_Download_Python_Status.setText(Status)
        )

        self.ui.Label_Download_PyReqs.setText("Python Requirements")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Install_PyReqs,
            ProgressBar = self.ui.ProgressBar_Download_PyReqs,
            Method = PyReqs_Installer.Execute,
            Params = (NormPath(Path(ResourceDir).joinpath('requirements.txt')), )
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            self.ui.Button_Install_PyReqs.click #if Config.GetValue('Env', 'PyReqs', 'Undetected') == 'Undetected' else EnvConfiguratorSignals.Signal_PyReqsDetected.emit
        )
        self.ui.Button_Install_PyReqs.setText('')
        self.ui.Button_Install_PyReqs.setCheckable(True)
        self.ui.Button_Install_PyReqs.setToolTipDuration(-1)
        self.ui.Button_Install_PyReqs.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_PyReqsUndetected.connect(
            lambda: Config.EditConfig('Env', 'PyReqs', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_PyReqsUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到Python依赖库，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_PyReqsInstalled.connect(#self.ui.Button_Install_PyReqs.click)
            lambda: EnvConfiguratorSignals.Signal_PyReqsDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PythonInstallFailed.connect(
            lambda: Function_ShowMessageBox(
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
            lambda: self.ui.ProgressBar_Download_PyReqs.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PyReqsStatus.connect(
            lambda Status: self.ui.Label_Download_PyReqs_Status.setText(Status)
        )

        self.ui.Label_Download_Pytorch.setText("Pytorch")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Install_Pytorch,
            ProgressBar = self.ui.ProgressBar_Download_Pytorch,
            Method = Pytorch_Installer.Execute,
            Params = ()
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            self.ui.Button_Install_Pytorch.click #if Config.GetValue('Env', 'Pytorch', 'Undetected') == 'Undetected' else EnvConfiguratorSignals.Signal_PytorchDetected.emit
        )
        self.ui.Button_Install_Pytorch.setText('')
        self.ui.Button_Install_Pytorch.setCheckable(True)
        self.ui.Button_Install_Pytorch.setToolTipDuration(-1)
        self.ui.Button_Install_Pytorch.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_PytorchUndetected.connect(
            lambda: Config.EditConfig('Env', 'Pytorch', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_PytorchUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到Pytorch，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_PytorchInstalled.connect(#self.ui.Button_Install_Pytorch.click)
            lambda: EnvConfiguratorSignals.Signal_PytorchDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PytorchInstallFailed.connect(
            lambda: Function_ShowMessageBox(
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
            lambda: self.ui.ProgressBar_Download_Pytorch.setValue(100),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PytorchStatus.connect(
            lambda Status: self.ui.Label_Download_Pytorch_Status.setText(Status)
        )

        ##########################################################
        ##################### Content: Tools #####################
        ##########################################################

        DialogBox = MessageBox_Stacked()
        DialogBox.setWindowTitle('Guidance（该引导仅出现一次）')
        DialogBox.SetContent(
            [
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance0.png')),
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance1.png')),
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance2.png')),
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance3.png')),
                NormPath(Path(ResourceDir).joinpath('Sources/Guidance4.png')),
            ],
            [
                '欢迎来到工具界面！这里集成了EVT目前支持的所有工具，来快速熟悉一下使用方法吧',
                '顶部区域用于切换当前工具',
                '中间区域用于设置当前工具的各项参数，从左至右依次为目录、设置、预览',
                '底部区域用于执行当前工具',
                '工具之间会自动继承可关联的参数选项，如果不希望这样可以到设置页面关闭该功能'
            ]
        )
        #DialogBox.setStandardButtons(QMessageBox.Ok)
        self.ui.Button_Menu_Tools.clicked.connect(
            lambda: DialogBox.exec() if eval(Config.GetValue('Dialog', 'GuidanceShown', 'False')) is False else None,
            type = Qt.QueuedConnection
        )
        self.ui.Button_Menu_Tools.clicked.connect(
            lambda: Config.EditConfig('Dialog', 'GuidanceShown', 'True'),
            type = Qt.QueuedConnection
        )

        '''
        self.ui.Label_Tools_Title.setText(QCA.translate("Label", "工具  -   "))

        self.ui.ComboBox_Tools.addItems([
                QCA.translate("ComboBox", "音频基本处理"),
                QCA.translate("ComboBox", "语音识别和筛选"),
                QCA.translate("ComboBox", "语音转文字字幕"),
                QCA.translate("ComboBox", "语音数据集制作"),
                QCA.translate("ComboBox", "语音模型训练"),
                QCA.translate("ComboBox", "语音模型推理")
            ]
        )
        self.ui.ComboBox_Tools.setCurrentText(QCA.translate("ComboBox", '音频基本处理'))
        self.ui.ComboBox_Tools.currentIndexChanged.connect(
            lambda Index: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = Index
            )
        )
        self.ui.ComboBox_Tools.currentIndexChanged.connect(
            lambda Index: self.ui.SpinBox_Tools.setValue(Index + 1)
        )
        '''

        self.ui.ToolButton_Tools_Title_AudioProcessor.setText(QCA.translate("ToolButton", '音频基本处理'))
        self.ui.ToolButton_Tools_Title_AudioProcessor.setCheckable(True)
        self.ui.ToolButton_Tools_Title_AudioProcessor.setChecked(True)
        self.ui.ToolButton_Tools_Title_AudioProcessor.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_AudioProcessor.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 0
            )
        )

        self.ui.ToolButton_Tools_Title_VoiceIdentifier.setText(QCA.translate("ToolButton", "语音识别和筛选"))
        self.ui.ToolButton_Tools_Title_VoiceIdentifier.setCheckable(True)
        self.ui.ToolButton_Tools_Title_VoiceIdentifier.setChecked(False)
        self.ui.ToolButton_Tools_Title_VoiceIdentifier.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_VoiceIdentifier.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 1
            )
        )

        self.ui.ToolButton_Tools_Title_VoiceTranscriber.setText(QCA.translate("ToolButton", "语音转文字字幕"))
        self.ui.ToolButton_Tools_Title_VoiceTranscriber.setCheckable(True)
        self.ui.ToolButton_Tools_Title_VoiceTranscriber.setChecked(False)
        self.ui.ToolButton_Tools_Title_VoiceTranscriber.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_VoiceTranscriber.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 2
            )
        )

        self.ui.ToolButton_Tools_Title_DatasetCreator.setText(QCA.translate("ToolButton", "语音数据集制作"))
        self.ui.ToolButton_Tools_Title_DatasetCreator.setCheckable(True)
        self.ui.ToolButton_Tools_Title_DatasetCreator.setChecked(False)
        self.ui.ToolButton_Tools_Title_DatasetCreator.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_DatasetCreator.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 3
            )
        )

        self.ui.ToolButton_Tools_Title_VoiceTrainer.setText(QCA.translate("ToolButton", "语音模型训练"))
        self.ui.ToolButton_Tools_Title_VoiceTrainer.setCheckable(True)
        self.ui.ToolButton_Tools_Title_VoiceTrainer.setChecked(False)
        self.ui.ToolButton_Tools_Title_VoiceTrainer.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_VoiceTrainer.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 4
            )
        )

        self.ui.ToolButton_Tools_Title_VoiceConverter.setText(QCA.translate("ToolButton", "语音模型推理"))
        self.ui.ToolButton_Tools_Title_VoiceConverter.setCheckable(True)
        self.ui.ToolButton_Tools_Title_VoiceConverter.setChecked(False)
        self.ui.ToolButton_Tools_Title_VoiceConverter.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_VoiceConverter.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 5
            )
        )

        ##################### Tool_AudioProcessor #####################
        '''
        Function_SetText(
            Widget = self.ui.TextBrowser_Intro_Tool_AudioProcessor,
            Text = SetRichText(
                Title = QCA.translate("TextBrowser", "音频基本处理"),
                TitleAlign = "center",
                TitleSize = 18,
                Body = QCA.translate("TextBrowser",
                    "\n"
                    "[介绍]\n"
                    "该工具会将媒体文件批量转换为音频文件，然后自动切除音频的静音部分\n"
                    "\n"
                    "[用法]\n"
                    "1. 设置位于页面右侧的参数\n"
                    "2. 点击位于页面底部的“执行”按钮\n"
                    "\n"
                    "[提示]\n"
                    "1. 您可以通过点击“打开输出目录”按钮以查看当前工具在执行完毕后输出的文件\n"
                )
            )
        )
        '''

        Path_Config_Tool_AudioProcessor = NormPath(Path(CurrentDir).joinpath('Config', 'Config_Tool_AudioProcessor.ini'))
        Config_Tool_AudioProcessor = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_Tool_AudioProcessor',
                Path_Config_Tool_AudioProcessor
            )
        )

        # Middle
        self.ui.GroupBox_EssentialParams_Tool_AudioProcessor.setTitle(QCA.translate("GroupBox", "必要参数"))

        self.ui.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor.setChecked(
            True #eval(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor,
            CheckedText = "基础设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_AudioProcessor.EditConfig
            ],
            CheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_AudioProcessor,...,...,0,self.ui.Frame_Tool_AudioProcessor_Media_Dir_Input.height()+self.ui.Frame_Tool_AudioProcessor_Media_Format_Output.height()+self.ui.Frame_Tool_AudioProcessor_Media_Dir_Output.height()+self.ui.Frame_Tool_AudioProcessor_Slice_Audio.height(),0,'Extend'),
                #('AudioProcessor', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_AudioProcessor.EditConfig
            ],
            UncheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_AudioProcessor,...,...,0,self.ui.Frame_Tool_AudioProcessor_Media_Dir_Input.height()+self.ui.Frame_Tool_AudioProcessor_Media_Format_Output.height()+self.ui.Frame_Tool_AudioProcessor_Media_Dir_Output.height()+self.ui.Frame_Tool_AudioProcessor_Slice_Audio.height(),0,'Reduce'),
                #('AudioProcessor', 'Toggle_BasicSettings', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_Media_Dir_Input,
            Text = SetRichText(
                Title = QCA.translate("Label", "媒体输入目录"),
                Body = QCA.translate("Label", "该目录中的媒体文件将会以下列设置输出为音频文件。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_AudioProcessor_Media_Dir_Input,
            LineEdit = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Input,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Input,
            Text = str(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Media_Dir_Input', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Input.textChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'Media_Dir_Input', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_Media_Format_Output,
            Text = SetRichText(
                Title = QCA.translate("Label", "媒体输出格式"),
                Body = QCA.translate("Label", "媒体文件将会以设置的格式输出为音频文件，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output.addItems(['flac', 'wav', 'mp3', 'aac', 'm4a', 'wma', 'aiff', 'au', 'ogg', 'None'])
        self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output.setCurrentText(
            str(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Media_Format_Output', 'wav'))
        )
        self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output.currentTextChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'Media_Format_Output', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_Slice_Audio,
            Text = SetRichText(
                Title = "启用静音切除",
                Body = QCA.translate("Label", "音频中的静音部分将被切除。")
            )
        )
        self.ui.CheckBox_Tool_AudioProcessor_Slice_Audio.setCheckable(True)
        self.ui.CheckBox_Tool_AudioProcessor_Slice_Audio.setChecked(
            eval(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Slice_Audio', 'True'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_AudioProcessor_Slice_Audio,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Tool_AudioProcessor.EditConfig,
                #self.ui.Frame_Tool_AudioProcessor_RMS_Threshold.setVisible,
                #self.ui.Frame_Tool_AudioProcessor_Hop_Size.setVisible,
                #self.ui.Frame_Tool_AudioProcessor_Silent_Interval_Min.setVisible,
                #self.ui.Frame_Tool_AudioProcessor_Silence_Kept_Max.setVisible,
                #self.ui.Frame_Tool_AudioProcessor_Audio_Length_Min.setVisible,
                #self.Function_AnimateFrame
            ],
            CheckedArgsList = [
                ('AudioProcessor', 'Slice_Audio', 'True'),
                #(True),
                #(True),
                #(True),
                #(True),
                #(True),
                #(self.ui.Frame_AdvanceSettings_Tool_AudioProcessor,...,...,0,self.ui.Frame_Tool_AudioProcessor_RMS_Threshold.height()+self.ui.Frame_Tool_AudioProcessor_Hop_Size.height()+self.ui.Frame_Tool_AudioProcessor_Silent_Interval_Min.height()+self.ui.Frame_Tool_AudioProcessor_Silence_Kept_Max.height()+self.ui.Frame_Tool_AudioProcessor_Audio_Length_Min.height()+self.ui.Frame_Tool_AudioProcessor_SampleRate.height()+self.ui.Frame_Tool_AudioProcessor_SampleWidth.height()+self.ui.Frame_Tool_AudioProcessor_ToMono.height(),0,'Extend')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Tool_AudioProcessor.EditConfig,
                #self.ui.Frame_Tool_AudioProcessor_RMS_Threshold.setVisible,
                #self.ui.Frame_Tool_AudioProcessor_Hop_Size.setVisible,
                #self.ui.Frame_Tool_AudioProcessor_Silent_Interval_Min.setVisible,
                #self.ui.Frame_Tool_AudioProcessor_Silence_Kept_Max.setVisible,
                #self.ui.Frame_Tool_AudioProcessor_Audio_Length_Min.setVisible,
                #self.Function_AnimateFrame
            ],
            UncheckedArgsList = [
                ('AudioProcessor', 'Slice_Audio', 'False'),
                #(False),
                #(False),
                #(False),
                #(False),
                #(False),
                #(self.ui.Frame_BasicSettings_Tool_AudioProcessor,...,...,0,self.ui.Frame_Tool_AudioProcessor_SampleRate.height()+self.ui.Frame_Tool_AudioProcessor_SampleWidth.height()+self.ui.Frame_Tool_AudioProcessor_ToMono.height(),0,'Reduce')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_Media_Dir_Output,
            Text = SetRichText(
                Title = QCA.translate("Label", "媒体输出目录"),
                Body = QCA.translate("Label", "最后生成的音频文件将被保存到该目录中。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_AudioProcessor_Media_Dir_Output,
            LineEdit = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,
            Text = str(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Media_Dir_Output', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output.textChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'Media_Dir_Output', str(Value))
        )
        '''
        self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output.textChanged.connect(
            lambda Value: Function_ShowMessageBox(
                MessageType = QMessageBox.Warning,
                WindowTitle = "Warning",
                Text = "输出路径与输入路径相同"
            ) if Value == self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Input.text() else None
        )
        '''

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor.setChecked(
            False #eval(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Toggle_AdvanceSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor,
            CheckedText = "高级设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_AudioProcessor.EditConfig
            ],
            CheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_AudioProcessor,...,...,0,self.ui.Frame_Tool_AudioProcessor_RMS_Threshold.height()+self.ui.Frame_Tool_AudioProcessor_Hop_Size.height()+self.ui.Frame_Tool_AudioProcessor_Silent_Interval_Min.height()+self.ui.Frame_Tool_AudioProcessor_Silence_Kept_Max.height()+self.ui.Frame_Tool_AudioProcessor_Audio_Length_Min.height()+self.ui.Frame_Tool_AudioProcessor_SampleRate.height()+self.ui.Frame_Tool_AudioProcessor_SampleWidth.height()+self.ui.Frame_Tool_AudioProcessor_ToMono.height(),0,'Extend'),
                #('AudioProcessor', 'Toggle_AdvanceSettings', 'True')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_AudioProcessor.EditConfig
            ],
            UncheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_AudioProcessor,...,...,0,self.ui.Frame_Tool_AudioProcessor_RMS_Threshold.height()+self.ui.Frame_Tool_AudioProcessor_Hop_Size.height()+self.ui.Frame_Tool_AudioProcessor_Silent_Interval_Min.height()+self.ui.Frame_Tool_AudioProcessor_Silence_Kept_Max.height()+self.ui.Frame_Tool_AudioProcessor_Audio_Length_Min.height()+self.ui.Frame_Tool_AudioProcessor_SampleRate.height()+self.ui.Frame_Tool_AudioProcessor_SampleWidth.height()+self.ui.Frame_Tool_AudioProcessor_ToMono.height(),0,'Reduce'),
                #('AudioProcessor', 'Toggle_AdvanceSettings', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_RMS_Threshold,
            Text = SetRichText(
                Title = QCA.translate("Label", "均方根阈值 (db)"),
                Body = QCA.translate("Label", "低于该阈值的片段将被视作静音进行处理，若有降噪需求可以增加该值。")
            )
        )
        self.ui.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setRange(-100, 0)
        #self.ui.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setValue(
            float(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'RMS_Threshold', '-40.'))
        )
        self.ui.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.valueChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'RMS_Threshold', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_Hop_Size,
            Text = SetRichText(
                Title = QCA.translate("Label", "跃点大小 (ms)"),
                Body = QCA.translate("Label", "每个RMS帧的长度，增加该值能够提高分割精度但会减慢进程。")
            )
        )
        self.ui.SpinBox_Tool_AudioProcessor_Hop_Size.setRange(0, 100)
        self.ui.SpinBox_Tool_AudioProcessor_Hop_Size.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Hop_Size.setValue(
            int(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Hop_Size', '10'))
        )
        self.ui.SpinBox_Tool_AudioProcessor_Hop_Size.valueChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'Hop_Size', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_Silent_Interval_Min,
            Text = SetRichText(
                Title = QCA.translate("Label", "最小静音间隔 (ms)"),
                Body = QCA.translate("Label", "静音部分被分割成的最小长度，若音频只包含短暂中断可以减小该值。")
            )
        )
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setRange(0, 3000)
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setValue(
            int(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Silent_Interval_Min', '300'))
        )
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.valueChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'Silent_Interval_Min', str(Value))
        )
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setToolTip(QCA.translate("ToolTip", "注意：这个值必须小于最小音频长度，大于跃点大小。"))

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_Silence_Kept_Max,
            Text = SetRichText(
                Title = QCA.translate("Label", "最大静音长度 (ms)"),
                Body = QCA.translate("Label", "被分割的音频周围保持静音的最大长度。")
            )
        )
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setRange(0, 10000)
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setValue(
            int(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Silence_Kept_Max', '1000'))
        )
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.valueChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'Silence_Kept_Max', str(Value))
        )
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setToolTip(QCA.translate("ToolTip", "注意：这个值无需完全对应被分割音频中的静音长度。算法将自行检索最佳的分割位置。"))

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_Audio_Length_Min,
            Text = SetRichText(
                Title = QCA.translate("Label", "最小音频长度 (ms)"),
                Body = QCA.translate("Label", "每个被分割的音频片段所需的最小长度。")
            )
        )
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setRange(300, 30000)
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setValue(
            int(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Audio_Length_Min', '3000'))
        )
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.valueChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'Audio_Length_Min', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_ToMono,
            Text = SetRichText(
                Title = "合并声道",
                Body = QCA.translate("Label", "将输出音频的声道合并为单声道。")
            )
        )
        self.ui.CheckBox_Tool_AudioProcessor_ToMono.setCheckable(True)
        self.ui.CheckBox_Tool_AudioProcessor_ToMono.setChecked(
            eval(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'ToMono', 'False'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_AudioProcessor_ToMono,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Tool_AudioProcessor.EditConfig
            ],
            CheckedArgsList = [
                ('AudioProcessor', 'ToMono', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Tool_AudioProcessor.EditConfig
            ],
            UncheckedArgsList = [
                ('AudioProcessor', 'ToMono', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_SampleRate,
            Text = SetRichText(
                Title = "输出采样率",
                Body = QCA.translate("Label", "输出音频所拥有的采样率，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Tool_AudioProcessor_SampleRate.addItems(['22050', '44100', '48000', '96000', '192000', 'None'])
        self.ui.ComboBox_Tool_AudioProcessor_SampleRate.setCurrentText(
            str(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'SampleRate', 'None'))
        )
        self.ui.ComboBox_Tool_AudioProcessor_SampleRate.currentTextChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'SampleRate', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_AudioProcessor_SampleWidth,
            Text = SetRichText(
                Title = "输出采样位数",
                Body = QCA.translate("Label", "输出音频所拥有的采样位数，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Tool_AudioProcessor_SampleWidth.addItems(['8', '16', '24', '32', '32 (Float)', 'None'])
        self.ui.ComboBox_Tool_AudioProcessor_SampleWidth.setCurrentText(
            str(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'SampleWidth', 'None'))
        )
        self.ui.ComboBox_Tool_AudioProcessor_SampleWidth.currentTextChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'SampleWidth', str(Value))
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_Tool_AudioProcessor,
            RootItemTexts = [self.ui.GroupBox_EssentialParams_Tool_AudioProcessor.title()],
            ChildItemTexts = [(self.ui.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor.text(),self.ui.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor.text())],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_AudioProcessor.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_EssentialParams_Tool_AudioProcessor,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_AudioProcessor
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_AudioProcessor.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_BasicSettings_Tool_AudioProcessor,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_AudioProcessor
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_AudioProcessor.topLevelItem(0).child(1),
            TargetWidget = self.ui.Frame_AdvanceSettings_Tool_AudioProcessor,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_AudioProcessor
        )

        # Right
        MonitorFile_Config_AudioProcessor = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_Tool_AudioProcessor')
        )
        MonitorFile_Config_AudioProcessor.start()
        MonitorFile_Config_AudioProcessor.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Tool_AudioProcessor.setText(
                FileContent
            )
        )

        self.ui.Button_CheckOutput_Tool_AudioProcessor.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Tool_AudioProcessor,
            URL = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,
            ButtonTooltip = "Click to open"
        )

        # Bottom
        self.ui.Button_Tool_AudioProcessor_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_AudioProcessor_Execute.setToolTip(QCA.translate("ToolTip", "执行音频基本处理"))
        self.ui.Button_Tool_AudioProcessor_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_AudioProcessor_Terminate.setToolTip(QCA.translate("ToolTip", "终止音频基本处理"))
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Tool_AudioProcessor_Execute,
            TerminateButton = self.ui.Button_Tool_AudioProcessor_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_AudioProcessor,
            ConsoleFrame = self.ui.Frame_Console,
            Method = Execute_Audio_Processing.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Input,
                self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,
                self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output,
                self.ui.ComboBox_Tool_AudioProcessor_SampleRate,
                self.ui.ComboBox_Tool_AudioProcessor_SampleWidth,
                self.ui.CheckBox_Tool_AudioProcessor_ToMono,
                #self.ui.CheckBox_Tool_AudioProcessor_Denoise_Audio,
                self.ui.CheckBox_Tool_AudioProcessor_Slice_Audio,
                self.ui.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold,
                self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min,
                self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min,
                self.ui.SpinBox_Tool_AudioProcessor_Hop_Size,
                self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max
            ],
            EmptyAllowed = [
                self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output,
                self.ui.ComboBox_Tool_AudioProcessor_SampleRate,
                self.ui.ComboBox_Tool_AudioProcessor_SampleWidth
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (QMessageBox.Question,"Ask","当前任务已执行结束，是否跳转至下一工具界面？",QMessageBox.Yes|QMessageBox.No,[QMessageBox.Yes],[[self.ui.Frame_Tools_Top.layout().itemAt(1).widget().click]],[[()]])
            ]
        )

        ##################### Tool_VoiceIdentifier #####################
        '''
        Function_SetText(
            Widget = self.ui.TextBrowser_Intro_Tool_VoiceIdentifier,
            Text = SetRichText(
                Title = QCA.translate("TextBrowser", "语音识别和筛选"),
                TitleAlign = "center",
                TitleSize = 18,
                Body = QCA.translate("TextBrowser",
                    "\n"
                    "[介绍]\n"
                    "该工具会在不同说话人的音频中批量筛选出属于同一说话人的音频。用户需要提供一段包含目标说话人的语音作为期望值\n"
                    "\n"
                    "[用法]\n"
                    "1. 设置位于页面右侧的参数\n"
                    "2. 点击位于页面底部的“执行”按钮\n"
                    "3. 若还有筛选其它人物的需要，可在更改“标准音频路径”和“人物名字”参数后重新执行\n"
                    "\n"
                    "[提示]\n"
                    "1. 您可以通过开启“自动同步...”选项以保持前后工具的部分参数设置一致，或者点击“同步...”按钮以快速设置当前工具的下列参数：\n"
                    "   Audio Dir Input\n"
                    "2. 您可以通过点击“打开输出目录”按钮以查看当前工具在执行完毕后输出的文件\n"
                )
            )
        )
        '''

        Path_Config_Tool_VoiceIdentifier = NormPath(Path(CurrentDir).joinpath('Config', 'Config_Tool_VoiceIdentifier.ini'))
        Config_Tool_VoiceIdentifier = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_Tool_VoiceIdentifier',
                Path_Config_Tool_VoiceIdentifier
            )
        )

        # Middle
        self.ui.GroupBox_EssentialParams_Tool_VoiceIdentifier.setTitle("必要参数")

        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier.setChecked(
            True #eval(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier,
            CheckedText = "基础设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceIdentifier.EditConfig
            ],
            CheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceIdentifier,...,...,0,self.ui.Frame_Tool_VoiceIdentifier_Audio_Dir_Input.height()+self.ui.Frame_Tool_VoiceIdentifier_StdAudioSpeaker.height()+self.ui.Frame_Tool_VoiceIdentifier_DecisionThreshold.height()+self.ui.Frame_Tool_VoiceIdentifier_Audio_Dir_Output.height(),0,'Extend'),
                #('VoiceIdentifier', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceIdentifier.EditConfig
            ],
            UncheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceIdentifier,...,...,0,self.ui.Frame_Tool_VoiceIdentifier_Audio_Dir_Input.height()+self.ui.Frame_Tool_VoiceIdentifier_StdAudioSpeaker.height()+self.ui.Frame_Tool_VoiceIdentifier_DecisionThreshold.height()+self.ui.Frame_Tool_VoiceIdentifier_Audio_Dir_Output.height(),0,'Reduce'),
                #('VoiceIdentifier', 'Toggle_BasicSettings', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceIdentifier_Audio_Dir_Input,
            Text = SetRichText(
                Title = "音频输入目录",
                Body = QCA.translate("Label", "该目录中的音频文件将会按照以下设置进行识别筛选。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Audio_Dir_Input,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input,
            Text = str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Audio_Dir_Input', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input.textChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Audio_Dir_Input', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceIdentifier_StdAudioSpeaker,
            Text = SetRichText(
                Title = "目标人物与音频",
                Body = QCA.translate("Label", "目标人物的名字及其语音文件的所在路径，音频中尽量不要混入杂音。")
            )
        )
        self.ui.Table_Tool_VoiceIdentifier_StdAudioSpeaker.SetHorizontalHeaders(['人物姓名', '音频路径', '增删'])
        self.ui.Table_Tool_VoiceIdentifier_StdAudioSpeaker.SetValue(
            eval(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'StdAudioSpeaker', '{"": ""}')),
            FileType = "音频类型 (*.mp3 *.aac *.wav *.flac)"
        )
        self.ui.Table_Tool_VoiceIdentifier_StdAudioSpeaker.ValueChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'StdAudioSpeaker', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceIdentifier_DecisionThreshold,
            Text = SetRichText(
                Title = "判断阈值",
                Body = QCA.translate("Label", "判断是否为同一人的阈值，若参与比对的说话人声音相识度较高可以增加该值。")
            )
        )
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setRange(0.5, 1)
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setValue(
            float(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'DecisionThreshold', '0.75'))
        )
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.valueChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'DecisionThreshold', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceIdentifier_Audio_Dir_Output,
            Text = SetRichText(
                Title = "音频输出目录",
                Body = QCA.translate("Label", "最后筛选出的音频文件将被复制到该目录中。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Audio_Dir_Output,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,
            Text = str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Audio_Dir_Output', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output.textChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Audio_Dir_Output', str(Value))
        )

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier,
            CheckedText = "高级设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame
            ],
            CheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceIdentifier,...,...,0,self.ui.Frame_Tool_VoiceIdentifier_Model_Dir.height()+self.ui.Frame_Tool_VoiceIdentifier_Model_Type.height()+self.ui.Frame_Tool_VoiceIdentifier_Model_Name.height()+self.ui.Frame_Tool_VoiceIdentifier_Feature_Method.height()+self.ui.Frame_Tool_VoiceIdentifier_Duration_of_Audio.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceIdentifier,...,...,0,self.ui.Frame_Tool_VoiceIdentifier_Model_Dir.height()+self.ui.Frame_Tool_VoiceIdentifier_Model_Type.height()+self.ui.Frame_Tool_VoiceIdentifier_Model_Name.height()+self.ui.Frame_Tool_VoiceIdentifier_Feature_Method.height()+self.ui.Frame_Tool_VoiceIdentifier_Duration_of_Audio.height(),0,'Reduce')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceIdentifier_Model_Dir,
            Text = SetRichText(
                Title = "模型存放目录",
                Body = QCA.translate("Label", "该目录将会用于存放下载的声纹识别模型，若模型已存在会直接使用。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Model_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Model_Dir,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_VoiceIdentifier_Model_Dir.setText(
            str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Model_Dir', NormPath(Path(CurrentDir).joinpath('Download'), 'Posix')))
        )
        self.ui.LineEdit_Tool_VoiceIdentifier_Model_Dir.textChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Model_Dir', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceIdentifier_Model_Type,
            Text = SetRichText(
                Title = "模型类型",
                Body = QCA.translate("Label", "声纹识别模型的类型。")
            )
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type.addItems(['Ecapa-Tdnn'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type.setCurrentText(
            str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Model_Type', 'Ecapa-Tdnn'))
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Model_Type', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceIdentifier_Model_Name,
            Text = SetRichText(
                Title = "模型名字",
                Body = QCA.translate("Label", "声纹识别模型的名字，默认代表模型的大小。")
            )
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name.addItems(['small'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name.setCurrentText(
            str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Model_Name', 'small'))
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Model_Name', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceIdentifier_Feature_Method,
            Text = SetRichText(
                Title = "特征提取方法",
                Body = QCA.translate("Label", "音频特征的提取方法。")
            )
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method.addItems(['spectrogram', 'melspectrogram'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method.setCurrentText(
            str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Feature_Method', 'spectrogram'))
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Feature_Method', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceIdentifier_Duration_of_Audio,
            Text = SetRichText(
                Title = "音频长度",
                Body = QCA.translate("Label", "用于预测的音频长度。")
            )
        )
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setRange(0, 30)
        #self.ui.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setValue(
            float(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Duration_of_Audio', '3.00'))
        )
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.textChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Duration_of_Audio', str(Value))
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_Tool_VoiceIdentifier,
            RootItemTexts = [self.ui.GroupBox_EssentialParams_Tool_VoiceIdentifier.title()],
            ChildItemTexts = [(self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier.text(),self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier.text())],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceIdentifier.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_EssentialParams_Tool_VoiceIdentifier,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceIdentifier
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceIdentifier.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_BasicSettings_Tool_VoiceIdentifier,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceIdentifier
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceIdentifier.topLevelItem(0).child(1),
            TargetWidget = self.ui.Frame_AdvanceSettings_Tool_VoiceIdentifier,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceIdentifier
        )

        # Right
        MonitorFile_Config_VoiceIdentifier = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_Tool_VoiceIdentifier')
        )
        MonitorFile_Config_VoiceIdentifier.start()
        MonitorFile_Config_VoiceIdentifier.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Tool_VoiceIdentifier.setText(
                FileContent
            )
        )

        self.ui.Button_SyncParams_Tool_VoiceIdentifier.setText(QCA.translate("Button", "关联参数设置"))
        Function_ParamsSynchronizer(
            Trigger = self.ui.Button_SyncParams_Tool_VoiceIdentifier,
            ParamsFrom = [
                self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output
            ],
            ParamsTo = [
                self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input
            ]
        )

        self.ui.Button_CheckOutput_Tool_VoiceIdentifier.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Tool_VoiceIdentifier,
            URL = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,
            ButtonTooltip = "Click to open"
        )

        # Bottom
        self.ui.Button_Tool_VoiceIdentifier_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceIdentifier_Execute.setToolTip("执行语音识别和筛选")
        self.ui.Button_Tool_VoiceIdentifier_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceIdentifier_Terminate.setToolTip("终止语音识别和筛选")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Tool_VoiceIdentifier_Execute,
            TerminateButton = self.ui.Button_Tool_VoiceIdentifier_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_VoiceIdentifier,
            ConsoleFrame = self.ui.Frame_Console,
            Method = Execute_Voice_Identifying.Execute,
            ParamsFrom = [
                self.ui.Table_Tool_VoiceIdentifier_StdAudioSpeaker,
                self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input,
                self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,
                self.ui.LineEdit_Tool_VoiceIdentifier_Model_Dir,
                self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type,
                self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name,
                self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method,
                self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold,
                self.ui.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (QMessageBox.Question,"Ask","当前任务已执行结束，是否跳转至下一工具界面？",QMessageBox.Yes|QMessageBox.No,[QMessageBox.Yes],[[self.ui.Frame_Tools_Top.layout().itemAt(2).widget().click]],[[()]])
            ]
        )

        ##################### Tool_VoiceTranscriber #####################
        '''
        Function_SetText(
            Widget = self.ui.TextBrowser_Intro_Tool_VoiceTranscriber,
            Text = SetRichText(
                Title = QCA.translate("TextBrowser", "语音转文字字幕"),
                TitleAlign = "center",
                TitleSize = 18,
                Body = QCA.translate("TextBrowser",
                    "\n"
                    "[介绍]\n"
                    "该工具会将语音文件的内容批量转换为带时间戳的文本并以字幕文件的形式保存\n"
                    "\n"
                    "[用法]\n"
                    "1. 设置位于页面右侧的参数\n"
                    "2. 点击位于页面底部的“执行”按钮\n"
                    "\n"
                    "[提示]\n"
                    "1. 您可以通过开启“自动同步...”选项以保持前后工具的部分参数设置一致，或者点击“同步...”按钮以快速设置当前工具的下列参数：\n"
                    "   WAV Dir\n"
                    "2. 您可以通过点击“打开输出目录”按钮以查看当前工具在执行完毕后输出的文件\n"
                )
            )
        )
        '''

        Path_Config_Tool_VoiceTranscriber = NormPath(Path(CurrentDir).joinpath('Config', 'Config_Tool_VoiceTranscriber.ini'))
        Config_Tool_VoiceTranscriber = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_Tool_VoiceTranscriber',
                Path_Config_Tool_VoiceTranscriber
            )
        )

        # Middle
        self.ui.GroupBox_EssentialParams_Tool_VoiceTranscriber.setTitle("必要参数")

        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber.setChecked(
            True #eval(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber,
            CheckedText = "基础设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceTranscriber.EditConfig
            ],
            CheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_WAV_Dir.height()+self.ui.Frame_Tool_VoiceTranscriber_SRT_Dir.height(),0,'Extend'),
                #('VoiceTranscriber', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceTranscriber.EditConfig
            ],
            UncheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_WAV_Dir.height()+self.ui.Frame_Tool_VoiceTranscriber_SRT_Dir.height(),0,'Reduce'),
                #('VoiceTranscriber', 'Toggle_BasicSettings', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTranscriber_WAV_Dir,
            Text = SetRichText(
                Title = "音频目录",
                Body = QCA.translate("Label", "该目录中的wav文件的语音内容将会按照以下设置转为文字。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_WAV_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,
            Text = str(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'WAV_Dir', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir.textChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'WAV_Dir', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTranscriber_SRT_Dir,
            Text = SetRichText(
                Title = "字幕输出目录",
                Body = QCA.translate("Label", "最后生成的字幕文件将会保存到该目录中。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_SRT_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir,
            Text = str(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'SRT_Dir', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir.textChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'SRT_Dir', str(Value))
        )

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber,
            CheckedText = "高级设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame
            ],
            CheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_Model_Dir.height()+self.ui.Frame_Tool_VoiceTranscriber_Model_Name.height()+self.ui.Frame_Tool_VoiceTranscriber_Verbose.height()+self.ui.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text.height()+self.ui.Frame_Tool_VoiceTranscriber_fp16.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_Model_Dir.height()+self.ui.Frame_Tool_VoiceTranscriber_Model_Name.height()+self.ui.Frame_Tool_VoiceTranscriber_Verbose.height()+self.ui.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text.height()+self.ui.Frame_Tool_VoiceTranscriber_fp16.height(),0,'Reduce')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTranscriber_Model_Dir,
            Text = SetRichText(
                Title = "模型存放目录",
                Body = QCA.translate("Label", "该目录将会用于存放下载的语音识别模型，若模型已存在会直接使用。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_Model_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_Model_Dir,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_VoiceTranscriber_Model_Dir.setText(
            str(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Model_Dir', NormPath(Path(CurrentDir).joinpath('Download'), 'Posix')))
        )
        self.ui.LineEdit_Tool_VoiceTranscriber_Model_Dir.textChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'Model_Dir', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTranscriber_Model_Name,
            Text = SetRichText(
                Title = "模型名字",
                Body = QCA.translate("Label", "语音识别 (whisper) 模型的名字，默认代表模型的大小。")
            )
        )
        self.ui.ComboBox_Tool_VoiceTranscriber_Model_Name.addItems(['tiny', 'base', 'small', 'medium', 'large'])
        self.ui.ComboBox_Tool_VoiceTranscriber_Model_Name.setCurrentText(
            str(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Model_Name', 'small'))
        )
        self.ui.ComboBox_Tool_VoiceTranscriber_Model_Name.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'Model_Name', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTranscriber_Verbose,
            Text = SetRichText(
                Title = "启用输出日志",
                Body = QCA.translate("Label", "输出debug日志。")
            )
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_Verbose.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_Verbose.setChecked(
            eval(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Verbose', 'True'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTranscriber_Verbose,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            CheckedArgsList = [
                ('VoiceTranscriber', 'Verbose', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            UncheckedArgsList = [
                ('VoiceTranscriber', 'Verbose', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTranscriber_Condition_on_Previous_Text,
            Text = SetRichText(
                Title = "前后文一致",
                Body = QCA.translate("Label", "将模型之前的输出作为下个窗口的提示，若模型陷入了失败循环则禁用此项。")
            )
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setChecked(
            eval(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Condition_on_Previous_Text', 'False'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            CheckedArgsList = [
                ('VoiceTranscriber', 'Condition_on_Previous_Text', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            UncheckedArgsList = [
                ('VoiceTranscriber', 'Condition_on_Previous_Text', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTranscriber_fp16,
            Text = SetRichText(
                Title = "半精度计算",
                Body = QCA.translate("Label", "主要使用半精度浮点数进行计算，若GPU不可用则忽略或禁用此项。")
            )
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_fp16.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_fp16.setChecked(
            eval(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'fp16', 'True'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTranscriber_fp16,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            CheckedArgsList = [
                ('VoiceTranscriber', 'fp16', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            UncheckedArgsList = [
                ('VoiceTranscriber', 'fp16', 'False')
            ],
            TakeEffect = True
        )

        self.ui.GroupBox_OptionalParams_Tool_VoiceTranscriber.setTitle("可选参数")

        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber.setChecked(
            True #eval(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Toggle_BasicOptionalSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber,
            CheckedText = "基础设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceTranscriber.EditConfig
            ],
            CheckedArgsList = [
                (self.ui.Frame_BasicOptionalSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_Language.height(),0,'Extend'),
                #('VoiceTranscriber', 'Toggle_BasicOptionalSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceTranscriber.EditConfig
            ],
            UncheckedArgsList = [
                (self.ui.Frame_BasicOptionalSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_Language.height(),0,'Reduce'),
                #('VoiceTranscriber', 'Toggle_BasicOptionalSettings', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTranscriber_Language,
            Text = SetRichText(
                Title = "所用语言",
                Body = QCA.translate("Label", "音频中说话人所使用的语言，若自动检测则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Tool_VoiceTranscriber_Language.addItems(['中', '英', '日', 'None'])
        self.ui.ComboBox_Tool_VoiceTranscriber_Language.setCurrentText(
            str(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Language', 'None'))
        )
        self.ui.ComboBox_Tool_VoiceTranscriber_Language.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'Language', str(Value))
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_Tool_VoiceTranscriber,
            RootItemTexts = [self.ui.GroupBox_EssentialParams_Tool_VoiceTranscriber.title(),self.ui.GroupBox_OptionalParams_Tool_VoiceTranscriber.title()],
            ChildItemTexts = [(self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber.text(),self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber.text()),(self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber.text(),)],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceTranscriber.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_EssentialParams_Tool_VoiceTranscriber,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceTranscriber
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceTranscriber.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_BasicSettings_Tool_VoiceTranscriber,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceTranscriber
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceTranscriber.topLevelItem(0).child(1),
            TargetWidget = self.ui.Frame_AdvanceSettings_Tool_VoiceTranscriber,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceTranscriber
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceTranscriber.topLevelItem(1),
            TargetWidget = self.ui.GroupBox_OptionalParams_Tool_VoiceTranscriber,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceTranscriber
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceTranscriber.topLevelItem(1).child(0),
            TargetWidget = self.ui.Frame_BasicOptionalSettings_Tool_VoiceTranscriber,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceTranscriber
        )

        # Right
        MonitorFile_Config_VoiceTranscriber = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_Tool_VoiceTranscriber')
        )
        MonitorFile_Config_VoiceTranscriber.start()
        MonitorFile_Config_VoiceTranscriber.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Tool_VoiceTranscriber.setText(
                FileContent
            )
        )

        self.ui.Button_SyncParams_Tool_VoiceTranscriber.setText("关联参数设置")
        Function_ParamsSynchronizer(
            Trigger = self.ui.Button_SyncParams_Tool_VoiceTranscriber,
            ParamsFrom = [
                self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output
            ],
            ParamsTo = [
                self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir
            ]
        )

        self.ui.Button_CheckOutput_Tool_VoiceTranscriber.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Tool_VoiceTranscriber,
            URL = self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir,
            ButtonTooltip = "Click to open"
        )

        # Bottom
        self.ui.Button_Tool_VoiceTranscriber_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceTranscriber_Execute.setToolTip("执行语音转文字字幕")
        self.ui.Button_Tool_VoiceTranscriber_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceTranscriber_Terminate.setToolTip("终止语音转文字字幕")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Tool_VoiceTranscriber_Execute,
            TerminateButton = self.ui.Button_Tool_VoiceTranscriber_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_VoiceTranscriber,
            ConsoleFrame = self.ui.Frame_Console,
            Method = Execute_Voice_Transcribing.Execute,
            ParamsFrom = [
                self.ui.ComboBox_Tool_VoiceTranscriber_Model_Name,
                self.ui.LineEdit_Tool_VoiceTranscriber_Model_Dir,
                self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,
                self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir,
                self.ui.CheckBox_Tool_VoiceTranscriber_Verbose,
                'transcribe', #self.ui.ComboBox_Tool_VoiceTranscriber_Task
                self.ui.ComboBox_Tool_VoiceTranscriber_Language,
                self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text,
                self.ui.CheckBox_Tool_VoiceTranscriber_fp16
            ],
            EmptyAllowed = [
                self.ui.ComboBox_Tool_VoiceTranscriber_Language
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (QMessageBox.Question,"Ask","当前任务已执行结束，是否跳转至下一工具界面？",QMessageBox.Yes|QMessageBox.No,[QMessageBox.Yes],[[self.ui.Frame_Tools_Top.layout().itemAt(3).widget().click]],[[()]])
            ]
        )

        ##################### Tool_DatasetCreator #####################
        '''
        Function_SetText(
            Widget = self.ui.TextBrowser_Intro_Tool_DatasetCreator,
            Text = SetRichText(
                Title = QCA.translate("TextBrowser", "语音数据集制作"),
                TitleAlign = "center",
                TitleSize = 18,
                Body = QCA.translate("TextBrowser",
                    "\n"
                    "[介绍]\n"
                    "该工具会生成适用于语音模型训练的数据集。用户需要提供语音文件与对应的字幕文件\n"
                    "\n"
                    "[用法]\n"
                    "1. 设置页面右侧的参数\n"
                    "2. 点击位于页面底部的“执行”按钮\n"
                    "\n"
                    "[提示]\n"
                    "1. 您可以通过开启“自动同步...”选项以保持前后工具的部分参数设置一致，或者点击“同步...”按钮以快速设置当前工具的下列参数：\n"
                    "   WAV Dir\n"
                    "   SRT Dir\n"
                    "2. 您可以通过点击“打开输出文件”按钮以查看当前工具在执行完毕后输出的文件\n"
                )
            )
        )
        '''

        Path_Config_Tool_DatasetCreator = NormPath(Path(CurrentDir).joinpath('Config', 'Config_Tool_DatasetCreator.ini'))
        Config_Tool_DatasetCreator = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_Tool_DatasetCreator',
                Path_Config_Tool_DatasetCreator
            )
        )

        # Middle
        self.ui.GroupBox_EssentialParams_Tool_DatasetCreator.setTitle("必要参数")

        self.ui.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator.setChecked(
            True #eval(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator,
            CheckedText = "基础设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_DatasetCreator.EditConfig
            ],
            CheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_DatasetCreator,...,...,0,self.ui.Frame_Tool_DatasetCreator_WAV_Dir.height()+self.ui.Frame_Tool_DatasetCreator_SRT_Dir.height()+self.ui.Frame_Tool_DatasetCreator_ModelType.height()+self.ui.Frame_Tool_DatasetCreator_WAV_Dir_Split.height()+self.ui.Frame_Tool_DatasetCreator_FileList_Path_Training.height()+self.ui.Frame_Tool_DatasetCreator_FileList_Path_Validation.height(),0,'Extend'),
                #('DatasetCreator', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_DatasetCreator.EditConfig
            ],
            UncheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_DatasetCreator,...,...,0,self.ui.Frame_Tool_DatasetCreator_WAV_Dir.height()+self.ui.Frame_Tool_DatasetCreator_SRT_Dir.height()+self.ui.Frame_Tool_DatasetCreator_ModelType.height()+self.ui.Frame_Tool_DatasetCreator_WAV_Dir_Split.height()+self.ui.Frame_Tool_DatasetCreator_FileList_Path_Training.height()+self.ui.Frame_Tool_DatasetCreator_FileList_Path_Validation.height(),0,'Reduce'),
                #('DatasetCreator', 'Toggle_BasicSettings', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_DatasetCreator_WAV_Dir,
            Text = SetRichText(
                Title = "音频输入目录",
                Body = QCA.translate("Label", "该目录中的wav文件将会按照以下设置重采样并根据字幕时间戳进行分割。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_WAV_Dir,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,
            Text = str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'WAV_Dir', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir.textChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'WAV_Dir', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_DatasetCreator_SRT_Dir,
            Text = SetRichText(
                Title = "字幕输入目录",
                Body = QCA.translate("Label", "该目录中的srt文件将会按照以下设置转为适用于模型训练的csv文件。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_SRT_Dir,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir,
            Text = str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'SRT_Dir', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir.textChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'SRT_Dir', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_DatasetCreator_ModelType,
            Text = SetRichText(
                Title = "模型类别",
                Body = QCA.translate("Label", "数据集适用的模型类别。")
            )
        )
        self.ui.ComboBox_Tool_DatasetCreator_ModelType.addItems(['VITS'])
        self.ui.ComboBox_Tool_DatasetCreator_ModelType.setCurrentText(
            str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'ModelType', 'VITS'))
        )
        self.ui.ComboBox_Tool_DatasetCreator_ModelType.currentTextChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'ModelType', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_DatasetCreator_WAV_Dir_Split,
            Text = SetRichText(
                Title = "音频输出目录",
                Body = QCA.translate("Label", "最后处理完成的音频将会保存到该目录中。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_WAV_Dir_Split,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir_Split,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir_Split,
            Text = str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'WAV_Dir_Split', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir_Split.textChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'WAV_Dir_Split', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_DatasetCreator_FileList_Path_Training,
            Text = SetRichText(
                Title = "训练集文本路径",
                Body = QCA.translate("Label", "最后生成的训练集txt文件将会保存到该路径。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_FileList_Path_Training,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
            Mode = "SaveFile",
            FileType = "txt类型 (*.txt)"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
            Text = str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'FileList_Path_Training', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training.textChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'FileList_Path_Training', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_DatasetCreator_FileList_Path_Validation,
            Text = SetRichText(
                Title = "验证集文本路径",
                Body = QCA.translate("Label", "最后生成的验证集txt文件将会保存到该路径。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_FileList_Path_Validation,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation,
            Mode = "SaveFile",
            FileType = "txt类型 (*.txt)"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation,
            Text = str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'FileList_Path_Validation', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation.textChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'FileList_Path_Validation', str(Value))
        )

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator,
            CheckedText = "高级设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame
            ],
            CheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_DatasetCreator,...,...,0,self.ui.Frame_Tool_DatasetCreator_SampleRate.height()+self.ui.Frame_Tool_DatasetCreator_SampleWidth.height()+self.ui.Frame_Tool_DatasetCreator_ToMono.height()+self.ui.Frame_Tool_DatasetCreator_TrainRatio.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_DatasetCreator,...,...,0,self.ui.Frame_Tool_DatasetCreator_SampleRate.height()+self.ui.Frame_Tool_DatasetCreator_SampleWidth.height()+self.ui.Frame_Tool_DatasetCreator_ToMono.height()+self.ui.Frame_Tool_DatasetCreator_TrainRatio.height(),0,'Reduce')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_DatasetCreator_SampleRate,
            Text = SetRichText(
                Title = "采样率 (HZ)",
                Body = QCA.translate("Label", "数据集所要求的音频采样率，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Tool_DatasetCreator_SampleRate.addItems(['22050', '44100', '48000', '96000', '192000', 'None'])
        self.ui.ComboBox_Tool_DatasetCreator_SampleRate.setCurrentText(
            str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'SampleRate', '22050'))
        )
        self.ui.ComboBox_Tool_DatasetCreator_SampleRate.currentTextChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'SampleRate', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_DatasetCreator_SampleWidth,
            Text = SetRichText(
                Title = "采样位数",
                Body = QCA.translate("Label", "数据集所要求的音频采样位数，若维持不变则保持'None'即可。")
            )
        )
        self.ui.ComboBox_Tool_DatasetCreator_SampleWidth.addItems(['8', '16', '24', '32', '32 (Float)', 'None'])
        self.ui.ComboBox_Tool_DatasetCreator_SampleWidth.setCurrentText(
            str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'SampleWidth', '16'))
        )
        self.ui.ComboBox_Tool_DatasetCreator_SampleWidth.currentTextChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'SampleWidth', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_DatasetCreator_ToMono,
            Text = SetRichText(
                Title = "合并声道",
                Body = QCA.translate("Label", "将数据集音频的声道合并为单声道。")
            )
        )
        self.ui.CheckBox_Tool_DatasetCreator_ToMono.setCheckable(True)
        self.ui.CheckBox_Tool_DatasetCreator_ToMono.setChecked(
            eval(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'ToMono', 'True'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_DatasetCreator_ToMono,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Tool_DatasetCreator.EditConfig
            ],
            CheckedArgsList = [
                ('DatasetCreator', 'ToMono', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Tool_DatasetCreator.EditConfig
            ],
            UncheckedArgsList = [
                ('DatasetCreator', 'ToMono', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_DatasetCreator_TrainRatio,
            Text = SetRichText(
                Title = "训练集占比",
                Body = QCA.translate("Label", "划分给训练集的数据在数据集中所占的比例。")
            )
        )
        self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setRange(0.5, 0.9)
        self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setSingleStep(0.1)
        self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setValue(
            float(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'TrainRatio', '0.7'))
        )
        self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.valueChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'TrainRatio', str(Value))
        )

        self.ui.GroupBox_OptionalParams_Tool_DatasetCreator.setTitle("可选参数")

        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_DatasetCreator.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_DatasetCreator.setChecked(
            True #eval(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'Toggle_BasicOptionalSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_DatasetCreator,
            CheckedText = "基础设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_DatasetCreator.EditConfig
            ],
            CheckedArgsList = [
                (self.ui.Frame_BasicOptionalSettings_Tool_DatasetCreator,...,...,0,self.ui.Frame_Tool_DatasetCreator_AuxiliaryData_Path.height(),0,'Extend'),
                #('DatasetCreator', 'Toggle_BasicOptionalSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_DatasetCreator.EditConfig
            ],
            UncheckedArgsList = [
                (self.ui.Frame_BasicOptionalSettings_Tool_DatasetCreator,...,...,0,self.ui.Frame_Tool_DatasetCreator_AuxiliaryData_Path.height(),0,'Reduce'),
                #('DatasetCreator', 'Toggle_BasicOptionalSettings', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_DatasetCreator_AuxiliaryData_Path,
            Text = SetRichText(
                Title = "辅助数据文本路径",
                Body = QCA.translate("Label", "辅助数据集的文本的所在路径。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_AuxiliaryData_Path,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_AuxiliaryData_Path,
            Mode = "SelectFile",
            FileType = "文本类型 (*.csv *.txt)"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_DatasetCreator_AuxiliaryData_Path,
            Text = str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'AuxiliaryData_Path', NormPath(Path(CurrentDir).joinpath('AuxiliaryData', 'AuxiliaryData.txt')) if Path(CurrentDir).joinpath('AuxiliaryData', 'AuxiliaryData.txt').exists() else '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_DatasetCreator_AuxiliaryData_Path.textChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'AuxiliaryData_Path', str(Value))
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_Tool_DatasetCreator,
            RootItemTexts = [self.ui.GroupBox_EssentialParams_Tool_DatasetCreator.title(),self.ui.GroupBox_OptionalParams_Tool_DatasetCreator.title()],
            ChildItemTexts = [(self.ui.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator.text(),self.ui.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator.text()),(self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_DatasetCreator.text(),)],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_DatasetCreator.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_EssentialParams_Tool_DatasetCreator,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_DatasetCreator
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_DatasetCreator.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_BasicSettings_Tool_DatasetCreator,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_DatasetCreator
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_DatasetCreator.topLevelItem(0).child(1),
            TargetWidget = self.ui.Frame_AdvanceSettings_Tool_DatasetCreator,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_DatasetCreator
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_DatasetCreator.topLevelItem(1),
            TargetWidget = self.ui.GroupBox_OptionalParams_Tool_DatasetCreator,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_DatasetCreator
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_DatasetCreator.topLevelItem(1).child(0),
            TargetWidget = self.ui.Frame_BasicOptionalSettings_Tool_DatasetCreator,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_DatasetCreator
        )

        # Right
        MonitorFile_Config_DatasetCreator = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_Tool_DatasetCreator')
        )
        MonitorFile_Config_DatasetCreator.start()
        MonitorFile_Config_DatasetCreator.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Tool_DatasetCreator.setText(
                FileContent
            )
        )

        self.ui.Button_SyncParams_Tool_DatasetCreator.setText("关联参数设置")
        Function_ParamsSynchronizer(
            Trigger = self.ui.Button_SyncParams_Tool_DatasetCreator,
            ParamsFrom = [
                self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir, #self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output
                self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir
            ],
            ParamsTo = [
                self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,
                self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir
            ]
        )

        self.ui.Button_CheckOutput_Tool_DatasetCreator.setText(QCA.translate("Button", "打开输出文件"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Tool_DatasetCreator,
            URL = [
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation
            ],
            ButtonTooltip = "Click to open"
        )

        # Bottom
        self.ui.Button_Tool_DatasetCreator_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_DatasetCreator_Execute.setToolTip("执行语音数据集制作")
        self.ui.Button_Tool_DatasetCreator_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_DatasetCreator_Terminate.setToolTip("终止语音数据集制作")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Tool_DatasetCreator_Execute,
            TerminateButton = self.ui.Button_Tool_DatasetCreator_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_DatasetCreator,
            ConsoleFrame = self.ui.Frame_Console,
            Method = Execute_Dataset_Creating.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir,
                self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,
                self.ui.ComboBox_Tool_DatasetCreator_SampleRate,
                self.ui.ComboBox_Tool_DatasetCreator_SampleWidth,
                self.ui.CheckBox_Tool_DatasetCreator_ToMono,
                self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir_Split,
                self.ui.LineEdit_Tool_DatasetCreator_AuxiliaryData_Path,
                self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio,
                self.ui.ComboBox_Tool_DatasetCreator_ModelType,
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation
            ],
            EmptyAllowed = [
                self.ui.ComboBox_Tool_DatasetCreator_SampleRate,
                self.ui.ComboBox_Tool_DatasetCreator_SampleWidth,
                self.ui.LineEdit_Tool_DatasetCreator_AuxiliaryData_Path
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (QMessageBox.Question,"Ask","当前任务已执行结束，是否跳转至下一工具界面？",QMessageBox.Yes|QMessageBox.No,[QMessageBox.Yes],[[self.ui.Frame_Tools_Top.layout().itemAt(4).widget().click]],[[()]])
            ]
        )

        ##################### Tool_VoiceTrainer #####################
        '''
        Function_SetText(
            Widget = self.ui.TextBrowser_Intro_Tool_VoiceTrainer,
            Text = SetRichText(
                Title = QCA.translate("TextBrowser", "语音模型训练"),
                TitleAlign = "center",
                TitleSize = 18,
                Body = QCA.translate("TextBrowser",
                    "\n"
                    "[介绍]\n"
                    "该工具会训练出适用于语音合成的模型文件。用户需要提供语音数据集\n"
                    "\n"
                    "[用法]\n"
                    "1. 设置页面右侧的参数\n"
                    "2. 点击位于页面底部的“执行”按钮\n"
                    "3. 执行过程中若要查看迭代轮数，请见系统的命令行窗口\n"
                    "\n"
                    "[提示]\n"
                    "1. 您可以通过开启“自动同步...”选项以保持前后工具的部分参数设置一致，或者点击“同步...”按钮以快速设置当前工具的下列参数：\n"
                    "   FileList Path Training\n"
                    "   FileList Path Validation\n"
                    "2. 您可以通过点击“打开输出目录”按钮以查看当前工具在执行完毕后输出的文件\n"
                )
            )
        )
        '''

        Path_Config_Tool_VoiceTrainer = NormPath(Path(CurrentDir).joinpath('Config', 'Config_Tool_VoiceTrainer.ini'))
        Config_Tool_VoiceTrainer = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_Tool_VoiceTrainer',
                Path_Config_Tool_VoiceTrainer
            )
        )

        # Midlle
        self.ui.GroupBox_EssentialParams_Tool_VoiceTrainer.setTitle("必要参数")

        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer.setChecked(
            True #eval(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer,
            CheckedText = "基础设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceTrainer.EditConfig
            ],
            CheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_FileList_Path_Training.height()+self.ui.Frame_Tool_VoiceTrainer_FileList_Path_Validation.height()+self.ui.Frame_Tool_VoiceTrainer_Epochs.height()+self.ui.Frame_Tool_VoiceTrainer_Batch_Size.height()+self.ui.Frame_Tool_VoiceTrainer_Config_Dir_Save.height()+self.ui.Frame_Tool_VoiceTrainer_Model_Dir_Save.height(),0,'Extend'),
                #('VoiceTrainer', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceTrainer.EditConfig
            ],
            UncheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_FileList_Path_Training.height()+self.ui.Frame_Tool_VoiceTrainer_FileList_Path_Validation.height()+self.ui.Frame_Tool_VoiceTrainer_Epochs.height()+self.ui.Frame_Tool_VoiceTrainer_Batch_Size.height()+self.ui.Frame_Tool_VoiceTrainer_Config_Dir_Save.height()+self.ui.Frame_Tool_VoiceTrainer_Model_Dir_Save.height(),0,'Reduce'),
                #('VoiceTrainer', 'Toggle_BasicSettings', 'False')
            ],
            TakeEffect = True
        )
        
        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_FileList_Path_Training,
            Text = SetRichText(
                Title = "训练集文本路径",
                Body = QCA.translate("Label", "用于提供训练集音频路径及其语音内容的训练集txt文件的所在路径。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_FileList_Path_Training,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,
            Text = str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'FileList_Path_Training', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'FileList_Path_Training', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_FileList_Path_Validation,
            Text = SetRichText(
                Title = "验证集文本路径",
                Body = QCA.translate("Label", "用于提供验证集音频路径及其语音内容的验证集txt文件的所在路径。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_FileList_Path_Validation,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation,
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation,
            Text = str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'FileList_Path_Validation', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'FileList_Path_Validation', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_Epochs,
            Text = SetRichText(
                Title = "迭代轮数",
                Body = QCA.translate("Label", "将全部样本完整迭代一轮的次数。")
            )
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setRange(30, 300000)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setValue(
            int(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Epochs', '100'))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.valueChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Epochs', str(Value))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setToolTip("提示：在均没有预训练模型与辅助数据的情况下建议从一万轮次起步")

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_Batch_Size,
            Text = SetRichText(
                Title = "批处理量",
                Body = QCA.translate("Label", "每轮迭代中单位批次的样本数量，需根据GPU的性能调节该值。")
            )
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setRange(2, 128)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setValue(
            int(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Batch_Size', '4'))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.valueChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Batch_Size', str(Value))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setToolTip("建议：4~6G: 2; 8~10G: 4; 12~14G: 8; ...")

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_Config_Dir_Save,
            Text = SetRichText(
                Title = "配置保存目录",
                Body = QCA.translate("Label", "根据以上设置更新参数后的配置文件的保存目录。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Config_Dir_Save,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Config_Dir_Save,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceTrainer_Config_Dir_Save,
            Text = str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Config_Dir_Save', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Config_Dir_Save.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Config_Dir_Save', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save,
            Text = SetRichText(
                Title = "模型保存目录",
                Body = QCA.translate("Label", "训练得到的模型的存放目录，若目录中已存在模型则会将其视为检查点。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Dir_Save,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save,
            Text = str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Model_Dir_Save', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Model_Dir_Save', str(Value))
        )
        self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save.setToolTipDuration(-1)
        self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save.setToolTip("提示：当目录中存在多个模型时，编号最大的那个会被选为检查点。")

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer,
            CheckedText = "高级设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame
            ],
            CheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Eval_Interval.height()+self.ui.Frame_Tool_VoiceTrainer_Num_Workers.height()+self.ui.Frame_Tool_VoiceTrainer_FP16_Run.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Eval_Interval.height()+self.ui.Frame_Tool_VoiceTrainer_Num_Workers.height()+self.ui.Frame_Tool_VoiceTrainer_FP16_Run.height(),0,'Reduce')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_Eval_Interval,
            Text = SetRichText(
                Title = "评估间隔",
                Body = QCA.translate("Label", "每次保存模型所间隔的步数。PS: 步数 ≈ 迭代轮次 * 训练样本数 / 批处理量")
            )
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setRange(300, 3000000)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setValue(
            int(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Eval_Interval', '1000'))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.valueChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Eval_Interval', str(Value))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setToolTip("提示：设置过小可能导致磁盘占用激增哦")

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_Num_Workers,
            Text = SetRichText(
                Title = "进程数量",
                Body = QCA.translate("Label", "进行数据加载时可并行的进程数量，需根据CPU的性能调节该值。")
            )
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.setRange(2, 32)
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.setSingleStep(2)
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.setValue(
            int(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Num_Workers', '4'))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.valueChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Num_Workers', str(Value))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.setToolTip("提示：如果配置属于低U高显的话不妨试试把数值降到2。")

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_FP16_Run,
            Text = SetRichText(
                Title = "半精度训练",
                Body = QCA.translate("Label", "通过混合了float16精度的训练方式减小显存占用以支持更大的批处理量。")
            )
        )
        self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run.setChecked(
            eval(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'FP16_Run', 'True'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Tool_VoiceTrainer.EditConfig
            ],
            CheckedArgsList = [
                ('VoiceTrainer', 'FP16_Run', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Tool_VoiceTrainer.EditConfig
            ],
            UncheckedArgsList = [
                ('VoiceTrainer', 'FP16_Run', 'False')
            ],
            TakeEffect = True
        )

        self.ui.GroupBox_OptionalParams_Tool_VoiceTrainer.setTitle("可选参数")

        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer.setChecked(
            True #eval(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Toggle_BasicOptionalSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer,
            CheckedText = "基础设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceTrainer.EditConfig
            ],
            CheckedArgsList = [
                (self.ui.Frame_BasicOptionalSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G.height()+self.ui.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D.height()+self.ui.Frame_Tool_VoiceTrainer_Config_Path_Load.height()+self.ui.Frame_Tool_VoiceTrainer_Keep_Original_Speakers.height(),0,'Extend'),
                #('VoiceTrainer', 'Toggle_BasicOptionalSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceTrainer.EditConfig
            ],
            UncheckedArgsList = [
                (self.ui.Frame_BasicOptionalSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G.height()+self.ui.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D.height()+self.ui.Frame_Tool_VoiceTrainer_Config_Path_Load.height()+self.ui.Frame_Tool_VoiceTrainer_Keep_Original_Speakers.height(),0,'Reduce'),
                #('VoiceTrainer', 'Toggle_BasicOptionalSettings', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            Text = SetRichText(
                Title = "预训练G_*模型路径",
                Body = QCA.translate("Label", "预训练生成器（Generator）模型的所在路径，载入优先级高于检查点。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            Text = str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Model_Path_Pretrained_G', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Model_Path_Pretrained_G', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            Text = SetRichText(
                Title = "预训练D_*模型路径",
                Body = QCA.translate("Label", "预训练判别器（Discriminator）模型的所在路径，载入优先级高于检查点。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            Text = str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Model_Path_Pretrained_D', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Model_Path_Pretrained_D', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_Config_Path_Load,
            Text = SetRichText(
                Title = "配置路径",
                Body = QCA.translate("Label", "用于加载人物等信息的配置文件的所在路径，载入优先级高于默认配置文件。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Config_Path_Load,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load,
            Mode = "SelectFile",
            FileType = "json类型 (*.json)"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load,
            Text = str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Config_Path_Load', '')),
            SetPlaceholderText = True,
            PlaceholderText = '保持空值将使用不含人物信息的默认配置'
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Config_Path_Load', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_Keep_Original_Speakers,
            Text = SetRichText(
                Title = "保留原说话人",
                Body = QCA.translate("Label", "保留底模中原有的说话人，需要设置相应的配置路径才能生效。")
            )
        )
        self.ui.CheckBox_Tool_VoiceTrainer_Keep_Original_Speakers.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTrainer_Keep_Original_Speakers.setChecked(
            eval(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Keep_Original_Speakers', 'False'))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTrainer_Keep_Original_Speakers,
            CheckedText = "已启用",
            CheckedEventList = [
                Config_Tool_VoiceTrainer.EditConfig
            ],
            CheckedArgsList = [
                ('VoiceTrainer', 'Keep_Original_Speakers', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedEventList = [
                Config_Tool_VoiceTrainer.EditConfig
            ],
            UncheckedArgsList = [
                ('VoiceTrainer', 'Keep_Original_Speakers', 'False')
            ],
            TakeEffect = True
        )

        self.ui.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer,
            CheckedText = "高级设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame
            ],
            CheckedArgsList = [
                (self.ui.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Speakers.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (self.ui.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Speakers.height(),0,'Reduce')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceTrainer_Speakers,
            Text = SetRichText(
                Title = "人物名字",
                Body = QCA.translate("Label", "若数据集使用的是人物编号而非人物名字，则在此处按编号填写名字并用逗号隔开。")
            )
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setReadOnly(False)
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceTrainer_Speakers,
            Text = str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Speakers', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Speakers', str(Value))
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setToolTipDuration(-1)
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setToolTip("注意：逗号后面不需要加空格")

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_Tool_VoiceTrainer,
            RootItemTexts = [self.ui.GroupBox_EssentialParams_Tool_VoiceTrainer.title(),self.ui.GroupBox_OptionalParams_Tool_VoiceTrainer.title()],
            ChildItemTexts = [(self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer.text(),self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer.text()),(self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer.text(),self.ui.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer.text())],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceTrainer.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_EssentialParams_Tool_VoiceTrainer,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceTrainer
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceTrainer.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_BasicSettings_Tool_VoiceTrainer,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceTrainer
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceTrainer.topLevelItem(0).child(1),
            TargetWidget = self.ui.Frame_AdvanceSettings_Tool_VoiceTrainer,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceTrainer
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceTrainer.topLevelItem(1),
            TargetWidget = self.ui.GroupBox_OptionalParams_Tool_VoiceTrainer,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceTrainer
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceTrainer.topLevelItem(1).child(0),
            TargetWidget = self.ui.Frame_BasicOptionalSettings_Tool_VoiceTrainer,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceTrainer
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceTrainer.topLevelItem(1).child(1),
            TargetWidget = self.ui.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceTrainer
        )

        # Right
        MonitorFile_Config_VoiceTrainer = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_Tool_VoiceTrainer')
        )
        MonitorFile_Config_VoiceTrainer.start()
        MonitorFile_Config_VoiceTrainer.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Tool_VoiceTrainer.setText(
                FileContent
            )
        )

        self.ui.Button_RunTensorboard_Tool_VoiceTrainer.setText("启动Tensorboard")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_RunTensorboard_Tool_VoiceTrainer,
            Method = Tensorboard_Runner.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save
            ]
        )

        self.ui.Button_SyncParams_Tool_VoiceTrainer.setText("关联参数设置")
        Function_ParamsSynchronizer(
            Trigger = self.ui.Button_SyncParams_Tool_VoiceTrainer,
            ParamsFrom = [
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation
            ],
            ParamsTo = [
                self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,
                self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation
            ]
        )

        self.ui.Button_CheckOutput_Tool_VoiceTrainer.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Tool_VoiceTrainer,
            URL = [
                self.ui.LineEdit_Tool_VoiceTrainer_Config_Dir_Save,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save
            ],
            ButtonTooltip = "Click to open"
        )

        # Bottom
        self.ui.Button_Tool_VoiceTrainer_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceTrainer_Execute.setToolTip("执行语音模型训练")
        self.ui.Button_Tool_VoiceTrainer_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceTrainer_Terminate.setToolTip("终止语音模型训练")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Tool_VoiceTrainer_Execute,
            TerminateButton = self.ui.Button_Tool_VoiceTrainer_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_VoiceTrainer,
            ConsoleFrame = self.ui.Frame_Console,
            Method = Execute_Voice_Training.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,
                self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation,
                self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load,
                self.ui.LineEdit_Tool_VoiceTrainer_Config_Dir_Save,
                self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval,
                self.ui.SpinBox_Tool_VoiceTrainer_Epochs,
                self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size,
                self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run,
                self.ui.LineEdit_Tool_VoiceTrainer_Speakers,
                self.ui.CheckBox_Tool_VoiceTrainer_Keep_Original_Speakers,
                self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save
            ],
            EmptyAllowed = [
                self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D,
                self.ui.LineEdit_Tool_VoiceTrainer_Speakers
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (QMessageBox.Question,"Ask","当前任务已执行结束，是否跳转至下一工具界面？",QMessageBox.Yes|QMessageBox.No,[QMessageBox.Yes],[[self.ui.Frame_Tools_Top.layout().itemAt(5).widget().click]],[[()]])
            ]
        )
        MainWindowSignals.Signal_TaskStatus.connect(
            lambda Task, Status: Function_ShowMessageBox(
                MessageType = QMessageBox.Question,
                WindowTitle = "Ask",
                Text = "是否稍后启用tensorboard？",
                Buttons = QMessageBox.Yes|QMessageBox.No,
                EventButtons = [QMessageBox.Yes],
                EventLists = [[self.ui.Button_RunTensorboard_Tool_VoiceTrainer.click]],
                ParamLists = [[()]]
            ) if Task == 'Execute_Voice_Training.Execute' and Status == 'Started' else None
        )

        ##################### Tool_VoiceConverter #####################
        '''
        Function_SetText(
            Widget = self.ui.TextBrowser_Intro_Tool_VoiceConverter,
            Text = SetRichText(
                Title = QCA.translate("TextBrowser", "语音模型推理"),
                TitleAlign = "center",
                TitleSize = 18,
                Body = QCA.translate("TextBrowser",
                    "\n"
                    "[介绍]\n"
                    "该工具会将文字转为语音并生成音频文件。用户需要提供相应的模型和配置文件\n"
                    "\n"
                    "[用法]\n"
                    "1. 设置页面右侧的参数\n"
                    "2. 点击位于页面底部的“执行”按钮\n"
                    "3. 执行过程中若要查看推理情况，请见系统的命令行窗口\n"
                    "\n"
                    "[提示]\n"
                    "1. 您可以通过点击“打开输出目录”按钮以查看当前工具在执行完毕后输出的文件\n"
                )
            )
        )
        '''

        Path_Config_Tool_VoiceConverter = NormPath(Path(CurrentDir).joinpath('Config', 'Config_Tool_VoiceConverter.ini'))
        Config_Tool_VoiceConverter = ManageConfig(
            Config.GetValue(
                'ConfigPath',
                'Path_Config_Tool_VoiceConverter',
                Path_Config_Tool_VoiceConverter
            )
        )

        # Middle
        self.ui.GroupBox_EssentialParams_Tool_VoiceConverter.setTitle(QCA.translate("GroupBox", "必要参数"))

        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter.setChecked(
            True #eval(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter,
            CheckedText = "基础设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceConverter.EditConfig
            ],
            CheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceConverter,...,...,0,self.ui.Frame_Tool_VoiceConverter_Config_Path_Load.height()+self.ui.Frame_Tool_VoiceConverter_Model_Path_Load.height()+self.ui.Frame_Tool_VoiceConverter_Text.height()+self.ui.Frame_Tool_VoiceConverter_Language.height()+self.ui.Frame_Tool_VoiceConverter_Speaker.height()+self.ui.Frame_Tool_VoiceConverter_Audio_Dir_Save.height(),0,'Extend'),
                #('VoiceConverter', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame,
                #Config_Tool_VoiceConverter.EditConfig
            ],
            UncheckedArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceConverter,...,...,0,self.ui.Frame_Tool_VoiceConverter_Config_Path_Load.height()+self.ui.Frame_Tool_VoiceConverter_Model_Path_Load.height()+self.ui.Frame_Tool_VoiceConverter_Text.height()+self.ui.Frame_Tool_VoiceConverter_Language.height()+self.ui.Frame_Tool_VoiceConverter_Speaker.height()+self.ui.Frame_Tool_VoiceConverter_Audio_Dir_Save.height(),0,'Reduce'),
                #('VoiceConverter', 'Toggle_BasicSettings', 'False')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceConverter_Config_Path_Load,
            Text = SetRichText(
                Title = "配置加载路径",
                Body = QCA.translate("Label", "用于推理的配置文件的所在路径。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceConverter_Config_Path_Load,
            LineEdit = self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load,
            Mode = "SelectFile",
            FileType = "json类型 (*.json)"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load,
            Text = str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Config_Path_Load', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load.textChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'Config_Path_Load', str(Value))
        )
        self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load.textChanged.connect(
            lambda: self.ui.ComboBox_Tool_VoiceConverter_Speaker.clear(),
            type = Qt.QueuedConnection
        )
        self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load.textChanged.connect(
            lambda Path: self.ui.ComboBox_Tool_VoiceConverter_Speaker.addItems(
                Get_Speakers(Path)
            ),
            type = Qt.QueuedConnection
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceConverter_Model_Path_Load,
            Text = SetRichText(
                Title = "G_*模型加载路径",
                Body = QCA.translate("Label", "用于推理的生成器（Generator）模型的所在路径。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceConverter_Model_Path_Load,
            LineEdit = self.ui.LineEdit_Tool_VoiceConverter_Model_Path_Load,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceConverter_Model_Path_Load,
            Text = str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Model_Path_Load', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceConverter_Model_Path_Load.textChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'Model_Path_Load', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceConverter_Text,
            Text = SetRichText(
                Title = "输入文字",
                Body = QCA.translate("Label", "输入的文字会作为说话人的语音内容。")
            )
        )
        Function_SetText(
            Widget = self.ui.PlainTextEdit_Tool_VoiceConverter_Text,
            Text = str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Text', '')),
            SetPlaceholderText = True,
            PlaceholderText = '请输入语句'
        )
        self.ui.PlainTextEdit_Tool_VoiceConverter_Text.textChanged.connect(
            lambda: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'Text', self.ui.PlainTextEdit_Tool_VoiceConverter_Text.toPlainText())
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceConverter_Language,
            Text = SetRichText(
                Title = "所用语言",
                Body = QCA.translate("Label", "说话人/文字所使用的语言。")
            )
        )
        self.ui.ComboBox_Tool_VoiceConverter_Language.addItems(['中', '英', '日'])
        self.ui.ComboBox_Tool_VoiceConverter_Language.setCurrentText(
            str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Language', '中'))
        )
        self.ui.ComboBox_Tool_VoiceConverter_Language.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'Language', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceConverter_Speaker,
            Text = SetRichText(
                Title = "人物名字",
                Body = QCA.translate("Label", "说话人物的名字。")
            )
        )
        self.ui.ComboBox_Tool_VoiceConverter_Speaker.addItems(
            Get_Speakers(str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Config_Path_Load', 'None')))
        )
        self.ui.ComboBox_Tool_VoiceConverter_Speaker.setCurrentText(
            str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Speaker', '')) if str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Speaker', '')) in Get_Speakers(str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Config_Path_Load', 'None')))
            else (Get_Speakers(str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Config_Path_Load', 'None')))[0] if Get_Speakers(str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Config_Path_Load', 'None'))) != '' else '')
        )
        self.ui.ComboBox_Tool_VoiceConverter_Speaker.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'Speaker', str(Value))
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceConverter_Audio_Dir_Save,
            Text = SetRichText(
                Title = "音频保存目录",
                Body = QCA.translate("Label", "推理得到的音频会保存到该目录。")
            )
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceConverter_Audio_Dir_Save,
            LineEdit = self.ui.LineEdit_Tool_VoiceConverter_Audio_Dir_Save,
            Mode = "SelectDir"
        )
        Function_SetText(
            Widget = self.ui.LineEdit_Tool_VoiceConverter_Audio_Dir_Save,
            Text = str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Audio_Dir_Save', '')),
            SetPlaceholderText = True
        )
        self.ui.LineEdit_Tool_VoiceConverter_Audio_Dir_Save.textChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'Audio_Dir_Save', str(Value))
        )

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter,
            CheckedText = "高级设置（显示）",
            CheckedEventList = [
                self.Function_AnimateFrame
            ],
            CheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceConverter,...,...,0,self.ui.Frame_Tool_VoiceConverter_EmotionStrength.height()+self.ui.Frame_Tool_VoiceConverter_PhonemeDuration.height()+self.ui.Frame_Tool_VoiceConverter_SpeechRate.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedEventList = [
                self.Function_AnimateFrame
            ],
            UncheckedArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceConverter,...,...,0,self.ui.Frame_Tool_VoiceConverter_EmotionStrength.height()+self.ui.Frame_Tool_VoiceConverter_PhonemeDuration.height()+self.ui.Frame_Tool_VoiceConverter_SpeechRate.height(),0,'Reduce')
            ],
            TakeEffect = True
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceConverter_EmotionStrength,
            Text = SetRichText(
                Title = "情感强度",
                Body = QCA.translate("Label", "情感的变化程度。")
            )
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setMinimum(0)
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setMaximum(100)
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setTickInterval(1)
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setValue(
            int(float(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'EmotionStrength', '0.67')) * 100)
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.valueChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'EmotionStrength', str(Value * 0.01))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength,
            ParamsFrom = [
                self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength
            ],
            Times = 0.01,
            ParamsTo = [
                self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength
            ]
        )
        self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength.setRange(0, 1)
        self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength.setValue(
            float(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'EmotionStrength', '0.67'))
        )
        self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength.valueChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'EmotionStrength', str(Value))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength,
            ParamsFrom = [
                self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength
            ],
            Times = 100,
            ParamsTo = [
                self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength
            ]
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceConverter_PhonemeDuration,
            Text = SetRichText(
                Title = "音素音长",
                Body = QCA.translate("Label", "音素的发音长度。")
            )
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setMinimum(0)
        self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setMaximum(10)
        self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setTickInterval(1)
        self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setValue(
            int(float(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'PhonemeDuration', '0.8')) * 10)
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.valueChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'PhonemeDuration', str(Value * 0.1))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration,
            ParamsFrom = [
                self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration
            ],
            Times = 0.1,
            ParamsTo = [
                self.ui.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration
            ]
        )
        self.ui.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration.setRange(0, 1)
        self.ui.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration.setSingleStep(0.1)
        self.ui.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration.setValue(
            float(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'PhonemeDuration', '0.8'))
        )
        self.ui.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration.valueChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'PhonemeDuration', str(Value))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration,
            ParamsFrom = [
                self.ui.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration
            ],
            Times = 10,
            ParamsTo = [
                self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration
            ]
        )

        Function_SetText(
            Widget = self.ui.Label_Tool_VoiceConverter_SpeechRate,
            Text = SetRichText(
                Title = "整体语速",
                Body = QCA.translate("Label", "整体的说话速度。")
            )
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setMinimum(0)
        self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setMaximum(20)
        self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setTickInterval(1)
        self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setValue(
            int(float(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'SpeechRate', '1.')) * 10)
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate.valueChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'SpeechRate', str(Value * 0.1))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate,
            ParamsFrom = [
                self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate
            ],
            Times = 0.1,
            ParamsTo = [
                self.ui.DoubleSpinBox_Tool_VoiceConverter_SpeechRate
            ]
        )
        self.ui.DoubleSpinBox_Tool_VoiceConverter_SpeechRate.setRange(0, 2)
        self.ui.DoubleSpinBox_Tool_VoiceConverter_SpeechRate.setSingleStep(0.1)
        self.ui.DoubleSpinBox_Tool_VoiceConverter_SpeechRate.setValue(
            float(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'SpeechRate', '1.'))
        )
        self.ui.DoubleSpinBox_Tool_VoiceConverter_SpeechRate.valueChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'SpeechRate', str(Value))
        )
        Function_ParamsSynchronizer(
            Trigger = self.ui.DoubleSpinBox_Tool_VoiceConverter_SpeechRate,
            ParamsFrom = [
                self.ui.DoubleSpinBox_Tool_VoiceConverter_SpeechRate
            ],
            Times = 10,
            ParamsTo = [
                self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate
            ]
        )

        # Right
        MonitorFile_Config_VoiceConverter = MonitorFile(
            Config.GetValue('ConfigPath', 'Path_Config_Tool_VoiceConverter')
        )
        MonitorFile_Config_VoiceConverter.start()
        MonitorFile_Config_VoiceConverter.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Tool_VoiceConverter.setText(
                FileContent
            )
        )

        self.ui.Button_CheckOutput_Tool_VoiceConverter.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Tool_VoiceConverter,
            URL = self.ui.LineEdit_Tool_VoiceConverter_Audio_Dir_Save,
            ButtonTooltip = "Click to open"
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_Tool_VoiceConverter,
            RootItemTexts = [self.ui.GroupBox_EssentialParams_Tool_VoiceConverter.title()],
            ChildItemTexts = [(self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter.text(),self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter.text())],
            AddVertically = True
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceConverter.topLevelItem(0),
            TargetWidget = self.ui.GroupBox_EssentialParams_Tool_VoiceConverter,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceConverter
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceConverter.topLevelItem(0).child(0),
            TargetWidget = self.ui.Frame_BasicSettings_Tool_VoiceConverter,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceConverter
        )
        Function_ScrollToWidget(
            Trigger = self.ui.TreeWidget_Catalogue_Tool_VoiceConverter.topLevelItem(0).child(1),
            TargetWidget = self.ui.Frame_AdvanceSettings_Tool_VoiceConverter,
            ScrollArea = self.ui.ScrollArea_Middle_Tool_VoiceConverter
        )

        # Bottom
        self.ui.Button_Tool_VoiceConverter_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceConverter_Execute.setToolTip("执行语音模型推理")
        self.ui.Button_Tool_VoiceConverter_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceConverter_Terminate.setToolTip("终止语音模型推理")
        self.Function_SetMethodExecutor(
            ExecuteButton = self.ui.Button_Tool_VoiceConverter_Execute,
            TerminateButton = self.ui.Button_Tool_VoiceConverter_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_VoiceConverter,
            ConsoleFrame = self.ui.Frame_Console,
            Method = Execute_Voice_Converting.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load,
                self.ui.LineEdit_Tool_VoiceConverter_Model_Path_Load,
                self.ui.PlainTextEdit_Tool_VoiceConverter_Text,
                self.ui.ComboBox_Tool_VoiceConverter_Language,
                self.ui.ComboBox_Tool_VoiceConverter_Speaker,
                self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength,
                self.ui.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration,
                self.ui.DoubleSpinBox_Tool_VoiceConverter_SpeechRate,
                self.ui.LineEdit_Tool_VoiceConverter_Audio_Dir_Save
            ],
            EmptyAllowed = [
                self.ui.ComboBox_Tool_VoiceConverter_Speaker
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                (QMessageBox.Information,"Tip","当前任务已执行结束！",QMessageBox.Ok)
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
        self.ui.Button_Setting_ClientRebooter.setCheckable(True)
        self.ui.Button_Setting_ClientRebooter.setToolTipDuration(-1)
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
        self.ui.Button_Setting_IntegrityChecker.setCheckable(True)
        self.ui.Button_Setting_IntegrityChecker.setToolTipDuration(-1)
        self.ui.Button_Setting_IntegrityChecker.setToolTip(QCA.translate("ToolTip", "检查文件完整性"))

        self.ui.Label_Setting_AutoUpdate.setText(QCA.translate("Label", "自动检查版本并更新"))
        self.ui.CheckBox_Setting_AutoUpdate.setCheckable(True)
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
        self.ui.CheckBox_Setting_Synchronizer.setCheckable(True)
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
                (self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,[self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output],None,[self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input]),
                (self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,[self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output],None,[self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir]),
                ([self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir],[self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir],None,[self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir]),
                ([self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation],[self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation],None,[self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation]),
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
                #(self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,[self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output],None,[self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input],"Disconnect"),
                #(self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,[self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output],None,[self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir],"Disconnect"),
                #([self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir],[self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir],None,[self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir],"Disconnect"),
                #([self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation],[self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation],None,[self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation],"Disconnect")
            ],
            TakeEffect = True
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Setting_Synchronizer,
            UncheckedEventList = [
                Function_ShowMessageBox
            ],
            UncheckedArgsList = [
                (QMessageBox.Information,"Tip", "该设置将于重启之后生效")
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
                    "3. 继续使用本项目被视为同意本仓库README中所述的相关条款。本仓库的 README 有义务进行劝导，但不承担可能出现的任何后续问题的责任。\n"
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
        self.ui.Button_Toggle_Console.setCheckable(True)
        self.ui.Button_Toggle_Console.setChecked(False)
        self.ui.Button_Toggle_Console.setAutoExclusive(False)
        self.ui.Button_Toggle_Console.setToolTipDuration(-1)
        self.ui.Button_Toggle_Console.setToolTip("Click to toggle console")
        self.ui.Button_Toggle_Console.clicked.connect(
            lambda: self.Function_AnimateFrame(
                Frame = self.ui.Frame_Console,
                MinHeight = 0,
                MaxHeight = 210
            )
        )

        # Print ConsoleInfo
        #MainWindowSignals.Signal_FrameStatus.connect(lambda FrameStatus: 
        self.ConsoleInfo.Signal_ConsoleInfo.connect(
            lambda Info: self.Function_PrintText(
                Panel = self.ui.PlainTextEdit_Console,
                FrameStatus = "Extended", #FrameStatus = FrameStatus,
                Text = Info
            )
        )
        #)

        '''
        # Display ToolIndex
        self.ui.Label_Tools.setText("工具编号：")
        self.ui.SpinBox_Tools.setMinimum(1)
        self.ui.SpinBox_Tools.setMaximum(6)
        self.ui.SpinBox_Tools.setValue(1)
        self.ui.SpinBox_Tools.valueChanged.connect(
            lambda Index: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = Index - 1
            )
        )
        self.ui.SpinBox_Tools.valueChanged.connect(
            lambda Index: self.ui.ComboBox_Tools.setCurrentIndex(Index - 1)
        )
        '''
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