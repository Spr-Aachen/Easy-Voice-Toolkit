import os
import sys
import platform
import shutil
import argparse
import subprocess
import PyEasyUtils as EasyUtils
from pathlib import Path
from PySide6.QtCore import Qt, QObject, QThreadPool
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QVBoxLayout, QSizePolicy, QWidget, QMessageBox, QPushButton, QProgressBar, QLabel
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets.Windows import MessageBoxBase

from functions import functionSignals, Function_SetMethodExecutor, Function_UpdateChecker
from config import *

##############################################################################################################################

# Get current path
currentPath = EasyUtils.getCurrentPath()

# Get current directory
currentDir = Path(currentPath).parent.as_posix()

# Set directory to load static dependencies
resourceDir = EasyUtils.getBaseDir(searchMEIPASS = True) or currentDir

# Check whether python file is compiled
_, isFileCompiled = EasyUtils.getFileInfo()

##############################################################################################################################

# Parse path settings
parser = argparse.ArgumentParser()
parser.add_argument("--programPath",    help = "path to main program", default = None)
parser.add_argument("--currentVersion", help = "dir of core files",    default = None)
parser.add_argument("--downloadURL",    help = "url for download",     default = None)
args = parser.parse_args()

programPath = args.programPath
currentVersion = args.currentVersion
downloadURL = args.downloadURL

# Set downloadDir&extractDir
programDir = Path(programPath).parent.as_posix()
downloadDir = programDir
extractDir = programDir

##############################################################################################################################

def updateDownloader(
    downloadURL: str = ...,
    downloadDir: str = ...,
    name: str = ...,
    extractDir: str = ...,
):
    try:
        # Download
        functionSignals.updateMessage.emit("正在下载文件...\nDownloading files...")
        fileInfo = EasyUtils.downloadFile(
            downloadURL = downloadURL,
            downloadDir = downloadDir,
            fileName = name,
            fileFormat = 'zip',
            sha = None
        )
    except Exception as e:
        #functionSignals.updateMessage.emit("文件下载失败！\nFailed to download files!")
        functionSignals.isUpdateSucceeded.emit(False, "文件下载失败！\nFailed to download files!")
    else:
        # Unpack
        functionSignals.updateMessage.emit("正在解压文件...\nUnpacking files...")
        try:
            shutil.unpack_archive(
                filename = fileInfo[1],
                extract_dir = extractDir
            )
        except:
            functionSignals.isUpdateSucceeded.emit(False, "文件解压失败！\nFailed to unpack files!")
            return
        os.remove(fileInfo[1])
        # Cover old files (About to finish)
        functionSignals.updateMessage.emit("即将重启客户端...\nRebooting client...")
        functionSignals.isUpdateSucceeded.emit(True, "")


# Show GUI
class MainWindow(QWidget):
    '''
    '''
    def __init__(self):
        super().__init__(
            parent = None,
            f = Qt.Widget #| Qt.FramelessWindowHint
        )

        self.threadPool = QThreadPool()

        self.setMaximumSize(246, 123)
        self.setGeometry(
            QApplication.primaryScreen().size().width() // 2 - self.width() // 2,
            QApplication.primaryScreen().size().height() // 2 - self.height() // 2,
            self.width(),
            self.height()
        )

        self.setWindowIcon(QIcon(EasyUtils.normPath(Path(resourceDir).joinpath('assets/images/Logo.ico'))))

        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.label.setStyleSheet("text-align: center; font-size: 11.1px;")

        self.progressBar = QProgressBar()
        self.progressBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #self.progressBar.setStyleSheet("text-align: center;")
        self.progressBar.setTextVisible(False)

        self.skipButton = QPushButton()
        self.skipButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.skipButton.setStyleSheet("text-align: center;")

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(21, 12, 21, 12)
        layout.setSpacing(12)
        layout.addWidget(self.label)
        layout.addWidget(self.progressBar)
        layout.addWidget(self.skipButton)

    def checkUpdate(self):
        Function_SetMethodExecutor(
            executeMethod = Function_UpdateChecker,
            executeParams = (
                repoOwner,
                repoName,
                fileName,
                fileFormat,
                currentVersion
            ),
            progressBar = self.progressBar,
            threadPool = self.threadPool,
            parentWindow = self,
        )

    def downloadUpdate(self, downloadURL):
        Function_SetMethodExecutor(
            executeMethod = updateDownloader,
            executeParams = (
                downloadURL,
                downloadDir,
                "EVT Update",
                extractDir
            ),
            progressBar = self.progressBar,
            threadPool = self.threadPool,
            parentWindow = self,
        )

    def main(self):
        functionSignals.updateMessage.connect(
            lambda message: QFunc.setText(
                self.label,
                EasyUtils.setRichText(message, 'center', 9, 420, 0.3, 12)
            )
        )
        functionSignals.readyToUpdate.connect(
            lambda downloadURL, versionInfo: (
                MessageBoxBase.pop(None,
                    QMessageBox.Question, "Ask",
                    text = "检测到可用的新版本，是否更新？\nNew version available, wanna update?",
                    detailedText = versionInfo,
                    buttons = QMessageBox.Yes|QMessageBox.No,
                    buttonEvents = {
                        QMessageBox.Yes: lambda: self.downloadUpdate(downloadURL),
                        QMessageBox.No: lambda: functionSignals.isUpdateSucceeded.emit(False, "已取消下载更新！\nDownload canceled!")
                    }
                )
            )
        )
        functionSignals.isUpdateSucceeded.connect(
            lambda succeeded, info: (
                MessageBoxBase.pop(None,
                    QMessageBox.Warning, "Warning",
                    text = info,
                ) if not succeeded and len(info) > 0 else None,
                subprocess.Popen(f'{"python" if isFileCompiled == False else ""} "{programPath}" {f"--deprecatedVersion {currentVersion}" if succeeded else ""}', shell = True),
                QApplication.instance().exit(),
                sys.exit(0) # In case the main event loop is not entered
            )
        )

        self.skipButton.setText("Skip")
        self.skipButton.clicked.connect(
            lambda: functionSignals.isUpdateSucceeded.emit(False, "")
        )

        self.checkUpdate() if downloadURL is None else self.downloadUpdate(downloadURL)

        self.show()

##############################################################################################################################

if __name__ == "__main__":
    sys.exit(0) if programPath is None else None

    App = QApplication(sys.argv)

    MW = MainWindow()
    MW.main()

    sys.exit(App.exec())

##############################################################################################################################