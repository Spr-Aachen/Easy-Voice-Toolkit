import os
import sys
sys.path.append('..')
import re
import psutil
import pynvml
from typing import Optional
from PySide6.QtCore import QObject, QThread, QMutex, Signal, Slot, QPropertyAnimation, QEasingCurve, QUrl#, QTimer, QEventLoop
from PySide6.QtGui import QTextCursor, QDesktopServices
from PySide6.QtWidgets import *

from Run import (Execute_Env_Configurator, Execute_Audio_Processing, Execute_Voice_Identifying, Execute_Voice_Transcribing, Execute_Dataset_Creating, Execute_Voice_Training, Execute_Voice_Converting)


# Handle the consol's output
class ConsolOutputHandler(QThread):
    '''
    Intercept the output of the consol and send to the UI
    '''
    Signal_ConsoleInfo = Signal(str)

    def __init__(self):
        super().__init__()

        self.Mutex = QMutex()

    def run(self):
        '''
        Function to redirect stdout & stderr to the childthread
        '''
        sys.stdout = self
        sys.stderr = self

    def write(self,
        Info: object
    ):
        '''
        Function to override the default write functions of sys.stdout & sys.stderr
        '''
        self.Mutex.lock()

        self.Signal_ConsoleInfo.emit(str(Info))

        self.Mutex.unlock()

        '''
        EventLoop = QEventLoop()
        QTimer.singleShot(123, EventLoop.quit)
        EventLoop.exec()
        '''

    def flush(self):
        '''
        Function to override the default flush functions of sys.stdout & sys.stderr
        '''
        pass


# Monitor the cpu&gpu's usage
class MonitorUsage(QThread):
    '''
    Get the usage of CPU and GPU and send to the UI
    '''
    Signal_UsageInfo = Signal(str, str)

    def __init__(self):
        super().__init__()

        pynvml.nvmlInit()
    '''
        Timer = QTimer(self)
        Timer.timeout.connect(self.MonitorUsage)
        Timer.start(1000)

    def MonitorUsage(self):
        Usage_CPU_Percent = psutil.cpu_percent(interval = 1.)
        Usage_CPU = f"{Usage_CPU_Percent}%"

        #Usage_RAM_Percent = psutil.virtual_memory().percent
        #Usage_RAM = f"{Usage_RAM_Percent}%"

        Usage_GPU_Percent = 0
        for Index in range(pynvml.nvmlDeviceGetCount()):
            Usage_GPU_Percent += pynvml.nvmlDeviceGetUtilizationRates(pynvml.nvmlDeviceGetHandleByIndex(Index)).gpu
        Usage_GPU = f"{Usage_GPU_Percent}%"

        self.Signal_UsageInfo.emit(Usage_CPU, Usage_GPU)
    '''
    def run(self):
        while True:
            Usage_CPU_Percent = psutil.cpu_percent(interval = 1.)
            Usage_CPU = f"{Usage_CPU_Percent}%"

            #Usage_RAM_Percent = psutil.virtual_memory().percent
            #Usage_RAM = f"{Usage_RAM_Percent}%"

            Usage_GPU_Percent = 0
            for Index in range(pynvml.nvmlDeviceGetCount()):
                Usage_GPU_Percent_Single = pynvml.nvmlDeviceGetUtilizationRates(pynvml.nvmlDeviceGetHandleByIndex(Index)).gpu
                Usage_GPU_Percent = Usage_GPU_Percent_Single if Usage_GPU_Percent < Usage_GPU_Percent_Single else Usage_GPU_Percent
            Usage_GPU = f"{Usage_GPU_Percent}%"

            self.Signal_UsageInfo.emit(Usage_CPU, Usage_GPU)

            self.msleep(1000)


# Where to store custom signals
class CustomSignals(QObject):
    '''
    Set up signals for custom functions
    '''
    # Monitor frame
    Signal_FrameStatus = Signal(str)

    # Run task
    Signal_ExecuteTask = Signal(list)


Signals = CustomSignals()


def Function_FindParentUI(
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


def Function_InsertUI(
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
                "color: rgba(255, 255, 255, 210);"
                "background-color: transparent;"
                "border-width: 0px;"
                "border-style: solid;"
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


def Function_ConfigureCheckBox(
    CheckBox: QCheckBox,
    CheckedText: str = ...,
    CheckedPermEventList: list = [],
    CheckedPermArgsList: list = [()],
    CheckedTempEventList: list = [],
    CheckedTempArgsList: list = [()],
    UncheckedText: str = ...,
    UncheckedPermEventList: list = [],
    UncheckedPermArgsList: list = [()],
    UncheckedTempEventList: list = [],
    UncheckedTempArgsList: list = [()]
):
    '''
    Function to configure checkbox
    '''
    CheckBox.toggled.connect(lambda: CheckBox.setText(CheckedText) if CheckBox.isChecked() else CheckBox.setText(UncheckedText))

    def SetToggleEvent(EventList, ArgsList, IsPermanent, IsChecked, CheckBox):
        for Index, Event in enumerate(EventList):
            Args = ArgsList[Index]
            if IsChecked:
                Event(*Args) if IsPermanent and CheckBox.isChecked() else None
                CheckBox.toggled.connect(lambda: Event(*Args) if CheckBox.isChecked() else None)
            else:
                Event(*Args) if IsPermanent and not CheckBox.isChecked() else None
                CheckBox.toggled.connect(lambda: Event(*Args) if not CheckBox.isChecked() else None)

    SetToggleEvent(CheckedPermEventList, CheckedPermArgsList, True, True, CheckBox)
    SetToggleEvent(CheckedTempEventList, CheckedTempArgsList, False, True, CheckBox)
    SetToggleEvent(UncheckedPermEventList, UncheckedPermArgsList, True, False, CheckBox)
    SetToggleEvent(UncheckedTempEventList, UncheckedTempArgsList, False, False, CheckBox)


@Slot(str)
def Function_AnimateStackedWidget(
    StackedWidget: QStackedWidget,
    TargetIndex: int = 0,
    Duration: int = 0
):
    '''
    Function to animate stackedwidget
    '''
    Index_Current = StackedWidget.currentIndex()

    def AnimateStackedWidget(Index_Altered):
        WidgetAnimation = QPropertyAnimation(StackedWidget, b"currentIndex")
        WidgetAnimation.setStartValue(Index_Current)
        WidgetAnimation.setEndValue(Index_Altered)
        WidgetAnimation.setDuration(Duration)
        WidgetAnimation.setEasingCurve(QEasingCurve.InOutQuart)
        WidgetAnimation.start()

    AnimateStackedWidget(TargetIndex)


@Slot(str)
def Function_AnimateFrame(
    Frame: QFrame,
    MinWidth: int = ...,
    MaxWidth: int = ...,
    MinHeight: int = ...,
    MaxHeight: int = ...,
    Duration: int = 0,
    Mode: str = "Toggle"
):
    '''
    Function to animate frame
    '''
    Width_Current = Frame.width()
    Height_Current = Frame.height()
    
    def AnimateFrame(Type, Length_Altered):
        if Type == "Width":
            FrameAnimation1 = QPropertyAnimation(Frame, b"minimumWidth")
            FrameAnimation2 = QPropertyAnimation(Frame, b"maximumWidth")
            for FrameAnimation in [FrameAnimation1, FrameAnimation2]:
                FrameAnimation.setStartValue(Width_Current)
                FrameAnimation.setEndValue(Length_Altered)
                FrameAnimation.setDuration(Duration)
                FrameAnimation.setEasingCurve(QEasingCurve.InOutQuart)
        if Type == "Height":
            FrameAnimation1 = QPropertyAnimation(Frame, b"minimumHeight")
            FrameAnimation2 = QPropertyAnimation(Frame, b"maximumHeight")
            for FrameAnimation in [FrameAnimation1, FrameAnimation2]:
                FrameAnimation.setStartValue(Height_Current)
                FrameAnimation.setEndValue(Length_Altered)
                FrameAnimation.setDuration(Duration)
                FrameAnimation.setEasingCurve(QEasingCurve.InOutQuart)
        FrameAnimation1.start()
        FrameAnimation2.start()

    if Mode == "Extend":
        if MaxWidth != ...:
            AnimateFrame("Width", MaxWidth)
        if MaxHeight != ...:
            AnimateFrame("Height", MaxHeight)
        Signals.Signal_FrameStatus.emit(f"{Frame.objectName()}Extended")
    if Mode == "Reduce":
        if MinWidth != ...:
            AnimateFrame("Width", MinWidth)
        if MinHeight != ...:
            AnimateFrame("Height", MinHeight)
        Signals.Signal_FrameStatus.emit(f"{Frame.objectName()}Reduced")
    if Mode == "Toggle":
        if Width_Current == MinWidth or Height_Current == MinHeight:
            if MaxWidth != ...:
                AnimateFrame("Width", MaxWidth)
            if MaxHeight != ...:
                AnimateFrame("Height", MaxHeight)
            Signals.Signal_FrameStatus.emit(f"{Frame.objectName()}Extended")
        else:
            if MinWidth != ...:
                AnimateFrame("Width", MinWidth)
            if MinHeight != ...:
                AnimateFrame("Height", MinHeight)
            Signals.Signal_FrameStatus.emit(f"{Frame.objectName()}Reduced")


@Slot(str)
def Function_AnimateButton(
    Button: QPushButton,
    Frame: Optional[QFrame] = None,
    FrameStatus: str = ...,
    Text: str = ...
):
    '''
    Function to animate button
    '''
    Frame = Function_FindParentUI(
        ChildUI = Button,
        ParentType = QFrame
    ) if Frame == None else Frame

    if FrameStatus == f"{Frame.objectName()}Extended":
        Button.setText(Text)
    if FrameStatus == f"{Frame.objectName()}Reduced":
        Button.setText("")


def Function_PrintText(
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

    Frame = Function_FindParentUI(
        ChildUI = Panel,
        ParentType = QFrame
    ) if Frame == None else Frame

    if FrameStatus == f"{Frame.objectName()}Extended":
        Panel.setVisible(True)
    if FrameStatus == f"{Frame.objectName()}Reduced":
        Panel.setVisible(False)


def Function_SetText(
    Panel: QObject,
    Title: Optional[str] = ...,
    TitleAlign: str = "left",
    TitleSize: float = 9.9,
    TitleWeight: float = 840.,
    TitleColor: str = "#ffffff",
    TitleLineHeight: float = 21.,
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
        ) if Content != None else ""
        return f"<p style={Style}>{Content}</p>"

    Text = (
        "<html>"
            "<head>"
                f"<title>{ToHtml(Title, TitleAlign, TitleSize, TitleWeight, TitleColor, TitleLineHeight)}</title>" # Not Working
            "</head>"
            "<body>"
                f"{ToHtml(Title, TitleAlign, TitleSize, TitleWeight, TitleColor, TitleLineHeight)}"
                f"{ToHtml(Body, BodyAlign, BodySize, BodyWeight, BodyColor, BodyLineHeight)}"
            "</body>"
        "</html>"
    )

    if isinstance(Panel, QLabel):
        Panel.setText(Text)
    if isinstance(Panel, QTextBrowser):
        Panel.setHtml(Text)


def Function_SetFileDialog(
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

    @Slot()
    def SetFileDialog():
        if Mode == "SelectDir":
            DisplayText = QFileDialog.getExistingDirectory(
                caption = "选择文件夹",
                dir = os.getcwd()
            )
        if Mode == "SelectFile":
            DisplayText, _ = QFileDialog.getOpenFileName(
                caption = "选择文件",
                dir = os.getcwd(),
                filter = FileType
            )
        if Mode == "SaveFile":
            DisplayText, _ = QFileDialog.getSaveFileName(
                caption = "保存文件",
                dir = os.getcwd(),
                filter = FileType
            )

        LineEdit.setText(DisplayText)
        LineEdit.setStatusTip(DisplayText)
    
    Button.clicked.connect(SetFileDialog)
    Button.setToolTipDuration(-1)
    Button.setToolTip(ButtonTooltip)


def Function_ShowMessageBox(
    MessageType: object = QMessageBox.Information,
    WindowTitle: str = ...,
    Text: str = ...,
    Buttons: object = QMessageBox.Ok,
    EventsButtons: list = [],
    Events: list = []
):
    '''
    Function to pop up a msgbox
    '''
    MsgBox = QMessageBox()

    MsgBox.setIcon(MessageType)
    MsgBox.setWindowTitle(WindowTitle)
    MsgBox.setText(Text)
    MsgBox.setStandardButtons(Buttons)
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

    @Slot(QPushButton)
    @Slot(QToolButton)
    def ConnectEvent(Button):
        if Button in EventsButtons:
            Events[EventsButtons.index(Button)]
        else:
            pass
    MsgBox.buttonClicked.connect(
        lambda Button: ConnectEvent(Button)
    )

    MsgBox.exec()


def Function_ParamsHandler(
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
        if isinstance(UI, QPlainTextEdit):
            return UI.toPlainText()
        if isinstance(UI, QComboBox):
            return UI.currentText()
        if isinstance(UI, (QSlider, QSpinBox, QDoubleSpinBox)):
            return UI.value()
        if isinstance(UI, (QCheckBox, QRadioButton)):
            return UI.isChecked()
    if Mode == "Set":
        if isinstance(UI, QLineEdit):
            UI.setText(Param)
        if isinstance(UI, QPlainTextEdit):
            UI.setPlainText(Param)
        if isinstance(UI, QComboBox):
            UI.setCurrentText(Param)
        if isinstance(UI, (QSlider, QSpinBox, QDoubleSpinBox)):
            UI.setValue(Param)
        if isinstance(UI, (QCheckBox, QRadioButton)):
            UI.setChecked(Param)


def Function_ParamsSynchronizer(
    Trigger: QObject, #Trigger: QObject | list,
    ParamsFrom: list = [],
    Times: Optional[float] = None,
    ParamsTo: list = [],
    Connection: str = "Connect"
):
    '''
    Function to synchronize params
    '''
    @Slot()
    def ParamsSynchronizer():
        for Index, UI_Get in enumerate(ParamsFrom):
            UI_Set = ParamsTo[Index]
            Param_Get = Function_ParamsHandler(UI_Get, "Get")
            Param_Get = Param_Get * Times if isinstance(Param_Get, (int, float, complex)) else Param_Get
            Function_ParamsHandler(UI_Set, Param_Get, "Set")
    
    try:
        iter(Trigger)
        TriggerList = Trigger
    except:
        TriggerList = []
        TriggerList.append(Trigger)

    for Trigger in TriggerList:
        if isinstance(Trigger, (QPushButton, QToolButton)):
            Trigger.clicked.connect(ParamsSynchronizer) if Connection == "Connect" else Trigger.clicked.disconnect(ParamsSynchronizer)
        if isinstance(Trigger, (QSlider, QSpinBox, QDoubleSpinBox)):
            Trigger.valueChanged.connect(ParamsSynchronizer) if Connection == "Connect" else Trigger.valueChanged.disconnect(ParamsSynchronizer)
        if isinstance(Trigger, QLineEdit):
            Trigger.textChanged.connect(ParamsSynchronizer) if Connection == "Connect" else Trigger.textChanged.disconnect(ParamsSynchronizer)


def Function_ParamsChecker(
    ParamsFrom: list = [],
    EmptyAllowed: list = []
):
    '''
    Function to return handled params
    '''
    Params = []

    for UI in ParamsFrom:
        Param = Function_ParamsHandler(UI, "Get")
        if isinstance(Param, str):
            if Param == "None" or Param == "":
                if UI in EmptyAllowed:
                    Param = None
                else:
                    Function_ShowMessageBox(
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


def Function_AnimateProgressBar(
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


def Function_ExecuteMethod(
    ExecuteButton: QPushButton,
    TerminateButton: Optional[QPushButton],
    ProgressBar: Optional[QProgressBar],
    ConsoleFrame: Optional[QFrame],
    Method: object,
    ParamsFrom: list = [],
    EmptyAllowed: list = []
):
    '''
    Function to execute outer class methods (through button)
    '''
    StackedWidget = Function_FindParentUI(
        ChildUI = ExecuteButton, #ChildUI = TerminateButton,
        ParentType = QStackedWidget
    ) if TerminateButton else None
    
    ClassName =  str(Method.__qualname__).split('.')[0]
    MethodName = str(Method.__qualname__).split('.')[1]

    ClassInstance = globals()[ClassName]()
    WorkerThread = QThread()

    ClassInstance.moveToThread(WorkerThread)
    ClassInstance.finished.connect(WorkerThread.quit)
    #ClassInstance.finished.connect(WorkerThread.wait)

    @Slot()
    def ExecuteMethod():
        '''
        Update the attributes for outer class methods and wait to execute with multithreading
        '''

        if Function_ParamsChecker(ParamsFrom, EmptyAllowed) != "Abort":
            Params = Function_ParamsChecker(ParamsFrom, EmptyAllowed)
        else:
            return print("Aborted.")

        Signals.Signal_ExecuteTask.connect(getattr(ClassInstance, MethodName))

        WorkerThread.started.connect(lambda: Function_AnimateFrame(Frame = ConsoleFrame, MinHeight = 0, MaxHeight = 210, Mode = "Extend")) if ConsoleFrame else None
        WorkerThread.started.connect(lambda: Function_AnimateProgressBar(ProgressBar = ProgressBar, IsTaskAlive = True)) if ProgressBar else None
        WorkerThread.started.connect(lambda: Function_AnimateStackedWidget(StackedWidget = StackedWidget, TargetIndex = 1)) if TerminateButton else None
        WorkerThread.finished.connect(lambda: Function_AnimateProgressBar(ProgressBar = ProgressBar, IsTaskAlive = False)) if ProgressBar else None
        WorkerThread.finished.connect(lambda: Function_AnimateStackedWidget(StackedWidget = StackedWidget, TargetIndex = 0)) if TerminateButton else None
        WorkerThread.finished.connect(lambda: Function_AnimateFrame(Frame = ConsoleFrame, MinHeight = 0, MaxHeight = 210, Mode = "Reduce")) if ConsoleFrame else None
        WorkerThread.finished.connect(lambda: Function_ShowMessageBox(WindowTitle = "提示", Text = "执行结束"))
        WorkerThread.finished.connect(lambda: Signals.Signal_ExecuteTask.disconnect(getattr(ClassInstance, MethodName)))
        WorkerThread.start()

        Signals.Signal_ExecuteTask.emit(Params)

    ExecuteButton.clicked.connect(ExecuteMethod)
    ExecuteButton.setText("Execute 执行") if ExecuteButton.text() == "" else None

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
    
        ProgressBar.setValue(0)

        Function_AnimateFrame(
            Frame = ConsoleFrame,
            MinHeight = 0,
            MaxHeight = 210,
            Mode = "Reduce"
        ) if ConsoleFrame else None

    TerminateButton.clicked.connect(TerminateMethod) if TerminateButton else None
    TerminateButton.setText("Terminate 终止") if TerminateButton != None and TerminateButton.text() == "" else None


def Function_SetURL(
    Button: QPushButton,
    URL: str, #URL: str | list
    ButtonTooltip: str = "Open"
):
    '''
    Function to open web/local URL
    '''
    def toQURL(URL):
        QURL = QUrl(URL)
        if QURL.isValid():
            QURL_Localized = QURL.toLocalFile()
            QDesktopServices.openUrl(QURL_Localized) if QURL_Localized != "" else QDesktopServices.openUrl(QURL)
        else:
            print(f"Invalid URL: {URL} !")

    @Slot()
    def SetURL(URL):
        if isinstance(URL, str):
            toQURL(URL)
        else:
            try:
                iter(URL)
                URLList = URL
            except:
                URLList = []
                URLList.append(URL)
            for Index, URL in enumerate(URLList):
                URL = Function_ParamsChecker(URLList)[Index] if isinstance(URL, QObject) else URL
                toQURL(URL)

    Button.clicked.connect(lambda: SetURL(URL))
    Button.setToolTipDuration(-1)
    Button.setToolTip(ButtonTooltip)