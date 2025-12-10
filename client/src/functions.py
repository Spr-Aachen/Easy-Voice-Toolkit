import os
import time
import json
import PyEasyUtils as EasyUtils
from typing import Union, Optional
from PySide6.QtCore import Qt, QObject, Signal, QThreadPool, QPoint
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *
from QEasyWidgets import QFunctions as QFunc, QWorker
from QEasyWidgets.Components import *
from QEasyWidgets.Windows import *

from components import *

##############################################################################################################################

class FunctionSignals(QObject):
    '''
    Set up signals for functions
    '''
    updateMessage = Signal(str)
    isUpdateSucceeded = Signal(bool, str)
    readyToUpdate = Signal(str, str)

    serverStarted = Signal()
    serverEnded = Signal()

    taskStatus = Signal(str, str)
    tasksEnded = Signal()

    forceQuit = Signal()


functionSignals = FunctionSignals()

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
        scrollArea = QFunc.findParent(targetWidget, QScrollArea)

    def _scrollToWidget():
        TargetRect = targetWidget.mapToGlobal(QPoint(0, 0))
        TargetYPos = TargetRect.y() - scrollArea.widget().mapToGlobal(QPoint(0, 0)).y()

        scrollArea.verticalScrollBar().setValue(TargetYPos)

    if isinstance(trigger, QTreeWidgetItem):
        def _treeWidgetEvent(Item, Column):
            _scrollToWidget() if Item == trigger else None
        trigger.treeWidget().itemClicked.connect(_treeWidgetEvent)

    if isinstance(trigger, QAbstractButton):
        trigger.clicked.connect(_scrollToWidget)


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

##############################################################################################################################

def Function_ConfigureCheckBox(
    checkBox: QCheckBox,
    checkedText: Optional[str] = None,
    checkedEvents: dict = {},
    uncheckedText: Optional[str] = None,
    uncheckedEvents: dict = {},
):
    '''
    Function to configure checkbox
    '''
    if checkedText is not None:
        checkedEvents[lambda: checkBox.setText(checkedText)] = True
    if uncheckedText is not None:
        uncheckedEvents[lambda: checkBox.setText(uncheckedText)] = True

    checkBox.toggled.connect(
        lambda isChecked: EasyUtils.runEvents(checkedEvents.keys() if isChecked else uncheckedEvents.keys())
    )

    EasyUtils.runEvents([event for event, takeEffect in (checkedEvents if checkBox.isChecked() else uncheckedEvents).items() if takeEffect])


def Function_ConfigureComboBox(
    comboBox: QComboBox,
    textChangedEvents: dict = {},
    takeEffect = False
):
    '''
    Function to configure checkbox
    '''
    comboBox.currentTextChanged.connect(
        lambda text: EasyUtils.runEvents(EasyUtils.toIterable(textChangedEvents[text]))
    )

    EasyUtils.runEvents(EasyUtils.toIterable(textChangedEvents[comboBox.currentText()])) if takeEffect else None

##############################################################################################################################

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
    else:
        progressBar.setRange(minValue, maxValue)
        progressBar.setValue(maxValue)


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
    WidgetAnimation.start()


def Function_AnimateFrame(
    frame: QWidget,
    minWidth: Optional[int] = None,
    maxWidth: Optional[int] = None,
    minHeight: Optional[int] = None,
    maxHeight: Optional[int] = None,
    duration: int = 210,
    mode: str = "Toggle",
):
    '''
    Function to animate frame
    '''
    def ExtendFrame():
        QFunc.setWidgetSizeAnimation(frame, maxWidth, None, duration).start() if maxWidth not in (None, frame.width()) else None
        QFunc.setWidgetSizeAnimation(frame, None, maxHeight, duration).start() if maxHeight not in (None, frame.height()) else None

    def ReduceFrame():
        QFunc.setWidgetSizeAnimation(frame, minWidth, None, duration).start() if minWidth not in (None, frame.width()) else None
        QFunc.setWidgetSizeAnimation(frame, None, minHeight, duration).start() if minHeight not in (None, frame.height()) else None

    if mode == "Extend":
        ExtendFrame()
    if mode == "Reduce":
        ReduceFrame()
    if mode == "Toggle":
        ExtendFrame() if frame.width() == minWidth or frame.height() == minHeight else ReduceFrame()


def Function_SetWidgetsVisibility(
    widgetsVisibility: dict,
):
    '''
    Function to set the visibility of widgets
    '''
    for widget, visibility in widgetsVisibility.items():
        if widget is None:
            continue
        animation = QFunc.setWidgetSizeAnimation(
            widget,
            targetHeight = widget.sizeHint().height() if visibility is True else 0,
            duration = 210
        )
        animation.finished.connect(lambda: widget.setVisible(visibility))
        animation.start()

##############################################################################################################################

def Function_SetWidgetValue(
    widget: QWidget,
    config: EasyUtils.configManager,
    section: str = ...,
    option: str = ...,
    value = ...,
    times: Union[int, float] = 1,
    setPlaceholderText: bool = False,
    placeholderText: Optional[str] = None
):
    fixDict = {'Enabled': True, 'Disabled': False}
    value = fixDict.get(value, value)

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
            widget.valueChanged.connect(EditConfig)
            EditConfig(value)


class ParamsManager:
    def __init__(self,
        configPath: str,
    ):
        self.configPath = configPath
        self.config = EasyUtils.configManager(configPath)

        self.RegistratedWidgets = {}

    def registrate(self, widget: QWidget, value: tuple):
        self.RegistratedWidgets[widget] = value

    def setParam(self,
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

    def resetParam(self, widget: QWidget):
        value = self.RegistratedWidgets[widget]
        Function_SetWidgetValue(widget, self.config, *value)

    def clearSettings(self):
        with open(self.configPath, 'w'):
            pass
        self.config = EasyUtils.configManager(self.configPath)

    def resetSettings(self):
        self.clearSettings()
        for widget in list(self.RegistratedWidgets.keys()):
            self.resetParam(widget)

    def importSettings(self, readPath: str):
        configParser = EasyUtils.configManager(readPath).parser()
        with open(self.configPath, 'w', encoding = 'utf-8') as config:
            configParser.write(config)
        for widget, value in list(self.RegistratedWidgets.items()):
            self.setParam(widget, *value)

    def exportSettings(self, savePath: str):
        with open(savePath, 'w', encoding = 'utf-8') as config:
            self.config.parser().write(config)

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
    if isinstance(ui, (QAbstractSpinBox, QSlider)):
        return ui.value()
    if isinstance(ui, (QCheckBox, QRadioButton)):
        return ui.isChecked()

    if isinstance(ui, Frame_RangeSetting):
        return ui.value()
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
    if isinstance(ui, (QAbstractSpinBox, QSlider)):
        ui.setValue(param)
    if isinstance(ui, (QCheckBox, QRadioButton)):
        ui.setChecked(param)

    if isinstance(ui, Frame_RangeSetting):
        ui.setValue(param)
    if isinstance(ui, Table_EditAudioSpeaker):
        ui.setValue(param)


def Function_ParamsSynchronizer(
    trigger: Union[QObject, list],
    fromTo: dict = {},
    times: Union[int, float] = 1,
    connection: str = "Connect"
):
    '''
    Function to synchronize params (paramTargets.value * times = ParamsTo.value)
    '''
    def _paramsSynchronizer():
        for UI_Get, UI_Set in fromTo.items():
            Param_Get = Function_GetParam(UI_Get)
            Param_Get = Param_Get * times if isinstance(Param_Get, (int, float, complex)) else Param_Get
            for UI_Set in EasyUtils.toIterable(UI_Set):
                Function_SetParam(UI_Set, Param_Get)

    TriggerList = EasyUtils.toIterable(trigger)

    for trigger in TriggerList:
        if isinstance(trigger, QAbstractButton):
            trigger.clicked.connect(_paramsSynchronizer) if connection == "Connect" else trigger.clicked.disconnect(_paramsSynchronizer)
        if isinstance(trigger, QAbstractSlider):
            trigger.sliderMoved.connect(_paramsSynchronizer) if connection == "Connect" else trigger.sliderMoved.disconnect(_paramsSynchronizer)
        if isinstance(trigger, QAbstractSpinBox):
            trigger.valueChanged.connect(_paramsSynchronizer) if connection == "Connect" else trigger.valueChanged.disconnect(_paramsSynchronizer)
        if isinstance(trigger, (QLineEdit)):
            trigger.textChanged.connect(_paramsSynchronizer) if connection == "Connect" else trigger.textChanged.disconnect(_paramsSynchronizer)


def Function_ParamsChecker(
    paramTarget: object,
    emptyAllowed: bool
):
    '''
    Function to return handled param
    '''
    param = Function_GetParam(paramTarget) if isinstance(paramTarget, QWidget) else paramTarget
    if isinstance(param, str):
        if param.strip() == "None" or param.strip() == "":
            if emptyAllowed:
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
            if emptyAllowed:
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

    return param

##############################################################################################################################

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
        lambda: QFunc.openURL([(Function_GetParam(url) if isinstance(url, QWidget) else url) for url in EasyUtils.toIterable(url)], createIfNotExist)
    )
    button.setToolTipDuration(-1)
    button.setToolTip(buttonTooltip)

##############################################################################################################################

class TaskStatus:
    Started = 'Started'
    Finished = 'Finished'
    Failed = 'Failed'
    Succeeded = 'Succeeded'


areTasksEnded: bool = True

def _updateAreTasksEnded(val):
    global areTasksEnded
    areTasksEnded = val

functionSignals.taskStatus.connect(lambda executeMethodName, taskStatus: _updateAreTasksEnded(False) if taskStatus == TaskStatus.Started else None)
functionSignals.tasksEnded.connect(lambda: _updateAreTasksEnded(True))


forceQuit: bool = False

def _updateForceQuit(val):
    global forceQuit
    forceQuit = val

functionSignals.forceQuit.connect(lambda: _updateForceQuit(True))


class WorkerManager(QWorker.WorkerManager):
    tasks: dict = {}
    endAllTasks: bool = False

    def __init__(self,
        executeMethod: object = ...,
        executeParams: Optional[dict] = None,
        terminateMethod: Optional[object] = None,
        autoDelete: bool = True,
        threadPool: Optional[QThreadPool] = None,
    ):
        super().__init__(executeMethod, terminateMethod, autoDelete, threadPool)

        self.executeMethodName = executeMethod.__qualname__
        self.executeParams = executeParams

        self.signals = QWorker.WorkerSignals()
        self.worker.signals.started.connect(self.signals.started.emit)
        self.worker.signals.error.connect(self.signals.error.emit)
        self.worker.signals.result.connect(self.signals.result.emit)
        self.worker.signals.finished.connect(self.signals.finished.emit)
        self.signals.started.connect(
            lambda: functionSignals.taskStatus.emit(self.executeMethodName, TaskStatus.Started)
        )
        self.signals.error.connect(
            lambda: functionSignals.taskStatus.emit(self.executeMethodName, TaskStatus.Failed)
        )
        self.signals.finished.connect(
            lambda: functionSignals.taskStatus.emit(self.executeMethodName, TaskStatus.Finished)
        )

        functionSignals.forceQuit.connect(self.terminateAll)

    def _validateParams(self, unvalidatedParams):
        validatedParams = []
        if unvalidatedParams is not None:
            unvalidatedParams = [(unvalidatedParam, unvalidatedParams[unvalidatedParam] if isinstance(unvalidatedParams, dict) else True) for unvalidatedParam in EasyUtils.toIterable(unvalidatedParams)]
            for paramTarget, emptyAllowed in unvalidatedParams:
                param = Function_ParamsChecker(paramTarget, emptyAllowed)
                if param == "Abort":
                    return print("Aborted.")
                else:
                    pass #print("Continued.\n")
                validatedParams.append(param)
        return validatedParams

    def execute(self):
        super().execute(*self._validateParams(self.executeParams))
        self.tasks.update({self: TaskStatus.Started})

    def terminate(self):
        super().terminate()
        self.tasks.update({self: TaskStatus.Failed})
        functionSignals.taskStatus.emit(self.executeMethodName, TaskStatus.Failed)

    def terminateAll(self):
        self.endAllTasks = True
        self.terminate()
        functionSignals.tasksEnded.emit() if not TaskStatus.Started in self.tasks.values() else None


def Function_SetMethodExecutor(
    executeMethod: object = ...,
    executeParams: Optional[dict] = None,
    executeButton: Optional[QAbstractButton] = None,
    terminateMethod: Optional[object] = None,
    terminateButton: Optional[QAbstractButton] = None,
    progressBar: Optional[QProgressBar] = None,
    consoleWidget: Optional[QWidget] = None,
    resultReciever: Optional[object] = None,
    finishedEvents: Optional[dict] = None,
    autoDelete: bool = True,
    threadPool: Optional[QThreadPool] = None,
    parentWindow: Optional[QWidget] = None,
):
    '''
    '''
    workerManager = WorkerManager(executeMethod, executeParams, terminateMethod, autoDelete, threadPool)

    isErrorOccurred = False
    def _setErrorOccuredFlag():
        global isErrorOccurred
        isErrorOccurred = True

    workerManager.signals.started.connect(
        lambda: (
            Function_AnimateFrame(consoleWidget, minHeight = 0, maxHeight = 210, mode = "Extend") if consoleWidget else None,
            Function_AnimateProgressBar(progressBar, isTaskAlive = True) if progressBar else None,
            Function_AnimateStackedWidget(QFunc.findParent(executeButton, QStackedWidget), target = 1) if terminateButton else None,
        )
    )
    workerManager.signals.result.connect(
        lambda: resultReciever() if callable(resultReciever) and not workerManager.endAllTasks else None
    )
    workerManager.signals.error.connect(
        lambda err: (
            _setErrorOccuredFlag(),
            MessageBoxBase.pop(parentWindow, QMessageBox.Warning, "Failure", "Exception occurred:(\n发生异常", str(err)),
            EasyUtils.runEvents([event for event, status in finishedEvents.items() if status == TaskStatus.Failed]) if finishedEvents is not None else None,
        ) if not workerManager.endAllTasks else None
    )
    workerManager.signals.finished.connect(
        lambda: (
            Function_AnimateStackedWidget(QFunc.findParent(executeButton, QStackedWidget), target = 0) if terminateButton else None,
            Function_AnimateProgressBar(progressBar, isTaskAlive = False) if progressBar else None,
            Function_AnimateFrame(consoleWidget, minHeight = 0, maxHeight = 210, mode = "Reduce") if consoleWidget else None,
            EasyUtils.runEvents([event for event, status in finishedEvents.items() if (not isErrorOccurred and status == TaskStatus.Succeeded) or TaskStatus.Finished]) if finishedEvents is not None else None,
        ) if not workerManager.endAllTasks else None
    )

    # Execution
    if executeButton is not None:
        executeButton.clicked.connect(workerManager.execute)
    else:
        tempButton = QPushButton(parentWindow)
        tempButton.clicked.connect(workerManager.execute)
        tempButton.setVisible(False)
        tempButton.click()
        workerManager.signals.finished.connect(tempButton.deleteLater)

    # Termination
    if terminateButton is not None:
        terminateButton.clicked.connect(
            lambda: MessageBoxBase.pop(parentWindow,
                messageType = QMessageBox.Question,
                windowTitle = "Ask",
                text = "The task is still running, do you wish to abort it?\n当前任务仍在执行中，是否确认终止？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {QMessageBox.Yes: workerManager.terminate}
            )
        )
    else:
        pass

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
        functionSignals.updateMessage.emit("正在检查更新，请稍等...\nChecking for updates, please wait...")
        IsUpdateNeeded, DownloadURL, VersionInfo = EasyUtils.checkUpdateFromGithub(repoOwner, repoName, fileName, fileFormat, currentVersion)

    except:
        #functionSignals.Signal_Message.emit("更新检查失败！\nFailed to check for updates!")
        functionSignals.isUpdateSucceeded.emit(False, "更新检查失败！\nFailed to check for updates!")

    else:
        if IsUpdateNeeded:
            functionSignals.readyToUpdate.emit(DownloadURL, VersionInfo)
        else:
            functionSignals.isUpdateSucceeded.emit(False, "已是最新版本！\nAlready up to date!")


def Function_RunTensorboard(logDir, maximumWaitTime = 30, port = 6007):
    """
    Function to run tensorboard
    """
    initialWaitTime = 0
    while EasyUtils.getPaths(logDir, 'events.out.tfevents') == None:
        time.sleep(1)
        initialWaitTime += 1
        if initialWaitTime >= maximumWaitTime:
            break
    spm = EasyUtils.subprocessManager(shell = True)
    spm.create(f'python -m tensorboard.main --logdir={logDir} --port={port}', env = os.environ)
    for outputLine, errorLine in spm.monitor():
        if f":{port}" in outputLine.decode(errors = 'ignore'):
            break
    QFunc.openURL(f'http://localhost:{port}/')

##############################################################################################################################

isServerEnded: bool = True

def _updateIsServerEnded(val):
    global isServerEnded
    isServerEnded = val

functionSignals.serverStarted.connect(lambda: _updateIsServerEnded(False))
functionSignals.serverEnded.connect(lambda: _updateIsServerEnded(True))


host = None
port = None
logPath = None

def getHostPort():
    return host, port

def getLogPath():
    return logPath

def startServer(
    filePath: str,
    logOutputPath: str
):
    global host, port, logPath
    host = "localhost"
    port = EasyUtils.findAvailablePorts((8000, 8080), host)[0]
    logPath = logOutputPath
    args = EasyUtils.mkPyFileCommand(
        filePath,
        host = host,
        port = port,
    )
    spm = EasyUtils.subprocessManager(shell = False)
    functionSignals.forceQuit.connect(
        lambda: (
            EasyUtils.terminateProcess(spm.subprocesses[-1].pid),
            functionSignals.serverEnded.emit()
        )
    )
    spm.create(args, env = os.environ)
    subprocessMonitor = spm.monitor(logPath = logOutputPath)
    for outputLine, errorLine in subprocessMonitor:
        if f"{host}:{port}" in outputLine.decode(errors = 'ignore'):
            functionSignals.serverStarted.emit()


def sendRequest(
    reqMethod: EasyUtils.requestManager,
    protocol: str,
    host: str,
    port: int,
    pathParams: Union[str, list[str], None] = None,
    queryParams: Union[str, list[str], None] = None,
    stream: bool = False,
    **reqParams,
):
    for parsed_content, status_code in reqMethod.response(protocol, host, port, pathParams, queryParams, None, json.dumps(reqParams), stream):
        yield parsed_content, status_code

##############################################################################################################################