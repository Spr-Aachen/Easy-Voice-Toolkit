from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import *

from components import LabelBase, Table_VPRResult, LineEditBase, HollowButton


class Ui_ChildWindow_VPR(object):
    def setupUi(self, ChildWindow_VPR):
        if not ChildWindow_VPR.objectName():
            ChildWindow_VPR.setObjectName(u"ChildWindow_VPR")
        ChildWindow_VPR.resize(630, 420)
        ChildWindow_VPR.setMinimumSize(QSize(630, 420))
        self.verticalLayout = QVBoxLayout(ChildWindow_VPR)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = QWidget(ChildWindow_VPR)
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

        self.CentralWidget = QWidget(ChildWindow_VPR)
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

        self.gridLayout.addWidget(self.Label_Title, 0, 0, 1, 4)

        self.Label_Text = LabelBase(self.CentralWidget)
        self.Label_Text.setObjectName(u"Label_Text")
        sizePolicy.setHeightForWidth(self.Label_Text.sizePolicy().hasHeightForWidth())
        self.Label_Text.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Label_Text, 1, 0, 1, 4)

        self.CheckBox = QCheckBox(self.CentralWidget)
        self.CheckBox.setObjectName(u"CheckBox")
        sizePolicy.setHeightForWidth(self.CheckBox.sizePolicy().hasHeightForWidth())
        self.CheckBox.setSizePolicy(sizePolicy)
        self.CheckBox.setStyleSheet(u"QCheckBox::indicator {\n"
"	background-color: transparent;\n"
"	border-image: url(:/CheckBox_Icon/images/icons/Square.png);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/images/icons/CheckedSquare.png);\n"
"}")

        self.gridLayout.addWidget(self.CheckBox, 3, 0, 1, 1)

        self.Table = Table_VPRResult(self.CentralWidget)
        self.Table.setObjectName(u"Table")

        self.gridLayout.addWidget(self.Table, 2, 0, 1, 4)

        self.LineEdit = LineEditBase(self.CentralWidget)
        self.LineEdit.setObjectName(u"LineEdit")
        sizePolicy.setHeightForWidth(self.LineEdit.sizePolicy().hasHeightForWidth())
        self.LineEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.LineEdit, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.CentralWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(21, 12, 21, 12)
        self.Button_Cancel = HollowButton(ChildWindow_VPR)
        self.Button_Cancel.setObjectName(u"Button_Cancel")

        self.horizontalLayout.addWidget(self.Button_Cancel)

        self.Button_Save = HollowButton(ChildWindow_VPR)
        self.Button_Save.setObjectName(u"Button_Save")

        self.horizontalLayout.addWidget(self.Button_Save)

        self.Button_Confirm = HollowButton(ChildWindow_VPR)
        self.Button_Confirm.setObjectName(u"Button_Confirm")

        self.horizontalLayout.addWidget(self.Button_Confirm)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ChildWindow_VPR)

        QMetaObject.connectSlotsByName(ChildWindow_VPR)
    # setupUi

    def retranslateUi(self, ChildWindow_VPR):
        ChildWindow_VPR.setWindowTitle(QCoreApplication.translate("ChildWindow_VPR", u"Form", None))
        self.Label_Title.setText(QCoreApplication.translate("ChildWindow_VPR", u"Title", None))
        self.Label_Text.setText(QCoreApplication.translate("ChildWindow_VPR", u"Text", None))
        self.CheckBox.setText(QCoreApplication.translate("ChildWindow_VPR", u"CheckBox", None))
        self.Button_Cancel.setText(QCoreApplication.translate("ChildWindow_VPR", u"PushButton", None))
        self.Button_Save.setText(QCoreApplication.translate("ChildWindow_VPR", u"PushButton", None))
        self.Button_Confirm.setText(QCoreApplication.translate("ChildWindow_VPR", u"PushButton", None))
    # retranslateUi