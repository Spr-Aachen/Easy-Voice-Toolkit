import os
import sys
import json
from PySide6 import __file__ as PySide6_File
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtCore import QCoreApplication as QCA
from PySide6.QtWidgets import *

from GUI.WindowCustomizer import Window_Customizing
from GUI.UI import Ui_MainWindow
from GUI.QFunctions import *
from GUI.Utils import *
from EnvConfigurator.Configure import Env_Configurator
from Tool_AudioProcessor.Process import Audio_Processing
from Tool_VoiceIdentifier.Identify import Voice_Identifying
from Tool_VoiceTranscriber.Transcribe import Voice_Transcribing
from Tool_DatasetCreator.Create import Dataset_Creating
from Tool_VoiceTrainer.Train import Voice_Training
from Tool_VoiceConverter.Convert import Voice_Converting


# Current version
CurrentVersion = "v1.0.0"


# Set workdir
CurrentDir = os.path.dirname(os.path.abspath('__file__'))
os.chdir(CurrentDir)


# Redirect PATH environment variable 'QT_QPA_PLATFORM_PLUGIN_PATH' to Pyside6 '/plugins/platforms' folder's path
PySide6_Dirname = os.path.dirname(PySide6_File)
PySide6_PluginPath = os.path.join(PySide6_Dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = PySide6_PluginPath


# Task: Configurate environment
class Execute_Env_Configurator(QObject):
    '''
    Install ffmpeg
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    @Slot()
    def Execute(self):
        Env_Configurator.FFmpeg_Installer()

        self.finished.emit()


# Tool1: AudioProcessor
class Execute_Audio_Processing(QObject):
    '''
    Change media format to WAV and cut off the silent parts
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    @Slot(list)
    def Execute(self, Params):
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

    @Slot(list)
    def Execute(self, Params):
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

    @Slot(list)
    def Execute(self, Params):
        LANGUAGES = {
            "中":      "zh",
            "Chinese": "zh",
            "英":      "en",
            "English": "en"
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

    @Slot(list)
    def Execute(self, Params):
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

    @Slot(list)
    def Execute(self, Params):
        LANGUAGES = {
            "中":                 "mandarin",
            "Mandarin":           "mandarin",
            "中英":               "mandarin_english",
            "Mandarin & English": "mandarin_english"
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
        with open(Config_Path_Load, "r") as File:
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

    @Slot(list)
    def Execute(self, Params):
        LANGUAGES = {
            "中":      "[ZH]",
            "Chinese": "[ZH]",
            "英":      "[EN]",
            "English": "[EN]"
        }
        TTS = Voice_Converting(*ItemReplacer(LANGUAGES, Params))
        TaskAccelerating(
            TargetList = [TTS.Converting],
            ArgsList = [()],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()


# Show GUI
class MainWindow(Window_Customizing):
    '''
    Show the user interface
    '''
    def __init__(self):
        Window_Customizing.__init__(self,
            parent = None,
            window_title = QCA.translate("Window", "简易语音工具箱")
        )

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ConsoleInfo = ConsolOutputHandler()
        self.ConsoleInfo.start()

        self.MonitorUsage = MonitorUsage()
        self.MonitorUsage.start()

        self.ManageConfig = ManageConfig(os.path.join(CurrentDir, 'Config.ini'))

    def Main(self):
        '''
        Main funtion to orgnize all the subfunctions
        '''
        self.ui.Label_Page.setText(QCA.translate("Label", "主页"))

        # Toggle Menu
        self.ui.Button_Toggle_Menu.clicked.connect(
            lambda: Function_AnimateFrame(
                Frame = self.ui.Frame_Menu,
                MinWidth = 45,
                MaxWidth = 159
            )
        )
        self.ui.Button_Toggle_Menu.setCheckable(True)
        self.ui.Button_Toggle_Menu.setChecked(False)
        self.ui.Button_Toggle_Menu.setAutoExclusive(False)
        self.ui.Button_Toggle_Menu.setToolTipDuration(-1)
        self.ui.Button_Toggle_Menu.setToolTip(QCA.translate("ToolTip", "点击以展开/折叠菜单"))

        # Print Titles & Choose Pages
        Signals.Signal_FrameStatus.connect(
            lambda FrameStatus: Function_AnimateButton(
                Button = self.ui.Button_Page_Home,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Button", "主页")
            )
        )
        self.ui.Button_Page_Home.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 0
            )
        )
        self.ui.Button_Page_Home.clicked.connect(
            lambda: self.ui.Label_Page.setText(QCA.translate("Label", "主页"))
        )
        self.ui.Button_Page_Home.setCheckable(True)
        self.ui.Button_Page_Home.setChecked(True)
        self.ui.Button_Page_Home.setAutoExclusive(True)
        self.ui.Button_Page_Home.setToolTipDuration(-1)
        self.ui.Button_Page_Home.setToolTip(QCA.translate("ToolTip", "主页"))

        Signals.Signal_FrameStatus.connect(
            lambda FrameStatus: Function_AnimateButton(
                Button = self.ui.Button_Page_Tools,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Button", "工具")
            )
        )
        self.ui.Button_Page_Tools.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 1
            )
        )
        self.ui.Button_Page_Tools.clicked.connect(
            lambda: self.ui.Label_Page.setText(QCA.translate("Label", "工具"))
        )
        self.ui.Button_Page_Tools.setCheckable(True)
        self.ui.Button_Page_Tools.setChecked(False)
        self.ui.Button_Page_Tools.setAutoExclusive(True)
        self.ui.Button_Page_Tools.setToolTipDuration(-1)
        self.ui.Button_Page_Tools.setToolTip(QCA.translate("ToolTip", "工具"))

        Signals.Signal_FrameStatus.connect(
            lambda FrameStatus: Function_AnimateButton(
                Button = self.ui.Button_Page_Settings,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = QCA.translate("Button", "设置")
            )
        )
        self.ui.Button_Page_Settings.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 2
            )
        )
        self.ui.Button_Page_Settings.clicked.connect(
            lambda: self.ui.Label_Page.setText(QCA.translate("Label", "设置"))
        )
        self.ui.Button_Page_Settings.setCheckable(True)
        self.ui.Button_Page_Settings.setChecked(False)
        self.ui.Button_Page_Settings.setAutoExclusive(True)
        self.ui.Button_Page_Settings.setToolTipDuration(-1)
        self.ui.Button_Page_Settings.setToolTip(QCA.translate("ToolTip", "设置"))

        # Page0: Home
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

        self.ui.Button_Demo.setText(QCA.translate("Button", "视频演示"))
        Function_SetURL(
            Button = self.ui.Button_Demo,
            URL = "https://www.bilibili.com/video/BV",
            ButtonTooltip = "Click to view demo video"
        )
        self.ui.Button_Server.setText(QCA.translate("Button", "云端版本"))
        Function_SetURL(
            Button = self.ui.Button_Server,
            URL = "https://colab.research.google.com/github/Spr-Aachen/EVT-Resources/blob/main/Easy_Voice_Toolkit_for_Colab.ipynb",
            ButtonTooltip = "Click to run on server"
        )
        self.ui.Button_Repo.setText(QCA.translate("Button", "项目仓库"))
        Function_SetURL(
            Button = self.ui.Button_Repo,
            URL = "https://github.com/Spr-Aachen/Easy-Voice-Toolkit",
            ButtonTooltip = "Click to view github repo"
        )
        self.ui.Button_Donate.setText(QCA.translate("Button", "赞助作者"))
        Function_SetURL(
            Button = self.ui.Button_Donate,
            URL = "https://",
            ButtonTooltip = "Click to buy him a coffee"
        )

        # Page1: Tools
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

        self.ui.Label_Tools_Synchronizer.setText(QCA.translate("Label", "自动同步前后工具的部分参数设置"))
        self.ui.CheckBox_Tools_Synchronizer.setText("已启用")
        self.ui.CheckBox_Tools_Synchronizer.setCheckable(True)
        self.ui.CheckBox_Tools_Synchronizer.setChecked(
            ItemReplacer(
                Dict = {
                    'Enabled': True,
                    'Disabled': False
                },
                Item = self.ManageConfig.GetValue('Tools', 'Synchronizer', 'Enabled')
            )
        )
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tools_Synchronizer,
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

        # Tool_AudioProcessor
        Function_SetText(
            Panel = self.ui.TextBrowser_Tool_AudioProcessor,
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
                "1. 运行工具前请确保已经正确安装了FFmpeg\n"
                "2. 您可以通过点击“打开输出目录”按钮以查看当前工具在执行完毕后输出的文件\n"
            )
        )

        self.ui.Button_Install_FFmpeg.setText(QCA.translate("Button", "安装FFmpeg"))
        Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Install_FFmpeg,
            TerminateButton = None,
            ProgressBar = None,
            ConsoleFrame = self.ui.Frame_Console,
            Method = Execute_Env_Configurator.Execute
        )

        self.ui.Button_CheckOutput_Tool_AudioProcessor.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Tool_AudioProcessor,
            URL = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,
            ButtonTooltip = "Click to open"
        )

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
            ]
        )

        self.ui.GroupBox_EssentialParams_Tool_AudioProcessor.setTitle(QCA.translate("GroupBox", "必要参数"))

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Media_Dir_Input,
            Title = QCA.translate("Label", "媒体输入目录"),
            Body = QCA.translate("Label", "该目录中的媒体文件将会以下列设置输出为音频文件。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_AudioProcessor_Media_Dir_Input,
            LineEdit = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Input,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Media_Format_Output,
            Title = QCA.translate("Label", "媒体输出格式"),
            Body = QCA.translate("Label", "媒体文件将会以设置的格式输出为音频文件。")
        )
        self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output.addItems(['wav', 'mp3'])
        self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output.setCurrentText('wav')

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_RMS_Threshold,
            Title = QCA.translate("Label", "均方根阈值 (db)"),
            Body = QCA.translate("Label", "低于该阈值的片段将被视作静音进行处理，若有降噪需求可以增加该值。")
        )
        #self.ui.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setValue(-40.)

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Hop_Size,
            Title = QCA.translate("Label", "跳跃大小 (ms)"),
            Body = QCA.translate("Label", "每个RMS帧的长度，增加该值能够提高分割精度但会减慢进程。")
        )
        self.ui.SpinBox_Tool_AudioProcessor_Hop_Size.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Hop_Size.setValue(10)

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Silent_Interval_Min,
            Title = QCA.translate("Label", "最小静音间隔 (ms)"),
            Body = QCA.translate("Label", "静音部分被分割成的最小长度，若音频只包含短暂中断可以减小该值。")
        )
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setValue(300)
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setToolTip(QCA.translate("ToolTip", "注意：这个值必须小于 Audio Length Min，大于 Hop Size。"))

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Silence_Kept_Max,
            Title = QCA.translate("Label", "最大静音长度 (ms)"),
            Body = QCA.translate("Label", "被分割的音频周围保持静音的最大长度。")
        )
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setValue(1000)
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setToolTip(QCA.translate("ToolTip", "注意：这个值无需完全对应被分割音频中的静音长度。算法将自行检索最佳的分割位置。"))

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Audio_Length_Min,
            Title = QCA.translate("Label", "最小音频长度 (ms)"),
            Body = QCA.translate("Label", "每个被分割的音频片段所需的最小长度。")
        )
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setValue(5000)

        Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Media_Dir_Output,
            Title = QCA.translate("Label", "媒体输出目录"),
            Body = QCA.translate("Label", "最后生成的音频文件将被保存到该目录中。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_AudioProcessor_Media_Dir_Output,
            LineEdit = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        # Tool_VoiceIdentifier
        Function_SetText(
            Panel = self.ui.TextBrowser_Tool_VoiceIdentifier,
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
                "\n"
                "[提示]\n"
                "1. 您可以通过开启“自动同步...”选项以保持前后工具的部分参数设置一致，或者点击“同步...”按钮以快速设置当前工具的下列参数：\n"
                "   Audio Dir Input\n"
                "2. 您可以通过点击“打开输出目录”按钮以查看当前工具在执行完毕后输出的文件\n"
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
                self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Path_Std,
                self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input,
                self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,
                self.ui.LineEdit_Tool_VoiceIdentifier_Model_Dir,
                self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type,
                self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name,
                self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method,
                self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold,
                self.ui.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio,
                self.ui.LineEdit_Tool_VoiceIdentifier_Speaker
            ],
            EmptyAllowed = [
                self.ui.LineEdit_Tool_VoiceIdentifier_Speaker
            ]
        )

        self.ui.GroupBox_EssentialParams_Tool_VoiceIdentifier.setTitle("EssentialParams 必要参数")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Audio_Dir_Input,
            Title = "音频输入目录",
            Body = QCA.translate("Label", "该目录中的音频文件将会按照以下设置进行识别筛选。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Audio_Dir_Input,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "无")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Audio_Path_Std,
            Title = "标准音频路径",
            Body = QCA.translate("Label", "该路径对应的音频将会作为识别的比对标准，即期望值。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Audio_Path_Std,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Path_Std,
            Mode = "SelectFile",
            FileType = "音频类型 (*.mp3 *.aac *.wav *.flac)",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Model_Dir,
            Title = "模型存放目录",
            Body = QCA.translate("Label", "该目录将会用于存放下载的声纹识别模型，若模型已存在会直接使用。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Model_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Model_Dir,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Model_Type,
            Title = "模型类型",
            Body = QCA.translate("Label", "声纹识别模型的类型。")
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type.addItems(['Ecapa-Tdnn'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type.setCurrentText('Ecapa-Tdnn')

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Model_Name,
            Title = "模型名字",
            Body = QCA.translate("Label", "声纹识别模型的名字，默认代表模型的大小。")
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name.addItems(['small'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name.setCurrentText('small')

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Feature_Method,
            Title = "特征提取方法",
            Body = QCA.translate("Label", "音频特征的提取方法。")
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method.addItems(['spectrogram', 'melspectrogram'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method.setCurrentText('spectrogram')

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_DecisionThreshold,
            Title = "判断阈值",
            Body = QCA.translate("Label", "判断是否为同一人的阈值，若参与比对的说话人声音相识度较高可以增加该值。")
        )
        #self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setValue(0.75)

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Duration_of_Audio,
            Title = "音频长度",
            Body = QCA.translate("Label", "用于预测的音频长度。")
        )
        #self.ui.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setValue(3.00)

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Audio_Dir_Output,
            Title = "音频输出目录",
            Body = QCA.translate("Label", "最后筛选出的音频文件将被复制到该目录中。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Audio_Dir_Output,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        self.ui.GroupBox_OptionalParams_Tool_VoiceIdentifier.setTitle("OptionalParams 可选参数")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Speaker,
            Title = "人物名字",
            Body = QCA.translate("Label", "说话人物的名字，若有进行语音模型训练的需求则推荐设置。")
        )
        self.ui.LineEdit_Tool_VoiceIdentifier_Speaker.setText("")
        self.ui.LineEdit_Tool_VoiceIdentifier_Speaker.setToolTipDuration(-1)
        self.ui.LineEdit_Tool_VoiceIdentifier_Speaker.setToolTip("注意：名字中尽量不要出现特殊符号")

        # Tool_VoiceTranscriber
        Function_SetText(
            Panel = self.ui.TextBrowser_Tool_VoiceTranscriber,
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
            ]
        )

        self.ui.GroupBox_EssentialParams_Tool_VoiceTranscriber.setTitle("EssentialParams 必要参数")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_WAV_Dir,
            Title = "音频目录",
            Body = QCA.translate("Label", "该目录中的wav文件的语音内容将会按照以下设置转为文字。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_WAV_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Model_Dir,
            Title = "模型存放目录",
            Body = QCA.translate("Label", "该目录将会用于存放下载的语音识别模型，若模型已存在会直接使用。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_Model_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_Model_Dir,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Model_Name,
            Title = "模型名字",
            Body = QCA.translate("Label", "语音识别 (whisper) 模型的名字，默认代表模型的大小。")
        )
        self.ui.ComboBox_Tool_VoiceTranscriber_Model_Name.addItems(['tiny', 'base', 'small', 'medium', 'large'])
        self.ui.ComboBox_Tool_VoiceTranscriber_Model_Name.setCurrentText('small')

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Verbose,
            Title = "启用输出日志",
            Body = QCA.translate("Label", "输出debug日志。")
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_Verbose.setText("已启用")
        self.ui.CheckBox_Tool_VoiceTranscriber_Verbose.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_Verbose.setChecked(True)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTranscriber_Verbose,
            CheckedText = "已启用",
            UncheckedText = "未启用"
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Condition_on_Previous_Text,
            Title = "前后文一致",
            Body = QCA.translate("Label", "将模型之前的输出作为下个窗口的提示，若模型陷入了失败循环则禁用此项。")
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setText("已启用")
        self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setChecked(True)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text,
            CheckedText = "已启用",
            UncheckedText = "未启用"
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_fp16,
            Title = "半精度",
            Body = QCA.translate("Label", "主要使用半精度浮点数进行计算，若GPU不可用则忽略或禁用此项。")
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_fp16.setText("已启用")
        self.ui.CheckBox_Tool_VoiceTranscriber_fp16.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_fp16.setChecked(True)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTranscriber_fp16,
            CheckedText = "已启用",
            UncheckedText = "未启用"
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_SRT_Dir,
            Title = "字幕输出目录",
            Body = QCA.translate("Label", "最后生成的字幕文件将会保存到该目录中。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_SRT_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        self.ui.GroupBox_OptionalParams_Tool_VoiceTranscriber.setTitle("OptionalParams 可选参数")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Language,
            Title = "所用语言",
            Body = QCA.translate("Label", "音频中说话人所使用的语言，若存在多种语言则保持'None'即可。")
        )
        self.ui.ComboBox_Tool_VoiceTranscriber_Language.addItems(['中', '英', 'None'])
        self.ui.ComboBox_Tool_VoiceTranscriber_Language.setCurrentText('None')

        # Tool_DatasetCreator
        Function_SetText(
            Panel = self.ui.TextBrowser_Tool_DatasetCreator,
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
                "2. 您可以通过点击“打开输出目录”按钮以查看当前工具在执行完毕后输出的文件\n"
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

        self.ui.Button_CheckOutput_Tool_DatasetCreator.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Tool_DatasetCreator,
            URL = [
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation
            ],
            ButtonTooltip = "Click to open"
        )

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
            ]
        )

        self.ui.GroupBox_EssentialParams_Tool_DatasetCreator.setTitle("EssentialParams 必要参数")

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_WAV_Dir,
            Title = "音频输入目录",
            Body = QCA.translate("Label", "该目录中的wav文件将会按照以下设置重采样并根据字幕时间戳进行分割。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_WAV_Dir,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_Sample_Rate,
            Title = "采样率 (HZ)",
            Body = QCA.translate("Label", "音频将要使用的新采样率。")
        )
        self.ui.SpinBox_Tool_DatasetCreator_Sample_Rate.setSingleStep(1)
        self.ui.SpinBox_Tool_DatasetCreator_Sample_Rate.setValue(22050)

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_Subtype,
            Title = "采样格式",
            Body = QCA.translate("Label", "音频将要使用的新采样格式。")
        )
        self.ui.ComboBox_Tool_DatasetCreator_Subtype.addItems(['PCM_16'])
        self.ui.ComboBox_Tool_DatasetCreator_Subtype.setCurrentText('PCM_16')

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_WAV_Dir_Split,
            Title = "音频输出目录",
            Body = QCA.translate("Label", "最后处理完成的音频将会保存到该目录中。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_WAV_Dir_Split,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir_Split,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_SRT_Dir,
            Title = "字幕输入目录",
            Body = QCA.translate("Label", "该目录中的srt文件将会按照以下设置转为适用于模型训练的csv文件。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_SRT_Dir,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_AutoEncoder,
            Title = "自编码器",
            Body = QCA.translate("Label", "模型训练所使用的自动编码器。")
        )
        self.ui.ComboBox_Tool_DatasetCreator_AutoEncoder.addItems(['VITS'])
        self.ui.ComboBox_Tool_DatasetCreator_AutoEncoder.setCurrentText('VITS')

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_TrainRatio,
            Title = "训练集占比",
            Body = QCA.translate("Label", "划分给训练集的数据在数据集中所占的比例。")
        )
        self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setRange(0.5, 0.9)
        self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setSingleStep(0.1)
        self.ui.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setValue(0.7)

        Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_FileList_Path_Training,
            Title = "训练集文本路径",
            Body = QCA.translate("Label", "最后生成的训练集txt文件将会保存到该路径。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_FileList_Path_Training,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
            Mode = "SaveFile",
            FileType = "txt类型 (*.txt)",
            DisplayText = QCA.translate("LineEdit", "None")
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
            FileType = "txt类型 (*.txt)",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        # Tool_VoiceTrainer
        Function_SetText(
            Panel = self.ui.TextBrowser_Tool_VoiceTrainer,
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
                "\n"
                "[提示]\n"
                "1. 您可以通过开启“自动同步...”选项以保持前后工具的部分参数设置一致，或者点击“同步...”按钮以快速设置当前工具的下列参数：\n"
                "   FileList Path Training\n"
                "   FileList Path Validation\n"
                "2. 您可以通过点击“打开输出目录”按钮以查看当前工具在执行完毕后输出的文件\n"
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
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save
            ],
            EmptyAllowed = [
                self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D,
                self.ui.LineEdit_Tool_VoiceTrainer_Speakers
            ]
        )

        self.ui.GroupBox_EssentialParams_Tool_VoiceTrainer.setTitle("EssentialParams 必要参数")
        
        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_FileList_Path_Training,
            Title = "训练集文本路径",
            Body = QCA.translate("Label", "该路径对应的训练集txt文件将用于提供训练集音频路径及其语音内容。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_FileList_Path_Training,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_FileList_Path_Validation,
            Title = "验证集文本路径",
            Body = QCA.translate("Label", "该路径对应的验证集txt文件将用于提供验证集音频路径及其语音内容。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_FileList_Path_Validation,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation,
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Language,
            Title = "所用语言",
            Body = QCA.translate("Label", "音频中说话人所使用的语言。")
        )
        self.ui.ComboBox_Tool_VoiceTrainer_Language.addItems(['中', '中英'])
        self.ui.ComboBox_Tool_VoiceTrainer_Language.setCurrentText('中英')

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Eval_Interval,
            Title = "评估间隔",
            Body = QCA.translate("Label", "每次评估并保存模型所间隔的step数。")
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setValue(1000)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setToolTip("提示：建议设置为默认的一千以满足保存的需求")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Epochs,
            Title = "迭代轮数",
            Body = QCA.translate("Label", "将全部样本完整迭代一轮的次数。")
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setValue(10000)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setToolTip("提示：建议为设置一万到两万以获得最佳效果")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Batch_Size,
            Title = "批处理量",
            Body = QCA.translate("Label", "每轮迭代中单位批次的样本数量，若用户GPU性能较弱可减小该值。")
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setValue(16)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setToolTip("注意：最好设置为2的幂次，若设置为1会导致网络很难收敛。")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Num_Workers,
            Title = "进程数量",
            Body = QCA.translate("Label", "进行数据加载时可并行的进程数量，若用户CPU性能较弱可减小该值。")
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.setValue(4)
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.setToolTip("提示：如果配置属于低U高显的话不妨试试把数值降到2。")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_FP16_Run,
            Title = "半精度训练",
            Body = QCA.translate("Label", "通过混合了float16精度的训练方式减小显存占用以支持更大的批处理量。")
        )
        self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run.setText("已启用")
        self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run.setChecked(True)
        Function_ConfigureCheckBox(
            CheckBox = self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run,
            CheckedText = "已启用",
            UncheckedText = "未启用"
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Config_Dir_Save,
            Title = "配置保存目录",
            Body = QCA.translate("Label", "根据以上设置更新参数后的配置文件的保存目录。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Config_Dir_Save,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Config_Dir_Save,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save,
            Title = "模型保存目录",
            Body = QCA.translate("Label", "训练得到的模型的存放目录，若目录中已存在模型则会将其视为检查点。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Dir_Save,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save,
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )
        self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save.setToolTipDuration(-1)
        self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save.setToolTip("提示：当目录中存在多个模型时，编号最大的那个会被选为检查点。")

        self.ui.GroupBox_OptionalParams_Tool_VoiceTrainer.setTitle("OptionalParams 可选参数")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Config_Path_Load,
            Title = "配置加载路径",
            Body = QCA.translate("Label", "该路径对应的配置文件将会替代默认的配置文件。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Config_Path_Load,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load,
            Mode = "SelectFile",
            FileType = "json类型 (*.json)",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            Title = "预训练G_0模型路径",
            Body = QCA.translate("Label", "该路径对应的预训练生成器（Generator）模型会被视为检查点。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            Title = "预训练D_0模型路径",
            Body = QCA.translate("Label", "该路径对应的预训练判别器（Discriminator）模型会被视为检查点。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Speakers,
            Title = "人物名字",
            Body = QCA.translate("Label", "若数据集非本工具箱生成且未包含人名信息，则应按序号设置并用逗号隔开。")
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setReadOnly(False)
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setText('')
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setToolTipDuration(-1)
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setToolTip("注意：逗号后面不需要加空格")

        # Tool_VoiceConverter
        Function_SetText(
            Panel = self.ui.TextBrowser_Tool_VoiceConverter,
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
                "\n"
                "[提示]\n"
                "1. 您可以通过点击“打开输出目录”按钮以查看当前工具在执行完毕后输出的文件\n"
            )
        )

        self.ui.Button_CheckOutput_Tool_VoiceConverter.setText(QCA.translate("Button", "打开输出目录"))
        Function_SetURL(
            Button = self.ui.Button_CheckOutput_Tool_VoiceConverter,
            URL = self.ui.LineEdit_Tool_VoiceConverter_Audio_Dir_Save,
            ButtonTooltip = "Click to open"
        )

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
            ]
        )

        self.ui.GroupBox_EssentialParams_Tool_VoiceConverter.setTitle(QCA.translate("GroupBox", "必要参数"))

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_Config_Path_Load,
            Title = "配置加载路径",
            Body = QCA.translate("Label", "该路径对应的配置文件会用于推理。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceConverter_Config_Path_Load,
            LineEdit = self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load,
            Mode = "SelectFile",
            FileType = "json类型 (*.json)",
            DisplayText = QCA.translate("LineEdit", "None")
        )
        self.ui.LineEdit_Tool_VoiceConverter_Config_Path_Load.textChanged.connect(
            lambda Path: self.ui.ComboBox_Tool_VoiceConverter_Speaker.addItems(
                Get_Speakers(Path)
            )
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_Model_Path_Load,
            Title = "G_*模型加载路径",
            Body = QCA.translate("Label", "该路径对应的生成器（Generator）模型会用于推理。")
        )
        Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceConverter_Model_Path_Load,
            LineEdit = self.ui.LineEdit_Tool_VoiceConverter_Model_Path_Load,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_Text,
            Title = "输入文字",
            Body = QCA.translate("Label", "输入的文字会作为说话人的语音内容。")
        )
        self.ui.PlainTextEdit_Tool_VoiceConverter_Text.setPlainText("请输入语句")

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_Language,
            Title = "所用语言",
            Body = QCA.translate("Label", "说话人/文字所使用的语言。")
        )
        self.ui.ComboBox_Tool_VoiceConverter_Language.addItems(['中', '英'])
        self.ui.ComboBox_Tool_VoiceConverter_Language.setCurrentText('中')

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_Speaker,
            Title = "人物名字",
            Body = QCA.translate("Label", "说话人物的名字。")
        )
        #self.ui.ComboBox_Tool_VoiceConverter_Speaker.addItems(Get_Speakers)
        self.ui.ComboBox_Tool_VoiceConverter_Speaker.setCurrentText('')

        Function_SetText(
            Panel = self.ui.Label_Tool_VoiceConverter_EmotionStrength,
            Title = "情感强度",
            Body = QCA.translate("Label", "情感的变化程度。")
        )
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setMinimum(0)
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setMaximum(1000)
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setTickInterval(1)
        self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setValue(667)
        Function_ParamsSynchronizer(
            Trigger = self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength,
            ParamsFrom = [
                self.ui.HorizontalSlider_Tool_VoiceConverter_EmotionStrength
            ],
            Times = 0.001,
            ParamsTo = [
                self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength
            ]
        )
        self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength.setValue(0.667)
        Function_ParamsSynchronizer(
            Trigger = self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength,
            ParamsFrom = [
                self.ui.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength
            ],
            Times = 1000,
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
        self.ui.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setValue(8)
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
        self.ui.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration.setValue(0.8)
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
        self.ui.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setValue(10)
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
        self.ui.DoubleSpinBox_Tool_VoiceConverter_SpeechRate.setValue(1.)
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
            Mode = "SelectDir",
            DisplayText = QCA.translate("LineEdit", "None")
        )

        # Settings
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
        #Signals.Signal_FrameStatus.connect(lambda FrameStatus: 
        self.ConsoleInfo.Signal_ConsoleInfo.connect(
            lambda Info: Function_PrintText(
                Panel = self.ui.PlainTextEdit_Console,
                FrameStatus = "Extended", #FrameStatus = FrameStatus,
                Text = Info
            )
        )
        #)

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

        # Show MainWindow
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)

    Window = MainWindow()
    Window.Main()
    
    sys.exit(App.exec())