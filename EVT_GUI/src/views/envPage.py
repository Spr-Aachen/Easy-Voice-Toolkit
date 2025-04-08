from typing import Type, Optional
from PyEasyUtils import setRichText
from PySide6.QtCore import Qt, QRect, QSize, SignalInstance
from PySide6.QtCore import QCoreApplication as QCA
from PySide6.QtWidgets import *
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets.Common import FileDialogMode
from QEasyWidgets.Components import *

from .common import SubPage, Page
#from assets import *
from functions import *

##############################################################################################################################

class SubEnvPage_Detector(SubPage):
    """
    """
    def __init__(self, parent = None):
        super().__init__(parent)

        layout = self.cleanLayout()
        layout.addWidget(self.contentWidget, 0, 0)

    def _addToChildFrame(self, titleLabel: QLabel, progressBar: QWidget, statusBrowser: QTextBrowser, detectButton: QPushButton):
        childFrame = QFrame()
        childFrame.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border: none;
            }
            QFrame:hover {
                background-color: rgba(36, 36, 36, 12);
            }
        """)
        childFrame_layout = QGridLayout(childFrame)
        childFrame_layout.setSpacing(12)
        childFrame_layout.setContentsMargins(21, 12, 21, 12)
        childFrame_layout.addWidget(titleLabel, 0, 0, 1, 2)
        childFrame_layout.addWidget(progressBar, 1, 0, 1, 2)
        childFrame_layout.addWidget(statusBrowser, 2, 0, 1, 2)
        childFrame_layout.addWidget(detectButton, 0, 2, 3, 1)
        return childFrame

    def addDetectorFrame(self,
        rootItemText: Optional[str] = None, toolBoxText: Optional[str] = None, text: str = ..., toolTip: str = ...,
        detectMethod: object = ..., params = [], terminateMethod: object = ..., threadPool = ..., 
        signal_detect: SignalInstance = ..., signal_detected: SignalInstance = ..., signal_undetected: SignalInstance = ..., statusSignal: SignalInstance = ...,
    ):
        titleLabel = LabelBase(self)
        titleLabel.setStyleSheet(u"QLabel {\n"
        "	font-size: 15px;\n"
        "	/*text-align: center;*/\n"
        "	background-color: transparent;\n"
        "	padding: 0px;\n"
        "	border-width: 0px;\n"
        "	border-radius: 0px;\n"
        "	border-style: solid;\n"
        "}")
        titleLabel.setText(text)
        progressBar = ProgressBarBase(self)
        progressBar.setMaximumHeight(3)
        statusBrowser = TextBrowserBase(self)
        statusBrowser.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred))
        statusBrowser.setStyleSheet(u"QTextBrowser {\n"
        "	font-size: 9.9px;\n"
        "	/*text-align: center;*/\n"
        "	background-color: transparent;\n"
        "	padding: 0px;\n"
        "	border-width: 0px;\n"
        "	border-radius: 0px;\n"
        "	border-style: solid;\n"
        "}")
        statusBrowser.setText("--")
        detectButton = QPushButton(self)
        detectButton.setFixedSize(QSize(33, 33))
        detectButton.setObjectName(text.splitlines()[0])
        detectButton.setStyleSheet(u"QPushButton {\n"
        "	text-align: center;\n"
        "	font-size: 15px;\n"
        "	image: url(:/Button_Icon/images/icons/Refresh.png);\n"
        "	background-color: transparent;\n"
        "	padding: 4.5px;\n"
        "	border-width: 1.2px;\n"
        "	border-radius: 6px;\n"
        "	border-style: solid;\n"
        "	border-color: rgba(123, 123, 123, 123);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	border-color: rgba(123, 123, 123, 210);\n"
        "}")
        detectButton.setToolTip(toolTip)
        self._addToContainer(rootItemText, toolBoxText, text, titleLabel, progressBar, statusBrowser, detectButton)
        Function_SetMethodExecutor(
            executeButton = detectButton,
            progressBar = progressBar,
            executeMethod = detectMethod,
            executeParams = params,
            terminateMethod = terminateMethod,
            threadPool = threadPool,
            parentWindow = self,
        )
        signal_detect.connect(
            detectButton.click
        )
        signal_detected.connect(
            lambda: progressBar.setValue(100)
        )
        signal_undetected.connect(
            lambda: MessageBoxBase.pop(self,
                QMessageBox.Information, "Tip",
                text = "缺失 %s，已开始下载" % text,
            )
        )
        statusSignal.connect(
            lambda Status: statusBrowser.setText(Status)
        )


class SubEnvPage_Manager(SubPage):
    """
    """
    def __init__(self, parent = None):
        super().__init__(parent)

        layout = self.cleanLayout()
        layout.addWidget(self.contentWidget, 0, 0)

    def _addToChildFrame(self, titleLabel: QLabel, comboBox: QComboBox, executeButton: QPushButton):
        titleLabel.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred))
        childFrame = QFrame()
        childFrame.setMinimumSize(QSize(0, 90))
        childFrame.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border: none;
            }
            QFrame:hover {
                background-color: rgba(36, 36, 36, 12);
            }
        """)
        childFrame_layout = QGridLayout(childFrame)
        childFrame_layout.setSpacing(12)
        childFrame_layout.setContentsMargins(21, 12, 21, 12)
        childFrame_layout.addWidget(titleLabel, 0, 0)
        childFrame_layout.addWidget(comboBox, 0, 1, Qt.AlignRight)
        childFrame_layout.addWidget(executeButton, 1, 1, Qt.AlignRight)
        return childFrame

    def addComboBoxFrame(self,
        rootItemText: Optional[str] = None, toolBoxText: Optional[str] = None, text: str = ..., toolTip: Optional[str] = None,
        items: list = ...,
        executorText: str = ..., executeMethod: object = ..., paramTargets: list[QObject] = [], terminateMethod: object = ..., threadPool = ...,
    ):
        titleLabel = LabelBase(self)
        titleLabel.setStyleSheet(u"QLabel {\n"
        "	font-size: 15px;\n"
        "	/*text-align: center;*/\n"
        "	background-color: transparent;\n"
        "	padding: 0px;\n"
        "	border-width: 0px;\n"
        "	border-radius: 0px;\n"
        "	border-style: solid;\n"
        "}")
        titleLabel.setText(text)
        comboBox = ComboBoxBase(self)
        comboBox.setMinimumSize(QSize(123, 30))
        comboBox.setToolTip(toolTip) if toolTip is not None else None
        comboBox.addItems(items)
        executeButton = HollowButton(self)
        executeButton.setFixedSize(QSize(123, 30))
        executeButton.setObjectName(text.splitlines()[0])
        executeButton.setText(executorText)
        self._addToContainer(rootItemText, toolBoxText, text, titleLabel, comboBox, executeButton)
        Function_SetMethodExecutor(
            executeButton = executeButton,
            executeMethod = executeMethod,
            executeParams = [paramTarget() if hasattr(paramTarget, '__call__') else paramTarget for paramTarget in paramTargets],
            terminateMethod = terminateMethod,
            threadPool = threadPool,
            parentWindow = self,
        )


class EnvPage(Page):
    """
    """
    def __init__(self, parent = None):
        super().__init__(parent)

        self.consoleButton = QPushButton()
        self.consoleButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.consoleButton.setStyleSheet("""
            QPushButton {
                image-position: center;
                image: url(:/Button_Icon/images/icons/Console.png);
                padding: 18px;
                background-color: transparent;
                border-width: 0px;
                border-style: solid;
            }
            QPushButton:hover {
                background-color: rgba(201, 210, 222, 33);
            }
        """)
        self.consoleButton.clicked.connect(
            lambda: EasyUtils.subprocessManager().create("cmd.exe /c start cmd.exe")
        )
        self.navigationAreaLayout.addWidget(self.consoleButton)

##############################################################################################################################