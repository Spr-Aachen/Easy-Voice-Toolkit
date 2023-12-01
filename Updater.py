import os
import sys
import shutil
from pathlib import Path
from typing import Optional
from PySide6.QtCore import Qt, QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizePolicy, QPushButton, QProgressBar, QLabel

from EVT_GUI.Functions import Function_AnimateProgressBar, Function_SetText#, Function_ShowMessageBox
from EVT_GUI.QSimpleWidgets.Utils import CheckUpdate, DownloadFile, NormPath, RunBat, BootWithBat, GetFileInfo, GetBaseDir, ManageConfig

##############################################################################################################################

_, IsFileCompiled = GetFileInfo()


TargetDir = GetBaseDir(__file__ if IsFileCompiled == False else sys.executable)
#os.chdir(TargetDir)


ConfigPath = NormPath(Path(TargetDir).joinpath('Config', 'Config.ini'))
Config = ManageConfig(ConfigPath)


CurrentVersion = str(Config.GetValue('Info', 'CurrentVersion'))
ExecuterName = str(Config.GetValue('Info', 'ExecuterName'))
DownloadDir = TargetDir
ExtractDir = NormPath(Path(TargetDir).joinpath('Temp'))
ExecuterPath = NormPath(Path(TargetDir).joinpath(ExecuterName))


FoldersToKeep = [NormPath(Path(TargetDir).joinpath('Config'))]
if Path(TargetDir).joinpath('FFmpeg').exists():
    FoldersToKeep.append(NormPath(Path(TargetDir).joinpath('FFmpeg')))
if Path(TargetDir).joinpath('Python').exists():
    FoldersToKeep.append(NormPath(Path(TargetDir).joinpath('Python')))
if Path(TargetDir).joinpath('Download').exists():
    FoldersToKeep.append(NormPath(Path(TargetDir).joinpath('Download')))

##############################################################################################################################

# Where to store custom signals
class CustomSignals_Updater(QObject):
    '''
    Set up signals for updater
    '''
    Signal_ExecuteTask = Signal(tuple)

    Signal_Message = Signal(str)

    Signal_IsUpdateSucceeded = Signal(bool)


UpdaterSignals = CustomSignals_Updater()


def RebootIfFailed():
    BootWithBat(
        ProgramPath = ExecuterPath,
        DelayTime = 0,
        BatFilePath = Path(NormPath(TargetDir)).joinpath('Booter.bat')
    )


def RebootIfSucceeded():
    RunBat(
        CommandList = [
            '@echo off',
            'echo Moving files...',
            f'xcopy /e /y "{ExtractDir}\*" "{TargetDir}\"',
            f'rmdir /q /s "{ExtractDir}"',
            f'start "Programm Running" "{ExecuterPath}"',
            'del "%~f0"'
        ],
        BatFilePath = NormPath(Path(TargetDir).joinpath('Updater.bat'))
    )


def Updater(
    CurrentVersion: str = ...,
    DownloadDir: str = ...,
    Name: str = ...,
    ExtractDir: str = ...,
    TargetDir: str = ...,
    #ExecuterPath: str = ...
):
    '''
    '''
    try:
        UpdaterSignals.Signal_Message.emit("正在检查更新，请稍等...\nChecking for updates, please wait...")
        IsUpdateNeeded, DownloadURL = CheckUpdate(
            RepoOwner = 'Spr-Aachen',
            RepoName = 'Easy-Voice-Toolkit',
            FileName = 'EVT',
            FileFormat = 'zip',
            Version_Current = CurrentVersion
        )

    except:
        UpdaterSignals.Signal_Message.emit("更新检查失败！\nFailed to check for updates!")
        UpdaterSignals.Signal_IsUpdateSucceeded.emit(False)

    else:
        if IsUpdateNeeded:
            try:
                # Download
                UpdaterSignals.Signal_Message.emit("正在下载文件...\nDownloading files...")
                FileInfo = DownloadFile(
                    DownloadURL = DownloadURL,
                    DownloadDir = DownloadDir,
                    FileName = Name,
                    FileFormat = 'zip',
                    SHA_Expected = None
                )
            except Exception as e:
                UpdaterSignals.Signal_Message.emit("文件下载失败！\nFailed to download files!")
                #Function_ShowMessageBox(WindowTitle = 'Error', Text = f'Error occurred while downloading files: {e}')
                UpdaterSignals.Signal_IsUpdateSucceeded.emit(False)
            else:
                # Unpack
                UpdaterSignals.Signal_Message.emit("正在解压文件...\nUnpacking files...")
                ExtractDir = NormPath(Path(TargetDir).joinpath('Temp')) if ExtractDir == TargetDir else ExtractDir
                shutil.unpack_archive(
                    filename = FileInfo[1],
                    extract_dir = ExtractDir
                )
                os.remove(FileInfo[1])
                # Cover old files (About to finish)
                UpdaterSignals.Signal_Message.emit("即将重启客户端...\nRebooting client...")
                '''
                CleanDirectory(
                    Directory = TargetDir,
                    WhiteList = [os.path.basename(ExtractDir), '__pycache__', '.git'].extend(FoldersToKeep)
                )
                shutil.copytree(ExtractDir, TargetDir, dirs_exist_ok = True)
                shutil.rmtree(ExtractDir)
                '''
                UpdaterSignals.Signal_IsUpdateSucceeded.emit(True)
        else:
            UpdaterSignals.Signal_Message.emit("已是最新版本！\nAlready up to date!")
            UpdaterSignals.Signal_IsUpdateSucceeded.emit(False)


class Execute_Update_Checking(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    def Execute(self):
        Updater(
            CurrentVersion = CurrentVersion,
            DownloadDir = DownloadDir,
            Name = f"Easy Voice Toolkit {Config.GetValue('Info', 'CurrentVersion')}",
            ExtractDir = ExtractDir,
            TargetDir = TargetDir
        )

        self.finished.emit()


# Show GUI
class Widget_Updater(QWidget):
    '''
    '''
    def __init__(self):
        super().__init__(
            parent = None,
            f = Qt.Widget #| Qt.FramelessWindowHint
        )

        self.setMaximumSize(246, 123)
        self.setGeometry(
            QApplication.primaryScreen().size().width() // 2 - self.width() // 2,
            QApplication.primaryScreen().size().height() // 2 - self.height() // 2,
            self.width(),
            self.height()
        )

        self.Label = QLabel()
        self.Label.setVisible(True)
        self.Label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #self.Label.setStyleSheet("text-align: center; font-size: 11.1px;")
        self.Label.clear()

        self.ExecuteButton = QPushButton()
        self.ExecuteButton.setVisible(False)
        self.ExecuteButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #self.ExecuteButton.setStyleSheet("text-align: center;")

        self.ProgressBar = QProgressBar()
        self.ProgressBar.setVisible(True)
        self.ProgressBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #self.ProgressBar.setStyleSheet("text-align: center;")

        self.SkipButton = QPushButton()
        self.SkipButton.setVisible(True)
        self.SkipButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.SkipButton.setStyleSheet("text-align: center;")

        self.Layout = QVBoxLayout()
        self.Layout.setAlignment(Qt.AlignCenter)
        self.Layout.setContentsMargins(21, 12, 21, 12)
        self.Layout.setSpacing(12)
        self.Layout.addWidget(self.Label)
        self.Layout.addWidget(self.ExecuteButton)
        self.Layout.addWidget(self.ProgressBar)
        self.Layout.addWidget(self.SkipButton)
        self.setLayout(self.Layout)

        UpdaterSignals.Signal_Message.connect(lambda Message: Function_SetText(self.Label, Message, 'center', 9, 420, 'black', 0.3, 12))
        UpdaterSignals.Signal_IsUpdateSucceeded.connect(lambda: Config.EditConfig('Updater', 'Status', 'Executed'), Qt.QueuedConnection)
        UpdaterSignals.Signal_IsUpdateSucceeded.connect(lambda Succeeded: RebootIfSucceeded() if Succeeded else RebootIfFailed(), Qt.QueuedConnection)
        UpdaterSignals.Signal_IsUpdateSucceeded.connect(lambda: self.close(), Qt.QueuedConnection)

    def Function_ExecuteMethod(self,
        ExecuteButton: QPushButton,
        ProgressBar: Optional[QProgressBar] = None,
        Method: object = ...,
        Params: Optional[tuple] = ()
    ):
        ClassName =  str(Method.__qualname__).split('.')[0]
        MethodName = str(Method.__qualname__).split('.')[1]

        ClassInstance = globals()[ClassName]()

        WorkerThread = QThread()
        ClassInstance.moveToThread(WorkerThread)
        ClassInstance.finished.connect(WorkerThread.quit)

        def ExecuteMethod():
            Args = Params

            QFunctionsSignals = CustomSignals_Updater()
            QFunctionsSignals.Signal_ExecuteTask.connect(getattr(ClassInstance, MethodName))

            WorkerThread.started.connect(lambda: Function_AnimateProgressBar(ProgressBar, IsTaskAlive = True)) if ProgressBar else None
            WorkerThread.finished.connect(lambda: Function_AnimateProgressBar(ProgressBar, IsTaskAlive = False)) if ProgressBar else None

            QFunctionsSignals.Signal_ExecuteTask.emit(Args)
            WorkerThread.start()

        ExecuteButton.clicked.connect(ExecuteMethod)

    def Main(self):
        self.Function_ExecuteMethod(
            ExecuteButton = self.ExecuteButton,
            ProgressBar = self.ProgressBar,
            Method = Execute_Update_Checking.Execute,
            Params = ()
        )
        self.ExecuteButton.click()

        self.SkipButton.setText('跳过更新')
        self.SkipButton.clicked.connect(
            lambda: UpdaterSignals.Signal_IsUpdateSucceeded.emit(False)
        )

        self.show()

##############################################################################################################################

if __name__ == "__main__":
    App = QApplication(sys.argv) #App = QApplication([])

    UpdaterWidget = Widget_Updater()
    UpdaterWidget.Main() #UpdaterWidget.show()

    sys.exit(App.exec()) #App.exec()

##############################################################################################################################