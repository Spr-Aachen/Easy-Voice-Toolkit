from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import *

from components import LabelBase, HollowButton, MediaPlayerBase


class Ui_ChildWindow_TTS(object):
    def setupUi(self, ChildWindow_TTS):
        if not ChildWindow_TTS.objectName():
            ChildWindow_TTS.setObjectName(u"ChildWindow_TTS")
        ChildWindow_TTS.resize(611, 300)
        ChildWindow_TTS.setMinimumSize(QSize(450, 300))
        self.verticalLayout = QVBoxLayout(ChildWindow_TTS)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = QWidget(ChildWindow_TTS)
        self.TitleBar.setObjectName(u"TitleBar")
        self.TitleBar.setMinimumSize(QSize(0, 30))
        self.TitleBar.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.TitleBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(792, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.Button_Maximize = QPushButton(self.TitleBar)
        self.Button_Maximize.setObjectName(u"Button_Maximize")
        self.Button_Maximize.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/images/icons/FullScreen.png);\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_2.addWidget(self.Button_Maximize)

        self.Button_Close = QPushButton(self.TitleBar)
        self.Button_Close.setObjectName(u"Button_Close")
        self.Button_Close.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/images/icons/X.png);\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(210, 123, 123, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_2.addWidget(self.Button_Close)


        self.verticalLayout.addWidget(self.TitleBar)

        self.CentralWidget = QWidget(ChildWindow_TTS)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.gridLayout = QGridLayout(self.CentralWidget)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(21, 12, 21, 12)
        self.Label_Title = LabelBase(self.CentralWidget)
        self.Label_Title.setObjectName(u"Label_Title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_Title.sizePolicy().hasHeightForWidth())
        self.Label_Title.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Label_Title, 0, 0, 1, 2)

        self.Label_Text = LabelBase(self.CentralWidget)
        self.Label_Text.setObjectName(u"Label_Text")
        sizePolicy.setHeightForWidth(self.Label_Text.sizePolicy().hasHeightForWidth())
        self.Label_Text.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Label_Text, 1, 0, 1, 2)

        self.widget = MediaPlayerBase(self.CentralWidget)
        self.widget.setObjectName(u"widget")

        self.gridLayout.addWidget(self.widget, 2, 0, 1, 2)


        self.verticalLayout.addWidget(self.CentralWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(21, 12, 21, 12)
        self.Button_Cancel = HollowButton(ChildWindow_TTS)
        self.Button_Cancel.setObjectName(u"Button_Cancel")

        self.horizontalLayout.addWidget(self.Button_Cancel)

        self.Button_Confirm = HollowButton(ChildWindow_TTS)
        self.Button_Confirm.setObjectName(u"Button_Confirm")

        self.horizontalLayout.addWidget(self.Button_Confirm)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ChildWindow_TTS)

        QMetaObject.connectSlotsByName(ChildWindow_TTS)
    # setupUi

    def retranslateUi(self, ChildWindow_TTS):
        ChildWindow_TTS.setWindowTitle(QCoreApplication.translate("ChildWindow_TTS", u"Form", None))
        self.Label_Title.setText(QCoreApplication.translate("ChildWindow_TTS", u"Title", None))
        self.Label_Text.setText(QCoreApplication.translate("ChildWindow_TTS", u"Text", None))
        self.Button_Cancel.setText(QCoreApplication.translate("ChildWindow_TTS", u"PushButton", None))
        self.Button_Confirm.setText(QCoreApplication.translate("ChildWindow_TTS", u"PushButton", None))
    # retranslateUi