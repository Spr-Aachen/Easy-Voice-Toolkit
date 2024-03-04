from typing import Optional
from PySide6.QtCore import Qt, QObject

from .QSimpleWidgets.WindowCustomizer import *
from .QSimpleWidgets.ComponentsCustomizer import *
from .UI_MainWindow import Ui_MainWindow
from .UI_ChildWindow_ASR import Ui_ChildWindow_ASR
from .UI_ChildWindow_STT import Ui_ChildWindow_STT
from .UI_ChildWindow_TTS import Ui_ChildWindow_TTS

##############################################################################################################################

class Window_MainWindow(MainWindowBase):
    ui = Ui_MainWindow()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 1280, min_height = 720)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)

        self.setCentralWidget(self.ui.CentralWidget)
        ComponentsSignals.Signal_SetTheme.connect(self.InitDefaultStyleSheet)
        self.InitDefaultStyleSheet('Auto')

    def InitDefaultStyleSheet(self, Theme: str) -> None:
        super().setStyleSheet(Function_GetStyleSheet('Window', Theme).replace('#CentralWidget', f'#{self.CentralWidget.objectName()}'))

##############################################################################################################################

class Window_ChildWindow_ASR(ChildWindowBase):
    ui = Ui_ChildWindow_ASR()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 960, min_height = 540)

        self.setWindowModality(Qt.ApplicationModal)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)

        ComponentsSignals.Signal_SetTheme.connect(self.InitDefaultStyleSheet)
        self.InitDefaultStyleSheet('Auto')

    def InitDefaultStyleSheet(self, Theme: str) -> None:
        super().setStyleSheet(Function_GetStyleSheet('Window', Theme).replace('#CentralWidget', f'#{self.objectName()}'))


class Window_ChildWindow_STT(ChildWindowBase):
    ui = Ui_ChildWindow_STT()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 960, min_height = 540)

        self.setWindowModality(Qt.ApplicationModal)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)

        ComponentsSignals.Signal_SetTheme.connect(self.InitDefaultStyleSheet)
        self.InitDefaultStyleSheet('Auto')

    def InitDefaultStyleSheet(self, Theme: str) -> None:
        super().setStyleSheet(Function_GetStyleSheet('Window', Theme).replace('#CentralWidget', f'#{self.objectName()}'))


class Window_ChildWindow_TTS(ChildWindowBase):
    ui = Ui_ChildWindow_TTS()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 450, min_height = 300)

        self.setWindowModality(Qt.ApplicationModal)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)

        ComponentsSignals.Signal_SetTheme.connect(self.InitDefaultStyleSheet)
        self.InitDefaultStyleSheet('Auto')

    def InitDefaultStyleSheet(self, Theme: str) -> None:
        super().setStyleSheet(Function_GetStyleSheet('Window', Theme).replace('#CentralWidget', f'#{self.objectName()}'))

##############################################################################################################################

class MessageBoxBase(DialogBase):
    '''
    '''
    ButtonDict = {
        QMessageBox.NoButton:        QDialogButtonBox.NoButton,
        QMessageBox.Ok:              QDialogButtonBox.Ok,
        QMessageBox.Cancel:          QDialogButtonBox.Cancel,
        QMessageBox.Yes:             QDialogButtonBox.Yes,
        QMessageBox.No:              QDialogButtonBox.No,
        QMessageBox.Retry:           QDialogButtonBox.Retry,
        QMessageBox.Ignore:          QDialogButtonBox.Ignore,
        QMessageBox.Open:            QDialogButtonBox.Open,
        QMessageBox.Close:           QDialogButtonBox.Close,
        QMessageBox.Save:            QDialogButtonBox.Save,
        QMessageBox.Discard:         QDialogButtonBox.Discard,
        QMessageBox.Apply:           QDialogButtonBox.Apply,
        QMessageBox.RestoreDefaults: QDialogButtonBox.RestoreDefaults,
        QMessageBox.Ok | QMessageBox.Cancel:             QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
        QMessageBox.Yes | QMessageBox.No:                QDialogButtonBox.Yes | QDialogButtonBox.No,
        QMessageBox.Retry | QMessageBox.Ignore:          QDialogButtonBox.Retry | QDialogButtonBox.Ignore,
        QMessageBox.Open | QMessageBox.Close:            QDialogButtonBox.Open | QDialogButtonBox.Close,
        QMessageBox.Save | QMessageBox.Discard:          QDialogButtonBox.Save | QDialogButtonBox.Discard,
        QMessageBox.Apply | QMessageBox.RestoreDefaults: QDialogButtonBox.Apply | QDialogButtonBox.RestoreDefaults
    }

    def __init__(self,
        parent: Optional[QWidget] = None,
        min_width = 630,
        min_height = 420
    ):  
        super().__init__(parent, Qt.Dialog, min_width, min_height)

        self.setWindowModality(Qt.ApplicationModal)
        self.setModal(True)

        self.Label = QLabel(str(), parent = self)

        self.ButtonBox = QDialogButtonBox(parent = self)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)
        self.ButtonBox.setOrientation(Qt.Horizontal)

        self.Layout = QVBoxLayout()
        self.Layout.setAlignment(Qt.AlignCenter)
        self.Layout.setContentsMargins(21, 12, 21, 12)
        self.Layout.setSpacing(21)
        self.Layout.addWidget(self.Label)
        self.Layout.addWidget(self.ButtonBox)
        self.setLayout(self.Layout)

        self.setIcon(QMessageBox.Information)
        self.setText('Text')
        self.setStandardButtons(QMessageBox.NoButton)

    def setIcon(self, arg__1):
        if arg__1 == QMessageBox.Question:
            self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxQuestion))
        if arg__1 == QMessageBox.Information:
            self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxInformation))
        if arg__1 == QMessageBox.Warning:
            self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxWarning))
        if arg__1 == QMessageBox.Critical:
            self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxCritical))

    def setText(self, text: str):
        Function_SetText(
            Widget = self.Label,
            Text = SetRichText(
                Title = text,
                TitleAlign = 'center'
            )
        )

    def setStandardButtons(self, buttons: QMessageBox.StandardButton):
        self.ButtonBox.setStandardButtons(self.ButtonDict.get(buttons))
        '''
        for PushButton in self.ButtonBox.buttons():
            StandardButton = FindKey(self.ButtonDict, self.ButtonBox.standardButton(PushButton))
            PushButton.clicked.connect(lambda: ComponentsSignals.Signal_ClickedButton.emit(StandardButton)) if PushButton is not None else None
        '''

    def exec(self) -> int:
        Result = super().exec()
        StandardButton = FindKey(self.ButtonDict, Result)
        return StandardButton if StandardButton is not None else Result

    def InsertItem(self, Item: QObject, Position: str = 'Center'):
        if isinstance(Item, QWidget):
            if Position is 'Top':
                self.Layout.insertWidget(0, Item)
            if Position is 'Center':
                self.Layout.insertWidget(1, Item)
            if Position is 'Bottom':
                self.Layout.insertWidget(2, Item)
        if isinstance(Item, QLayout):
            if Position is 'Top':
                self.Layout.insertLayout(0, Item)
            if Position is 'Center':
                self.Layout.insertLayout(1, Item)
            if Position is 'Bottom':
                self.Layout.insertLayout(2, Item)


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
        self.InsertItem(Layout, Position = 'Top')

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
        self.InsertItem(Layout, Position = 'Bottom')


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
        self.InsertItem(Layout, Position = 'Bottom')

    def SetContent(self, Title: str, Body:str):
        self.setText(Title)
        Function_SetText(self.TextLabel, SetRichText(Body = Body, BodySize = 9.6))

##############################################################################################################################