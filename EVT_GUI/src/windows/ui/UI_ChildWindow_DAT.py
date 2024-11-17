from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import *

from components.components import LabelBase, HollowButton, Table_DATResult, TabWidgetBase
from assets import sources


class Ui_ChildWindow_DAT(object):
    def setupUi(self, ChildWindow_DAT):
        if not ChildWindow_DAT.objectName():
            ChildWindow_DAT.setObjectName(u"ChildWindow_DAT")
        ChildWindow_DAT.resize(630, 420)
        ChildWindow_DAT.setMinimumSize(QSize(630, 420))
        self.verticalLayout = QVBoxLayout(ChildWindow_DAT)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = QWidget(ChildWindow_DAT)
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

        self.CentralWidget = QWidget(ChildWindow_DAT)
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

        self.gridLayout.addWidget(self.Label_Title, 0, 0, 1, 1)

        self.Label_Text = LabelBase(self.CentralWidget)
        self.Label_Text.setObjectName(u"Label_Text")
        sizePolicy.setHeightForWidth(self.Label_Text.sizePolicy().hasHeightForWidth())
        self.Label_Text.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Label_Text, 1, 0, 1, 1)

        self.TabWidget = TabWidgetBase(self.CentralWidget)
        self.TabWidget.setObjectName(u"TabWidget")
        self.Tab_Train = QWidget()
        self.Tab_Train.setObjectName(u"Tab_Train")
        self.verticalLayout_72 = QVBoxLayout(self.Tab_Train)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.Table_Train = Table_DATResult(self.Tab_Train)
        self.Table_Train.setObjectName(u"Table_Train")

        self.verticalLayout_72.addWidget(self.Table_Train)

        self.TabWidget.addTab(self.Tab_Train, "")
        self.Tab_Val = QWidget()
        self.Tab_Val.setObjectName(u"Tab_Val")
        self.verticalLayout_38 = QVBoxLayout(self.Tab_Val)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.Table_Val = Table_DATResult(self.Tab_Val)
        self.Table_Val.setObjectName(u"Table_Val")

        self.verticalLayout_38.addWidget(self.Table_Val)

        self.TabWidget.addTab(self.Tab_Val, "")

        self.gridLayout.addWidget(self.TabWidget, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.CentralWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(21, 12, 21, 12)
        self.Button_Cancel = HollowButton(ChildWindow_DAT)
        self.Button_Cancel.setObjectName(u"Button_Cancel")

        self.horizontalLayout.addWidget(self.Button_Cancel)

        self.Button_Confirm = HollowButton(ChildWindow_DAT)
        self.Button_Confirm.setObjectName(u"Button_Confirm")

        self.horizontalLayout.addWidget(self.Button_Confirm)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ChildWindow_DAT)

        QMetaObject.connectSlotsByName(ChildWindow_DAT)
    # setupUi

    def retranslateUi(self, ChildWindow_DAT):
        ChildWindow_DAT.setWindowTitle(QCoreApplication.translate("ChildWindow_DAT", u"Form", None))
        self.Label_Title.setText(QCoreApplication.translate("ChildWindow_DAT", u"Title", None))
        self.Label_Text.setText(QCoreApplication.translate("ChildWindow_DAT", u"Text", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.Tab_Train), QCoreApplication.translate("ChildWindow_DAT", u"\u9875", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.Tab_Val), QCoreApplication.translate("ChildWindow_DAT", u"Tab 1", None))
        self.Button_Cancel.setText(QCoreApplication.translate("ChildWindow_DAT", u"PushButton", None))
        self.Button_Confirm.setText(QCoreApplication.translate("ChildWindow_DAT", u"PushButton", None))
    # retranslateUi