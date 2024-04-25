from typing import Optional
from PySide6.QtCore import Qt, QObject

from QEasyWidgets.WindowCustomizer import *
from QEasyWidgets.ComponentsCustomizer import *
from .UI_MainWindow import Ui_MainWindow
from .UI_ChildWindow_ASR import Ui_ChildWindow_ASR
from .UI_ChildWindow_STT import Ui_ChildWindow_STT
from .UI_ChildWindow_DAT_GPPTSoVITS import Ui_ChildWindow_DAT_GPTSoVITS
from .UI_ChildWindow_DAT_VITS import Ui_ChildWindow_DAT_VITS
from .UI_ChildWindow_TTS import Ui_ChildWindow_TTS

##############################################################################################################################

class Window_MainWindow(MainWindowBase):
    ui = Ui_MainWindow()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 1280, min_height = 720)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)

        self.setCentralWidget(self.ui.CentralWidget)

##############################################################################################################################

class Window_ChildWindow_ASR(ChildWindowBase):
    ui = Ui_ChildWindow_ASR()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 960, min_height = 540)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)


class Window_ChildWindow_STT(ChildWindowBase):
    ui = Ui_ChildWindow_STT()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 960, min_height = 540)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)


class Window_ChildWindow_DAT_GPTSoVITS(ChildWindowBase):
    ui = Ui_ChildWindow_DAT_GPTSoVITS()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 960, min_height = 540)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)


class Window_ChildWindow_DAT_VITS(ChildWindowBase):
    ui = Ui_ChildWindow_DAT_VITS()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 960, min_height = 540)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)


class Window_ChildWindow_TTS(ChildWindowBase):
    ui = Ui_ChildWindow_TTS()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 450, min_height = 300)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)

##############################################################################################################################

class MessageBox_Stacked(MessageBoxBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent, min_width = 810, min_height = 480)

        self.layout().setContentsMargins(6, 12, 6, 12)
        self.layout().setSpacing(6)

        self.StackedWidget = QStackedWidget()

        self.ButtonP = QPushButton()
        self.ButtonP.clicked.connect(lambda: self.StackedWidget.setCurrentIndex(self.StackedWidget.currentIndex() - 1))
        self.ButtonP.setFixedWidth(33)
        self.ButtonP.setFixedHeight(66)
        Function_SetRetainSizeWhenHidden(self.ButtonP)
        self.ButtonP.setStyleSheet(
            "QPushButton {"
            "   background-color: transparent;"
            "   padding: 12px;"
            "   border-image: url(:/Button_Icon/Sources/LeftArrow.png);"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(210, 222, 234, 12);"
            "}"
        )
        self.ButtonP.setToolTip("Prev Page")

        self.ButtonN = QPushButton()
        self.ButtonN.clicked.connect(lambda: self.StackedWidget.setCurrentIndex(self.StackedWidget.currentIndex() + 1))
        self.ButtonN.setFixedWidth(33)
        self.ButtonN.setFixedHeight(66)
        Function_SetRetainSizeWhenHidden(self.ButtonN)
        self.ButtonN.setStyleSheet(
            "QPushButton {"
            "   background-color: transparent;"
            "   padding: 12px;"
            "   border-image: url(:/Button_Icon/Sources/RightArrow.png);"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(210, 222, 234, 12);"
            "}"
        )
        self.ButtonN.setToolTip("Next Page")

        Layout = QHBoxLayout()
        Layout.setAlignment(Qt.AlignCenter)
        Layout.setContentsMargins(0, 0, 0, 0)
        Layout.setSpacing(self.layout().spacing())
        Layout.addWidget(self.ButtonP)
        Layout.addWidget(self.StackedWidget)
        Layout.addWidget(self.ButtonN)
        self.Layout.insertLayout(0, Layout)

    def SetContent(self, Images: list, Texts: list):
        Function_SetNoContents(self.StackedWidget)

        for Index, Image in enumerate(ToIterable(Images)):
            Label = QLabel()
            Function_SetText(Label, SetRichText(ToIterable(Texts)[Index], 'left', 9.9, 420))

            TextBrowser = QTextBrowser()
            TextBrowser.setStyleSheet(
                "QTextBrowser {"
                f"    background-image: url({NormPath(Image, 'Posix')});"
                "    background-repeat: no-repeat;"
                "    background-position: center 0px;"
                "    padding: 0px;"
                "    border-width: 0px;"
                "    border-radius: 6px;"
                "    border-style: solid;"
                "}"
            ) if Image is not None else None

            SubLayout = QVBoxLayout()
            SubLayout.setAlignment(Qt.AlignCenter)
            SubLayout.setContentsMargins(0, 0, 0, 0)
            SubLayout.setSpacing(self.layout().spacing())
            SubLayout.addWidget(Label)
            SubLayout.addWidget(TextBrowser)

            Widget = QWidget()
            Widget.setLayout(SubLayout)
            self.StackedWidget.addWidget(Widget)
    
        self.StackedWidget.currentChanged.connect(lambda: self.ButtonP.setVisible(False) if self.StackedWidget.currentIndex() == 0 else self.ButtonP.setVisible(True))
        self.ButtonP.setVisible(False)
        self.StackedWidget.currentChanged.connect(lambda: self.ButtonN.setVisible(False) if self.StackedWidget.currentIndex() == self.StackedWidget.count() - 1 else self.ButtonN.setVisible(True))
        self.ButtonN.setVisible(True)

        self.StackedWidget.currentChanged.connect(lambda: self.setText(f'{self.StackedWidget.currentIndex() + 1} / {self.StackedWidget.count()}'))
        self.setText(f'1 / {self.StackedWidget.count()}')


class MessageBox_Buttons(MessageBoxBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent, min_width = 240, min_height = 120)

        self.layout().setContentsMargins(6, 12, 6, 12)
        self.layout().setSpacing(6)

        ButtonStyle = '''
        QPushButton {
            background-color: transparent;
            padding: 6px;
            border-width: 1px;
            border-style: solid;
            border-color: rgb(90, 90, 90);
        }
        QPushButton:hover {
            border-color: rgb(120, 120, 120);
        }
        '''

        self.Button1 = QPushButton()
        #self.Button1.setFixedHeight(33)
        self.Button1.setStyleSheet(ButtonStyle)

        self.Button2 = QPushButton()
        #self.Button2.setFixedHeight(33)
        self.Button2.setStyleSheet(ButtonStyle)

        Layout = QGridLayout()
        Layout.setAlignment(Qt.AlignCenter)
        Layout.setContentsMargins(21, 12, 21, 12)
        Layout.setSpacing(21)
        Layout.addWidget(self.Button1, 1, 0, 1, 2)
        Layout.addWidget(self.Button2, 2, 0, 1, 2)
        self.Layout.insertLayout(2, Layout)


class MessageBox_LineEdit(MessageBoxBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent, min_width = 450, min_height = 300)

        self.layout().setContentsMargins(6, 12, 6, 12)
        self.layout().setSpacing(6)

        self.TitleBar.CloseButton.hide()

        ButtonStyle = '''
        QPushButton {
            background-color: transparent;
            padding: 6px;
            border-width: 1px;
            border-style: solid;
            border-color: rgb(90, 90, 90);
        }
        QPushButton:hover {
            border-color: rgb(120, 120, 120);
        }
        '''

        self.TextLabel = QLabel()

        self.LineEdit = LineEditBase()
        self.LineEdit.setFixedHeight(27)
        self.LineEdit.ClearDefaultStyleSheet()
        self.LineEdit.setStyleSheet(self.LineEdit.styleSheet() + 'LineEditBase {border-width: 0px 0px 1px 0px; border-radius: 0px;}')

        self.Button_Confirm = QPushButton()
        #self.Button_Confirm.setFixedHeight(33)
        self.Button_Confirm.setStyleSheet(ButtonStyle)

        self.Button_Cancel = QPushButton()
        #self.Button_Cancel.setFixedHeight(33)
        self.Button_Cancel.setStyleSheet(ButtonStyle)

        Layout = QGridLayout()
        Layout.setAlignment(Qt.AlignCenter)
        Layout.setContentsMargins(21, 12, 21, 12)
        Layout.setSpacing(21)
        Layout.addWidget(self.TextLabel, 0, 0, 2, 2)
        Layout.addWidget(self.LineEdit, 2, 0, 1, 2)
        Layout.addWidget(self.Button_Cancel, 3, 0, 1, 1)
        Layout.addWidget(self.Button_Confirm, 3, 1, 1, 1)
        self.Layout.insertLayout(2, Layout)

    def SetContent(self, Title: str, Body:str):
        self.setText(Title)
        Function_SetText(self.TextLabel, SetRichText(Body = Body, BodySize = 9.6))

##############################################################################################################################