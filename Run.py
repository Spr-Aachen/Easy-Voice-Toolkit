import os
import sys
import re
from typing import Optional
from PySide6 import __file__ as PySide6_File
from PySide6.QtCore import QObject, QThread, Signal, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import *

from GUI.WindowCustomizer import Window_Customizing
from GUI.UI import Ui_MainWindow
from GUI.Utils import TaskAccelerating
from EnvConfigurator.Configure import Env_Configurator
from Tool_AudioProcessor.Process import Audio_Processing
from Tool_VoiceIdentifier.Identify import Voice_Identifying
from Tool_VoiceTranscriber.Transcribe import Voice_Transcribing
from Tool_DatasetCreator.Create import Dataset_Creating
from Tool_VoiceTrainer.Train import Voice_Training


# Redirect PATH environment variable 'QT_QPA_PLATFORM_PLUGIN_PATH' to Pyside6 '/plugins/platforms' folder's path
PySide6_Dirname = os.path.dirname(PySide6_File)
PySide6_PluginPath = os.path.join(PySide6_Dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = PySide6_PluginPath


# Where to store custom signals
class CustomSignals(QObject):
    '''
    Set up signals for custom functions
    '''
    # Monitor frame
    Signal_FrameStatus = Signal(str)

    # Run task
    Signal_ExecuteTask = Signal(list)


# Task: Configurate environment
class Execute_Env_Configurator(QObject):
    '''
    Install ffmpeg
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

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

    def Execute(self, Params):
        WAVtoSRT = Voice_Transcribing(*Params)
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

    def Execute(self, Params):
        PreprocessandTrain = Voice_Training(*Params)
        TaskAccelerating(
            TargetList = [PreprocessandTrain.Preprocessing_and_Training],
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
            window_title = "Easy Voice Toolkit"
        )

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.CustomSignals = CustomSignals()

    def Function_FindParentUI(self,
        ChildUI: QObject,
        ParentType: object
    ):
        '''
        Function to find parent UI
        '''
        ChildUI_Parent = ChildUI.parent()

        while not isinstance(ChildUI_Parent, ParentType):
            try:
                ChildUI_Parent = ChildUI_Parent.parent()
            except:
                raise Exception(f"{ChildUI}'s parent UI not found! Please check if the layout is correct.")

        return ChildUI_Parent

    def Function_InsertUI(self,
        ParentUI: QObject,
        InsertType: object,
        InsertPosition: str = "End",
        UIParam: Optional[str] = None,
        UIToolTip: Optional[str] = None,
    ):
        '''
        Function to insert UI
        '''
        InsertUI = InsertType(UIParam)
        if isinstance(InsertUI, (QPushButton, QToolButton)):
            InsertUI.setMinimumHeight(24)
            InsertUI.setStyleSheet(
                f"{InsertType.__name__}"
                "{"
                    "text-align: center;"
                    "font-size: 12px;"
                    "color: rgb(255, 255, 255);"
                    "background-color: rgb(90, 90, 90);"
                    "padding: 0px;"
                    "border-width: 0px;"
                    "border-radius: 6px;"
                    "border-style: solid;"
                "}"
                f"{InsertType.__name__}:hover"
                "{"
                    "background-color: rgb(120, 120, 120);"
                "}"

                "QToolTip"
                "{"
                    "color: white;"
                    "background-color: transparent;"
                "}"
            )
        else:
            pass

        Layout = ParentUI.layout() if ParentUI.layout() != None else QGridLayout(ParentUI)
        if InsertPosition == "Start":
            RowCount = 0
        if InsertPosition == "End":
            RowCount = ParentUI.document().lineCount() if isinstance(ParentUI, (QPlainTextEdit, QTextEdit, QTextBrowser)) else round(ParentUI.height()/15)
        for Row in range(0, RowCount):
            SpacingUI = QWidget(ParentUI)
            SpacingUI.setStyleSheet(
                "QWidget"
                "{"
                    "background-color: transparent;"
                    "padding: 0px;"
                    "border-width: 0px;"
                "}"
            )
            Layout.addWidget(SpacingUI, Row, 0)
        Layout.addWidget(InsertUI, RowCount, 0)
        
        InsertUI.setToolTipDuration(-1)
        InsertUI.setToolTip(UIToolTip)

        return InsertUI

    def Function_AnimateStackedWidget(self,
        StackedWidget: QStackedWidget,
        TargetIndex: int = 0,
        Duration: int = 0
    ):
        '''
        Function to animate stackedwidget
        '''
        Index_Current = StackedWidget.currentIndex()

        WidgetAnimation = QPropertyAnimation(StackedWidget, b"currentIndex")

        def AnimateStackedWidget(Index_Altered):
            WidgetAnimation.setDuration(Duration)
            WidgetAnimation.setStartValue(Index_Current)
            WidgetAnimation.setEndValue(Index_Altered)
            WidgetAnimation.setEasingCurve(QEasingCurve.InOutQuart)
            WidgetAnimation.start()

        AnimateStackedWidget(TargetIndex)

    def Function_AnimateFrame(self,
        Frame: QFrame,
        MinWidth: int = ...,
        MaxWidth: int = ...,
        Duration: int = 0,
        Mode: str = "Toggle"
    ):
        '''
        Function to animate frame
        '''
        Width_Current = Frame.width()

        FrameAnimation = QPropertyAnimation(Frame, b"minimumWidth")

        def AnimateFrame(Width_Altered):
            FrameAnimation.setDuration(Duration)
            FrameAnimation.setStartValue(Width_Current)
            FrameAnimation.setEndValue(Width_Altered)
            FrameAnimation.setEasingCurve(QEasingCurve.InOutQuart)
            FrameAnimation.start()

        if Mode == "Extend":
            AnimateFrame(MaxWidth)
            self.CustomSignals.Signal_FrameStatus.emit(f"{Frame.objectName()}Extended")
        if Mode == "Reduce":
            AnimateFrame(MinWidth)
            self.CustomSignals.Signal_FrameStatus.emit(f"{Frame.objectName()}Reduced")
        if Mode == "Toggle":
            if Width_Current == MinWidth:
                AnimateFrame(MaxWidth)
                self.CustomSignals.Signal_FrameStatus.emit(f"{Frame.objectName()}Extended")
            else:
                AnimateFrame(MinWidth)
                self.CustomSignals.Signal_FrameStatus.emit(f"{Frame.objectName()}Reduced")

    def Function_AnimateButton(self,
        Button: QPushButton,
        Frame: Optional[QFrame] = None,
        FrameStatus: str = ...,
        Text: str = ...
    ):
        '''
        Function to animate button
        '''
        Frame = self.Function_FindParentUI(
            ChildUI = Button,
            ParentType = QFrame
        ) if Frame == None else Frame

        if FrameStatus == f"{Frame.objectName()}Extended":
            Button.setText(Text)
        if FrameStatus == f"{Frame.objectName()}Reduced":
            Button.setText("")

    def Function_PrintText(self,
        Panel: QPlainTextEdit,
        Frame: Optional[QFrame] = None,
        FrameStatus: str = ...,
        Text: str = ...,
        ShowCursor: bool = False
    ):
        '''
        Function to print text on panel while its parent frame is extended
        '''
        TextCursor = Panel.textCursor()
        TextCursor.movePosition(QTextCursor.End)
        TextCursor.insertText(Text)
        Panel.setTextCursor(TextCursor)
        Panel.ensureCursorVisible() if ShowCursor == True else None

        Frame = self.Function_FindParentUI(
            ChildUI = Panel,
            ParentType = QFrame
        ) if Frame == None else Frame

        if FrameStatus == f"{Frame.objectName()}Extended":
            Panel.setVisible(True)
        if FrameStatus == f"{Frame.objectName()}Reduced":
            Panel.setVisible(False)

    def Function_SetText(self,
        Panel: QObject,
        Title: Optional[str] = ...,
        TitleAlign: str = "left",
        TitleSize: float = 9.9,
        TitleWeight: float = 840.,
        TitleColor: str = "#ffffff",
        TitleLineHeight: float = 21.,
        TitleOnly: bool = False,
        Body: Optional[str] = ...,
        BodyAlign: str = "left",
        BodySize: float = 9.9,
        BodyWeight: float = 420.,
        BodyLineHeight: float = 21.,
        BodyColor: str = "#ffffff",
    ):
        '''
        Function to set text for label or textbrowser
        '''
        def ToHtml(Content, Align, Size, Weight, Color, LineHeight):
            Style = f"'text-align:{Align}; font-size:{Size}pt; font-weight:{Weight}; color:{Color}; line-height:{LineHeight}px'"
            Content = re.sub(
                pattern = "[\n]",
                repl = "<br>",
                string = Content
            )
            return f"<p style={Style}>{Content}</p>"

        Text = (
            "<html>"
            "<body>"
            f"{ToHtml(Title, TitleAlign, TitleSize, TitleWeight, TitleColor, TitleLineHeight)}"
            f"{ToHtml(Body, BodyAlign, BodySize, BodyWeight, BodyColor, BodyLineHeight)}"
            "</body>"
            "</html>"
        ) if not TitleOnly else (
            "<html>"
            "<body>"
            f"{ToHtml(Title, TitleAlign, TitleSize, TitleWeight, TitleColor, TitleLineHeight)}"
            "</body>"
            "</html>"
        )

        if isinstance(Panel, QLabel):
            Panel.setText(Text)
        if isinstance(Panel, QTextBrowser):
            Panel.setHtml(Text)

    def Function_SetFileDialog(self,
        Button: QPushButton,
        LineEdit: QLabel,
        Mode: str,
        FileType: Optional[str] = None,
        DisplayText: str = "None",
        ButtonTooltip: str = "Browse"
    ):
        '''
        Function to select/save file path (through button)
        '''
        LineEdit.setText(DisplayText)

        def SetFileDialog():
            if Mode == "SelectDir":
                DisplayText = QFileDialog.getExistingDirectory(self,
                    caption = "选择文件夹",
                    dir = os.getcwd()
                )
            if Mode == "SelectFile":
                DisplayText, _ = QFileDialog.getOpenFileName(self,
                    caption = "选择文件",
                    dir = os.getcwd(),
                    filter = FileType
                )
            if Mode == "SaveFile":
                DisplayText, _ = QFileDialog.getSaveFileName(self,
                    caption = "保存文件",
                    dir = os.getcwd(),
                    filter = FileType
                )

            LineEdit.setText(DisplayText)
            LineEdit.setStatusTip(DisplayText)
        
        Button.clicked.connect(SetFileDialog)
        Button.setToolTipDuration(-1)
        Button.setToolTip(ButtonTooltip)
    
    def Function_ShowMessageBox(self,
        WindowTitle: str = ...,
        Text: str = ...,
    ):
        '''
        Function to pop up a msgbox
        '''
        MsgBox = QMessageBox(self)

        MsgBox.setWindowTitle(WindowTitle)
        MsgBox.setText(Text)
        MsgBox.setIcon(QMessageBox.Information)
        MsgBox.setStyleSheet(
            "QMessageBox"
            "{"
                "background-color: rgb(60, 60, 60);"
                "padding: 0px;"
                "border-width: 0px;"
                "border-radius: 6px;"
                "border-style: solid;"
            "}"

            "QMessageBox QLabel#qt_msgbox_label"
            "{"
                "text-align: center;"
                "font-size: 12px;"
                "color: rgb(255, 255, 255);"
                "background-color: transparent;"
                "min-width: 240px;"
                "min-height: 40px;"
            "}"

            "QMessageBox QLabel#qt_msgboxex_icon_label"
            "{"
                "background-color: transparent;"
                "width: 40px;"
                "height: 40px;"
            "}"

            "QMessageBox QPushButton"
            "{"
                "font-size: 12pt;"
                "color: rgb(255, 255, 255);"
                "background-color: rgb(90, 90, 90);"
                "border-width: 0px;"
                "border-radius: 6px;"
                "border-style: solid;"
                "min-width: 70px;"
                "min-height: 25px;"
            "}"

            "QMessageBox QPushButton:hover"
            "{"
                "background-color: rgb(120, 120, 120);"
            "}"
        )

        MsgBox.exec()

    def Function_ParamsHandler(self,
        UI: QObject,
        Param: Optional[str],
        Mode: str = "Get",
    ):
        '''
        Function to get/set the param of UI
        '''
        if Mode == "Get":
            if isinstance(UI, QLineEdit):
                return UI.text()
            if isinstance(UI, QComboBox):
                return UI.currentText()
            if isinstance(UI, (QSpinBox, QDoubleSpinBox)):
                return UI.value()
            if isinstance(UI, (QCheckBox, QRadioButton)):
                return UI.isChecked()
        if Mode == "Set":
            if isinstance(UI, QLineEdit):
                UI.setText(Param)
            if isinstance(UI, QComboBox):
                UI.setCurrentText(Param)
            if isinstance(UI, (QSpinBox, QDoubleSpinBox)):
                UI.setValue(Param)
            if isinstance(UI, (QCheckBox, QRadioButton)):
                UI.setChecked(Param)

    def Function_ParamsSynchronizer(self,
        Button: QPushButton,
        ParamsFrom: list = [],
        ParamsTo: list = [],
    ):
        '''
        Function to synchronize params
        '''
        def ParamsSynchronizer():
            for UI_Get in ParamsFrom:
                UI_Set = ParamsTo[ParamsFrom.index(UI_Get)]
                Param_Get = self.Function_ParamsHandler(UI_Get, "Get")
                self.Function_ParamsHandler(UI_Set, Param_Get, "Set")
        
        Button.clicked.connect(ParamsSynchronizer)

    def Function_ParamsChecker(self,
        ParamsFrom: list = [],
        EmptyAllowed: list = []
    ):
        '''
        Function to return handled params
        '''
        Params = []

        for UI in ParamsFrom:
            Param = self.Function_ParamsHandler(UI, "Get")
            if isinstance(Param, str):
                if Param == "None" or Param == "":
                    if UI in EmptyAllowed:
                        Param = None
                    else:
                        self.Function_ShowMessageBox(
                            WindowTitle = "Warning",
                            Text = "Empty param detected!\n检测到参数空缺！"
                        )
                        return "Abort"
                else:
                    if "，" in Param or "," in Param:
                        Param = re.split(
                            pattern = '[，,]',
                            string = Param,
                            maxsplit = 0
                        )
            else:
                pass
            Params.append(Param)

        return Params

    def Function_AnimateProgressBar(self,
        ProgressBar: QProgressBar,
        MinValue: int = 0,
        MaxValue: int = 100,
        DisplayValue: bool = False,
        IsTaskAlive: bool = False
    ):
        '''
        Function to animate progressbar
        '''
        ProgressBar.setTextVisible(DisplayValue)
        ProgressBar.setRange(MinValue, MaxValue)
        ProgressBar.setValue(MinValue)

        if IsTaskAlive == True:
            ProgressBar.setRange(0, 0)
            #QApplication.processEvents()
        else:
            ProgressBar.setRange(MinValue, MaxValue)
            ProgressBar.setValue(MaxValue)

    def Function_ExecuteMethod(self,
        ExecuteButton: QPushButton,
        TerminateButton: Optional[QPushButton],
        ProgressBar: Optional[QProgressBar],
        Method: object,
        ParamsFrom: list = [],
        EmptyAllowed: list = []
    ):
        '''
        Function to execute outer class methods (through button)
        '''
        ClassName = str(Method.__qualname__).split('.')[0]

        WorkerThread = QThread(self)
        ClassInstance = globals()[ClassName]()
        ClassInstance.moveToThread(WorkerThread)
        ClassInstance.finished.connect(WorkerThread.quit)

        MethodName = str(Method.__qualname__).split('.')[1]

        def ExecuteMethod():
            '''
            Update the attributes for outer class methods and wait to execute with multithreading
            '''
            if self.Function_ParamsChecker(ParamsFrom, EmptyAllowed) != "Abort":
                Params = self.Function_ParamsChecker(ParamsFrom, EmptyAllowed)
            else:
                return print("Aborted.")
            
            StackedWidget = self.Function_FindParentUI(
                ChildUI = ExecuteButton, #ChildUI = TerminateButton,
                ParentType = QStackedWidget
            ) if TerminateButton else None
            
            self.CustomSignals.Signal_ExecuteTask.connect(getattr(ClassInstance, MethodName))
            self.CustomSignals.Signal_ExecuteTask.emit(Params)
            WorkerThread.started.connect(lambda: self.Function_AnimateProgressBar(ProgressBar = ProgressBar, IsTaskAlive = True)) if ProgressBar else None
            WorkerThread.started.connect(lambda: self.Function_AnimateStackedWidget(StackedWidget = StackedWidget, TargetIndex = 1)) if TerminateButton else None
            WorkerThread.finished.connect(lambda: self.Function_AnimateProgressBar(ProgressBar = ProgressBar, IsTaskAlive = False)) if ProgressBar else None
            WorkerThread.finished.connect(lambda: self.Function_AnimateStackedWidget(StackedWidget = StackedWidget, TargetIndex = 0)) if TerminateButton else None
            WorkerThread.start()

        ExecuteButton.clicked.connect(ExecuteMethod)
        ExecuteButton.setText("Execute 执行")

        def TerminateMethod():
            '''
            Terminate the running thread
            '''
            if not WorkerThread.isFinished():
                try:
                    WorkerThread.terminate()
                except:
                    WorkerThread.quit()
        
            ProgressBar.setValue(0)

        TerminateButton.clicked.connect(TerminateMethod) if TerminateButton else None
        TerminateButton.setText("Terminate 终止") if TerminateButton else None

    def Main(self):
        '''
        Main funtion to orgnize all the subfunctions
        '''
        # Toggle/Burger Menu
        self.ui.Button_Toggle_Menu.clicked.connect(
            lambda: self.Function_AnimateFrame(
                Frame = self.ui.Frame_Menu,
                MinWidth = 45,
                MaxWidth = 210
            )
        )
        self.ui.Button_Toggle_Menu.setCheckable(True)
        self.ui.Button_Toggle_Menu.setChecked(False)
        self.ui.Button_Toggle_Menu.setAutoExclusive(False)
        self.ui.Button_Toggle_Menu.setToolTipDuration(-1)
        self.ui.Button_Toggle_Menu.setToolTip("Click to toggle/burger menu")

        # Print Titles & Choose Pages
        self.CustomSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: self.Function_AnimateButton(
                Button = self.ui.Button_Home,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = "主页"
            )
        )
        self.ui.Button_Home.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 0
            )
        )
        self.ui.Button_Home.setCheckable(True)
        self.ui.Button_Home.setChecked(True)
        self.ui.Button_Home.setAutoExclusive(True)
        self.ui.Button_Home.setToolTipDuration(-1)
        self.ui.Button_Home.setToolTip("Homepage")

        self.CustomSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: self.Function_AnimateButton(
                Button = self.ui.Button_Page_1,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = "音频转换和分割"
            )
        )
        self.ui.Button_Page_1.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 1
            )
        )
        self.ui.Button_Page_1.setCheckable(True)
        self.ui.Button_Page_1.setChecked(False)
        self.ui.Button_Page_1.setAutoExclusive(True)
        self.ui.Button_Page_1.setToolTipDuration(-1)
        self.ui.Button_Page_1.setToolTip("Audio Processor")

        self.CustomSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: self.Function_AnimateButton(
                Button = self.ui.Button_Page_2,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = "语音识别和筛选"
            )
        )
        self.ui.Button_Page_2.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 2
            )
        )
        self.ui.Button_Page_2.setCheckable(True)
        self.ui.Button_Page_2.setChecked(False)
        self.ui.Button_Page_2.setAutoExclusive(True)
        self.ui.Button_Page_2.setToolTipDuration(-1)
        self.ui.Button_Page_2.setToolTip("Voice Identifier")

        self.CustomSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: self.Function_AnimateButton(
                Button = self.ui.Button_Page_3,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = "语音转文字字幕"
            )
        )
        self.ui.Button_Page_3.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 3
            )
        )
        self.ui.Button_Page_3.setCheckable(True)
        self.ui.Button_Page_3.setChecked(False)
        self.ui.Button_Page_3.setAutoExclusive(True)
        self.ui.Button_Page_3.setToolTipDuration(-1)
        self.ui.Button_Page_3.setToolTip("Voice Transcriber")

        self.CustomSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: self.Function_AnimateButton(
                Button = self.ui.Button_Page_4,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = "语音数据集制作"
            )
        )
        self.ui.Button_Page_4.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 4
            )
        )
        self.ui.Button_Page_4.setCheckable(True)
        self.ui.Button_Page_4.setChecked(False)
        self.ui.Button_Page_4.setAutoExclusive(True)
        self.ui.Button_Page_4.setToolTipDuration(-1)
        self.ui.Button_Page_4.setToolTip("Dataset Creator")

        self.CustomSignals.Signal_FrameStatus.connect(
            lambda FrameStatus: self.Function_AnimateButton(
                Button = self.ui.Button_Page_5,
                Frame = self.ui.Frame_Menu,
                FrameStatus = FrameStatus,
                Text = "语音模型训练"
            )
        )
        self.ui.Button_Page_5.clicked.connect(
            lambda: self.Function_AnimateStackedWidget(
                StackedWidget = self.ui.StackedWidget_Pages,
                TargetIndex = 5
            )
        )
        self.ui.Button_Page_5.setCheckable(True)
        self.ui.Button_Page_5.setChecked(False)
        self.ui.Button_Page_5.setAutoExclusive(True)
        self.ui.Button_Page_5.setToolTipDuration(-1)
        self.ui.Button_Page_5.setToolTip("Voice Trainer")

        # Page0: Home
        self.Function_SetText(
            Panel = self.ui.TextBrowser_Page_0,
            Title = "Easy Voice Toolkit",
            TitleAlign = "center",
            TitleSize = 48,
            TitleWeight = 840,
            Body = "Version 1.0",
            BodyAlign = "center",
            BodySize = 24,
            BodyWeight = 840
        )

        # Page1: Tool_AudioProcessor
        self.Function_SetText(
            Panel = self.ui.TextBrowser_Tool_AudioProcessor,
            Title = "Audio Processor 音频转换和分割",
            TitleAlign = "center",
            TitleSize = 18,
            Body = "\n"
                "[介绍]\n"
                "该工具会将媒体文件批量转换为音频文件，然后自动切除音频的静音部分。\n"
                "\n"
                "[提示]\n"
                "请确保已经正确安装了FFmpeg\n"
        )
        self.Function_ExecuteMethod(
            ExecuteButton = self.Function_InsertUI(
                ParentUI = self.ui.TextBrowser_Tool_AudioProcessor,
                InsertType = QPushButton,
                InsertPosition = "End",
                UIParam = "Install 安装",
                UIToolTip = "尝试安装FFmpeg (有概率失败)"
            ),
            TerminateButton = None,
            ProgressBar = None,
            Method = Execute_Env_Configurator.Execute
        )

        self.Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Tool_AudioProcessor_Execute,
            TerminateButton = self.ui.Button_Tool_AudioProcessor_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_AudioProcessor,
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
        self.ui.Button_Tool_AudioProcessor_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_AudioProcessor_Execute.setToolTip("执行音频转换和分割")
        self.ui.Button_Tool_AudioProcessor_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_AudioProcessor_Terminate.setToolTip("终止音频转换和分割")

        self.ui.GroupBox_EssentialParams_Page_1.setTitle("EssentialParams 必要参数")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Media_Dir_Input,
            Title = "Media Dir Input",
            Body = "媒体输入目录。该目录中的媒体文件将会以下列设置输出为音频文件。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_AudioProcessor_Media_Dir_Input,
            LineEdit = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Input,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Media_Format_Output,
            Title = "Media Format Output",
            Body = "媒体输出格式。媒体文件将会以设置的格式输出为音频文件。"
        )
        self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output.addItems(['wav', 'mp3'])
        self.ui.ComboBox_Tool_AudioProcessor_Media_Format_Output.setCurrentText('wav')

        self.Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_RMS_Threshold,
            Title = "RMS Threshold (db)",
            Body = "均方根阈值 (db)。低于该阈值的片段将被视作静音进行处理，若有降噪需求可以增加该值。"
        )
        #self.ui.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setValue(-40.)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Hop_Size,
            Title = "Hop Size (ms)",
            Body = "跳跃大小 (ms)。每个RMS帧的长度，增加该值能够提高分割精度但会减慢进程。"
        )
        self.ui.SpinBox_Tool_AudioProcessor_Hop_Size.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Hop_Size.setValue(10)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Silent_Interval_Min,
            Title = "Silent Interval Min (ms)",
            Body = "最小静音间隔 (ms)。静音部分被分割成的最小长度，若音频只包含短暂中断可以减小该值。"
        )
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setValue(300)
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setToolTip("注意，这个值必须小于 Audio Length Min，大于 Hop Size。")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Silence_Kept_Max,
            Title = "Silence Kept Max (ms)",
            Body = "最大静音长度 (ms)。被分割的音频周围保持静音的最大长度。"
        )
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setValue(1000)
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setToolTip("注意，这个值无需完全对应被分割音频中的静音长度。算法将自行检索最佳的分割位置。")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Audio_Length_Min,
            Title = "Audio Length Min (ms)",
            Body = "最小音频长度 (ms)。每个被分割的音频片段所需的最小长度。"
        )
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setSingleStep(1)
        self.ui.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setValue(5000)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_AudioProcessor_Media_Dir_Output,
            Title = "Media Dir Output",
            Body = "媒体输出目录。最后生成的音频文件将被保存到该目录中。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_AudioProcessor_Media_Dir_Output,
            LineEdit = self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        # Page2: Tool_VoiceIdentifier
        self.Function_SetText(
            Panel = self.ui.TextBrowser_Tool_VoiceIdentifier,
            Title = "Voice Identifier 语音识别和筛选",
            TitleAlign = "center",
            TitleSize = 18,
            Body = "\n"
                "[介绍]\n"
                "该工具会在不同说话人的音频中批量筛选出属于同一说话人的音频。用户需要提供一段包含目标说话人的语音作为期望值。\n"
                "\n"
                "[提示]\n"
                "若有使用完整流程的需求，建议检查以下设置是否正确衔接了前面工具的输出项以及部分设定：\n"
                "Audio Dir Input\n"
        )
        self.Function_ParamsSynchronizer(
            Button = self.Function_InsertUI(
                ParentUI = self.ui.TextBrowser_Tool_VoiceIdentifier,
                InsertType = QPushButton,
                InsertPosition = "End",
                UIParam = "Sync 同步",
                UIToolTip = "同步以上设置 (适用于完整流程)"
            ),
            ParamsFrom = [
                self.ui.LineEdit_Tool_AudioProcessor_Media_Dir_Output
            ],
            ParamsTo = [
                self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input
            ]
        )

        self.Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Tool_VoiceIdentifier_Execute,
            TerminateButton = self.ui.Button_Tool_VoiceIdentifier_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_VoiceIdentifier,
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
                self.ui.SpinBox_Tool_VoiceIdentifier_SpeakerID
            ],
            EmptyAllowed = [
                self.ui.SpinBox_Tool_VoiceIdentifier_SpeakerID
            ]
        )
        self.ui.Button_Tool_VoiceIdentifier_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceIdentifier_Execute.setToolTip("执行语音识别和筛选")
        self.ui.Button_Tool_VoiceIdentifier_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceIdentifier_Terminate.setToolTip("终止语音识别和筛选")

        self.ui.GroupBox_EssentialParams_Page_2.setTitle("EssentialParams 必要参数")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Audio_Dir_Input,
            Title = "Audio Dir Input",
            Body = "音频输入目录。该目录中的音频文件将会按照以下设置进行识别筛选。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Audio_Dir_Input,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Audio_Path_Std,
            Title = "Audio Path Std",
            Body = "标准音频路径。该路径对应的音频将会作为识别的比对标准，即期望值。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Audio_Path_Std,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Path_Std,
            Mode = "SelectFile",
            FileType = "音频类型 (*.mp3 *.aac *.wav *.flac)",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Model_Dir,
            Title = "Model Dir",
            Body = "模型存放目录。该目录将会用于存放下载的声纹识别模型，若模型已存在会直接使用。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Model_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Model_Dir,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Model_Type,
            Title = "Model Type",
            Body = "模型类型。声纹识别模型的类型。"
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type.addItems(['Ecapa-Tdnn'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Type.setCurrentText('Ecapa-Tdnn')

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Model_Name,
            Title = "Model Name",
            Body = "模型名字。声纹识别模型的名字，默认代表模型的大小。"
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name.addItems(['small'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Model_Name.setCurrentText('small')

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Feature_Method,
            Title = "Feature Method",
            Body = "特征提取方法。音频特征的提取方法。"
        )
        self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method.addItems(['spectrogram', 'melspectrogram'])
        self.ui.ComboBox_Tool_VoiceIdentifier_Feature_Method.setCurrentText('spectrogram')

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_DecisionThreshold,
            Title = "Decision Threshold",
            Body = "判断阈值。判断是否为同一人的阈值，若参与比对的说话人声音相识度较高可以增加该值。"
        )
        #self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setValue(0.84)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Duration_of_Audio,
            Title = "Duration of Audio",
            Body = "音频长度。用于预测的音频长度。"
        )
        #self.ui.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setSingleStep(0.01)
        self.ui.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setValue(3.00)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_Audio_Dir_Output,
            Title = "Audio Dir Output",
            Body = "音频输出目录。最后筛选出的音频文件将被复制到该目录中。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceIdentifier_Audio_Dir_Output,
            LineEdit = self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        self.ui.GroupBox_OptionalParams_Page_2.setTitle("OptionalParams 可选参数")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceIdentifier_SpeakerID,
            Title = "SpeakerID",
            Body = "人物编号。说话人物的编号，单人模型可不填写，多人模型需填写对应编号。"
        )
        #self.ui.SpinBox_Tool_VoiceIdentifier_SpeakerID.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceIdentifier_SpeakerID.setValue(0)
        self.ui.SpinBox_Tool_VoiceIdentifier_SpeakerID.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceIdentifier_SpeakerID.setToolTip("注意，第一个人物的编号为0，第二个为1，以此类推")

        # Page3: Tool_VoiceTranscriber
        self.Function_SetText(
            Panel = self.ui.TextBrowser_Tool_VoiceTranscriber,
            Title = "Voice Transcriber 语音转文字字幕",
            TitleAlign = "center",
            TitleSize = 18,
            Body = "\n"
                "[介绍]\n"
                "该工具会将语音文件的内容批量转换为带时间戳的文本并以字幕文件的形式保存。\n"
                "\n"
                "[提示]\n"
                "若有使用完整流程的需求，建议检查以下设置是否正确衔接了前面工具的输出项以及部分设定：\n"
                "WAV Dir\n"
        )
        self.Function_ParamsSynchronizer(
            Button = self.Function_InsertUI(
                ParentUI = self.ui.TextBrowser_Tool_VoiceTranscriber,
                InsertType = QPushButton,
                InsertPosition = "End",
                UIParam = "Sync 同步",
                UIToolTip = "同步以上设置 (适用于完整流程)"
            ),
            ParamsFrom = [
                self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output
            ],
            ParamsTo = [
                self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir
            ]
        )

        self.Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Tool_VoiceTranscriber_Execute,
            TerminateButton = self.ui.Button_Tool_VoiceTranscriber_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_VoiceTranscriber,
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
        self.ui.Button_Tool_VoiceTranscriber_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceTranscriber_Execute.setToolTip("执行语音转文字字幕")
        self.ui.Button_Tool_VoiceTranscriber_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceTranscriber_Terminate.setToolTip("终止语音转文字字幕")

        self.ui.GroupBox_EssentialParams_Page_3.setTitle("EssentialParams 必要参数")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_WAV_Dir,
            Title = "WAV Dir",
            Body = "音频目录。该目录中的wav文件的语音内容将会按照以下设置转为文字。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_WAV_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Model_Dir,
            Title = "Model Dir",
            Body = "模型存放目录。该目录将会用于存放下载的语音识别模型，若模型已存在会直接使用。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_Model_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_Model_Dir,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Model_Name,
            Title = "Model Name",
            Body = "模型名字。语音识别 (whisper) 模型的名字，默认代表模型的大小。"
        )
        self.ui.ComboBox_Tool_VoiceTranscriber_Model_Name.addItems(['tiny', 'base', 'small', 'medium', 'large'])
        self.ui.ComboBox_Tool_VoiceTranscriber_Model_Name.setCurrentText('small')

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Verbose,
            Title = "Verbose",
            Body = "启用输出日志。输出debug日志。"
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_Verbose.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_Verbose.setChecked(True)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Condition_on_Previous_Text,
            Title = "Condition on Previous Text",
            Body = "前后文一致。将模型之前的输出作为下个窗口的提示，若模型陷入了失败循环则禁用此项。"
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setChecked(True)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_fp16,
            Title = "FP16",
            Body = "半精度。主要使用半精度浮点数进行计算，若GPU不可用则忽略或禁用此项。"
        )
        self.ui.CheckBox_Tool_VoiceTranscriber_fp16.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTranscriber_fp16.setChecked(True)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_SRT_Dir,
            Title = "SRT Dir",
            Body = "字幕输出目录。最后生成的字幕文件将会保存到该目录中。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTranscriber_SRT_Dir,
            LineEdit = self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        self.ui.GroupBox_OptionalParams_Page_3.setTitle("OptionalParams 可选参数")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTranscriber_Language,
            Title = "Language",
            Body = "所用语言。音频中说话人所使用的语言，若存在多种语言则保持'None'即可。"
        )
        self.ui.ComboBox_Tool_VoiceTranscriber_Language.addItems(['zh', 'en', 'None'])
        self.ui.ComboBox_Tool_VoiceTranscriber_Language.setCurrentText('None')

        # Page4: Tool_DatasetCreator
        self.Function_SetText(
            Panel = self.ui.TextBrowser_Tool_DatasetCreator,
            Title = "Dataset Creator 语音数据集制作",
            TitleAlign = "center",
            TitleSize = 18,
            Body = "\n"
                "[介绍]\n"
                "该工具会生成适用于语音模型训练的数据集。用户需要提供语音文件与对应的字幕文件。\n"
                "\n"
                "[提示]\n"
                "若有使用完整流程的需求，建议检查以下设置是否正确衔接了前面工具的输出项以及部分设定：\n"
                "WAV Dir\n"
                "SRT Dir\n"
        )
        self.Function_ParamsSynchronizer(
            Button = self.Function_InsertUI(
                ParentUI = self.ui.TextBrowser_Tool_DatasetCreator,
                InsertType = QPushButton,
                InsertPosition = "End",
                UIParam = "Sync 同步",
                UIToolTip = "同步以上设置 (适用于完整流程)"
            ),
            ParamsFrom = [
                self.ui.LineEdit_Tool_VoiceTranscriber_WAV_Dir, #self.ui.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output
                self.ui.LineEdit_Tool_VoiceTranscriber_SRT_Dir
            ],
            ParamsTo = [
                self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,
                self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir
            ]
        )

        self.Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Tool_DatasetCreator_Execute,
            TerminateButton = self.ui.Button_Tool_DatasetCreator_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_DatasetCreator,
            Method = Execute_Dataset_Creating.Execute,
            ParamsFrom = [
                self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir,
                self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,
                self.ui.SpinBox_Tool_DatasetCreator_Sample_Rate,
                self.ui.ComboBox_Tool_DatasetCreator_Subtype,
                self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir_Split,
                self.ui.ComboBox_Tool_DatasetCreator_AutoEncoder,
                self.ui.CheckBox_Tool_DatasetCreator_IsSpeakerMultiple,
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation
            ]
        )
        self.ui.Button_Tool_DatasetCreator_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_DatasetCreator_Execute.setToolTip("执行语音数据集制作")
        self.ui.Button_Tool_DatasetCreator_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_DatasetCreator_Terminate.setToolTip("终止语音数据集制作")

        self.ui.GroupBox_EssentialParams_Page_4.setTitle("EssentialParams 必要参数")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_WAV_Dir,
            Title = "WAV Dir",
            Body = "音频输入目录。该目录中的wav文件将会按照以下设置重采样并根据字幕时间戳进行分割。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_WAV_Dir,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_Sample_Rate,
            Title = "Sample Rate (HZ)",
            Body = "采样率 (HZ)。音频将要使用的新采样率。"
        )
        self.ui.SpinBox_Tool_DatasetCreator_Sample_Rate.setSingleStep(1)
        self.ui.SpinBox_Tool_DatasetCreator_Sample_Rate.setValue(22050)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_Subtype,
            Title = "Subtype",
            Body = "采样格式。音频将要使用的新采样格式。"
        )
        self.ui.ComboBox_Tool_DatasetCreator_Subtype.addItems(['PCM_16'])
        self.ui.ComboBox_Tool_DatasetCreator_Subtype.setCurrentText('PCM_16')

        self.Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_WAV_Dir_Split,
            Title = "WAV Dir Split",
            Body = "音频输出目录。最后处理完成的音频将会保存到该目录中。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_WAV_Dir_Split,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_WAV_Dir_Split,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_SRT_Dir,
            Title = "SRT Dir",
            Body = "字幕输入目录。该目录中的srt文件将会按照以下设置转为适用于模型训练的csv文件。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_SRT_Dir,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_SRT_Dir,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_AutoEncoder,
            Title = "AutoEncoder",
            Body = "自编码器。模型训练所使用的自动编码器。"
        )
        self.ui.ComboBox_Tool_DatasetCreator_AutoEncoder.addItems(['VITS'])
        self.ui.ComboBox_Tool_DatasetCreator_AutoEncoder.setCurrentText('VITS')

        self.Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_IsSpeakerMultiple,
            Title = "Is Speaker Multiple",
            Body = "是否多人。启用以支持多人模型训练。"
        )
        self.ui.CheckBox_Tool_DatasetCreator_IsSpeakerMultiple.setCheckable(True)
        self.ui.CheckBox_Tool_DatasetCreator_IsSpeakerMultiple.setChecked(False)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_FileList_Path_Training,
            Title = "FileList Path Training",
            Body = "训练集文本路径。最后生成的训练集txt文件将会保存到该路径。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_FileList_Path_Training,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
            Mode = "SaveFile",
            FileType = "txt类型 (*.txt)",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_DatasetCreator_FileList_Path_Validation,
            Title = "FileList Path Validation",
            Body = "验证集文本路径。最后生成的验证集txt文件将会保存到该路径。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_DatasetCreator_FileList_Path_Validation,
            LineEdit = self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation,
            Mode = "SaveFile",
            FileType = "txt类型 (*.txt)",
            DisplayText = "None"
        )

        # Page5: Tool_VoiceTrainer
        self.Function_SetText(
            Panel = self.ui.TextBrowser_Tool_VoiceTrainer,
            Title = "Voice Trainer 语音模型训练",
            TitleAlign = "center",
            TitleSize = 18,
            Body = "\n"
                "[介绍]\n"
                "该工具会训练出适用于语音合成的模型文件。用户需要提供语音数据集。\n"
                "\n"
                "[提示]\n"
                "若有使用完整流程的需求，建议检查以下设置是否正确衔接了前面工具的输出项以及部分设定：\n"
                "FileList Path Training\n"
                "FileList Path Validation\n"
        )
        self.Function_ParamsSynchronizer(
            Button = self.Function_InsertUI(
                ParentUI = self.ui.TextBrowser_Tool_VoiceTrainer,
                InsertType = QPushButton,
                InsertPosition = "End",
                UIParam = "Sync 同步",
                UIToolTip = "同步以上设置 (适用于完整流程)"
            ),
            ParamsFrom = [
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Training,
                self.ui.LineEdit_Tool_DatasetCreator_FileList_Path_Validation
            ],
            ParamsTo = [
                self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,
                self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation
            ]
        )

        self.Function_ExecuteMethod(
            ExecuteButton = self.ui.Button_Tool_VoiceTrainer_Execute,
            TerminateButton = self.ui.Button_Tool_VoiceTrainer_Terminate,
            ProgressBar = self.ui.ProgressBar_Tool_VoiceTrainer,
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
                self.ui.LineEdit_Tool_VoiceTrainer_Speakers,
                self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G,
                self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D
            ]
        )
        self.ui.Button_Tool_VoiceTrainer_Execute.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceTrainer_Execute.setToolTip("执行语音模型训练")
        self.ui.Button_Tool_VoiceTrainer_Terminate.setToolTipDuration(-1)
        self.ui.Button_Tool_VoiceTrainer_Terminate.setToolTip("终止语音模型训练")

        self.ui.GroupBox_EssentialParams_Page_5.setTitle("EssentialParams 必要参数")
        
        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_FileList_Path_Training,
            Title = "FileList Path Training",
            Body = "训练集文本路径。该路径对应的训练集txt文件将用于提供训练集音频路径及其语音内容。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_FileList_Path_Training,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Training,
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_FileList_Path_Validation,
            Title = "FileList Path Validation",
            Body = "验证集文本路径。该路径对应的验证集txt文件将用于提供验证集音频路径及其语音内容。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_FileList_Path_Validation,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation,
            Mode = "SelectFile",
            FileType = "txt类型 (*.txt)",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Language,
            Title = "Language",
            Body = "所用语言。音频中说话人所使用的语言。"
        )
        self.ui.ComboBox_Tool_VoiceTrainer_Language.addItems(['mandarin', 'mandarin_english'])
        self.ui.ComboBox_Tool_VoiceTrainer_Language.setCurrentText('mandarin_english')

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Eval_Interval,
            Title = "Eval Interval",
            Body = "评估间隔。每次评估并保存模型所间隔的step数。"
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setValue(1000)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Eval_Interval.setToolTip("建议设置为默认的一千以满足保存的需求")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Epochs,
            Title = "Epochs",
            Body = "迭代轮数。将全部样本完整迭代一轮的次数。"
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setValue(10000)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Epochs.setToolTip("建议为设置一万到两万以获得最佳效果")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Batch_Size,
            Title = "Batch Size",
            Body = "批处理量。每轮迭代中单位批次的样本数量，若用户GPU性能较弱可减小该值。"
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setValue(8)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setToolTipDuration(-1)
        self.ui.SpinBox_Tool_VoiceTrainer_Batch_Size.setToolTip("注意，最好设置为2的幂次。设置为1会导致网络很难收敛。")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Num_Workers,
            Title = "Num Workers",
            Body = "进程数量。进行数据加载时可使用的子进程数量，若用户CPU性能较弱可减小该值。"
        )
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.setSingleStep(1)
        self.ui.SpinBox_Tool_VoiceTrainer_Num_Workers.setValue(8)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_FP16_Run,
            Title = "FP16 Run",
            Body = "半精度训练。通过混合了float16精度的训练方式减小显存占用以支持更大的批处理量。"
        )
        self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run.setCheckable(True)
        self.ui.CheckBox_Tool_VoiceTrainer_FP16_Run.setChecked(True)

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Speakers,
            Title = "Speakers",
            Body = "人物名字。说话人物的名字，单人模型可不填写，多人模型需填写对应名字。"
        )
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setReadOnly(False)
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setText('')
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setToolTipDuration(-1)
        self.ui.LineEdit_Tool_VoiceTrainer_Speakers.setToolTip("注意，不同人物名之间要用逗号隔开。")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Config_Dir_Save,
            Title = "Config Dir Save",
            Body = "配置保存目录。根据以上设置更新参数后的配置文件的保存目录。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Config_Dir_Save,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Config_Dir_Save,
            Mode = "SelectDir",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save,
            Title = "Model Dir Save",
            Body = "模型保存目录。最后生成的模型的存放目录。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Dir_Save,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Dir_Save,
            Mode = "SelectDir",
            DisplayText = "None"
        )
        self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save.setToolTipDuration(-1)
        self.ui.Label_Tool_VoiceTrainer_Model_Dir_Save.setToolTip("注意，请勿将不同数据集训练得到的模型置于同一目录下。")

        self.ui.GroupBox_OptionalParams_Page_5.setTitle("OptionalParams 可选参数")

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Config_Path_Load,
            Title = "Config Path Load",
            Body = "配置加载路径。该路径对应的配置文件将会替代默认的配置文件。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Config_Path_Load,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Config_Path_Load,
            Mode = "SelectFile",
            FileType = "json类型 (*.json)",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            Title = "Model Path Pretrained G",
            Body = "预训练G模型路径。该路径对应的预训练生成器（Generator）模型会被视作检查点。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            DisplayText = "None"
        )

        self.Function_SetText(
            Panel = self.ui.Label_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            Title = "Model Path Pretrained D",
            Body = "预训练D模型路径。该路径对应的预训练判别器（Discriminator）模型会被视作检查点。"
        )
        self.Function_SetFileDialog(
            Button = self.ui.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            LineEdit = self.ui.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D,
            Mode = "SelectFile",
            FileType = "pth类型 (*.pth)",
            DisplayText = "None"
        )

        # Toggle/Burger Console
        self.ui.Button_Toggle_Console.clicked.connect(
            lambda: self.Function_AnimateFrame(
                Frame = self.ui.Frame_Console,
                MinWidth = 45,
                MaxWidth = 333
            )
        )
        self.ui.Button_Toggle_Console.setCheckable(True)
        self.ui.Button_Toggle_Console.setChecked(False)
        self.ui.Button_Toggle_Console.setAutoExclusive(False)
        self.ui.Button_Toggle_Console.setToolTipDuration(-1)
        self.ui.Button_Toggle_Console.setToolTip("Click to toggle/burger console")

        # Show MainWindow
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)

    Window = MainWindow()
    Window.Main()
    
    sys.exit(App.exec())