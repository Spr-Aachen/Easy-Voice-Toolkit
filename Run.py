import os
import sys
import json
from PySide6 import __file__ as PySide6_File
from PySide6.QtCore import Qt, QObject, Signal, Slot
from PySide6.QtCore import QCoreApplication as QCA
from PySide6.QtWidgets import *

from GUI.QSimpleWidgets.Utils import *
from GUI.QSimpleWidgets.QTasks import *
from GUI.Window import Window_Customizing
from GUI.Functions import *
from GUI.EnvConfigurator import *


# Current version
CurrentVersion = "v1.0.0"


# Set working directory
CurrentDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(CurrentDir)


# Set path to config
ConfigPath = os.path.join(CurrentDir, 'Config.ini')


# Redirect PATH variable 'QT_QPA_PLATFORM_PLUGIN_PATH' to Pyside6 '/plugins/platforms' folder's path
try:
    PySide6_Dirname = os.path.dirname(PySide6_File)
    PySide6_PluginPath = os.path.join(PySide6_Dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = PySide6_PluginPath
except:
    pass


# Import Tools
def ToolsImporter():
    os.chdir(os.path.dirname(os.path.realpath('__file__')))
    if 'Undetected' and 'Checking' not in [
        ManageConfig(ConfigPath).GetValue('Env', 'FFmpeg',  'Checking'),
        ManageConfig(ConfigPath).GetValue('Env', 'GCC',     'Checking'),
        ManageConfig(ConfigPath).GetValue('Env', 'CMake',   'Checking'),
        ManageConfig(ConfigPath).GetValue('Env', 'Python',  'Checking'),
        ManageConfig(ConfigPath).GetValue('Env', 'PyReqs',  'Checking'),
        ManageConfig(ConfigPath).GetValue('Env', 'Pytorch', 'Checking')
    ]:
        try:
            from Tool_AudioProcessor.Process import Audio_Processing
            from Tool_VoiceIdentifier.Identify import Voice_Identifying
            from Tool_VoiceTranscriber.Transcribe import Voice_Transcribing
            from Tool_DatasetCreator.Create import Dataset_Creating
            from Tool_VoiceTrainer.Train import Voice_Training
            from Tool_VoiceConverter.Convert import Voice_Converting
        except: # Unpack & Restart
            shutil.unpack_archive(
                filename = './Tools.zip',
                extract_dir = './',
                format = 'zip'
            )
            os.execv(sys.executable, [sys.executable] + sys.argv) #os.execl(sys.executable, sys.executable, *sys.argv)


# Tool1: AudioProcessor
class Execute_Audio_Processing(QObject):
    '''
    Change media format to WAV and cut off the silent parts
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        AudioConvertandSlice = Audio_Processing(*Params)
        TaskAccelerating(
            TargetList = [AudioConvertandSlice.Convert_Media, AudioConvertandSlice.Slice_Audio],
            ArgsList = [(), ()],
            TypeList = ['MultiThreading', 'MultiThreading']
        )

        self.finished.emit()


# Tool2: VoiceIdentifier
class Execute_Voice_Identifying(QObject):
    '''
    Contrast the voice and filter out the similar ones
    '''
    finished = Signal()
    
    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        AudioContrastInference = Voice_Identifying(*Params)
        TaskAccelerating(
            TargetList = [AudioContrastInference.GetModel, AudioContrastInference.Inference],
            ArgsList = [(), ()],
            TypeList = ['MultiThreading', 'MultiThreading']
        )

        self.finished.emit()


# Tool3: VoiceTranscriber
class Execute_Voice_Transcribing(QObject):
    '''
    Transcribe WAV content to SRT
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        LANGUAGES = {
            "中":       "zh",
            "Chinese":  "zh",
            "英":       "en",
            "English":  "en",
            "日":       "ja",
            "japanese": "ja"
        }
        WAVtoSRT = Voice_Transcribing(*ItemReplacer(LANGUAGES, Params))
        TaskAccelerating(
            TargetList = [WAVtoSRT.Transcriber],
            ArgsList = [()],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()


# Tool4: DatasetCreator
class Execute_Dataset_Creating(QObject):
    '''
    Convert the whisper-generated SRT to CSV and split the WAV
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        SRTtoCSVandSplitAudio = Dataset_Creating(*Params)
        TaskAccelerating(
            TargetList = [SRTtoCSVandSplitAudio.CallingFunctions],
            ArgsList = [()],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()


# Tool5: VoiceTrainer
class Execute_Voice_Training(QObject):
    '''
    Preprocess and then start training
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        LANGUAGES = {
            "中":                            "mandarin",
            "Mandarin":                      "mandarin",
            "中英日":                        "mandarin_english_japanese",
            "Mandarin & English & Japanese": "mandarin_english_japanese"
        }
        PreprocessandTrain = Voice_Training(*ItemReplacer(LANGUAGES, Params))
        TaskAccelerating(
            TargetList = [PreprocessandTrain.Preprocessing_and_Training],
            ArgsList = [()],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()


# Tool6: VoiceConverter
def Get_Speakers(Config_Path_Load):
    try:
        with open(Config_Path_Load, 'r', encoding = 'utf-8') as File:
            Params = json.load(File)
        Speakers = Params["speakers"]
        return Speakers
    except:
        pass

class Execute_Voice_Converting(QObject):
    '''
    Inference model
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    @Slot(tuple)
    def Execute(self, Params: tuple):
        LANGUAGES = {
            "中":       "[ZH]",
            "Chinese":  "[ZH]",
            "英":       "[EN]",
            "English":  "[EN]",
            "日":       "[JA]",
            "Japanese": "[JA]"
        }
        TTS = Voice_Converting(*ItemReplacer(LANGUAGES, Params))
        TaskAccelerating(
            TargetList = [TTS.Converting],
            ArgsList = [()],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()


# Where to store custom signals
class CustomSignals_MainWindow(QObject):
    '''
    Set up signals for MainWindow
    '''
    Signal_MainWindowShown = Signal()


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

        self.ManageConfig = ManageConfig(ConfigPath)

    def Main(self):
        '''
        Main funtion to orgnize all the subfunctions
        '''
        self.ui.Label_Title.setText("Easy Voice Toolkit - by Spr_Aachen")

        # Toggle Menu
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
        self.ui.Button_Toggle_Menu.setToolTipDuration(-1)
        self.ui.Button_Toggle_Menu.setToolTip(QCA.translate("ToolTip", "点击以展开/折叠菜单"))

        # Print Titles & Choose Pages
        QFunctionsSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: Function_PrintText(
                Panel = self.ui.Label_Menu_Home_Text,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Label", "主页")
            )
        )
        self.ui.Button_Menu_Home.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 0
            )
        )
        self.ui.Button_Menu_Home.setCheckable(True)
        self.ui.Button_Menu_Home.setChecked(True)
        self.ui.Button_Menu_Home.setAutoExclusive(True)
        self.ui.Button_Menu_Home.setToolTipDuration(-1)
        self.ui.Button_Menu_Home.setToolTip(QCA.translate("ToolTip", "主页"))

        QFunctionsSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: Function_PrintText(
                Panel = self.ui.Label_Menu_Download_Text,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Label", "下载")
            )
        )
        self.ui.Button_Menu_Download.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 1
            )
        )
        self.ui.Button_Menu_Download.setCheckable(True)
        self.ui.Button_Menu_Download.setChecked(False)
        self.ui.Button_Menu_Download.setAutoExclusive(True)
        self.ui.Button_Menu_Download.setToolTipDuration(-1)
        self.ui.Button_Menu_Download.setToolTip(QCA.translate("ToolTip", "下载"))

        QFunctionsSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: Function_PrintText(
                Panel = self.ui.Label_Menu_Tools_Text,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Label", "工具")
            )
        )
        self.ui.Button_Menu_Tools.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 2
            )
        )
        self.ui.Button_Menu_Tools.setCheckable(True)
        self.ui.Button_Menu_Tools.setChecked(False)
        self.ui.Button_Menu_Tools.setAutoExclusive(True)
        self.ui.Button_Menu_Tools.setToolTipDuration(-1)
        self.ui.Button_Menu_Tools.setToolTip(QCA.translate("ToolTip", "工具"))

        QFunctionsSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: Function_PrintText(
                Panel = self.ui.Label_Menu_Settings_Text,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Label", "设置")
            )
        )
        self.ui.Button_Menu_Settings.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 3
            )
        )
        self.ui.Button_Menu_Settings.setCheckable(True)
        self.ui.Button_Menu_Settings.setChecked(False)
        self.ui.Button_Menu_Settings.setAutoExclusive(True)
        self.ui.Button_Menu_Settings.setToolTipDuration(-1)
        self.ui.Button_Menu_Settings.setToolTip(QCA.translate("ToolTip", "设置"))

        #########################################################
        ##################### Content: Home #####################
        #########################################################

        #self.ui.ToolButton_Home_Title.setText(QCA.translate("Label", "主页"))

        Function_SetText(
            Panel = self.ui.TextBrowser_Text_Home,
            Title = QCA.translate("TextBrowser", "介绍"),
            TitleAlign = "left",
            TitleSize = 24,
            TitleWeight = 840,
            Body = QCA.translate("TextBrowser",
                "一个基于Whisper、VITS等项目实现的简易语音工具箱，提供了包括语音模型训练在内的多种自动化音频工具\n"
                "\n"
                "工具箱目前包含以下功能：\n"
                "音频转换和分割\n"
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
            BodyWeight = 420
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

        self.ui.ToolButton_Download_Title.setText(QCA.translate("Label", "下载"))

        self.ui.Label_Download_FFmpeg.setText("FFmpeg")
        Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Install_FFmpeg,
            ProgressBar = self.ui.ProgressBar_Download_FFmpeg,
            Method = FFmpeg_Installer.Execute,
            Params = ()
        )
        MainWindowSignals.Signal_MainWindowShown.connect(self.ui.Button_Install_FFmpeg.click)
        self.ui.Button_Install_FFmpeg.setText('')
        self.ui.Button_Install_FFmpeg.setCheckable(True)
        self.ui.Button_Install_FFmpeg.setToolTipDuration(-1)
        self.ui.Button_Install_FFmpeg.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_FFmpegUndetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'FFmpeg', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_FFmpegUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到FFmpeg，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [Function_AnimateStackedWidget, self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [(self.ui.StackedWidget_Pages,1), ()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_FFmpegDetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'FFmpeg', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_FFmpegDetected.connect(
            ToolsImporter,
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_FFmpegDetected.connect(
            lambda: self.ui.ProgressBar_Download_FFmpeg.setValue(100)
        )

        self.ui.Label_Download_GCC.setText("GCC")
        Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Install_GCC,
            ProgressBar = self.ui.ProgressBar_Download_GCC,
            Method = GCC_Installer.Execute,
            Params = ()
        )
        MainWindowSignals.Signal_MainWindowShown.connect(self.ui.Button_Install_GCC.click)
        self.ui.Button_Install_GCC.setText('')
        self.ui.Button_Install_GCC.setCheckable(True)
        self.ui.Button_Install_GCC.setToolTipDuration(-1)
        self.ui.Button_Install_GCC.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_GCCUndetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'GCC', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_GCCUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到GCC，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [Function_AnimateStackedWidget, self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [(self.ui.StackedWidget_Pages,1), ()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_GCCDetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'GCC', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_GCCDetected.connect(
            ToolsImporter,
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_GCCDetected.connect(
            lambda: self.ui.ProgressBar_Download_GCC.setValue(100)
        )

        self.ui.Label_Download_CMake.setText("CMake")
        Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Install_CMake,
            ProgressBar = self.ui.ProgressBar_Download_CMake,
            Method = CMake_Installer.Execute,
            Params = ()
        )
        EnvConfiguratorSignals.Signal_GCCDetected.connect(self.ui.Button_Install_CMake.click) #MainWindowSignals.Signal_MainWindowShown.connect(self.ui.Button_Install_CMake.click)
        self.ui.Button_Install_CMake.setText('')
        self.ui.Button_Install_CMake.setCheckable(True)
        self.ui.Button_Install_CMake.setToolTipDuration(-1)
        self.ui.Button_Install_CMake.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_CMakeUndetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'CMake', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_CMakeUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到CMake，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [Function_AnimateStackedWidget, self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [(self.ui.StackedWidget_Pages,1), ()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_CMakeDetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'CMake', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_CMakeDetected.connect(
            ToolsImporter,
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_CMakeDetected.connect(
            lambda: self.ui.ProgressBar_Download_CMake.setValue(100)
        )

        self.ui.Label_Download_Python.setText("Python")
        Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Install_Python,
            ProgressBar = self.ui.ProgressBar_Download_Python,
            Method = Python_Installer.Execute,
            Params = ('3.9', )
        )
        EnvConfiguratorSignals.Signal_CMakeDetected.connect(self.ui.Button_Install_Python.click) #MainWindowSignals.Signal_MainWindowShown.connect(self.ui.Button_Install_Python.click)
        self.ui.Button_Install_Python.setText('')
        self.ui.Button_Install_Python.setCheckable(True)
        self.ui.Button_Install_Python.setToolTipDuration(-1)
        self.ui.Button_Install_Python.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_PythonUndetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'Python', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_PythonUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到Python，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [Function_AnimateStackedWidget, self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [(self.ui.StackedWidget_Pages,1), ()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'Python', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            ToolsImporter,
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(
            lambda: self.ui.ProgressBar_Download_Python.setValue(100)
        )

        self.ui.Label_Download_PyReqs.setText("Python Requirements")
        Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Install_PyReqs,
            ProgressBar = self.ui.ProgressBar_Download_PyReqs,
            Method = PyReqs_Installer.Execute,
            Params = (os.path.join(CurrentDir, 'requirements.txt'), )
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(self.ui.Button_Install_PyReqs.click) #MainWindowSignals.Signal_MainWindowShown.connect(self.ui.Button_Install_PyReqs.click)
        self.ui.Button_Install_PyReqs.setText('')
        self.ui.Button_Install_PyReqs.setCheckable(True)
        self.ui.Button_Install_PyReqs.setToolTipDuration(-1)
        self.ui.Button_Install_PyReqs.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_PyReqsUndetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'PyReqs', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_PyReqsUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到Python依赖库，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [Function_AnimateStackedWidget, self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [(self.ui.StackedWidget_Pages,1), ()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_PyReqsDetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'PyReqs', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PyReqsDetected.connect(
            ToolsImporter,
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PyReqsDetected.connect(
            lambda: self.ui.ProgressBar_Download_PyReqs.setValue(100)
        )

        self.ui.Label_Download_Pytorch.setText("Pytorch")
        Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Install_Pytorch,
            ProgressBar = self.ui.ProgressBar_Download_Pytorch,
            Method = Pytorch_Installer.Execute,
            Params = ()
        )
        EnvConfiguratorSignals.Signal_PythonDetected.connect(self.ui.Button_Install_Pytorch.click) #MainWindowSignals.Signal_MainWindowShown.connect(self.ui.Button_Install_Pytorch.click)
        self.ui.Button_Install_Pytorch.setText('')
        self.ui.Button_Install_Pytorch.setCheckable(True)
        self.ui.Button_Install_Pytorch.setToolTipDuration(-1)
        self.ui.Button_Install_Pytorch.setToolTip(QCA.translate("ToolTip", "重新下载"))
        EnvConfiguratorSignals.Signal_PytorchUndetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'Pytorch', 'Undetected'),
        )
        EnvConfiguratorSignals.Signal_PytorchUndetected.connect(
            lambda: Function_ShowMessageBox(
                WindowTitle = "Tip",
                Text = "未检测到Pytorch，已开始下载",
                EventButtons = [QMessageBox.Ok],
                EventLists = [
                    [Function_AnimateStackedWidget, self.ui.Button_Menu_Download.click]
                ],
                ParamLists = [
                    [(self.ui.StackedWidget_Pages,1), ()]
                ]
            )
        )
        EnvConfiguratorSignals.Signal_PytorchDetected.connect(
            lambda: self.ManageConfig.EditConfig('Env', 'Pytorch', 'Detected'),
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PytorchDetected.connect(
            ToolsImporter,
            type = Qt.QueuedConnection
        )
        EnvConfiguratorSignals.Signal_PytorchDetected.connect(
            lambda: self.ui.ProgressBar_Download_Pytorch.setValue(100)
        )

        ##########################################################
        ##################### Content: Tools #####################
        ##########################################################

        '''
        self.ui.Label_Tools_Title.setText(QCA.translate("Label", "工具  -   "))

        self.ui.ComboBox_Tools.addItems([
                QCA.translate("ComboBox", "音频转换和分割"),
                QCA.translate("ComboBox", "语音识别和筛选"),
                QCA.translate("ComboBox", "语音转文字字幕"),
                QCA.translate("ComboBox", "语音数据集制作"),
                QCA.translate("ComboBox", "语音模型训练"),
                QCA.translate("ComboBox", "语音模型推理")
            ]
        )
        self.ui.ComboBox_Tools.setCurrentText(QCA.translate("ComboBox", '音频转换和分割'))
        self.ui.ComboBox_Tools.currentIndexChanged.connect(
            lambda Index: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = Index
            )
        )
        self.ui.ComboBox_Tools.currentIndexChanged.connect(
            lambda Index: self.ui.SpinBox_Tools.setValue(Index + 1)
        )
        '''

        self.ui.ToolButton_Tools_Title_AudioProcessor.setText(QCA.translate("ComboBox", '音频转换和分割'))
        self.ui.ToolButton_Tools_Title_AudioProcessor.setCheckable(True)
        self.ui.ToolButton_Tools_Title_AudioProcessor.setChecked(True)
        self.ui.ToolButton_Tools_Title_AudioProcessor.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_AudioProcessor.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 0
            )
        )

        self.ui.ToolButton_Tools_Title_VoiceIdentifier.setText(QCA.translate("ComboBox", "语音识别和筛选"))
        self.ui.ToolButton_Tools_Title_VoiceIdentifier.setCheckable(True)
        self.ui.ToolButton_Tools_Title_VoiceIdentifier.setChecked(False)
        self.ui.ToolButton_Tools_Title_VoiceIdentifier.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_VoiceIdentifier.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 1
            )
        )

        self.ui.ToolButton_Tools_Title_VoiceTranscriber.setText(QCA.translate("ComboBox", "语音转文字字幕"))
        self.ui.ToolButton_Tools_Title_VoiceTranscriber.setCheckable(True)
        self.ui.ToolButton_Tools_Title_VoiceTranscriber.setChecked(False)
        self.ui.ToolButton_Tools_Title_VoiceTranscriber.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_VoiceTranscriber.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 2
            )
        )

        self.ui.ToolButton_Tools_Title_DatasetCreator.setText(QCA.translate("ComboBox", "语音数据集制作"))
        self.ui.ToolButton_Tools_Title_DatasetCreator.setCheckable(True)
        self.ui.ToolButton_Tools_Title_DatasetCreator.setChecked(False)
        self.ui.ToolButton_Tools_Title_DatasetCreator.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_DatasetCreator.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 3
            )
        )

        self.ui.ToolButton_Tools_Title_VoiceTrainer.setText(QCA.translate("ComboBox", "语音模型训练"))
        self.ui.ToolButton_Tools_Title_VoiceTrainer.setCheckable(True)
        self.ui.ToolButton_Tools_Title_VoiceTrainer.setChecked(False)
        self.ui.ToolButton_Tools_Title_VoiceTrainer.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_VoiceTrainer.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 4
            )
        )

        self.ui.ToolButton_Tools_Title_VoiceConverter.setText(QCA.translate("ComboBox", "语音模型推理"))
        self.ui.ToolButton_Tools_Title_VoiceConverter.setCheckable(True)
        self.ui.ToolButton_Tools_Title_VoiceConverter.setChecked(False)
        self.ui.ToolButton_Tools_Title_VoiceConverter.setAutoExclusive(True)
        self.ui.ToolButton_Tools_Title_VoiceConverter.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = 5
            )
        )

        ##################### Tool_AudioProcessor #####################
        '''
        Function_SetText(
            Panel = self.ui.TextBrowser_Intro_Tool_AudioProcessor,
            Title = QCA.translate("TextBrowser", "音频转换和分割"),
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
        '''

        Path_Config_Tool_AudioProcessor = os.path.join(CurrentDir, 'Config_Tool_AudioProcessor.ini')
        Config_Tool_AudioProcessor = ManageConfig(
            self.ManageConfig.GetValue(
                'ConfigPath',
                'Path_Config_Tool_AudioProcessor',
                Path_Config_Tool_AudioProcessor
            )
        )

        # Middle
        self.ui.GroupBox_EssentialParams_Tool_AudioProcessor.setTitle(QCA.translate("GroupBox", "必要参数"))

        self.ui.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor.setText("基础设置（显示）")
        self.ui.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor.setChecked(
            True #bool(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor,
            CheckedText = "基础设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_AudioProcessor.EditConfig
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_AudioProcessor,...,...,0,self.ui.Frame_Tool_AudioProcessor_Media_Dir_Input.height()+self.ui.Frame_Tool_AudioProcessor_Media_Format_Output.height()+self.ui.Frame_Tool_AudioProcessor_Media_Dir_Output.height(),0,'Extend'),
                #('AudioProcessor', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_AudioProcessor.EditConfig
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_AudioProcessor,...,...,0,self.ui.Frame_Tool_AudioProcessor_Media_Dir_Input.height()+self.ui.Frame_Tool_AudioProcessor_Media_Format_Output.height()+self.ui.Frame_Tool_AudioProcessor_Media_Dir_Output.height(),0,'Reduce'),
                #('AudioProcessor', 'Toggle_BasicSettings', 'False')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Media_Dir_Input,
            Title = QCA.translate("Label", "媒体输入目录"),
            Body = QCA.translate("Label", "该目录中的媒体文件将会以下列设置输出为音频文件。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_AudioProcessor_Media_Dir_Input,
            LineEdit = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Input,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Input.setText(
            str(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Media_Dir_Input', 'None'))
        )
        self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Input.textChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'Media_Dir_Input', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Media_Format_Output,
            Title = QCA.translate("Label", "媒体输出格式"),
            Body = QCA.translate("Label", "媒体文件将会以设置的格式输出为音频文件。")
        )
        self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output.addItems(['flac', 'wav', 'mp3', 'aac', 'ogg', 'm4a', 'wma', 'aiff', 'au'])
        self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output.setCurrentText(
            str(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Media_Format_Output', 'wav'))
        )
        self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output.currentTextChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'Media_Format_Output', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Media_Dir_Output,
            Title = QCA.translate("Label", "媒体输出目录"),
            Body = QCA.translate("Label", "最后生成的音频文件将被保存到该目录中。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_AudioProcessor_Media_Dir_Output,
            LineEdit = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output.setText(
            str(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Media_Dir_Output', 'None'))
        )
        self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output.textChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'Media_Dir_Output', str(Value))
        )

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor.setText("高级设置（隐藏）")
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor.setChecked(
            False #bool(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Toggle_AdvanceSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor,
            CheckedText = "高级设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_AudioProcessor.EditConfig
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_AudioProcessor,...,...,0,self.ui.Frame_Tool_AudioProcessor_RMS_Threshold.height()+self.ui.Frame_Tool_AudioProcessor_Hop_Size.height()+self.ui.Frame_Tool_AudioProcessor_Silent_Interval_Min.height()+self.ui.Frame_Tool_AudioProcessor_Silence_Kept_Max.height()+self.ui.Frame_Tool_AudioProcessor_Audio_Length_Min.height(),0,'Extend'),
                #('AudioProcessor', 'Toggle_AdvanceSettings', 'True')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_AudioProcessor.EditConfig
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_AudioProcessor,...,...,0,self.ui.Frame_Tool_AudioProcessor_RMS_Threshold.height()+self.ui.Frame_Tool_AudioProcessor_Hop_Size.height()+self.ui.Frame_Tool_AudioProcessor_Silent_Interval_Min.height()+self.ui.Frame_Tool_AudioProcessor_Silence_Kept_Max.height()+self.ui.Frame_Tool_AudioProcessor_Audio_Length_Min.height(),0,'Reduce'),
                #('AudioProcessor', 'Toggle_AdvanceSettings', 'False')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_RMS_Threshold,
            Title = QCA.translate("Label", "均方根阈值 (db)"),
            Body = QCA.translate("Label", "低于该阈值的片段将被视作静音进行处理，若有降噪需求可以增加该值。")
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
            Panel = self.ui.Label_Tool_AudioProcessor_Hop_Size,
            Title = QCA.translate("Label", "跃点大小 (ms)"),
            Body = QCA.translate("Label", "每个RMS帧的长度，增加该值能够提高分割精度但会减慢进程。")
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
            Panel = self.ui.Label_Tool_AudioProcessor_Silent_Interval_Min,
            Title = QCA.translate("Label", "最小静音间隔 (ms)"),
            Body = QCA.translate("Label", "静音部分被分割成的最小长度，若音频只包含短暂中断可以减小该值。")
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
            Panel = self.ui.Label_Tool_AudioProcessor_Silence_Kept_Max,
            Title = QCA.translate("Label", "最大静音长度 (ms)"),
            Body = QCA.translate("Label", "被分割的音频周围保持静音的最大长度。")
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
            Panel = self.ui.Label_Tool_AudioProcessor_Audio_Length_Min,
            Title = QCA.translate("Label", "最小音频长度 (ms)"),
            Body = QCA.translate("Label", "每个被分割的音频片段所需的最小长度。")
        )
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setRange(300, 30000)
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setValue(
            int(Config_Tool_AudioProcessor.GetValue('AudioProcessor', 'Audio_Length_Min', '3000'))
        )
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.valueChanged.connect(
            lambda Value: Config_Tool_AudioProcessor.EditConfig('AudioProcessor', 'Audio_Length_Min', str(Value))
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
        MonitorFile_Config_AudioProcessor = MonitorFile(Path_Config_Tool_AudioProcessor)
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
        self.ui.Button_Tool_AudioProcessor_Execute.setToolTip(QCA.translate("ToolTip", "执行音频转换和分割"))
        self.ui.Button_Tool_AudioProcessor_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_AudioProcessor_Terminate.setToolTip(QCA.translate("ToolTip", "终止音频转换和分割"))
        Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Tool_AudioProcessor_Execute,
            TerminateButton = self.ui.Button_Tool_AudioProcessor_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_AudioProcessor,
            ConsoleFrame = self.ui.Frame_Console,
            Method = Execute_Audio_Processing.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Input,
                self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,
                self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output,
                self.ui.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold,
                self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min,
                self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min,
                self.ui.SpinBox_Tool_AudioProcessor_Hop_Size,
                self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                ("Ask","当前任务已执行完成，是否跳转至下一工具界面？",QMessageBox.Yes|QMessageBox.No,[QMessageBox.Yes],[[Function_AnimateStackedWidget,self.ui.Frame_Tools_Top.layout().itemAt(self.ui.StackedWidget_Pages_Tools.currentIndex()+1).widget().click]],[[(self.ui.StackedWidget_Pages_Tools,self.ui.StackedWidget_Pages_Tools.currentIndex()+1),()]])
            ]
        )

        ##################### Tool_VoiceIdentifier #####################
        '''
        Function_SetText(
            Panel = self.ui.TextBrowser_Intro_Tool_VoiceIdentifier,
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
        '''

        Path_Config_Tool_VoiceIdentifier = os.path.join(CurrentDir, 'Config_Tool_VoiceIdentifier.ini')
        Config_Tool_VoiceIdentifier = ManageConfig(
            self.ManageConfig.GetValue(
                'ConfigPath',
                'Path_Config_Tool_VoiceIdentifier',
                Path_Config_Tool_VoiceIdentifier
            )
        )

        # Middle
        self.ui.GroupBox_EssentialParams_Tool_VoiceIdentifier.setTitle("必要参数")

        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier.setText("基础设置（显示）")
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier.setChecked(
            True #bool(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier,
            CheckedText = "基础设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceIdentifier.EditConfig
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceIdentifier,...,...,0,self.ui.Frame_Tool_VoiceIdentifier_Audio_Dir_Input.height()+self.ui.Frame_Tool_VoiceIdentifier_StdAudioSpeaker.height()+self.ui.Frame_Tool_VoiceIdentifier_DecisionThreshold.height()+self.ui.Frame_Tool_VoiceIdentifier_Audio_Dir_Output.height(),0,'Extend'),
                #('VoiceIdentifier', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceIdentifier.EditConfig
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceIdentifier,...,...,0,self.ui.Frame_Tool_VoiceIdentifier_Audio_Dir_Input.height()+self.ui.Frame_Tool_VoiceIdentifier_StdAudioSpeaker.height()+self.ui.Frame_Tool_VoiceIdentifier_DecisionThreshold.height()+self.ui.Frame_Tool_VoiceIdentifier_Audio_Dir_Output.height(),0,'Reduce'),
                #('VoiceIdentifier', 'Toggle_BasicSettings', 'False')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Audio_Dir_Input,
            Title = "音频输入目录",
            Body = QCA.translate("Label", "该目录中的音频文件将会按照以下设置进行识别筛选。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Audio_Dir_Input,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input.setText(
            str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Audio_Dir_Input', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input.textChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Audio_Dir_Input', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_StdAudioSpeaker,
            Title = "目标人物与音频",
            Body = QCA.translate("Label", "目标人物的名字及其语音文件的所在路径，音频中尽量不要混入杂音。")
        )
        self.ui.Table_Tool_VoiceIdentifier_StdAudioSpeaker.SetValue(
            eval(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'StdAudioSpeaker', '{"": ""}'))
        )
        self.ui.Table_Tool_VoiceIdentifier_StdAudioSpeaker.ValueChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'StdAudioSpeaker', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_DecisionThreshold,
            Title = "判断阈值",
            Body = QCA.translate("Label", "判断是否为同一人的阈值，若参与比对的说话人声音相识度较高可以增加该值。")
        )
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setRange(0.5, 1)
        #self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setValue(
            float(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'DecisionThreshold', '0.75'))
        )
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.valueChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'DecisionThreshold', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Audio_Dir_Output,
            Title = "音频输出目录",
            Body = QCA.translate("Label", "最后筛选出的音频文件将被复制到该目录中。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Audio_Dir_Output,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output.setText(
            str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Audio_Dir_Output', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output.textChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Audio_Dir_Output', str(Value))
        )

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier.setText("高级设置（隐藏）")
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier,
            CheckedText = "高级设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceIdentifier,...,...,0,self.ui.Frame_Tool_VoiceIdentifier_Model_Dir.height()+self.ui.Frame_Tool_VoiceIdentifier_Model_Type.height()+self.ui.Frame_Tool_VoiceIdentifier_Model_Name.height()+self.ui.Frame_Tool_VoiceIdentifier_Feature_Method.height()+self.ui.Frame_Tool_VoiceIdentifier_Duration_of_Audio.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceIdentifier,...,...,0,self.ui.Frame_Tool_VoiceIdentifier_Model_Dir.height()+self.ui.Frame_Tool_VoiceIdentifier_Model_Type.height()+self.ui.Frame_Tool_VoiceIdentifier_Model_Name.height()+self.ui.Frame_Tool_VoiceIdentifier_Feature_Method.height()+self.ui.Frame_Tool_VoiceIdentifier_Duration_of_Audio.height(),0,'Reduce')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Model_Dir,
            Title = "模型存放目录",
            Body = QCA.translate("Label", "该目录将会用于存放下载的声纹识别模型，若模型已存在会直接使用。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Model_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Model_Dir,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_VoiceIdentifier_Model_Dir.setText(
            str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Model_Dir', os.path.join(CurrentDir, 'Download')))
        )
        self.ui.LineEdit_Tool_VoiceIdentifier_Model_Dir.textChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Model_Dir', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Model_Type,
            Title = "模型类型",
            Body = QCA.translate("Label", "声纹识别模型的类型。")
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type.addItems(['Ecapa-Tdnn'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type.setCurrentText(
            str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Model_Type', 'Ecapa-Tdnn'))
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Model_Type', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Model_Name,
            Title = "模型名字",
            Body = QCA.translate("Label", "声纹识别模型的名字，默认代表模型的大小。")
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name.addItems(['small'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name.setCurrentText(
            str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Model_Name', 'small'))
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Model_Name', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Feature_Method,
            Title = "特征提取方法",
            Body = QCA.translate("Label", "音频特征的提取方法。")
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method.addItems(['spectrogram', 'melspectrogram'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method.setCurrentText(
            str(Config_Tool_VoiceIdentifier.GetValue('VoiceIdentifier', 'Feature_Method', 'spectrogram'))
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceIdentifier.EditConfig('VoiceIdentifier', 'Feature_Method', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Duration_of_Audio,
            Title = "音频长度",
            Body = QCA.translate("Label", "用于预测的音频长度。")
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
        MonitorFile_Config_VoiceIdentifier = MonitorFile(Path_Config_Tool_VoiceIdentifier)
        MonitorFile_Config_VoiceIdentifier.start()
        MonitorFile_Config_VoiceIdentifier.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Tool_VoiceIdentifier.setText(
                FileContent
            )
        )

        self.ui.Button_SyncParams_Tool_VoiceIdentifier.setText(QCA.translate("Button", "同步参数设置"))
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
        Function_ExecuteMethod(
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
                ("Ask","当前任务已执行完成，是否跳转至下一工具界面？",QMessageBox.Yes|QMessageBox.No,[QMessageBox.Yes],[[Function_AnimateStackedWidget,self.ui.Frame_Tools_Top.layout().itemAt(self.ui.StackedWidget_Pages_Tools.currentIndex()+1).widget().click]],[[(self.ui.StackedWidget_Pages_Tools,self.ui.StackedWidget_Pages_Tools.currentIndex()+1),()]])
            ]
        )

        ##################### Tool_VoiceTranscriber #####################
        '''
        Function_SetText(
            Panel = self.ui.TextBrowser_Intro_Tool_VoiceTranscriber,
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
        '''

        Path_Config_Tool_VoiceTranscriber = os.path.join(CurrentDir, 'Config_Tool_VoiceTranscriber.ini')
        Config_Tool_VoiceTranscriber = ManageConfig(
            self.ManageConfig.GetValue(
                'ConfigPath',
                'Path_Config_Tool_VoiceTranscriber',
                Path_Config_Tool_VoiceTranscriber
            )
        )

        # Middle
        self.ui.GroupBox_EssentialParams_Tool_VoiceTranscriber.setTitle("必要参数")

        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber.setText("基础设置（显示）")
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber.setChecked(
            True #bool(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber,
            CheckedText = "基础设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceTranscriber.EditConfig
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_WAV_Dir.height()+self.ui.Frame_Tool_VoiceTranscriber_SRT_Dir.height(),0,'Extend'),
                #('VoiceTranscriber', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceTranscriber.EditConfig
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_WAV_Dir.height()+self.ui.Frame_Tool_VoiceTranscriber_SRT_Dir.height(),0,'Reduce'),
                #('VoiceTranscriber', 'Toggle_BasicSettings', 'False')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_WAV_Dir,
            Title = "音频目录",
            Body = QCA.translate("Label", "该目录中的wav文件的语音内容将会按照以下设置转为文字。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_WAV_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir.setText(
            str(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'WAV_Dir', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir.textChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'WAV_Dir', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_SRT_Dir,
            Title = "字幕输出目录",
            Body = QCA.translate("Label", "最后生成的字幕文件将会保存到该目录中。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_SRT_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir.setText(
            str(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'SRT_Dir', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir.textChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'SRT_Dir', str(Value))
        )

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber.setText("高级设置（隐藏）")
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber,
            CheckedText = "高级设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_Model_Dir.height()+self.ui.Frame_Tool_VoiceTranscriber_Model_Name.height()+self.ui.Frame_Tool_VoiceTranscriber_Verbose.height()+self.ui.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text.height()+self.ui.Frame_Tool_VoiceTranscriber_fp16.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_Model_Dir.height()+self.ui.Frame_Tool_VoiceTranscriber_Model_Name.height()+self.ui.Frame_Tool_VoiceTranscriber_Verbose.height()+self.ui.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text.height()+self.ui.Frame_Tool_VoiceTranscriber_fp16.height(),0,'Reduce')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Model_Dir,
            Title = "模型存放目录",
            Body = QCA.translate("Label", "该目录将会用于存放下载的语音识别模型，若模型已存在会直接使用。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_Model_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_Model_Dir,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_VoiceTranscriber_Model_Dir.setText(
            str(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Model_Dir', os.path.join(CurrentDir, 'Download')))
        )
        self.ui.LineEdit_Tool_VoiceTranscriber_Model_Dir.textChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'Model_Dir', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Model_Name,
            Title = "模型名字",
            Body = QCA.translate("Label", "语音识别 (whisper) 模型的名字，默认代表模型的大小。")
        )
        self.ui.ComboBox_Tool_VoiceTranscriber_Model_Name.addItems(['tiny', 'base', 'small', 'medium', 'large'])
        self.ui.ComboBox_Tool_VoiceTranscriber_Model_Name.setCurrentText(
            str(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Model_Name', 'small'))
        )
        self.ui.ComboBox_Tool_VoiceTranscriber_Model_Name.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'Model_Name', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Verbose,
            Title = "启用输出日志",
            Body = QCA.translate("Label", "输出debug日志。")
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_Verbose.setText("已启用")
        self.ui.CheckBox_Tool_VoiceTranscriber_Verbose.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_Verbose.setChecked(
            bool(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Verbose', 'True'))
        )
        '''
        self.ui.CheckBox_Tool_VoiceTranscriber_Verbose.stateChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'Verbose', str(Value))
        )
        '''
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTranscriber_Verbose,
            CheckedText = "已启用",
            CheckedPermEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            CheckedPermArgsList = [
                ('VoiceTranscriber', 'Verbose', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedPermEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            UncheckedPermArgsList = [
                ('VoiceTranscriber', 'Verbose', 'False')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Condition_on_Previous_Text,
            Title = "前后文一致",
            Body = QCA.translate("Label", "将模型之前的输出作为下个窗口的提示，若模型陷入了失败循环则禁用此项。")
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setText("已启用")
        self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setChecked(
            bool(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Condition_on_Previous_Text', 'True'))
        )
        '''
        self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.stateChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'Condition_on_Previous_Text', str(Value))
        )
        '''
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text,
            CheckedText = "已启用",
            CheckedPermEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            CheckedPermArgsList = [
                ('VoiceTranscriber', 'Condition_on_Previous_Text', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedPermEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            UncheckedPermArgsList = [
                ('VoiceTranscriber', 'Condition_on_Previous_Text', 'False')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_fp16,
            Title = "半精度",
            Body = QCA.translate("Label", "主要使用半精度浮点数进行计算，若GPU不可用则忽略或禁用此项。")
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_fp16.setText("已启用")
        self.ui.CheckBox_Tool_VoiceTranscriber_fp16.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_fp16.setChecked(
            bool(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'fp16', 'True'))
        )
        '''
        self.ui.CheckBox_Tool_VoiceTranscriber_fp16.stateChanged.connect(
            lambda Value: Config_Tool_VoiceTranscriber.EditConfig('VoiceTranscriber', 'fp16', str(Value))
        )
        '''
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTranscriber_fp16,
            CheckedText = "已启用",
            CheckedPermEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            CheckedPermArgsList = [
                ('VoiceTranscriber', 'fp16', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedPermEventList = [
                Config_Tool_VoiceTranscriber.EditConfig
            ],
            UncheckedPermArgsList = [
                ('VoiceTranscriber', 'fp16', 'False')
            ]
        )

        self.ui.GroupBox_OptionalParams_Tool_VoiceTranscriber.setTitle("可选参数")

        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber.setText("基础设置（显示）")
        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber.setChecked(
            True #bool(Config_Tool_VoiceTranscriber.GetValue('VoiceTranscriber', 'Toggle_BasicOptionalSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber,
            CheckedText = "基础设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceTranscriber.EditConfig
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_BasicOptionalSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_Language.height(),0,'Extend'),
                #('VoiceTranscriber', 'Toggle_BasicOptionalSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceTranscriber.EditConfig
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_BasicOptionalSettings_Tool_VoiceTranscriber,...,...,0,self.ui.Frame_Tool_VoiceTranscriber_Language.height(),0,'Reduce'),
                #('VoiceTranscriber', 'Toggle_BasicOptionalSettings', 'False')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Language,
            Title = "所用语言",
            Body = QCA.translate("Label", "音频中说话人所使用的语言，若存在多种语言则保持'None'即可。")
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
        MonitorFile_Config_VoiceTranscriber = MonitorFile(Path_Config_Tool_VoiceTranscriber)
        MonitorFile_Config_VoiceTranscriber.start()
        MonitorFile_Config_VoiceTranscriber.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Tool_VoiceTranscriber.setText(
                FileContent
            )
        )

        self.ui.Button_SyncParams_Tool_VoiceTranscriber.setText("同步参数设置")
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
            URL = [
                self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir,
                self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir
            ],
            ButtonTooltip = "Click to open"
        )

        # Bottom
        self.ui.Button_Tool_VoiceTranscriber_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceTranscriber_Execute.setToolTip("执行语音转文字字幕")
        self.ui.Button_Tool_VoiceTranscriber_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceTranscriber_Terminate.setToolTip("终止语音转文字字幕")
        Function_ExecuteMethod(
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
                ("Ask","当前任务已执行完成，是否跳转至下一工具界面？",QMessageBox.Yes|QMessageBox.No,[QMessageBox.Yes],[[Function_AnimateStackedWidget,self.ui.Frame_Tools_Top.layout().itemAt(self.ui.StackedWidget_Pages_Tools.currentIndex()+1).widget().click]],[[(self.ui.StackedWidget_Pages_Tools,self.ui.StackedWidget_Pages_Tools.currentIndex()+1),()]])
            ]
        )

        ##################### Tool_DatasetCreator #####################
        '''
        Function_SetText(
            Panel = self.ui.TextBrowser_Intro_Tool_DatasetCreator,
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
        '''

        Path_Config_Tool_DatasetCreator = os.path.join(CurrentDir, 'Config_Tool_DatasetCreator.ini')
        Config_Tool_DatasetCreator = ManageConfig(
            self.ManageConfig.GetValue(
                'ConfigPath',
                'Path_Config_Tool_DatasetCreator',
                Path_Config_Tool_DatasetCreator
            )
        )

        # Middle
        self.ui.GroupBox_EssentialParams_Tool_DatasetCreator.setTitle("必要参数")

        self.ui.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator.setText("基础设置（显示）")
        self.ui.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator.setChecked(
            True #bool(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator,
            CheckedText = "基础设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_DatasetCreator.EditConfig
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_DatasetCreator,...,...,0,self.ui.Frame_Tool_DatasetCreator_WAV_Dir.height()+self.ui.Frame_Tool_DatasetCreator_SRT_Dir.height()+self.ui.Frame_Tool_DatasetCreator_AutoEncoder.height()+self.ui.Frame_Tool_DatasetCreator_WAV_Dir_Split.height()+self.ui.Frame_Tool_DatasetCreator_FileList_Path_Training.height()+self.ui.Frame_Tool_DatasetCreator_FileList_Path_Validation.height(),0,'Extend'),
                #('DatasetCreator', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_DatasetCreator.EditConfig
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_DatasetCreator,...,...,0,self.ui.Frame_Tool_DatasetCreator_WAV_Dir.height()+self.ui.Frame_Tool_DatasetCreator_SRT_Dir.height()+self.ui.Frame_Tool_DatasetCreator_AutoEncoder.height()+self.ui.Frame_Tool_DatasetCreator_WAV_Dir_Split.height()+self.ui.Frame_Tool_DatasetCreator_FileList_Path_Training.height()+self.ui.Frame_Tool_DatasetCreator_FileList_Path_Validation.height(),0,'Reduce'),
                #('DatasetCreator', 'Toggle_BasicSettings', 'False')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_WAV_Dir,
            Title = "音频输入目录",
            Body = QCA.translate("Label", "该目录中的wav文件将会按照以下设置重采样并根据字幕时间戳进行分割。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_WAV_Dir,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir.setText(
            str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'WAV_Dir', 'None'))
        )
        self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir.textChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'WAV_Dir', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_SRT_Dir,
            Title = "字幕输入目录",
            Body = QCA.translate("Label", "该目录中的srt文件将会按照以下设置转为适用于模型训练的csv文件。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_SRT_Dir,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir.setText(
            str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'SRT_Dir', 'None'))
        )
        self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir.textChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'SRT_Dir', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_AutoEncoder,
            Title = "自编码器",
            Body = QCA.translate("Label", "模型训练所使用的自动编码器。")
        )
        self.ui.ComboBox_Tool_DatasetCreator_AutoEncoder.addItems(['VITS'])
        self.ui.ComboBox_Tool_DatasetCreator_AutoEncoder.setCurrentText(
            str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'AutoEncoder', 'VITS'))
        )
        self.ui.ComboBox_Tool_DatasetCreator_AutoEncoder.currentTextChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'AutoEncoder', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_WAV_Dir_Split,
            Title = "音频输出目录",
            Body = QCA.translate("Label", "最后处理完成的音频将会保存到该目录中。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_WAV_Dir_Split,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir_Split,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir_Split.setText(
            str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'WAV_Dir_Split', 'None'))
        )
        self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir_Split.textChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'WAV_Dir_Split', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_FileList_Path_Training,
            Title = "训练集文本路径",
            Body = QCA.translate("Label", "最后生成的训练集txt文件将会保存到该路径。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_FileList_Path_Training,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
            Mode = "SaveFile",
            FileType = "txt类型 (*.txt)"
        )
        self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training.setText(
            str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'FileList_Path_Training', 'None'))
        )
        self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training.textChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'FileList_Path_Training', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_FileList_Path_Validation,
            Title = "验证集文本路径",
            Body = QCA.translate("Label", "最后生成的验证集txt文件将会保存到该路径。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_FileList_Path_Validation,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation,
            Mode = "SaveFile",
            FileType = "txt类型 (*.txt)"
        )
        self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation.setText(
            str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'FileList_Path_Validation', 'None'))
        )
        self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation.textChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'FileList_Path_Validation', str(Value))
        )

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator.setText("高级设置（隐藏）")
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator,
            CheckedText = "高级设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_DatasetCreator,...,...,0,self.ui.Frame_Tool_DatasetCreator_Sample_Rate.height()+self.ui.Frame_Tool_DatasetCreator_Subtype.height()+self.ui.Frame_Tool_DatasetCreator_TrainRatio.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_DatasetCreator,...,...,0,self.ui.Frame_Tool_DatasetCreator_Sample_Rate.height()+self.ui.Frame_Tool_DatasetCreator_Subtype.height()+self.ui.Frame_Tool_DatasetCreator_TrainRatio.height(),0,'Reduce')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_Sample_Rate,
            Title = "采样率 (HZ)",
            Body = QCA.translate("Label", "音频将要使用的新采样率。")
        )
        self.ui.SpinBox_Tool_DatasetCreator_Sample_Rate.setRange(16000, 96000)
        self.ui.SpinBox_Tool_DatasetCreator_Sample_Rate.setSingleStep(1)
        self.ui.SpinBox_Tool_DatasetCreator_Sample_Rate.setValue(
            int(Config_Tool_DatasetCreator.GetValue('DatasetCreato', 'Sample_Rate', '22050'))
        )
        self.ui.SpinBox_Tool_DatasetCreator_Sample_Rate.valueChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreato', 'Sample_Rate', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_Subtype,
            Title = "采样格式",
            Body = QCA.translate("Label", "音频将要使用的新采样格式。")
        )
        self.ui.ComboBox_Tool_DatasetCreator_Subtype.addItems(['PCM_16'])
        self.ui.ComboBox_Tool_DatasetCreator_Subtype.setCurrentText(
            str(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'Subtype', 'PCM_16'))
        )
        self.ui.ComboBox_Tool_DatasetCreator_Subtype.currentTextChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'Subtype', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_TrainRatio,
            Title = "训练集占比",
            Body = QCA.translate("Label", "划分给训练集的数据在数据集中所占的比例。")
        )
        self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setRange(0.5, 0.9)
        self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setSingleStep(0.1)
        self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setValue(
            float(Config_Tool_DatasetCreator.GetValue('DatasetCreator', 'TrainRatio', '0.7'))
        )
        self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.valueChanged.connect(
            lambda Value: Config_Tool_DatasetCreator.EditConfig('DatasetCreator', 'TrainRatio', str(Value))
        )

        # Left
        Function_SetTreeWidget(
            TreeWidget = self.ui.TreeWidget_Catalogue_Tool_DatasetCreator,
            RootItemTexts = [self.ui.GroupBox_EssentialParams_Tool_DatasetCreator.title()],
            ChildItemTexts = [(self.ui.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator.text(),self.ui.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator.text())],
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

        # Right
        MonitorFile_Config_DatasetCreator = MonitorFile(Path_Config_Tool_DatasetCreator)
        MonitorFile_Config_DatasetCreator.start()
        MonitorFile_Config_DatasetCreator.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Tool_DatasetCreator.setText(
                FileContent
            )
        )

        self.ui.Button_SyncParams_Tool_DatasetCreator.setText("同步参数设置")
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
        Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Tool_DatasetCreator_Execute,
            TerminateButton = self.ui.Button_Tool_DatasetCreator_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_DatasetCreator,
            ConsoleFrame = self.ui.Frame_Console,
            Method = Execute_Dataset_Creating.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir,
                self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,
                self.ui.SpinBox_Tool_DatasetCreator_Sample_Rate,
                self.ui.ComboBox_Tool_DatasetCreator_Subtype,
                self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir_Split,
                self.ui.ComboBox_Tool_DatasetCreator_AutoEncoder,
                self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio,
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation
            ],
            FinishEventList = [
                Function_ShowMessageBox
            ],
            FinishParamList = [
                ("Ask","当前任务已执行完成，是否跳转至下一工具界面？",QMessageBox.Yes|QMessageBox.No,[QMessageBox.Yes],[[Function_AnimateStackedWidget,self.ui.Frame_Tools_Top.layout().itemAt(self.ui.StackedWidget_Pages_Tools.currentIndex()+1).widget().click]],[[(self.ui.StackedWidget_Pages_Tools,self.ui.StackedWidget_Pages_Tools.currentIndex()+1),()]])
            ]
        )

        ##################### Tool_VoiceTrainer #####################
        '''
        Function_SetText(
            Panel = self.ui.TextBrowser_Intro_Tool_VoiceTrainer,
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
        '''

        Path_Config_Tool_VoiceTrainer = os.path.join(CurrentDir, 'Config_Tool_VoiceTrainer.ini')
        Config_Tool_VoiceTrainer = ManageConfig(
            self.ManageConfig.GetValue(
                'ConfigPath',
                'Path_Config_Tool_VoiceTrainer',
                Path_Config_Tool_VoiceTrainer
            )
        )

        # Midlle
        self.ui.GroupBox_EssentialParams_Tool_VoiceTrainer.setTitle("必要参数")

        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer.setText("基础设置（显示）")
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer.setChecked(
            True #bool(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer,
            CheckedText = "基础设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceTrainer.EditConfig
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_FileList_Path_Training.height()+self.ui.Frame_Tool_VoiceTrainer_FileList_Path_Validation.height()+self.ui.Frame_Tool_VoiceTrainer_Language.height()+self.ui.Frame_Tool_VoiceTrainer_Epochs.height()+self.ui.Frame_Tool_VoiceTrainer_Batch_Size.height()+self.ui.Frame_Tool_VoiceTrainer_Config_Dir_Save.height()+self.ui.Frame_Tool_VoiceTrainer_Model_Dir_Save.height(),0,'Extend'),
                #('VoiceTrainer', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceTrainer.EditConfig
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_FileList_Path_Training.height()+self.ui.Frame_Tool_VoiceTrainer_FileList_Path_Validation.height()+self.ui.Frame_Tool_VoiceTrainer_Language.height()+self.ui.Frame_Tool_VoiceTrainer_Epochs.height()+self.ui.Frame_Tool_VoiceTrainer_Batch_Size.height()+self.ui.Frame_Tool_VoiceTrainer_Config_Dir_Save.height()+self.ui.Frame_Tool_VoiceTrainer_Model_Dir_Save.height(),0,'Reduce'),
                #('VoiceTrainer', 'Toggle_BasicSettings', 'False')
            ]
        )
        
        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_FileList_Path_Training,
            Title = "训练集文本路径",
            Body = QCA.translate("Label", "用于提供训练集音频路径及其语音内容的训练集txt文件的所在路径。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_FileList_Path_Training,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)"
        )
        self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training.setText(
            str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'FileList_Path_Training', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'FileList_Path_Training', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_FileList_Path_Validation,
            Title = "验证集文本路径",
            Body = QCA.translate("Label", "用于提供验证集音频路径及其语音内容的验证集txt文件的所在路径。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_FileList_Path_Validation,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation,
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)"
        )
        self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation.setText(
            str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'FileList_Path_Validation', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'FileList_Path_Validation', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Language,
            Title = "所用语言",
            Body = QCA.translate("Label", "音频中说话人所使用的语言。")
        )
        self.ui.ComboBox_Tool_VoiceTrainer_Language.addItems(['中', '中英日'])
        self.ui.ComboBox_Tool_VoiceTrainer_Language.setCurrentText(
            str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Language', '中英日'))
        )
        self.ui.ComboBox_Tool_VoiceTrainer_Language.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Language', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Epochs,
            Title = "迭代轮数",
            Body = QCA.translate("Label", "将全部样本完整迭代一轮的次数。")
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setRange(0, 1000000)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setValue(
            int(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Epochs', '10000'))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.valueChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Epochs', str(Value))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setToolTip("提示：建议为设置一万到两万以获得最佳效果")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Batch_Size,
            Title = "批处理量",
            Body = QCA.translate("Label", "每轮迭代中单位批次的样本数量，若用户GPU性能较弱可减小该值。")
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setRange(2, 128)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setSingleStep(2)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setValue(
            int(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Batch_Size', '16'))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.valueChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Batch_Size', str(Value))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setToolTip("注意：最好设置为2的幂次。")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Config_Dir_Save,
            Title = "配置保存目录",
            Body = QCA.translate("Label", "根据以上设置更新参数后的配置文件的保存目录。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Config_Dir_Save,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Config_Dir_Save,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Config_Dir_Save.setText(
            str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Config_Dir_Save', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Config_Dir_Save.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Config_Dir_Save', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save,
            Title = "模型保存目录",
            Body = QCA.translate("Label", "训练得到的模型的存放目录，若目录中已存在模型则会将其视为检查点。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Dir_Save,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save.setText(
            str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Model_Dir_Save', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Model_Dir_Save', str(Value))
        )
        self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save.setToolTipDuration(-1)
        self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save.setToolTip("提示：当目录中存在多个模型时，编号最大的那个会被选为检查点。")

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer.setText("高级设置（隐藏）")
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer,
            CheckedText = "高级设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Eval_Interval.height()+self.ui.Frame_Tool_VoiceTrainer_Num_Workers.height()+self.ui.Frame_Tool_VoiceTrainer_FP16_Run.height()+self.ui.Label_Tool_VoiceTrainer_Find_Unused_Parameters.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Eval_Interval.height()+self.ui.Frame_Tool_VoiceTrainer_Num_Workers.height()+self.ui.Frame_Tool_VoiceTrainer_FP16_Run.height()+self.ui.Label_Tool_VoiceTrainer_Find_Unused_Parameters.height(),0,'Reduce')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Eval_Interval,
            Title = "评估间隔",
            Body = QCA.translate("Label", "每次评估并保存模型所间隔的step数。")
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setRange(0, 10000)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setValue(
            int(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Eval_Interval', '1000'))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.valueChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Eval_Interval', str(Value))
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setToolTip("提示：建议设置为默认的一千以满足保存的需求")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Num_Workers,
            Title = "进程数量",
            Body = QCA.translate("Label", "进行数据加载时可并行的进程数量，若用户CPU性能较弱可减小该值。")
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
            Panel = self.ui.Label_Tool_VoiceTrainer_FP16_Run,
            Title = "半精度训练",
            Body = QCA.translate("Label", "通过混合了float16精度的训练方式减小显存占用以支持更大的批处理量。")
        )
        self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run.setText("已启用")
        self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run.setChecked(
            bool(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'FP16_Run', 'True'))
        )
        '''
        self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run.stateChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'FP16_Run', str(Value))
        )
        '''
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run,
            CheckedText = "已启用",
            CheckedPermEventList = [
                Config_Tool_VoiceTrainer.EditConfig
            ],
            CheckedPermArgsList = [
                ('VoiceTrainer', 'FP16_Run', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedPermEventList = [
                Config_Tool_VoiceTrainer.EditConfig
            ],
            UncheckedPermArgsList = [
                ('VoiceTrainer', 'FP16_Run', 'False')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Find_Unused_Parameters,
            Title = "寻找未用参数",
            Body = QCA.translate("Label", "寻找没用到的参数以防止在对梯度进行平均时报错，但会带来额外的运行开销。")
        )
        self.ui.CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters.setText("已启用")
        self.ui.CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters.setChecked(
            bool(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Find_Unused_Parameters', 'True'))
        )
        '''
        self.ui.CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters.stateChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceTrainer', 'Find_Unused_Parameters', str(Value))
        )
        '''
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters,
            CheckedText = "已启用",
            CheckedPermEventList = [
                Config_Tool_VoiceTrainer.EditConfig
            ],
            CheckedPermArgsList = [
                ('VoiceTrainer', 'Find_Unused_Parameters', 'True')
            ],
            UncheckedText = "未启用",
            UncheckedPermEventList = [
                Config_Tool_VoiceTrainer.EditConfig
            ],
            UncheckedPermArgsList = [
                ('VoiceTrainer', 'Find_Unused_Parameters', 'False')
            ]
        )

        self.ui.GroupBox_OptionalParams_Tool_VoiceTrainer.setTitle("可选参数")

        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer.setText("基础设置（显示）")
        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer.setChecked(
            True #bool(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Toggle_BasicOptionalSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer,
            CheckedText = "基础设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceTrainer.EditConfig
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_BasicOptionalSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G.height()+self.ui.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D.height(),0,'Extend'),
                #('VoiceTrainer', 'Toggle_BasicOptionalSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceTrainer.EditConfig
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_BasicOptionalSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G.height()+self.ui.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D.height(),0,'Reduce'),
                #('VoiceTrainer', 'Toggle_BasicOptionalSettings', 'False')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            Title = "预训练G_*模型路径",
            Body = QCA.translate("Label", "预训练生成器（Generator）模型的所在路径，载入优先级高于检查点。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)"
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G.setText(
            str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Model_Path_Pretrained_G', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Model_Path_Pretrained_G', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            Title = "预训练D_*模型路径",
            Body = QCA.translate("Label", "预训练判别器（Discriminator）模型的所在路径，载入优先级高于检查点。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)"
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D.setText(
            str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Model_Path_Pretrained_D', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Model_Path_Pretrained_D', str(Value))
        )

        self.ui.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer.setText("高级设置（隐藏）")
        self.ui.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer,
            CheckedText = "高级设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Config_Path_Load.height()+self.ui.Frame_Tool_VoiceTrainer_Speakers.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer,...,...,0,self.ui.Frame_Tool_VoiceTrainer_Config_Path_Load.height()+self.ui.Frame_Tool_VoiceTrainer_Speakers.height(),0,'Reduce')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Config_Path_Load,
            Title = "配置加载路径",
            Body = QCA.translate("Label", "该路径对应的配置文件将会替代默认的配置文件。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Config_Path_Load,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load,
            Mode = "SelectFile",
            FileType = "json类型 (*.json)"
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load.setText(
            str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Config_Path_Load', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load.textChanged.connect(
            lambda Value: Config_Tool_VoiceTrainer.EditConfig('VoiceTrainer', 'Config_Path_Load', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Speakers,
            Title = "人物名字",
            Body = QCA.translate("Label", "若数据集非本工具箱生成且未包含人名信息，则应按序号设置并用逗号隔开。")
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setReadOnly(False)
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setText(
            str(Config_Tool_VoiceTrainer.GetValue('VoiceTrainer', 'Speakers', ''))
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
        MonitorFile_Config_VoiceTrainer = MonitorFile(Path_Config_Tool_VoiceTrainer)
        MonitorFile_Config_VoiceTrainer.start()
        MonitorFile_Config_VoiceTrainer.Signal_FileContent.connect(
            lambda FileContent: self.ui.TextBrowser_Params_Tool_VoiceTrainer.setText(
                FileContent
            )
        )

        self.ui.Button_SyncParams_Tool_VoiceTrainer.setText("同步参数设置")
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
        Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Tool_VoiceTrainer_Execute,
            TerminateButton = self.ui.Button_Tool_VoiceTrainer_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_VoiceTrainer,
            ConsoleFrame = self.ui.Frame_Console,
            Method = Execute_Voice_Training.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation,
                self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,
                self.ui.ComboBox_Tool_VoiceTrainer_Language,
                self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load,
                self.ui.LineEdit_Tool_VoiceTrainer_Config_Dir_Save,
                self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval,
                self.ui.SpinBox_Tool_VoiceTrainer_Epochs,
                self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size,
                self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run,
                self.ui.LineEdit_Tool_VoiceTrainer_Speakers,
                self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers,
                self.ui.CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters,
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
                ("Ask","当前任务已执行完成，是否跳转至下一工具界面？",QMessageBox.Yes|QMessageBox.No,[QMessageBox.Yes],[[Function_AnimateStackedWidget,self.ui.Frame_Tools_Top.layout().itemAt(self.ui.StackedWidget_Pages_Tools.currentIndex()+1).widget().click]],[[(self.ui.StackedWidget_Pages_Tools,self.ui.StackedWidget_Pages_Tools.currentIndex()+1),()]])
            ]
        )

        ##################### Tool_VoiceConverter #####################
        '''
        Function_SetText(
            Panel = self.ui.TextBrowser_Intro_Tool_VoiceConverter,
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
        '''

        Path_Config_Tool_VoiceConverter = os.path.join(CurrentDir, 'Config_Tool_VoiceConverter.ini')
        Config_Tool_VoiceConverter = ManageConfig(
            self.ManageConfig.GetValue(
                'ConfigPath',
                'Path_Config_Tool_VoiceConverter',
                Path_Config_Tool_VoiceConverter
            )
        )

        # Middle
        self.ui.GroupBox_EssentialParams_Tool_VoiceConverter.setTitle(QCA.translate("GroupBox", "必要参数"))

        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter.setText("基础设置（显示）")
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter.setCheckable(True)
        self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter.setChecked(
            True #bool(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Toggle_BasicSettings', ''))
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter,
            CheckedText = "基础设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceConverter.EditConfig
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceConverter,...,...,0,self.ui.Frame_Tool_VoiceConverter_Config_Path_Load.height()+self.ui.Frame_Tool_VoiceConverter_Model_Path_Load.height()+self.ui.Frame_Tool_VoiceConverter_Text.height()+self.ui.Frame_Tool_VoiceConverter_Language.height(),0,'Extend'),
                #('VoiceConverter', 'Toggle_BasicSettings', 'True')
            ],
            UncheckedText = "基础设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame,
                #Config_Tool_VoiceConverter.EditConfig
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_BasicSettings_Tool_VoiceConverter,...,...,0,self.ui.Frame_Tool_VoiceConverter_Config_Path_Load.height()+self.ui.Frame_Tool_VoiceConverter_Model_Path_Load.height()+self.ui.Frame_Tool_VoiceConverter_Text.height()+self.ui.Frame_Tool_VoiceConverter_Language.height(),0,'Reduce'),
                #('VoiceConverter', 'Toggle_BasicSettings', 'False')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_Config_Path_Load,
            Title = "配置加载路径",
            Body = QCA.translate("Label", "用于推理的配置文件的所在路径。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceConverter_Config_Path_Load,
            LineEdit = self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load,
            Mode = "SelectFile",
            FileType = "json类型 (*.json)"
        )
        self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load.setText(
            str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Config_Path_Load', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load.textChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'Config_Path_Load', str(Value))
        )
        self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load.textChanged.connect(
            lambda Path: self.ui.ComboBox_Tool_VoiceConverter_Speaker.addItems(
                Get_Speakers(Path)
            )
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_Model_Path_Load,
            Title = "G_*模型加载路径",
            Body = QCA.translate("Label", "用于推理的生成器（Generator）模型的所在路径。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceConverter_Model_Path_Load,
            LineEdit = self.ui.LineEdit_Tool_VoiceConverter_Model_Path_Load,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)"
        )
        self.ui.LineEdit_Tool_VoiceConverter_Model_Path_Load.setText(
            str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Model_Path_Load', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceConverter_Model_Path_Load.textChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'Model_Path_Load', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_Text,
            Title = "输入文字",
            Body = QCA.translate("Label", "输入的文字会作为说话人的语音内容。")
        )
        self.ui.PlainTextEdit_Tool_VoiceConverter_Text.setPlainText(
            str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Text', '请输入语句'))
        )
        self.ui.PlainTextEdit_Tool_VoiceConverter_Text.textChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'Text', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_Language,
            Title = "所用语言",
            Body = QCA.translate("Label", "说话人/文字所使用的语言。")
        )
        self.ui.ComboBox_Tool_VoiceConverter_Language.addItems(['中', '英', '日'])
        self.ui.ComboBox_Tool_VoiceConverter_Language.setCurrentText(
            str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Language', '中'))
        )
        self.ui.ComboBox_Tool_VoiceConverter_Language.currentTextChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'Language', str(Value))
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_Speaker,
            Title = "人物名字",
            Body = QCA.translate("Label", "说话人物的名字。")
        )
        #self.ui.ComboBox_Tool_VoiceConverter_Speaker.addItems(Get_Speakers)
        self.ui.ComboBox_Tool_VoiceConverter_Speaker.setCurrentText('')

        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter.setText("高级设置（隐藏）")
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter.setCheckable(True)
        self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter.setChecked(False)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter,
            CheckedText = "高级设置（显示）",
            CheckedPermEventList = [
                Function_AnimateFrame
            ],
            CheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceConverter,...,...,0,self.ui.Frame_Tool_VoiceConverter_EmotionStrength.height()+self.ui.Frame_Tool_VoiceConverter_PhonemeDuration.height()+self.ui.Frame_Tool_VoiceConverter_SpeechRate.height(),0,'Extend')
            ],
            UncheckedText = "高级设置（隐藏）",
            UncheckedPermEventList = [
                Function_AnimateFrame
            ],
            UncheckedPermArgsList = [
                (self.ui.Frame_AdvanceSettings_Tool_VoiceConverter,...,...,0,self.ui.Frame_Tool_VoiceConverter_EmotionStrength.height()+self.ui.Frame_Tool_VoiceConverter_PhonemeDuration.height()+self.ui.Frame_Tool_VoiceConverter_SpeechRate.height(),0,'Reduce')
            ]
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_EmotionStrength,
            Title = "情感强度",
            Body = QCA.translate("Label", "情感的变化程度。")
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setMinimum(0)
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setMaximum(100)
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setTickInterval(1)
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setValue(
            int(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'EmotionStrength', '67'))
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.valueChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'EmotionStrength', str(Value))
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
            Panel = self.ui.Label_Tool_VoiceConverter_PhonemeDuration,
            Title = "音素音长",
            Body = QCA.translate("Label", "音素的发音长度。")
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setMinimum(0)
        self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setMaximum(10)
        self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setTickInterval(1)
        self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setValue(
            int(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'PhonemeDuration', '8'))
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.valueChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'PhonemeDuration', str(Value))
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
            Panel = self.ui.Label_Tool_VoiceConverter_SpeechRate,
            Title = "整体语速",
            Body = QCA.translate("Label", "整体的说话速度。")
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setMinimum(0)
        self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setMaximum(20)
        self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setTickInterval(1)
        self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setValue(
            int(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'SpeechRate', '10'))
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate.valueChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'SpeechRate', str(Value))
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

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_Audio_Dir_Save,
            Title = "音频保存目录",
            Body = QCA.translate("Label", "推理得到的音频会保存到该目录。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceConverter_Audio_Dir_Save,
            LineEdit = self.ui.LineEdit_Tool_VoiceConverter_Audio_Dir_Save,
            Mode = "SelectDir"
        )
        self.ui.LineEdit_Tool_VoiceConverter_Audio_Dir_Save.setText(
            str(Config_Tool_VoiceConverter.GetValue('VoiceConverter', 'Audio_Dir_Save', 'None'))
        )
        self.ui.LineEdit_Tool_VoiceConverter_Audio_Dir_Save.textChanged.connect(
            lambda Value: Config_Tool_VoiceConverter.EditConfig('VoiceConverter', 'Audio_Dir_Save', str(Value))
        )

        # Right
        MonitorFile_Config_VoiceConverter = MonitorFile(Path_Config_Tool_VoiceConverter)
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
        Function_ExecuteMethod(
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
                ("Tip","当前任务已执行完成！",QMessageBox.Ok)
            ]
        )

        #############################################################
        ##################### Content: Settings #####################
        #############################################################

        self.ui.ToolButton_Settings_Title.setText(QCA.translate("Label", "设置"))

        self.ui.Label_Setting_Language.setText(QCA.translate("Label", "语言"))
        self.ui.ComboBox_Setting_Language.addItems(['中文'])
        self.ui.ComboBox_Setting_Language.setCurrentText(
            ItemReplacer(
                Dict = {
                    'Chinese': '中文'
                },
                Item = self.ManageConfig.GetValue(
                    'Settings',
                    'Language',
                    'Chinese'
                )
            )
        )
        self.ui.ComboBox_Setting_Language.currentIndexChanged.connect(
            lambda: self.ManageConfig.EditConfig(
                'Settings',
                'Language',
                ItemReplacer(
                    Dict = {
                        '中文': 'Chinese'
                    },
                    Item = self.ui.ComboBox_Setting_Language.currentText()
                )
            )
        )

        self.ui.Label_Setting_AutoUpdate.setText(QCA.translate("Label", "自动检查版本并更新"))
        self.ui.CheckBox_Setting_AutoUpdate.setText("已启用")
        self.ui.CheckBox_Setting_AutoUpdate.setCheckable(True)
        self.ui.CheckBox_Setting_AutoUpdate.setChecked(
            ItemReplacer(
                Dict = {
                    'Enabled': True,
                    'Disabled': False
                },
                Item = self.ManageConfig.GetValue('Settings', 'AutoUpdate', 'Enabled')
            )
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Setting_AutoUpdate,
            CheckedText = "已启用",
            CheckedPermEventList = [
                self.ManageConfig.EditConfig,
                Updater
            ],
            CheckedPermArgsList = [
                ('Settings', 'AutoUpdate', 'Enabled'),
                (CurrentVersion, CurrentDir, f'Easy Voice Toolkit {CurrentVersion}', CurrentDir)
            ],
            UncheckedText = "未启用",
            UncheckedPermEventList = [
                self.ManageConfig.EditConfig
            ],
            UncheckedPermArgsList = [
                ('Settings', 'AutoUpdate', 'Disabled')
            ]
        )

        self.ui.Label_Setting_Synchronizer.setText(QCA.translate("Label", "自动同步前后工具的部分参数设置"))
        self.ui.CheckBox_Setting_Synchronizer.setText("已启用")
        self.ui.CheckBox_Setting_Synchronizer.setCheckable(True)
        self.ui.CheckBox_Setting_Synchronizer.setChecked(
            ItemReplacer(
                Dict = {
                    'Enabled': True,
                    'Disabled': False
                },
                Item = self.ManageConfig.GetValue('Tools', 'Synchronizer', 'Enabled')
            )
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Setting_Synchronizer,
            CheckedText = "已启用",
            CheckedPermEventList = [
                self.ManageConfig.EditConfig,
                Function_ParamsSynchronizer,
                Function_ParamsSynchronizer,
                Function_ParamsSynchronizer,
                Function_ParamsSynchronizer
            ],
            CheckedPermArgsList = [
                ('Tools', 'Synchronizer', 'Enabled'),
                (self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,[self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output],None,[self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input]),
                (self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,[self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output],None,[self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir]),
                ([self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir],[self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir],None,[self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir]),
                ([self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation],[self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation],None,[self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation]),
            ],
            UncheckedText = "未启用",
            UncheckedPermEventList = [
                self.ManageConfig.EditConfig,
                #Function_ParamsSynchronizer,
                #Function_ParamsSynchronizer,
                #Function_ParamsSynchronizer,
                #Function_ParamsSynchronizer
            ],
            UncheckedPermArgsList = [
                ('Tools', 'Synchronizer', 'Disabled'),
                #(self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,[self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output],None,[self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input],"Disconnect"),
                #(self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,[self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output],None,[self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir],"Disconnect"),
                #([self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir],[self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir],None,[self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir],"Disconnect"),
                #([self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation],[self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation],None,[self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation],"Disconnect"),
            ],
            UncheckedTempEventList = [
                Function_ShowMessageBox
            ],
            UncheckedTempArgsList = [
                (QMessageBox.Information, "提示", "该设置将于重启之后生效")
            ]
        )

        #####################################################################################################
        # StatusBar
        #####################################################################################################

        # Toggle Console
        self.ui.Button_Toggle_Console.setCheckable(True)
        self.ui.Button_Toggle_Console.setChecked(False)
        self.ui.Button_Toggle_Console.setAutoExclusive(False)
        self.ui.Button_Toggle_Console.setToolTipDuration(-1)
        self.ui.Button_Toggle_Console.setToolTip("Click to toggle console")
        self.ui.Button_Toggle_Console.clicked.connect(
            lambda: Function_AnimateFrame(
                Frame = self.ui.Frame_Console,
                MinHeight = 0,
                MaxHeight = 210
            )
        )

        # Print ConsoleInfo
        #QFunctionsSignals.Signal_FrameStatus.connect(lambda FrameStatus: 
        self.ConsoleInfo.Signal_ConsoleInfo.connect(
            lambda Info: Function_PrintText(
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
            lambda Index: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages_Tools,
                TargetIndex = Index - 1
            )
        )
        self.ui.SpinBox_Tools.valueChanged.connect(
            lambda Index: self.ui.ComboBox_Tools.setCurrentIndex(Index - 1)
        )
        '''
        # Display ToolsStatus
        self.ui.Label_ToolsStatus.setText("工具状态：")

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


if __name__ == "__main__":
    App = QApplication(sys.argv)

    Window = MainWindow()
    Window.Main()
    
    sys.exit(App.exec())