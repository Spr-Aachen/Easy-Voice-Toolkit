import PyEasyUtils as EasyUtils
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets.Windows import MessageBoxBase
from QEasyWidgets.Components import *
from QEasyWidgets import IconBase

##############################################################################################################################

class MessageBox_Stacked(MessageBoxBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent, min_width = 810, min_height = 480)

        self.layout().setContentsMargins(6, 12, 6, 12)
        self.layout().setSpacing(6)

        self.StackedWidget = QStackedWidget()

        self.ButtonP = ButtonBase()
        self.ButtonP.clicked.connect(lambda: self.StackedWidget.setCurrentIndex(self.StackedWidget.currentIndex() - 1))
        self.ButtonP.setFixedSize(33, 66)
        QFunc.setRetainSizeWhenHidden(self.ButtonP)
        self.ButtonP.setIcon(IconBase.CompactChevron_Left)
        self.ButtonP.setToolTip("Prev Page")

        self.ButtonN = ButtonBase()
        self.ButtonN.clicked.connect(lambda: self.StackedWidget.setCurrentIndex(self.StackedWidget.currentIndex() + 1))
        self.ButtonN.setFixedSize(33, 66)
        QFunc.setRetainSizeWhenHidden(self.ButtonN)
        self.ButtonN.setIcon(IconBase.CompactChevron_Right)
        self.ButtonN.setToolTip("Next Page")

        Layout = QHBoxLayout()
        Layout.setAlignment(Qt.AlignCenter)
        Layout.setContentsMargins(0, 0, 0, 0)
        Layout.setSpacing(self.layout().spacing())
        Layout.addWidget(self.ButtonP)
        Layout.addWidget(self.StackedWidget)
        Layout.addWidget(self.ButtonN)
        self.layout().insertLayout(0, Layout)

    def setContent(self, Images: list, Texts: list):
        QFunc.setNoContents(self.StackedWidget)

        for Index, Image in enumerate(EasyUtils.toIterable(Images)):
            Label = LabelBase()
            QFunc.setText(Label, EasyUtils.setRichText(EasyUtils.toIterable(Texts)[Index], 'left', 9.9, 420))

            TextBrowser = QTextBrowser()
            TextBrowser.setStyleSheet(
                "QTextBrowser {"
                f"    background-image: url({EasyUtils.normPath(Image, 'Posix')});"
                "    background-repeat: no-repeat;"
                "    background-position: center 0px;"
                "    padding: 0px;"
                "    border: none;"
                "    border-radius: 6px;"
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

        self.Button1 = HollowButton()
        #self.Button1.setFixedHeight(33)

        self.Button2 = HollowButton()
        #self.Button2.setFixedHeight(33)

        Layout = QGridLayout()
        Layout.setAlignment(Qt.AlignCenter)
        Layout.setContentsMargins(21, 12, 21, 12)
        Layout.setSpacing(21)
        Layout.addWidget(self.Button1, 1, 0, 1, 2)
        Layout.addWidget(self.Button2, 2, 0, 1, 2)
        self.layout().insertLayout(2, Layout)

##############################################################################################################################