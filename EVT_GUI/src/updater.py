import os
import sys
import platform
import shutil
import argparse
from pathlib import Path
from typing import Optional
from PySide6.QtCore import Qt, QObject, QThread, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QVBoxLayout, QSizePolicy, QWidget, QMessageBox, QPushButton, QProgressBar, QLabel
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets.Windows import MessageBoxBase

from functions import FunctionSignals, Function_SetMethodExecutor, Function_UpdateChecker
from config import *

##############################################################################################################################

# Parse path settings
parser = argparse.ArgumentParser()
parser.add_argument("--config",    help = "path to config",    default = Path(currentDir).joinpath('config', 'config.ini'))
args = parser.parse_args()

configPath = args.config

# Set downloadDir&extractDir
downloadDir = currentDir
extractDir = QFunc.normPath(Path(currentDir).joinpath('Temp'))

# Set up client config
config = QFunc.configManager(configPath)

# Set path of executer
executerName = str(config.getValue('Info', 'executerName', ''))
executerPath = QFunc.normPath(Path(currentDir).joinpath(executerName))
bootExecuter = True if executerName.strip() != '' else False

##############################################################################################################################

def RebootIfFailed():
    if platform.system() == 'Windows':
        ScriptName = 'Booter.bat'
    if platform.system() == 'Linux':
        ScriptName = 'Booter.sh'
    if ScriptName:
        QFunc.bootWithScript(
            programPath = executerPath,
            delayTime = 0,
            scriptPath = Path(QFunc.normPath(currentDir)).joinpath(ScriptName)
        )


def RebootIfSucceeded():
    if platform.system() == 'Windows':
        QFunc.runScript(
            commandList = [
                '@echo off',
                'echo Ready to move files and reboot',
                #f'taskkill /pid {os.getpid()} /f /t',
                'timeout /t 2 /nobreak',
                'echo Moving files...',
                f'robocopy "{extractDir}" "{currentDir}" /E /MOVE /R:3 /W:1 /NP',
                f'start "Programm Running" "{executerPath}"',
                'del "%~f0"'
            ],
            scriptPath = QFunc.normPath(Path(currentDir).joinpath('Updater.bat'))
        )
    if platform.system() == 'Linux':
        QFunc.runScript(
            commandList = [
                'echo Ready to move files and reboot',
                #f'kill -9 {os.getpid()}',
                'sleep 2',
                'echo Moving files...',
                f'rsync -a --delete "{extractDir}" "{currentDir}"',
                f'./{executerName}', #f'nohup ./{executerName} &',
                'rm -rf Updater.sh'
            ],
            scriptPath = QFunc.normPath(Path(currentDir).joinpath('Updater.sh'))
        )


def UpdateDownloader(
    downloadURL: str = ...,
    downloadDir: str = ...,
    name: str = ...,
    extractDir: str = ...,
    targetDir: str = ...,
    #executerPath: str = ...
):
    try:
        # Download
        FunctionSignals.Signal_UpdateMessage.emit("正在下载文件...\nDownloading files...")
        FileInfo = QFunc.downloadFile(
            downloadURL = downloadURL,
            downloadDir = downloadDir,
            fileName = name,
            fileFormat = 'zip',
            sha = None
        )
    except Exception as e:
        #FunctionSignals.Signal_UpdateMessage.emit("文件下载失败！\nFailed to download files!")
        FunctionSignals.Signal_IsUpdateSucceeded.emit(False, "文件下载失败！\nFailed to download files!")
    else:
        # Unpack
        FunctionSignals.Signal_UpdateMessage.emit("正在解压文件...\nUnpacking files...")
        extractDir = QFunc.normPath(Path(targetDir).joinpath('Temp')) if extractDir == targetDir else extractDir
        shutil.unpack_archive(
            filename = FileInfo[1],
            extract_dir = extractDir
        )
        os.remove(FileInfo[1])
        # Cover old files (About to finish)
        FunctionSignals.Signal_UpdateMessage.emit("即将重启客户端...\nRebooting client...")
        FunctionSignals.Signal_IsUpdateSucceeded.emit(True, "")


class Execute_Update_Checking(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    def Execute(self):
        Function_UpdateChecker(
            repoOwner = repoOwner,
            repoName = repoName,
            fileName = fileName,
            fileFormat = fileFormat,
            currentVersion = currentVersion
        )

        self.finished.emit()


class Execute_Update_Downloading(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    def Execute(self, downloadURL):
        UpdateDownloader(
            downloadURL = downloadURL,
            downloadDir = downloadDir,
            name = "EVT Update",
            extractDir = extractDir,
            targetDir = currentDir
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

        self.setWindowIcon(QIcon(QFunc.normPath(Path(resourceDir).joinpath('assets/images/Logo.ico'))))

        self.Label = QLabel()
        self.Label.setVisible(True)
        self.Label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #self.Label.setStyleSheet("text-align: center; font-size: 11.1px;")

        self.progressBar = QProgressBar()
        self.progressBar.setVisible(True)
        self.progressBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #self.progressBar.setStyleSheet("text-align: center;")

        self.SkipButton = QPushButton()
        self.SkipButton.setVisible(True)
        self.SkipButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.SkipButton.setStyleSheet("text-align: center;")

        self.Layout = QVBoxLayout(self)
        self.Layout.setAlignment(Qt.AlignCenter)
        self.Layout.setContentsMargins(21, 12, 21, 12)
        self.Layout.setSpacing(12)
        self.Layout.addWidget(self.Label)
        self.Layout.addWidget(self.progressBar)
        self.Layout.addWidget(self.SkipButton)

    def main(self):
        self.downloadURL = str()
        def UpdateDownloadURL(downloadURL):
            self.downloadURL = downloadURL

        FunctionSignals.Signal_UpdateMessage.connect(
            lambda Message: QFunc.setText(
                self.Label,
                QFunc.setRichText(Message, 'center', 9, 420, 0.3, 12)
            )
        )
        FunctionSignals.Signal_ReadyToUpdate.connect(
            lambda downloadURL, VersionInfo: (
                UpdateDownloadURL(downloadURL),
                MessageBoxBase.pop(None,
                    QMessageBox.Question, "Ask",
                    text = "检测到可用的新版本，是否更新？\nNew version available, wanna update?",
                    detailedText = VersionInfo,
                    buttons = QMessageBox.Yes|QMessageBox.No,
                    buttonEvents = {
                        QMessageBox.Yes: lambda: Function_SetMethodExecutor(self,
                            progressBar = self.progressBar,
                            method = Execute_Update_Downloading.Execute,
                            params = (self.downloadURL)
                        ),
                        QMessageBox.No: lambda: FunctionSignals.Signal_IsUpdateSucceeded.emit(False, "已取消下载更新！\nDownload canceled!")
                    }
                )
            ) if eval(config.getValue('Updater', 'Asked', 'False')) is False else (
                Function_SetMethodExecutor(self,
                    progressBar = self.progressBar,
                    method = Execute_Update_Downloading.Execute,
                    params = (self.downloadURL)
                ),
                config.editConfig('Updater', 'Asked', 'False')
            )
        )
        FunctionSignals.Signal_IsUpdateSucceeded.connect(
            lambda Succeeded, Info: (
                MessageBoxBase.pop(None,
                    QMessageBox.Warning, "Warning",
                    text = Info
                ) if not Succeeded else None,
                (RebootIfSucceeded() if Succeeded else RebootIfFailed()) if bootExecuter else None,
                QApplication.instance().exit()
            )
        )

        Function_SetMethodExecutor(self,
            progressBar = self.progressBar,
            method = Execute_Update_Checking.Execute,
            params = ()
        )

        self.SkipButton.setText("跳过")
        self.SkipButton.clicked.connect(
            lambda: FunctionSignals.Signal_IsUpdateSucceeded.emit(False, "")
        )

        self.show()

##############################################################################################################################

if __name__ == "__main__":
    App = QApplication(sys.argv) #App = QApplication([])

    UpdaterWidget = Widget_Updater()
    UpdaterWidget.main() #UpdaterWidget.show()

    sys.exit(App.exec()) #App.exec()

##############################################################################################################################