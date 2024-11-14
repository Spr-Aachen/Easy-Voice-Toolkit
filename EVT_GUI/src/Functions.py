import os
import platform
from typing import Union, Optional
from PySide6.QtCore import Qt, QObject, Signal, Slot, QThread, QPoint
from PySide6.QtCore import QCoreApplication as QCA
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMessageBox
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets.Components import *

from components.Components import *
from windows.Windows import *

##############################################################################################################################

# Where to store custom signals
class CustomSignals_Functions(QObject):
    '''
    Set up signals for functions
    '''
    # Run task
    Signal_ExecuteTask = Signal(tuple)

    # Monitor task
    Signal_TaskStatus = Signal(str, str)

    # Force exit
    Signal_ForceQuit = Signal()


    Signal_UpdateMessage = Signal(str)

    Signal_IsUpdateSucceeded = Signal(bool, str)

    Signal_ReadyToUpdate = Signal(str, str)


FunctionSignals = CustomSignals_Functions()

##############################################################################################################################

def Function_ScrollToWidget(
    trigger: QWidget,
    targetWidget: QWidget,
    scrollArea: Optional[QScrollArea] = None,
    #alignment: str = 'Top'
):
    '''
    '''
    if scrollArea is None:
        scrollArea = QFunc.findParentUI(targetWidget, QScrollArea)

    def ScrollToWidget():
        TargetRect = targetWidget.mapToGlobal(QPoint(0, 0))
        TargetYPos = TargetRect.y() - scrollArea.widget().mapToGlobal(QPoint(0, 0)).y()

        scrollArea.verticalScrollBar().setValue(TargetYPos)

    if isinstance(trigger, QTreeWidgetItem):
        def TreeWidgetEvent(Item, Column):
            ScrollToWidget() if Item == trigger else None
        trigger.treeWidget().itemClicked.connect(TreeWidgetEvent)

    if isinstance(trigger, QAbstractButton):
        trigger.clicked.connect(ScrollToWidget)


def Function_AddToTreeWidget(
    widget: QWidget,
    treeWidget: TreeWidgetBase,
    rootItemText: str,
    childItemText: Optional[str] = None,
    scrollArea: Optional[QScrollArea] = None
):
    '''
    '''
    RootItemTexts = treeWidget.rootItemTexts()
    if rootItemText in RootItemTexts:
        RootItem = treeWidget.topLevelItem(RootItemTexts.index(rootItemText))
    else:
        RootItem = QTreeWidgetItem(treeWidget)
        RootItem.setText(0, rootItemText)
        RootItemTextFont = QFont()
        RootItemTextFont.setPixelSize(15)
        RootItem.setFont(0, RootItemTextFont)
    RootItem.setExpanded(True) if not RootItem.isExpanded() else None

    ChildItemTexts = treeWidget.childItemTexts(RootItem)
    if childItemText is None:
        ChildItem = None
    elif childItemText in ChildItemTexts:
        ChildItem = RootItem.child(ChildItemTexts.index(childItemText))
    else:
        ChildItem = QTreeWidgetItem(RootItem)
        ChildItem.setText(0, childItemText)
        ChildItemTextFont = QFont()
        ChildItemTextFont.setPixelSize(12)
        ChildItem.setFont(0, ChildItemTextFont)

    Function_ScrollToWidget(
        trigger = ChildItem if ChildItem is not None else RootItem,
        targetWidget = widget,
        scrollArea = scrollArea
    )


def Function_SetChildWidgetsVisibility(
    container: QWidget,
    childWidgets: list[Optional[QWidget]],
    setVisible: bool,
    adjustContainer: bool = True
):
    '''
    Function to set the visibility of child-widgets
    '''
    childWidgets = [ChildWidget for ChildWidget in childWidgets if ChildWidget is not None]
    for ChildWidget in childWidgets:
        ChildWidget.setVisible(setVisible)
    if adjustContainer:
        CurrentHeight = container.height()
        #container.updateGeometry()
        AdjustedHeight = container.minimumSizeHint().height()
        Function_AnimateFrame(
            frame = container,
            minHeight = CurrentHeight if setVisible else AdjustedHeight,
            maxHeight = AdjustedHeight if setVisible else CurrentHeight,
            mode = 'Extend' if setVisible else 'Reduce'
        )


def Function_ConfigureCheckBox(
    checkBox: QCheckBox,
    checkedText: Optional[str] = None,
    checkedEvents: list = [],
    uncheckedText: Optional[str] = None,
    uncheckedEvents: list = [],
    takeEffect: bool = False
):
    '''
    Function to configure checkbox
    '''
    if checkedText is not None:
        checkedEvents.append(lambda: checkBox.setText(checkedText))
    if uncheckedText is not None:
        uncheckedEvents.append(lambda: checkBox.setText(uncheckedText))

    checkBox.toggled.connect(
        lambda IsChecked: QFunc.runEvents(checkedEvents if IsChecked else uncheckedEvents)
    )

    QFunc.runEvents(checkedEvents) if takeEffect and checkBox.isChecked() else None
    QFunc.runEvents(uncheckedEvents) if takeEffect and not checkBox.isChecked() else None


def Function_SetURL(
    button: QAbstractButton,
    url: Union[str, QWidget, list],
    buttonTooltip: str = "Open",
    createIfNotExist: bool = False
):
    '''
    Function to open url (through button)
    '''
    button.clicked.connect(
        lambda: QFunc.openURL([(Function_GetParam(url) if isinstance(url, QWidget) else url) for url in QFunc.toIterable(url)], createIfNotExist)
    )
    button.setToolTipDuration(-1)
    button.setToolTip(buttonTooltip)

##############################################################################################################################

def Function_GetParam(
    ui: QObject
):
    '''
    Function to get the param of ui
    '''
    if isinstance(ui, (QLineEdit, QTextEdit, QPlainTextEdit)):
        return QFunc.getText(ui)
    if isinstance(ui, QComboBox):
        return ui.currentText()
    if isinstance(ui, (QAbstractSpinBox, QSlider, Frame_RangeSetting)):
        return ui.value()
    if isinstance(ui, (QCheckBox, QRadioButton)):
        return ui.isChecked()

    if isinstance(ui, Table_EditAudioSpeaker):
        return ui.getValue()


def Function_SetParam(
    ui: QObject,
    param: Optional[str]
):
    '''
    Function to set the param of ui
    '''
    if isinstance(ui, (QLineEdit, QTextEdit)):
        ui.setText(param)
    if isinstance(ui, QPlainTextEdit):
        ui.setPlainText(param)
    if isinstance(ui, QComboBox):
        ui.setCurrentText(param)
    if isinstance(ui, (QAbstractSpinBox, QSlider, Frame_RangeSetting)):
        ui.setValue(param)
    if isinstance(ui, (QCheckBox, QRadioButton)):
        ui.setChecked(param)

    if isinstance(ui, Table_EditAudioSpeaker):
        ui.setValue(param)


def Function_ParamsSynchronizer(
    trigger: Union[QObject, list],
    fromTo: dict = {},
    times: Union[int, float] = 1,
    connection: str = "Connect"
):
    '''
    Function to synchronize params (paramsFrom.value * times = ParamsTo.value)
    '''
    @Slot()
    def ParamsSynchronizer():
        for UI_Get, UI_Set in fromTo.items():
            Param_Get = Function_GetParam(UI_Get)
            Param_Get = Param_Get * times if isinstance(Param_Get, (int, float, complex)) else Param_Get
            for UI_Set in QFunc.toIterable(UI_Set):
                Function_SetParam(UI_Set, Param_Get)

    TriggerList = QFunc.toIterable(trigger)

    for trigger in TriggerList:
        if isinstance(trigger, QAbstractButton):
            trigger.clicked.connect(ParamsSynchronizer) if connection == "Connect" else trigger.clicked.disconnect(ParamsSynchronizer)
        if isinstance(trigger, QAbstractSlider):
            trigger.sliderMoved.connect(ParamsSynchronizer) if connection == "Connect" else trigger.sliderMoved.disconnect(ParamsSynchronizer)
        if isinstance(trigger, QAbstractSpinBox):
            trigger.valueChanged.connect(ParamsSynchronizer) if connection == "Connect" else trigger.valueChanged.disconnect(ParamsSynchronizer)
        if isinstance(trigger, (QLineEdit)):
            trigger.textChanged.connect(ParamsSynchronizer) if connection == "Connect" else trigger.textChanged.disconnect(ParamsSynchronizer)


def Function_ParamsChecker(
    paramsFrom: list = [],
    emptyAllowed: list = []
):
    '''
    Function to return handled params
    '''
    params = []

    for ui in paramsFrom:
        param = Function_GetParam(ui) if isinstance(ui, QWidget) else ui
        if isinstance(param, str):
            if param.strip() == "None" or param.strip() == "":
                if ui in QFunc.toIterable(emptyAllowed):
                    param = None
                else:
                    MessageBoxBase.pop(
                        messageType = QMessageBox.Warning,
                        windowTitle = "Warning",
                        text = "Empty param detected!\n检测到参数空缺！"
                    )
                    return "Abort"
            else:
                '''
                if "，" in param or "," in param:
                    param = re.split(
                        pattern = '[，,]',
                        string = param,
                        maxsplit = 0
                    )
                '''
        if isinstance(param, dict):
            if "None" in list(param.keys()&param.values()) or "" in list(param.keys()&param.values()):
                if ui in QFunc.toIterable(emptyAllowed):
                    param = None
                else:
                    MessageBoxBase.pop(
                        messageType = QMessageBox.Warning,
                        windowTitle = "Warning",
                        text = "Empty param detected!\n检测到参数空缺！"
                    )
                    return "Abort"
            else:
                pass
        else:
            pass
        params.append(param)

    Args = tuple(params)#if params != [] else None

    return Args

##############################################################################################################################

def Function_AnimateStackedWidget(
    stackedWidget: QStackedWidget,
    target: Union[int, QWidget] = 0,
    duration: int = 99
):
    '''
    Function to animate stackedwidget
    '''
    OriginalWidget = stackedWidget.currentWidget()
    OriginalGeometry = OriginalWidget.geometry()

    if isinstance(target, int):
        TargetIndex = target
    if isinstance(target, QWidget):
        TargetIndex = stackedWidget.indexOf(target)

    WidgetAnimation = QFunc.setWidgetPosAnimation(OriginalWidget, duration)
    WidgetAnimation.finished.connect(
        lambda: stackedWidget.setCurrentIndex(TargetIndex),
        type = Qt.QueuedConnection
    )
    WidgetAnimation.finished.connect(
        lambda: OriginalWidget.setGeometry(OriginalGeometry),
        type = Qt.QueuedConnection
    )
    WidgetAnimation.start() if stackedWidget.currentIndex() != TargetIndex else None


def Function_AnimateFrame(
    frame: QWidget,
    minWidth: Optional[int] = None,
    maxWidth: Optional[int] = None,
    minHeight: Optional[int] = None,
    maxHeight: Optional[int] = None,
    duration: int = 210,
    mode: str = "Toggle",
    supportSplitter: bool = False
):
    '''
    Function to animate frame
    '''
    def ExtendFrame():
        QFunc.setWidgetSizeAnimation(frame, maxWidth, None, duration, supportSplitter).start() if maxWidth not in (None, frame.width()) else None
        QFunc.setWidgetSizeAnimation(frame, None, maxHeight, duration, supportSplitter).start() if maxHeight not in (None, frame.height()) else None

    def ReduceFrame():
        QFunc.setWidgetSizeAnimation(frame, minWidth, None, duration, supportSplitter).start() if minWidth not in (None, frame.width()) else None
        QFunc.setWidgetSizeAnimation(frame, None, minHeight, duration, supportSplitter).start() if minHeight not in (None, frame.height()) else None

    if mode == "Extend":
        ExtendFrame()
    if mode == "Reduce":
        ReduceFrame()
    if mode == "Toggle":
        ExtendFrame() if frame.width() == minWidth or frame.height() == minHeight else ReduceFrame()


def Function_AnimateProgressBar(
    progressBar: QProgressBar,
    minValue: int = 0,
    maxValue: int = 100,
    displayValue: bool = False,
    isTaskAlive: bool = False
):
    '''
    Function to animate progressbar
    '''
    progressBar.setTextVisible(displayValue)
    progressBar.setRange(minValue, maxValue)
    progressBar.setValue(minValue)

    if isTaskAlive == True:
        progressBar.setRange(0, 0)
        #QApplication.processEvents()
    else:
        progressBar.setRange(minValue, maxValue)
        progressBar.setValue(maxValue)

##############################################################################################################################

def Function_SetWidgetValue(
    widget: QWidget,
    config: QFunc.configManager,
    section: str = ...,
    option: str = ...,
    value = ...,
    times: Union[int, float] = 1,
    setPlaceholderText: bool = False,
    placeholderText: Optional[str] = None
):
    if isinstance(widget, (QLineEdit, QTextEdit, QPlainTextEdit)):
        QFunc.setText(widget, value, setPlaceholderText = setPlaceholderText, placeholderText = placeholderText)
        def EditConfig(value):
            config.editConfig(section, option, str(value))
        if config is not None:
            widget.textChanged.connect(lambda: EditConfig(widget.text() if isinstance(widget, (QLineEdit)) else widget.toPlainText()))
            EditConfig(value)

    if isinstance(widget, (QComboBox)):
        itemTexts = []
        for index in range(widget.count()):
            itemTexts.append(widget.itemText(index))
        widget.setCurrentText(str(value)) if str(value) in itemTexts else None
        def EditConfig(value):
            config.editConfig(section, option, str(value))
        if config is not None:
            widget.currentTextChanged.connect(EditConfig)
            EditConfig(value) if str(value) in itemTexts else None

    if isinstance(widget, (QSpinBox, QSlider)):
        widget.setValue(int(eval(str(value)) * times))
        def EditConfig(value):
            config.editConfig(section, option, str(eval(str(value)) / times))
        if config is not None:
            widget.valueChanged.connect(EditConfig)
            EditConfig(value)

    if isinstance(widget, (QDoubleSpinBox, SliderBase, Frame_RangeSetting)):
        widget.setValue(float(eval(str(value)) * times))
        def EditConfig(value):
            config.editConfig(section, option, str(eval(str(value)) / times))
        if config is not None:
            widget.valueChanged.connect(EditConfig)
            EditConfig(value)

    if isinstance(widget, (QCheckBox, QRadioButton)):
        widget.setChecked(eval(str(value)))
        def EditConfig(value):
            config.editConfig(section, option, str(value))
        if config is not None:
            widget.toggled.connect(EditConfig)
            EditConfig(value)

    if isinstance(widget, Table_EditAudioSpeaker):
        widget.setValue(eval(str(value)))
        def EditConfig(value):
            config.editConfig(section, option, str(value))
        if config is not None:
            widget.ValueChanged.connect(EditConfig)
            EditConfig(value)


class ParamsManager:
    def __init__(self,
        configPath: str,
    ):
        self.configPath = configPath
        self.config = QFunc.configManager(configPath)

        self.RegistratedWidgets = {}

    def registrate(self, widget: QWidget, value: tuple):
        self.RegistratedWidgets[widget] = value

    def SetParam(self,
        widget: QWidget,
        section: str = ...,
        option: str = ...,
        defaultValue = None,
        times: Union[int, float] = 1,
        setPlaceholderText: bool = False,
        placeholderText: Optional[str] = None,
        registrate: bool = True
    ):
        value = self.config.getValue(section, option, str(defaultValue))
        Function_SetWidgetValue(widget, self.config, section, option, value, times, setPlaceholderText, placeholderText)
        self.registrate(widget, (section, option, defaultValue, times, setPlaceholderText, placeholderText)) if registrate else None

    def ResetParam(self, widget: QWidget):
        value = self.RegistratedWidgets[widget]
        Function_SetWidgetValue(widget, self.config, *value)

    def ClearSettings(self):
        with open(self.configPath, 'w'):
            pass
        self.config = QFunc.configManager(self.configPath)

    def ResetSettings(self):
        self.ClearSettings()
        for widget in list(self.RegistratedWidgets.keys()):
            self.ResetParam(widget)

    def ImportSettings(self, readPath: str):
        configParser = QFunc.configManager(readPath).parser()
        with open(self.configPath, 'w', encoding = 'utf-8') as config:
            configParser.write(config)
        for widget, value in list(self.RegistratedWidgets.items()):
            self.SetParam(widget, *value)

    def ExportSettings(self, savePath: str):
        with open(savePath, 'w', encoding = 'utf-8') as config:
            self.config.parser().write(config)

##############################################################################################################################

def Function_SetMethodExecutor(
    parentWindow: Optional[QWidget] = None,
    executeButton: Optional[QAbstractButton] = None,
    terminateButton: Optional[QAbstractButton] = None,
    progressBar: Optional[QProgressBar] = None,
    consoleWidget: Optional[QWidget] = None,
    method: object = ...,
    params: Optional[tuple] = None,
    paramsFrom: Optional[list[QObject]] = None,
    emptyAllowed: Optional[list[QObject]] = None,
    successEvents: Optional[list] = None
):
    '''
    Function to execute outer class methods
    '''
    QualName = str(method.__qualname__)
    MethodName = QualName.split('.')[1]

    ClassInstance = QFunc.getClassFromMethod(method)()
    ClassInstance.started.connect(lambda: FunctionSignals.Signal_TaskStatus.emit(QualName, 'Started')) if hasattr(ClassInstance, 'started') else None
    ClassInstance.errChk.connect(
        lambda Err: (
            QFunc.runEvents(successEvents) if Err == str(None) else None,
            MessageBoxBase.pop(parentWindow, QMessageBox.Warning, "Failure", "发生异常", Err) if Err != str(None) else None,
            FunctionSignals.Signal_TaskStatus.emit(QualName, 'Failed') if Err != str(None) else None
        )
    ) if hasattr(ClassInstance, 'errChk') else None
    ClassInstance.finished.connect(lambda: FunctionSignals.Signal_TaskStatus.emit(QualName, 'Finished')) if hasattr(ClassInstance, 'finished') else None

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
        Args = params#if params != () else None
        if paramsFrom not in ([], None):
            Args = Function_ParamsChecker(paramsFrom, emptyAllowed)
            if Args == "Abort":
                return print("Aborted.")
            else:
                pass #print("Continued.\n")

        FunctionSignals = CustomSignals_Functions()
        FunctionSignals.Signal_ExecuteTask.connect(getattr(ClassInstance, MethodName)) #FunctionSignals.Signal_ExecuteTask.connect(lambda Args: getattr(ClassInstance, MethodName)(*Args))

        WorkerThread.started.connect(lambda: Function_AnimateFrame(consoleWidget, minHeight = 0, maxHeight = 210, mode = "Extend")) if consoleWidget else None
        WorkerThread.started.connect(lambda: Function_AnimateProgressBar(progressBar, isTaskAlive = True)) if progressBar else None
        WorkerThread.started.connect(lambda: Function_AnimateStackedWidget(QFunc.findParentUI(executeButton, QStackedWidget), target = 1)) if terminateButton else None
        WorkerThread.finished.connect(lambda: Function_AnimateFrame(consoleWidget, minHeight = 0, maxHeight = 210, mode = "Reduce")) if consoleWidget else None
        WorkerThread.finished.connect(lambda: Function_AnimateProgressBar(progressBar, isTaskAlive = False)) if progressBar else None
        WorkerThread.finished.connect(lambda: Function_AnimateStackedWidget(QFunc.findParentUI(executeButton, QStackedWidget), target = 0)) if terminateButton else None
        #WorkerThread.finished.connect(lambda: FunctionSignals.Signal_ExecuteTask.disconnect(getattr(ClassInstance, MethodName)))

        FunctionSignals.Signal_ExecuteTask.emit(Args)

        WorkerThread.start()

    if executeButton is not None:
        executeButton.clicked.connect(ExecuteMethod)
    else:
        TempButton = QPushButton(parentWindow)
        TempButton.clicked.connect(ExecuteMethod)
        TempButton.setVisible(False)
        TempButton.click()
        WorkerThread.finished.connect(TempButton.deleteLater)

    @Slot()
    def TerminateMethod():
        '''
        Terminate the running thread
        '''
        ClassInstance.Terminate() if hasattr(ClassInstance, 'Terminate') else None

        WorkerThread.quit() if not WorkerThread.isFinished() else None

        FunctionSignals.Signal_TaskStatus.emit(QualName, 'Failed') if hasattr(ClassInstance, 'errChk') else None

        progressBar.setValue(0) if progressBar else None

    if terminateButton is not None:
        terminateButton.clicked.connect(
            lambda: MessageBoxBase.pop(parentWindow,
                messageType = QMessageBox.Question,
                windowTitle = "Ask",
                text = "当前任务仍在执行中，是否确认终止？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {QMessageBox.Yes: lambda: TerminateMethod()}
            )
        )
    else:
        pass

    FunctionSignals.Signal_ForceQuit.connect(TerminateMethod)

##############################################################################################################################

def Function_UpdateChecker(
    repoOwner: str,
    repoName: str,
    fileName: str,
    fileFormat: str,
    currentVersion: str = ...,
):
    '''
    '''
    try:
        FunctionSignals.Signal_UpdateMessage.emit("正在检查更新，请稍等...\nChecking for updates, please wait...")
        IsUpdateNeeded, DownloadURL, VersionInfo = QFunc.checkUpdateFromGithub(repoOwner, repoName, fileName, fileFormat, currentVersion)

    except:
        #FunctionSignals.Signal_Message.emit("更新检查失败！\nFailed to check for updates!")
        FunctionSignals.Signal_IsUpdateSucceeded.emit(False, "更新检查失败！\nFailed to check for updates!")

    else:
        if IsUpdateNeeded:
            FunctionSignals.Signal_ReadyToUpdate.emit(DownloadURL, VersionInfo)
        else:
            FunctionSignals.Signal_UpdateMessage.emit("已是最新版本！\nAlready up to date!")
            FunctionSignals.Signal_IsUpdateSucceeded.emit(False, "")

##############################################################################################################################