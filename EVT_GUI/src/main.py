import os
import sys
import time
import argparse
import subprocess
import PyEasyUtils as EasyUtils
from pathlib import Path
from datetime import date
from PySide6 import __file__ as PySide6_File
from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtCore import QCoreApplication as QCA, QThreadPool, QTimer
from PySide6.QtGui import QColor, QPixmap, QIcon, QTextCursor
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets import QTasks
from QEasyWidgets import ComponentsSignals, Theme, currentTheme, Language, currentLanguage, IconBase
from QEasyWidgets.Windows import MessageBoxBase

from views import *
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
parser.add_argument("--updater",           help = "path to updater",          default = Path(resourceDir).joinpath('updater.exe') if isFileCompiled else Path(currentDir).joinpath('updater.py'))
parser.add_argument("--core",              help = "dir of core files",        default = Path(resourceDir).joinpath('EVT_Core'))
parser.add_argument("--manifest",          help = "path to manifest.json",    default = Path(resourceDir).joinpath('manifest.json'))
parser.add_argument("--requirements",      help = "path to requirements.txt", default = Path(resourceDir).joinpath('requirements.txt'))
parser.add_argument("--dependencies",      help = "dir of dependencies",      default = Path(currentDir).joinpath(''))
parser.add_argument("--models",            help = "dir of models",            default = Path(currentDir).joinpath('Models'))
parser.add_argument("--output",            help = "dir of output",            default = Path(currentDir).joinpath(''))
parser.add_argument("--profile",           help = "dir of profile",           default = Path(currentDir).joinpath(''))
parser.add_argument("--deprecatedVersion", help = "deprecated version",       default = None)
args = parser.parse_args()

updaterPath = args.updater
coreDir = args.core
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

def checkIntegrity():
    """
    ClientFunc: check file integrity
    """
    error = EasyUtils.runCMD(
        args = [
            f'cd "{coreDir}"',
            'python -c "'
            'from AudioProcessor.Process import Audio_Processing; '
            'from VPR.Identify import Voice_Identifying; '
            'from Whisper.Transcribe import Voice_Transcribing; '
            'from GPT_SoVITS.Create import Dataset_Creating; '
            'from GPT_SoVITS.Train import Train; '
            'from GPT_SoVITS.Convert import Convert; '
            'from VITS.Create import Dataset_Creating; '
            'from VITS.Train import Train; '
            'from VITS.Convert import Convert"'
        ],
        communicateThroughConsole = True,
        decodeResult = True,
        logPath = logPath
    )[1]
    if 'error' in str(error).lower():
        error += "（详情请见终端输出信息）"
        raise Exception(error)


def runTensorboard(logDir):
    """
    ClientFunc: run tensorboard
    """
    initialWaitTime = 0
    maximumWaitTime = 30
    while EasyUtils.getPaths(logDir, 'events.out.tfevents') == None:
        time.sleep(3)
        initialWaitTime += 3
        if initialWaitTime >= maximumWaitTime:
            break
    subprocess.Popen(['python', '-m', 'tensorboard.main', '--logdir', logDir], env = os.environ)
    time.sleep(9)
    QFunc.openURL('http://localhost:6006/')

##############################################################################################################################

# Show GUI
class MainWindow(Window_MainWindow):
    """
    Show the user interface
    """
    Signal_MainWindowShown = Signal()

    Signal_ModelView_Process_UVR = Signal(list)
    Signal_ModelView_VPR_TDNN = Signal(list)
    Signal_ModelView_ASR_Whisper = Signal(list)
    Signal_ModelView_TTS_GPTSoVITS = Signal(list)
    Signal_ModelView_TTS_VITS = Signal(list)

    def __init__(self):
        super().__init__()

        self.threadPool = QThreadPool()

        self.MonitorUsage = QTasks.MonitorUsage()
        self.MonitorUsage.start()

    def closeEvent(self, event):
        FunctionSignals.Signal_TaskStatus.connect(lambda: QApplication.instance().exit())
        FunctionSignals.Signal_ForceQuit.emit()

    def showGuidance(self, windowTitle: str, images: list, texts: list):
        stackedMsgBox = MessageBox_Stacked(self)
        stackedMsgBox.setWindowTitle(windowTitle)
        stackedMsgBox.setContent(images, texts)
        stackedMsgBox.exec()

    def _getFileDialog(self, widget, **kwargs):
        text = QFunc.getFileDialog(**kwargs)
        Function_SetParam(widget, text) if text != '' else None

    def viewModels(self):
        worker_modelView_Process_UVR = WorkerManager(
            executeMethod = getModelsInfo,
            executeParams = (
                manifestPath,
                EasyUtils.normPath(Path(modelDir).joinpath('Process', 'UVR')),
                ['pth', 'onnx']
            ),
            threadPool = self.threadPool,
        )
        worker_modelView_Process_UVR.signals.result.connect(self.Signal_ModelView_Process_UVR.emit)
        worker_modelView_Process_UVR.execute()

        worker_modelView_VPR_TDNN = WorkerManager(
            executeMethod = getModelsInfo,
            executeParams = (
                manifestPath,
                EasyUtils.normPath(Path(modelDir).joinpath('VPR', 'TDNN')),
                ['pth']
            ),
            threadPool = self.threadPool,
        )
        worker_modelView_VPR_TDNN.signals.result.connect(self.Signal_ModelView_VPR_TDNN.emit)
        worker_modelView_VPR_TDNN.execute()

        worker_modelView_ASR_Whisper = WorkerManager(
            executeMethod = getModelsInfo,
            executeParams = (
                manifestPath,
                EasyUtils.normPath(Path(modelDir).joinpath('ASR', 'Whisper')),
                ['pt']
            ),
            threadPool = self.threadPool,
        )
        worker_modelView_ASR_Whisper.signals.result.connect(self.Signal_ModelView_ASR_Whisper.emit)
        worker_modelView_ASR_Whisper.execute()

        worker_modelView_TTS_GPTSoVITS = WorkerManager(
            executeMethod = getModelsInfo,
            executeParams = (
                manifestPath,
                EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS')),
                ['pth', 'ckpt', 'bin', 'json']
            ),
            threadPool = self.threadPool,
        )
        worker_modelView_TTS_GPTSoVITS.signals.result.connect(self.Signal_ModelView_TTS_GPTSoVITS.emit)
        worker_modelView_TTS_GPTSoVITS.execute()

        worker_modelView_TTS_VITS = WorkerManager(
            executeMethod = getModelsInfo,
            executeParams = (
                manifestPath,
                EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'VITS')),
                ['pth', 'json']
            ),
            threadPool = self.threadPool,
        )
        worker_modelView_TTS_VITS.signals.result.connect(self.Signal_ModelView_TTS_VITS.emit)
        worker_modelView_TTS_VITS.execute()

    def appendModels(self):
        LineEdit_Models_Append = QLineEdit()
        DialogBox_Models_Append = MessageBox_Buttons(self)
        DialogBox_Models_Append.setText(QCA.translate('MainWindow', "请选择添加方式"))
        DialogBox_Models_Append.Button1.setText(QCA.translate('MainWindow', "模型文件目录（多文件）"))
        DialogBox_Models_Append.Button1.clicked.connect(
            lambda: (
                self._getFileDialog(
                    LineEdit_Models_Append,
                    mode = FileDialogMode.SelectFolder
                ),
                DialogBox_Models_Append.close(),
            )
        )
        DialogBox_Models_Append.Button2.setText(QCA.translate('MainWindow', "模型文件路径（单文件）"))
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
        dirPathSelectionDialogBox.setText(QCA.translate('MainWindow', "请选择参数类型"))
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

    def showVPRResult(self, audioSaveDir, audioSpeakersData_path, comboItems):
        ChildWindow_VPR = Window_ChildWindow_VPR(self)

        ChildWindow_VPR.ui.Button_Close.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认放弃编辑？",
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
                QCA.translate('ChildWindow_VPR', "语音识别结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_VPR.ui.Label_Text,
            text = EasyUtils.setRichText(
                QCA.translate('ChildWindow_VPR', "这里记录了每个语音文件与其对应的人物名（留空表示无匹配人物且最终不会被保留）\n你可以对这些人物名进行更改并在表格下方设置音频的保存路径")
            )
        )

        ChildWindow_VPR.ui.Table.setHorizontalHeaderLabels(['音频路径', '人物姓名', '相似度', '播放', '操作'])

        ChildWindow_VPR.ui.CheckBox.setText(QCA.translate('ChildWindow_VPR', "结束编辑时将拥有匹配人物的音频保存到:"))
        ChildWindow_VPR.ui.CheckBox.setChecked(True)
        ChildWindow_VPR.ui.LineEdit.clearDefaultStyleSheet()
        ChildWindow_VPR.ui.LineEdit.setStyleSheet(ChildWindow_VPR.ui.LineEdit.styleSheet() + 'LineEditBase {border-width: 0px 0px 1px 0px; border-radius: 0px;}')
        ChildWindow_VPR.ui.LineEdit.setText(audioSaveDir)
        ChildWindow_VPR.ui.LineEdit.setReadOnly(True)

        ChildWindow_VPR.ui.Button_Cancel.setText(QCA.translate('ChildWindow_VPR', "取消"))
        ChildWindow_VPR.ui.Button_Cancel.clicked.connect(ChildWindow_VPR.ui.Button_Close.click)
        ChildWindow_VPR.ui.Button_Save.setText(QCA.translate('ChildWindow_VPR', "保存"))
        ChildWindow_VPR.ui.Button_Save.clicked.connect(
            lambda: (
                VPRResult_Save(
                    ChildWindow_VPR.ui.Table.getValue(),
                    audioSpeakersData_path,
                    False
                ),
                MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "已保存当前结果。"
                )
            )
        )
        ChildWindow_VPR.ui.Button_Confirm.setText(QCA.translate('ChildWindow_VPR', "确认"))
        ChildWindow_VPR.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认结束并应用编辑？",
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
                text = "确认放弃编辑？",
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
                QCA.translate('ChildWindow_ASR', "语音转录结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_ASR.ui.Label_Text,
            text = EasyUtils.setRichText(
                QCA.translate('ChildWindow_ASR', "这里记录了每个语音文件与其对应的字幕文本（包含了时间戳）\n你可以对这些文本进行更改，若启用了语种标注则小心不要误删")
            )
        )

        ChildWindow_ASR.ui.Table.setHorizontalHeaderLabels(['音频路径', '音频内容', '播放'])

        ChildWindow_ASR.ui.Button_Cancel.setText(QCA.translate('ChildWindow_ASR', "取消"))
        ChildWindow_ASR.ui.Button_Cancel.clicked.connect(ChildWindow_ASR.ui.Button_Close.click)
        ChildWindow_ASR.ui.Button_Confirm.setText(QCA.translate('ChildWindow_ASR', "确认"))
        ChildWindow_ASR.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认应用编辑？",
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
                text = "确认放弃编辑？",
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
                QCA.translate('ChildWindow_DAT', "数据集制作结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_DAT.ui.Label_Text,
            text = EasyUtils.setRichText(
                QCA.translate('ChildWindow_DAT', "这里记录了每个语音文件与其对应的数据文本\n你可以对这些文本进行更改")
            )
        )

        ChildWindow_DAT.ui.Table_Train.setHorizontalHeaderLabels(['数据文本', '播放'])
        ChildWindow_DAT.ui.Table_Val.setHorizontalHeaderLabels(['数据文本', '播放'])

        ChildWindow_DAT.ui.Button_Cancel.setText(QCA.translate('ChildWindow_DAT', "取消"))
        ChildWindow_DAT.ui.Button_Cancel.clicked.connect(ChildWindow_DAT.ui.Button_Close.click)
        ChildWindow_DAT.ui.Button_Confirm.setText(QCA.translate('ChildWindow_DAT', "确认"))
        ChildWindow_DAT.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认应用编辑？",
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
                text = "确认退出试听？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS.ui.widget.releaseMediaPlayer(),
                        ChildWindow_TTS.close()
                    )
                } 
            )
        )
        ChildWindow_TTS.ui.Button_Maximize.clicked.connect(lambda: ChildWindow_TTS.showNormal() if ChildWindow_TTS.isMaximized() else ChildWindow_TTS.showMaximized())

        QFunc.setText(
            widget = ChildWindow_TTS.ui.Label_Title,
            text = EasyUtils.setRichText(
                QCA.translate('ChildWindow_TTS', "语音合成结果"),
                size = 12
            )
        )
        QFunc.setText(
            widget = ChildWindow_TTS.ui.Label_Text,
            text = EasyUtils.setRichText(
                QCA.translate('ChildWindow_TTS', "点击播放按钮以试听合成语音")
            )
        )

        ChildWindow_TTS.ui.Button_Cancel.setText(QCA.translate('ChildWindow_TTS', "丢弃"))
        ChildWindow_TTS.ui.Button_Cancel.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认丢弃音频？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS.ui.widget.releaseMediaPlayer(),
                        os.remove(mediaPath),
                        ChildWindow_TTS.close()
                    )
                }
            )
        )
        ChildWindow_TTS.ui.Button_Confirm.setText(QCA.translate('ChildWindow_TTS', "保留"))
        ChildWindow_TTS.ui.Button_Confirm.clicked.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "确认保留音频？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {
                    QMessageBox.Yes: lambda: (
                        ChildWindow_TTS.ui.widget.releaseMediaPlayer(),
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

        ChildWindow_TTS.ui.widget.setMediaPlayer(
            mediaPath
        )
        ChildWindow_TTS.exec()

    def chkUpdate(self, runUpdateChecker: bool):
        recordedVersion = deprecatedVersion or config.getValue('Info', 'RecordedVersion', currentVersion)
        if not EasyUtils.isVersionSatisfied(recordedVersion, currentVersion):
            deprecatedDir = Path(resourceDir).parent.joinpath(recordedVersion).as_posix()
            time.sleep(3)
            try:
                shutil.rmtree(deprecatedDir)
            except:
                pass
            else:
                config.editConfig('Info', 'RecordedVersion', currentVersion)

        FunctionSignals.Signal_ReadyToUpdate.connect(
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
        ComponentsSignals.Signal_SetTheme.connect(
            lambda: self.ui.CheckBox_SwitchTheme.setChecked(
                {Theme.Light: True, Theme.Dark: False}.get(currentTheme())
            )
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_SwitchTheme,
            checkedEvents = {
                lambda: config.editConfig('Settings', 'Theme', Theme.Light): False,
                lambda: ComponentsSignals.Signal_SetTheme.emit(Theme.Light) if currentTheme() != Theme.Light else None : False
            },
            uncheckedEvents = {
                lambda: config.editConfig('Settings', 'Theme', Theme.Dark) : False,
                lambda: ComponentsSignals.Signal_SetTheme.emit(Theme.Dark) if currentTheme() != Theme.Dark else None : False
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
        self.ui.Button_Toggle_Menu.setToolTip(QCA.translate('MainWindow', "点击以展开/折叠菜单"))

        #############################################################
        ############################ Menu ###########################
        #############################################################

        self.ui.Button_Menu_Home.setText(QCA.translate('MainWindow', "主页"))
        self.ui.Button_Menu_Home.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 0
            )
        )
        self.ui.Button_Menu_Home.setChecked(True)
        self.ui.Button_Menu_Home.setToolTip(QCA.translate('MainWindow', "主页"))

        self.ui.Button_Menu_Env.setText(QCA.translate('MainWindow', "环境"))
        self.ui.Button_Menu_Env.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 1
            )
        )
        self.ui.Button_Menu_Env.setChecked(False)
        self.ui.Button_Menu_Env.setToolTip(QCA.translate('MainWindow', "环境配置"))

        self.ui.Button_Menu_Models.setText(QCA.translate('MainWindow', "模型"))
        self.ui.Button_Menu_Models.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 2
            )
        )
        self.ui.Button_Menu_Models.setChecked(False)
        self.ui.Button_Menu_Models.setToolTip(QCA.translate('MainWindow', "模型管理"))

        self.ui.Button_Menu_Process.setText(QCA.translate('MainWindow', "处理"))
        self.ui.Button_Menu_Process.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 3
            )
        )
        self.ui.Button_Menu_Process.setChecked(False)
        self.ui.Button_Menu_Process.setToolTip(QCA.translate('MainWindow', "工具：音频处理"))

        self.ui.Button_Menu_VPR.setText(QCA.translate('MainWindow', "识别"))
        self.ui.Button_Menu_VPR.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 4
            )
        )
        self.ui.Button_Menu_VPR.setChecked(False)
        self.ui.Button_Menu_VPR.setToolTip(QCA.translate('MainWindow', "工具：语音识别"))

        self.ui.Button_Menu_ASR.setText(QCA.translate('MainWindow', "转录"))
        self.ui.Button_Menu_ASR.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 5
            )
        )
        self.ui.Button_Menu_ASR.setChecked(False)
        self.ui.Button_Menu_ASR.setToolTip(QCA.translate('MainWindow', "工具：语音转文字"))

        self.ui.Button_Menu_Dataset.setText(QCA.translate('MainWindow', "数据"))
        self.ui.Button_Menu_Dataset.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 6
            )
        )
        self.ui.Button_Menu_Dataset.setChecked(False)
        self.ui.Button_Menu_Dataset.setToolTip(QCA.translate('MainWindow', "工具：数据集制作"))

        self.ui.Button_Menu_Train.setText(QCA.translate('MainWindow', "训练"))
        self.ui.Button_Menu_Train.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 7
            )
        )
        self.ui.Button_Menu_Train.setChecked(False)
        self.ui.Button_Menu_Train.setToolTip(QCA.translate('MainWindow', "工具：模型训练"))

        self.ui.Button_Menu_TTS.setText(QCA.translate('MainWindow', "合成"))
        self.ui.Button_Menu_TTS.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 8
            )
        )
        self.ui.Button_Menu_TTS.setChecked(False)
        self.ui.Button_Menu_TTS.setToolTip(QCA.translate('MainWindow', "工具：语音合成"))

        self.ui.Button_Menu_Settings.setText(QCA.translate('MainWindow', "设置"))
        self.ui.Button_Menu_Settings.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 9
            )
        )
        self.ui.Button_Menu_Settings.setChecked(False)
        self.ui.Button_Menu_Settings.setToolTip(QCA.translate('MainWindow', "客户端设置"))

        self.ui.Button_Menu_Info.setText(QCA.translate('MainWindow', "关于"))
        self.ui.Button_Menu_Info.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages,
                target = 10
            )
        )
        self.ui.Button_Menu_Info.setChecked(False)
        self.ui.Button_Menu_Info.setToolTip(QCA.translate('MainWindow', "关于本软件"))

        #############################################################
        ####################### Content: Home #######################
        #############################################################

        self.ui.Label_Cover_Home.setPixmap(QPixmap(Path(resourceDir).joinpath('assets/images/others/Cover.png')))

        QFunc.setText(
            widget = self.ui.TextBrowser_Text_Home,
            text = EasyUtils.richTextManager().addTitle(
                text = QCA.translate('MainWindow', "介绍"),
                align = "left",
                size = 24,
                weight = 840,
            ).addBody(
                text = QCA.translate('MainWindow',
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
                align = "left",
                size = 12,
                weight = 420,
                lineHeight = 27
            ).richText()
        )

        self.ui.Label_Demo_Text.setText(QCA.translate('MainWindow', "视频演示"))
        Function_SetURL(
            button = self.ui.Button_Demo,
            url = "https://www.bilibili.com/video/BV",
            buttonTooltip = "Click to view demo video"
        )
        self.ui.Label_Server_Text.setText(QCA.translate('MainWindow', "云端版本"))
        Function_SetURL(
            button = self.ui.Button_Server,
            url = "https://colab.research.google.com/github/Spr-Aachen/EVT-Reassets/images/others/blob/main/Easy_Voice_Toolkit_for_Colab.ipynb",
            buttonTooltip = "Click to run on server"
        )
        self.ui.Label_Repo_Text.setText(QCA.translate('MainWindow', "项目仓库"))
        Function_SetURL(
            button = self.ui.Button_Repo,
            url = "https://github.com/Spr-Aachen/Easy-Voice-Toolkit",
            buttonTooltip = "Click to view github repo"
        )
        self.ui.Label_Donate_Text.setText(QCA.translate('MainWindow', "赞助作者"))
        Function_SetURL(
            button = self.ui.Button_Donate,
            url = "https://afdian.tv/a/Spr_Aachen/plan",
            buttonTooltip = "Click to buy author a coffee"
        )

        #############################################################
        ##################### Content: Environ ######################
        #############################################################

        # EnvInstallation
        subEnvPage_detection = SubEnvPage_Detector(self.ui.Page_Env)
        subEnvPage_detection.addDetectorFrame(
            text = QCA.translate('MainWindow', "Aria2"),
            toolTip = QCA.translate('MainWindow', "重新检测安装"),
            detectMethod = Aria2_Installer.execute,
            terminateMethod = Aria2_Installer.terminate,
            threadPool = self.threadPool,
            signal_detect = self.Signal_MainWindowShown,
            signal_detected = EnvConfiguratorSignals.Signal_Aria2Detected,
            signal_undetected = EnvConfiguratorSignals.Signal_Aria2Undetected,
            statusSignal = EnvConfiguratorSignals.Signal_Aria2Status,
        )
        EnvConfiguratorSignals.Signal_Aria2Installed.connect(#self.ui.Button_Install_Aria2.click)
            lambda: EnvConfiguratorSignals.Signal_Aria2Detected.emit()
        )
        EnvConfiguratorSignals.Signal_Aria2InstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = f"安装Aria2出错",
                detailedText = str(Exception)
            )
        )
        subEnvPage_detection.addDetectorFrame(
            text = QCA.translate('MainWindow', "FFmpeg"),
            toolTip = QCA.translate('MainWindow', "重新检测安装"),
            detectMethod = FFmpeg_Installer.execute,
            terminateMethod = FFmpeg_Installer.terminate,
            threadPool = self.threadPool,
            signal_detect = self.Signal_MainWindowShown,
            signal_detected = EnvConfiguratorSignals.Signal_FFmpegDetected,
            signal_undetected = EnvConfiguratorSignals.Signal_FFmpegUndetected,
            statusSignal = EnvConfiguratorSignals.Signal_FFmpegStatus,
        )
        EnvConfiguratorSignals.Signal_FFmpegInstalled.connect(#self.ui.Button_Install_FFmpeg.click)
            lambda: EnvConfiguratorSignals.Signal_FFmpegDetected.emit()
        )
        EnvConfiguratorSignals.Signal_FFmpegInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = f"安装FFmpeg出错",
                detailedText = str(Exception)
            )
        )
        subEnvPage_detection.addDetectorFrame(
            text = QCA.translate('MainWindow', "Python"),
            toolTip = QCA.translate('MainWindow', "重新检测安装"),
            detectMethod = Python_Installer.execute,
            params = ('3.9.0'),
            terminateMethod = Python_Installer.terminate,
            threadPool = self.threadPool,
            signal_detect = self.Signal_MainWindowShown,
            signal_detected = EnvConfiguratorSignals.Signal_PythonDetected,
            signal_undetected = EnvConfiguratorSignals.Signal_PythonUndetected,
            statusSignal = EnvConfiguratorSignals.Signal_PythonStatus,
        )
        EnvConfiguratorSignals.Signal_PythonInstalled.connect(#self.ui.Button_Install_Python.click)
            lambda: EnvConfiguratorSignals.Signal_PythonDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PythonInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = f"安装Python出错",
                detailedText = str(Exception)
            )
        )
        subEnvPage_detection.addDetectorFrame(
            text = QCA.translate('MainWindow', "Python 依赖库 (Requirements)"),
            toolTip = QCA.translate('MainWindow', "重新检测安装"),
            detectMethod = PyReqs_Installer.execute,
            params = (EasyUtils.normPath(requirementsPath)),
            terminateMethod = PyReqs_Installer.terminate,
            threadPool = self.threadPool,
            signal_detect = EnvConfiguratorSignals.Signal_PythonDetected,
            signal_detected = EnvConfiguratorSignals.Signal_PyReqsDetected,
            signal_undetected = EnvConfiguratorSignals.Signal_PyReqsUndetected,
            statusSignal = EnvConfiguratorSignals.Signal_PyReqsStatus,
        )
        EnvConfiguratorSignals.Signal_PyReqsInstalled.connect(#self.ui.Button_Install_PyReqs.click)
            lambda: EnvConfiguratorSignals.Signal_PyReqsDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PyReqsInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = f"安装Python依赖库出错",
                detailedText = str(Exception)
            )
        )
        subEnvPage_detection.addDetectorFrame(
            text = QCA.translate('MainWindow', "Pytorch 相关库"),
            toolTip = QCA.translate('MainWindow', "重新检测安装"),
            detectMethod = Pytorch_Installer.execute,
            terminateMethod = Pytorch_Installer.terminate,
            threadPool = self.threadPool,
            signal_detect = EnvConfiguratorSignals.Signal_PyReqsDetected,
            signal_detected = EnvConfiguratorSignals.Signal_PytorchDetected,
            signal_undetected = EnvConfiguratorSignals.Signal_PytorchUndetected,
            statusSignal = EnvConfiguratorSignals.Signal_PytorchStatus,
        )
        EnvConfiguratorSignals.Signal_PytorchInstalled.connect(#self.ui.Button_Install_Pytorch.click)
            lambda: EnvConfiguratorSignals.Signal_PytorchDetected.emit()
        )
        EnvConfiguratorSignals.Signal_PytorchInstallFailed.connect(
            lambda Exception: MessageBoxBase.pop(self,
                QMessageBox.Warning, "Warning",
                text = f"安装Pytorch出错",
                detailedText = str(Exception)
            )
        )

        self.ui.Page_Env.addSubPage(
            QCA.translate('MainWindow', "自动配置"), subEnvPage_detection
        )

        # EnvManagement
        subEnvPage_manager = SubEnvPage_Manager(self.ui.Page_Env)
        subEnvPage_manager.addComboBoxFrame(
            toolBoxText = QCA.translate('MainWindow', "Pytorch"),
            text = QCA.translate('MainWindow', "选择Pytorch版本"),
            items = [ '2.0.1', '2.2.2'],
            executorText = QCA.translate('MainWindow', "安装"),
            executeMethod = Pytorch_Installer.execute,
            terminateMethod = Pytorch_Installer.terminate,
            executeParamTargets = [
                lambda: subEnvPage_manager.findChildWidget(None, "Pytorch", "选择Pytorch版本", QComboBox),
                True
            ],
            threadPool = self.threadPool,
        )

        self.ui.Page_Env.addSubPage(
            QCA.translate('MainWindow', "安装管理"), subEnvPage_manager
        )

        #############################################################
        ####################### Content: Models #####################
        #############################################################

        self.Signal_MainWindowShown.connect(self.viewModels)

        self.ui.Button_Models_Process_Title.setText(QCA.translate('MainWindow', '基本处理'))
        self.ui.Button_Models_Process_Title.setHorizontal(True)
        self.ui.Button_Models_Process_Title.setChecked(True)
        self.ui.Button_Models_Process_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 0
            )
        )
        self.ui.Button_Models_Process_Title.setToolTip(QCA.translate('MainWindow', "基本处理模型"))

        self.ui.TabWidget_Models_Process.setTabText(0, 'UVR（人声分离）')
        self.ui.Table_Models_Process_UVR.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        self.Signal_ModelView_Process_UVR.connect(self.ui.Table_Models_Process_UVR.setValue)
        self.ui.Table_Models_Process_UVR.Download.connect(
            lambda params: Function_SetMethodExecutor(
                executeMethod = downloadModel,
                executeParams = params,
                threadPool = self.threadPool,
                parentWindow = self,
            )
        )

        self.ui.Button_Models_VPR_Title.setText(QCA.translate('MainWindow', 'VPR（识别）'))
        self.ui.Button_Models_VPR_Title.setHorizontal(True)
        self.ui.Button_Models_VPR_Title.setChecked(False)
        self.ui.Button_Models_VPR_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 1
            )
        )
        self.ui.Button_Models_VPR_Title.setToolTip(QCA.translate('MainWindow', "语音识别模型"))

        self.ui.TabWidget_Models_VPR.setTabText(0, 'VPR（声纹识别）')
        self.ui.Table_Models_VPR_TDNN.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        self.Signal_ModelView_VPR_TDNN.connect(self.ui.Table_Models_VPR_TDNN.setValue)
        self.ui.Table_Models_VPR_TDNN.Download.connect(
            lambda params: Function_SetMethodExecutor(
                executeMethod = downloadModel,
                executeParams = params,
                threadPool = self.threadPool,
                parentWindow = self,
            )
        )

        self.ui.Button_Models_ASR_Title.setText(QCA.translate('MainWindow', 'ASR（转录）'))
        self.ui.Button_Models_ASR_Title.setHorizontal(True)
        self.ui.Button_Models_ASR_Title.setChecked(False)
        self.ui.Button_Models_ASR_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 2
            )
        )
        self.ui.Button_Models_ASR_Title.setToolTip(QCA.translate('MainWindow', "语音转录模型"))

        self.ui.TabWidget_Models_ASR.setTabText(0, 'Whisper')
        self.ui.Table_Models_ASR_Whisper.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        self.Signal_ModelView_ASR_Whisper.connect(self.ui.Table_Models_ASR_Whisper.setValue)
        self.ui.Table_Models_ASR_Whisper.Download.connect(
            lambda params: Function_SetMethodExecutor(
                executeMethod = downloadModel,
                executeParams = params,
                threadPool = self.threadPool,
                parentWindow = self,
            )
        )

        self.ui.Button_Models_TTS_Title.setText(QCA.translate('MainWindow', 'TTS（合成）'))
        self.ui.Button_Models_TTS_Title.setHorizontal(True)
        self.ui.Button_Models_TTS_Title.setChecked(False)
        self.ui.Button_Models_TTS_Title.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Models,
                target = 3
            )
        )
        self.ui.Button_Models_TTS_Title.setToolTip(QCA.translate('MainWindow', "语音合成模型"))

        self.ui.TabWidget_Models_TTS.setTabText(0, 'GPT-SoVITS')
        self.ui.Table_Models_TTS_GPTSoVITS.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        self.Signal_ModelView_TTS_GPTSoVITS.connect(self.ui.Table_Models_TTS_GPTSoVITS.setValue)
        self.ui.Table_Models_TTS_GPTSoVITS.Download.connect(
            lambda params: Function_SetMethodExecutor(
                executeMethod = downloadModel,
                executeParams = params,
                threadPool = self.threadPool,
                parentWindow = self,
            )
        )

        self.ui.TabWidget_Models_TTS.setTabText(1, 'VITS')
        self.ui.Table_Models_TTS_VITS.setHorizontalHeaderLabels(['名字', '类型', '大小', '日期', '操作'])
        self.Signal_ModelView_TTS_VITS.connect(self.ui.Table_Models_TTS_VITS.setValue)
        self.ui.Table_Models_TTS_VITS.Download.connect(
            lambda params: Function_SetMethodExecutor(
                executeMethod = downloadModel,
                executeParams = params,
                threadPool = self.threadPool,
                parentWindow = self,
            )
        )

        self.ui.Button_Models_Refresh.setText(QCA.translate('MainWindow', '刷新'))
        self.ui.Button_Models_Refresh.clicked.connect(self.viewModels)

        self.ui.Button_Models_Append.setText(QCA.translate('MainWindow', '添加'))
        self.ui.Button_Models_Append.clicked.connect(self.appendModels)

        #############################################################
        ###################### Content: Process #####################
        #############################################################

        # Guidance
        self.ui.Page_Process.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = QCA.translate('MainWindow', "引导（仅出现一次）"),
                images = [
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Process.png')),
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                texts = [
                    '欢迎来到音频处理工具界面\n该工具用于将媒体文件批量转换为音频文件并进行降噪、静音切除等操作',
                    '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
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

        subPage_process = SubToolPage(self.ui.Page_Process, paramsManager_process)
        subPage_process.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "媒体输入目录\n需要处理的音频文件的所在目录。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            section = 'Input params',
            option = 'Media_Dir_Input',
            defaultValue = ''
        )
        subPage_process.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "降噪参数"),
            text = QCA.translate('MainWindow', "启用杂音去除\n弱化音频中的非人声部分。"),
            section = 'Denoiser params',
            option = 'Denoise_Audio',
            defaultValue = True
        )
        subPage_process.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "降噪参数"),
            text = QCA.translate('MainWindow', "uvr5模型路径\n用于uvr5降噪的模型文件的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型/onnx类型 (*.pth *.onnx)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('Process', 'UVR', 'Downloaded')),
            section = 'Denoiser params',
            option = 'Denoise_Model_Path',
            defaultValue = Path(modelDir).joinpath('Process', 'UVR', 'Downloaded', 'HP5_only_main_vocal.pth').as_posix()
        )
        subPage_process.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "降噪参数"),
            text = QCA.translate('MainWindow', "提取目标\n选择在降噪时要保留的声音对象。"),
            items = [QCA.translate('MainWindow', '人声'), QCA.translate('MainWindow', '背景声')],
            section = 'Denoiser params',
            option = 'Denoise_Target',
            defaultValue = '人声'
        )
        subPage_process.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            text = QCA.translate('MainWindow', "启用静音切除\n切除音频中的静音部分。"),
            section = 'Slicer params',
            option = 'Slice_Audio',
            defaultValue = True
        )
        subPage_process.addDoubleSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "均方根阈值 (db)\n低于该阈值的片段将被视作静音进行处理，若有降噪需求可以增加该值。"),
            minimum = -100, maximum = 0,
            section = 'Slicer params',
            option = 'RMS_Threshold',
            defaultValue = -34.
        )
        subPage_process.addSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "跃点大小 (ms)\n每个RMS帧的长度，增加该值能够提高分割精度但会减慢进程。"),
            minimum = 0, maximum = 100, step = 1,
            section = 'Slicer params',
            option = 'Hop_Size',
            defaultValue = 10
        )
        subPage_process.addSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "最小静音间隔 (ms)\n静音部分被分割成的最小长度，若音频只包含短暂中断可以减小该值。"),
            toolTip = QCA.translate('MainWindow', "注意：这个值必须小于最小音频长度，大于跃点大小。"),
            minimum = 0, maximum = 3000, step = 1,
            section = 'Slicer params',
            option = 'Silent_Interval_Min',
            defaultValue = 300
        )
        subPage_process.addSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "最大静音长度 (ms)\n被分割的音频周围保持静音的最大长度。"),
            toolTip = QCA.translate('MainWindow', "注意：这个值无需完全对应被分割音频中的静音长度。算法将自行检索最佳的分割位置。"),
            minimum = 0, maximum = 10000, step = 1,
            section = 'Slicer params',
            option = 'Silence_Kept_Max',
            defaultValue = 500
        )
        subPage_process.addSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "静音切除参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "最小音频长度 (ms)\n每个被分割的音频片段所需的最小长度。"),
            minimum = 300, maximum = 30000, step = 1,
            section = 'Slicer params',
            option = 'Audio_Length_Min',
            defaultValue = 4000
        )
        subPage_process.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            text = QCA.translate('MainWindow', "媒体输出格式\n媒体文件输出为音频文件的格式，若维持不变则保持'None'即可。"),
            items = ['flac', 'wav', 'mp3', 'aac', 'm4a', 'wma', 'aiff', 'au', 'ogg', 'None'],
            section = 'Output params',
            option = 'Media_Format_Output',
            defaultValue = 'wav'
        )
        subPage_process.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            text = QCA.translate('MainWindow', "输出目录名\n用于保存最后生成的音频文件的目录的名字。"),
            section = 'Output params',
            option = 'Output_Dir_Name',
            defaultValue = '',
            placeholderText = str(date.today())
        )
        LineEdit_Process_OutputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = subPage_process.findChildWidget("输出参数", None, "输出目录名", LineEditBase),
            rootEdit = self.ui.LineEdit_Process_OutputRoot,
            dirEdit = LineEdit_Process_OutputDir
        )
        subPage_process.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "合并声道\n将输出音频的声道合并为单声道。"),
            section = 'Output params',
            option = 'ToMono',
            defaultValue = False,
            emptyAllowed = True
        )
        subPage_process.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "输出采样率\n输出音频所拥有的采样率，若维持不变则保持'None'即可。"),
            items = ['22050', '44100', '48000', '96000', '192000', 'None'],
            section = 'Output params',
            option = 'SampleRate',
            defaultValue = None,
            emptyAllowed = True
        )
        subPage_process.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "输出采样位数\n输出音频所拥有的采样位数，若维持不变则保持'None'即可。"),
            items = ['8', '16', '24', '32', '32 (Float)', 'None'],
            section = 'Output params',
            option = 'SampleWidth',
            defaultValue = None,
            emptyAllowed = True
        )
        subPage_process.addChkOutputSideBtn(
            outputRootEdit = self.ui.LineEdit_Process_OutputRoot,
        )
        self.task_audioProcessing = Execute_Audio_Processing(coreDir, logPath)
        subPage_process.setExecutor(
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_audioProcessing.execute,
            executeParamTargets = [
                subPage_process.findChildWidget("输入参数", None, "媒体输入目录"),
                subPage_process.findChildWidget("输出参数", None, "媒体输出格式"),
                subPage_process.findChildWidget("输出参数", "高级设置", "输出采样率"),
                subPage_process.findChildWidget("输出参数", "高级设置", "输出采样位数"),
                subPage_process.findChildWidget("输出参数", "高级设置", "合并声道"),
                subPage_process.findChildWidget("降噪参数", None, "启用杂音去除"),
                subPage_process.findChildWidget("降噪参数", None, "uvr5模型路径"),
                subPage_process.findChildWidget("降噪参数", None, "提取目标"),
                subPage_process.findChildWidget("静音切除参数", None, "启用静音切除"),
                subPage_process.findChildWidget("静音切除参数", "高级设置", "均方根阈值 (db)"),
                subPage_process.findChildWidget("静音切除参数", "高级设置", "最小音频长度 (ms)"),
                subPage_process.findChildWidget("静音切除参数", "高级设置", "最小静音间隔 (ms)"),
                subPage_process.findChildWidget("静音切除参数", "高级设置", "跃点大小 (ms)"),
                subPage_process.findChildWidget("静音切除参数", "高级设置", "最大静音长度 (ms)"),
                self.ui.LineEdit_Process_OutputRoot,
                subPage_process.findChildWidget("输出参数", None, "输出目录名")
            ],
            terminateMethod = self.task_audioProcessing.terminate,
            finishedEvents = {
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool,
        )
        Function_ConfigureCheckBox(
            checkBox = subPage_process.findChildWidget("降噪参数", None, "启用杂音去除", QCheckBox),
            checkedEvents = {
                lambda: Function_SetChildWidgetsVisibility(
                    container = subPage_process.findChildWidget("降噪参数"),
                    childWidgetsVisibility = {
                        subPage_process.findChildWidget("降噪参数", None, "uvr5模型路径"): True,
                        subPage_process.findChildWidget("降噪参数", None, "提取目标"): True,
                    },
                ) : True
            },
            uncheckedEvents = {
                lambda: Function_SetChildWidgetsVisibility(
                    container = subPage_process.findChildWidget("降噪参数"),
                    childWidgetsVisibility = {
                        subPage_process.findChildWidget("降噪参数", None, "uvr5模型路径"): False,
                        subPage_process.findChildWidget("降噪参数", None, "提取目标"): False,
                    },
                ) : True
            },
        )
        Function_ConfigureCheckBox(
            checkBox = subPage_process.findChildWidget("静音切除参数", None, "启用静音切除", QCheckBox),
            checkedEvents = {
                lambda: Function_SetChildWidgetsVisibility(
                    container = subPage_process.findChildWidget("静音切除参数", "高级设置"),
                    childWidgetsVisibility = {
                        subPage_process.findChildWidget("静音切除参数", "高级设置", "均方根阈值 (db)"): True,
                        subPage_process.findChildWidget("静音切除参数", "高级设置", "跃点大小 (ms)"): True,
                        subPage_process.findChildWidget("静音切除参数", "高级设置", "最小静音间隔 (ms)"): True,
                        subPage_process.findChildWidget("静音切除参数", "高级设置", "最大静音长度 (ms)"): True,
                        subPage_process.findChildWidget("静音切除参数", "高级设置", "最小音频长度 (ms)"): True,
                    },
                ) : True
            },
            uncheckedEvents = {
                lambda: Function_SetChildWidgetsVisibility(
                    container = subPage_process.findChildWidget("静音切除参数", "高级设置"),
                    childWidgetsVisibility = {
                        subPage_process.findChildWidget("静音切除参数", "高级设置", "均方根阈值 (db)"): False,
                        subPage_process.findChildWidget("静音切除参数", "高级设置", "跃点大小 (ms)"): False,
                        subPage_process.findChildWidget("静音切除参数", "高级设置", "最小静音间隔 (ms)"): False,
                        subPage_process.findChildWidget("静音切除参数", "高级设置", "最大静音长度 (ms)"): False,
                        subPage_process.findChildWidget("静音切除参数", "高级设置", "最小音频长度 (ms)"): False,
                    },
                ) : True
            },
        )

        self.ui.Page_Process.addSubPage(
            QCA.translate('MainWindow', '音频基本处理'), subPage_process
        )

        #############################################################
        ######################## Content: VPR #######################
        #############################################################

        # Guidance
        self.ui.Page_VPR.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = QCA.translate('MainWindow', "引导（仅出现一次）"),
                images = [
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_VPR.png')),
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                texts = [
                    '欢迎来到语音识别工具界面\n该工具用于从不同说话人的音频中批量筛选出属于同一说话人的音频',
                    '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
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
        configPath_VPR_TDNN = EasyUtils.normPath(Path(configDir).joinpath('config_VPR_TDNN.ini'))
        paramsManager_VPR_TDNN = ParamsManager(configPath_VPR_TDNN)

        subPage_VPR = SubToolPage(self.ui.Page_VPR, paramsManager_VPR_TDNN)
        subPage_VPR.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "音频输入目录\n需要进行语音识别筛选的音频文件的所在目录。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = Path(currentDir).joinpath('音频处理结果').as_posix(),
            section = 'Input params',
            option = 'Audio_Dir_Input',
            defaultValue = '',
        )
        subPage_VPR.addEditAudioSpeakerTableFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "目标人物与音频\n目标人物的名字及其语音文件的路径。"),
            headerLabels = ['人物姓名', '音频路径', '增删'],
            fileType = "音频类型 (*.flac *.wav *.mp3 *.aac *.m4a *.wma *.aiff *.au *.ogg)",
            section = 'Input params',
            option = 'StdAudioSpeaker',
            defaultValue = {"": ""}
        )
        subPage_VPR.addDoubleSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "语音识别参数"),
            text = QCA.translate('MainWindow', "判断阈值\n判断相似度的阈值，若参与比对的说话人声音相似度较高可以增加该值。"),
            minimum = 0.5,
            maximum = 1,
            step = 0.01,
            section = 'VPR params',
            option = 'DecisionThreshold',
            defaultValue = 0.75
        )
        VPR_TDNN_ModelPath_Default = Path(modelDir).joinpath('VPR', 'TDNN', 'Downloaded', 'Ecapa-Tdnn_spectrogram.pth').as_posix()
        subPage_VPR.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "语音识别参数"),
            text = QCA.translate('MainWindow', "模型加载路径\n用于加载的声纹识别模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('VPR', 'TDNN', 'Downloaded')),
            section = 'VPR params',
            option = 'Model_Path',
            defaultValue = VPR_TDNN_ModelPath_Default,
            placeholderText = VPR_TDNN_ModelPath_Default
        )
        subPage_VPR.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "语音识别参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "模型类型\n声纹识别模型的类型。"),
            items = ['Ecapa-Tdnn'],
            section = 'VPR params',
            option = 'Model_Type',
            defaultValue = 'Ecapa-Tdnn'
        )
        subPage_VPR.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "语音识别参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "预处理方法\n音频的预处理方法。"),
            items = ['spectrogram', 'melspectrogram'],
            section = 'VPR params',
            option = 'Feature_Method',
            defaultValue = 'spectrogram'
        )
        subPage_VPR.addDoubleSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "语音识别参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "音频长度\n用于预测的音频长度。"),
            minimum = 0,
            maximum = 30,
            #step = 0.01,
            section = 'VPR params',
            option = 'Duration_of_Audio',
            defaultValue = 3.00
        )
        VPR_TDNN_OutputDirName_Default = str(date.today())
        subPage_VPR.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            text = QCA.translate('MainWindow', "输出目录名\n用于保存最后生成的结果文件的目录的名字。"),
            section = 'Output params',
            option = 'Audio_Dir_Output',
            defaultValue = '',
            placeholderText = VPR_TDNN_OutputDirName_Default
        )
        LineEdit_VPR_TDNN_OutputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = subPage_VPR.findChildWidget("输出参数", None, "输出目录名", LineEditBase),
            rootEdit = self.ui.LineEdit_VPR_TDNN_OutputRoot,
            dirEdit = LineEdit_VPR_TDNN_OutputDir
        )
        VPR_TDNN_AudioSpeakersDataName_Default = "Recgonition_" + str(date.today())
        subPage_VPR.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "识别结果文本名\n用于保存最后生成的记录音频文件与对应说话人的txt文件的名字。"),
            section = 'Output params',
            option = 'FileList_Name',
            defaultValue = VPR_TDNN_AudioSpeakersDataName_Default,
            placeholderText = VPR_TDNN_AudioSpeakersDataName_Default
        )
        LineEdit_VPR_TDNN_AudioSpeakersDataPath = LineEditBase()
        self.setPathAlert(
            fileNameEdit = subPage_VPR.findChildWidget("输出参数", "高级设置", "识别结果文本名", LineEditBase),
            dirEdit = LineEdit_VPR_TDNN_OutputDir,
            suffix = ".txt",
            fileEdit = LineEdit_VPR_TDNN_AudioSpeakersDataPath
        )
        subPage_VPR.addChkOutputSideBtn(
            outputRootEdit = self.ui.LineEdit_VPR_TDNN_OutputRoot,
        )
        def EditVPRResult():
            VPRResultPath = QFunc.getFileDialog(
                mode = FileDialogMode.SelectFile,
                fileType = "txt类型 (*.txt)",
                directory = Path(currentDir).joinpath('语音识别结果', 'VPR').as_posix()
            )
            if EasyUtils.normPath(VPRResultPath) is not None:
                self.showMask(True, "正在加载表单")
                self.showVPRResult(
                    LineEdit_VPR_TDNN_OutputDir.text(),
                    VPRResultPath,
                    None
                )
        subPage_VPR.addSideBtn(
            text = QCA.translate('MainWindow', "编辑识别结果"),
            events = [
                EditVPRResult
            ]
        )
        self.task_voiceIdentifying_vpr = Execute_Voice_Identifying_VPR(coreDir, logPath)
        subPage_VPR.setExecutor(
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_voiceIdentifying_vpr.execute,
            executeParamTargets = [
                subPage_VPR.findChildWidget("输入参数", None, "目标人物与音频"),
                subPage_VPR.findChildWidget("输入参数", None, "音频输入目录"),
                subPage_VPR.findChildWidget("语音识别参数", None, "模型加载路径"),
                subPage_VPR.findChildWidget("语音识别参数", "高级设置", "模型类型"),
                subPage_VPR.findChildWidget("语音识别参数", "高级设置", "预处理方法"),
                subPage_VPR.findChildWidget("语音识别参数", None, "判断阈值"),
                subPage_VPR.findChildWidget("语音识别参数", "高级设置", "音频长度"),
                self.ui.LineEdit_VPR_TDNN_OutputRoot,
                subPage_VPR.findChildWidget("输出参数", None, "输出目录名"),
                subPage_VPR.findChildWidget("输出参数", "高级设置", "识别结果文本名")
            ],
            terminateMethod = self.task_voiceIdentifying_vpr.terminate,
            finishedEvents = {
                lambda: self.showMask(True, "正在加载表单"): TaskStatus.Succeeded,
                lambda: self.showVPRResult(
                    LineEdit_VPR_TDNN_OutputDir.text(),
                    LineEdit_VPR_TDNN_AudioSpeakersDataPath.text(),
                    list(subPage_VPR.findChildWidget("输入参数", None, "目标人物与音频", TableBase).getValue().keys()) + ['']
                ): TaskStatus.Succeeded,
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool,
        )

        self.ui.Page_VPR.addSubPage(
            QCA.translate('MainWindow', 'VPR（声纹识别）'), subPage_VPR
        )

        #############################################################
        ######################## Content: ASR #######################
        #############################################################

        # Guidance
        self.ui.Page_ASR.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = QCA.translate('MainWindow', "引导（仅出现一次）"),
                images = [
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_ASR.png')),
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                texts = [
                    '欢迎来到语音转录工具界面\n该工具用于将语音文件批量转换为字幕文件并进行语言标注等操作',
                    '顶部区域用于切换当前工具类型\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
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
        configPath_ASR_Whisper = EasyUtils.normPath(Path(configDir).joinpath('Config_ASR_Whisper.ini'))
        paramsManager_ASR_Whisper = ParamsManager(configPath_ASR_Whisper)

        subPage_ASR = SubToolPage(self.ui.Page_ASR, paramsManager_ASR_Whisper)
        subPage_ASR.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "音频输入目录\n需要将语音内容转为文字的音频文件的所在目录。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            section = 'Input params',
            option = 'Audio_Dir',
            defaultValue = ''
        )
        subPage_ASR.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "语音转录参数"),
            text = QCA.translate('MainWindow', "语种标注\n标注音频中说话人所使用的语言，若用于数据集制作则建议启用。"),
            section = 'Whisper params',
            option = 'Add_LanguageInfo',
            defaultValue = True
        )
        ASR_Whisper_ModelPath_Default = Path(modelDir).joinpath('ASR', 'Whisper', 'Downloaded', 'small.pt').as_posix()
        subPage_ASR.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "语音转录参数"),
            text = QCA.translate('MainWindow', "模型加载路径\n用于加载的Whisper模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pt类型 (*.pt)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('ASR', 'Whisper', 'Downloaded')),
            section = 'Whisper params',
            option = 'Model_Path',
            defaultValue = ASR_Whisper_ModelPath_Default,
            placeholderText = ASR_Whisper_ModelPath_Default
        )
        subPage_ASR.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "语音转录参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "显示转录内容\n启用该项后会在运行过程中显示转录的内容，否则只显示进度。"),
            section = 'Whisper params',
            option = 'Verbose',
            defaultValue = True
        )
        subPage_ASR.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "语音转录参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "半精度计算\n主要使用半精度浮点数进行计算，若GPU不可用则忽略或禁用此项。"),
            section = 'Whisper params',
            option = 'fp16',
            defaultValue = True
        )
        subPage_ASR.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "语音转录参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "关联上下文\n在音频之间的内容具有关联性时启用该项可以获得更好的效果。"),
            section = 'Whisper params',
            option = 'Condition_on_Previous_Text',
            defaultValue = False
        )
        ASR_Whisper_OutputDirName_Default = str(date.today())
        subPage_ASR.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            text = QCA.translate('MainWindow', "输出目录名\n用于保存最后生成的字幕文件的目录的名字。"),
            section = 'Output params',
            option = 'SRT_Dir_Name',
            defaultValue = '',
            placeholderText = ASR_Whisper_OutputDirName_Default
        )
        LineEdit_ASR_Whisper_OutputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = subPage_ASR.findChildWidget("输出参数", None, "输出目录名", LineEditBase),
            rootEdit = self.ui.LineEdit_ASR_Whisper_OutputRoot,
            dirEdit = LineEdit_ASR_Whisper_OutputDir
        )
        subPage_ASR.addChkOutputSideBtn(
            outputRootEdit = self.ui.LineEdit_ASR_Whisper_OutputRoot
        )
        self.task_voiceTranscribing_whisper = Execute_Voice_Transcribing_Whisper(coreDir, logPath)
        subPage_ASR.setExecutor(
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_voiceTranscribing_whisper.execute,
            executeParamTargets = [
                subPage_ASR.findChildWidget("语音转录参数", None, "模型加载路径"),
                subPage_ASR.findChildWidget("输入参数", None, "音频输入目录"),
                subPage_ASR.findChildWidget("语音转录参数", "高级设置", "显示转录内容"),
                subPage_ASR.findChildWidget("语音转录参数", None, "语种标注"),
                subPage_ASR.findChildWidget("语音转录参数", "高级设置", "高级设置"),
                subPage_ASR.findChildWidget("语音转录参数", "高级设置", "半精度计算"),
                self.ui.LineEdit_ASR_Whisper_OutputRoot,
                subPage_ASR.findChildWidget("输出参数", None, "输出目录名")
            ],
            terminateMethod = self.task_voiceTranscribing_whisper.terminate,
            finishedEvents = {
                lambda: self.showMask(True, "正在加载表单"): TaskStatus.Succeeded,
                lambda: self.showASRResult(
                    LineEdit_ASR_Whisper_OutputDir.text(),
                    subPage_ASR.findChildWidget("输入参数", None, "音频输入目录", LineEditBase).text()
                ): TaskStatus.Succeeded,
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool,
        )

        self.ui.Page_ASR.addSubPage(
            QCA.translate('MainWindow', 'Whisper'), subPage_ASR
        )

        #############################################################
        ###################### Content: Dataset #####################
        #############################################################

        # Guidance
        self.ui.Page_Dataset.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = QCA.translate('MainWindow', "引导（仅出现一次）"),
                images = [
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Dataset.png')),
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                texts = [
                    '欢迎来到数据集工具界面\n该工具用于生成适用于语音模型训练的数据集',
                    '顶部区域用于切换当前工具类型\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
                ]
            )
        )

        self.ui.Button_Menu_Dataset.clicked.connect(
            lambda: (
                self.ui.Page_Dataset.helpButton.click(),
                config.editConfig('Dialog', 'GuidanceShown_Dataset', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_Dataset', 'False')) is False else None
        )

        # ParamsManager - GPT-SoVITS
        configPath_DAT_GPTSoVITS = EasyUtils.normPath(Path(configDir).joinpath('Config_DAT_GPT-SoVITS.ini'))
        paramsManager_DAT_GPTSoVITS = ParamsManager(configPath_DAT_GPTSoVITS)

        subPage_dataset_GPTSoVITS = SubToolPage(self.ui.Page_Dataset, paramsManager_DAT_GPTSoVITS)
        subPage_dataset_GPTSoVITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "音频文件目录/语音识别结果文本路径\n音频文件的所在目录，或者提供由语音识别得到的文本文件。"),
            section = 'Input params',
            option = 'WAV_Dir',
            defaultValue = ''
        )
        subPage_dataset_GPTSoVITS.findChildWidget("输入参数", None, "音频文件目录/语音识别结果文本路径", LineEditBase).fileButton.clicked.connect(
            lambda: self.setDirPathSelection(
                textReciever = subPage_dataset_GPTSoVITS.findChildWidget("输入参数", None, "音频文件目录/语音识别结果文本路径", LineEditBase),
                dirSelectionText = "语音识别结果文本路径",
                pathSelectionText = "音频文件目录",
                fileType = "txt类型 (*.txt)",
                directory = Path(currentDir).joinpath('语音识别结果', 'VPR').as_posix()
            )
        )
        subPage_dataset_GPTSoVITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "字幕输入目录\n字幕文件的所在目录，字幕文件须与对应音频文件同名且在文本中注明所属语言。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = Path(currentDir).joinpath('语音转录结果', 'Whisper').as_posix(),
            section = 'Input params',
            option = 'SRT_Dir',
            defaultValue = ''
        )
        DAT_GPTSoVITS_DataFormat_Default = '路径|人名|语言|文本'
        subPage_dataset_GPTSoVITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            text = QCA.translate('MainWindow', "数据文本格式\n数据集的文本格式，默认使用GPT-SoVITS的标准。"),
            section = 'GPT-SoVITS params',
            option = 'DataFormat_Path',
            defaultValue = DAT_GPTSoVITS_DataFormat_Default,
            placeholderText = DAT_GPTSoVITS_DataFormat_Default
        )
        subPage_dataset_GPTSoVITS.findChildWidget("数据集参数", None, "数据文本格式", LineEditBase).textChanged.connect(
            lambda value: (
                MessageBoxBase.pop(self,
                    QMessageBox.Warning, "Warning",
                    "请保留关键词：'路径'，'人名'，'语言'，'文本'",
                ),
                paramsManager_DAT_GPTSoVITS.resetParam(self.ui.LineEdit_DAT_GPTSoVITS_DataFormat),
            ) if not all(Keyword in value for Keyword in ['路径', '人名', '语言', '文本']) else None
        )
        DAT_GPTSoVITS_OutputDirName_Default = str(date.today())
        subPage_dataset_GPTSoVITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            text = QCA.translate('MainWindow', "输出目录名\n用于保存最后生成的数据集文件的目录的名字。"),
            section = 'Output params',
            option = 'Output_Dir_Name',
            defaultValue = '',
            placeholderText = DAT_GPTSoVITS_OutputDirName_Default
        )
        LineEdit_DAT_GPTSoVITS_OutputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = subPage_dataset_GPTSoVITS.findChildWidget("输出参数", None, "输出目录名", LineEditBase),
            rootEdit = self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot,
            dirEdit = LineEdit_DAT_GPTSoVITS_OutputDir
        )
        DAT_GPTSoVITS_FileListName_Default = "Train_" + str(date.today())
        subPage_dataset_GPTSoVITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "数据集文本名\n用于保存最后生成的数据集txt文件的名字。"),
            section = 'Output params',
            option = 'FileList_Name',
            defaultValue = DAT_GPTSoVITS_FileListName_Default,
            placeholderText = DAT_GPTSoVITS_FileListName_Default
        )
        LineEdit_DAT_GPTSoVITS_FileListPath = LineEditBase()
        self.setPathAlert(
            fileNameEdit = subPage_dataset_GPTSoVITS.findChildWidget("输出参数", "高级设置", "数据集文本名", LineEditBase),
            dirEdit = LineEdit_DAT_GPTSoVITS_OutputDir,
            suffix = ".txt",
            fileEdit = LineEdit_DAT_GPTSoVITS_FileListPath,
        )
        subPage_dataset_GPTSoVITS.addChkOutputSideBtn(
            outputRootEdit = self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot
        )
        self.task_datasetCreating_gptsovits = Execute_Dataset_Creating_GPTSoVITS(coreDir, logPath)
        subPage_dataset_GPTSoVITS.setExecutor(
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_datasetCreating_gptsovits.execute,
            executeParamTargets = [
                subPage_dataset_GPTSoVITS.findChildWidget("输入参数", None, "字幕输入目录"),
                subPage_dataset_GPTSoVITS.findChildWidget("输入参数", None, "音频文件目录/语音识别结果文本路径"),
                subPage_dataset_GPTSoVITS.findChildWidget("数据集参数", None, "数据文本格式"),
                self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot,
                subPage_dataset_GPTSoVITS.findChildWidget("输出参数", None, "输出目录名"),
                subPage_dataset_GPTSoVITS.findChildWidget("输出参数", "高级设置", "数据集文本名")
            ],
            terminateMethod = self.task_datasetCreating_gptsovits.terminate,
            finishedEvents = {
                lambda: self.showMask(True, "正在加载表单"): TaskStatus.Succeeded,
                lambda: self.showDATResult(
                    LineEdit_DAT_GPTSoVITS_FileListPath.text(),
                    None
                ): TaskStatus.Succeeded,
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool,
        )

        self.ui.Page_Dataset.addSubPage(
            QCA.translate('MainWindow', 'GPT-SoVITS'), subPage_dataset_GPTSoVITS
        )

        # ParamsManager - VITS
        configPath_DAT_VITS = EasyUtils.normPath(Path(configDir).joinpath('Config_DAT_VITS.ini'))
        paramsManager_DAT_VITS = ParamsManager(configPath_DAT_VITS)

        subPage_dataset_VITS = SubToolPage(self.ui.Page_Dataset, paramsManager_DAT_VITS)
        subPage_dataset_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "音频文件目录/语音识别结果文本路径\n音频文件的所在目录（要求按说话人分类），或者提供由语音识别得到的文本文件。"),
            section = 'Input params',
            option = 'WAV_Dir',
            defaultValue = ''
        )
        subPage_dataset_VITS.findChildWidget("输入参数", None, "音频文件目录/语音识别结果文本路径", LineEditBase).fileButton.clicked.connect(
            lambda: self.setDirPathSelection(
                textReciever = subPage_dataset_VITS.findChildWidget("输入参数", None, "音频文件目录/语音识别结果文本路径", LineEditBase),
                dirSelectionText = "语音识别结果文本路径",
                pathSelectionText = "音频文件目录",
                fileType = "txt类型 (*.txt)",
                directory = Path(currentDir).joinpath('语音识别结果', 'VPR').as_posix()
            )
        )
        subPage_dataset_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "字幕输入目录\n字幕文件的所在目录，字幕文件须与对应音频文件同名且在文本中注明所属语言。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = Path(currentDir).joinpath('语音转录结果', 'Whisper').as_posix(),
            section = 'Input params',
            option = 'SRT_Dir',
            defaultValue = ''
        )
        DAT_VITS_DataFormat_Default = '路径|人名|[语言]文本[语言]'
        subPage_dataset_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            text = QCA.translate('MainWindow', "数据文本格式\n数据集的文本格式，默认使用VITS的标准。"),
            section = 'VITS params',
            option = 'DataFormat_Path',
            defaultValue = DAT_VITS_DataFormat_Default,
            placeholderText = DAT_VITS_DataFormat_Default
        )
        subPage_dataset_VITS.findChildWidget("数据集参数", None, "数据文本格式", LineEditBase).textChanged.connect(
            lambda value: (
                MessageBoxBase.pop(self,
                    QMessageBox.Warning, "Warning",
                    "请保留关键词：'路径'，'人名'，'语言'，'文本'",
                ),
                paramsManager_DAT_VITS.resetParam(subPage_dataset_VITS.findChildWidget("数据集参数", None, "数据文本格式")),
            ) if not all(Keyword in value for Keyword in ['路径', '人名', '语言', '文本']) else None
        )
        subPage_dataset_VITS.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            text = QCA.translate('MainWindow', "添加辅助数据\n添加用以辅助训练的数据集，若当前语音数据的质量/数量较低则建议启用。"),
            section = 'VITS params',
            option = 'Add_AuxiliaryData',
            defaultValue = False
        )
        DAT_VITS_AuxiliaryDataPath_Default = Path(currentDir).joinpath('AuxiliaryData', 'VITS', 'AuxiliaryData.txt').as_posix()
        subPage_dataset_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            text = QCA.translate('MainWindow', "辅助数据文本路径\n辅助数据集的文本的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "文本类型 (*.csv *.txt)",
            directory = EasyUtils.normPath(Path(currentDir).joinpath('AuxiliaryData', 'VITS')),
            section = 'VITS params',
            option = 'AuxiliaryData_Path',
            defaultValue = DAT_VITS_AuxiliaryDataPath_Default,
            placeholderText = DAT_VITS_AuxiliaryDataPath_Default,
            emptyAllowed = True
        )
        subPage_dataset_VITS.addDoubleSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "训练集占比\n划分给训练集的数据在数据集中所占的比例。"),
            minimum = 0.5,
            maximum = 0.9,
            step = 0.1,
            section = 'VITS params',
            option = 'TrainRatio',
            defaultValue = 0.7
        )
        subPage_dataset_VITS.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "采样率 (HZ)\n数据集所要求的音频采样率，若维持不变则保持'None'即可。"),
            items = ['22050', '44100', '48000', '96000', '192000', 'None'],
            section = 'VITS params',
            option = 'SampleRate',
            defaultValue = 22050,
            emptyAllowed = True
        )
        subPage_dataset_VITS.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "采样位数\n数据集所要求的音频采样位数，若维持不变则保持'None'即可。"),
            items = ['8', '16', '24', '32', '32 (Float)', 'None'],
            section = 'VITS params',
            option = 'SampleWidth',
            defaultValue = 16,
            emptyAllowed = True
        )
        subPage_dataset_VITS.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "数据集参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "合并声道\n将数据集音频的声道合并为单声道。"),
            section = 'VITS params',
            option = 'ToMono',
            defaultValue = True
        )
        DAT_VITS_OutputDirName_Default = str(date.today())
        subPage_dataset_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            text = QCA.translate('MainWindow', "输出目录名\n用于保存最后生成的数据集文件的目录的名字。"),
            section = 'Output params',
            option = 'Output_Dir_Name',
            defaultValue = '',
            placeholderText = DAT_VITS_OutputDirName_Default
        )
        LineEdit_DAT_VITS_OutputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = subPage_dataset_VITS.findChildWidget("输出参数", None, "输出目录名", LineEditBase),
            rootEdit = self.ui.LineEdit_DAT_VITS_OutputRoot,
            dirEdit = LineEdit_DAT_VITS_OutputDir
        )
        DAT_VITS_FileListNameTraining_Default = "Train_" + str(date.today())
        subPage_dataset_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "训练集文本名\n用于保存最后生成的训练集txt文件的名字。"),
            section = 'Output params',
            option = 'FileList_Name_Training',
            defaultValue = DAT_VITS_FileListNameTraining_Default,
            placeholderText = DAT_VITS_FileListNameTraining_Default
        )
        LineEdit_DAT_VITS_FileListPathTraining = LineEditBase()
        self.setPathAlert(
            fileNameEdit = subPage_dataset_VITS.findChildWidget("输出参数", "高级设置", "训练集文本名", LineEditBase),
            dirEdit = LineEdit_DAT_VITS_OutputDir,
            suffix = ".txt",
            fileEdit = LineEdit_DAT_VITS_FileListPathTraining
        )
        DAT_VITS_FileListNameValidation_Default = "Val_" + str(date.today())
        subPage_dataset_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "验证集文本名\n用于保存最后生成的验证集txt文件的名字。"),
            section = 'Output params',
            option = 'FileList_Name_Validation',
            defaultValue = DAT_VITS_FileListNameValidation_Default,
            placeholderText = DAT_VITS_FileListNameValidation_Default
        )
        LineEdit_DAT_VITS_FileListPathValidation = LineEditBase()
        self.setPathAlert(
            fileNameEdit = subPage_dataset_VITS.findChildWidget("输出参数", "高级设置", "验证集文本名", LineEditBase),
            dirEdit = LineEdit_DAT_VITS_OutputDir,
            suffix = ".txt",
            fileEdit = LineEdit_DAT_VITS_FileListPathValidation
        )
        subPage_dataset_VITS.addChkOutputSideBtn(
            outputRootEdit = self.ui.LineEdit_DAT_VITS_OutputRoot
        )
        self.task_datasetCreating_vits = Execute_Dataset_Creating_VITS(coreDir, logPath)
        subPage_dataset_VITS.setExecutor(
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_datasetCreating_vits.execute,
            executeParamTargets = [
                subPage_dataset_VITS.findChildWidget("输入参数", None, "字幕输入目录"),
                subPage_dataset_VITS.findChildWidget("输入参数", None, "音频文件目录/语音识别结果文本路径"),
                subPage_dataset_VITS.findChildWidget("数据集参数", "高级设置", "采样率 (HZ)"),
                subPage_dataset_VITS.findChildWidget("数据集参数", "高级设置", "采样位数"),
                subPage_dataset_VITS.findChildWidget("数据集参数", "高级设置", "合并声道"),
                subPage_dataset_VITS.findChildWidget("数据集参数", None, "数据文本格式"),
                subPage_dataset_VITS.findChildWidget("数据集参数", None, "添加辅助数据"),
                subPage_dataset_VITS.findChildWidget("数据集参数", None, "辅助数据文本路径"),
                subPage_dataset_VITS.findChildWidget("数据集参数", "高级设置", "训练集占比"),
                self.ui.LineEdit_DAT_VITS_OutputRoot,
                subPage_dataset_VITS.findChildWidget("输出参数", None, "输出目录名"),
                subPage_dataset_VITS.findChildWidget("输出参数", "高级设置", "训练集文本名"),
                subPage_dataset_VITS.findChildWidget("输出参数", "高级设置", "验证集文本名")
            ],
            terminateMethod = self.task_datasetCreating_vits.terminate,
            finishedEvents = {
                lambda: self.showMask(True, "正在加载表单"): TaskStatus.Succeeded,
                lambda: self.showDATResult(
                    LineEdit_DAT_VITS_FileListPathTraining.text(),
                    LineEdit_DAT_VITS_FileListPathValidation.text()
                ): TaskStatus.Succeeded,
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool,
        )
        Function_ConfigureCheckBox(
            checkBox = subPage_dataset_VITS.findChildWidget("数据集参数", None, "添加辅助数据", CheckBoxBase),
            checkedEvents = {
                lambda: Function_SetChildWidgetsVisibility(
                    subPage_dataset_VITS.findChildWidget("数据集参数"),
                    childWidgetsVisibility = {
                        subPage_dataset_VITS.findChildWidget("数据集参数", None, "辅助数据文本路径"): True
                    },
                ) : True
            },
            uncheckedEvents = {
                lambda: Function_SetChildWidgetsVisibility(
                    subPage_dataset_VITS.findChildWidget("数据集参数"),
                    childWidgetsVisibility = {
                        subPage_dataset_VITS.findChildWidget("数据集参数", None, "辅助数据文本路径"): False
                    },
                ) : True
            },
        )

        self.ui.Page_Dataset.addSubPage(
            QCA.translate('MainWindow', 'VITS2'), subPage_dataset_VITS
        )

        #############################################################
        ####################### Content: Train ######################
        #############################################################

        # Guidance
        self.ui.Page_Train.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = QCA.translate('MainWindow', "引导（仅出现一次）"),
                images = [
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Train.png')),
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                texts = [
                    '欢迎来到语音训练工具界面\n该工具用于训练出适用于语音合成的模型文件',
                    '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
                ]
            )
        )

        self.ui.Button_Menu_Train.clicked.connect(
            lambda: (
                self.ui.Page_Train.helpButton.click(),
                config.editConfig('Dialog', 'GuidanceShown_Train', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_Train', 'False')) is False else None
        )

        # ParamsManager - GPT-SoVITS
        configPath_train_gptsovits = EasyUtils.normPath(Path(configDir).joinpath('Config_Train_GPT-SoVITS.ini'))
        paramsManager_train_gptsovits = ParamsManager(configPath_train_gptsovits)

        subPage_train_gptsovits = SubToolPage(self.ui.Page_Train, paramsManager_train_gptsovits)
        subPage_train_gptsovits.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "全局设置"),
            text = QCA.translate('MainWindow', "训练版本\nGPT-SoVITS模型的训练版本，注意v3训练需要8G以上的显存。"),
            items = ['v2', 'v3'],
            section = 'Input params',
            option = 'version',
            defaultValue = 'v2'
        )
        subPage_train_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "训练集文本路径\n用于提供训练集音频路径及其语音内容的训练集txt文件的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "txt类型 (*.txt)",
            directory = Path(currentDir).joinpath('数据集制作结果', 'GPT-SoVITS').as_posix(),
            section = 'Input params',
            option = 'FileList_Path',
            defaultValue = ''
        )
        Train_GPTSoVITS_ModelPathPretrainedS1_Default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's1bert25hz-5kh-longer-epoch=12-step=369668.ckpt').as_posix()
        subPage_train_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "预训练GPT模型路径\n预训练GPT（s1）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "ckpt类型 (*.ckpt)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2')),
            section = 'GPT-SoVITS params',
            option = 'Model_Path_Pretrained_s1',
            defaultValue = Train_GPTSoVITS_ModelPathPretrainedS1_Default,
            placeholderText = Train_GPTSoVITS_ModelPathPretrainedS1_Default
        )
        Train_GPTSoVITS_ModelPathPretrainedS2G_Default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2G2333k.pth').as_posix()
        subPage_train_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "预训练SoVITS生成器模型路径\n预训练SoVITS生成器（s2G）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2')),
            section = 'GPT-SoVITS params',
            option = 'Model_Path_Pretrained_s2G',
            defaultValue = Train_GPTSoVITS_ModelPathPretrainedS2G_Default,
            placeholderText = Train_GPTSoVITS_ModelPathPretrainedS2G_Default
        )
        Train_GPTSoVITS_ModelPathPretrainedS2D_Default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2D2333k.pth').as_posix()
        subPage_train_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "预训练SoVITS判别器模型路径\n预训练SoVITS判别器（s2D）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2')),
            section = 'GPT-SoVITS params',
            option = 'Model_Path_Pretrained_s2D',
            defaultValue = Train_GPTSoVITS_ModelPathPretrainedS2D_Default,
            placeholderText = Train_GPTSoVITS_ModelPathPretrainedS2D_Default
        )
        Train_GPTSoVITS_ModelDirPretrainedBert_Default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-roberta-wwm-ext-large').as_posix()
        subPage_train_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "预训练BERT模型路径\n预训练BERT模型（文件夹）的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'GPT-SoVITS params',
            option = 'Model_Dir_Pretrained_bert',
            defaultValue = Train_GPTSoVITS_ModelDirPretrainedBert_Default,
            placeholderText = Train_GPTSoVITS_ModelDirPretrainedBert_Default
        )
        Train_GPTSoVITS_ModelDirPretrainedSSL_Default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-hubert-base').as_posix()
        subPage_train_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "预训练HuBERT模型路径\n预训练HuBERT模型（文件夹）的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'GPT-SoVITS params',
            option = 'Model_Dir_Pretrained_ssl',
            defaultValue = Train_GPTSoVITS_ModelDirPretrainedSSL_Default,
            placeholderText = Train_GPTSoVITS_ModelDirPretrainedSSL_Default
        )
        # subPage_train_gptsovits.addSpinBoxFrame(
        #     rootItemText = QCA.translate('MainWindow', "训练参数"),
        #     text = QCA.translate('MainWindow', "GPT模型模型迭代轮数\nGPT模型训练时将全部样本完整迭代一轮的次数。"),
        #     minimum = 1,
        #     maximum = 100,
        #     step = 1,
        #     section = 'GPT-SoVITS params',
        #     option = 'gpt_epochs',
        #     defaultValue = 8
        # )
        # subPage_train_gptsovits.addSpinBoxFrame(
        #     rootItemText = QCA.translate('MainWindow', "训练参数"),
        #     text = QCA.translate('MainWindow', "SoVITS模型迭代轮数\nSoVITS模型训练时将全部样本完整迭代一轮的次数。"),
        #     minimum = 1,
        #     maximum = 100,
        #     step = 1,
        #     section = 'GPT-SoVITS params',
        #     option = 'sovits_epochs',
        #     defaultValue = 15
        # )
        subPage_train_gptsovits.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            text = QCA.translate('MainWindow', "半精度训练\n通过混合了float16精度的训练方式减小显存占用。"),
            section = 'GPT-SoVITS params',
            option = 'half_precision',
            defaultValue = True
        )
        subPage_train_gptsovits.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            text = QCA.translate('MainWindow', "梯度检查点\n是否开启梯度检查点节省显存占用。"),
            section = 'GPT-SoVITS params',
            option = 'if_grad_ckpt',
            defaultValue = True
        )
        subPage_train_gptsovits.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            text = QCA.translate('MainWindow', "Lora秩\n。"),
            items = ['16', '32', '64', '128'],
            section = 'GPT-SoVITS params',
            option = 'lora_rank',
            defaultValue = '32'
        )
        Train_GPTSoVITS_OutputDirName_Default = str(date.today())
        subPage_train_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            text = QCA.translate('MainWindow', "输出目录名\n存放训练所得模型的目录的名字。"),
            section = 'Output params',
            option = 'Output_Dir_Name',
            defaultValue = '',
            placeholderText = Train_GPTSoVITS_OutputDirName_Default
        )
        LineEdit_Train_GPTSoVITS_OutputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = subPage_train_gptsovits.findChildWidget("输出参数", None, "输出目录名", LineEditBase),
            rootEdit = self.ui.LineEdit_Train_GPTSoVITS_OutputRoot,
            dirEdit = LineEdit_Train_GPTSoVITS_OutputDir
        )
        Train_GPTSoVITS_LogDir_Default = Path(Path(currentDir).root).joinpath('EVT_TrainLog', 'GPT-SoVITS', str(date.today())).as_posix()
        subPage_train_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "日志输出目录\n训练时生成的日志的存放目录。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(Train_GPTSoVITS_LogDir_Default).parent),
            section = 'Output params',
            option = 'Output_LogDir',
            defaultValue = Train_GPTSoVITS_LogDir_Default,
            placeholderText = Train_GPTSoVITS_LogDir_Default
        )
        subPage_train_gptsovits.findChildWidget("输出参数", "高级设置", "日志输出目录", LineEditBase).textChanged.connect(
            lambda value: (
                MessageBoxBase.pop(self,
                    QMessageBox.Warning, "Warning",
                    "保存路径不支持非ASCII字符，请使用英文路径以避免训练报错",
                ),
                subPage_train_gptsovits.findChildWidget("输出参数", "高级设置", "日志输出目录", LineEditBase).clear()
            ) if not all(Char.isascii() for Char in value) else None
        )
        subPage_train_gptsovits.addChkOutputSideBtn(
            outputRootEdit = self.ui.LineEdit_Train_GPTSoVITS_OutputRoot
        )
        subPage_train_gptsovits.addSideBtn(
            text = QCA.translate('MainWindow', "启动Tensorboard"),
            events = [
                lambda: Function_SetMethodExecutor(
                    executeMethod = runTensorboard,
                    executeParams = subPage_train_gptsovits.findChildWidget("输出参数", "高级设置", "日志输出目录", LineEditBase).text(),
                    threadPool = self.threadPool,
                    parentWindow = self,
                )
            ]
        )
        self.task_voiceTraining_gptsovits = Execute_Voice_Training_GPTSoVITS(coreDir, logPath)
        subPage_train_gptsovits.setExecutor(
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_voiceTraining_gptsovits.execute,
            executeParamTargets = [
                subPage_train_gptsovits.findChildWidget("全局设置", None, "训练版本"),
                subPage_train_gptsovits.findChildWidget("输入参数", None, "训练集文本路径"),
                subPage_train_gptsovits.findChildWidget("输入参数", None, "预训练BERT模型路径"),
                subPage_train_gptsovits.findChildWidget("输入参数", None, "预训练HuBERT模型路径"),
                subPage_train_gptsovits.findChildWidget("输入参数", None, "预训练GPT模型路径"),
                subPage_train_gptsovits.findChildWidget("输入参数", None, "预训练SoVITS生成器模型路径"),
                subPage_train_gptsovits.findChildWidget("输入参数", None, "预训练SoVITS判别器模型路径"),
                subPage_train_gptsovits.findChildWidget("训练参数", None, "半精度训练"),
                subPage_train_gptsovits.findChildWidget("训练参数", None, "梯度检查点"),
                subPage_train_gptsovits.findChildWidget("训练参数", None, "Lora秩"),
                self.ui.LineEdit_Train_GPTSoVITS_OutputRoot,
                subPage_train_gptsovits.findChildWidget("输出参数", None, "输出目录名"),
                subPage_train_gptsovits.findChildWidget("输出参数", "高级设置", "日志输出目录")
            ],
            terminateMethod = self.task_voiceTraining_gptsovits.terminate,
            finishedEvents = {
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool,
        )
        FunctionSignals.Signal_TaskStatus.connect(
            lambda Task, Status: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "是否稍后启用tensorboard？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {QMessageBox.Yes: lambda: subPage_train_gptsovits.findChildWidget("启动Tensorboard").click()}
            ) if Task == self.task_voiceTraining_gptsovits.__class__.execute.__qualname__ and Status == TaskStatus.Started else None
        )
        Function_ConfigureComboBox(
            comboBox = subPage_train_gptsovits.findChildWidget("全局设置", None, "训练版本", ComboBoxBase),
            textChangedEvents = {
                'v2': lambda: Function_SetChildWidgetsVisibility(
                    container = subPage_train_gptsovits.findChildWidget("输入参数"),
                    childWidgetsVisibility = {
                        subPage_train_gptsovits.findChildWidget("输入参数", None, "预训练SoVITS判别器模型路径"): True,
                        subPage_train_gptsovits.findChildWidget("训练参数", None, "梯度检查点"): False,
                        subPage_train_gptsovits.findChildWidget("训练参数", None, "Lora秩"): False,
                    }
                ),
                'v3': lambda: Function_SetChildWidgetsVisibility(
                    container = subPage_train_gptsovits.findChildWidget("输入参数"),
                    childWidgetsVisibility = {
                        subPage_train_gptsovits.findChildWidget("输入参数", None, "预训练SoVITS判别器模型路径"): False,
                        subPage_train_gptsovits.findChildWidget("训练参数", None, "梯度检查点"): True,
                        subPage_train_gptsovits.findChildWidget("训练参数", None, "Lora秩"): True,
                    }
                ),
            },
            takeEffect = True
        )

        self.ui.Page_Train.addSubPage(
            QCA.translate('MainWindow', 'GPT-SoVITS'), subPage_train_gptsovits
        )

        # ParamsManager - VITS
        configPath_Train_VITS = EasyUtils.normPath(Path(configDir).joinpath('Config_Train_VITS.ini'))
        paramsManager_Train_VITS = ParamsManager(configPath_Train_VITS)

        subPage_train_VITS = SubToolPage(self.ui.Page_Train, paramsManager_Train_VITS)
        subPage_train_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "训练集文本路径\n用于提供训练集音频路径及其语音内容的训练集txt文件的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "txt类型 (*.txt)",
            directory = Path(currentDir).joinpath('数据集制作结果', 'VITS').as_posix(),
            section = 'Input params',
            option = 'FileList_Path_Training',
            defaultValue = ''
        )
        subPage_train_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "验证集文本路径\n用于提供验证集音频路径及其语音内容的验证集txt文件的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "txt类型 (*.txt)",
            directory = Path(currentDir).joinpath('数据集制作结果', 'VITS').as_posix(),
            section = 'Input params',
            option = 'FileList_Path_Validation',
            defaultValue = ''
        )
        subPage_train_VITS.addSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            text = QCA.translate('MainWindow', "迭代轮数\n将全部样本完整迭代一轮的次数。"),
            minimum = 10,
            maximum = 100000,
            step = 1,
            section = 'VITS params',
            option = 'Epochs',
            defaultValue = 1000
        )
        subPage_train_VITS.addSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            text = QCA.translate('MainWindow', "批处理量\n每轮迭代中单位批次的样本数量，需根据GPU的性能调节该值。"),
            toolTip = QCA.translate('MainWindow', "建议：2~4G: 2\n6~8G: 4\n10~12G: 8\n14~16G: 16"),
            minimum = 2,
            maximum = 128,
            step = 1,
            section = 'VITS params',
            option = 'Batch_Size',
            defaultValue = 4
        )
        subPage_train_VITS.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            text = QCA.translate('MainWindow', "使用预训练模型\n使用预训练模型（底模），其载入优先级高于检查点。"),
            section = 'VITS params',
            option = 'Use_PretrainedModels',
            defaultValue = True
        )
        Train_VITS_ModelPathPretrainedG_Default = Path(modelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_G.pth').as_posix()
        subPage_train_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            text = QCA.translate('MainWindow', "预训练G模型路径\n预训练生成器（Generator）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'VITS', 'Downloaded')),
            section = 'VITS params',
            option = 'Model_Path_Pretrained_G',
            defaultValue = Train_VITS_ModelPathPretrainedG_Default,
            placeholderText = Train_VITS_ModelPathPretrainedG_Default,
            emptyAllowed = True
        )
        Train_VITS_ModelPathPretrainedD_Default = Path(modelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_D.pth').as_posix()
        subPage_train_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            text = QCA.translate('MainWindow', "预训练D模型路径\n预训练判别器（Discriminator）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'VITS', 'Downloaded')),
            section = 'VITS params',
            option = 'Model_Path_Pretrained_D',
            defaultValue = Train_VITS_ModelPathPretrainedD_Default,
            placeholderText = Train_VITS_ModelPathPretrainedD_Default,
            emptyAllowed = True
        )
        subPage_train_VITS.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            text = QCA.translate('MainWindow', "保留原说话人（实验性）\n保留预训练模型中原有的说话人。"),
            section = 'VITS params',
            option = 'Keep_Original_Speakers',
            defaultValue = False
        )
        Train_VITS_ConfigPathLoad_Default = Path(modelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_Config.json').as_posix()
        subPage_train_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            text = QCA.translate('MainWindow', "配置加载路径\n用于加载底模人物信息的配置文件的路径"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "json类型 (*.json)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'VITS', 'Downloaded')),
            section = 'VITS params',
            option = 'Config_Path_Load',
            defaultValue = Train_VITS_ConfigPathLoad_Default,
            placeholderText = Train_VITS_ConfigPathLoad_Default,
            emptyAllowed = True
        )
        subPage_train_VITS.addSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "进程数量\n进行数据加载时可并行的进程数量，需根据CPU的性能调节该值。"),
            minimum = 2,
            maximum = 128,
            step = 2,
            section = 'VITS params',
            option = 'Num_Workers',
            defaultValue = 4
        )
        subPage_train_VITS.addCheckBoxFrame(
            rootItemText = QCA.translate('MainWindow', "训练参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "半精度训练\n通过混合了float16精度的训练方式减小显存占用以支持更大的批处理量。"),
            section = 'VITS params',
            option = 'FP16_Run',
            defaultValue = False
        )
        subPage_train_VITS.addSpinBoxFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            text = QCA.translate('MainWindow', "保存间隔\n每次保存模型所间隔的步数。PS: 步数 ≈ 迭代轮次 * 训练样本数 / 批处理量"),
            toolTip = QCA.translate('MainWindow', "提示：设置过小可能导致磁盘占用激增哦"),
            minimum = 10,
            maximum = 100000,
            step = 1,
            section = 'Output params',
            option = 'Eval_Interval',
            defaultValue = 1000
        )
        Train_VITS_OutputDirName_Default = str(date.today())
        subPage_train_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            text = QCA.translate('MainWindow', "输出目录名\n存放训练所得模型的目录的名字，若目录中已存在模型则会将其视为检查点。"),
            section = 'Output params',
            option = 'Output_Dir_Name',
            defaultValue = '',
            placeholderText = Train_VITS_OutputDirName_Default
        )
        LineEdit_Train_VITS_OutputDir = LineEditBase()
        self.setDirAlert(
            dirNameEdit = subPage_train_VITS.findChildWidget("输出参数", None, "输出目录名", LineEditBase),
            rootEdit = self.ui.LineEdit_Train_VITS_OutputRoot,
            dirEdit = LineEdit_Train_VITS_OutputDir
        )
        Train_VITS_LogDir_Default = Path(Path(currentDir).root).joinpath('EVT_TrainLog', 'VITS', str(date.today())).as_posix()
        subPage_train_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输出参数"),
            toolBoxText = QCA.translate('MainWindow', "高级设置"),
            text = QCA.translate('MainWindow', "日志输出目录\n训练时生成的日志的存放目录。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(Train_VITS_LogDir_Default).parent),
            section = 'Output params',
            option = 'Output_LogDir',
            defaultValue = Train_VITS_LogDir_Default,
            placeholderText = Train_VITS_LogDir_Default
        )
        subPage_train_VITS.findChildWidget("输出参数", "高级设置", "日志输出目录", LineEditBase).textChanged.connect(
            lambda value: (
                MessageBoxBase.pop(self,
                    QMessageBox.Warning, "Warning",
                    text = "保存路径不支持非ASCII字符，请使用英文路径以避免训练报错",
                ),
                subPage_train_VITS.findChildWidget("输出参数", "高级设置", "日志输出目录", LineEditBase).clear()
            ) if not all(Char.isascii() for Char in value) else None
        )
        subPage_train_VITS.addChkOutputSideBtn(
            outputRootEdit = self.ui.LineEdit_Train_VITS_OutputRoot
        )
        subPage_train_VITS.addSideBtn(
            text = QCA.translate('MainWindow', "启动Tensorboard"),
            events = [
                lambda: Function_SetMethodExecutor(
                    executeMethod = runTensorboard,
                    executeParams = subPage_train_VITS.findChildWidget("输出参数", "高级设置", "日志输出目录", LineEditBase).text(),
                    threadPool = self.threadPool,
                    parentWindow = self,
                )
            ]
        )
        self.task_voiceTraining_vits = Execute_Voice_Training_VITS(coreDir, logPath)
        subPage_train_VITS.setExecutor(
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_voiceTraining_vits.execute,
            executeParamTargets = [
                subPage_train_VITS.findChildWidget("输入参数", None, "训练集文本路径"),
                subPage_train_VITS.findChildWidget("输入参数", None, "验证集文本路径"),
                subPage_train_VITS.findChildWidget("训练参数", None, "迭代轮数"),
                subPage_train_VITS.findChildWidget("训练参数", None, "保存间隔"),
                subPage_train_VITS.findChildWidget("训练参数", None, "批处理量"),
                subPage_train_VITS.findChildWidget("训练参数", "高级设置", "半精度训练"),
                subPage_train_VITS.findChildWidget("训练参数", None, "保留原说话人（实验性）"),
                subPage_train_VITS.findChildWidget("训练参数", None, "配置加载路径"),
                subPage_train_VITS.findChildWidget("训练参数", "高级设置", "进程数量"),
                subPage_train_VITS.findChildWidget("训练参数", None, "使用预训练模型"),
                subPage_train_VITS.findChildWidget("训练参数", None, "预训练G模型路径"),
                subPage_train_VITS.findChildWidget("训练参数", None, "预训练D模型路径"),
                self.ui.LineEdit_Train_VITS_OutputRoot,
                subPage_train_VITS.findChildWidget("输出参数", None, "输出目录名"),
                'config.json',
                subPage_train_VITS.findChildWidget("输出参数", "高级设置", "日志输出目录")
            ],
            terminateMethod = self.task_voiceTraining_vits.terminate,
            finishedEvents = {
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool,
        )
        FunctionSignals.Signal_TaskStatus.connect(
            lambda Task, Status: MessageBoxBase.pop(self,
                QMessageBox.Question, "Ask",
                text = "是否稍后启用tensorboard？",
                buttons = QMessageBox.Yes|QMessageBox.No,
                buttonEvents = {QMessageBox.Yes: lambda: subPage_train_VITS.findChildWidget("启动Tensorboard").click()}
            ) if Task == self.task_voiceTraining_vits.__class__.execute.__qualname__ and Status == TaskStatus.Started else None
        )
        Function_ConfigureCheckBox(
            checkBox = subPage_train_VITS.findChildWidget("训练参数", None, "使用预训练模型", CheckBoxBase),
            checkedEvents = {
                lambda: Function_SetChildWidgetsVisibility(
                    subPage_train_VITS.findChildWidget("训练参数"),
                    childWidgetsVisibility = {
                        subPage_train_VITS.findChildWidget("训练参数", None, "预训练G模型路径"): True,
                        subPage_train_VITS.findChildWidget("训练参数", None, "预训练D模型路径"): True,
                        subPage_train_VITS.findChildWidget("训练参数", None, "保留原说话人（实验性）"): True,
                        subPage_train_VITS.findChildWidget("训练参数", None, "配置加载路径") if subPage_train_VITS.findChildWidget("训练参数", None, "保留原说话人（实验性）", CheckBoxBase).isChecked() else None: True
                    },
                ) : True
            },
            uncheckedEvents = {
                lambda: Function_SetChildWidgetsVisibility(
                    subPage_train_VITS.findChildWidget("训练参数"),
                    childWidgetsVisibility = {
                        subPage_train_VITS.findChildWidget("训练参数", None, "预训练G模型路径"): False,
                        subPage_train_VITS.findChildWidget("训练参数", None, "预训练D模型路径"): False,
                        subPage_train_VITS.findChildWidget("训练参数", None, "保留原说话人（实验性）"): False,
                        subPage_train_VITS.findChildWidget("训练参数", None, "配置加载路径"): False
                    },
                ) : True
            },
        )
        Function_ConfigureCheckBox(
            checkBox = subPage_train_VITS.findChildWidget("训练参数", None, "保留原说话人（实验性）", CheckBoxBase),
            checkedEvents = {
                lambda: Function_SetChildWidgetsVisibility(
                    subPage_train_VITS.findChildWidget("训练参数"),
                    childWidgetsVisibility = {
                        subPage_train_VITS.findChildWidget("训练参数", None, "配置加载路径"): True
                    },
                ) : True,
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Question, "Tip",
                    text = """
                        开启该实验性功能需要注意以下几点：
                        1. 为防止老角色的音色在训练过程中被逐渐遗忘，请保证每个原角色至少有一两条音频参与训练。\n
                        2. 为防止老角色的顺序被重组（导致音色混乱），请在下方设置包含了底模角色信息的配置文件路径。
                    """,
                    buttons = QMessageBox.Yes|QMessageBox.No,
                    buttonEvents = {QMessageBox.No: lambda: subPage_train_VITS.findChildWidget("训练参数", None, "保留原说话人（实验性）", CheckBoxBase).setChecked(False)}
                ) : False
            },
            uncheckedEvents = {
                lambda: Function_SetChildWidgetsVisibility(
                    subPage_train_VITS.findChildWidget("训练参数"),
                    childWidgetsVisibility = {
                        subPage_train_VITS.findChildWidget("训练参数", None, "配置加载路径"): False
                    },
                ) : True
            },
        )

        self.ui.Page_Train.addSubPage(
            QCA.translate('MainWindow', 'VITS2'), subPage_train_VITS
        )

        #############################################################
        ######################## Content: TTS #######################
        #############################################################

        # Guidance
        self.ui.Page_TTS.setHelpBtnEvent(
            lambda: self.showGuidance(
                windowTitle = QCA.translate('MainWindow', "引导（仅出现一次）"),
                images = [
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_TTS.png')),
                    EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/Guidance_Layout.png'))
                ],
                texts = [
                    '欢迎来到语音合成工具界面\n该工具用于将文字转为语音，用户需要提供相应的模型和配置文件',
                    '顶部区域用于切换当前工具类型（目前仅有一种）\n中间区域用于设置当前工具的各项参数；设置完毕后点击底部区域的按钮即可执行当前工具'
                ]
            )
        )

        self.ui.Button_Menu_TTS.clicked.connect(
            lambda: (
                self.ui.Page_TTS.helpButton.click(),
                config.editConfig('Dialog', 'GuidanceShown_TTS', 'True')
            ) if eval(config.getValue('Dialog', 'GuidanceShown_TTS', 'False')) is False else None
        )

        # ParamsManager - GPT-SoVITS
        configPath_tts_gptsovits = EasyUtils.normPath(Path(configDir).joinpath('Config_TTS_GPT-SoVITS.ini'))
        paramsManager_tts_gptsovits = ParamsManager(configPath_tts_gptsovits)

        subPage_tts_gptsovits = SubToolPage(self.ui.Page_TTS, paramsManager_tts_gptsovits)
        subPage_tts_gptsovits.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "全局设置"),
            text = QCA.translate('MainWindow', "推理版本\nGPT-SoVITS模型的推理版本。"),
            items = ['v2', 'v3'],
            section = 'Input params',
            option = 'version',
            defaultValue = 'v2'
        )
        TTS_GPTSoVITS_ModelPathLoadS1_Default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's1bert25hz-5kh-longer-epoch=12-step=369668.ckpt').as_posix()
        subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "GPT模型加载路径\nGPT（s1）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "ckpt类型 (*.ckpt)",
            directory = Path(currentDir).joinpath('模型训练结果', 'GPT-SoVITS').as_posix(),
            section = 'Input params',
            option = 'Model_Path_Load_s1',
            defaultValue = TTS_GPTSoVITS_ModelPathLoadS1_Default,
            placeholderText = TTS_GPTSoVITS_ModelPathLoadS1_Default
        )
        TTS_GPTSoVITS_ModelPathLoadS2G_Default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2G2333k.pth').as_posix()
        subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "SoVITS模型加载路径\nSoVITS（s2G）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = Path(currentDir).joinpath('模型训练结果', 'GPT-SoVITS').as_posix(),
            section = 'Input params',
            option = 'Model_Path_Load_s2G',
            defaultValue = TTS_GPTSoVITS_ModelPathLoadS2G_Default,
            placeholderText = TTS_GPTSoVITS_ModelPathLoadS2G_Default
        )
        TTS_GPTSoVITS_ModelPathLoadS2Gv3_Default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 's1&s2', 's2Gv3.pth').as_posix()
        subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "SoVITSv3底模加载路径\nSoVITSv3（s2G2333k）底模的路径，用于加载lora。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'Input params',
            option = 'Model_Path_Load_s2Gv3',
            defaultValue = TTS_GPTSoVITS_ModelPathLoadS2Gv3_Default,
            placeholderText = TTS_GPTSoVITS_ModelPathLoadS2Gv3_Default
        )
        TTS_GPTSoVITS_ModelDirLoadBert_Default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-roberta-wwm-ext-large').as_posix()
        subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "预训练BERT模型加载路径\n预训练BERT模型（文件夹）的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'Input params',
            option = 'Model_Dir_Load_bert',
            defaultValue = TTS_GPTSoVITS_ModelDirLoadBert_Default,
            placeholderText = TTS_GPTSoVITS_ModelDirLoadBert_Default
        )
        TTS_GPTSoVITS_ModelDirLoadSSL_Default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'chinese-hubert-base').as_posix()
        subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "预训练HuBERT模型加载路径\n预训练HuBERT模型（文件夹）的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'Input params',
            option = 'Model_Dir_Load_ssl',
            defaultValue = TTS_GPTSoVITS_ModelDirLoadSSL_Default,
            placeholderText = TTS_GPTSoVITS_ModelDirLoadSSL_Default
        )
        TTS_GPTSoVITS_ModelDirLoadBigVGAN_Default = Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded', 'nvidia--bigvgan').as_posix()
        subPage_tts_gptsovits.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "预训练BigVGan模型加载路径\n预训练BigVGan模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(modelDir).joinpath('TTS', 'GPT-SoVITS', 'Downloaded')),
            section = 'Input params',
            option = 'Model_Dir_Load_bigvgan',
            defaultValue = TTS_GPTSoVITS_ModelDirLoadBigVGAN_Default,
            placeholderText = TTS_GPTSoVITS_ModelDirLoadBigVGAN_Default
        )
        TTS_GPTSoVITS_AudioDirSave = Path(currentDir).joinpath('语音合成结果', 'GPTSoVITS').as_posix()
        os.makedirs(TTS_GPTSoVITS_AudioDirSave) if not Path(TTS_GPTSoVITS_AudioDirSave).exists() else None
        subPage_tts_gptsovits.addSideBtn(
            text = QCA.translate('MainWindow', "查看输出文件"),
            events = [
                lambda: QFunc.openURL(
                    url = Function_GetParam(TTS_GPTSoVITS_AudioDirSave),
                    createIfNotExist = True
                )
            ]
        )
        self.task_voiceConverting_gptsovits = Execute_Voice_Converting_GPTSoVITS(coreDir, logPath)
        subPage_tts_gptsovits.setExecutor(
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_voiceConverting_gptsovits.execute,
            executeParamTargets = [
                subPage_tts_gptsovits.findChildWidget("全局设置", None, "推理版本"),
                subPage_tts_gptsovits.findChildWidget("输入参数", None, "SoVITS模型加载路径"),
                subPage_tts_gptsovits.findChildWidget("输入参数", None, "SoVITSv3底模加载路径"),
                subPage_tts_gptsovits.findChildWidget("输入参数", None, "GPT模型加载路径"),
                subPage_tts_gptsovits.findChildWidget("输入参数", None, "预训练HuBERT模型加载路径"),
                subPage_tts_gptsovits.findChildWidget("输入参数", None, "预训练BERT模型加载路径"),
                subPage_tts_gptsovits.findChildWidget("输入参数", None, "预训练BigVGan模型加载路径"),
            ],
            terminateMethod = self.task_voiceConverting_gptsovits.terminate,
            finishedEvents = {
                # lambda: self.showMask(True, "正在加载播放器"): TaskStatus.Succeeded,
                # lambda: self.showTTSResult(
                #     TTS_GPTSoVITS_AudioDirSave
                # ): TaskStatus.Succeeded,
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool,
        )
        Function_ConfigureComboBox(
            comboBox = subPage_tts_gptsovits.findChildWidget("全局设置", None, "推理版本", ComboBoxBase),
            textChangedEvents = {
                "v2": lambda: Function_SetChildWidgetsVisibility(
                    container = subPage_tts_gptsovits.findChildWidget("输入参数"),
                    childWidgetsVisibility = {
                        subPage_tts_gptsovits.findChildWidget("输入参数", None, "SoVITSv3底模加载路径"): False,
                        subPage_tts_gptsovits.findChildWidget("输入参数", None, "预训练BigVGan模型加载路径"): False,
                    },
                ),
                "v3": lambda: Function_SetChildWidgetsVisibility(
                    container = subPage_tts_gptsovits.findChildWidget("输入参数"),
                    childWidgetsVisibility = {
                        subPage_tts_gptsovits.findChildWidget("输入参数", None, "SoVITSv3底模加载路径"): True,
                        subPage_tts_gptsovits.findChildWidget("输入参数", None, "预训练BigVGan模型加载路径"): True,
                    },
                ),
            },
            takeEffect = True
        )

        self.ui.Page_TTS.addSubPage(
            QCA.translate('MainWindow', 'GPT-SoVITS'), subPage_tts_gptsovits
        )

        # ParamsManager - VITS
        configPath_TTS_VITS = EasyUtils.normPath(Path(configDir).joinpath('Config_TTS_VITS.ini'))
        paramsManager_TTS_VITS = ParamsManager(configPath_TTS_VITS)
     
        subPage_TTS_VITS = SubToolPage(self.ui.Page_TTS, paramsManager_TTS_VITS)
        TTS_VITS_ConfigPathLoad_Default = Path(modelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_Config.json').as_posix()
        subPage_TTS_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "配置加载路径\n用于推理的配置文件的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "json类型 (*.json)",
            directory = Path(currentDir).joinpath('模型训练结果', 'VITS').as_posix(),
            section = 'Input params',
            option = 'Config_Path_Load',
            defaultValue = '',
            placeholderText = TTS_VITS_ConfigPathLoad_Default
        )
        subPage_TTS_VITS.findChildWidget("输入参数", None, "配置加载路径", LineEditBase).textChanged.connect(
            lambda Path: (
                subPage_TTS_VITS.findChildWidget("语音合成参数", None, "人物名字", ComboBoxBase).clear(),
                subPage_TTS_VITS.findChildWidget("语音合成参数", None, "人物名字", ComboBoxBase).addItems(Get_Speakers(Path))
            )
        )
        TTS_VITS_ModelPathLoad_Default = Path(modelDir).joinpath('TTS', 'VITS', 'Downloaded', 'standard_G.pth').as_posix()
        subPage_TTS_VITS.addLineEditFrame(
            rootItemText = QCA.translate('MainWindow', "输入参数"),
            text = QCA.translate('MainWindow', "G模型加载路径\n用于推理的生成器（Generator）模型的路径。"),
            fileDialogMode = FileDialogMode.SelectFile,
            fileType = "pth类型 (*.pth)",
            directory = Path(currentDir).joinpath('模型训练结果', 'VITS').as_posix(),
            section = 'Input params',
            option = 'Model_Path_Load',
            defaultValue = '',
            placeholderText = TTS_VITS_ModelPathLoad_Default
        )
        subPage_TTS_VITS.addTextEditFrame(
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            text = QCA.translate('MainWindow', "输入文字\n输入的文字会作为说话人的语音内容。"),
            section = 'VITS params',
            option = 'text',
            defaultValue = '',
            placeholderText = '请输入语句'
        )
        subPage_TTS_VITS.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            text = QCA.translate('MainWindow', "所属语言\n文字所属的语言，若使用自动检测则保持'None'即可（有概率报错）。"),
            items = ['None', QCA.translate('MainWindow', '中'), QCA.translate('MainWindow', '英'), QCA.translate('MainWindow', '日')],
            section = 'VITS params',
            option = 'Language',
            defaultValue = None,
            emptyAllowed = True
        )
        subPage_TTS_VITS.addComboBoxFrame(
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            text = QCA.translate('MainWindow', "人物名字\n说话人物的名字。"),
            items = [],
            section = 'VITS params',
            option = 'Speaker',
            defaultValue = '',
            emptyAllowed = True
        )
        subPage_TTS_VITS.addRangeSettingFrame(
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            text = QCA.translate('MainWindow', "情感强度\n情感的变化程度。"),
            minimum = 0,
            maximum = 1,
            step = 0.01,
            section = 'VITS params',
            option = 'EmotionStrength',
            defaultValue = 0.67
        )
        subPage_TTS_VITS.addRangeSettingFrame(
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            text = QCA.translate('MainWindow', "音素音长\n音素的发音长度。"),
            minimum = 0,
            maximum = 1,
            step = 0.1,
            section = 'VITS params',
            option = 'PhonemeDuration',
            defaultValue = 0.8
        )
        subPage_TTS_VITS.addRangeSettingFrame(
            rootItemText = QCA.translate('MainWindow', "语音合成参数"),
            text = QCA.translate('MainWindow', "整体语速\n整体的说话速度。"),
            minimum = 0,
            maximum = 20,
            step = 1,
            section = 'VITS params',
            option = 'SpeechRate',
            defaultValue = 1.
        )
        TTS_VITS_AudioDirSave = Path(currentDir).joinpath('语音合成结果', 'VITS').as_posix()
        TTS_VITS_AudioPathSave = Path(TTS_VITS_AudioDirSave).joinpath("temp.wav").as_posix()
        os.makedirs(TTS_VITS_AudioDirSave) if not Path(TTS_VITS_AudioDirSave).exists() else None
        subPage_TTS_VITS.addSideBtn(
            text = QCA.translate('MainWindow', "查看输出文件"),
            events = [
                lambda: QFunc.openURL(
                    url = Function_GetParam(TTS_VITS_AudioDirSave),
                    createIfNotExist = True
                )
            ]
        )
        self.task_voiceConverting_vits = Execute_Voice_Converting_VITS(coreDir, logPath)
        subPage_TTS_VITS.setExecutor(
            consoleWidget = self.ui.Frame_Console,
            executeMethod = self.task_voiceConverting_vits.execute,
            executeParamTargets = [
                subPage_TTS_VITS.findChildWidget("语音合成参数", None, "配置加载路径"),
                subPage_TTS_VITS.findChildWidget("语音合成参数", None, "G模型加载路径"),
                subPage_TTS_VITS.findChildWidget("语音合成参数", None, "输入文字"),
                subPage_TTS_VITS.findChildWidget("语音合成参数", None, "所属语言"),
                subPage_TTS_VITS.findChildWidget("语音合成参数", None, "人物名字"),
                subPage_TTS_VITS.findChildWidget("语音合成参数", "高级设置", "情感强度"),
                subPage_TTS_VITS.findChildWidget("语音合成参数", "高级设置", "音素音长"),
                subPage_TTS_VITS.findChildWidget("语音合成参数", "高级设置", "整体语速"),
                TTS_VITS_AudioPathSave
            ],
            terminateMethod = self.task_voiceConverting_vits.terminate,
            finishedEvents = {
                lambda: self.showMask(True, "正在加载播放器"): TaskStatus.Succeeded,
                lambda: self.showTTSResult(
                    TTS_VITS_AudioPathSave
                ): TaskStatus.Succeeded,
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "当前任务已执行结束。"
                ): TaskStatus.Succeeded
            },
            threadPool = self.threadPool,
        )

        self.ui.Page_TTS.addSubPage(
            QCA.translate('MainWindow', 'VITS2'), subPage_TTS_VITS
        )

        #############################################################
        ##################### Content: Settings #####################
        #############################################################

        # Client
        self.ui.Button_Settings_Title_Client.setText(QCA.translate('MainWindow', "系统选项"))
        self.ui.Button_Settings_Title_Client.setHorizontal(True)
        self.ui.Button_Settings_Title_Client.setChecked(True)
        self.ui.Button_Settings_Title_Client.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Settings,
                target = 0
            )
        )

        self.ui.GroupBox_Settings_Client_Outlook.setTitle(QCA.translate('MainWindow', "外观设置"))

        self.ui.Label_Setting_Theme.setText(QCA.translate('MainWindow', "主题"))
        self.ui.ComboBox_Setting_Theme.addItems([QCA.translate('MainWindow', '跟随系统'), QCA.translate('MainWindow', '亮色'), QCA.translate('MainWindow', '暗色')])
        ThemeDict = {
            '跟随系统': Theme.Auto,
            '亮色': Theme.Light,
            '暗色': Theme.Dark
        }
        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.ui.ComboBox_Setting_Theme.setCurrentText(
                QCA.translate('MainWindow', EasyUtils.findKey(ThemeDict, Theme))
            )
        )
        self.ui.ComboBox_Setting_Theme.currentIndexChanged.connect(
            lambda: (
                config.editConfig(
                    'Settings', 'Theme', ThemeDict.get(self.ui.ComboBox_Setting_Theme.currentText())
                ),
                ComponentsSignals.Signal_SetTheme.emit(
                    ThemeDict.get(self.ui.ComboBox_Setting_Theme.currentText())
                ) if currentTheme() != ThemeDict.get(self.ui.ComboBox_Setting_Theme.currentText()) else None
            )
        )

        self.ui.Label_Setting_Language.setText(QCA.translate('MainWindow', "语言"))
        self.ui.ComboBox_Setting_Language.addItems([QCA.translate('MainWindow', '跟随系统'), QCA.translate('MainWindow', '中文'), QCA.translate('MainWindow', '英文')])
        LanguageDict = {
            '跟随系统': Language.Auto,
            '中文': Language.ZH,
            '英文': Language.EN
        }
        ComponentsSignals.Signal_SetLanguage.connect(
            lambda Language: self.ui.ComboBox_Setting_Language.setCurrentText(
                QCA.translate('MainWindow', EasyUtils.findKey(LanguageDict, Language))
            )
        )
        self.ui.ComboBox_Setting_Language.currentIndexChanged.connect(
            lambda: (
                config.editConfig(
                    'Settings', 'Language', LanguageDict.get(self.ui.ComboBox_Setting_Language.currentText())
                ),
                ComponentsSignals.Signal_SetLanguage.emit(
                    LanguageDict.get(self.ui.ComboBox_Setting_Language.currentText())
                ) if currentLanguage() != LanguageDict.get(self.ui.ComboBox_Setting_Language.currentText()) else None
            )
        )

        self.ui.GroupBox_Settings_Client_Function.setTitle(QCA.translate('MainWindow', "功能设置"))

        self.ui.Label_Setting_AutoUpdate.setText(QCA.translate('MainWindow', "自动检查版本并更新"))
        self.ui.CheckBox_Setting_AutoUpdate.setChecked(
            {
                'Enabled': True,
                'Disabled': False
            }.get(config.getValue('Settings', 'AutoUpdate', 'Enabled'))
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Setting_AutoUpdate,
            checkedText = "已启用",
            checkedEvents = {
                lambda: config.editConfig('Settings', 'AutoUpdate', 'Enabled') : True,
            },
            uncheckedText = "未启用",
            uncheckedEvents = {
                lambda: config.editConfig('Settings', 'AutoUpdate', 'Disabled'): True
            },
        )

        self.ui.GroupBox_Settings_Client_Operation.setTitle(QCA.translate('MainWindow', "操作"))

        Function_SetMethodExecutor(
            executeButton = self.ui.Button_Setting_IntegrityChecker,
            executeMethod = checkIntegrity,
            threadPool = self.threadPool,
            parentWindow = self,
        )
        FunctionSignals.Signal_TaskStatus.connect(
            lambda Task, Status: self.ui.Button_Setting_IntegrityChecker.setCheckable(
                False if Status == TaskStatus.Started else True
            )
        )
        self.ui.Button_Setting_IntegrityChecker.setText(QCA.translate('MainWindow', "检查完整性"))
        self.ui.Button_Setting_IntegrityChecker.setToolTip(QCA.translate('MainWindow', "检查文件完整性"))

        # Tools
        self.ui.Button_Settings_Title_Tools.setText(QCA.translate('MainWindow', "工具选项"))
        self.ui.Button_Settings_Title_Tools.setHorizontal(True)
        self.ui.Button_Settings_Title_Tools.setChecked(False)
        self.ui.Button_Settings_Title_Tools.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.ui.StackedWidget_Pages_Settings,
                target = 1
            )
        )

        self.ui.GroupBox_Settings_Tools_Function.setTitle(QCA.translate('MainWindow', "功能设置"))

        self.ui.Label_Setting_AutoReset.setText(QCA.translate('MainWindow', "启动时重置所有工具的参数设置"))
        self.ui.CheckBox_Setting_AutoReset.setChecked(
            {
                'Enabled': True,
                'Disabled': False
            }.get(config.getValue('Tools', 'AutoReset', 'Enabled'))
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Setting_AutoReset,
            checkedText = "已启用",
            checkedEvents = {
                lambda: config.editConfig('Tools', 'AutoReset', 'Enabled') : True,
                lambda: self.Signal_MainWindowShown.connect(
                    lambda: (
                        paramsManager_process.resetSettings(),
                        paramsManager_VPR_TDNN.resetSettings(),
                        paramsManager_ASR_Whisper.resetSettings(),
                        paramsManager_DAT_GPTSoVITS.resetSettings(),
                        paramsManager_DAT_VITS.resetSettings(),
                        paramsManager_train_gptsovits.resetSettings(),
                        paramsManager_Train_VITS.resetSettings(),
                        paramsManager_tts_gptsovits.resetSettings(),
                        paramsManager_TTS_VITS.resetSettings()
                    )
                ) : True
            },
            uncheckedText = "未启用",
            uncheckedEvents = {
                lambda: config.editConfig('Tools', 'AutoReset', 'Disabled') : True,
            },
        )

        self.ui.Label_Setting_Synchronizer.setText(QCA.translate('MainWindow', "自动关联前后工具的部分参数设置"))
        self.ui.CheckBox_Setting_Synchronizer.setChecked(
            {
                'Enabled': True,
                'Disabled': False
            }.get(config.getValue('Tools', 'Synchronizer', 'Enabled'))
        )
        Function_ConfigureCheckBox(
            checkBox = self.ui.CheckBox_Setting_Synchronizer,
            checkedText = "已启用",
            checkedEvents = {
                lambda: config.editConfig('Tools', 'Synchronizer', 'Enabled') : True,
                lambda: Function_ParamsSynchronizer(
                    LineEdit_Process_OutputDir,
                    {LineEdit_Process_OutputDir: subPage_VPR.findChildWidget("输入参数", None, "音频输入目录", LineEditBase)}
                ) : True,
                lambda: Function_ParamsSynchronizer(
                    LineEdit_VPR_TDNN_AudioSpeakersDataPath,
                    {LineEdit_VPR_TDNN_AudioSpeakersDataPath: [subPage_dataset_GPTSoVITS.findChildWidget("输入参数", None, "音频文件目录/语音识别结果文本路径", LineEditBase), subPage_dataset_VITS.findChildWidget("输入参数", None, "音频文件目录/语音识别结果文本路径", LineEditBase)]}
                ) : True,
                lambda: Function_ParamsSynchronizer(
                    LineEdit_VPR_TDNN_OutputDir,
                    {LineEdit_VPR_TDNN_OutputDir: subPage_ASR.findChildWidget("输入参数", None, "音频输入目录", LineEditBase)}
                ) : True,
                lambda: Function_ParamsSynchronizer(
                    LineEdit_ASR_Whisper_OutputDir,
                    {LineEdit_ASR_Whisper_OutputDir: [subPage_dataset_GPTSoVITS.findChildWidget("输入参数", None, "字幕输入目录", LineEditBase), subPage_dataset_VITS.findChildWidget("输入参数", None, "字幕输入目录", LineEditBase)]}
                ) : True,
                lambda: Function_ParamsSynchronizer(
                    LineEdit_DAT_GPTSoVITS_FileListPath,
                    {LineEdit_DAT_GPTSoVITS_FileListPath: subPage_train_gptsovits.findChildWidget("输入参数", None, "训练集文本路径", LineEditBase)}
                ) : True,
                lambda: Function_ParamsSynchronizer(
                    [LineEdit_DAT_VITS_FileListPathTraining, LineEdit_DAT_VITS_FileListPathValidation],
                    {LineEdit_DAT_VITS_FileListPathTraining: subPage_train_VITS.findChildWidget("输入参数", None, "训练集文本路径", LineEditBase), LineEdit_DAT_VITS_FileListPathValidation: subPage_train_VITS.findChildWidget("输入参数", None, "验证集文本路径", LineEditBase)}
                ) : True
            },
            uncheckedText = "未启用",
            uncheckedEvents = {
                lambda: config.editConfig('Tools', 'Synchronizer', 'Disabled') : True,
                lambda: MessageBoxBase.pop(self,
                    QMessageBox.Information, "Tip",
                    "该设置将于重启之后生效"
                ) : False
            },
        )

        self.ui.GroupBox_Settings_Tools_Path.setTitle(QCA.translate('MainWindow', "路径设置"))

        self.ui.Label_Process_OutputRoot.setText(QCA.translate('MainWindow', "音频处理输出目录"))
        Process_OutputRoot_Default = Path(outputDir).joinpath('音频处理结果').as_posix()
        paramsManager_process.setParam(
            widget = self.ui.LineEdit_Process_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = Process_OutputRoot_Default,
            placeholderText = Process_OutputRoot_Default
        )
        self.ui.LineEdit_Process_OutputRoot.setFileDialog(
            mode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(Process_OutputRoot_Default).parent)
        )
        self.ui.Button_Process_OutputRoot_MoreActions.setMenu(
            actionEvents = {
                "重置": lambda: paramsManager_process.resetParam(self.ui.LineEdit_Process_OutputRoot)
            }
        )

        self.ui.Label_VPR_TDNN_OutputRoot.setText(QCA.translate('MainWindow', "声纹识别结果输出目录"))
        VPR_TDNN_AudioSpeakersDataRoot_Default = Path(currentDir).joinpath('语音识别结果', 'VPR').as_posix()
        paramsManager_VPR_TDNN.setParam(
            widget = self.ui.LineEdit_VPR_TDNN_OutputRoot,
            section = 'Output params',
            option = 'Audio_Root_Output',
            defaultValue = VPR_TDNN_AudioSpeakersDataRoot_Default,
            placeholderText = VPR_TDNN_AudioSpeakersDataRoot_Default
        )
        self.ui.LineEdit_VPR_TDNN_OutputRoot.setFileDialog(
            mode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(VPR_TDNN_AudioSpeakersDataRoot_Default).parent)
        )
        self.ui.Button_VPR_TDNN_OutputRoot_MoreActions.setMenu(
            actionEvents = {
                "重置": lambda: paramsManager_VPR_TDNN.resetParam(self.ui.LineEdit_VPR_TDNN_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_VPR_TDNN_OutputRoot.text())
            }
        )

        self.ui.Label_ASR_Whisper_OutputRoot.setText(QCA.translate('MainWindow', "Whisper转录输出目录"))
        ASR_Whisper_OutputRoot_Default = Path(outputDir).joinpath('语音转录结果', 'Whisper').as_posix()
        paramsManager_ASR_Whisper.setParam(
            widget = self.ui.LineEdit_ASR_Whisper_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = ASR_Whisper_OutputRoot_Default,
            placeholderText = ASR_Whisper_OutputRoot_Default
        )
        self.ui.LineEdit_ASR_Whisper_OutputRoot.setFileDialog(
            mode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(ASR_Whisper_OutputRoot_Default).parent)
        )
        self.ui.Button_ASR_Whisper_OutputRoot_MoreActions.setMenu(
            actionEvents = {
                "重置": lambda: paramsManager_ASR_Whisper.resetParam(self.ui.LineEdit_ASR_Whisper_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_ASR_Whisper_OutputRoot.text())
            }
        )

        self.ui.Label_DAT_GPTSoVITS_OutputRoot.setText( QCA.translate('MainWindow', "GPTSoVITS数据集输出目录"))
        DAT_GPTSoVITS_OutputRoot_Default = Path(outputDir).joinpath('数据集制作结果', 'GPT-SoVITS').as_posix()
        paramsManager_DAT_GPTSoVITS.setParam(
            widget = self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = DAT_GPTSoVITS_OutputRoot_Default,
            placeholderText = DAT_GPTSoVITS_OutputRoot_Default
        )
        self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot.setFileDialog(
            mode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(DAT_GPTSoVITS_OutputRoot_Default).parent)
        )
        self.ui.Button_DAT_GPTSoVITS_OutputRoot_MoreActions.setMenu(
            actionEvents = {
                "重置": lambda: paramsManager_DAT_GPTSoVITS.resetParam(self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_GPTSoVITS_OutputRoot.text())
            }
        )

        self.ui.Label_DAT_VITS_OutputRoot.setText(QCA.translate('MainWindow', "VITS数据集输出目录"))
        DAT_VITS_OutputRoot_Default = Path(outputDir).joinpath('数据集制作结果', 'VITS').as_posix()
        paramsManager_DAT_VITS.setParam(
            widget = self.ui.LineEdit_DAT_VITS_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = DAT_VITS_OutputRoot_Default,
            placeholderText = DAT_VITS_OutputRoot_Default
        )
        self.ui.LineEdit_DAT_VITS_OutputRoot.setFileDialog(
            mode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(DAT_VITS_OutputRoot_Default).parent)
        )
        self.ui.Button_DAT_VITS_OutputRoot_MoreActions.setMenu(
            actionEvents = {
                "重置": lambda: paramsManager_DAT_VITS.resetParam(self.ui.LineEdit_DAT_VITS_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_DAT_VITS_OutputRoot.text())
            }
        )

        self.ui.Label_Train_GPTSoVITS_OutputRoot.setText(QCA.translate('MainWindow', "GPTSoVITS训练输出目录"))
        Train_GPTSoVITS_OutputRoot_Default = Path(outputDir).joinpath('模型训练结果', 'GPT-SoVITS').as_posix()
        paramsManager_train_gptsovits.setParam(
            widget = self.ui.LineEdit_Train_GPTSoVITS_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = Train_GPTSoVITS_OutputRoot_Default,
            placeholderText = Train_GPTSoVITS_OutputRoot_Default
        )
        self.ui.LineEdit_Train_GPTSoVITS_OutputRoot.setFileDialog(
            mode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(Train_GPTSoVITS_OutputRoot_Default).parent)
        )
        self.ui.Button_Train_GPTSoVITS_OutputRoot_MoreActions.setMenu(
            actionEvents = {
                "重置": lambda: paramsManager_train_gptsovits.resetParam(self.ui.LineEdit_Train_GPTSoVITS_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_GPTSoVITS_OutputRoot.text())
            }
        )

        self.ui.Label_Train_VITS_OutputRoot.setText(QCA.translate('MainWindow', "VITS训练输出目录"))
        Train_VITS_OutputRoot_Default = Path(outputDir).joinpath('模型训练结果', 'VITS').as_posix()
        paramsManager_Train_VITS.setParam(
            widget = self.ui.LineEdit_Train_VITS_OutputRoot,
            section = 'Output params',
            option = 'Output_Root',
            defaultValue = Train_VITS_OutputRoot_Default,
            placeholderText = Train_VITS_OutputRoot_Default
        )
        self.ui.LineEdit_Train_VITS_OutputRoot.setFileDialog(
            mode = FileDialogMode.SelectFolder,
            directory = EasyUtils.normPath(Path(Train_VITS_OutputRoot_Default).parent)
        )
        self.ui.Button_Train_VITS_OutputRoot_MoreActions.setMenu(
            actionEvents = {
                "重置": lambda: paramsManager_Train_VITS.resetParam(self.ui.LineEdit_Train_VITS_OutputRoot),
                "复制": lambda: QApplication.clipboard().setText(self.ui.LineEdit_Train_VITS_OutputRoot.text())
            }
        )

        #############################################################
        ####################### Content: Info #######################
        #############################################################

        self.ui.Button_Info_Title.setText(QCA.translate('MainWindow', "用户须知"))

        QFunc.setText(
            widget = self.ui.TextBrowser_Text_Info,
            text = EasyUtils.richTextManager().addTitle(
                text = QCA.translate('MainWindow', "声明"),
                align = "left",
                size = 24,
                weight = 840
            ).addBody(
                text = QCA.translate('MainWindow',
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
                align = "left",
                size = 12,
                weight = 420,
                lineHeight = 27
            ).richText()
        )

        #############################################################
        ###################### Content: Console #####################
        #############################################################

        self.ui.Button_Console_Title.setText(QCA.translate('MainWindow', "终端"))

        MonitorLog = QTasks.MonitorLogFile(logPath)
        MonitorLog.start()
        MonitorLog.Signal_ConsoleInfo.connect(
            lambda Info: (
                self.ui.PlainTextEdit_Console.setPlainText(Info),
                self.ui.PlainTextEdit_Console.moveCursor(QTextCursor.End)
            )
        )

        self.ui.Button_Console_Copy.clicked.connect(
            lambda: (
                QApplication.clipboard().setText(self.ui.PlainTextEdit_Console.toPlainText()),
                MessageBoxBase.pop(self, windowTitle = "Tip", text = "已复制输出日志到剪切板")
            )
        )

        self.ui.Button_Console_Clear.clicked.connect(MonitorLog.clear)

        self.ui.Button_Console_Fold.clicked.connect(self.ui.Button_Toggle_Console.click)

        #############################################################
        ######################### StatusBar #########################
        #############################################################

        # Toggle Console
        self.ui.Button_Toggle_Console.setToolTip(QCA.translate('MainWindow', "点击以展开/折叠终端"))
        self.ui.Button_Toggle_Console.clicked.connect(
            lambda: Function_AnimateFrame(
                frame = self.ui.Frame_Console,
                minHeight = 0,
                maxHeight = 210,
                supportSplitter = True
            )
        )
        self.ui.Frame_Console.setFixedHeight(0)

        # Display ToolsStatus
        self.ui.Label_ToolsStatus.clear()
        FunctionSignals.Signal_TaskStatus.connect(
            lambda Task, Status: self.ui.Label_ToolsStatus.setText(
                f"工具状态：{'忙碌' if Status == TaskStatus.Started else '空闲'}"
            ) if Task in [
                self.task_audioProcessing.__class__.execute.__qualname__,
                self.task_voiceIdentifying_vpr.__class__.execute.__qualname__,
                self.task_voiceTranscribing_whisper.__class__.execute.__qualname__,
                self.task_datasetCreating_gptsovits.__class__.execute.__qualname__,
                self.task_datasetCreating_vits.__class__.execute.__qualname__,
                self.task_voiceTraining_gptsovits.__class__.execute.__qualname__,
                self.task_voiceTraining_vits.__class__.execute.__qualname__,
                self.task_voiceConverting_gptsovits.__class__.execute.__qualname__,
                self.task_voiceConverting_vits.__class__.execute.__qualname__
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
        self.ui.Label_Version.setText(currentVersion)

        # Set Theme
        ComponentsSignals.Signal_SetTheme.emit(config.getValue('Settings', 'Theme', Theme.Auto))

        # Set Language
        ComponentsSignals.Signal_SetLanguage.emit(config.getValue('Settings', 'Language', Language.Auto))

        # Show MainWindow (and emit signal)
        self.show()
        self.Signal_MainWindowShown.emit()

##############################################################################################################################

if __name__ == "__main__":
    App = QApplication(sys.argv)

    # Create&Show SplashScreen
    SC = QSplashScreen(QPixmap(EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/others/SplashScreen.png'))))
    #SC.showMessage('Loading...', alignment = Qt.AlignmentFlag.AlignCenter)
    SC.show()

    # Init&Show MainWindow
    MW = MainWindow()
    MW.main()

    # Close SplashScreen
    SC.finish(MW) #SC.close()

    sys.exit(App.exec())

##############################################################################################################################