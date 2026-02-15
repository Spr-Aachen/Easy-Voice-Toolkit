import os
import sys
import argparse
import subprocess
import PyEasyUtils as EasyUtils
from pathlib import Path
from datetime import date
from PySide6 import __file__ as PySide6_File
from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtCore import QThreadPool, QTimer
from PySide6.QtGui import QColor, QPixmap, QIcon, QTextCursor
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets import QTasks
from QEasyWidgets import componentsSignals, Theme, currentTheme, Language, currentLanguage, updateLanguage, IconBase
from QEasyWidgets.Windows import MessageBoxBase

from pages import *
from windows import *
from functions import *
from envConfigurator import *
from modelsManager import *
from toolsManager import *
from config import *

##############################################################################################################################

# Get current path
currentPath = EasyUtils.getCurrentPath()

# Get current directory
currentDir = Path(currentPath).parent.as_posix()

# Set path to store log
logPath = EasyUtils.normPath(Path(currentDir).joinpath('log.txt'))

# Set directory to load static dependencies
resourceDir = EasyUtils.getBaseDir(searchMEIPASS = True) or currentDir

# Check whether python file is compiled
_, isFileCompiled = EasyUtils.getFileInfo()

# Get current version (assume resourceDir is the name of current version after being compiled)
currentVersion = Path(resourceDir).name if isFileCompiled else 'beta version'

##############################################################################################################################

# Change working directory to current directory
os.chdir(currentDir)


# Parse path settings
parser = argparse.ArgumentParser()
parser.add_argument("--updater",           help = "path to updater",          default = EasyUtils.normPath(Path(resourceDir).joinpath('updater.exe') if isFileCompiled else Path(currentDir).joinpath('updater.py')))
parser.add_argument("--server",            help = "path to server file",      default = EasyUtils.normPath(Path(resourceDir).joinpath('server.exe') if isFileCompiled else Path(resourceDir).joinpath('server', 'app', 'main.py')))
parser.add_argument("--manifest",          help = "path to manifest.json",    default = EasyUtils.normPath(Path(resourceDir).joinpath('manifest.json')))
parser.add_argument("--requirements",      help = "path to requirements.txt", default = EasyUtils.normPath(Path(resourceDir).joinpath('requirements.txt')))
parser.add_argument("--dependencies",      help = "dir of dependencies",      default = EasyUtils.normPath(Path(currentDir).joinpath('')))
parser.add_argument("--models",            help = "dir of models",            default = EasyUtils.normPath(Path(currentDir).joinpath('Models')))
parser.add_argument("--output",            help = "dir of output",            default = EasyUtils.normPath(Path(currentDir).joinpath('')))
parser.add_argument("--profile",           help = "dir of profile",           default = EasyUtils.normPath(Path(currentDir).joinpath('')))
parser.add_argument("--deprecatedVersion", help = "deprecated version",       default = None)
args = parser.parse_known_args()[0]

updaterPath = args.updater
serverPath = args.server
manifestPath = args.manifest
requirementsPath = args.requirements
dependencyDir = args.dependencies
modelDir = args.models
outputDir = args.output
profileDir = args.profile
deprecatedVersion = args.deprecatedVersion


# Set up client config
configDir = EasyUtils.normPath(Path(profileDir).joinpath('config'))
configPath = EasyUtils.normPath(Path(configDir).joinpath('config.ini'))
config = EasyUtils.configManager(configPath)


# Set up environment variables while python file is not compiled
if isFileCompiled == False:
    EasyUtils.setEnvVar( # Redirect PATH variable 'QT_QPA_PLATFORM_PLUGIN_PATH' to Pyside6 '/plugins/platforms' folder's path
        variable = 'QT_QPA_PLATFORM_PLUGIN_PATH',
        value = EasyUtils.normPath(Path(EasyUtils.getBaseDir(PySide6_File)).joinpath('plugins', 'platforms'))
    )
# Set up environment variables while environment is configured
if Path(dependencyDir).joinpath('Aria2').exists():
    EasyUtils.setEnvVar(
        variable = 'PATH',
        value = EasyUtils.normPath(Path(dependencyDir).joinpath('Aria2'))
    )
if Path(dependencyDir).joinpath('FFmpeg').exists():
    EasyUtils.setEnvVar(
        variable = 'PATH',
        value = EasyUtils.normPath(Path(dependencyDir).joinpath('FFmpeg', 'bin'))
    )
if Path(dependencyDir).joinpath('Python').exists():
    EasyUtils.setEnvVar(
        variable = 'PATH',
        value = EasyUtils.normPath(Path(dependencyDir).joinpath('Python'), trailingSlash = True)
    )
    EasyUtils.setEnvVar(
        variable = 'PATH',
        value = EasyUtils.normPath(Path(dependencyDir).joinpath('Python', 'Scripts'), trailingSlash = True)
    )

##############################################################################################################################

# Show GUI
class MainWindow(Window_MainWindow):
    """
    Show the user interface
    """
    mainWindowShown = Signal()

    modelView_process_uvr = Signal(list)
    modelView_vpr_tdnn = Signal(list)
    modelView_asr_whisper = Signal(list)
    modelView_tts_gptsovits = Signal(list)

    def __init__(self):
        super().__init__()

        self.threadPool = QThreadPool.globalInstance()
        self.threadPool_env = QThreadPool()
        self.threadPool_models = QThreadPool()
        self.threadPool_tasks = QThreadPool()

        self.MonitorUsage = QTasks.MonitorUsage()
        self.MonitorUsage.start()

        self.task_audioProcessor = Tool_AudioProcessor()
        self.task_vpr = Tool_VPR()
        self.task_whisper = Tool_Whisper()
        self.task_gptsovits = Tool_GPTSoVITS()

    def closeEvent(self, event):
        def _endEvent():
            QApplication.instance().exit() if areTasksEnded and isServerEnded else None
        functionSignals.tasksEnded.connect(_endEvent)
        functionSignals.serverEnded.connect(_endEvent)
        functionSignals.forceQuit.emit()

    def showGuidance(self, windowTitle: str, htmlPaths: list):
        stackedMsgBox = MessageBox_Stacked(self)
        stackedMsgBox.setWindowTitle(windowTitle)
        stackedMsgBox.setContent(htmlPaths)
        stackedMsgBox.exec()

    def _getFileDialog(self, widget, **kwargs):
        text = QFunc.getFileDialog(**kwargs)
        Function_SetParam(widget, text) if text != '' else None

    def viewModels(self):
        worker_modelView_process_uvr = WorkerManager(
            executeMethod = getModelsInfo,
            executeParams = (
                manifestPath,
                EasyUtils.normPath(Path(modelDir).joinpath('Process', 'UVR')),
                ['pth', 'onnx']
            ),
            threadPool = self.threadPool_models,
        )
        worker_modelView_process_uvr.signals.result.connect(self.modelView_process_uvr.emit)
        worker_modelView_process_uvr.execute()

        worker_modelView_vpr_tdnn = WorkerManager(
            executeMethod = getModelsInfo,
            executeParams = (
                manifestPath,
                EasyUtils.normPath(Path(modelDir).joinpath('VPR', 'TDNN')),
                ['pth']
            ),
            threadPool = self.threadPool_models,
        )
        worker_modelView_vpr_tdnn.signals.result.connect(self.modelView_vpr_tdnn.emit)
        worker_modelView_vpr_tdnn.execute()

        worker_modelView_asr_whisper = WorkerManager(
            executeMethod = getModelsInfo,
            executeParams = (
                manifestPath,
                EasyUtils.normPath(Path(modelDir).joinpath('ASR', 'Whisper')),
                ['pt']
            ),
            threadPool = self.threadPool_models,
        )
        worker_modelView_asr_whisper.signals.result.connect(self.modelView_asr_whisper.emit)
        worker_modelView_asr_whisper.execute()

        worker_modelView_tts_gptsovits = WorkerManager(
            executeMethod = getModelsInfo,
            executeParams = (
                manifestPath,
                EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS')),
                ['pth', 'ckpt', 'bin', 'json']
            ),
            threadPool = self.threadPool_models,
        )
        worker_modelView_tts_gptsovits.signals.result.connect(self.modelView_tts_gptsovits.emit)
        worker_modelView_tts_gptsovits.execute()

    def appendModels(self):
        LineEdit_Models_Append = QLineEdit()
        DialogBox_Models_Append = MessageBox_Buttons(self)
        DialogBox_Models_Append.setText(self.tr("请选择添加方式"))
        DialogBox_Models_Append.Button1.setText(self.tr("模型文件目录（多文件）"))
        DialogBox_Models_Append.Button1.clicked.connect(
            lambda: (
                self._getFileDialog(
                    LineEdit_Models_Append,
                    mode = FileDialogMode.SelectFolder
                ),
                DialogBox_Models_Append.close(),
            )
        )
        DialogBox_Models_Append.Button2.setText(self.tr("模型文件路径（单文件）"))
        DialogBox_Models_Append.Button2.clicked.connect(
            lambda: (
                self._getFileDialog(
                    LineEdit_Models_Append,
                    mode = FileDialogMode.SelectFile,
                    fileType = "模型文件 (*.pt *.pth *.ckpt *.bin *.json')"
                ),
                DialogBox_Models_Append.close(),
            )
        )
        DialogBox_Models_Append.exec()
        modelPath = LineEdit_Models_Append.text()
        if EasyUtils.normPath(modelPath) is None:
            return
        ToolIndexList = ['Process', 'VPR', 'ASR', 'TTS']
        ToolIndex = self.ui.StackedWidget_Pages_Models.currentIndex()
        TabWidget = QFunc.findChild(self.ui.StackedWidget_Pages_Models.currentWidget(), QTabWidget)
        TypeIndex = TabWidget.currentIndex()
        sector = [
            ToolIndexList[ToolIndex],
            TabWidget.tabText(TypeIndex).rsplit('（')[0],
        ]
        addLocalModel(modelDir, modelPath, sector)
        self.ui.Button_Models_Refresh.click()

    def setDirAlert(self, dirNameEdit: LineEditBase, rootEdit: LineEditBase, dirEdit: QLineEdit):
        def SetText_Dir():
            DirName = dirNameEdit.text()
            if len(DirName.strip()) == 0:
                alert = False
            else:
                DirText = Path(rootEdit.text()).joinpath(DirName).as_posix()
                alert = Path(DirText).exists() and list(Path(DirText).iterdir()) != []
                dirEdit.setText(DirText)
            dirNameEdit.alert(True if alert else False, "注意：目录已包含文件")
        dirNameEdit.interacted.connect(SetText_Dir)
        rootEdit.interacted.connect(SetText_Dir)

    def setPathAlert(self, fileNameEdit: LineEditBase, dirEdit: LineEditBase, suffix: str, fileEdit: QLineEdit):
        def SetText_File():
            fileName = fileNameEdit.text()
            if len(fileName.strip()) == 0:
                alert = False
            else:
                FileText = Path(dirEdit.text()).joinpath(fileName).as_posix() + suffix
                alert = Path(FileText).exists()
                fileEdit.setText(FileText)
            fileNameEdit.alert(True if alert else False, "注意：路径已存在")
        fileNameEdit.interacted.connect(SetText_File)
        dirEdit.interacted.connect(SetText_File)

    def setDirPathSelection(self, textReciever, dirSelectionText, pathSelectionText, fileType, directory):
        dirPathSelectionDialogBox = MessageBox_Buttons(self)
        dirPathSelectionDialogBox.setText(self.tr("请选择参数类型"))
        dirPathSelectionDialogBox.Button1.setText(pathSelectionText)
        dirPathSelectionDialogBox.Button1.clicked.connect(
            lambda: (
                self._getFileDialog(
                    textReciever,
                    mode = FileDialogMode.SelectFolder,
                ),
                dirPathSelectionDialogBox.close(),
            )
        )
        dirPathSelectionDialogBox.Button2.setText(dirSelectionText)
        dirPathSelectionDialogBox.Button2.clicked.connect(
            lambda: (
                self._getFileDialog(
                    textReciever,
                    mode = FileDialogMode.SelectFile,
                    fileType = fileType,
                    directory = directory
                ),
                dirPathSelectionDialogBox.close(),
            )
        )
        dirPathSelectionDialogBox.exec()

    def startServer(self):
        global isServerEnded, forceQuit
        if forceQuit or not isServerEnded:
            return
        WorkerManager(
            executeMethod = startServer,
            executeParams = (serverPath, logPath),
            autoDelete = True,
            threadPool = self.threadPool_tasks,
        ).execute()
        isServerEnded = False

    def showVPRResult(self, audioSaveDir, audioSpeakersData_path, comboItems):
        ChildWindow_VPR = Window_ChildWindow_VPR(self)

        ChildWindow_VPR.ui.Button_Close.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = self.tr("确认放弃编辑？"),
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
            text = EasyUtils.setRichText(
                self.tr("语音识别结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_VPR.ui.Label_Text,
            text = EasyUtils.setRichText(
                self.tr("这里记录了每个语音文件与其对应的人物名（留空表示无匹配人物且最终不会被保留）\n你可以对这些人物名进行更改并在表格下方设置音频的保存路径")
            )
        )

        ChildWindow_VPR.ui.CheckBox.setText(self.tr("结束编辑时将拥有匹配人物的音频保存到:"))
        ChildWindow_VPR.ui.CheckBox.setChecked(True)
        ChildWindow_VPR.ui.LineEdit.clearDefaultStyleSheet()
        ChildWindow_VPR.ui.LineEdit.setStyleSheet(ChildWindow_VPR.ui.LineEdit.styleSheet() + 'LineEditBase {border-width: 0px 0px 1px 0px; border-radius: 0px;}')
        ChildWindow_VPR.ui.LineEdit.setText(audioSaveDir)
        ChildWindow_VPR.ui.LineEdit.setReadOnly(True)

        ChildWindow_VPR.ui.Button_Cancel.setText(self.tr("取消"))
        ChildWindow_VPR.ui.Button_Cancel.clicked.connect(ChildWindow_VPR.ui.Button_Close.click)
        ChildWindow_VPR.ui.Button_Save.setText(self.tr("保存"))
        ChildWindow_VPR.ui.Button_Save.clicked.connect(
            lambda: (
                VPRResult_Save(
                    ChildWindow_VPR.ui.Table.getValue(),
                    audioSpeakersData_path,
                    False
                ),
                MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    self.tr("已保存当前结果。")
                )
            )
        )
        ChildWindow_VPR.ui.Button_Confirm.setText(self.tr("确认"))
        ChildWindow_VPR.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = self.tr("确认结束并应用编辑？"),
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        VPRResult_Save(
                            ChildWindow_VPR.ui.Table.getValue(),
                            audioSpeakersData_path,
                            ChildWindow_VPR.ui.CheckBox.isChecked(),
                            audioSaveDir
                        ),
                        ChildWindow_VPR.close()
                    )
                }
            )
        )

        ChildWindow_VPR.ui.Table.setValue(
            VPRResult_Get(audioSpeakersData_path),
            comboItems
        )
        ChildWindow_VPR.exec()

    def showASRResult(self, srtDir, audioDir):
        ChildWindow_ASR = Window_ChildWindow_ASR(self)

        ChildWindow_ASR.ui.Button_Close.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = self.tr("确认放弃编辑？"),
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
            text = EasyUtils.setRichText(
                self.tr("语音转录结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_ASR.ui.Label_Text,
            text = EasyUtils.setRichText(
                self.tr("这里记录了每个语音文件与其对应的字幕文本（包含了时间戳）\n你可以对这些文本进行更改，若启用了语种标注则小心不要误删")
            )
        )

        ChildWindow_ASR.ui.Button_Cancel.setText(self.tr("取消"))
        ChildWindow_ASR.ui.Button_Cancel.clicked.connect(ChildWindow_ASR.ui.Button_Close.click)
        ChildWindow_ASR.ui.Button_Confirm.setText(self.tr("确认"))
        ChildWindow_ASR.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = self.tr("确认结束并应用编辑？"),
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ASRResult_Save(
                            ChildWindow_ASR.ui.Table.getValue(),
                            srtDir
                        ),
                        ChildWindow_ASR.close()
                    )
                }
            )
        )

        ChildWindow_ASR.ui.Table.setValue(
            ASRResult_Get(srtDir, audioDir)
        )
        ChildWindow_ASR.exec()

    def showDATResult(self, datPath_training, datPath_validation):
        ChildWindow_DAT = Window_ChildWindow_DAT(self)

        ChildWindow_DAT.ui.Button_Close.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = self.tr("确认放弃编辑？"),
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
            text = EasyUtils.setRichText(
                self.tr("数据预处理结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_DAT.ui.Label_Text,
            text = EasyUtils.setRichText(
                self.tr("这里记录了每个语音文件与其对应的数据文本\n你可以对这些文本进行更改")
            )
        )

        ChildWindow_DAT.ui.Button_Cancel.setText(self.tr("取消"))
        ChildWindow_DAT.ui.Button_Cancel.clicked.connect(ChildWindow_DAT.ui.Button_Close.click)
        ChildWindow_DAT.ui.Button_Confirm.setText(self.tr("确认"))
        ChildWindow_DAT.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = self.tr("确认结束并应用编辑？"),
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        DATResult_Save(
                            ChildWindow_DAT.ui.Table_Train.getValue(),
                            datPath_training
                        ),
                        DATResult_Save(
                            ChildWindow_DAT.ui.Table_Val.getValue(),
                            datPath_validation
                        ) if datPath_validation is not None else None,
                        ChildWindow_DAT.close()
                    )
                }
            )
        )

        ChildWindow_DAT.ui.Table_Train.setValue(
            DATResult_Get(datPath_training)
        )
        ChildWindow_DAT.ui.Table_Val.setValue(
            DATResult_Get(datPath_validation)
        ) if datPath_validation is not None else None
        ChildWindow_DAT.exec()

    def showTTSResult(self, mediaPath):
        ChildWindow_TTS = Window_ChildWindow_TTS(self)

        ChildWindow_TTS.ui.Button_Close.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = self.tr("确认退出试听？"),
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS.ui.Widget.releaseMediaPlayer(),
                        ChildWindow_TTS.close()
                    )
                } 
            )
        )
        ChildWindow_TTS.ui.Button_Maximize.clicked.connect(lambda: ChildWindow_TTS.showNormal() if ChildWindow_TTS.isMaximized() else ChildWindow_TTS.showMaximized())

        QFunc.setText(
            widget = ChildWindow_TTS.ui.Label_Title,
            text = EasyUtils.setRichText(
                self.tr("语音合成结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_TTS.ui.Label_Text,
            text = EasyUtils.setRichText(
                self.tr("点击播放按钮以试听合成语音")
            )
        )

        ChildWindow_TTS.ui.Button_Cancel.setText(self.tr("丢弃"))
        ChildWindow_TTS.ui.Button_Cancel.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = self.tr("确认丢弃音频？"),
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS.ui.Widget.releaseMediaPlayer(),
                        os.remove(mediaPath),
                        ChildWindow_TTS.close()
                    )
                }
            )
        )
        ChildWindow_TTS.ui.Button_Confirm.setText(self.tr("保留"))
        ChildWindow_TTS.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = self.tr("确认保留音频？"),
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS.ui.Widget.releaseMediaPlayer(),
                        shutil.move(
                            mediaPath,
                            QFunc.getFileDialog(
                                mode = FileDialogMode.SaveFile,
                                fileType = "wav类型 (*.wav)"
                            )
                        ),
                        ChildWindow_TTS.close()
                    )
                }
            )
        )

        ChildWindow_TTS.ui.Widget.setMediaPlayer(
            mediaPath
        )
        ChildWindow_TTS.exec()

    def chkUpdate(self, runUpdateChecker: bool):
        recordedVersion = deprecatedVersion or config.getValue('Info', 'RecordedVersion', currentVersion)
        if not EasyUtils.isVersionSatisfied(recordedVersion, currentVersion):
            deprecatedDir = Path(resourceDir).parent.joinpath(recordedVersion).as_posix()
            try:
                EasyUtils.rmtree(deprecatedDir)
            except:
                pass
            else:
                config.editConfig('Info', 'RecordedVersion', currentVersion)

        functionSignals.readyToUpdate.connect(
            lambda downloadURL, versionInfo: (
                MessageBoxBase.pop(None,
                    QMessageBox.Question, "Ask",
                    text = "检测到可用的新版本，是否更新？\nNew version available, wanna update?",
                    detailedText = versionInfo,
                    buttons = QMessageBox.Yes|QMessageBox.No,
                    buttonEvents = {
                        QMessageBox.Yes: lambda: (
                            config.editConfig('Updater', 'Asked', 'True'),
                            subprocess.Popen(f'{"python" if isFileCompiled == False else ""} "{updaterPath}" --programPath "{currentPath}" --currentVersion {currentVersion} --downloadURL "{downloadURL}"', shell = True, env = os.environ),
                            QApplication.instance().exit(),
                            sys.exit(0) # In case the main event loop is not entered
                        ),
                        QMessageBox.No: lambda: (
                            config.editConfig('Updater', 'Asked', 'False'),
                        )
                    }
                )
            )
        )
        Function_SetMethodExecutor(
            executeMethod = Function_UpdateChecker,
            executeParams = (
                repoOwner,
                repoName,
                fileName,
                fileFormat,
                currentVersion
            ),
            threadPool = self.threadPool,
            parentWindow = self,
        ) if runUpdateChecker else None

    def main(self):
        '''
        Main funtion to orgnize all the subfunctions
        '''
        # Check for updates
        self.chkUpdate(config.getValue('Settings', 'AutoUpdate', 'Enabled') == 'Enabled') if isFileCompiled else None

        # Logo
        self.setWindowIcon(QIcon(EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/Logo.ico'))))

        #############################################################
        ########################## TitleBar #########################
        #############################################################

        # Theme toggler
        componentsSignals.setTheme.connect(
            lambda: self.ui.CheckBox_SwitchTheme.setChecked(
                {Theme.Light: True, Theme.Dark: False}.get(currentTheme())
            )
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_SwitchTheme,
            checkedText = "☀",
            checkedEvents = {
                lambda: config.editConfig('Settings', 'Theme', Theme.Light): False,
                lambda: componentsSignals.setTheme.emit(Theme.Light) if currentTheme() != Theme.Light else None : False
            },
            uncheckedText = "☼",
            uncheckedEvents = {
                lambda: config.editConfig('Settings', 'Theme', Theme.Dark) : False,
                lambda: componentsSignals.setTheme.emit(Theme.Dark) if currentTheme() != Theme.Dark else None : False
            }
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
        self.ui.Button_Toggle_Menu.setToolTip(self.tr("点击以展开/折叠菜单"))

        #############################################################
        ############################ Menu ###########################
        #############################################################

        self.ui.Button_Menu_Home.setText(self.tr("主页"))
        self.ui.Button_Menu_Home.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 0
            )
        )
        self.ui.Button_Menu_Home.setChecked(True)

        self.ui.Button_Menu_Env.setText(self.tr("环境"))
        self.ui.Button_Menu_Env.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 1
            )
        )
        self.ui.Button_Menu_Env.setChecked(False)

        self.ui.Button_Menu_Models.setText(self.tr("模型"))
        self.ui.Button_Menu_Models.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 2
            )
        )
        self.ui.Button_Menu_Models.setChecked(False)

        self.ui.Button_Menu_Process.setText(self.tr("处理"))
        self.ui.Button_Menu_Process.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 3
            )
        )
        self.ui.Button_Menu_Process.setChecked(False)

        self.ui.Button_Menu_VPR.setText(self.tr("识别"))
        self.ui.Button_Menu_VPR.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 4
            )
        )
        self.ui.Button_Menu_VPR.setChecked(False)

        self.ui.Button_Menu_ASR.setText(self.tr("转录"))
        self.ui.Button_Menu_ASR.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 5
            )
        )
        self.ui.Button_Menu_ASR.setChecked(False)

        self.ui.Button_Menu_Dataset.setText(self.tr("预处理"))
        self.ui.Button_Menu_Dataset.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 6
            )
        )
        self.ui.Button_Menu_Dataset.setChecked(False)

        self.ui.Button_Menu_Train.setText(self.tr("训练"))
        self.ui.Button_Menu_Train.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 7
            )
        )
        self.ui.Button_Menu_Train.setChecked(False)

        self.ui.Button_Menu_TTS.setText(self.tr("合成"))
        self.ui.Button_Menu_TTS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 8
            )
        )
        self.ui.Button_Menu_TTS.setChecked(False)

        self.ui.Button_Menu_Settings.setText(self.tr("设置"))
        self.ui.Button_Menu_Settings.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 9
            )
        )
        self.ui.Button_Menu_Settings.setChecked(False)

        self.ui.Button_Menu_Info.setText(self.tr("关于"))
        self.ui.Button_Menu_Info.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 10
            )
        )
        self.ui.Button_Menu_Info.setChecked(False)

        #############################################################
        ##################### Content: Settings #####################
        #############################################################

        '''Client'''
        # ParamsManager
        configPath_settings_client = config.configPath
        paramsManager_settings_client = ParamsManager(configPath_settings_client)
        # Subpage
        subSettingsPage_Client = SubSettingsPage(self.ui.Page_Settings, paramsManager_settings_client)
        themeDict = {
            self.tr("跟随系统"): Theme.Auto,
            self.tr("亮色"): Theme.Light,
            self.tr("暗色"): Theme.Dark
        }
        subSettingsPage_Client.addComboBoxFrame(
            rootItemText = self.tr("界面设置"),
            text = self.tr("主题"),
            items = themeDict.keys(),
            signal = componentsSignals.setTheme,
            textDict = themeDict,
            section = 'Settings',
            option = 'Theme',
        )
        languageDict = {
            self.tr("跟随系统"): Language.Auto,
            self.tr("中文"): Language.ZH,
            self.tr("英文"): Language.EN
        }
        subSettingsPage_Client.addComboBoxFrame(
            rootItemText = self.tr("界面设置"),
            text = self.tr("语言"),
            items = languageDict.keys(),
            signal = componentsSignals.setLanguage,
            textDict = languageDict,
            section = 'Settings',
            option = 'Language',
        )
        componentsSignals.setLanguage.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Information, "Tip",
                "Restart to fully refresh.\n该设置将在重启后完全生效"
            )
        )
        component_settings_autoUpdate = subSettingsPage_Client.addCheckBoxFrame(
            rootItemText = self.tr("功能设置"),
            text = self.tr("自动检查版本并更新"),
            section = 'Settings',
            option = 'AutoUpdate',
            defaultValue = True
        )
        Function_ConfigureCheckBox(
            checkBox = component_settings_autoUpdate.get(ComponentFlag.CheckBox),
            checkedEvents = {
            },
            uncheckedEvents = {
            },
        )
        self.ui.Page_Settings.addSubPage(
            self.tr("系统选项"), subSettingsPage_Client
        )

        '''Tools'''
        # ParamsManager
        configPath_settings_tools = config.configPath
        paramsManager_settings_tools = ParamsManager(configPath_settings_tools)
        # Subpage
        subSettingsPage_Tools = SubSettingsPage(self.ui.Page_Settings, paramsManager_settings_tools)
        component_settings_autoReset = subSettingsPage_Tools.addCheckBoxFrame(
            rootItemText = self.tr("功能设置"),
            text = self.tr("启动时重置所有工具的参数设置"),
            section = 'Settings',
            option = 'AutoReset',
            defaultValue = False
        )
        component_settings_autoCorrelate = subSettingsPage_Tools.addCheckBoxFrame(
            rootItemText = self.tr("功能设置"),
            text = self.tr("自动关联前后工具的部分参数设置"),
            section = 'Settings',
            option = 'AutoCorrelate',
            defaultValue = True
        )
        process_outputRoot_default = Path(outputDir).joinpath("音频处理结果" if currentLanguage() == Language.ZH else "Process Results").as_posix()
        component_process_outputRoot = subSettingsPage_Tools.addLineEditFrame(
            rootItemText = self.tr("路径设置"),
            text = self.tr("音频处理输出目录"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(process_outputRoot_default).parent),
            section = 'Output params',
            option = 'Process_OutputRoot',
            defaultValue = process_outputRoot_default,
            placeholderText = process_outputRoot_default
        )
        vpr_outputRoot_default = Path(outputDir).joinpath("声纹识别结果" if currentLanguage() == Language.ZH else "VPR Results")
        vpr_tdnn_audioSpeakersDataRoot_default = vpr_outputRoot_default.joinpath("TDNN").as_posix()
        component_vpr_tdnn_outputRoot = subSettingsPage_Tools.addLineEditFrame(
            rootItemText = self.tr("路径设置"),
            text = self.tr("TDNN识别结果输出目录"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(vpr_tdnn_audioSpeakersDataRoot_default).parent),
            section = 'Output params',
            option = 'VPR_TDNN_OutputRoot',
            defaultValue = vpr_tdnn_audioSpeakersDataRoot_default,
            placeholderText = vpr_tdnn_audioSpeakersDataRoot_default
        )
        asr_outputRoot_default = Path(outputDir).joinpath("语音转录结果" if currentLanguage() == Language.ZH else "ASR Results")
        asr_whisper_outputRoot_default = asr_outputRoot_default.joinpath("Whisper").as_posix()
        component_asr_whisper_outputRoot = subSettingsPage_Tools.addLineEditFrame(
            rootItemText = self.tr("路径设置"),
            text = self.tr("Whisper转录输出目录"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(asr_whisper_outputRoot_default).parent),
            section = 'Output params',
            option = 'ASR_Whisper_OutputRoot',
            defaultValue = asr_whisper_outputRoot_default,
            placeholderText = asr_whisper_outputRoot_default
        )
        dat_outputRoot_default = Path(outputDir).joinpath("数据预处理结果" if currentLanguage() == Language.ZH else "Preprocess Results")
        dat_gptsovits_outputRoot_default = dat_outputRoot_default.joinpath("GPT-SoVITS").as_posix()
        component_dat_gptsovits_outputRoot = subSettingsPage_Tools.addLineEditFrame(
            rootItemText = self.tr("路径设置"),
            text = self.tr("GPTSoVITS数据集输出目录"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(dat_gptsovits_outputRoot_default).parent),
            section = 'Output params',
            option = 'DAT_GPTSoVITS_OutputRoot',
            defaultValue = dat_gptsovits_outputRoot_default,
            placeholderText = dat_gptsovits_outputRoot_default
        )
        train_outputRoot_default = Path(outputDir).joinpath("模型训练结果" if currentLanguage() == Language.ZH else "Train Results")
        train_gptsovits_outputRoot_default = train_outputRoot_default.joinpath("GPT-SoVITS").as_posix()
        component_train_gptsovits_outputRoot = subSettingsPage_Tools.addLineEditFrame(
            rootItemText = self.tr("路径设置"),
            text = self.tr("GPTSoVITS训练输出目录"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(train_gptsovits_outputRoot_default).parent),
            section = 'Output params',
            option = 'Train_GPTSoVITS_OutputRoot',
            defaultValue = train_gptsovits_outputRoot_default,
            placeholderText = train_gptsovits_outputRoot_default
        )
        self.ui.Page_Settings.addSubPage(
            self.tr("工具选项"), subSettingsPage_Tools
        )

        #############################################################
        ####################### Content: Home #######################
        #############################################################

        self.ui.Label_Cover_Home.setPixmap(QPixmap(Path(resourceDir).joinpath('assets/images/others/Cover.png')))

        self.ui.TextBrowser_Text_Home.setFont(QFont("Microsoft YaHei", 12))
        self.ui.TextBrowser_Text_Home.loadMarkdown(Path(resourceDir).joinpath('assets/docs/intro_zh.md').as_posix() if currentLanguage() == Language.ZH else Path(resourceDir).joinpath('assets/docs/intro.md').as_posix())

        self.ui.Label_Demo_Text.setText(self.tr("视频演示"))
        Function_SetURL(
            button = self.ui.Button_Demo,
            url = "https://space.bilibili.com/359461611/lists/2668347" if currentLanguage() == Language.ZH else "https://www.youtube.com/playlist?list=PLzjq8Hx1SRV7zJ9cQvzwOU_4yOE65UfVW",
            buttonTooltip = "Click to view demo video"
        )
        self.ui.Label_Server_Text.setText(self.tr("云端版本"))
        Function_SetURL(
            button = self.ui.Button_Server,
            url = "https://colab.research.google.com/github/Spr-Aachen/EVT-Reassets/images/others/blob/main/Easy_Voice_Toolkit_for_Colab.ipynb",
            buttonTooltip = "Click to run on server"
        )
        self.ui.Label_Repo_Text.setText(self.tr("项目仓库"))
        Function_SetURL(
            button = self.ui.Button_Repo,
            url = "https://github.com/Spr-Aachen/Easy-Voice-Toolkit",
            buttonTooltip = "Click to view github repo"
        )
        self.ui.Label_Donate_Text.setText(self.tr("赞助作者"))
        Function_SetURL(
            button = self.ui.Button_Donate,
            url = "https://afdian.com/a/Spr_Aachen" if currentLanguage() == Language.ZH else "https://ko-fi.com/spr_aachen",
            buttonTooltip = "Click to buy author a coffee"
        )

        #############################################################
        ##################### Content: Environ ######################
        #############################################################

        '''EnvDetection'''
        # Subpage
        subEnvPage_detection = SubEnvPage_Detector(self.ui.Page_Env)
        subEnvPage_detection.addDetectorFrame(
            text = self.tr("Aria2"),
            toolTip = self.tr("重新检测安装"),
            detectMethod = Aria2_Installer.execute,
            terminateMethod = Aria2_Installer.terminate,
            threadPool = self.threadPool_env,
            signal_detect = self.mainWindowShown,
            signal_detected = envConfiguratorSignals.aria2Detected,
            signal_undetected = envConfiguratorSignals.aria2Undetected,
            statusSignal = envConfiguratorSignals.aria2Status,
        )
        envConfiguratorSignals.aria2Installed.connect(#self.ui.Button_Install_Aria2.click)
            lambda: envConfiguratorSignals.aria2Detected.emit()
        )
        envConfiguratorSignals.aria2InstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = self.tr("安装Aria2出错"),
                detailedText = str(Exception)
            )
        )
        subEnvPage_detection.addDetectorFrame(
            text = self.tr("FFmpeg"),
            toolTip = self.tr("重新检测安装"),
            detectMethod = FFmpeg_Installer.execute,
            terminateMethod = FFmpeg_Installer.terminate,
            threadPool = self.threadPool_env,
            signal_detect = self.mainWindowShown,
            signal_detected = envConfiguratorSignals.ffmpegDetected,
            signal_undetected = envConfiguratorSignals.ffmpegUndetected,
            statusSignal = envConfiguratorSignals.ffmpegStatus,
        )
        envConfiguratorSignals.ffmpegInstalled.connect(#self.ui.Button_Install_FFmpeg.click)
            lambda: envConfiguratorSignals.ffmpegDetected.emit()
        )
        envConfiguratorSignals.ffmpegInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = self.tr("安装FFmpeg出错"),
                detailedText = str(Exception)
            )
        )
        subEnvPage_detection.addDetectorFrame(
            text = self.tr("Python"),
            toolTip = self.tr("重新检测安装"),
            detectMethod = Python_Installer.execute,
            params = ('3.9.0'),
            terminateMethod = Python_Installer.terminate,
            threadPool = self.threadPool_env,
            signal_detect = self.mainWindowShown,
            signal_detected = envConfiguratorSignals.pythonDetected,
            signal_undetected = envConfiguratorSignals.pythonUndetected,
            statusSignal = envConfiguratorSignals.pythonStatus,
        )
        envConfiguratorSignals.pythonInstalled.connect(#self.ui.Button_Install_Python.click)
            lambda: envConfiguratorSignals.pythonDetected.emit()
        )
        envConfiguratorSignals.pythonInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = self.tr("安装Python出错"),
                detailedText = str(Exception)
            )
        )
        subEnvPage_detection.addDetectorFrame(
            text = self.tr("Python 依赖库"),
            toolTip = self.tr("重新检测安装"),
            detectMethod = PyReqs_Installer.execute,
            params = (EasyUtils.normPath(requirementsPath)),
            terminateMethod = PyReqs_Installer.terminate,
            threadPool = self.threadPool_env,
            signal_detect = envConfiguratorSignals.pythonDetected,
            signal_detected = envConfiguratorSignals.pyReqsDetected,
            signal_undetected = envConfiguratorSignals.pyReqsUndetected,
            statusSignal = envConfiguratorSignals.pyReqsStatus,
        )
        envConfiguratorSignals.pyReqsInstalled.connect(#self.ui.Button_Install_PyReqs.click)
            lambda: envConfiguratorSignals.pyReqsDetected.emit()
        )
        envConfiguratorSignals.pyReqsInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = self.tr("安装Python依赖库出错"),
                detailedText = str(Exception)
            )
        )
        subEnvPage_detection.addDetectorFrame(
            text = self.tr("Pytorch 框架"),
            toolTip = self.tr("重新检测安装"),
            detectMethod = Pytorch_Installer.execute,
            terminateMethod = Pytorch_Installer.terminate,
            threadPool = self.threadPool_env,
            signal_detect = envConfiguratorSignals.pyReqsDetected,
            signal_detected = envConfiguratorSignals.pytorchDetected,
            signal_undetected = envConfiguratorSignals.pytorchUndetected,
            statusSignal = envConfiguratorSignals.pytorchStatus,
        )
        envConfiguratorSignals.pytorchInstalled.connect(#self.ui.Button_Install_Pytorch.click)
            lambda: envConfiguratorSignals.pytorchDetected.emit()
        )
        envConfiguratorSignals.pytorchInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = self.tr("安装Pytorch出错"),
                detailedText = str(Exception)
            )
        )
        self.ui.Page_Env.addSubPage(
            self.tr("自动配置"), subEnvPage_detection
        )

        '''EnvManagement'''
        # Subpage
        subEnvPage_manager = SubEnvPage_Manager(self.ui.Page_Env)
        component_manager_pytorch = subEnvPage_manager.addComboBoxButtonFrame(
            toolBoxText = self.tr("Pytorch"),
            text = self.tr("选择Pytorch版本"),
            items = [ '2.0.1', '2.2.2'],
            buttonText = self.tr("安装"),
        )
        Function_SetMethodExecutor(
            executeButton = component_manager_pytorch.get(ComponentFlag.Button),
            executeMethod = Pytorch_Installer.execute,
            executeParams = [
                component_manager_pytorch.get(ComponentFlag.ComboBox),
                True
            ],
            terminateMethod = Pytorch_Installer.terminate,
            threadPool = self.threadPool_env,
            parentWindow = self,
        )
        self.ui.Page_Env.addSubPage(
            self.tr("安装管理"), subEnvPage_manager
        )

        #############################################################
        ####################### Content: Models #####################
        #############################################################

        self.mainWindowShown.connect(self.viewModels)

        self.ui.Button_Models_Process_Title.setText(self.tr("音频处理"))
        self.ui.Button_Models_Process_Title.setHorizontal(True)
        self.ui.Button_Models_Process_Title.setChecked(True)
        self.ui.Button_Models_Process_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 0
            )
        )
        self.ui.TabWidget_Models_Process.setTabText(0, "UVR")
        self.modelView_process_uvr.connect(self.ui.Table_Models_Process_UVR.setValue)
        self.ui.Table_Models_Process_UVR.download.connect(
            lambda params: Function_SetMethodExecutor(
                executeMethod = downloadModel,
                executeParams = params,
                threadPool = self.threadPool_models,
                parentWindow = self,
            )
        )

        self.ui.Button_Models_VPR_Title.setText(self.tr("声纹识别 (VPR)"))
        self.ui.Button_Models_VPR_Title.setHorizontal(True)
        self.ui.Button_Models_VPR_Title.setChecked(False)
        self.ui.Button_Models_VPR_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 1
            )
        )
        self.ui.TabWidget_Models_VPR.setTabText(0, "TDNN")
        self.modelView_vpr_tdnn.connect(self.ui.Table_Models_VPR_TDNN.setValue)
        self.ui.Table_Models_VPR_TDNN.download.connect(
            lambda params: Function_SetMethodExecutor(
                executeMethod = downloadModel,
                executeParams = params,
                threadPool = self.threadPool_models,
                parentWindow = self,
            )
        )

        self.ui.Button_Models_ASR_Title.setText(self.tr("语音转录 (ASR)"))
        self.ui.Button_Models_ASR_Title.setHorizontal(True)
        self.ui.Button_Models_ASR_Title.setChecked(False)
        self.ui.Button_Models_ASR_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 2
            )
        )
        self.ui.TabWidget_Models_ASR.setTabText(0, "Whisper")
        self.modelView_asr_whisper.connect(self.ui.Table_Models_ASR_Whisper.setValue)
        self.ui.Table_Models_ASR_Whisper.download.connect(
            lambda params: Function_SetMethodExecutor(
                executeMethod = downloadModel,
                executeParams = params,
                threadPool = self.threadPool_models,
                parentWindow = self,
            )
        )

        self.ui.Button_Models_TTS_Title.setText(self.tr("语音合成 (TTS)"))
        self.ui.Button_Models_TTS_Title.setHorizontal(True)
        self.ui.Button_Models_TTS_Title.setChecked(False)
        self.ui.Button_Models_TTS_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 3
            )
        )
        self.ui.TabWidget_Models_TTS.setTabText(0, "GPT-SoVITS")
        self.modelView_tts_gptsovits.connect(self.ui.Table_Models_TTS_GPTSoVITS.setValue)
        self.ui.Table_Models_TTS_GPTSoVITS.download.connect(
            lambda params: Function_SetMethodExecutor(
                executeMethod = downloadModel,
                executeParams = params,
                threadPool = self.threadPool_models,
                parentWindow = self,
            )
        )

        self.ui.Button_Models_Refresh.setText(self.tr("刷新"))
        self.ui.Button_Models_Refresh.clicked.connect(self.viewModels)

        self.ui.Button_Models_Append.setText(self.tr("添加"))
        self.ui.Button_Models_Append.clicked.connect(self.appendModels)

        #############################################################
        ###################### Content: Process #####################
        #############################################################

        # Guidance
        self.ui.Page_Process.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = self.tr("引导（仅出现一次）"),
                htmlPaths = [
                    Path(resourceDir).joinpath('assets/docs/guidance_process_1_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_process_1.html'),
                    Path(resourceDir).joinpath('assets/docs/guidance_process_2_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_process_2.html')
                ]
            )
        )
        self.ui.Button_Menu_Process.clicked.connect(
            lambda: (
                self.ui.Page_Process.helpButton.click(),
                config.editConfig('Dialog', 'GuidanceShown_Process', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_Process', 'False')) is False else None
        )
        # ParamsManager
        configPath_process = EasyUtils.normPath(Path(configDir).joinpath('config_process.ini'))
        paramsManager_process = ParamsManager(configPath_process)
        # Subpage
        subPage_process = SubToolPage(self.ui.Page_Process, paramsManager_process)
        component_process_mediaDirInput = subPage_process.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("媒体输入目录\n需要处理的音频文件的所在目录。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            section = 'Input params',
            option = 'MediaDirInput',
            defaultValue = ''
        )
        component_process_denoiseAudio = subPage_process.addCheckBoxFrame(
            rootItemText = self.tr("降噪参数"),
            text = self.tr("启用杂音去除\n弱化音频中的非人声部分。"),
            section = 'Denoiser params',
            option = 'DenoiseAudio',
            defaultValue = True
        )
        component_process_denoiseModelPath = subPage_process.addLineEditFrame(
            rootItemText = self.tr("降噪参数"),
            text = self.tr("uvr5模型路径\n用于uvr5降噪的模型文件的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型/onnx类型 (*.pth *.onnx)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('Process', 'UVR', 'Downloaded')),
            section = 'Denoiser params',
            option = 'DenoiseModelPath',
            defaultValue = Path(modelDir).joinpath('Process', 'UVR', 'Downloaded', 'HP5_only_main_vocal.pth').as_posix()
        )
        component_process_denoiseTarget = subPage_process.addComboBoxFrame(
            rootItemText = self.tr("降噪参数"),
            text = self.tr("提取目标\n选择在降噪时要保留的声音对象。"),
            items = [self.tr("人声"), self.tr("背景声")],
            section = 'Denoiser params',
            option = 'DenoiseTarget',
            defaultValue = '人声'
        )
        component_process_sliceAudio = subPage_process.addCheckBoxFrame(
            rootItemText = self.tr("静音切除参数"),
            text = self.tr("启用静音切除\n切除音频中的静音部分。"),
            section = 'Slicer params',
            option = 'SliceAudio',
            defaultValue = True
        )
        component_process_rmsThreshold = subPage_process.addDoubleSpinBoxFrame(
            rootItemText = self.tr("静音切除参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("均方根阈值 (db)\n低于该阈值的片段将被视作静音进行处理，若有降噪需求可以增加该值。"),
            minimum = -100, maximum = 0,
            section = 'Slicer params',
            option = 'RMSThreshold',
            defaultValue = -34.
        )
        component_process_hopSize = subPage_process.addSpinBoxFrame(
            rootItemText = self.tr("静音切除参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("跃点大小 (ms)\n每个RMS帧的长度，增加该值能够提高分割精度但会减慢进程。"),
            minimum = 0, maximum = 100, step = 1,
            section = 'Slicer params',
            option = 'HopSize',
            defaultValue = 10
        )
        component_process_silentInterval = subPage_process.addSpinBoxFrame(
            rootItemText = self.tr("静音切除参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("最小静音间隔 (ms)\n静音部分被分割成的最小长度，若音频只包含短暂中断可以减小该值。"),
            toolTip = self.tr("注意：这个值必须小于最小音频长度，大于跃点大小。"),
            minimum = 0, maximum = 3000, step = 1,
            section = 'Slicer params',
            option = 'SilentInterval',
            defaultValue = 300
        )
        component_process_silenceKept = subPage_process.addSpinBoxFrame(
            rootItemText = self.tr("静音切除参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("最大静音长度 (ms)\n被分割的音频周围保持静音的最大长度。"),
            toolTip = self.tr("注意：这个值无需完全对应被分割音频中的静音长度。算法将自行检索最佳的分割位置。"),
            minimum = 0, maximum = 10000, step = 1,
            section = 'Slicer params',
            option = 'SilenceKept',
            defaultValue = 500
        )
        component_process_audioLength = subPage_process.addSpinBoxFrame(
            rootItemText = self.tr("静音切除参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("最小音频长度 (ms)\n每个被分割的音频片段所需的最小长度。"),
            minimum = 300, maximum = 30000, step = 1,
            section = 'Slicer params',
            option = 'AudioLengthMin',
            defaultValue = 4000
        )
        component_process_mediaFormatOutput = subPage_process.addComboBoxFrame(
            rootItemText = self.tr("输出参数"),
            text = self.tr("媒体输出格式\n媒体文件输出为音频文件的格式，若维持不变则保持'None'即可。"),
            items = ['flac', 'wav', 'mp3', 'aac', 'm4a', 'wma', 'aiff', 'au', 'ogg', 'None'],
            section = 'Output params',
            option = 'MediaFormatOutput',
            defaultValue = 'wav'
        )
        component_process_outputDirName = subPage_process.addLineEditFrame(
            rootItemText = self.tr("输出参数"),
            text = self.tr("输出目录名\n用于保存最后生成的音频文件的目录的名字。"),
            section = 'Output params',
            option = 'OutputDirName',
            defaultValue = '',
            placeholderText = str(date.today())
        )
        lineEdit_process_outputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = component_process_outputDirName.get(ComponentFlag.LineEdit),
            rootEdit = component_process_outputRoot.get(ComponentFlag.LineEdit),
            dirEdit = lineEdit_process_outputDir
        )
        component_process_toMono = subPage_process.addCheckBoxFrame(
            rootItemText = self.tr("输出参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("合并声道\n将输出音频的声道合并为单声道。"),
            section = 'Output params',
            option = 'ToMono',
            defaultValue = False,
            emptyAllowed = True
        )
        component_process_sampleRate = subPage_process.addComboBoxFrame(
            rootItemText = self.tr("输出参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("输出采样率\n输出音频所拥有的采样率，若维持不变则保持'None'即可。"),
            items = ['22050', '44100', '48000', '96000', '192000', 'None'],
            section = 'Output params',
            option = 'SampleRate',
            defaultValue = None,
            emptyAllowed = True
        )
        component_process_sampleWidth = subPage_process.addComboBoxFrame(
            rootItemText = self.tr("输出参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("输出采样位数\n输出音频所拥有的采样位数，若维持不变则保持'None'即可。"),
            items = ['8', '16', '24', '32', '32 (Float)', 'None'],
            section = 'Output params',
            option = 'SampleWidth',
            defaultValue = None,
            emptyAllowed = True
        )
        subPage_process.addChkOutputSideBtn(
            outputRootEdit = component_process_outputRoot.get(ComponentFlag.LineEdit),
        )
        subPage_process.setExecutor(
            prepareSignal = functionSignals.serverStarted,
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_audioProcessor.processAudio,
            executeParamTargets = [
                component_process_mediaDirInput.get(ComponentFlag.LineEdit),
                component_process_mediaFormatOutput.get(ComponentFlag.ComboBox),
                component_process_sampleRate.get(ComponentFlag.ComboBox),
                component_process_sampleWidth.get(ComponentFlag.ComboBox),
                component_process_toMono.get(ComponentFlag.CheckBox),
                component_process_denoiseAudio.get(ComponentFlag.CheckBox),
                component_process_denoiseModelPath.get(ComponentFlag.LineEdit),
                component_process_denoiseTarget.get(ComponentFlag.ComboBox),
                component_process_sliceAudio.get(ComponentFlag.CheckBox),
                component_process_rmsThreshold.get(ComponentFlag.DoubleSpinBox),
                component_process_audioLength.get(ComponentFlag.SpinBox),
                component_process_silentInterval.get(ComponentFlag.SpinBox),
                component_process_hopSize.get(ComponentFlag.SpinBox),
                component_process_silenceKept.get(ComponentFlag.SpinBox),
                component_process_outputRoot.get(ComponentFlag.LineEdit),
                component_process_outputDirName.get(ComponentFlag.LineEdit),
            ],
            terminateMethod = self.task_audioProcessor.terminate_processAudio,
            finishedEvents = {
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool_tasks,
        )
        Function_ConfigureCheckBox(
            checkBox = component_process_denoiseAudio.get(ComponentFlag.CheckBox),
            checkedEvents = {
                lambda: Function_SetWidgetsVisibility(
                    widgetsVisibility = {
                        component_process_denoiseModelPath.get(ComponentFlag.Frame): True,
                        component_process_denoiseTarget.get(ComponentFlag.Frame): True,
                    },
                ) : True
            },
            uncheckedEvents = {
                lambda: Function_SetWidgetsVisibility(
                    widgetsVisibility = {
                        component_process_denoiseModelPath.get(ComponentFlag.Frame): False,
                        component_process_denoiseTarget.get(ComponentFlag.Frame): False,
                    },
                ) : True
            },
        )
        Function_ConfigureCheckBox(
            checkBox = component_process_sliceAudio.get(ComponentFlag.CheckBox),
            checkedEvents = {
                lambda: Function_SetWidgetsVisibility(
                    widgetsVisibility = {
                        component_process_rmsThreshold.get(ComponentFlag.Frame): True,
                        component_process_audioLength.get(ComponentFlag.Frame): True,
                        component_process_silentInterval.get(ComponentFlag.Frame): True,
                        component_process_hopSize.get(ComponentFlag.Frame): True,
                        component_process_silenceKept.get(ComponentFlag.Frame): True,
                    },
                ) : True
            },
            uncheckedEvents = {
                lambda: Function_SetWidgetsVisibility(
                    widgetsVisibility = {
                        component_process_rmsThreshold.get(ComponentFlag.Frame): False,
                        component_process_audioLength.get(ComponentFlag.Frame): False,
                        component_process_silentInterval.get(ComponentFlag.Frame): False,
                        component_process_hopSize.get(ComponentFlag.Frame): False,
                        component_process_silenceKept.get(ComponentFlag.Frame): False,
                    },
                ) : True
            },
        )
        self.ui.Page_Process.addSubPage(
            self.tr("音频处理"), subPage_process
        )

        #############################################################
        ######################## Content: VPR #######################
        #############################################################

        '''TDNN'''
        # Guidance
        self.ui.Page_VPR.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = self.tr("引导（仅出现一次）"),
                htmlPaths = [
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/docs/guidance_vpr_1_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_vpr_1.html')),
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/docs/guidance_vpr_2_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_vpr_2.html'))
                ]
            )
        )
        self.ui.Button_Menu_VPR.clicked.connect(
            lambda: (
                self.ui.Page_VPR.helpButton.click(),
                config.editConfig('Dialog', 'GuidanceShown_VPR', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_VPR', 'False')) is False else None
        )
        # ParamsManager
        configPath_vpr_tdnn = EasyUtils.normPath(Path(configDir).joinpath('config_vpr_tdnn.ini'))
        paramsManager_vpr_tdnn = ParamsManager(configPath_vpr_tdnn)
        # Subpage
        subPage_VPR = SubToolPage(self.ui.Page_VPR, paramsManager_vpr_tdnn)
        component_vpr_tdnn_audioDirInput = subPage_VPR.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("音频输入目录\n需要进行语音识别筛选的音频文件的所在目录。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = process_outputRoot_default,
            section = 'Input params',
            option = 'AudioDirInput',
            defaultValue = '',
        )
        component_vpr_tdnn_stdAudioSpeaker = subPage_VPR.addEditAudioSpeakerTableFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("目标人物与音频\n目标人物的名字及其语音文件的路径。"),
            fileType = "音频类型 (*.flac *.wav *.mp3 *.aac *.m4a *.wma *.aiff *.au *.ogg)",
            section = 'Input params',
            option = 'StdAudioSpeaker',
            defaultValue = {"": ""}
        )
        component_vpr_tdnn_decisionThreshold = subPage_VPR.addDoubleSpinBoxFrame(
            rootItemText = self.tr("语音识别参数"),
            text = self.tr("判断阈值\n判断相似度的阈值，若参与比对的说话人声音相似度较高可以增加该值。"),
            minimum = 0.5,
            maximum = 1,
            step = 0.01,
            section = 'VPR params',
            option = 'DecisionThreshold',
            defaultValue = 0.75
        )
        vpr_tdnn_modelPath_default = Path(modelDir).joinpath('VPR', 'TDNN', 'Downloaded', 'Ecapa-Tdnn_spectrogram.pth').as_posix()
        component_vpr_tdnn_modelPath = subPage_VPR.addLineEditFrame(
            rootItemText = self.tr("语音识别参数"),
            text = self.tr("模型加载路径\n用于加载的声纹识别模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('VPR', 'TDNN', 'Downloaded')),
            section = 'VPR params',
            option = 'ModelPath',
            defaultValue = vpr_tdnn_modelPath_default,
            placeholderText = vpr_tdnn_modelPath_default
        )
        component_vpr_tdnn_modelType = subPage_VPR.addComboBoxFrame(
            rootItemText = self.tr("语音识别参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("模型类型\n声纹识别模型的类型。"),
            items = ['Ecapa-Tdnn'],
            section = 'VPR params',
            option = 'ModelType',
            defaultValue = 'Ecapa-Tdnn'
        )
        component_vpr_tdnn_featureMethod = subPage_VPR.addComboBoxFrame(
            rootItemText = self.tr("语音识别参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("预处理方法\n音频的预处理方法。"),
            items = ['spectrogram', 'melspectrogram'],
            section = 'VPR params',
            option = 'FeatureMethod',
            defaultValue = 'spectrogram'
        )
        component_vpr_tdnn_durationOfAudio = subPage_VPR.addDoubleSpinBoxFrame(
            rootItemText = self.tr("语音识别参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("音频长度\n用于预测的音频长度。"),
            minimum = 0,
            maximum = 30,
            #step = 0.01,
            section = 'VPR params',
            option = 'DurationOfAudio',
            defaultValue = 3.00
        )
        vpr_tdnn_outputDirName_default = str(date.today())
        component_vpr_tdnn_audioDirOutput = subPage_VPR.addLineEditFrame(
            rootItemText = self.tr("输出参数"),
            text = self.tr("输出目录名\n用于保存最后生成的结果文件的目录的名字。"),
            section = 'Output params',
            option = 'AudioDirOutput',
            defaultValue = '',
            placeholderText = vpr_tdnn_outputDirName_default
        )
        lineEdit_vpr_tdnn_outputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = component_vpr_tdnn_audioDirOutput.get(ComponentFlag.LineEdit),
            rootEdit = component_vpr_tdnn_outputRoot.get(ComponentFlag.LineEdit),
            dirEdit = lineEdit_vpr_tdnn_outputDir
        )
        vpr_tdnn_audioSpeakersDataName_default = "Recgonition_" + str(date.today())
        component_vpr_tdnn_fileListName = subPage_VPR.addLineEditFrame(
            rootItemText = self.tr("输出参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("识别结果文本名\n用于保存最后生成的记录音频文件与对应说话人的txt文件的名字。"),
            section = 'Output params',
            option = 'FileListName',
            defaultValue = vpr_tdnn_audioSpeakersDataName_default,
            placeholderText = vpr_tdnn_audioSpeakersDataName_default
        )
        lineEdit_vpr_tdnn_audioSpeakersDataPath = LineEditBase()
        self.setPathAlert(
            fileNameEdit = component_vpr_tdnn_fileListName.get(ComponentFlag.LineEdit),
            dirEdit = lineEdit_vpr_tdnn_outputDir,
            suffix = ".txt",
            fileEdit = lineEdit_vpr_tdnn_audioSpeakersDataPath
        )
        subPage_VPR.addChkOutputSideBtn(
            outputRootEdit = component_vpr_tdnn_outputRoot.get(ComponentFlag.LineEdit),
        )
        def EditVPRResult():
            VPRResultPath = QFunc.getFileDialog(
                mode = FileDialogMode.SelectFile,
                fileType = "txt类型 (*.txt)",
                directory = vpr_tdnn_audioSpeakersDataRoot_default
            )
            if EasyUtils.normPath(VPRResultPath) is not None:
                self.showMask(True, "Generating Form")
                self.showVPRResult(
                    lineEdit_vpr_tdnn_outputDir.text(),
                    VPRResultPath,
                    None
                )
        subPage_VPR.addSideBtn(
            text = self.tr("编辑识别结果"),
            events = [
                EditVPRResult
            ]
        )
        subPage_VPR.setExecutor(
            prepareSignal = functionSignals.serverStarted,
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_vpr.infer,
            executeParamTargets = [
                component_vpr_tdnn_stdAudioSpeaker.get(ComponentFlag.Table),
                component_vpr_tdnn_audioDirInput.get(ComponentFlag.LineEdit),
                component_vpr_tdnn_modelPath.get(ComponentFlag.LineEdit),
                component_vpr_tdnn_modelType.get(ComponentFlag.ComboBox),
                component_vpr_tdnn_featureMethod.get(ComponentFlag.ComboBox),
                component_vpr_tdnn_decisionThreshold.get(ComponentFlag.DoubleSpinBox),
                component_vpr_tdnn_durationOfAudio.get(ComponentFlag.DoubleSpinBox),
                component_vpr_tdnn_outputRoot.get(ComponentFlag.LineEdit),
                component_vpr_tdnn_audioDirOutput.get(ComponentFlag.LineEdit),
                component_vpr_tdnn_fileListName.get(ComponentFlag.LineEdit)
            ],
            terminateMethod = self.task_vpr.terminate_infer,
            finishedEvents = {
                lambda: self.showMask(True, "Generating Form"): TaskStatus.Succeeded,
                lambda: self.showVPRResult(
                    lineEdit_vpr_tdnn_outputDir.text(),
                    lineEdit_vpr_tdnn_audioSpeakersDataPath.text(),
                    list(component_vpr_tdnn_stdAudioSpeaker.get(ComponentFlag.Table).getValue().keys()) + ['']
                ): TaskStatus.Succeeded,
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool_tasks,
        )
        self.ui.Page_VPR.addSubPage(
            self.tr("TDNN"), subPage_VPR
        )

        #############################################################
        ######################## Content: ASR #######################
        #############################################################

        '''Whisper'''
        # Guidance
        self.ui.Page_ASR.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = self.tr("引导（仅出现一次）"),
                htmlPaths = [
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/docs/guidance_asr_1_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_asr_1.html')),
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/docs/guidance_asr_2_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_asr_2.html'))
                ]
            )
        )
        self.ui.Button_Menu_ASR.clicked.connect(
            lambda: (
                self.ui.Page_ASR.helpButton.click(),
                config.editConfig('Dialog', 'GuidanceShown_ASR', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_ASR', 'False')) is False else None
        )
        # ParamsManager
        configPath_asr_whisper = EasyUtils.normPath(Path(configDir).joinpath('config_asr_whisper.ini'))
        paramsManager_asr_whisper = ParamsManager(configPath_asr_whisper)
        # Subpage
        subPage_ASR = SubToolPage(self.ui.Page_ASR, paramsManager_asr_whisper)
        component_asr_whisper_audioDir = subPage_ASR.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("音频输入目录\n需要将语音内容转为文字的音频文件的所在目录。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            section = 'Input params',
            option = 'AudioDir',
            defaultValue = ''
        )
        component_asr_whisper_language = subPage_ASR.addComboBoxFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("音频语种\n指定音频中的语言，若使用自动检测则选择'None'即可。"),
            items = ['zh', 'en', 'de', 'ru', 'ko', 'ja', 'None'],
            section = 'Input params',
            option = 'Language',
            defaultValue = None
        )
        component_asr_whisper_addLanguageInfo = subPage_ASR.addCheckBoxFrame(
            rootItemText = self.tr("语音转录参数"),
            text = self.tr("语种标注\n标注音频中说话人所使用的语言，若用于数据集制作则建议启用。"),
            section = 'Whisper params',
            option = 'AddLanguageInfo',
            defaultValue = True
        )
        asr_whisper_modelPath_default = Path(modelDir).joinpath('ASR', 'Whisper', 'Downloaded', 'small.pt').as_posix()
        component_asr_whisper_modelPath = subPage_ASR.addLineEditFrame(
            rootItemText = self.tr("语音转录参数"),
            text = self.tr("模型加载路径\n用于加载的Whisper模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pt类型 (*.pt)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('ASR', 'Whisper', 'Downloaded')),
            section = 'Whisper params',
            option = 'ModelPath',
            defaultValue = asr_whisper_modelPath_default,
            placeholderText = asr_whisper_modelPath_default
        )
        component_asr_whisper_verbose = subPage_ASR.addCheckBoxFrame(
            rootItemText = self.tr("语音转录参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("显示转录内容\n启用该项后会在运行过程中显示转录的内容，否则只显示进度。"),
            section = 'Whisper params',
            option = 'Verbose',
            defaultValue = True
        )
        component_asr_whisper_fp16 = subPage_ASR.addCheckBoxFrame(
            rootItemText = self.tr("语音转录参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("半精度计算\n主要使用半精度浮点数进行计算，若GPU不可用则忽略或禁用此项。"),
            section = 'Whisper params',
            option = 'fp16',
            defaultValue = True
        )
        component_asr_whisper_conditionOnPreviousText = subPage_ASR.addCheckBoxFrame(
            rootItemText = self.tr("语音转录参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("关联上下文\n在音频之间的内容具有关联性时启用该项可以获得更好的效果。"),
            section = 'Whisper params',
            option = 'ConditionOnPreviousText',
            defaultValue = False
        )
        asr_whisper_outputDirName_default = str(date.today())
        component_asr_whisper_srtDirName = subPage_ASR.addLineEditFrame(
            rootItemText = self.tr("输出参数"),
            text = self.tr("输出目录名\n用于保存最后生成的字幕文件的目录的名字。"),
            section = 'Output params',
            option = 'SRTDirName',
            defaultValue = '',
            placeholderText = asr_whisper_outputDirName_default
        )
        lineEdit_asr_whisper_outputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = component_asr_whisper_srtDirName.get(ComponentFlag.LineEdit),
            rootEdit = component_asr_whisper_outputRoot.get(ComponentFlag.LineEdit),
            dirEdit = lineEdit_asr_whisper_outputDir
        )
        subPage_ASR.addChkOutputSideBtn(
            outputRootEdit = component_asr_whisper_outputRoot.get(ComponentFlag.LineEdit)
        )
        subPage_ASR.setExecutor(
            prepareSignal = functionSignals.serverStarted,
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_whisper.infer,
            executeParamTargets = [
                component_asr_whisper_modelPath.get(ComponentFlag.LineEdit),
                component_asr_whisper_audioDir.get(ComponentFlag.LineEdit),
                component_asr_whisper_verbose.get(ComponentFlag.CheckBox),
                component_asr_whisper_addLanguageInfo.get(ComponentFlag.CheckBox),
                component_asr_whisper_language.get(ComponentFlag.ComboBox),
                component_asr_whisper_conditionOnPreviousText.get(ComponentFlag.CheckBox),
                component_asr_whisper_fp16.get(ComponentFlag.CheckBox),
                component_asr_whisper_outputRoot.get(ComponentFlag.LineEdit),
                component_asr_whisper_srtDirName.get(ComponentFlag.LineEdit)
            ],
            terminateMethod = self.task_whisper.terminate_infer,
            finishedEvents = {
                lambda: self.showMask(True, "Generating Form"): TaskStatus.Succeeded,
                lambda: self.showASRResult(
                    lineEdit_asr_whisper_outputDir.text(),
                    component_asr_whisper_audioDir.get(ComponentFlag.LineEdit).text()
                ): TaskStatus.Succeeded,
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool_tasks,
        )
        self.ui.Page_ASR.addSubPage(
            self.tr("Whisper"), subPage_ASR
        )

        #############################################################
        ###################### Content: Dataset #####################
        #############################################################

        '''GPT-SoVITS'''
        # Guidance
        self.ui.Page_Dataset.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = self.tr("引导（仅出现一次）"),
                htmlPaths = [
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/docs/guidance_dataset_1_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_dataset_1.html')),
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/docs/guidance_dataset_2_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_dataset_2.html'))
                ]
            )
        )
        self.ui.Button_Menu_Dataset.clicked.connect(
            lambda: (
                self.ui.Page_Dataset.helpButton.click(),
                config.editConfig('Dialog', 'GuidanceShown_Dataset', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_Dataset', 'False')) is False else None
        )
        # ParamsManager
        configPath_dat_gptsovits = EasyUtils.normPath(Path(configDir).joinpath('config_dataset_gpt-sovits.ini'))
        paramsManager_dat_gptsovits = ParamsManager(configPath_dat_gptsovits)
        # Subpage
        subPage_dataset_gptsovits = SubToolPage(self.ui.Page_Dataset, paramsManager_dat_gptsovits)
        component_dat_gptsovits_wavDir = subPage_dataset_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("音频文件目录/语音识别结果文本路径\n音频文件的所在目录，或者提供由语音识别得到的文本文件。"),
            section = 'Input params',
            option = 'WAVDir',
            defaultValue = ''
        )
        component_dat_gptsovits_wavDir.get(ComponentFlag.LineEdit).fileButton.clicked.connect(
            lambda: self.setDirPathSelection(
                textReciever = component_dat_gptsovits_wavDir.get(ComponentFlag.LineEdit),
                dirSelectionText = "语音识别结果文本路径",
                pathSelectionText = "音频文件目录",
                fileType = "txt类型 (*.txt)",
                directory = vpr_tdnn_audioSpeakersDataRoot_default
            )
        )
        component_dat_gptsovits_srtDir = subPage_dataset_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("字幕输入目录\n字幕文件的所在目录，字幕文件须与对应音频文件同名且在文本中注明所属语言。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = asr_whisper_outputRoot_default,
            section = 'Input params',
            option = 'SRTDir',
            defaultValue = ''
        )
        asr_whisper_outputDirName_default = '路径|人名|语言|文本'
        component_dat_gptsovits_dataFormatPath = subPage_dataset_gptsovits.addLineEditFrame(
            rootItemText = self.tr("预处理参数"),
            text = self.tr("数据文本格式\n数据集的文本格式，默认使用GPT-SoVITS的标准。"),
            section = 'GPT-SoVITS params',
            option = 'DataFormatPath',
            defaultValue = asr_whisper_outputDirName_default,
            placeholderText = asr_whisper_outputDirName_default
        )
        component_dat_gptsovits_dataFormatPath.get(ComponentFlag.LineEdit).textChanged.connect(
            lambda value: (
                MessageBoxBase.pop(self,
                    QMessageBox.Warning, "Warning",
                    "请保留关键词：'路径'，'人名'，'语言'，'文本'",
                ),
                paramsManager_dat_gptsovits.resetParam(component_dat_gptsovits_dataFormatPath.get(ComponentFlag.LineEdit)),
            ) if not all(Keyword in value for Keyword in ['路径', '人名', '语言', '文本']) else None
        )
        dat_gptsovits_outputDirName_default = str(date.today())
        component_dat_gptsovits_outputDirName = subPage_dataset_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输出参数"),
            text = self.tr("输出目录名\n用于保存最后生成的数据集文件的目录的名字。"),
            section = 'Output params',
            option = 'OutputDirName',
            defaultValue = '',
            placeholderText = dat_gptsovits_outputDirName_default
        )
        lineEdit_dat_gptsovits_outputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = component_dat_gptsovits_outputDirName.get(ComponentFlag.LineEdit),
            rootEdit = component_dat_gptsovits_outputRoot.get(ComponentFlag.LineEdit),
            dirEdit = lineEdit_dat_gptsovits_outputDir
        )
        dat_gptsovits_fileListName_default = "Train_" + str(date.today())
        component_dat_gptsovits_fileListName = subPage_dataset_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输出参数"),
            toolBoxText = self.tr("高级设置"),
            text = self.tr("数据集文本名\n用于保存最后生成的数据集txt文件的名字。"),
            section = 'Output params',
            option = 'FileListName',
            defaultValue = dat_gptsovits_fileListName_default,
            placeholderText = dat_gptsovits_fileListName_default
        )
        lineEdit_dat_gptsovits_fileListPath = LineEditBase()
        self.setPathAlert(
            fileNameEdit = component_dat_gptsovits_fileListName.get(ComponentFlag.LineEdit),
            dirEdit = lineEdit_dat_gptsovits_outputDir,
            suffix = ".txt",
            fileEdit = lineEdit_dat_gptsovits_fileListPath,
        )
        subPage_dataset_gptsovits.addChkOutputSideBtn(
            outputRootEdit = component_dat_gptsovits_outputRoot.get(ComponentFlag.LineEdit)
        )
        subPage_dataset_gptsovits.setExecutor(
            prepareSignal = functionSignals.serverStarted,
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_gptsovits.preprocess,
            executeParamTargets = [
                component_dat_gptsovits_srtDir.get(ComponentFlag.LineEdit),
                component_dat_gptsovits_wavDir.get(ComponentFlag.LineEdit),
                component_dat_gptsovits_dataFormatPath.get(ComponentFlag.LineEdit),
                component_dat_gptsovits_outputRoot.get(ComponentFlag.LineEdit),
                component_dat_gptsovits_outputDirName.get(ComponentFlag.LineEdit),
                component_dat_gptsovits_fileListName.get(ComponentFlag.LineEdit)
            ],
            terminateMethod = self.task_gptsovits.terminate_preprocess,
            finishedEvents = {
                lambda: self.showMask(True, "Generating Form"): TaskStatus.Succeeded,
                lambda: self.showDATResult(
                    lineEdit_dat_gptsovits_fileListPath.text(),
                    None
                ): TaskStatus.Succeeded,
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool_tasks,
        )
        self.ui.Page_Dataset.addSubPage(
            self.tr("GPT-SoVITS"), subPage_dataset_gptsovits
        )

        #############################################################
        ####################### Content: Train ######################
        #############################################################

        '''GPT-SoVITS'''
        # Guidance
        self.ui.Page_Train.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = self.tr("引导（仅出现一次）"),
                htmlPaths = [
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/docs/guidance_train_1_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_train_1.html')),
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/docs/guidance_train_2_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_train_2.html'))
                ]
            )
        )
        self.ui.Button_Menu_Train.clicked.connect(
            lambda: (
                self.ui.Page_Train.helpButton.click(),
                config.editConfig('Dialog', 'GuidanceShown_Train', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_Train', 'False')) is False else None
        )

        # ParamsManager
        configPath_train_gptsovits = EasyUtils.normPath(Path(configDir).joinpath('config_train_gpt-sovits.ini'))
        paramsManager_train_gptsovits = ParamsManager(configPath_train_gptsovits)
        # Subpage
        subPage_train_gptsovits = SubToolPage(self.ui.Page_Train, paramsManager_train_gptsovits)
        component_train_gptsovits_version = subPage_train_gptsovits.addComboBoxFrame(
            rootItemText = self.tr("全局设置"),
            text = self.tr("训练版本\nGPT-SoVITS模型的训练版本，注意v4训练需要8G以上的显存。"),
            items = ['v2Pro', 'v4'],
            section = 'Input params',
            option = 'version',
            defaultValue = 'v2Pro'
        )
        component_train_gptsovits_fileListPath = subPage_train_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("训练集文本路径\n用于提供训练集音频路径及其语音内容的训练集txt文件的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "txt类型 (*.txt)",
            directory = dat_gptsovits_outputRoot_default,
            section = 'Input params',
            option = 'FileListPath',
            defaultValue = ''
        )
        train_gptsovits_modelPathS1_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's1bert25hz-5kh-longer-epoch=12-step=369668.ckpt').as_posix()
        component_train_gptsovits_modelPathS1 = subPage_train_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("GPT模型路径\nGPT（s1）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "ckpt类型 (*.ckpt)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2')),
            section = 'GPT-SoVITS params',
            option = 'ModelPathS1',
            defaultValue = train_gptsovits_modelPathS1_default,
            placeholderText = train_gptsovits_modelPathS1_default
        )
        train_gptsovits_modelPathS2G_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2Gv2Pro.pth').as_posix()
        component_train_gptsovits_modelPathS2G = subPage_train_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("SoVITS生成器底模路径\nSoVITS生成器（s2G）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2')),
            section = 'GPT-SoVITS params',
            option = 'ModelPathS2G',
            defaultValue = train_gptsovits_modelPathS2G_default,
            placeholderText = train_gptsovits_modelPathS2G_default
        )
        train_gptsovits_modelPathS2D_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2Dv2Pro.pth').as_posix()
        component_train_gptsovits_modelPathS2D = subPage_train_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("SoVITS判别器底模路径\nSoVITS判别器（s2D）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2')),
            section = 'GPT-SoVITS params',
            option = 'ModelPathS2D',
            defaultValue = train_gptsovits_modelPathS2D_default,
            placeholderText = train_gptsovits_modelPathS2D_default
        )
        train_gptsovits_modelPathSV_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'sv', 'eres2netv2w24s4ep4.ckpt').as_posix()
        component_train_gptsovits_modelPathSV = subPage_train_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("SV模型路径\nSV模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "ckpt类型 (*.ckpt)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'sv')),
            section = 'GPT-SoVITS params',
            option = 'ModelPathSV',
            defaultValue = train_gptsovits_modelPathSV_default,
            placeholderText = train_gptsovits_modelPathSV_default
        )
        train_gptsovits_modelDirBERT_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-roberta-wwm-ext-large').as_posix()
        component_train_gptsovits_modelDirBERT = subPage_train_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("BERT模型路径\nBERT模型（文件夹）的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'GPT-SoVITS params',
            option = 'ModelDirBERT',
            defaultValue = train_gptsovits_modelDirBERT_default,
            placeholderText = train_gptsovits_modelDirBERT_default
        )
        train_gptsovits_modelDirHuBERT_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-hubert-base').as_posix()
        component_train_gptsovits_modelDirHuBERT = subPage_train_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("HuBERT模型路径\nHuBERT模型（文件夹）的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'GPT-SoVITS params',
            option = 'ModelDirHuBERT',
            defaultValue = train_gptsovits_modelDirHuBERT_default,
            placeholderText = train_gptsovits_modelDirHuBERT_default
        )
        train_gptsovits_modelDirG2PW_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'g2pw').as_posix()
        component_train_gptsovits_modelDirG2PW = subPage_train_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("G2PW模型路径\nG2PW模型（文件夹）的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'Input params',
            option = 'ModelDirG2PW',
            defaultValue = train_gptsovits_modelDirG2PW_default,
            placeholderText = train_gptsovits_modelDirG2PW_default
        )
        component_train_gptsovits_halfPrecision = subPage_train_gptsovits.addCheckBoxFrame(
            rootItemText = self.tr("训练参数"),
            text = self.tr("半精度训练\n通过混合了float16精度的训练方式减小显存占用。"),
            section = 'GPT-SoVITS params',
            option = 'HalfPrecision',
            defaultValue = True
        )
        component_train_gptsovits_ifGradCkpt = subPage_train_gptsovits.addCheckBoxFrame(
            rootItemText = self.tr("训练参数"),
            text = self.tr("梯度检查点\n是否开启梯度检查点节省显存占用。"),
            section = 'GPT-SoVITS params',
            option = 'IfGradCkpt',
            defaultValue = True
        )
        component_train_gptsovits_loraRank = subPage_train_gptsovits.addComboBoxFrame(
            rootItemText = self.tr("训练参数"),
            text = self.tr("Lora秩\n提高秩会增加训练参数的数量，但也会增加计算成本和存储需求。"),
            items = ['16', '32', '64', '128'],
            section = 'GPT-SoVITS params',
            option = 'LoraRank',
            defaultValue = '32'
        )
        train_gptsovits_outputDirName_default = str(date.today())
        component_train_gptsovits_outputDirName = subPage_train_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输出参数"),
            text = self.tr("输出目录名\n存放训练所得模型的目录的名字。"),
            section = 'Output params',
            option = 'OutputDirName',
            defaultValue = '',
            placeholderText = train_gptsovits_outputDirName_default
        )
        lineEdit_train_gptsovits_outputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = component_train_gptsovits_outputDirName.get(ComponentFlag.LineEdit),
            rootEdit = component_train_gptsovits_outputRoot.get(ComponentFlag.LineEdit),
            dirEdit = lineEdit_train_gptsovits_outputDir
        )
        train_gptsovits_logDir_default = Path(currentDir).joinpath('EVT_TrainLog', 'GPT-SoVITS').as_posix()
        component_train_gptsovits_outputLogDir = subPage_train_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输出参数"),
            text = self.tr("日志输出目录\n训练时生成的日志等文件的存放目录，子目录会使用输出目录名。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(train_gptsovits_logDir_default).parent),
            section = 'Output params',
            option = 'OutputLogDir',
            defaultValue = train_gptsovits_logDir_default,
            placeholderText = train_gptsovits_logDir_default
        )
        subPage_train_gptsovits.addChkOutputSideBtn(
            outputRootEdit = component_train_gptsovits_outputRoot.get(ComponentFlag.LineEdit)
        )
        component_train_gptsovits_runTensorboard = subPage_train_gptsovits.addSideBtn(
            text = self.tr("启动Tensorboard"),
            events = [
                lambda: Function_SetMethodExecutor(
                    executeMethod = Function_RunTensorboard,
                    executeParams = component_train_gptsovits_outputLogDir.get(ComponentFlag.LineEdit).text(),
                    threadPool = self.threadPool_tasks,
                    parentWindow = self,
                )
            ]
        )
        subPage_train_gptsovits.setExecutor(
            prepareSignal = functionSignals.serverStarted,
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_gptsovits.train,
            executeParamTargets = [
                component_train_gptsovits_version.get(ComponentFlag.ComboBox),
                component_train_gptsovits_fileListPath.get(ComponentFlag.LineEdit),
                component_train_gptsovits_modelPathS1.get(ComponentFlag.LineEdit),
                component_train_gptsovits_modelPathS2G.get(ComponentFlag.LineEdit),
                component_train_gptsovits_modelPathS2D.get(ComponentFlag.LineEdit),
                component_train_gptsovits_modelPathSV.get(ComponentFlag.LineEdit),
                component_train_gptsovits_modelDirBERT.get(ComponentFlag.LineEdit),
                component_train_gptsovits_modelDirHuBERT.get(ComponentFlag.LineEdit),
                component_train_gptsovits_modelDirG2PW.get(ComponentFlag.LineEdit),
                component_train_gptsovits_halfPrecision.get(ComponentFlag.CheckBox),
                component_train_gptsovits_ifGradCkpt.get(ComponentFlag.CheckBox),
                component_train_gptsovits_loraRank.get(ComponentFlag.ComboBox),
                component_train_gptsovits_outputRoot.get(ComponentFlag.LineEdit),
                component_train_gptsovits_outputDirName.get(ComponentFlag.LineEdit),
                component_train_gptsovits_outputLogDir.get(ComponentFlag.LineEdit)
            ],
            terminateMethod = self.task_gptsovits.terminate_train,
            finishedEvents = {
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool_tasks,
        )
        Function_ConfigureComboBox(
            comboBox = component_train_gptsovits_version.get(ComponentFlag.ComboBox),
            textChangedEvents = {
                'v2Pro': lambda: Function_SetWidgetsVisibility(
                    widgetsVisibility = {
                        component_train_gptsovits_modelPathS2D.get(ComponentFlag.Frame): True,
                        component_train_gptsovits_modelPathSV.get(ComponentFlag.Frame): True,
                        component_train_gptsovits_ifGradCkpt.get(ComponentFlag.Frame): False,
                        component_train_gptsovits_loraRank.get(ComponentFlag.Frame): False,
                    }
                ),
                'v4': lambda: Function_SetWidgetsVisibility(
                    widgetsVisibility = {
                        component_train_gptsovits_modelPathS2D.get(ComponentFlag.Frame): False,
                        component_train_gptsovits_modelPathSV.get(ComponentFlag.Frame): False,
                        component_train_gptsovits_ifGradCkpt.get(ComponentFlag.Frame): True,
                        component_train_gptsovits_loraRank.get(ComponentFlag.Frame): True,
                    }
                ),
            },
            takeEffect = True
        )
        self.ui.Page_Train.addSubPage(
            self.tr("GPT-SoVITS"), subPage_train_gptsovits
        )

        #############################################################
        ######################## Content: TTS #######################
        #############################################################

        '''GPT-SoVITS'''
        # Guidance
        self.ui.Page_TTS.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = self.tr("引导（仅出现一次）"),
                htmlPaths = [
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/docs/guidance_tts_1_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_tts_1.html')),
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/docs/guidance_tts_2_zh.html' if currentLanguage() == Language.ZH else 'assets/docs/guidance_tts_2.html'))
                ]
            )
        )
        self.ui.Button_Menu_TTS.clicked.connect(
            lambda: (
                self.ui.Page_TTS.helpButton.click(),
                config.editConfig('Dialog', 'GuidanceShown_TTS', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_TTS', 'False')) is False else None
        )

        # ParamsManager
        configPath_tts_gptsovits = EasyUtils.normPath(Path(configDir).joinpath('config_tts_gpt-sovits.ini'))
        paramsManager_tts_gptsovits = ParamsManager(configPath_tts_gptsovits)
        # Subpage
        subPage_tts_gptsovits = SubToolPage(self.ui.Page_TTS, paramsManager_tts_gptsovits)
        component_tts_gptsovits_version = subPage_tts_gptsovits.addComboBoxFrame(
            rootItemText = self.tr("全局设置"),
            text = self.tr("推理版本\nGPT-SoVITS模型的推理版本。"),
            items = ['v2Pro', 'v4'],
            section = 'Input params',
            option = 'Version',
            defaultValue = 'v2Pro'
        )
        tts_gptsovits_modelPathS1_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's1bert25hz-5kh-longer-epoch=12-step=369668.ckpt').as_posix()
        component_tts_gptsovits_modelPathS1 = subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("GPT模型路径\nGPT（s1）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "ckpt类型 (*.ckpt)",
            directory = train_gptsovits_outputRoot_default,
            section = 'Input params',
            option = 'ModelPathS1',
            defaultValue = tts_gptsovits_modelPathS1_default,
            placeholderText = tts_gptsovits_modelPathS1_default
        )
        tts_gptsovits_modelPathS2Gv2Pro_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2Gv2Pro.pth').as_posix()
        component_tts_gptsovits_modelPathS2Gv2Pro = subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("SoVITSv2Pro模型路径\nSoVITSv2Pro（s2Gv2Pro）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = train_gptsovits_outputRoot_default,
            section = 'Input params',
            option = 'ModelPathS2Gv2Pro',
            defaultValue = tts_gptsovits_modelPathS2Gv2Pro_default,
            placeholderText = tts_gptsovits_modelPathS2Gv2Pro_default
        )
        tts_gptsovits_modelPathS2Gv4_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2Gv4.pth').as_posix()
        component_tts_gptsovits_modelPathS2Gv4 = subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("SoVITSv4底模路径\nSoVITSv4（s2Gv4）底模的路径，用于加载lora。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'Input params',
            option = 'ModelPathS2Gv4',
            defaultValue = tts_gptsovits_modelPathS2Gv4_default,
            placeholderText = tts_gptsovits_modelPathS2Gv4_default
        )
        tts_gptsovits_modelDirBERT_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-roberta-wwm-ext-large').as_posix()
        component_tts_gptsovits_modelDirBERT = subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("BERT模型路径\nBERT模型（文件夹）的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'Input params',
            option = 'ModelDirBERT',
            defaultValue = tts_gptsovits_modelDirBERT_default,
            placeholderText = tts_gptsovits_modelDirBERT_default
        )
        tts_gptsovits_modelDirHuBERT_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-hubert-base').as_posix()
        component_tts_gptsovits_modelDirHuBERT = subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("HuBERT模型路径\nHuBERT模型（文件夹）的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'Input params',
            option = 'ModelDirHuBERT',
            defaultValue = tts_gptsovits_modelDirHuBERT_default,
            placeholderText = tts_gptsovits_modelDirHuBERT_default
        )
        tts_gptsovits_modelDirBigVGAN_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'nvidia--bigvgan').as_posix()
        component_tts_gptsovits_modelDirBigVGAN = subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("BigVGAN模型路径\nBigVGAN模型（文件夹）的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'Input params',
            option = 'ModelDirBigVGAN',
            defaultValue = tts_gptsovits_modelDirBigVGAN_default,
            placeholderText = tts_gptsovits_modelDirBigVGAN_default
        )
        tts_gptsovits_modelPathVocoder_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 'vocoder.pth').as_posix()
        component_tts_gptsovits_modelPathVocoder = subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("Vocoder模型路径\nVocoder模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'Input params',
            option = 'ModelPathVocoder',
            defaultValue = tts_gptsovits_modelPathVocoder_default,
            placeholderText = tts_gptsovits_modelPathVocoder_default
        )
        tts_gptsovits_modelPathSV_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'sv', 'eres2netv2w24s4ep4.ckpt').as_posix()
        component_tts_gptsovits_modelPathSV = subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("SV模型路径\nSV模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "ckpt类型 (*.ckpt)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'sv')),
            section = 'Input params',
            option = 'ModelPathSV',
            defaultValue = tts_gptsovits_modelPathSV_default,
            placeholderText = tts_gptsovits_modelPathSV_default
        )
        tts_gptsovits_modelDirG2PW_default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'g2pw').as_posix()
        component_tts_gptsovits_modelDirG2PW = subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = self.tr("输入参数"),
            text = self.tr("G2PW模型路径\nG2PW模型（文件夹）的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'Input params',
            option = 'ModelDirG2PW',
            defaultValue = tts_gptsovits_modelDirG2PW_default,
            placeholderText = tts_gptsovits_modelDirG2PW_default
        )
        subPage_tts_gptsovits.setExecutor(
            prepareSignal = functionSignals.serverStarted,
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_gptsovits.infer_webui,
            executeParamTargets = [
                component_tts_gptsovits_version.get(ComponentFlag.ComboBox),
                component_tts_gptsovits_modelPathS2Gv2Pro.get(ComponentFlag.LineEdit),
                component_tts_gptsovits_modelPathS2Gv4.get(ComponentFlag.LineEdit),
                component_tts_gptsovits_modelPathS1.get(ComponentFlag.LineEdit),
                component_tts_gptsovits_modelDirHuBERT.get(ComponentFlag.LineEdit),
                component_tts_gptsovits_modelDirBERT.get(ComponentFlag.LineEdit),
                component_tts_gptsovits_modelDirBigVGAN.get(ComponentFlag.LineEdit),
                component_tts_gptsovits_modelPathVocoder.get(ComponentFlag.LineEdit),
                component_tts_gptsovits_modelPathSV.get(ComponentFlag.LineEdit),
                component_tts_gptsovits_modelDirG2PW.get(ComponentFlag.LineEdit),
            ],
            terminateMethod = self.task_gptsovits.terminate_infer_webui,
            finishedEvents = {
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool_tasks,
        )
        Function_ConfigureComboBox(
            comboBox = component_tts_gptsovits_version.get(ComponentFlag.ComboBox),
            textChangedEvents = {
                "v2Pro": lambda: Function_SetWidgetsVisibility(
                    widgetsVisibility = {
                        component_tts_gptsovits_modelPathS2Gv4.get(ComponentFlag.Frame): False,
                        component_tts_gptsovits_modelDirBigVGAN.get(ComponentFlag.Frame): False,
                        component_tts_gptsovits_modelPathSV.get(ComponentFlag.Frame): True,
                        component_tts_gptsovits_modelPathVocoder.get(ComponentFlag.Frame): False,
                    },
                ),
                "v4": lambda: Function_SetWidgetsVisibility(
                    widgetsVisibility = {
                        component_tts_gptsovits_modelPathS2Gv4.get(ComponentFlag.Frame): True,
                        component_tts_gptsovits_modelDirBigVGAN.get(ComponentFlag.Frame): True,
                        component_tts_gptsovits_modelPathSV.get(ComponentFlag.Frame): False,
                        component_tts_gptsovits_modelPathVocoder.get(ComponentFlag.Frame): True,
                    },
                ),
            },
            takeEffect = True
        )
        self.ui.Page_TTS.addSubPage(
            self.tr("GPT-SoVITS"), subPage_tts_gptsovits
        )

        #############################################################
        ##################### Content: Settings #####################
        #############################################################

        Function_ConfigureCheckBox(
            checkBox = component_settings_autoReset.get(ComponentFlag.CheckBox),
            checkedEvents = {
                lambda: self.mainWindowShown.connect(
                    lambda: (
                        paramsManager_process.resetSettings(),
                        paramsManager_vpr_tdnn.resetSettings(),
                        paramsManager_asr_whisper.resetSettings(),
                        paramsManager_dat_gptsovits.resetSettings(),
                        paramsManager_train_gptsovits.resetSettings(),
                        paramsManager_tts_gptsovits.resetSettings(),
                    )
                ) : True
            },
            uncheckedEvents = {
            },
        )
        Function_ConfigureCheckBox(
            checkBox = component_settings_autoCorrelate.get(ComponentFlag.CheckBox),
            checkedEvents = {
                lambda: Function_ParamsSynchronizer(
                    lineEdit_process_outputDir,
                    {lineEdit_process_outputDir: component_vpr_tdnn_audioDirInput.get(ComponentFlag.LineEdit)}
                ) : True,
                lambda: Function_ParamsSynchronizer(
                    lineEdit_vpr_tdnn_audioSpeakersDataPath,
                    {lineEdit_vpr_tdnn_audioSpeakersDataPath: component_dat_gptsovits_wavDir.get(ComponentFlag.LineEdit)}
                ) : True,
                lambda: Function_ParamsSynchronizer(
                    lineEdit_vpr_tdnn_outputDir,
                    {lineEdit_vpr_tdnn_outputDir: component_asr_whisper_audioDir.get(ComponentFlag.LineEdit)}
                ) : True,
                lambda: Function_ParamsSynchronizer(
                    lineEdit_asr_whisper_outputDir,
                    {lineEdit_asr_whisper_outputDir: component_dat_gptsovits_srtDir.get(ComponentFlag.LineEdit)}
                ) : True,
                lambda: Function_ParamsSynchronizer(
                    lineEdit_dat_gptsovits_fileListPath,
                    {lineEdit_dat_gptsovits_fileListPath: component_train_gptsovits_fileListPath.get(ComponentFlag.LineEdit)}
                ) : True,
            },
            uncheckedEvents = {
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "The setting will take effect after restart.\n该设置将于重启之后生效"
                ) : False
            },
        )

        #############################################################
        ####################### Content: Info #######################
        #############################################################

        self.ui.Button_Info_Title.setText(self.tr("用户须知"))

        self.ui.TextBrowser_Text_Info.setFont(QFont("Microsoft YaHei", 12))
        self.ui.TextBrowser_Text_Info.loadMarkdown(Path(resourceDir).joinpath('assets/docs/announcement_zh.md').as_posix() if currentLanguage() == Language.ZH else Path(resourceDir).joinpath('assets/docs/announcement.md').as_posix())

        #############################################################
        ###################### Content: Console #####################
        #############################################################

        self.ui.Button_Console_Title.setText(self.tr("终端"))

        self.ui.PlainTextEdit_Console.setMaximumLines(333)
        logMonitor = QTasks.MonitorFile(logPath, mode = 'append')
        logMonitor.start()
        logMonitor.contentChanged.connect(
            lambda content: (
                self.ui.PlainTextEdit_Console.clear() if content == "" else self.ui.PlainTextEdit_Console.append(content),
                self.ui.PlainTextEdit_Console.moveCursor(QTextCursor.End)
            )
        )

        self.ui.Button_Console_Copy.clicked.connect(
            lambda: (
                QApplication.clipboard().setText(self.ui.PlainTextEdit_Console.toPlainText()),
                MessageBoxBase.pop(self, windowTitle = "Tip", text = "已复制输出日志到剪切板")
            )
        )

        self.ui.Button_Console_Clear.clicked.connect(logMonitor.clear)

        self.ui.Button_Console_Fold.clicked.connect(self.ui.Button_Toggle_Console.click)

        #############################################################
        ######################### StatusBar #########################
        #############################################################

        # Toggle Console
        self.ui.Button_Toggle_Console.setToolTip(self.tr("点击以展开/折叠终端"))
        self.ui.Button_Toggle_Console.clicked.connect(
            lambda: Function_AnimateFrame(
                frame = self.ui.Frame_Console,
                minHeight = 0,
                maxHeight = 210,
            )
        )
        self.ui.Frame_Console.setFixedHeight(0)

        # Display ToolsStatus
        self.ui.Label_ToolsStatus.clear()
        functionSignals.taskStatus.connect(
            lambda Task, Status: self.ui.Label_ToolsStatus.setText(
                f"工具状态：{'忙碌' if Status == TaskStatus.Started else '空闲'}"
            ) if Task in [
                self.task_audioProcessor.__class__.processAudio.__qualname__,
                self.task_vpr.__class__.infer.__qualname__,
                self.task_whisper.__class__.infer.__qualname__,
                self.task_gptsovits.__class__.preprocess.__qualname__,
                self.task_gptsovits.__class__.train.__qualname__,
                self.task_gptsovits.__class__.infer_webui.__qualname__,
            ] else None
        )

        # Display Usage
        self.MonitorUsage.usageInfo.connect(
            lambda Usage_CPU, Usage_GPU: (
                self.ui.Label_Usage_CPU.setText(f"CPU: {Usage_CPU}"),
                self.ui.Label_Usage_GPU.setText(f"GPU: {Usage_GPU}")
            )
        )

        # Display Version
        self.ui.Label_Version.setText(currentVersion)

        # Set Theme
        componentsSignals.setTheme.emit(config.getValue('Settings', 'Theme', Theme.Auto))

        # Show MainWindow (and emit signal)
        self.show()
        self.mainWindowShown.emit()

        # Start server
        self.startServer()

##############################################################################################################################

if __name__ == "__main__":
    App = QApplication(sys.argv)

    # Set Language
    updateLanguage(config.getValue('Settings', 'Language', Language.Auto))

    # Create&Show SplashScreen
    SC = QSplashScreen(QPixmap(EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/SplashScreen.png'))))
    #SC.showMessage('Loading...', alignment = Qt.AlignmentFlag.AlignCenter)
    SC.show()

    def showMainWindow():
        # Flush UI
        App.processEvents()
        # Init&Show MainWindow
        MW = MainWindow()
        MW.main()
        # Close SplashScreen
        SC.finish(MW) #SC.close()

    QTimer.singleShot(1984, showMainWindow)

    sys.exit(App.exec())

##############################################################################################################################