from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtWidgets import *

from .Components import LineEditBase, Table_ViewModels, Table_EditAudioSpeaker
from .QSimpleWidgets import Sources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"color: rgb(210, 222, 234);\n"
"background-color: rgba(24, 24, 24, 240);")
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.verticalLayout = QVBoxLayout(self.CentralWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = QFrame(self.CentralWidget)
        self.TitleBar.setObjectName(u"TitleBar")
        self.TitleBar.setMinimumSize(QSize(0, 30))
        self.TitleBar.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_30 = QHBoxLayout(self.TitleBar)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.Frame_Top_Toggle_Menu = QFrame(self.TitleBar)
        self.Frame_Top_Toggle_Menu.setObjectName(u"Frame_Top_Toggle_Menu")
        self.Frame_Top_Toggle_Menu.setMinimumSize(QSize(48, 0))
        self.Frame_Top_Toggle_Menu.setMaximumSize(QSize(48, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.Frame_Top_Toggle_Menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Button_Toggle_Menu = QPushButton(self.Frame_Top_Toggle_Menu)
        self.Button_Toggle_Menu.setObjectName(u"Button_Toggle_Menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Toggle_Menu.sizePolicy().hasHeightForWidth())
        self.Button_Toggle_Menu.setSizePolicy(sizePolicy)
        self.Button_Toggle_Menu.setStyleSheet(u"QPushButton {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	image: url(:/Button_Icon/Sources/Menu.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	border-width: 1.5px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"QPushButton:checked {\n"
"	/*background-color: rgb(45, 45, 45);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_2.addWidget(self.Button_Toggle_Menu)


        self.horizontalLayout_30.addWidget(self.Frame_Top_Toggle_Menu)

        self.Frame_Top = QFrame(self.TitleBar)
        self.Frame_Top.setObjectName(u"Frame_Top")
        self.horizontalLayout_11 = QHBoxLayout(self.Frame_Top)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSpacer_Left_Top = QSpacerItem(588, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.HorizontalSpacer_Left_Top)

        self.Label_Title = QLabel(self.Frame_Top)
        self.Label_Title.setObjectName(u"Label_Title")
        self.Label_Title.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	/*text-align: center;*/\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_55 = QHBoxLayout(self.Label_Title)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(90, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.Label_Title)

        self.HorizontalSpacer_Right_Top = QSpacerItem(587, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.HorizontalSpacer_Right_Top)

        self.Frame_Top_Control_Window = QFrame(self.Frame_Top)
        self.Frame_Top_Control_Window.setObjectName(u"Frame_Top_Control_Window")
        self.Frame_Top_Control_Window.setMinimumSize(QSize(144, 0))
        self.Frame_Top_Control_Window.setMaximumSize(QSize(144, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.Frame_Top_Control_Window)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Button_Minimize_Window = QPushButton(self.Frame_Top_Control_Window)
        self.Button_Minimize_Window.setObjectName(u"Button_Minimize_Window")
        sizePolicy.setHeightForWidth(self.Button_Minimize_Window.sizePolicy().hasHeightForWidth())
        self.Button_Minimize_Window.setSizePolicy(sizePolicy)
        self.Button_Minimize_Window.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Dash.png);\n"
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

        self.horizontalLayout_12.addWidget(self.Button_Minimize_Window)

        self.Button_Maximize_Window = QPushButton(self.Frame_Top_Control_Window)
        self.Button_Maximize_Window.setObjectName(u"Button_Maximize_Window")
        sizePolicy.setHeightForWidth(self.Button_Maximize_Window.sizePolicy().hasHeightForWidth())
        self.Button_Maximize_Window.setSizePolicy(sizePolicy)
        self.Button_Maximize_Window.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/FullScreen.png);\n"
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

        self.horizontalLayout_12.addWidget(self.Button_Maximize_Window)

        self.Button_Close_Window = QPushButton(self.Frame_Top_Control_Window)
        self.Button_Close_Window.setObjectName(u"Button_Close_Window")
        sizePolicy.setHeightForWidth(self.Button_Close_Window.sizePolicy().hasHeightForWidth())
        self.Button_Close_Window.setSizePolicy(sizePolicy)
        self.Button_Close_Window.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/X.png);\n"
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

        self.horizontalLayout_12.addWidget(self.Button_Close_Window)


        self.horizontalLayout_11.addWidget(self.Frame_Top_Control_Window)


        self.horizontalLayout_30.addWidget(self.Frame_Top)


        self.verticalLayout.addWidget(self.TitleBar)

        self.Content = QFrame(self.CentralWidget)
        self.Content.setObjectName(u"Content")
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Frame_Menu = QFrame(self.Content)
        self.Frame_Menu.setObjectName(u"Frame_Menu")
        self.Frame_Menu.setMinimumSize(QSize(210, 0))
        self.Frame_Menu.setMaximumSize(QSize(210, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.Frame_Menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 3, 0, 3)
        self.Button_Menu_Home = QToolButton(self.Frame_Menu)
        self.Button_Menu_Home.setObjectName(u"Button_Menu_Home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Button_Menu_Home.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Home.setSizePolicy(sizePolicy1)
        self.Button_Menu_Home.setMinimumSize(QSize(0, 48))
        self.Button_Menu_Home.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 123), stop:1 transparent);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(120, 180, 240);\n"
"	border-right-color: transparent;\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	/*padding-left: 0.6px;*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.Button_Menu_Home)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Home_Icon = QLabel(self.Button_Menu_Home)
        self.Label_Menu_Home_Icon.setObjectName(u"Label_Menu_Home_Icon")
        self.Label_Menu_Home_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Home_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_Home_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Home.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")
        self.Label_Menu_Home_Icon.setProperty("flat", False)

        self.horizontalLayout_8.addWidget(self.Label_Menu_Home_Icon)

        self.Label_Menu_Home_Text = QLabel(self.Button_Menu_Home)
        self.Label_Menu_Home_Text.setObjectName(u"Label_Menu_Home_Text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Label_Menu_Home_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_Home_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_Home_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_8.addWidget(self.Label_Menu_Home_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Home)

        self.Button_Menu_Download = QToolButton(self.Frame_Menu)
        self.Button_Menu_Download.setObjectName(u"Button_Menu_Download")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Download.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Download.setSizePolicy(sizePolicy1)
        self.Button_Menu_Download.setMinimumSize(QSize(0, 48))
        self.Button_Menu_Download.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 123), stop:1 transparent);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(120, 180, 240);\n"
"	border-right-color: transparent;\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	/*padding-left: 0.6px;*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.Button_Menu_Download)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Env_Install_Icon = QLabel(self.Button_Menu_Download)
        self.Label_Menu_Env_Install_Icon.setObjectName(u"Label_Menu_Env_Install_Icon")
        self.Label_Menu_Env_Install_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Env_Install_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_Env_Install_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Box.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_7.addWidget(self.Label_Menu_Env_Install_Icon)

        self.Label_Menu_Env_Install_Text = QLabel(self.Button_Menu_Download)
        self.Label_Menu_Env_Install_Text.setObjectName(u"Label_Menu_Env_Install_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_Env_Install_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_Env_Install_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_Env_Install_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_7.addWidget(self.Label_Menu_Env_Install_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Download)

        self.Button_Menu_Models = QToolButton(self.Frame_Menu)
        self.Button_Menu_Models.setObjectName(u"Button_Menu_Models")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Models.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Models.setSizePolicy(sizePolicy1)
        self.Button_Menu_Models.setMinimumSize(QSize(0, 48))
        self.Button_Menu_Models.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 123), stop:1 transparent);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(120, 180, 240);\n"
"	border-right-color: transparent;\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	/*padding-left: 0.6px;*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_34 = QHBoxLayout(self.Button_Menu_Models)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Models_Icon = QLabel(self.Button_Menu_Models)
        self.Label_Menu_Models_Icon.setObjectName(u"Label_Menu_Models_Icon")
        self.Label_Menu_Models_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Models_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_Models_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Boxes.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_34.addWidget(self.Label_Menu_Models_Icon)

        self.Label_Menu_Models_Text = QLabel(self.Button_Menu_Models)
        self.Label_Menu_Models_Text.setObjectName(u"Label_Menu_Models_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_Models_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_Models_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_Models_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_34.addWidget(self.Label_Menu_Models_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Models)

        self.Button_Menu_Process = QToolButton(self.Frame_Menu)
        self.Button_Menu_Process.setObjectName(u"Button_Menu_Process")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Process.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Process.setSizePolicy(sizePolicy1)
        self.Button_Menu_Process.setMinimumSize(QSize(0, 48))
        self.Button_Menu_Process.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 123), stop:1 transparent);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(120, 180, 240);\n"
"	border-right-color: transparent;\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	/*padding-left: 0.6px;*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_33 = QHBoxLayout(self.Button_Menu_Process)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Process_Icon = QLabel(self.Button_Menu_Process)
        self.Label_Menu_Process_Icon.setObjectName(u"Label_Menu_Process_Icon")
        self.Label_Menu_Process_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Process_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_Process_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Audio.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_33.addWidget(self.Label_Menu_Process_Icon)

        self.Label_Menu_Process_Text = QLabel(self.Button_Menu_Process)
        self.Label_Menu_Process_Text.setObjectName(u"Label_Menu_Process_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_Process_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_Process_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_Process_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_33.addWidget(self.Label_Menu_Process_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Process)

        self.Button_Menu_ASR = QToolButton(self.Frame_Menu)
        self.Button_Menu_ASR.setObjectName(u"Button_Menu_ASR")
        sizePolicy1.setHeightForWidth(self.Button_Menu_ASR.sizePolicy().hasHeightForWidth())
        self.Button_Menu_ASR.setSizePolicy(sizePolicy1)
        self.Button_Menu_ASR.setMinimumSize(QSize(0, 48))
        self.Button_Menu_ASR.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 123), stop:1 transparent);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(120, 180, 240);\n"
"	border-right-color: transparent;\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	/*padding-left: 0.6px;*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.Button_Menu_ASR)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_ASR_Icon = QLabel(self.Button_Menu_ASR)
        self.Label_Menu_ASR_Icon.setObjectName(u"Label_Menu_ASR_Icon")
        self.Label_Menu_ASR_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_ASR_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_ASR_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/ASR.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_10.addWidget(self.Label_Menu_ASR_Icon)

        self.Label_Menu_ASR_Text = QLabel(self.Button_Menu_ASR)
        self.Label_Menu_ASR_Text.setObjectName(u"Label_Menu_ASR_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_ASR_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_ASR_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_ASR_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_10.addWidget(self.Label_Menu_ASR_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_ASR)

        self.Button_Menu_STT = QToolButton(self.Frame_Menu)
        self.Button_Menu_STT.setObjectName(u"Button_Menu_STT")
        sizePolicy1.setHeightForWidth(self.Button_Menu_STT.sizePolicy().hasHeightForWidth())
        self.Button_Menu_STT.setSizePolicy(sizePolicy1)
        self.Button_Menu_STT.setMinimumSize(QSize(0, 48))
        self.Button_Menu_STT.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 123), stop:1 transparent);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(120, 180, 240);\n"
"	border-right-color: transparent;\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	/*padding-left: 0.6px;*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_36 = QHBoxLayout(self.Button_Menu_STT)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_STT_Icon = QLabel(self.Button_Menu_STT)
        self.Label_Menu_STT_Icon.setObjectName(u"Label_Menu_STT_Icon")
        self.Label_Menu_STT_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_STT_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_STT_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/STT.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_36.addWidget(self.Label_Menu_STT_Icon)

        self.Label_Menu_STT_Text = QLabel(self.Button_Menu_STT)
        self.Label_Menu_STT_Text.setObjectName(u"Label_Menu_STT_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_STT_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_STT_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_STT_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_36.addWidget(self.Label_Menu_STT_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_STT)

        self.Button_Menu_Dataset = QToolButton(self.Frame_Menu)
        self.Button_Menu_Dataset.setObjectName(u"Button_Menu_Dataset")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Dataset.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Dataset.setSizePolicy(sizePolicy1)
        self.Button_Menu_Dataset.setMinimumSize(QSize(0, 48))
        self.Button_Menu_Dataset.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 123), stop:1 transparent);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(120, 180, 240);\n"
"	border-right-color: transparent;\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	/*padding-left: 0.6px;*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_38 = QHBoxLayout(self.Button_Menu_Dataset)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Dataset_Icon = QLabel(self.Button_Menu_Dataset)
        self.Label_Menu_Dataset_Icon.setObjectName(u"Label_Menu_Dataset_Icon")
        self.Label_Menu_Dataset_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Dataset_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_Dataset_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Dataset.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_38.addWidget(self.Label_Menu_Dataset_Icon)

        self.Label_Menu_Dataset_Text = QLabel(self.Button_Menu_Dataset)
        self.Label_Menu_Dataset_Text.setObjectName(u"Label_Menu_Dataset_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_Dataset_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_Dataset_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_Dataset_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_38.addWidget(self.Label_Menu_Dataset_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Dataset)

        self.Button_Menu_Train = QToolButton(self.Frame_Menu)
        self.Button_Menu_Train.setObjectName(u"Button_Menu_Train")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Train.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Train.setSizePolicy(sizePolicy1)
        self.Button_Menu_Train.setMinimumSize(QSize(0, 48))
        self.Button_Menu_Train.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 123), stop:1 transparent);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(120, 180, 240);\n"
"	border-right-color: transparent;\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	/*padding-left: 0.6px;*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_40 = QHBoxLayout(self.Button_Menu_Train)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Train_Icon = QLabel(self.Button_Menu_Train)
        self.Label_Menu_Train_Icon.setObjectName(u"Label_Menu_Train_Icon")
        self.Label_Menu_Train_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Train_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_Train_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/HDD.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_40.addWidget(self.Label_Menu_Train_Icon)

        self.Label_Menu_Train_Text = QLabel(self.Button_Menu_Train)
        self.Label_Menu_Train_Text.setObjectName(u"Label_Menu_Train_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_Train_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_Train_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_Train_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_40.addWidget(self.Label_Menu_Train_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Train)

        self.Button_Menu_TTS = QToolButton(self.Frame_Menu)
        self.Button_Menu_TTS.setObjectName(u"Button_Menu_TTS")
        sizePolicy1.setHeightForWidth(self.Button_Menu_TTS.sizePolicy().hasHeightForWidth())
        self.Button_Menu_TTS.setSizePolicy(sizePolicy1)
        self.Button_Menu_TTS.setMinimumSize(QSize(0, 48))
        self.Button_Menu_TTS.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 123), stop:1 transparent);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(120, 180, 240);\n"
"	border-right-color: transparent;\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	/*padding-left: 0.6px;*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_47 = QHBoxLayout(self.Button_Menu_TTS)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_TTS_Icon = QLabel(self.Button_Menu_TTS)
        self.Label_Menu_TTS_Icon.setObjectName(u"Label_Menu_TTS_Icon")
        self.Label_Menu_TTS_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_TTS_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_TTS_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/TTS.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_47.addWidget(self.Label_Menu_TTS_Icon)

        self.Label_Menu_TTS_Text = QLabel(self.Button_Menu_TTS)
        self.Label_Menu_TTS_Text.setObjectName(u"Label_Menu_TTS_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_TTS_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_TTS_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_TTS_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_47.addWidget(self.Label_Menu_TTS_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_TTS)

        self.VerticalSpacer_Menu = QSpacerItem(20, 522, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.VerticalSpacer_Menu)

        self.Button_Menu_Settings = QToolButton(self.Frame_Menu)
        self.Button_Menu_Settings.setObjectName(u"Button_Menu_Settings")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Settings.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Settings.setSizePolicy(sizePolicy1)
        self.Button_Menu_Settings.setMinimumSize(QSize(0, 48))
        self.Button_Menu_Settings.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 123), stop:1 transparent);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(120, 180, 240);\n"
"	border-right-color: transparent;\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	/*padding-left: 0.6px;*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_9 = QHBoxLayout(self.Button_Menu_Settings)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Settings_Icon = QLabel(self.Button_Menu_Settings)
        self.Label_Menu_Settings_Icon.setObjectName(u"Label_Menu_Settings_Icon")
        self.Label_Menu_Settings_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Settings_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_Settings_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Settings.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_9.addWidget(self.Label_Menu_Settings_Icon)

        self.Label_Menu_Settings_Text = QLabel(self.Button_Menu_Settings)
        self.Label_Menu_Settings_Text.setObjectName(u"Label_Menu_Settings_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_Settings_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_Settings_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_Settings_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_9.addWidget(self.Label_Menu_Settings_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Settings)

        self.Button_Menu_Info = QToolButton(self.Frame_Menu)
        self.Button_Menu_Info.setObjectName(u"Button_Menu_Info")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Info.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Info.setSizePolicy(sizePolicy1)
        self.Button_Menu_Info.setMinimumSize(QSize(0, 48))
        self.Button_Menu_Info.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 123), stop:1 transparent);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(120, 180, 240);\n"
"	border-right-color: transparent;\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	/*padding-left: 0.6px;*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_13 = QHBoxLayout(self.Button_Menu_Info)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Info_Icon = QLabel(self.Button_Menu_Info)
        self.Label_Menu_Info_Icon.setObjectName(u"Label_Menu_Info_Icon")
        self.Label_Menu_Info_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Info_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_Info_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Info.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_13.addWidget(self.Label_Menu_Info_Icon)

        self.Label_Menu_Info_Text = QLabel(self.Button_Menu_Info)
        self.Label_Menu_Info_Text.setObjectName(u"Label_Menu_Info_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_Info_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_Info_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_Info_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_13.addWidget(self.Label_Menu_Info_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Info)


        self.horizontalLayout_2.addWidget(self.Frame_Menu)

        self.Frame_Pages = QFrame(self.Content)
        self.Frame_Pages.setObjectName(u"Frame_Pages")
        self.verticalLayout_5 = QVBoxLayout(self.Frame_Pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Pages = QStackedWidget(self.Frame_Pages)
        self.StackedWidget_Pages.setObjectName(u"StackedWidget_Pages")
        self.Page_Home = QWidget()
        self.Page_Home.setObjectName(u"Page_Home")
        self.verticalLayout_99 = QVBoxLayout(self.Page_Home)
        self.verticalLayout_99.setSpacing(21)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(21, 12, 21, 12)
        self.Frame_High_Home = QFrame(self.Page_Home)
        self.Frame_High_Home.setObjectName(u"Frame_High_Home")
        self.Frame_High_Home.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.verticalLayout_100 = QVBoxLayout(self.Frame_High_Home)
        self.verticalLayout_100.setSpacing(21)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(12, 0, 12, 0)
        self.TextBrowser_Pic_Home = QTextBrowser(self.Frame_High_Home)
        self.TextBrowser_Pic_Home.setObjectName(u"TextBrowser_Pic_Home")
        self.TextBrowser_Pic_Home.setMinimumSize(QSize(0, 210))
        self.TextBrowser_Pic_Home.setStyleSheet(u"QTextBrowser {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QTextBrowser:hover {\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page"
                        ":vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontro"
                        "l-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.verticalLayout_100.addWidget(self.TextBrowser_Pic_Home)

        self.TextBrowser_Text_Home = QTextBrowser(self.Frame_High_Home)
        self.TextBrowser_Text_Home.setObjectName(u"TextBrowser_Text_Home")
        self.TextBrowser_Text_Home.setStyleSheet(u"QTextBrowser {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"	border-radius: 6px;\n"
"}\n"
"QTextBrowser:hover {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-ra"
                        "dius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:hori"
                        "zontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.verticalLayout_100.addWidget(self.TextBrowser_Text_Home)


        self.verticalLayout_99.addWidget(self.Frame_High_Home)

        self.Frame_Low_Home = QFrame(self.Page_Home)
        self.Frame_Low_Home.setObjectName(u"Frame_Low_Home")
        self.Frame_Low_Home.setMinimumSize(QSize(0, 90))
        self.Frame_Low_Home.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.Frame_Low_Home)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 0, 12, 0)
        self.Button_Demo = QToolButton(self.Frame_Low_Home)
        self.Button_Demo.setObjectName(u"Button_Demo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Button_Demo.sizePolicy().hasHeightForWidth())
        self.Button_Demo.setSizePolicy(sizePolicy3)
        self.Button_Demo.setMinimumSize(QSize(210, 75))
        self.Button_Demo.setStyleSheet(u"QToolButton {\n"
"	background-color: transparent;\n"
"	/*padding: 12px 60px;*/\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QToolButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_70 = QHBoxLayout(self.Button_Demo)
        self.horizontalLayout_70.setSpacing(12)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(21, 12, 21, 12)
        self.Label_Demo_Icon = QLabel(self.Button_Demo)
        self.Label_Demo_Icon.setObjectName(u"Label_Demo_Icon")
        self.Label_Demo_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	image: url(:/Button_Icon/Sources/Play.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_70.addWidget(self.Label_Demo_Icon)

        self.Label_Demo_Text = QLabel(self.Button_Demo)
        self.Label_Demo_Text.setObjectName(u"Label_Demo_Text")
        self.Label_Demo_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_70.addWidget(self.Label_Demo_Text)

        self.horizontalLayout_70.setStretch(0, 2)
        self.horizontalLayout_70.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.Button_Demo)

        self.HorizontalSpacer_Low_Home_1 = QSpacerItem(107, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.HorizontalSpacer_Low_Home_1)

        self.Button_Server = QToolButton(self.Frame_Low_Home)
        self.Button_Server.setObjectName(u"Button_Server")
        sizePolicy3.setHeightForWidth(self.Button_Server.sizePolicy().hasHeightForWidth())
        self.Button_Server.setSizePolicy(sizePolicy3)
        self.Button_Server.setMinimumSize(QSize(210, 75))
        self.Button_Server.setStyleSheet(u"QToolButton {\n"
"	background-color: transparent;\n"
"	/*padding: 12px 60px;*/\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QToolButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_71 = QHBoxLayout(self.Button_Server)
        self.horizontalLayout_71.setSpacing(12)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(21, 12, 21, 12)
        self.Label_Server_Icon = QLabel(self.Button_Server)
        self.Label_Server_Icon.setObjectName(u"Label_Server_Icon")
        self.Label_Server_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	image: url(:/Button_Icon/Sources/Server.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_71.addWidget(self.Label_Server_Icon)

        self.Label_Server_Text = QLabel(self.Button_Server)
        self.Label_Server_Text.setObjectName(u"Label_Server_Text")
        self.Label_Server_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_71.addWidget(self.Label_Server_Text)

        self.horizontalLayout_71.setStretch(0, 2)
        self.horizontalLayout_71.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.Button_Server)

        self.HorizontalSpacer_Low_Home_2 = QSpacerItem(106, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.HorizontalSpacer_Low_Home_2)

        self.Button_Repo = QToolButton(self.Frame_Low_Home)
        self.Button_Repo.setObjectName(u"Button_Repo")
        sizePolicy3.setHeightForWidth(self.Button_Repo.sizePolicy().hasHeightForWidth())
        self.Button_Repo.setSizePolicy(sizePolicy3)
        self.Button_Repo.setMinimumSize(QSize(210, 75))
        self.Button_Repo.setStyleSheet(u"QToolButton {\n"
"	background-color: transparent;\n"
"	/*padding: 12px 60px;*/\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QToolButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_76 = QHBoxLayout(self.Button_Repo)
        self.horizontalLayout_76.setSpacing(12)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(21, 12, 21, 12)
        self.Label_Repo_Icon = QLabel(self.Button_Repo)
        self.Label_Repo_Icon.setObjectName(u"Label_Repo_Icon")
        self.Label_Repo_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	image: url(:/Button_Icon/Sources/GitHub.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_76.addWidget(self.Label_Repo_Icon)

        self.Label_Repo_Text = QLabel(self.Button_Repo)
        self.Label_Repo_Text.setObjectName(u"Label_Repo_Text")
        self.Label_Repo_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_76.addWidget(self.Label_Repo_Text)

        self.horizontalLayout_76.setStretch(0, 2)
        self.horizontalLayout_76.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.Button_Repo)

        self.HorizontalSpacer_Low_Home_3 = QSpacerItem(107, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.HorizontalSpacer_Low_Home_3)

        self.Button_Donate = QToolButton(self.Frame_Low_Home)
        self.Button_Donate.setObjectName(u"Button_Donate")
        sizePolicy3.setHeightForWidth(self.Button_Donate.sizePolicy().hasHeightForWidth())
        self.Button_Donate.setSizePolicy(sizePolicy3)
        self.Button_Donate.setMinimumSize(QSize(210, 75))
        self.Button_Donate.setStyleSheet(u"QToolButton {\n"
"	background-color: transparent;\n"
"	/*padding: 12px 60px;*/\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QToolButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_79 = QHBoxLayout(self.Button_Donate)
        self.horizontalLayout_79.setSpacing(12)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(21, 12, 21, 12)
        self.Label_Donate_Icon = QLabel(self.Button_Donate)
        self.Label_Donate_Icon.setObjectName(u"Label_Donate_Icon")
        self.Label_Donate_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	image: url(:/Button_Icon/Sources/Heart.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	/*padding: 11.1px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;*/\n"
"}")

        self.horizontalLayout_79.addWidget(self.Label_Donate_Icon)

        self.Label_Donate_Text = QLabel(self.Button_Donate)
        self.Label_Donate_Text.setObjectName(u"Label_Donate_Text")
        self.Label_Donate_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_79.addWidget(self.Label_Donate_Text)

        self.horizontalLayout_79.setStretch(0, 2)
        self.horizontalLayout_79.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.Button_Donate)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(2, 3)
        self.horizontalLayout_5.setStretch(4, 3)
        self.horizontalLayout_5.setStretch(6, 3)

        self.verticalLayout_99.addWidget(self.Frame_Low_Home)

        self.StackedWidget_Pages.addWidget(self.Page_Home)
        self.Page_Download = QWidget()
        self.Page_Download.setObjectName(u"Page_Download")
        self.verticalLayout_81 = QVBoxLayout(self.Page_Download)
        self.verticalLayout_81.setSpacing(21)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(21, 12, 21, 12)
        self.Frame_Env_Install_Top = QFrame(self.Page_Download)
        self.Frame_Env_Install_Top.setObjectName(u"Frame_Env_Install_Top")
        self.Frame_Env_Install_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Env_Install_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.Frame_Env_Install_Top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_Env_Install_Title = QToolButton(self.Frame_Env_Install_Top)
        self.ToolButton_Env_Install_Title.setObjectName(u"ToolButton_Env_Install_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_Env_Install_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_Env_Install_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_Env_Install_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}/*\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}*/\n"
"\n"
"QToolTip {\n"
"	co"
                        "lor: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_3.addWidget(self.ToolButton_Env_Install_Title)

        self.Frame_Env_Install_Title_Spacer = QLabel(self.Frame_Env_Install_Top)
        self.Frame_Env_Install_Title_Spacer.setObjectName(u"Frame_Env_Install_Title_Spacer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Frame_Env_Install_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Env_Install_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_Env_Install_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;*/\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_3.addWidget(self.Frame_Env_Install_Title_Spacer)


        self.verticalLayout_81.addWidget(self.Frame_Env_Install_Top)

        self.Frame_Env_Install_Middle = QFrame(self.Page_Download)
        self.Frame_Env_Install_Middle.setObjectName(u"Frame_Env_Install_Middle")
        self.Frame_Env_Install_Middle.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.verticalLayout_34 = QVBoxLayout(self.Frame_Env_Install_Middle)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.Frame_Env_Install_Aria2 = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_Aria2.setObjectName(u"Frame_Env_Install_Aria2")
        self.Frame_Env_Install_Aria2.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_Aria2.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_Aria2.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.gridLayout_75 = QGridLayout(self.Frame_Env_Install_Aria2)
        self.gridLayout_75.setSpacing(12)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.gridLayout_75.setContentsMargins(21, 12, 21, 12)
        self.Label_Env_Install_Aria2 = QLabel(self.Frame_Env_Install_Aria2)
        self.Label_Env_Install_Aria2.setObjectName(u"Label_Env_Install_Aria2")
        self.Label_Env_Install_Aria2.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_75.addWidget(self.Label_Env_Install_Aria2, 0, 0, 1, 1)

        self.HorizontalSpacer_Env_Install_Aria2 = QSpacerItem(969, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_75.addItem(self.HorizontalSpacer_Env_Install_Aria2, 0, 1, 1, 1)

        self.Button_Install_Aria2 = QPushButton(self.Frame_Env_Install_Aria2)
        self.Button_Install_Aria2.setObjectName(u"Button_Install_Aria2")
        self.Button_Install_Aria2.setMaximumSize(QSize(33, 33))
        self.Button_Install_Aria2.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	image: url(:/Button_Icon/Sources/RepeatArrow.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_75.addWidget(self.Button_Install_Aria2, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_Aria2 = QProgressBar(self.Frame_Env_Install_Aria2)
        self.ProgressBar_Env_Install_Aria2.setObjectName(u"ProgressBar_Env_Install_Aria2")
        self.ProgressBar_Env_Install_Aria2.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Env_Install_Aria2.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 3px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgb(120, 180, 240));\n"
"}")

        self.gridLayout_75.addWidget(self.ProgressBar_Env_Install_Aria2, 1, 0, 1, 2)

        self.Label_Env_Install_Aria2_Status = QLabel(self.Frame_Env_Install_Aria2)
        self.Label_Env_Install_Aria2_Status.setObjectName(u"Label_Env_Install_Aria2_Status")
        self.Label_Env_Install_Aria2_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_75.addWidget(self.Label_Env_Install_Aria2_Status, 2, 0, 1, 1)


        self.verticalLayout_34.addWidget(self.Frame_Env_Install_Aria2)

        self.Frame_Env_Install_FFmpeg = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_FFmpeg.setObjectName(u"Frame_Env_Install_FFmpeg")
        self.Frame_Env_Install_FFmpeg.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_FFmpeg.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_FFmpeg.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.Frame_Env_Install_FFmpeg)
        self.gridLayout_2.setSpacing(12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(21, 12, 21, 12)
        self.Label_Env_Install_FFmpeg = QLabel(self.Frame_Env_Install_FFmpeg)
        self.Label_Env_Install_FFmpeg.setObjectName(u"Label_Env_Install_FFmpeg")
        self.Label_Env_Install_FFmpeg.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_2.addWidget(self.Label_Env_Install_FFmpeg, 0, 0, 1, 1)

        self.HorizontalSpacer_Env_Install_FFmpeg = QSpacerItem(969, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.HorizontalSpacer_Env_Install_FFmpeg, 0, 1, 1, 1)

        self.Button_Install_FFmpeg = QPushButton(self.Frame_Env_Install_FFmpeg)
        self.Button_Install_FFmpeg.setObjectName(u"Button_Install_FFmpeg")
        self.Button_Install_FFmpeg.setMaximumSize(QSize(33, 33))
        self.Button_Install_FFmpeg.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	image: url(:/Button_Icon/Sources/RepeatArrow.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_2.addWidget(self.Button_Install_FFmpeg, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_FFmpeg = QProgressBar(self.Frame_Env_Install_FFmpeg)
        self.ProgressBar_Env_Install_FFmpeg.setObjectName(u"ProgressBar_Env_Install_FFmpeg")
        self.ProgressBar_Env_Install_FFmpeg.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Env_Install_FFmpeg.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 3px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgb(120, 180, 240));\n"
"}")

        self.gridLayout_2.addWidget(self.ProgressBar_Env_Install_FFmpeg, 1, 0, 1, 2)

        self.Label_Env_Install_FFmpeg_Status = QLabel(self.Frame_Env_Install_FFmpeg)
        self.Label_Env_Install_FFmpeg_Status.setObjectName(u"Label_Env_Install_FFmpeg_Status")
        self.Label_Env_Install_FFmpeg_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_2.addWidget(self.Label_Env_Install_FFmpeg_Status, 2, 0, 1, 1)


        self.verticalLayout_34.addWidget(self.Frame_Env_Install_FFmpeg)

        self.Frame_Env_Install_Python = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_Python.setObjectName(u"Frame_Env_Install_Python")
        self.Frame_Env_Install_Python.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_Python.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_Python.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.Frame_Env_Install_Python)
        self.gridLayout_3.setSpacing(12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(21, 12, 21, 12)
        self.Label_Env_Install_Python = QLabel(self.Frame_Env_Install_Python)
        self.Label_Env_Install_Python.setObjectName(u"Label_Env_Install_Python")
        self.Label_Env_Install_Python.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_3.addWidget(self.Label_Env_Install_Python, 0, 0, 1, 1)

        self.HorizontalSpacer_Env_Install_Python = QSpacerItem(969, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.HorizontalSpacer_Env_Install_Python, 0, 1, 1, 1)

        self.Button_Install_Python = QPushButton(self.Frame_Env_Install_Python)
        self.Button_Install_Python.setObjectName(u"Button_Install_Python")
        self.Button_Install_Python.setMaximumSize(QSize(33, 33))
        self.Button_Install_Python.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	image: url(:/Button_Icon/Sources/RepeatArrow.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_3.addWidget(self.Button_Install_Python, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_Python = QProgressBar(self.Frame_Env_Install_Python)
        self.ProgressBar_Env_Install_Python.setObjectName(u"ProgressBar_Env_Install_Python")
        self.ProgressBar_Env_Install_Python.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Env_Install_Python.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 3px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgb(120, 180, 240));\n"
"}")

        self.gridLayout_3.addWidget(self.ProgressBar_Env_Install_Python, 1, 0, 1, 2)

        self.Label_Env_Install_Python_Status = QLabel(self.Frame_Env_Install_Python)
        self.Label_Env_Install_Python_Status.setObjectName(u"Label_Env_Install_Python_Status")
        self.Label_Env_Install_Python_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_3.addWidget(self.Label_Env_Install_Python_Status, 2, 0, 1, 1)


        self.verticalLayout_34.addWidget(self.Frame_Env_Install_Python)

        self.Frame_Env_Install_PyReqs = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_PyReqs.setObjectName(u"Frame_Env_Install_PyReqs")
        self.Frame_Env_Install_PyReqs.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_PyReqs.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_PyReqs.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.Frame_Env_Install_PyReqs)
        self.gridLayout_4.setSpacing(12)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(21, 12, 21, 12)
        self.Label_Env_Install_PyReqs = QLabel(self.Frame_Env_Install_PyReqs)
        self.Label_Env_Install_PyReqs.setObjectName(u"Label_Env_Install_PyReqs")
        self.Label_Env_Install_PyReqs.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_4.addWidget(self.Label_Env_Install_PyReqs, 0, 0, 1, 1)

        self.HorizontalSpacer_Env_Install_PyReqs = QSpacerItem(969, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.HorizontalSpacer_Env_Install_PyReqs, 0, 1, 1, 1)

        self.Button_Install_PyReqs = QPushButton(self.Frame_Env_Install_PyReqs)
        self.Button_Install_PyReqs.setObjectName(u"Button_Install_PyReqs")
        self.Button_Install_PyReqs.setMaximumSize(QSize(33, 33))
        self.Button_Install_PyReqs.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	image: url(:/Button_Icon/Sources/RepeatArrow.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_4.addWidget(self.Button_Install_PyReqs, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_PyReqs = QProgressBar(self.Frame_Env_Install_PyReqs)
        self.ProgressBar_Env_Install_PyReqs.setObjectName(u"ProgressBar_Env_Install_PyReqs")
        self.ProgressBar_Env_Install_PyReqs.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Env_Install_PyReqs.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 3px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgb(120, 180, 240));\n"
"}")

        self.gridLayout_4.addWidget(self.ProgressBar_Env_Install_PyReqs, 1, 0, 1, 2)

        self.Label_Env_Install_PyReqs_Status = QLabel(self.Frame_Env_Install_PyReqs)
        self.Label_Env_Install_PyReqs_Status.setObjectName(u"Label_Env_Install_PyReqs_Status")
        self.Label_Env_Install_PyReqs_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_4.addWidget(self.Label_Env_Install_PyReqs_Status, 2, 0, 1, 1)


        self.verticalLayout_34.addWidget(self.Frame_Env_Install_PyReqs)

        self.Frame_Env_Install_Pytorch = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_Pytorch.setObjectName(u"Frame_Env_Install_Pytorch")
        self.Frame_Env_Install_Pytorch.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_Pytorch.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_Pytorch.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.gridLayout_5 = QGridLayout(self.Frame_Env_Install_Pytorch)
        self.gridLayout_5.setSpacing(12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(21, 12, 21, 12)
        self.Label_Env_Install_Pytorch = QLabel(self.Frame_Env_Install_Pytorch)
        self.Label_Env_Install_Pytorch.setObjectName(u"Label_Env_Install_Pytorch")
        self.Label_Env_Install_Pytorch.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_5.addWidget(self.Label_Env_Install_Pytorch, 0, 0, 1, 1)

        self.HorizontalSpacer_Env_Install_Pytorch = QSpacerItem(969, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.HorizontalSpacer_Env_Install_Pytorch, 0, 1, 1, 1)

        self.Button_Install_Pytorch = QPushButton(self.Frame_Env_Install_Pytorch)
        self.Button_Install_Pytorch.setObjectName(u"Button_Install_Pytorch")
        self.Button_Install_Pytorch.setMaximumSize(QSize(33, 33))
        self.Button_Install_Pytorch.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	image: url(:/Button_Icon/Sources/RepeatArrow.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_5.addWidget(self.Button_Install_Pytorch, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_Pytorch = QProgressBar(self.Frame_Env_Install_Pytorch)
        self.ProgressBar_Env_Install_Pytorch.setObjectName(u"ProgressBar_Env_Install_Pytorch")
        self.ProgressBar_Env_Install_Pytorch.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Env_Install_Pytorch.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 3px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgb(120, 180, 240));\n"
"}")

        self.gridLayout_5.addWidget(self.ProgressBar_Env_Install_Pytorch, 1, 0, 1, 2)

        self.Label_Env_Install_Pytorch_Status = QLabel(self.Frame_Env_Install_Pytorch)
        self.Label_Env_Install_Pytorch_Status.setObjectName(u"Label_Env_Install_Pytorch_Status")
        self.Label_Env_Install_Pytorch_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_5.addWidget(self.Label_Env_Install_Pytorch_Status, 2, 0, 1, 1)


        self.verticalLayout_34.addWidget(self.Frame_Env_Install_Pytorch)


        self.verticalLayout_81.addWidget(self.Frame_Env_Install_Middle)

        self.VerticalSpacer_Download = QSpacerItem(17, 198, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_81.addItem(self.VerticalSpacer_Download)

        self.StackedWidget_Pages.addWidget(self.Page_Download)
        self.Page_Models = QWidget()
        self.Page_Models.setObjectName(u"Page_Models")
        self.verticalLayout_244 = QVBoxLayout(self.Page_Models)
        self.verticalLayout_244.setSpacing(21)
        self.verticalLayout_244.setObjectName(u"verticalLayout_244")
        self.verticalLayout_244.setContentsMargins(21, 12, 21, 12)
        self.Frame_Models_Top = QFrame(self.Page_Models)
        self.Frame_Models_Top.setObjectName(u"Frame_Models_Top")
        self.Frame_Models_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Models_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_99 = QHBoxLayout(self.Frame_Models_Top)
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_Models_ASR_Title = QToolButton(self.Frame_Models_Top)
        self.ToolButton_Models_ASR_Title.setObjectName(u"ToolButton_Models_ASR_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_Models_ASR_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_Models_ASR_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_Models_ASR_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color:"
                        " rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_99.addWidget(self.ToolButton_Models_ASR_Title)

        self.ToolButton_Models_STT_Title = QToolButton(self.Frame_Models_Top)
        self.ToolButton_Models_STT_Title.setObjectName(u"ToolButton_Models_STT_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_Models_STT_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_Models_STT_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_Models_STT_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color:"
                        " rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_99.addWidget(self.ToolButton_Models_STT_Title)

        self.ToolButton_Models_TTS_Title = QToolButton(self.Frame_Models_Top)
        self.ToolButton_Models_TTS_Title.setObjectName(u"ToolButton_Models_TTS_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_Models_TTS_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_Models_TTS_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_Models_TTS_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color:"
                        " rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_99.addWidget(self.ToolButton_Models_TTS_Title)

        self.Frame_Models_Title_Spacer = QLabel(self.Frame_Models_Top)
        self.Frame_Models_Title_Spacer.setObjectName(u"Frame_Models_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_Models_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Models_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_Models_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;*/\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_99.addWidget(self.Frame_Models_Title_Spacer)


        self.verticalLayout_244.addWidget(self.Frame_Models_Top)

        self.StackedWidget_Pages_Models = QStackedWidget(self.Page_Models)
        self.StackedWidget_Pages_Models.setObjectName(u"StackedWidget_Pages_Models")
        self.StackedWidget_Pages_Models.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*\n"
"QTabWidget {\n"
"	background-color: transparent;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"}\n"
"QTabWidget::pane {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"	font-size: 18px;\n"
"	font-weight: 420;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 12px;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:selected {\n"
"	color: rgba(255, 255, 255, 255);\n"
"}\n"
"QTabBar::tab:hover:!selected {\n"
"}\n"
"\n"
"\n"
"QTabBar QToolButton {\n"
"}\n"
"QTabBar QToolButton:hover {\n"
"}\n"
"*/")
        self.SubPage_Models_ASR = QWidget()
        self.SubPage_Models_ASR.setObjectName(u"SubPage_Models_ASR")
        self.gridLayout_7 = QGridLayout(self.SubPage_Models_ASR)
        self.gridLayout_7.setSpacing(12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.TabWidget_Models_ASR = QTabWidget(self.SubPage_Models_ASR)
        self.TabWidget_Models_ASR.setObjectName(u"TabWidget_Models_ASR")
        self.TabWidget_Models_ASR.setStyleSheet(u"QTabBar::tab {\n"
"    min-width: 84px;\n"
"	min-height: 42px;\n"
"	font-size: 21px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:hover, QTabBar::tab:selected {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"QTabWidget::pane {\n"
"	background: rgba(36, 36, 36, 123);;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}")
        self.Tab_Models_ASR_VPR = QWidget()
        self.Tab_Models_ASR_VPR.setObjectName(u"Tab_Models_ASR_VPR")
        self.verticalLayout_27 = QVBoxLayout(self.Tab_Models_ASR_VPR)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_ASR_VPR = Table_ViewModels(self.Tab_Models_ASR_VPR)
        self.Table_Models_ASR_VPR.setObjectName(u"Table_Models_ASR_VPR")

        self.verticalLayout_27.addWidget(self.Table_Models_ASR_VPR)

        self.TabWidget_Models_ASR.addTab(self.Tab_Models_ASR_VPR, "")

        self.gridLayout_7.addWidget(self.TabWidget_Models_ASR, 0, 0, 1, 1)

        self.StackedWidget_Pages_Models.addWidget(self.SubPage_Models_ASR)
        self.SubPage_Models_STT = QWidget()
        self.SubPage_Models_STT.setObjectName(u"SubPage_Models_STT")
        self.gridLayout_11 = QGridLayout(self.SubPage_Models_STT)
        self.gridLayout_11.setSpacing(12)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.TabWidget_Models_STT = QTabWidget(self.SubPage_Models_STT)
        self.TabWidget_Models_STT.setObjectName(u"TabWidget_Models_STT")
        self.TabWidget_Models_STT.setStyleSheet(u"QTabBar::tab {\n"
"    min-width: 84px;\n"
"	min-height: 42px;\n"
"	font-size: 21px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:hover, QTabBar::tab:selected {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"QTabWidget::pane {\n"
"	background: rgba(36, 36, 36, 123);;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}")
        self.Tab_Models_STT_Whisper = QWidget()
        self.Tab_Models_STT_Whisper.setObjectName(u"Tab_Models_STT_Whisper")
        self.verticalLayout_46 = QVBoxLayout(self.Tab_Models_STT_Whisper)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_STT_Whisper = Table_ViewModels(self.Tab_Models_STT_Whisper)
        self.Table_Models_STT_Whisper.setObjectName(u"Table_Models_STT_Whisper")

        self.verticalLayout_46.addWidget(self.Table_Models_STT_Whisper)

        self.TabWidget_Models_STT.addTab(self.Tab_Models_STT_Whisper, "")

        self.gridLayout_11.addWidget(self.TabWidget_Models_STT, 0, 0, 1, 1)

        self.StackedWidget_Pages_Models.addWidget(self.SubPage_Models_STT)
        self.SubPage_Models_TTS = QWidget()
        self.SubPage_Models_TTS.setObjectName(u"SubPage_Models_TTS")
        self.gridLayout_10 = QGridLayout(self.SubPage_Models_TTS)
        self.gridLayout_10.setSpacing(12)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.TabWidget_Models_TTS = QTabWidget(self.SubPage_Models_TTS)
        self.TabWidget_Models_TTS.setObjectName(u"TabWidget_Models_TTS")
        self.TabWidget_Models_TTS.setStyleSheet(u"QTabBar::tab {\n"
"    min-width: 84px;\n"
"	min-height: 42px;\n"
"	font-size: 21px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:hover, QTabBar::tab:selected {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"QTabWidget::pane {\n"
"	background: rgba(36, 36, 36, 123);;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}")
        self.Tab_Models_TTS_VITS = QWidget()
        self.Tab_Models_TTS_VITS.setObjectName(u"Tab_Models_TTS_VITS")
        self.verticalLayout_38 = QVBoxLayout(self.Tab_Models_TTS_VITS)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_TTS_VITS = Table_ViewModels(self.Tab_Models_TTS_VITS)
        self.Table_Models_TTS_VITS.setObjectName(u"Table_Models_TTS_VITS")

        self.verticalLayout_38.addWidget(self.Table_Models_TTS_VITS)

        self.TabWidget_Models_TTS.addTab(self.Tab_Models_TTS_VITS, "")

        self.gridLayout_10.addWidget(self.TabWidget_Models_TTS, 0, 0, 1, 1)

        self.StackedWidget_Pages_Models.addWidget(self.SubPage_Models_TTS)

        self.verticalLayout_244.addWidget(self.StackedWidget_Pages_Models)

        self.StackedWidget_Pages.addWidget(self.Page_Models)
        self.Page_Process = QWidget()
        self.Page_Process.setObjectName(u"Page_Process")
        self.verticalLayout_40 = QVBoxLayout(self.Page_Process)
        self.verticalLayout_40.setSpacing(21)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(21, 12, 21, 12)
        self.Frame_Process_Top = QFrame(self.Page_Process)
        self.Frame_Process_Top.setObjectName(u"Frame_Process_Top")
        self.Frame_Process_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Process_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_68 = QHBoxLayout(self.Frame_Process_Top)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_AudioProcessor_Title = QToolButton(self.Frame_Process_Top)
        self.ToolButton_AudioProcessor_Title.setObjectName(u"ToolButton_AudioProcessor_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_AudioProcessor_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_AudioProcessor_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_AudioProcessor_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color:"
                        " rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_68.addWidget(self.ToolButton_AudioProcessor_Title)

        self.Frame_Process_Title_Spacer = QLabel(self.Frame_Process_Top)
        self.Frame_Process_Title_Spacer.setObjectName(u"Frame_Process_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_Process_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Process_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_Process_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;*/\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_68.addWidget(self.Frame_Process_Title_Spacer)


        self.verticalLayout_40.addWidget(self.Frame_Process_Top)

        self.StackedWidget_Pages_Process = QStackedWidget(self.Page_Process)
        self.StackedWidget_Pages_Process.setObjectName(u"StackedWidget_Pages_Process")
        self.StackedWidget_Pages_Process.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*\n"
"QTabWidget {\n"
"	background-color: transparent;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"}\n"
"QTabWidget::pane {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"	font-size: 18px;\n"
"	font-weight: 420;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 12px;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:selected {\n"
"	color: rgba(255, 255, 255, 255);\n"
"}\n"
"QTabBar::tab:hover:!selected {\n"
"}\n"
"\n"
"\n"
"QTabBar QToolButton {\n"
"}\n"
"QTabBar QToolButton:hover {\n"
"}\n"
"*/")
        self.Subpage_Process = QWidget()
        self.Subpage_Process.setObjectName(u"Subpage_Process")
        self.gridLayout_6 = QGridLayout(self.Subpage_Process)
        self.gridLayout_6.setSpacing(12)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_Process = QWidget(self.Subpage_Process)
        self.Widget_Left_Process.setObjectName(u"Widget_Left_Process")
        self.Widget_Left_Process.setMinimumSize(QSize(150, 0))
        self.Widget_Left_Process.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_162 = QVBoxLayout(self.Widget_Left_Process)
        self.verticalLayout_162.setSpacing(12)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Process = QTreeWidget(self.Widget_Left_Process)
        __qtreewidgetitem = QTreeWidgetItem(self.TreeWidget_Catalogue_Process)
        QTreeWidgetItem(__qtreewidgetitem)
        self.TreeWidget_Catalogue_Process.setObjectName(u"TreeWidget_Catalogue_Process")
        self.TreeWidget_Catalogue_Process.setStyleSheet(u"QTreeView {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"	background-color: transparent;\n"
"	padding: 2.4px;\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"QTreeView::item:selected {\n"
"    background-color: ;\n"
"}\n"
"\n"
"QTreeView::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeView::branch:open:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeView::branch:closed:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:adjoins-item {\n"
"    background-color: ;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: rgba(45, 45, 45, 135);\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"	background-color: r"
                        "gba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(90, 90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}")

        self.verticalLayout_162.addWidget(self.TreeWidget_Catalogue_Process)


        self.gridLayout_6.addWidget(self.Widget_Left_Process, 0, 0, 1, 1)

        self.ScrollArea_Middle_Process = QScrollArea(self.Subpage_Process)
        self.ScrollArea_Middle_Process.setObjectName(u"ScrollArea_Middle_Process")
        self.ScrollArea_Middle_Process.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_Process.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollArea:hover {\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	"
                        "height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	borde"
                        "r-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")
        self.ScrollArea_Middle_Process.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Process.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_Process = QWidget()
        self.ScrollArea_Middle_WidgetContents_Process.setObjectName(u"ScrollArea_Middle_WidgetContents_Process")
        self.ScrollArea_Middle_WidgetContents_Process.setGeometry(QRect(0, 0, 591, 1484))
        self.verticalLayout_14 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_Process)
        self.verticalLayout_14.setSpacing(12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_Process_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Process)
        self.GroupBox_Process_InputParams.setObjectName(u"GroupBox_Process_InputParams")
        self.GroupBox_Process_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_150 = QVBoxLayout(self.GroupBox_Process_InputParams)
        self.verticalLayout_150.setSpacing(0)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 12, 0, 12)
        self.Frame_Process_InputParams_BasicSettings = QFrame(self.GroupBox_Process_InputParams)
        self.Frame_Process_InputParams_BasicSettings.setObjectName(u"Frame_Process_InputParams_BasicSettings")
        self.verticalLayout_20 = QVBoxLayout(self.Frame_Process_InputParams_BasicSettings)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.Frame_Process_MediaDirInput = QFrame(self.Frame_Process_InputParams_BasicSettings)
        self.Frame_Process_MediaDirInput.setObjectName(u"Frame_Process_MediaDirInput")
        self.Frame_Process_MediaDirInput.setMinimumSize(QSize(0, 105))
        self.Frame_Process_MediaDirInput.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_12 = QGridLayout(self.Frame_Process_MediaDirInput)
        self.gridLayout_12.setSpacing(12)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_MediaDirInput = QLabel(self.Frame_Process_MediaDirInput)
        self.Label_Process_MediaDirInput.setObjectName(u"Label_Process_MediaDirInput")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Label_Process_MediaDirInput.sizePolicy().hasHeightForWidth())
        self.Label_Process_MediaDirInput.setSizePolicy(sizePolicy5)
        self.Label_Process_MediaDirInput.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_12.addWidget(self.Label_Process_MediaDirInput, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_MediaDirInput = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.HorizontalSpacer_Process_MediaDirInput, 0, 1, 1, 1)

        self.Button_Process_MediaDirInput_Undo = QPushButton(self.Frame_Process_MediaDirInput)
        self.Button_Process_MediaDirInput_Undo.setObjectName(u"Button_Process_MediaDirInput_Undo")
        self.Button_Process_MediaDirInput_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_MediaDirInput_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_MediaDirInput_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_12.addWidget(self.Button_Process_MediaDirInput_Undo, 0, 2, 1, 1)

        self.LineEdit_Process_MediaDirInput = LineEditBase(self.Frame_Process_MediaDirInput)
        self.LineEdit_Process_MediaDirInput.setObjectName(u"LineEdit_Process_MediaDirInput")
        self.LineEdit_Process_MediaDirInput.setMinimumSize(QSize(0, 27))

        self.gridLayout_12.addWidget(self.LineEdit_Process_MediaDirInput, 1, 0, 1, 3)


        self.verticalLayout_20.addWidget(self.Frame_Process_MediaDirInput)


        self.verticalLayout_150.addWidget(self.Frame_Process_InputParams_BasicSettings)


        self.verticalLayout_14.addWidget(self.GroupBox_Process_InputParams)

        self.GroupBox_Process_AudioSlicerParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Process)
        self.GroupBox_Process_AudioSlicerParams.setObjectName(u"GroupBox_Process_AudioSlicerParams")
        self.GroupBox_Process_AudioSlicerParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_186 = QVBoxLayout(self.GroupBox_Process_AudioSlicerParams)
        self.verticalLayout_186.setSpacing(0)
        self.verticalLayout_186.setObjectName(u"verticalLayout_186")
        self.verticalLayout_186.setContentsMargins(0, 12, 0, 12)
        self.Frame_Process_AudioSlicerParams_BasicSettings = QFrame(self.GroupBox_Process_AudioSlicerParams)
        self.Frame_Process_AudioSlicerParams_BasicSettings.setObjectName(u"Frame_Process_AudioSlicerParams_BasicSettings")
        self.verticalLayout_51 = QVBoxLayout(self.Frame_Process_AudioSlicerParams_BasicSettings)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.Frame_Process_SliceAudio = QFrame(self.Frame_Process_AudioSlicerParams_BasicSettings)
        self.Frame_Process_SliceAudio.setObjectName(u"Frame_Process_SliceAudio")
        self.Frame_Process_SliceAudio.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SliceAudio.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_13 = QGridLayout(self.Frame_Process_SliceAudio)
        self.gridLayout_13.setSpacing(12)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_SliceAudio = QLabel(self.Frame_Process_SliceAudio)
        self.Label_Process_SliceAudio.setObjectName(u"Label_Process_SliceAudio")
        sizePolicy5.setHeightForWidth(self.Label_Process_SliceAudio.sizePolicy().hasHeightForWidth())
        self.Label_Process_SliceAudio.setSizePolicy(sizePolicy5)
        self.Label_Process_SliceAudio.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_13.addWidget(self.Label_Process_SliceAudio, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_SliceAudio = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.HorizontalSpacer_Process_SliceAudio, 0, 1, 1, 1)

        self.Button_Process_SliceAudio_Undo = QPushButton(self.Frame_Process_SliceAudio)
        self.Button_Process_SliceAudio_Undo.setObjectName(u"Button_Process_SliceAudio_Undo")
        self.Button_Process_SliceAudio_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_SliceAudio_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_SliceAudio_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_13.addWidget(self.Button_Process_SliceAudio_Undo, 0, 2, 1, 1)

        self.CheckBox_Process_SliceAudio = QCheckBox(self.Frame_Process_SliceAudio)
        self.CheckBox_Process_SliceAudio.setObjectName(u"CheckBox_Process_SliceAudio")
        self.CheckBox_Process_SliceAudio.setMinimumSize(QSize(0, 27))
        self.CheckBox_Process_SliceAudio.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_13.addWidget(self.CheckBox_Process_SliceAudio, 1, 0, 1, 3)


        self.verticalLayout_51.addWidget(self.Frame_Process_SliceAudio)


        self.verticalLayout_186.addWidget(self.Frame_Process_AudioSlicerParams_BasicSettings)

        self.CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings = QCheckBox(self.GroupBox_Process_AudioSlicerParams)
        self.CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings.setObjectName(u"CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings")
        self.CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	font-weight: 630;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding-top: 9px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"    background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: transparent;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/RightCaret.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/DownCaret.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_186.addWidget(self.CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings)

        self.Frame_Process_AudioSlicerParams_AdvanceSettings = QFrame(self.GroupBox_Process_AudioSlicerParams)
        self.Frame_Process_AudioSlicerParams_AdvanceSettings.setObjectName(u"Frame_Process_AudioSlicerParams_AdvanceSettings")
        self.verticalLayout_54 = QVBoxLayout(self.Frame_Process_AudioSlicerParams_AdvanceSettings)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.Frame_Process_RMSThreshold = QFrame(self.Frame_Process_AudioSlicerParams_AdvanceSettings)
        self.Frame_Process_RMSThreshold.setObjectName(u"Frame_Process_RMSThreshold")
        self.Frame_Process_RMSThreshold.setMinimumSize(QSize(0, 105))
        self.Frame_Process_RMSThreshold.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_17 = QGridLayout(self.Frame_Process_RMSThreshold)
        self.gridLayout_17.setSpacing(12)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_RMSThreshold = QLabel(self.Frame_Process_RMSThreshold)
        self.Label_Process_RMSThreshold.setObjectName(u"Label_Process_RMSThreshold")
        sizePolicy5.setHeightForWidth(self.Label_Process_RMSThreshold.sizePolicy().hasHeightForWidth())
        self.Label_Process_RMSThreshold.setSizePolicy(sizePolicy5)
        self.Label_Process_RMSThreshold.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_17.addWidget(self.Label_Process_RMSThreshold, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_RMSThreshold = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.HorizontalSpacer_Process_RMSThreshold, 0, 1, 1, 1)

        self.Button_Process_RMSThreshold_Undo = QPushButton(self.Frame_Process_RMSThreshold)
        self.Button_Process_RMSThreshold_Undo.setObjectName(u"Button_Process_RMSThreshold_Undo")
        self.Button_Process_RMSThreshold_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_RMSThreshold_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_RMSThreshold_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_17.addWidget(self.Button_Process_RMSThreshold_Undo, 0, 2, 1, 1)

        self.DoubleSpinBox_Process_RMSThreshold = QDoubleSpinBox(self.Frame_Process_RMSThreshold)
        self.DoubleSpinBox_Process_RMSThreshold.setObjectName(u"DoubleSpinBox_Process_RMSThreshold")
        self.DoubleSpinBox_Process_RMSThreshold.setEnabled(True)
        self.DoubleSpinBox_Process_RMSThreshold.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_Process_RMSThreshold.setStyleSheet(u"QDoubleSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	/*height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::down-arr"
                        "ow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.DoubleSpinBox_Process_RMSThreshold.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_Process_RMSThreshold.setMaximum(999999.000000000000000)

        self.gridLayout_17.addWidget(self.DoubleSpinBox_Process_RMSThreshold, 1, 0, 1, 3)


        self.verticalLayout_54.addWidget(self.Frame_Process_RMSThreshold)

        self.Frame_Process_AudioLengthMin = QFrame(self.Frame_Process_AudioSlicerParams_AdvanceSettings)
        self.Frame_Process_AudioLengthMin.setObjectName(u"Frame_Process_AudioLengthMin")
        self.Frame_Process_AudioLengthMin.setMinimumSize(QSize(0, 105))
        self.Frame_Process_AudioLengthMin.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_23 = QGridLayout(self.Frame_Process_AudioLengthMin)
        self.gridLayout_23.setSpacing(12)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_AudioLengthMin = QLabel(self.Frame_Process_AudioLengthMin)
        self.Label_Process_AudioLengthMin.setObjectName(u"Label_Process_AudioLengthMin")
        sizePolicy5.setHeightForWidth(self.Label_Process_AudioLengthMin.sizePolicy().hasHeightForWidth())
        self.Label_Process_AudioLengthMin.setSizePolicy(sizePolicy5)
        self.Label_Process_AudioLengthMin.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_23.addWidget(self.Label_Process_AudioLengthMin, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_AudioLengthMin = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.HorizontalSpacer_Process_AudioLengthMin, 0, 1, 1, 1)

        self.Button_Process_AudioLengthMin_Undo = QPushButton(self.Frame_Process_AudioLengthMin)
        self.Button_Process_AudioLengthMin_Undo.setObjectName(u"Button_Process_AudioLengthMin_Undo")
        self.Button_Process_AudioLengthMin_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_AudioLengthMin_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_AudioLengthMin_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_23.addWidget(self.Button_Process_AudioLengthMin_Undo, 0, 2, 1, 1)

        self.SpinBox_Process_AudioLengthMin = QSpinBox(self.Frame_Process_AudioLengthMin)
        self.SpinBox_Process_AudioLengthMin.setObjectName(u"SpinBox_Process_AudioLengthMin")
        self.SpinBox_Process_AudioLengthMin.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_AudioLengthMin.setStyleSheet(u"QSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"	border-image: url(:/(Double)"
                        "SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.SpinBox_Process_AudioLengthMin.setMinimum(-999999)
        self.SpinBox_Process_AudioLengthMin.setMaximum(999999)

        self.gridLayout_23.addWidget(self.SpinBox_Process_AudioLengthMin, 1, 0, 1, 3)


        self.verticalLayout_54.addWidget(self.Frame_Process_AudioLengthMin)

        self.Frame_Process_SilentIntervalMin = QFrame(self.Frame_Process_AudioSlicerParams_AdvanceSettings)
        self.Frame_Process_SilentIntervalMin.setObjectName(u"Frame_Process_SilentIntervalMin")
        self.Frame_Process_SilentIntervalMin.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SilentIntervalMin.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_24 = QGridLayout(self.Frame_Process_SilentIntervalMin)
        self.gridLayout_24.setSpacing(12)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_SilentIntervalMin = QLabel(self.Frame_Process_SilentIntervalMin)
        self.Label_Process_SilentIntervalMin.setObjectName(u"Label_Process_SilentIntervalMin")
        sizePolicy5.setHeightForWidth(self.Label_Process_SilentIntervalMin.sizePolicy().hasHeightForWidth())
        self.Label_Process_SilentIntervalMin.setSizePolicy(sizePolicy5)
        self.Label_Process_SilentIntervalMin.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_24.addWidget(self.Label_Process_SilentIntervalMin, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_SilentIntervalMin = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_24.addItem(self.HorizontalSpacer_Process_SilentIntervalMin, 0, 1, 1, 1)

        self.Button_Process_SilentIntervalMin_Undo = QPushButton(self.Frame_Process_SilentIntervalMin)
        self.Button_Process_SilentIntervalMin_Undo.setObjectName(u"Button_Process_SilentIntervalMin_Undo")
        self.Button_Process_SilentIntervalMin_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_SilentIntervalMin_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_SilentIntervalMin_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_24.addWidget(self.Button_Process_SilentIntervalMin_Undo, 0, 2, 1, 1)

        self.SpinBox_Process_SilentIntervalMin = QSpinBox(self.Frame_Process_SilentIntervalMin)
        self.SpinBox_Process_SilentIntervalMin.setObjectName(u"SpinBox_Process_SilentIntervalMin")
        self.SpinBox_Process_SilentIntervalMin.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_SilentIntervalMin.setStyleSheet(u"QSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"	border-image: url(:/(Double)"
                        "SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.SpinBox_Process_SilentIntervalMin.setMinimum(-999999)
        self.SpinBox_Process_SilentIntervalMin.setMaximum(999999)

        self.gridLayout_24.addWidget(self.SpinBox_Process_SilentIntervalMin, 1, 0, 1, 3)


        self.verticalLayout_54.addWidget(self.Frame_Process_SilentIntervalMin)

        self.Frame_Process_HopSize = QFrame(self.Frame_Process_AudioSlicerParams_AdvanceSettings)
        self.Frame_Process_HopSize.setObjectName(u"Frame_Process_HopSize")
        self.Frame_Process_HopSize.setMinimumSize(QSize(0, 105))
        self.Frame_Process_HopSize.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_25 = QGridLayout(self.Frame_Process_HopSize)
        self.gridLayout_25.setSpacing(12)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_HopSize = QLabel(self.Frame_Process_HopSize)
        self.Label_Process_HopSize.setObjectName(u"Label_Process_HopSize")
        sizePolicy5.setHeightForWidth(self.Label_Process_HopSize.sizePolicy().hasHeightForWidth())
        self.Label_Process_HopSize.setSizePolicy(sizePolicy5)
        self.Label_Process_HopSize.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_25.addWidget(self.Label_Process_HopSize, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_HopSize = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.HorizontalSpacer_Process_HopSize, 0, 1, 1, 1)

        self.Button_Process_HopSize_Undo = QPushButton(self.Frame_Process_HopSize)
        self.Button_Process_HopSize_Undo.setObjectName(u"Button_Process_HopSize_Undo")
        self.Button_Process_HopSize_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_HopSize_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_HopSize_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_25.addWidget(self.Button_Process_HopSize_Undo, 0, 2, 1, 1)

        self.SpinBox_Process_HopSize = QSpinBox(self.Frame_Process_HopSize)
        self.SpinBox_Process_HopSize.setObjectName(u"SpinBox_Process_HopSize")
        self.SpinBox_Process_HopSize.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_HopSize.setStyleSheet(u"QSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"	border-image: url(:/(Double)"
                        "SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.SpinBox_Process_HopSize.setMinimum(-999999)
        self.SpinBox_Process_HopSize.setMaximum(999999)

        self.gridLayout_25.addWidget(self.SpinBox_Process_HopSize, 1, 0, 1, 3)


        self.verticalLayout_54.addWidget(self.Frame_Process_HopSize)

        self.Frame_Process_SilenceKeptMax = QFrame(self.Frame_Process_AudioSlicerParams_AdvanceSettings)
        self.Frame_Process_SilenceKeptMax.setObjectName(u"Frame_Process_SilenceKeptMax")
        self.Frame_Process_SilenceKeptMax.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SilenceKeptMax.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_26 = QGridLayout(self.Frame_Process_SilenceKeptMax)
        self.gridLayout_26.setSpacing(12)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_SilenceKeptMax = QLabel(self.Frame_Process_SilenceKeptMax)
        self.Label_Process_SilenceKeptMax.setObjectName(u"Label_Process_SilenceKeptMax")
        sizePolicy5.setHeightForWidth(self.Label_Process_SilenceKeptMax.sizePolicy().hasHeightForWidth())
        self.Label_Process_SilenceKeptMax.setSizePolicy(sizePolicy5)
        self.Label_Process_SilenceKeptMax.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_26.addWidget(self.Label_Process_SilenceKeptMax, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_SilenceKeptMax = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.HorizontalSpacer_Process_SilenceKeptMax, 0, 1, 1, 1)

        self.Button_Process_SilenceKeptMax_Undo = QPushButton(self.Frame_Process_SilenceKeptMax)
        self.Button_Process_SilenceKeptMax_Undo.setObjectName(u"Button_Process_SilenceKeptMax_Undo")
        self.Button_Process_SilenceKeptMax_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_SilenceKeptMax_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_SilenceKeptMax_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_26.addWidget(self.Button_Process_SilenceKeptMax_Undo, 0, 2, 1, 1)

        self.SpinBox_Process_SilenceKeptMax = QSpinBox(self.Frame_Process_SilenceKeptMax)
        self.SpinBox_Process_SilenceKeptMax.setObjectName(u"SpinBox_Process_SilenceKeptMax")
        self.SpinBox_Process_SilenceKeptMax.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_SilenceKeptMax.setStyleSheet(u"QSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"	border-image: url(:/(Double)"
                        "SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.SpinBox_Process_SilenceKeptMax.setMinimum(-999999)
        self.SpinBox_Process_SilenceKeptMax.setMaximum(999999)

        self.gridLayout_26.addWidget(self.SpinBox_Process_SilenceKeptMax, 1, 0, 1, 3)


        self.verticalLayout_54.addWidget(self.Frame_Process_SilenceKeptMax)


        self.verticalLayout_186.addWidget(self.Frame_Process_AudioSlicerParams_AdvanceSettings)


        self.verticalLayout_14.addWidget(self.GroupBox_Process_AudioSlicerParams)

        self.GroupBox_Process_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Process)
        self.GroupBox_Process_OutputParams.setObjectName(u"GroupBox_Process_OutputParams")
        self.GroupBox_Process_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_197 = QVBoxLayout(self.GroupBox_Process_OutputParams)
        self.verticalLayout_197.setSpacing(0)
        self.verticalLayout_197.setObjectName(u"verticalLayout_197")
        self.verticalLayout_197.setContentsMargins(0, 12, 0, 12)
        self.Frame_Process_OutputParams_BasicSettings = QFrame(self.GroupBox_Process_OutputParams)
        self.Frame_Process_OutputParams_BasicSettings.setObjectName(u"Frame_Process_OutputParams_BasicSettings")
        self.verticalLayout_61 = QVBoxLayout(self.Frame_Process_OutputParams_BasicSettings)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.Frame_Process_MediaFormatOutput = QFrame(self.Frame_Process_OutputParams_BasicSettings)
        self.Frame_Process_MediaFormatOutput.setObjectName(u"Frame_Process_MediaFormatOutput")
        self.Frame_Process_MediaFormatOutput.setMinimumSize(QSize(0, 105))
        self.Frame_Process_MediaFormatOutput.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_27 = QGridLayout(self.Frame_Process_MediaFormatOutput)
        self.gridLayout_27.setSpacing(12)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_MediaFormatOutput = QLabel(self.Frame_Process_MediaFormatOutput)
        self.Label_Process_MediaFormatOutput.setObjectName(u"Label_Process_MediaFormatOutput")
        sizePolicy5.setHeightForWidth(self.Label_Process_MediaFormatOutput.sizePolicy().hasHeightForWidth())
        self.Label_Process_MediaFormatOutput.setSizePolicy(sizePolicy5)
        self.Label_Process_MediaFormatOutput.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_27.addWidget(self.Label_Process_MediaFormatOutput, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_MediaFormatOutput = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.HorizontalSpacer_Process_MediaFormatOutput, 0, 1, 1, 1)

        self.Button_Process_MediaFormatOutput_Undo = QPushButton(self.Frame_Process_MediaFormatOutput)
        self.Button_Process_MediaFormatOutput_Undo.setObjectName(u"Button_Process_MediaFormatOutput_Undo")
        self.Button_Process_MediaFormatOutput_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_MediaFormatOutput_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_MediaFormatOutput_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_27.addWidget(self.Button_Process_MediaFormatOutput_Undo, 0, 2, 1, 1)

        self.ComboBox_Process_MediaFormatOutput = QComboBox(self.Frame_Process_MediaFormatOutput)
        self.ComboBox_Process_MediaFormatOutput.setObjectName(u"ComboBox_Process_MediaFormatOutput")
        self.ComboBox_Process_MediaFormatOutput.setMinimumSize(QSize(0, 27))
        self.ComboBox_Process_MediaFormatOutput.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QComboBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	/*width: 12px;\n"
"	height: 12px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	margin-right: 6px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"	border-image: url(:/ComboBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"\n"
"QCom"
                        "boBox QAbstractItemView::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
""
                        "	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:vertical, QComboBox QAbstractScrollArea QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	borde"
                        "r-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:horizontal, QComboBox QAbstractScrollArea QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	"
                        "border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_27.addWidget(self.ComboBox_Process_MediaFormatOutput, 1, 0, 1, 3)


        self.verticalLayout_61.addWidget(self.Frame_Process_MediaFormatOutput)

        self.Frame_Process_MediaDirOutput = QFrame(self.Frame_Process_OutputParams_BasicSettings)
        self.Frame_Process_MediaDirOutput.setObjectName(u"Frame_Process_MediaDirOutput")
        self.Frame_Process_MediaDirOutput.setMinimumSize(QSize(0, 105))
        self.Frame_Process_MediaDirOutput.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_28 = QGridLayout(self.Frame_Process_MediaDirOutput)
        self.gridLayout_28.setSpacing(12)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_MediaDirOutput = QLabel(self.Frame_Process_MediaDirOutput)
        self.Label_Process_MediaDirOutput.setObjectName(u"Label_Process_MediaDirOutput")
        sizePolicy5.setHeightForWidth(self.Label_Process_MediaDirOutput.sizePolicy().hasHeightForWidth())
        self.Label_Process_MediaDirOutput.setSizePolicy(sizePolicy5)
        self.Label_Process_MediaDirOutput.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_28.addWidget(self.Label_Process_MediaDirOutput, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_MediaDirOutput = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.HorizontalSpacer_Process_MediaDirOutput, 0, 1, 1, 1)

        self.Button_Process_MediaDirOutput_Undo = QPushButton(self.Frame_Process_MediaDirOutput)
        self.Button_Process_MediaDirOutput_Undo.setObjectName(u"Button_Process_MediaDirOutput_Undo")
        self.Button_Process_MediaDirOutput_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_MediaDirOutput_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_MediaDirOutput_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_28.addWidget(self.Button_Process_MediaDirOutput_Undo, 0, 2, 1, 1)

        self.LineEdit_Process_MediaDirOutput = LineEditBase(self.Frame_Process_MediaDirOutput)
        self.LineEdit_Process_MediaDirOutput.setObjectName(u"LineEdit_Process_MediaDirOutput")
        self.LineEdit_Process_MediaDirOutput.setMinimumSize(QSize(0, 27))

        self.gridLayout_28.addWidget(self.LineEdit_Process_MediaDirOutput, 1, 0, 1, 3)


        self.verticalLayout_61.addWidget(self.Frame_Process_MediaDirOutput)


        self.verticalLayout_197.addWidget(self.Frame_Process_OutputParams_BasicSettings)

        self.CheckBox_Process_OutputParams_Toggle_AdvanceSettings = QCheckBox(self.GroupBox_Process_OutputParams)
        self.CheckBox_Process_OutputParams_Toggle_AdvanceSettings.setObjectName(u"CheckBox_Process_OutputParams_Toggle_AdvanceSettings")
        self.CheckBox_Process_OutputParams_Toggle_AdvanceSettings.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	font-weight: 630;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding-top: 9px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"    background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: transparent;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/RightCaret.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/DownCaret.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_197.addWidget(self.CheckBox_Process_OutputParams_Toggle_AdvanceSettings)

        self.Frame_Process_OutputParams_AdvanceSettings = QFrame(self.GroupBox_Process_OutputParams)
        self.Frame_Process_OutputParams_AdvanceSettings.setObjectName(u"Frame_Process_OutputParams_AdvanceSettings")
        self.verticalLayout_67 = QVBoxLayout(self.Frame_Process_OutputParams_AdvanceSettings)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.Frame_Process_SampleRate = QFrame(self.Frame_Process_OutputParams_AdvanceSettings)
        self.Frame_Process_SampleRate.setObjectName(u"Frame_Process_SampleRate")
        self.Frame_Process_SampleRate.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SampleRate.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_29 = QGridLayout(self.Frame_Process_SampleRate)
        self.gridLayout_29.setSpacing(12)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_SampleRate = QLabel(self.Frame_Process_SampleRate)
        self.Label_Process_SampleRate.setObjectName(u"Label_Process_SampleRate")
        sizePolicy5.setHeightForWidth(self.Label_Process_SampleRate.sizePolicy().hasHeightForWidth())
        self.Label_Process_SampleRate.setSizePolicy(sizePolicy5)
        self.Label_Process_SampleRate.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_29.addWidget(self.Label_Process_SampleRate, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_SampleRate = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.HorizontalSpacer_Process_SampleRate, 0, 1, 1, 1)

        self.Button_Process_SampleRate_Undo = QPushButton(self.Frame_Process_SampleRate)
        self.Button_Process_SampleRate_Undo.setObjectName(u"Button_Process_SampleRate_Undo")
        self.Button_Process_SampleRate_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_SampleRate_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_SampleRate_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_29.addWidget(self.Button_Process_SampleRate_Undo, 0, 2, 1, 1)

        self.ComboBox_Process_SampleRate = QComboBox(self.Frame_Process_SampleRate)
        self.ComboBox_Process_SampleRate.setObjectName(u"ComboBox_Process_SampleRate")
        self.ComboBox_Process_SampleRate.setMinimumSize(QSize(0, 27))
        self.ComboBox_Process_SampleRate.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QComboBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	/*width: 12px;\n"
"	height: 12px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	margin-right: 6px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"	border-image: url(:/ComboBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"\n"
"QCom"
                        "boBox QAbstractItemView::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
""
                        "	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:vertical, QComboBox QAbstractScrollArea QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	borde"
                        "r-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:horizontal, QComboBox QAbstractScrollArea QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	"
                        "border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_29.addWidget(self.ComboBox_Process_SampleRate, 1, 0, 1, 3)


        self.verticalLayout_67.addWidget(self.Frame_Process_SampleRate)

        self.Frame_Process_SampleWidth = QFrame(self.Frame_Process_OutputParams_AdvanceSettings)
        self.Frame_Process_SampleWidth.setObjectName(u"Frame_Process_SampleWidth")
        self.Frame_Process_SampleWidth.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SampleWidth.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_30 = QGridLayout(self.Frame_Process_SampleWidth)
        self.gridLayout_30.setSpacing(12)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_SampleWidth = QLabel(self.Frame_Process_SampleWidth)
        self.Label_Process_SampleWidth.setObjectName(u"Label_Process_SampleWidth")
        sizePolicy5.setHeightForWidth(self.Label_Process_SampleWidth.sizePolicy().hasHeightForWidth())
        self.Label_Process_SampleWidth.setSizePolicy(sizePolicy5)
        self.Label_Process_SampleWidth.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_30.addWidget(self.Label_Process_SampleWidth, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_SampleWidth = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.HorizontalSpacer_Process_SampleWidth, 0, 1, 1, 1)

        self.Button_Process_SampleWidth_Undo = QPushButton(self.Frame_Process_SampleWidth)
        self.Button_Process_SampleWidth_Undo.setObjectName(u"Button_Process_SampleWidth_Undo")
        self.Button_Process_SampleWidth_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_SampleWidth_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_SampleWidth_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_30.addWidget(self.Button_Process_SampleWidth_Undo, 0, 2, 1, 1)

        self.ComboBox_Process_SampleWidth = QComboBox(self.Frame_Process_SampleWidth)
        self.ComboBox_Process_SampleWidth.setObjectName(u"ComboBox_Process_SampleWidth")
        self.ComboBox_Process_SampleWidth.setMinimumSize(QSize(0, 27))
        self.ComboBox_Process_SampleWidth.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QComboBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	/*width: 12px;\n"
"	height: 12px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	margin-right: 6px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"	border-image: url(:/ComboBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"\n"
"QCom"
                        "boBox QAbstractItemView::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
""
                        "	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:vertical, QComboBox QAbstractScrollArea QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	borde"
                        "r-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:horizontal, QComboBox QAbstractScrollArea QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	"
                        "border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_30.addWidget(self.ComboBox_Process_SampleWidth, 1, 0, 1, 3)


        self.verticalLayout_67.addWidget(self.Frame_Process_SampleWidth)

        self.Frame_Process_ToMono = QFrame(self.Frame_Process_OutputParams_AdvanceSettings)
        self.Frame_Process_ToMono.setObjectName(u"Frame_Process_ToMono")
        self.Frame_Process_ToMono.setMinimumSize(QSize(0, 105))
        self.Frame_Process_ToMono.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_31 = QGridLayout(self.Frame_Process_ToMono)
        self.gridLayout_31.setSpacing(12)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_ToMono = QLabel(self.Frame_Process_ToMono)
        self.Label_Process_ToMono.setObjectName(u"Label_Process_ToMono")
        sizePolicy5.setHeightForWidth(self.Label_Process_ToMono.sizePolicy().hasHeightForWidth())
        self.Label_Process_ToMono.setSizePolicy(sizePolicy5)
        self.Label_Process_ToMono.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_31.addWidget(self.Label_Process_ToMono, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_ToMono = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.HorizontalSpacer_Process_ToMono, 0, 1, 1, 1)

        self.Button_Process_ToMono_Undo = QPushButton(self.Frame_Process_ToMono)
        self.Button_Process_ToMono_Undo.setObjectName(u"Button_Process_ToMono_Undo")
        self.Button_Process_ToMono_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Process_ToMono_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Process_ToMono_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_31.addWidget(self.Button_Process_ToMono_Undo, 0, 2, 1, 1)

        self.CheckBox_Process_ToMono = QCheckBox(self.Frame_Process_ToMono)
        self.CheckBox_Process_ToMono.setObjectName(u"CheckBox_Process_ToMono")
        self.CheckBox_Process_ToMono.setMinimumSize(QSize(0, 27))
        self.CheckBox_Process_ToMono.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_31.addWidget(self.CheckBox_Process_ToMono, 1, 0, 1, 3)


        self.verticalLayout_67.addWidget(self.Frame_Process_ToMono)


        self.verticalLayout_197.addWidget(self.Frame_Process_OutputParams_AdvanceSettings)


        self.verticalLayout_14.addWidget(self.GroupBox_Process_OutputParams)

        self.VerticalSpacer_Process = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.VerticalSpacer_Process)

        self.ScrollArea_Middle_Process.setWidget(self.ScrollArea_Middle_WidgetContents_Process)

        self.gridLayout_6.addWidget(self.ScrollArea_Middle_Process, 0, 1, 1, 1)

        self.Widget_Right_Process = QWidget(self.Subpage_Process)
        self.Widget_Right_Process.setObjectName(u"Widget_Right_Process")
        self.Widget_Right_Process.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout_9 = QGridLayout(self.Widget_Right_Process)
        self.gridLayout_9.setSpacing(12)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Process = QTextBrowser(self.Widget_Right_Process)
        self.TextBrowser_Params_Process.setObjectName(u"TextBrowser_Params_Process")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Process.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Process.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Process.setStyleSheet(u"QTextBrowser {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	bord"
                        "er-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px"
                        ";\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_9.addWidget(self.TextBrowser_Params_Process, 0, 0, 1, 1)

        self.Button_CheckOutput_Process = QPushButton(self.Widget_Right_Process)
        self.Button_CheckOutput_Process.setObjectName(u"Button_CheckOutput_Process")
        self.Button_CheckOutput_Process.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 9.9px;\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_9.addWidget(self.Button_CheckOutput_Process, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.Widget_Right_Process, 0, 2, 1, 1)

        self.ProgressBar_Process = QProgressBar(self.Subpage_Process)
        self.ProgressBar_Process.setObjectName(u"ProgressBar_Process")
        self.ProgressBar_Process.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Process.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(60, 60, 60);\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(60, 60, 60), stop:1  rgb(123, 123, 123));\n"
"}")
        self.ProgressBar_Process.setValue(0)
        self.ProgressBar_Process.setTextVisible(False)
        self.verticalLayout_24 = QVBoxLayout(self.ProgressBar_Process)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Process = QStackedWidget(self.ProgressBar_Process)
        self.StackedWidget_Process.setObjectName(u"StackedWidget_Process")
        self.StackedWidget_Process.setMinimumSize(QSize(0, 30))
        self.StackedWidget_Process.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_Process.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_Process_Execute = QWidget()
        self.Page_Process_Execute.setObjectName(u"Page_Process_Execute")
        self.verticalLayout_86 = QVBoxLayout(self.Page_Process_Execute)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.Button_Process_Execute = QPushButton(self.Page_Process_Execute)
        self.Button_Process_Execute.setObjectName(u"Button_Process_Execute")
        sizePolicy3.setHeightForWidth(self.Button_Process_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Process_Execute.setSizePolicy(sizePolicy3)
        self.Button_Process_Execute.setMinimumSize(QSize(0, 30))
        self.Button_Process_Execute.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_86.addWidget(self.Button_Process_Execute)

        self.StackedWidget_Process.addWidget(self.Page_Process_Execute)
        self.Page_Process_Terminate = QWidget()
        self.Page_Process_Terminate.setObjectName(u"Page_Process_Terminate")
        self.verticalLayout_87 = QVBoxLayout(self.Page_Process_Terminate)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.Button_Process_Terminate = QPushButton(self.Page_Process_Terminate)
        self.Button_Process_Terminate.setObjectName(u"Button_Process_Terminate")
        sizePolicy3.setHeightForWidth(self.Button_Process_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Process_Terminate.setSizePolicy(sizePolicy3)
        self.Button_Process_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_Process_Terminate.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 6px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_87.addWidget(self.Button_Process_Terminate)

        self.StackedWidget_Process.addWidget(self.Page_Process_Terminate)

        self.verticalLayout_24.addWidget(self.StackedWidget_Process)


        self.gridLayout_6.addWidget(self.ProgressBar_Process, 1, 0, 1, 3)

        self.gridLayout_6.setColumnStretch(0, 3)
        self.gridLayout_6.setColumnStretch(1, 10)
        self.gridLayout_6.setColumnStretch(2, 7)
        self.StackedWidget_Pages_Process.addWidget(self.Subpage_Process)

        self.verticalLayout_40.addWidget(self.StackedWidget_Pages_Process)

        self.StackedWidget_Pages.addWidget(self.Page_Process)
        self.Page_ASR = QWidget()
        self.Page_ASR.setObjectName(u"Page_ASR")
        self.verticalLayout_44 = QVBoxLayout(self.Page_ASR)
        self.verticalLayout_44.setSpacing(21)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(21, 12, 21, 12)
        self.Frame_ASR_Top = QFrame(self.Page_ASR)
        self.Frame_ASR_Top.setObjectName(u"Frame_ASR_Top")
        self.Frame_ASR_Top.setMinimumSize(QSize(0, 60))
        self.Frame_ASR_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_69 = QHBoxLayout(self.Frame_ASR_Top)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_VoiceIdentifier_Title = QToolButton(self.Frame_ASR_Top)
        self.ToolButton_VoiceIdentifier_Title.setObjectName(u"ToolButton_VoiceIdentifier_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_VoiceIdentifier_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_VoiceIdentifier_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_VoiceIdentifier_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color:"
                        " rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_69.addWidget(self.ToolButton_VoiceIdentifier_Title)

        self.Frame_ASR_Title_Spacer = QLabel(self.Frame_ASR_Top)
        self.Frame_ASR_Title_Spacer.setObjectName(u"Frame_ASR_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_ASR_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_ASR_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_ASR_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;*/\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_69.addWidget(self.Frame_ASR_Title_Spacer)


        self.verticalLayout_44.addWidget(self.Frame_ASR_Top)

        self.StackedWidget_Pages_ASR = QStackedWidget(self.Page_ASR)
        self.StackedWidget_Pages_ASR.setObjectName(u"StackedWidget_Pages_ASR")
        self.StackedWidget_Pages_ASR.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*\n"
"QTabWidget {\n"
"	background-color: transparent;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"}\n"
"QTabWidget::pane {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"	font-size: 18px;\n"
"	font-weight: 420;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 12px;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:selected {\n"
"	color: rgba(255, 255, 255, 255);\n"
"}\n"
"QTabBar::tab:hover:!selected {\n"
"}\n"
"\n"
"\n"
"QTabBar QToolButton {\n"
"}\n"
"QTabBar QToolButton:hover {\n"
"}\n"
"*/")
        self.Subpage_ASR_VPR = QWidget()
        self.Subpage_ASR_VPR.setObjectName(u"Subpage_ASR_VPR")
        self.gridLayout_21 = QGridLayout(self.Subpage_ASR_VPR)
        self.gridLayout_21.setSpacing(12)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_ASR_VPR = QWidget(self.Subpage_ASR_VPR)
        self.Widget_Left_ASR_VPR.setObjectName(u"Widget_Left_ASR_VPR")
        self.Widget_Left_ASR_VPR.setMinimumSize(QSize(150, 0))
        self.Widget_Left_ASR_VPR.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.Widget_Left_ASR_VPR)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_ASR_VPR = QTreeWidget(self.Widget_Left_ASR_VPR)
        __qtreewidgetitem1 = QTreeWidgetItem(self.TreeWidget_Catalogue_ASR_VPR)
        QTreeWidgetItem(__qtreewidgetitem1)
        self.TreeWidget_Catalogue_ASR_VPR.setObjectName(u"TreeWidget_Catalogue_ASR_VPR")
        self.TreeWidget_Catalogue_ASR_VPR.setStyleSheet(u"QTreeView {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"	background-color: transparent;\n"
"	padding: 2.4px;\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"QTreeView::item:selected {\n"
"    background-color: ;\n"
"}\n"
"\n"
"QTreeView::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeView::branch:open:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeView::branch:closed:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:adjoins-item {\n"
"    background-color: ;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: rgba(45, 45, 45, 135);\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"	background-color: r"
                        "gba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(90, 90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}")

        self.verticalLayout_4.addWidget(self.TreeWidget_Catalogue_ASR_VPR)


        self.gridLayout_21.addWidget(self.Widget_Left_ASR_VPR, 0, 0, 1, 1)

        self.ScrollArea_Middle_ASR_VPR = QScrollArea(self.Subpage_ASR_VPR)
        self.ScrollArea_Middle_ASR_VPR.setObjectName(u"ScrollArea_Middle_ASR_VPR")
        self.ScrollArea_Middle_ASR_VPR.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_ASR_VPR.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollArea:hover {\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	"
                        "height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	borde"
                        "r-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")
        self.ScrollArea_Middle_ASR_VPR.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_ASR_VPR.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_ASR_VPR = QWidget()
        self.ScrollArea_Middle_WidgetContents_ASR_VPR.setObjectName(u"ScrollArea_Middle_WidgetContents_ASR_VPR")
        self.ScrollArea_Middle_WidgetContents_ASR_VPR.setGeometry(QRect(0, 0, 591, 1144))
        self.verticalLayout_7 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_ASR_VPR)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_ASR_VPR_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_ASR_VPR)
        self.GroupBox_ASR_VPR_InputParams.setObjectName(u"GroupBox_ASR_VPR_InputParams")
        self.GroupBox_ASR_VPR_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_33 = QVBoxLayout(self.GroupBox_ASR_VPR_InputParams)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 12, 0, 12)
        self.Frame_ASR_VPR_InputParams_BasicSettings = QFrame(self.GroupBox_ASR_VPR_InputParams)
        self.Frame_ASR_VPR_InputParams_BasicSettings.setObjectName(u"Frame_ASR_VPR_InputParams_BasicSettings")
        self.verticalLayout_137 = QVBoxLayout(self.Frame_ASR_VPR_InputParams_BasicSettings)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_VPR_AudioDirInput = QFrame(self.Frame_ASR_VPR_InputParams_BasicSettings)
        self.Frame_ASR_VPR_AudioDirInput.setObjectName(u"Frame_ASR_VPR_AudioDirInput")
        self.Frame_ASR_VPR_AudioDirInput.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_AudioDirInput.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_32 = QGridLayout(self.Frame_ASR_VPR_AudioDirInput)
        self.gridLayout_32.setSpacing(12)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_AudioDirInput = QLabel(self.Frame_ASR_VPR_AudioDirInput)
        self.Label_ASR_VPR_AudioDirInput.setObjectName(u"Label_ASR_VPR_AudioDirInput")
        sizePolicy5.setHeightForWidth(self.Label_ASR_VPR_AudioDirInput.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_AudioDirInput.setSizePolicy(sizePolicy5)
        self.Label_ASR_VPR_AudioDirInput.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_32.addWidget(self.Label_ASR_VPR_AudioDirInput, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_AudioDirInput = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.HorizontalSpacer_ASR_VPR_AudioDirInput, 0, 1, 1, 1)

        self.Button_ASR_VPR_AudioDirInput_Undo = QPushButton(self.Frame_ASR_VPR_AudioDirInput)
        self.Button_ASR_VPR_AudioDirInput_Undo.setObjectName(u"Button_ASR_VPR_AudioDirInput_Undo")
        self.Button_ASR_VPR_AudioDirInput_Undo.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_AudioDirInput_Undo.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_AudioDirInput_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_32.addWidget(self.Button_ASR_VPR_AudioDirInput_Undo, 0, 2, 1, 1)

        self.LineEdit_ASR_VPR_AudioDirInput = LineEditBase(self.Frame_ASR_VPR_AudioDirInput)
        self.LineEdit_ASR_VPR_AudioDirInput.setObjectName(u"LineEdit_ASR_VPR_AudioDirInput")
        self.LineEdit_ASR_VPR_AudioDirInput.setMinimumSize(QSize(0, 27))

        self.gridLayout_32.addWidget(self.LineEdit_ASR_VPR_AudioDirInput, 1, 0, 1, 3)


        self.verticalLayout_137.addWidget(self.Frame_ASR_VPR_AudioDirInput)

        self.Frame_ASR_VPR_StdAudioSpeaker = QFrame(self.Frame_ASR_VPR_InputParams_BasicSettings)
        self.Frame_ASR_VPR_StdAudioSpeaker.setObjectName(u"Frame_ASR_VPR_StdAudioSpeaker")
        self.Frame_ASR_VPR_StdAudioSpeaker.setMinimumSize(QSize(0, 222))
        self.Frame_ASR_VPR_StdAudioSpeaker.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.Frame_ASR_VPR_StdAudioSpeaker)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_StdAudioSpeaker = QLabel(self.Frame_ASR_VPR_StdAudioSpeaker)
        self.Label_ASR_VPR_StdAudioSpeaker.setObjectName(u"Label_ASR_VPR_StdAudioSpeaker")
        sizePolicy5.setHeightForWidth(self.Label_ASR_VPR_StdAudioSpeaker.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_StdAudioSpeaker.setSizePolicy(sizePolicy5)
        self.Label_ASR_VPR_StdAudioSpeaker.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_12.addWidget(self.Label_ASR_VPR_StdAudioSpeaker)

        self.Table_ASR_VPR_StdAudioSpeaker = Table_EditAudioSpeaker(self.Frame_ASR_VPR_StdAudioSpeaker)
        self.Table_ASR_VPR_StdAudioSpeaker.setObjectName(u"Table_ASR_VPR_StdAudioSpeaker")

        self.verticalLayout_12.addWidget(self.Table_ASR_VPR_StdAudioSpeaker)


        self.verticalLayout_137.addWidget(self.Frame_ASR_VPR_StdAudioSpeaker)


        self.verticalLayout_33.addWidget(self.Frame_ASR_VPR_InputParams_BasicSettings)


        self.verticalLayout_7.addWidget(self.GroupBox_ASR_VPR_InputParams)

        self.GroupBox_ASR_VPR_VPRParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_ASR_VPR)
        self.GroupBox_ASR_VPR_VPRParams.setObjectName(u"GroupBox_ASR_VPR_VPRParams")
        self.GroupBox_ASR_VPR_VPRParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_47 = QVBoxLayout(self.GroupBox_ASR_VPR_VPRParams)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 12, 0, 12)
        self.Frame_ASR_VPR_VPRParams_BasicSettings = QFrame(self.GroupBox_ASR_VPR_VPRParams)
        self.Frame_ASR_VPR_VPRParams_BasicSettings.setObjectName(u"Frame_ASR_VPR_VPRParams_BasicSettings")
        self.verticalLayout_45 = QVBoxLayout(self.Frame_ASR_VPR_VPRParams_BasicSettings)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_VPR_DecisionThreshold = QFrame(self.Frame_ASR_VPR_VPRParams_BasicSettings)
        self.Frame_ASR_VPR_DecisionThreshold.setObjectName(u"Frame_ASR_VPR_DecisionThreshold")
        self.Frame_ASR_VPR_DecisionThreshold.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_DecisionThreshold.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_33 = QGridLayout(self.Frame_ASR_VPR_DecisionThreshold)
        self.gridLayout_33.setSpacing(12)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_DecisionThreshold = QLabel(self.Frame_ASR_VPR_DecisionThreshold)
        self.Label_ASR_VPR_DecisionThreshold.setObjectName(u"Label_ASR_VPR_DecisionThreshold")
        sizePolicy5.setHeightForWidth(self.Label_ASR_VPR_DecisionThreshold.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_DecisionThreshold.setSizePolicy(sizePolicy5)
        self.Label_ASR_VPR_DecisionThreshold.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_33.addWidget(self.Label_ASR_VPR_DecisionThreshold, 0, 0, 1, 1)

        self.DoubleSpinBox_ASR_VPR_DecisionThreshold = QDoubleSpinBox(self.Frame_ASR_VPR_DecisionThreshold)
        self.DoubleSpinBox_ASR_VPR_DecisionThreshold.setObjectName(u"DoubleSpinBox_ASR_VPR_DecisionThreshold")
        self.DoubleSpinBox_ASR_VPR_DecisionThreshold.setEnabled(True)
        self.DoubleSpinBox_ASR_VPR_DecisionThreshold.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_ASR_VPR_DecisionThreshold.setStyleSheet(u"QDoubleSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	/*height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::down-arr"
                        "ow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.DoubleSpinBox_ASR_VPR_DecisionThreshold.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_ASR_VPR_DecisionThreshold.setMaximum(999999.000000000000000)

        self.gridLayout_33.addWidget(self.DoubleSpinBox_ASR_VPR_DecisionThreshold, 1, 0, 1, 3)

        self.Button_ASR_VPR_DecisionThreshold_Undo = QPushButton(self.Frame_ASR_VPR_DecisionThreshold)
        self.Button_ASR_VPR_DecisionThreshold_Undo.setObjectName(u"Button_ASR_VPR_DecisionThreshold_Undo")
        self.Button_ASR_VPR_DecisionThreshold_Undo.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_DecisionThreshold_Undo.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_DecisionThreshold_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_33.addWidget(self.Button_ASR_VPR_DecisionThreshold_Undo, 0, 2, 1, 1)

        self.HorizontalSpacer_ASR_VPR_DecisionThreshold = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_33.addItem(self.HorizontalSpacer_ASR_VPR_DecisionThreshold, 0, 1, 1, 1)


        self.verticalLayout_45.addWidget(self.Frame_ASR_VPR_DecisionThreshold)

        self.Frame_ASR_VPR_ModelPath = QFrame(self.Frame_ASR_VPR_VPRParams_BasicSettings)
        self.Frame_ASR_VPR_ModelPath.setObjectName(u"Frame_ASR_VPR_ModelPath")
        self.Frame_ASR_VPR_ModelPath.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_ModelPath.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_34 = QGridLayout(self.Frame_ASR_VPR_ModelPath)
        self.gridLayout_34.setSpacing(12)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_ModelPath = QLabel(self.Frame_ASR_VPR_ModelPath)
        self.Label_ASR_VPR_ModelPath.setObjectName(u"Label_ASR_VPR_ModelPath")
        sizePolicy5.setHeightForWidth(self.Label_ASR_VPR_ModelPath.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_ModelPath.setSizePolicy(sizePolicy5)
        self.Label_ASR_VPR_ModelPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_34.addWidget(self.Label_ASR_VPR_ModelPath, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_ModelPath = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_34.addItem(self.HorizontalSpacer_ASR_VPR_ModelPath, 0, 1, 1, 1)

        self.Button_ASR_VPR_ModelPath_Undo = QPushButton(self.Frame_ASR_VPR_ModelPath)
        self.Button_ASR_VPR_ModelPath_Undo.setObjectName(u"Button_ASR_VPR_ModelPath_Undo")
        self.Button_ASR_VPR_ModelPath_Undo.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_ModelPath_Undo.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_ModelPath_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_34.addWidget(self.Button_ASR_VPR_ModelPath_Undo, 0, 2, 1, 1)

        self.LineEdit_ASR_VPR_ModelPath = LineEditBase(self.Frame_ASR_VPR_ModelPath)
        self.LineEdit_ASR_VPR_ModelPath.setObjectName(u"LineEdit_ASR_VPR_ModelPath")
        self.LineEdit_ASR_VPR_ModelPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_34.addWidget(self.LineEdit_ASR_VPR_ModelPath, 1, 0, 1, 3)


        self.verticalLayout_45.addWidget(self.Frame_ASR_VPR_ModelPath)


        self.verticalLayout_47.addWidget(self.Frame_ASR_VPR_VPRParams_BasicSettings)

        self.CheckBox_ASR_VPR_VPRParams_Toggle_AdvanceSettings = QCheckBox(self.GroupBox_ASR_VPR_VPRParams)
        self.CheckBox_ASR_VPR_VPRParams_Toggle_AdvanceSettings.setObjectName(u"CheckBox_ASR_VPR_VPRParams_Toggle_AdvanceSettings")
        self.CheckBox_ASR_VPR_VPRParams_Toggle_AdvanceSettings.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	font-weight: 630;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding-top: 9px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"    background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: transparent;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/RightCaret.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/DownCaret.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_47.addWidget(self.CheckBox_ASR_VPR_VPRParams_Toggle_AdvanceSettings)

        self.Frame_ASR_VPR_VPRParams_AdvanceSettings = QFrame(self.GroupBox_ASR_VPR_VPRParams)
        self.Frame_ASR_VPR_VPRParams_AdvanceSettings.setObjectName(u"Frame_ASR_VPR_VPRParams_AdvanceSettings")
        self.verticalLayout_21 = QVBoxLayout(self.Frame_ASR_VPR_VPRParams_AdvanceSettings)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_VPR_ModelType = QFrame(self.Frame_ASR_VPR_VPRParams_AdvanceSettings)
        self.Frame_ASR_VPR_ModelType.setObjectName(u"Frame_ASR_VPR_ModelType")
        self.Frame_ASR_VPR_ModelType.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_ModelType.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_35 = QGridLayout(self.Frame_ASR_VPR_ModelType)
        self.gridLayout_35.setSpacing(12)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_ModelType = QLabel(self.Frame_ASR_VPR_ModelType)
        self.Label_ASR_VPR_ModelType.setObjectName(u"Label_ASR_VPR_ModelType")
        sizePolicy5.setHeightForWidth(self.Label_ASR_VPR_ModelType.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_ModelType.setSizePolicy(sizePolicy5)
        self.Label_ASR_VPR_ModelType.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_35.addWidget(self.Label_ASR_VPR_ModelType, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_ModelType = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_35.addItem(self.HorizontalSpacer_ASR_VPR_ModelType, 0, 1, 1, 1)

        self.Button_ASR_VPR_ModelType_Undo = QPushButton(self.Frame_ASR_VPR_ModelType)
        self.Button_ASR_VPR_ModelType_Undo.setObjectName(u"Button_ASR_VPR_ModelType_Undo")
        self.Button_ASR_VPR_ModelType_Undo.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_ModelType_Undo.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_ModelType_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_35.addWidget(self.Button_ASR_VPR_ModelType_Undo, 0, 2, 1, 1)

        self.ComboBox_ASR_VPR_ModelType = QComboBox(self.Frame_ASR_VPR_ModelType)
        self.ComboBox_ASR_VPR_ModelType.setObjectName(u"ComboBox_ASR_VPR_ModelType")
        self.ComboBox_ASR_VPR_ModelType.setMinimumSize(QSize(0, 27))
        self.ComboBox_ASR_VPR_ModelType.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QComboBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	/*width: 12px;\n"
"	height: 12px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	margin-right: 6px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"	border-image: url(:/ComboBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"\n"
"QCom"
                        "boBox QAbstractItemView::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
""
                        "	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:vertical, QComboBox QAbstractScrollArea QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	borde"
                        "r-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:horizontal, QComboBox QAbstractScrollArea QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	"
                        "border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_35.addWidget(self.ComboBox_ASR_VPR_ModelType, 1, 0, 1, 3)


        self.verticalLayout_21.addWidget(self.Frame_ASR_VPR_ModelType)

        self.Frame_ASR_VPR_FeatureMethod = QFrame(self.Frame_ASR_VPR_VPRParams_AdvanceSettings)
        self.Frame_ASR_VPR_FeatureMethod.setObjectName(u"Frame_ASR_VPR_FeatureMethod")
        self.Frame_ASR_VPR_FeatureMethod.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_FeatureMethod.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_36 = QGridLayout(self.Frame_ASR_VPR_FeatureMethod)
        self.gridLayout_36.setSpacing(12)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_FeatureMethod = QLabel(self.Frame_ASR_VPR_FeatureMethod)
        self.Label_ASR_VPR_FeatureMethod.setObjectName(u"Label_ASR_VPR_FeatureMethod")
        sizePolicy5.setHeightForWidth(self.Label_ASR_VPR_FeatureMethod.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_FeatureMethod.setSizePolicy(sizePolicy5)
        self.Label_ASR_VPR_FeatureMethod.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_36.addWidget(self.Label_ASR_VPR_FeatureMethod, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_FeatureMethod = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_36.addItem(self.HorizontalSpacer_ASR_VPR_FeatureMethod, 0, 1, 1, 1)

        self.Button_ASR_VPR_FeatureMethod_Undo = QPushButton(self.Frame_ASR_VPR_FeatureMethod)
        self.Button_ASR_VPR_FeatureMethod_Undo.setObjectName(u"Button_ASR_VPR_FeatureMethod_Undo")
        self.Button_ASR_VPR_FeatureMethod_Undo.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_FeatureMethod_Undo.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_FeatureMethod_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_36.addWidget(self.Button_ASR_VPR_FeatureMethod_Undo, 0, 2, 1, 1)

        self.ComboBox_ASR_VPR_FeatureMethod = QComboBox(self.Frame_ASR_VPR_FeatureMethod)
        self.ComboBox_ASR_VPR_FeatureMethod.setObjectName(u"ComboBox_ASR_VPR_FeatureMethod")
        self.ComboBox_ASR_VPR_FeatureMethod.setMinimumSize(QSize(0, 27))
        self.ComboBox_ASR_VPR_FeatureMethod.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QComboBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	/*width: 12px;\n"
"	height: 12px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	margin-right: 6px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"	border-image: url(:/ComboBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"\n"
"QCom"
                        "boBox QAbstractItemView::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
""
                        "	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:vertical, QComboBox QAbstractScrollArea QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	borde"
                        "r-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:horizontal, QComboBox QAbstractScrollArea QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	"
                        "border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_36.addWidget(self.ComboBox_ASR_VPR_FeatureMethod, 1, 0, 1, 3)


        self.verticalLayout_21.addWidget(self.Frame_ASR_VPR_FeatureMethod)

        self.Frame_ASR_VPR_DurationOfAudio = QFrame(self.Frame_ASR_VPR_VPRParams_AdvanceSettings)
        self.Frame_ASR_VPR_DurationOfAudio.setObjectName(u"Frame_ASR_VPR_DurationOfAudio")
        self.Frame_ASR_VPR_DurationOfAudio.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_DurationOfAudio.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_37 = QGridLayout(self.Frame_ASR_VPR_DurationOfAudio)
        self.gridLayout_37.setSpacing(12)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_DurationOfAudio = QLabel(self.Frame_ASR_VPR_DurationOfAudio)
        self.Label_ASR_VPR_DurationOfAudio.setObjectName(u"Label_ASR_VPR_DurationOfAudio")
        sizePolicy5.setHeightForWidth(self.Label_ASR_VPR_DurationOfAudio.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_DurationOfAudio.setSizePolicy(sizePolicy5)
        self.Label_ASR_VPR_DurationOfAudio.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_37.addWidget(self.Label_ASR_VPR_DurationOfAudio, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_DurationOfAudio = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_37.addItem(self.HorizontalSpacer_ASR_VPR_DurationOfAudio, 0, 1, 1, 1)

        self.Button_ASR_VPR_DurationOfAudio_Undo = QPushButton(self.Frame_ASR_VPR_DurationOfAudio)
        self.Button_ASR_VPR_DurationOfAudio_Undo.setObjectName(u"Button_ASR_VPR_DurationOfAudio_Undo")
        self.Button_ASR_VPR_DurationOfAudio_Undo.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_DurationOfAudio_Undo.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_DurationOfAudio_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_37.addWidget(self.Button_ASR_VPR_DurationOfAudio_Undo, 0, 2, 1, 1)

        self.DoubleSpinBox_ASR_VPR_DurationOfAudio = QDoubleSpinBox(self.Frame_ASR_VPR_DurationOfAudio)
        self.DoubleSpinBox_ASR_VPR_DurationOfAudio.setObjectName(u"DoubleSpinBox_ASR_VPR_DurationOfAudio")
        self.DoubleSpinBox_ASR_VPR_DurationOfAudio.setEnabled(True)
        self.DoubleSpinBox_ASR_VPR_DurationOfAudio.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_ASR_VPR_DurationOfAudio.setStyleSheet(u"QDoubleSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	/*height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::down-arr"
                        "ow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.DoubleSpinBox_ASR_VPR_DurationOfAudio.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_ASR_VPR_DurationOfAudio.setMaximum(999999.000000000000000)

        self.gridLayout_37.addWidget(self.DoubleSpinBox_ASR_VPR_DurationOfAudio, 1, 0, 1, 3)


        self.verticalLayout_21.addWidget(self.Frame_ASR_VPR_DurationOfAudio)


        self.verticalLayout_47.addWidget(self.Frame_ASR_VPR_VPRParams_AdvanceSettings)


        self.verticalLayout_7.addWidget(self.GroupBox_ASR_VPR_VPRParams)

        self.GroupBox_ASR_VPR_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_ASR_VPR)
        self.GroupBox_ASR_VPR_OutputParams.setObjectName(u"GroupBox_ASR_VPR_OutputParams")
        self.GroupBox_ASR_VPR_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_48 = QVBoxLayout(self.GroupBox_ASR_VPR_OutputParams)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 12, 0, 12)
        self.Frame_ASR_VPR_OutputParams_BasicSettings = QFrame(self.GroupBox_ASR_VPR_OutputParams)
        self.Frame_ASR_VPR_OutputParams_BasicSettings.setObjectName(u"Frame_ASR_VPR_OutputParams_BasicSettings")
        self.verticalLayout_139 = QVBoxLayout(self.Frame_ASR_VPR_OutputParams_BasicSettings)
        self.verticalLayout_139.setSpacing(0)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_VPR_AudioSpeakersDataPath = QFrame(self.Frame_ASR_VPR_OutputParams_BasicSettings)
        self.Frame_ASR_VPR_AudioSpeakersDataPath.setObjectName(u"Frame_ASR_VPR_AudioSpeakersDataPath")
        self.Frame_ASR_VPR_AudioSpeakersDataPath.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_AudioSpeakersDataPath.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_38 = QGridLayout(self.Frame_ASR_VPR_AudioSpeakersDataPath)
        self.gridLayout_38.setSpacing(12)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_AudioSpeakersDataPath = QLabel(self.Frame_ASR_VPR_AudioSpeakersDataPath)
        self.Label_ASR_VPR_AudioSpeakersDataPath.setObjectName(u"Label_ASR_VPR_AudioSpeakersDataPath")
        sizePolicy5.setHeightForWidth(self.Label_ASR_VPR_AudioSpeakersDataPath.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_AudioSpeakersDataPath.setSizePolicy(sizePolicy5)
        self.Label_ASR_VPR_AudioSpeakersDataPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_38.addWidget(self.Label_ASR_VPR_AudioSpeakersDataPath, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_AudioSpeakersDataPath = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_38.addItem(self.HorizontalSpacer_ASR_VPR_AudioSpeakersDataPath, 0, 1, 1, 1)

        self.Button_ASR_VPR_AudioSpeakersDataPath_Undo = QPushButton(self.Frame_ASR_VPR_AudioSpeakersDataPath)
        self.Button_ASR_VPR_AudioSpeakersDataPath_Undo.setObjectName(u"Button_ASR_VPR_AudioSpeakersDataPath_Undo")
        self.Button_ASR_VPR_AudioSpeakersDataPath_Undo.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_AudioSpeakersDataPath_Undo.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_AudioSpeakersDataPath_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_38.addWidget(self.Button_ASR_VPR_AudioSpeakersDataPath_Undo, 0, 2, 1, 1)

        self.LineEdit_ASR_VPR_AudioSpeakersDataPath = LineEditBase(self.Frame_ASR_VPR_AudioSpeakersDataPath)
        self.LineEdit_ASR_VPR_AudioSpeakersDataPath.setObjectName(u"LineEdit_ASR_VPR_AudioSpeakersDataPath")
        self.LineEdit_ASR_VPR_AudioSpeakersDataPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_38.addWidget(self.LineEdit_ASR_VPR_AudioSpeakersDataPath, 1, 0, 1, 3)


        self.verticalLayout_139.addWidget(self.Frame_ASR_VPR_AudioSpeakersDataPath)


        self.verticalLayout_48.addWidget(self.Frame_ASR_VPR_OutputParams_BasicSettings)


        self.verticalLayout_7.addWidget(self.GroupBox_ASR_VPR_OutputParams)

        self.ScrollArea_Middle_ASR_VPR.setWidget(self.ScrollArea_Middle_WidgetContents_ASR_VPR)

        self.gridLayout_21.addWidget(self.ScrollArea_Middle_ASR_VPR, 0, 1, 1, 1)

        self.Widget_Right_ASR_VPR = QWidget(self.Subpage_ASR_VPR)
        self.Widget_Right_ASR_VPR.setObjectName(u"Widget_Right_ASR_VPR")
        self.Widget_Right_ASR_VPR.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout_14 = QGridLayout(self.Widget_Right_ASR_VPR)
        self.gridLayout_14.setSpacing(12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_ASR_VPR = QTextBrowser(self.Widget_Right_ASR_VPR)
        self.TextBrowser_Params_ASR_VPR.setObjectName(u"TextBrowser_Params_ASR_VPR")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_ASR_VPR.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_ASR_VPR.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_ASR_VPR.setStyleSheet(u"QTextBrowser {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	bord"
                        "er-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px"
                        ";\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_14.addWidget(self.TextBrowser_Params_ASR_VPR, 0, 0, 1, 2)

        self.Button_CheckOutput_ASR_VPR = QPushButton(self.Widget_Right_ASR_VPR)
        self.Button_CheckOutput_ASR_VPR.setObjectName(u"Button_CheckOutput_ASR_VPR")
        self.Button_CheckOutput_ASR_VPR.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 9.9px;\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_14.addWidget(self.Button_CheckOutput_ASR_VPR, 1, 0, 1, 2)


        self.gridLayout_21.addWidget(self.Widget_Right_ASR_VPR, 0, 2, 1, 1)

        self.ProgressBar_ASR_VPR = QProgressBar(self.Subpage_ASR_VPR)
        self.ProgressBar_ASR_VPR.setObjectName(u"ProgressBar_ASR_VPR")
        self.ProgressBar_ASR_VPR.setMinimumSize(QSize(0, 30))
        self.ProgressBar_ASR_VPR.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(60, 60, 60);\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(60, 60, 60), stop:1  rgb(123, 123, 123));\n"
"}")
        self.ProgressBar_ASR_VPR.setValue(0)
        self.ProgressBar_ASR_VPR.setTextVisible(False)
        self.horizontalLayout_73 = QHBoxLayout(self.ProgressBar_ASR_VPR)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_ASR_VPR = QStackedWidget(self.ProgressBar_ASR_VPR)
        self.StackedWidget_ASR_VPR.setObjectName(u"StackedWidget_ASR_VPR")
        self.StackedWidget_ASR_VPR.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_ASR_VPR.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_ASR_VPR_Execute = QWidget()
        self.Page_ASR_VPR_Execute.setObjectName(u"Page_ASR_VPR_Execute")
        self.verticalLayout_102 = QVBoxLayout(self.Page_ASR_VPR_Execute)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.Button_ASR_VPR_Execute = QPushButton(self.Page_ASR_VPR_Execute)
        self.Button_ASR_VPR_Execute.setObjectName(u"Button_ASR_VPR_Execute")
        sizePolicy3.setHeightForWidth(self.Button_ASR_VPR_Execute.sizePolicy().hasHeightForWidth())
        self.Button_ASR_VPR_Execute.setSizePolicy(sizePolicy3)
        self.Button_ASR_VPR_Execute.setMinimumSize(QSize(0, 30))
        self.Button_ASR_VPR_Execute.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_102.addWidget(self.Button_ASR_VPR_Execute)

        self.StackedWidget_ASR_VPR.addWidget(self.Page_ASR_VPR_Execute)
        self.Page_ASR_VPR_Terminate = QWidget()
        self.Page_ASR_VPR_Terminate.setObjectName(u"Page_ASR_VPR_Terminate")
        self.verticalLayout_119 = QVBoxLayout(self.Page_ASR_VPR_Terminate)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.Button_ASR_VPR_Terminate = QPushButton(self.Page_ASR_VPR_Terminate)
        self.Button_ASR_VPR_Terminate.setObjectName(u"Button_ASR_VPR_Terminate")
        sizePolicy3.setHeightForWidth(self.Button_ASR_VPR_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_ASR_VPR_Terminate.setSizePolicy(sizePolicy3)
        self.Button_ASR_VPR_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_ASR_VPR_Terminate.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_119.addWidget(self.Button_ASR_VPR_Terminate)

        self.StackedWidget_ASR_VPR.addWidget(self.Page_ASR_VPR_Terminate)

        self.horizontalLayout_73.addWidget(self.StackedWidget_ASR_VPR)


        self.gridLayout_21.addWidget(self.ProgressBar_ASR_VPR, 1, 0, 1, 3)

        self.gridLayout_21.setColumnStretch(0, 3)
        self.gridLayout_21.setColumnStretch(1, 10)
        self.gridLayout_21.setColumnStretch(2, 7)
        self.StackedWidget_Pages_ASR.addWidget(self.Subpage_ASR_VPR)

        self.verticalLayout_44.addWidget(self.StackedWidget_Pages_ASR)

        self.StackedWidget_Pages.addWidget(self.Page_ASR)
        self.Page_STT = QWidget()
        self.Page_STT.setObjectName(u"Page_STT")
        self.verticalLayout_41 = QVBoxLayout(self.Page_STT)
        self.verticalLayout_41.setSpacing(21)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(21, 12, 21, 12)
        self.Frame_STT_Top = QFrame(self.Page_STT)
        self.Frame_STT_Top.setObjectName(u"Frame_STT_Top")
        self.Frame_STT_Top.setMinimumSize(QSize(0, 60))
        self.Frame_STT_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_82 = QHBoxLayout(self.Frame_STT_Top)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_VoiceTranscriber_Title = QToolButton(self.Frame_STT_Top)
        self.ToolButton_VoiceTranscriber_Title.setObjectName(u"ToolButton_VoiceTranscriber_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_VoiceTranscriber_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_VoiceTranscriber_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_VoiceTranscriber_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color:"
                        " rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_82.addWidget(self.ToolButton_VoiceTranscriber_Title)

        self.Frame_STT_Title_Spacer = QLabel(self.Frame_STT_Top)
        self.Frame_STT_Title_Spacer.setObjectName(u"Frame_STT_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_STT_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_STT_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_STT_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;*/\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_82.addWidget(self.Frame_STT_Title_Spacer)


        self.verticalLayout_41.addWidget(self.Frame_STT_Top)

        self.StackedWidget_Pages_STT = QStackedWidget(self.Page_STT)
        self.StackedWidget_Pages_STT.setObjectName(u"StackedWidget_Pages_STT")
        self.StackedWidget_Pages_STT.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*\n"
"QTabWidget {\n"
"	background-color: transparent;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"}\n"
"QTabWidget::pane {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"	font-size: 18px;\n"
"	font-weight: 420;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 12px;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:selected {\n"
"	color: rgba(255, 255, 255, 255);\n"
"}\n"
"QTabBar::tab:hover:!selected {\n"
"}\n"
"\n"
"\n"
"QTabBar QToolButton {\n"
"}\n"
"QTabBar QToolButton:hover {\n"
"}\n"
"*/")
        self.Subpage_STT_Whisper = QWidget()
        self.Subpage_STT_Whisper.setObjectName(u"Subpage_STT_Whisper")
        self.gridLayout_19 = QGridLayout(self.Subpage_STT_Whisper)
        self.gridLayout_19.setSpacing(12)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_STT_Whisper = QWidget(self.Subpage_STT_Whisper)
        self.Widget_Left_STT_Whisper.setObjectName(u"Widget_Left_STT_Whisper")
        self.Widget_Left_STT_Whisper.setMinimumSize(QSize(150, 0))
        self.Widget_Left_STT_Whisper.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.Widget_Left_STT_Whisper)
        self.verticalLayout_8.setSpacing(12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_STT_Whisper = QTreeWidget(self.Widget_Left_STT_Whisper)
        __qtreewidgetitem2 = QTreeWidgetItem(self.TreeWidget_Catalogue_STT_Whisper)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.TreeWidget_Catalogue_STT_Whisper.setObjectName(u"TreeWidget_Catalogue_STT_Whisper")
        self.TreeWidget_Catalogue_STT_Whisper.setStyleSheet(u"QTreeView {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"	background-color: transparent;\n"
"	padding: 2.4px;\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"QTreeView::item:selected {\n"
"    background-color: ;\n"
"}\n"
"\n"
"QTreeView::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeView::branch:open:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeView::branch:closed:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:adjoins-item {\n"
"    background-color: ;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: rgba(45, 45, 45, 135);\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"	background-color: r"
                        "gba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(90, 90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}")

        self.verticalLayout_8.addWidget(self.TreeWidget_Catalogue_STT_Whisper)


        self.gridLayout_19.addWidget(self.Widget_Left_STT_Whisper, 0, 0, 1, 1)

        self.ScrollArea_Middle_STT_Whisper = QScrollArea(self.Subpage_STT_Whisper)
        self.ScrollArea_Middle_STT_Whisper.setObjectName(u"ScrollArea_Middle_STT_Whisper")
        self.ScrollArea_Middle_STT_Whisper.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_STT_Whisper.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollArea:hover {\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	"
                        "height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	borde"
                        "r-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")
        self.ScrollArea_Middle_STT_Whisper.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_STT_Whisper.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_STT_Whisper = QWidget()
        self.ScrollArea_Middle_WidgetContents_STT_Whisper.setObjectName(u"ScrollArea_Middle_WidgetContents_STT_Whisper")
        self.ScrollArea_Middle_WidgetContents_STT_Whisper.setGeometry(QRect(0, 0, 591, 934))
        self.verticalLayout_16 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_STT_Whisper)
        self.verticalLayout_16.setSpacing(12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_STT_Whisper_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_STT_Whisper)
        self.GroupBox_STT_Whisper_InputParams.setObjectName(u"GroupBox_STT_Whisper_InputParams")
        self.GroupBox_STT_Whisper_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_32 = QVBoxLayout(self.GroupBox_STT_Whisper_InputParams)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 12, 0, 12)
        self.Frame_STT_Whisper_InputParams_BasicSettings = QFrame(self.GroupBox_STT_Whisper_InputParams)
        self.Frame_STT_Whisper_InputParams_BasicSettings.setObjectName(u"Frame_STT_Whisper_InputParams_BasicSettings")
        self.verticalLayout_129 = QVBoxLayout(self.Frame_STT_Whisper_InputParams_BasicSettings)
        self.verticalLayout_129.setSpacing(0)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.Frame_STT_Whisper_AudioDir = QFrame(self.Frame_STT_Whisper_InputParams_BasicSettings)
        self.Frame_STT_Whisper_AudioDir.setObjectName(u"Frame_STT_Whisper_AudioDir")
        self.Frame_STT_Whisper_AudioDir.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_AudioDir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_39 = QGridLayout(self.Frame_STT_Whisper_AudioDir)
        self.gridLayout_39.setSpacing(12)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_AudioDir = QLabel(self.Frame_STT_Whisper_AudioDir)
        self.Label_STT_Whisper_AudioDir.setObjectName(u"Label_STT_Whisper_AudioDir")
        sizePolicy5.setHeightForWidth(self.Label_STT_Whisper_AudioDir.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_AudioDir.setSizePolicy(sizePolicy5)
        self.Label_STT_Whisper_AudioDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_39.addWidget(self.Label_STT_Whisper_AudioDir, 0, 0, 1, 1)

        self.HorizontalSpacer_STT_Whisper_AudioDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_39.addItem(self.HorizontalSpacer_STT_Whisper_AudioDir, 0, 1, 1, 1)

        self.Button_STT_Whisper_AudioDir_Undo = QPushButton(self.Frame_STT_Whisper_AudioDir)
        self.Button_STT_Whisper_AudioDir_Undo.setObjectName(u"Button_STT_Whisper_AudioDir_Undo")
        self.Button_STT_Whisper_AudioDir_Undo.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_AudioDir_Undo.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_AudioDir_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_39.addWidget(self.Button_STT_Whisper_AudioDir_Undo, 0, 2, 1, 1)

        self.LineEdit_STT_Whisper_AudioDir = LineEditBase(self.Frame_STT_Whisper_AudioDir)
        self.LineEdit_STT_Whisper_AudioDir.setObjectName(u"LineEdit_STT_Whisper_AudioDir")
        self.LineEdit_STT_Whisper_AudioDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_39.addWidget(self.LineEdit_STT_Whisper_AudioDir, 1, 0, 1, 3)


        self.verticalLayout_129.addWidget(self.Frame_STT_Whisper_AudioDir)


        self.verticalLayout_32.addWidget(self.Frame_STT_Whisper_InputParams_BasicSettings)


        self.verticalLayout_16.addWidget(self.GroupBox_STT_Whisper_InputParams)

        self.GroupBox_STT_Whisper_WhisperParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_STT_Whisper)
        self.GroupBox_STT_Whisper_WhisperParams.setObjectName(u"GroupBox_STT_Whisper_WhisperParams")
        self.GroupBox_STT_Whisper_WhisperParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_49 = QVBoxLayout(self.GroupBox_STT_Whisper_WhisperParams)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 12, 0, 12)
        self.Frame_STT_Whisper_WhisperParams_BasicSettings = QFrame(self.GroupBox_STT_Whisper_WhisperParams)
        self.Frame_STT_Whisper_WhisperParams_BasicSettings.setObjectName(u"Frame_STT_Whisper_WhisperParams_BasicSettings")
        self.verticalLayout_37 = QVBoxLayout(self.Frame_STT_Whisper_WhisperParams_BasicSettings)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.Frame_STT_Whisper_AddLanguageInfo = QFrame(self.Frame_STT_Whisper_WhisperParams_BasicSettings)
        self.Frame_STT_Whisper_AddLanguageInfo.setObjectName(u"Frame_STT_Whisper_AddLanguageInfo")
        self.Frame_STT_Whisper_AddLanguageInfo.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_AddLanguageInfo.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_40 = QGridLayout(self.Frame_STT_Whisper_AddLanguageInfo)
        self.gridLayout_40.setSpacing(12)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_AddLanguageInfo = QLabel(self.Frame_STT_Whisper_AddLanguageInfo)
        self.Label_STT_Whisper_AddLanguageInfo.setObjectName(u"Label_STT_Whisper_AddLanguageInfo")
        sizePolicy5.setHeightForWidth(self.Label_STT_Whisper_AddLanguageInfo.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_AddLanguageInfo.setSizePolicy(sizePolicy5)
        self.Label_STT_Whisper_AddLanguageInfo.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_40.addWidget(self.Label_STT_Whisper_AddLanguageInfo, 0, 0, 1, 1)

        self.HorizontalSpacer_STT_Whisper_AddLanguageInfo = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_40.addItem(self.HorizontalSpacer_STT_Whisper_AddLanguageInfo, 0, 1, 1, 1)

        self.Button_STT_Whisper_AddLanguageInfo_Undo = QPushButton(self.Frame_STT_Whisper_AddLanguageInfo)
        self.Button_STT_Whisper_AddLanguageInfo_Undo.setObjectName(u"Button_STT_Whisper_AddLanguageInfo_Undo")
        self.Button_STT_Whisper_AddLanguageInfo_Undo.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_AddLanguageInfo_Undo.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_AddLanguageInfo_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_40.addWidget(self.Button_STT_Whisper_AddLanguageInfo_Undo, 0, 2, 1, 1)

        self.CheckBox_STT_Whisper_AddLanguageInfo = QCheckBox(self.Frame_STT_Whisper_AddLanguageInfo)
        self.CheckBox_STT_Whisper_AddLanguageInfo.setObjectName(u"CheckBox_STT_Whisper_AddLanguageInfo")
        self.CheckBox_STT_Whisper_AddLanguageInfo.setMinimumSize(QSize(0, 27))
        self.CheckBox_STT_Whisper_AddLanguageInfo.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_40.addWidget(self.CheckBox_STT_Whisper_AddLanguageInfo, 1, 0, 1, 3)


        self.verticalLayout_37.addWidget(self.Frame_STT_Whisper_AddLanguageInfo)

        self.Frame_STT_Whisper_ModelPath = QFrame(self.Frame_STT_Whisper_WhisperParams_BasicSettings)
        self.Frame_STT_Whisper_ModelPath.setObjectName(u"Frame_STT_Whisper_ModelPath")
        self.Frame_STT_Whisper_ModelPath.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_ModelPath.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_41 = QGridLayout(self.Frame_STT_Whisper_ModelPath)
        self.gridLayout_41.setSpacing(12)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_ModelPath = QLabel(self.Frame_STT_Whisper_ModelPath)
        self.Label_STT_Whisper_ModelPath.setObjectName(u"Label_STT_Whisper_ModelPath")
        sizePolicy5.setHeightForWidth(self.Label_STT_Whisper_ModelPath.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_ModelPath.setSizePolicy(sizePolicy5)
        self.Label_STT_Whisper_ModelPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_41.addWidget(self.Label_STT_Whisper_ModelPath, 0, 0, 1, 1)

        self.HorizontalSpacer_STT_Whisper_ModelPath = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_41.addItem(self.HorizontalSpacer_STT_Whisper_ModelPath, 0, 1, 1, 1)

        self.Button_STT_Whisper_ModelPath_Undo = QPushButton(self.Frame_STT_Whisper_ModelPath)
        self.Button_STT_Whisper_ModelPath_Undo.setObjectName(u"Button_STT_Whisper_ModelPath_Undo")
        self.Button_STT_Whisper_ModelPath_Undo.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_ModelPath_Undo.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_ModelPath_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_41.addWidget(self.Button_STT_Whisper_ModelPath_Undo, 0, 2, 1, 1)

        self.LineEdit_STT_Whisper_ModelPath = LineEditBase(self.Frame_STT_Whisper_ModelPath)
        self.LineEdit_STT_Whisper_ModelPath.setObjectName(u"LineEdit_STT_Whisper_ModelPath")
        self.LineEdit_STT_Whisper_ModelPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_41.addWidget(self.LineEdit_STT_Whisper_ModelPath, 1, 0, 1, 3)


        self.verticalLayout_37.addWidget(self.Frame_STT_Whisper_ModelPath)


        self.verticalLayout_49.addWidget(self.Frame_STT_Whisper_WhisperParams_BasicSettings)

        self.CheckBox_STT_Whisper_WhisperParams_Toggle_AdvanceSettings = QCheckBox(self.GroupBox_STT_Whisper_WhisperParams)
        self.CheckBox_STT_Whisper_WhisperParams_Toggle_AdvanceSettings.setObjectName(u"CheckBox_STT_Whisper_WhisperParams_Toggle_AdvanceSettings")
        self.CheckBox_STT_Whisper_WhisperParams_Toggle_AdvanceSettings.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	font-weight: 630;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding-top: 9px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"    background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: transparent;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/RightCaret.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/DownCaret.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_49.addWidget(self.CheckBox_STT_Whisper_WhisperParams_Toggle_AdvanceSettings)

        self.Frame_STT_Whisper_WhisperParams_AdvanceSettings = QFrame(self.GroupBox_STT_Whisper_WhisperParams)
        self.Frame_STT_Whisper_WhisperParams_AdvanceSettings.setObjectName(u"Frame_STT_Whisper_WhisperParams_AdvanceSettings")
        self.verticalLayout_15 = QVBoxLayout(self.Frame_STT_Whisper_WhisperParams_AdvanceSettings)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Frame_STT_Whisper_fp16 = QFrame(self.Frame_STT_Whisper_WhisperParams_AdvanceSettings)
        self.Frame_STT_Whisper_fp16.setObjectName(u"Frame_STT_Whisper_fp16")
        self.Frame_STT_Whisper_fp16.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_fp16.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_44 = QGridLayout(self.Frame_STT_Whisper_fp16)
        self.gridLayout_44.setSpacing(12)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_fp16 = QLabel(self.Frame_STT_Whisper_fp16)
        self.Label_STT_Whisper_fp16.setObjectName(u"Label_STT_Whisper_fp16")
        sizePolicy5.setHeightForWidth(self.Label_STT_Whisper_fp16.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_fp16.setSizePolicy(sizePolicy5)
        self.Label_STT_Whisper_fp16.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_44.addWidget(self.Label_STT_Whisper_fp16, 0, 0, 1, 1)

        self.HorizontalSpacer_STT_Whisper_fp16 = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_44.addItem(self.HorizontalSpacer_STT_Whisper_fp16, 0, 1, 1, 1)

        self.CheckBox_STT_Whisper_fp16 = QCheckBox(self.Frame_STT_Whisper_fp16)
        self.CheckBox_STT_Whisper_fp16.setObjectName(u"CheckBox_STT_Whisper_fp16")
        self.CheckBox_STT_Whisper_fp16.setMinimumSize(QSize(0, 27))
        self.CheckBox_STT_Whisper_fp16.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_44.addWidget(self.CheckBox_STT_Whisper_fp16, 1, 0, 1, 3)

        self.Button_STT_Whisper_fp16_Undo = QPushButton(self.Frame_STT_Whisper_fp16)
        self.Button_STT_Whisper_fp16_Undo.setObjectName(u"Button_STT_Whisper_fp16_Undo")
        self.Button_STT_Whisper_fp16_Undo.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_fp16_Undo.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_fp16_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_44.addWidget(self.Button_STT_Whisper_fp16_Undo, 0, 2, 1, 1)


        self.verticalLayout_15.addWidget(self.Frame_STT_Whisper_fp16)

        self.Frame_STT_Whisper_ConditionOnPreviousText = QFrame(self.Frame_STT_Whisper_WhisperParams_AdvanceSettings)
        self.Frame_STT_Whisper_ConditionOnPreviousText.setObjectName(u"Frame_STT_Whisper_ConditionOnPreviousText")
        self.Frame_STT_Whisper_ConditionOnPreviousText.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_ConditionOnPreviousText.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_43 = QGridLayout(self.Frame_STT_Whisper_ConditionOnPreviousText)
        self.gridLayout_43.setSpacing(12)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(21, 12, 21, 12)
        self.CheckBox_STT_Whisper_ConditionOnPreviousText = QCheckBox(self.Frame_STT_Whisper_ConditionOnPreviousText)
        self.CheckBox_STT_Whisper_ConditionOnPreviousText.setObjectName(u"CheckBox_STT_Whisper_ConditionOnPreviousText")
        self.CheckBox_STT_Whisper_ConditionOnPreviousText.setMinimumSize(QSize(0, 27))
        self.CheckBox_STT_Whisper_ConditionOnPreviousText.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_43.addWidget(self.CheckBox_STT_Whisper_ConditionOnPreviousText, 1, 0, 1, 3)

        self.HorizontalSpacer_STT_Whisper_ConditionOnPreviousText = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_43.addItem(self.HorizontalSpacer_STT_Whisper_ConditionOnPreviousText, 0, 1, 1, 1)

        self.Button_STT_Whisper_ConditionOnPreviousText_Undo = QPushButton(self.Frame_STT_Whisper_ConditionOnPreviousText)
        self.Button_STT_Whisper_ConditionOnPreviousText_Undo.setObjectName(u"Button_STT_Whisper_ConditionOnPreviousText_Undo")
        self.Button_STT_Whisper_ConditionOnPreviousText_Undo.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_ConditionOnPreviousText_Undo.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_ConditionOnPreviousText_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_43.addWidget(self.Button_STT_Whisper_ConditionOnPreviousText_Undo, 0, 2, 1, 1)

        self.Label_STT_Whisper_ConditionOnPreviousText = QLabel(self.Frame_STT_Whisper_ConditionOnPreviousText)
        self.Label_STT_Whisper_ConditionOnPreviousText.setObjectName(u"Label_STT_Whisper_ConditionOnPreviousText")
        sizePolicy5.setHeightForWidth(self.Label_STT_Whisper_ConditionOnPreviousText.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_ConditionOnPreviousText.setSizePolicy(sizePolicy5)
        self.Label_STT_Whisper_ConditionOnPreviousText.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_43.addWidget(self.Label_STT_Whisper_ConditionOnPreviousText, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.Frame_STT_Whisper_ConditionOnPreviousText)

        self.Frame_STT_Whisper_Verbose = QFrame(self.Frame_STT_Whisper_WhisperParams_AdvanceSettings)
        self.Frame_STT_Whisper_Verbose.setObjectName(u"Frame_STT_Whisper_Verbose")
        self.Frame_STT_Whisper_Verbose.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_Verbose.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_42 = QGridLayout(self.Frame_STT_Whisper_Verbose)
        self.gridLayout_42.setSpacing(12)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_Verbose = QLabel(self.Frame_STT_Whisper_Verbose)
        self.Label_STT_Whisper_Verbose.setObjectName(u"Label_STT_Whisper_Verbose")
        sizePolicy5.setHeightForWidth(self.Label_STT_Whisper_Verbose.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_Verbose.setSizePolicy(sizePolicy5)
        self.Label_STT_Whisper_Verbose.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_42.addWidget(self.Label_STT_Whisper_Verbose, 0, 0, 1, 1)

        self.HorizontalSpacer_STT_Whisper_Verbose = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_42.addItem(self.HorizontalSpacer_STT_Whisper_Verbose, 0, 1, 1, 1)

        self.CheckBox_STT_Whisper_Verbose = QCheckBox(self.Frame_STT_Whisper_Verbose)
        self.CheckBox_STT_Whisper_Verbose.setObjectName(u"CheckBox_STT_Whisper_Verbose")
        self.CheckBox_STT_Whisper_Verbose.setMinimumSize(QSize(0, 27))
        self.CheckBox_STT_Whisper_Verbose.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_42.addWidget(self.CheckBox_STT_Whisper_Verbose, 1, 0, 1, 3)

        self.Button_STT_Whisper_Verbose_Undo = QPushButton(self.Frame_STT_Whisper_Verbose)
        self.Button_STT_Whisper_Verbose_Undo.setObjectName(u"Button_STT_Whisper_Verbose_Undo")
        self.Button_STT_Whisper_Verbose_Undo.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_Verbose_Undo.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_Verbose_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_42.addWidget(self.Button_STT_Whisper_Verbose_Undo, 0, 2, 1, 1)


        self.verticalLayout_15.addWidget(self.Frame_STT_Whisper_Verbose)


        self.verticalLayout_49.addWidget(self.Frame_STT_Whisper_WhisperParams_AdvanceSettings)


        self.verticalLayout_16.addWidget(self.GroupBox_STT_Whisper_WhisperParams)

        self.GroupBox_STT_Whisper_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_STT_Whisper)
        self.GroupBox_STT_Whisper_OutputParams.setObjectName(u"GroupBox_STT_Whisper_OutputParams")
        self.GroupBox_STT_Whisper_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_89 = QVBoxLayout(self.GroupBox_STT_Whisper_OutputParams)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 12, 0, 12)
        self.Frame_STT_Whisper_OutputParams_BasicSettings = QFrame(self.GroupBox_STT_Whisper_OutputParams)
        self.Frame_STT_Whisper_OutputParams_BasicSettings.setObjectName(u"Frame_STT_Whisper_OutputParams_BasicSettings")
        self.verticalLayout_135 = QVBoxLayout(self.Frame_STT_Whisper_OutputParams_BasicSettings)
        self.verticalLayout_135.setSpacing(0)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.Frame_STT_Whisper_SRTDir = QFrame(self.Frame_STT_Whisper_OutputParams_BasicSettings)
        self.Frame_STT_Whisper_SRTDir.setObjectName(u"Frame_STT_Whisper_SRTDir")
        self.Frame_STT_Whisper_SRTDir.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_SRTDir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_45 = QGridLayout(self.Frame_STT_Whisper_SRTDir)
        self.gridLayout_45.setSpacing(12)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_SRTDir = QLabel(self.Frame_STT_Whisper_SRTDir)
        self.Label_STT_Whisper_SRTDir.setObjectName(u"Label_STT_Whisper_SRTDir")
        sizePolicy5.setHeightForWidth(self.Label_STT_Whisper_SRTDir.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_SRTDir.setSizePolicy(sizePolicy5)
        self.Label_STT_Whisper_SRTDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_45.addWidget(self.Label_STT_Whisper_SRTDir, 0, 0, 1, 1)

        self.HorizontalSpacer_STT_Whisper_SRTDir = QSpacerItem(481, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_45.addItem(self.HorizontalSpacer_STT_Whisper_SRTDir, 0, 1, 1, 1)

        self.Button_STT_Whisper_SRTDir_Undo = QPushButton(self.Frame_STT_Whisper_SRTDir)
        self.Button_STT_Whisper_SRTDir_Undo.setObjectName(u"Button_STT_Whisper_SRTDir_Undo")
        self.Button_STT_Whisper_SRTDir_Undo.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_SRTDir_Undo.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_SRTDir_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_45.addWidget(self.Button_STT_Whisper_SRTDir_Undo, 0, 2, 1, 1)

        self.LineEdit_STT_Whisper_SRTDir = LineEditBase(self.Frame_STT_Whisper_SRTDir)
        self.LineEdit_STT_Whisper_SRTDir.setObjectName(u"LineEdit_STT_Whisper_SRTDir")
        self.LineEdit_STT_Whisper_SRTDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_45.addWidget(self.LineEdit_STT_Whisper_SRTDir, 1, 0, 1, 3)


        self.verticalLayout_135.addWidget(self.Frame_STT_Whisper_SRTDir)


        self.verticalLayout_89.addWidget(self.Frame_STT_Whisper_OutputParams_BasicSettings)


        self.verticalLayout_16.addWidget(self.GroupBox_STT_Whisper_OutputParams)

        self.VerticalSpacer_STT_Whisper = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.VerticalSpacer_STT_Whisper)

        self.ScrollArea_Middle_STT_Whisper.setWidget(self.ScrollArea_Middle_WidgetContents_STT_Whisper)

        self.gridLayout_19.addWidget(self.ScrollArea_Middle_STT_Whisper, 0, 1, 1, 1)

        self.Widget_Right_STT_Whisper = QWidget(self.Subpage_STT_Whisper)
        self.Widget_Right_STT_Whisper.setObjectName(u"Widget_Right_STT_Whisper")
        self.Widget_Right_STT_Whisper.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout_15 = QGridLayout(self.Widget_Right_STT_Whisper)
        self.gridLayout_15.setSpacing(12)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_STT_Whisper = QTextBrowser(self.Widget_Right_STT_Whisper)
        self.TextBrowser_Params_STT_Whisper.setObjectName(u"TextBrowser_Params_STT_Whisper")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_STT_Whisper.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_STT_Whisper.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_STT_Whisper.setStyleSheet(u"QTextBrowser {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	bord"
                        "er-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px"
                        ";\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_15.addWidget(self.TextBrowser_Params_STT_Whisper, 0, 0, 1, 2)

        self.Button_CheckOutput_STT_Whisper = QPushButton(self.Widget_Right_STT_Whisper)
        self.Button_CheckOutput_STT_Whisper.setObjectName(u"Button_CheckOutput_STT_Whisper")
        self.Button_CheckOutput_STT_Whisper.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 9.9px;\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_15.addWidget(self.Button_CheckOutput_STT_Whisper, 1, 0, 1, 2)


        self.gridLayout_19.addWidget(self.Widget_Right_STT_Whisper, 0, 2, 1, 1)

        self.ProgressBar_STT_Whisper = QProgressBar(self.Subpage_STT_Whisper)
        self.ProgressBar_STT_Whisper.setObjectName(u"ProgressBar_STT_Whisper")
        self.ProgressBar_STT_Whisper.setMinimumSize(QSize(0, 30))
        self.ProgressBar_STT_Whisper.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(60, 60, 60);\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(60, 60, 60), stop:1  rgb(123, 123, 123));\n"
"}")
        self.ProgressBar_STT_Whisper.setValue(0)
        self.ProgressBar_STT_Whisper.setTextVisible(False)
        self.horizontalLayout_35 = QHBoxLayout(self.ProgressBar_STT_Whisper)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_STT_Whisper = QStackedWidget(self.ProgressBar_STT_Whisper)
        self.StackedWidget_STT_Whisper.setObjectName(u"StackedWidget_STT_Whisper")
        self.StackedWidget_STT_Whisper.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_STT_Whisper.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_STT_Whisper_Execute = QWidget()
        self.Page_STT_Whisper_Execute.setObjectName(u"Page_STT_Whisper_Execute")
        self.verticalLayout_90 = QVBoxLayout(self.Page_STT_Whisper_Execute)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.Button_STT_Whisper_Execute = QPushButton(self.Page_STT_Whisper_Execute)
        self.Button_STT_Whisper_Execute.setObjectName(u"Button_STT_Whisper_Execute")
        sizePolicy3.setHeightForWidth(self.Button_STT_Whisper_Execute.sizePolicy().hasHeightForWidth())
        self.Button_STT_Whisper_Execute.setSizePolicy(sizePolicy3)
        self.Button_STT_Whisper_Execute.setMinimumSize(QSize(0, 30))
        self.Button_STT_Whisper_Execute.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_90.addWidget(self.Button_STT_Whisper_Execute)

        self.StackedWidget_STT_Whisper.addWidget(self.Page_STT_Whisper_Execute)
        self.Page_STT_Whisper_Terminate = QWidget()
        self.Page_STT_Whisper_Terminate.setObjectName(u"Page_STT_Whisper_Terminate")
        self.verticalLayout_91 = QVBoxLayout(self.Page_STT_Whisper_Terminate)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.Button_STT_Whisper_Terminate = QPushButton(self.Page_STT_Whisper_Terminate)
        self.Button_STT_Whisper_Terminate.setObjectName(u"Button_STT_Whisper_Terminate")
        sizePolicy3.setHeightForWidth(self.Button_STT_Whisper_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_STT_Whisper_Terminate.setSizePolicy(sizePolicy3)
        self.Button_STT_Whisper_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_STT_Whisper_Terminate.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_91.addWidget(self.Button_STT_Whisper_Terminate)

        self.StackedWidget_STT_Whisper.addWidget(self.Page_STT_Whisper_Terminate)

        self.horizontalLayout_35.addWidget(self.StackedWidget_STT_Whisper)


        self.gridLayout_19.addWidget(self.ProgressBar_STT_Whisper, 1, 0, 1, 3)

        self.gridLayout_19.setColumnStretch(0, 3)
        self.gridLayout_19.setColumnStretch(1, 10)
        self.gridLayout_19.setColumnStretch(2, 7)
        self.StackedWidget_Pages_STT.addWidget(self.Subpage_STT_Whisper)

        self.verticalLayout_41.addWidget(self.StackedWidget_Pages_STT)

        self.StackedWidget_Pages.addWidget(self.Page_STT)
        self.Page_Dataset = QWidget()
        self.Page_Dataset.setObjectName(u"Page_Dataset")
        self.verticalLayout_39 = QVBoxLayout(self.Page_Dataset)
        self.verticalLayout_39.setSpacing(21)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(21, 12, 21, 12)
        self.Frame_Dataset_Top = QFrame(self.Page_Dataset)
        self.Frame_Dataset_Top.setObjectName(u"Frame_Dataset_Top")
        self.Frame_Dataset_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Dataset_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_83 = QHBoxLayout(self.Frame_Dataset_Top)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_DatasetCreator_Title = QToolButton(self.Frame_Dataset_Top)
        self.ToolButton_DatasetCreator_Title.setObjectName(u"ToolButton_DatasetCreator_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_DatasetCreator_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_DatasetCreator_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_DatasetCreator_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color:"
                        " rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_83.addWidget(self.ToolButton_DatasetCreator_Title)

        self.Frame_Dataset_Title_Spacer = QLabel(self.Frame_Dataset_Top)
        self.Frame_Dataset_Title_Spacer.setObjectName(u"Frame_Dataset_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_Dataset_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Dataset_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_Dataset_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;*/\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_83.addWidget(self.Frame_Dataset_Title_Spacer)


        self.verticalLayout_39.addWidget(self.Frame_Dataset_Top)

        self.StackedWidget_Pages_Dataset = QStackedWidget(self.Page_Dataset)
        self.StackedWidget_Pages_Dataset.setObjectName(u"StackedWidget_Pages_Dataset")
        self.StackedWidget_Pages_Dataset.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*\n"
"QTabWidget {\n"
"	background-color: transparent;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"}\n"
"QTabWidget::pane {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"	font-size: 18px;\n"
"	font-weight: 420;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 12px;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:selected {\n"
"	color: rgba(255, 255, 255, 255);\n"
"}\n"
"QTabBar::tab:hover:!selected {\n"
"}\n"
"\n"
"\n"
"QTabBar QToolButton {\n"
"}\n"
"QTabBar QToolButton:hover {\n"
"}\n"
"*/")
        self.Subpage_DAT_VITS = QWidget()
        self.Subpage_DAT_VITS.setObjectName(u"Subpage_DAT_VITS")
        self.gridLayout_8 = QGridLayout(self.Subpage_DAT_VITS)
        self.gridLayout_8.setSpacing(12)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_DAT_VITS = QWidget(self.Subpage_DAT_VITS)
        self.Widget_Left_DAT_VITS.setObjectName(u"Widget_Left_DAT_VITS")
        self.Widget_Left_DAT_VITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_DAT_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.Widget_Left_DAT_VITS)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_DAT_VITS = QTreeWidget(self.Widget_Left_DAT_VITS)
        __qtreewidgetitem3 = QTreeWidgetItem(self.TreeWidget_Catalogue_DAT_VITS)
        QTreeWidgetItem(__qtreewidgetitem3)
        self.TreeWidget_Catalogue_DAT_VITS.setObjectName(u"TreeWidget_Catalogue_DAT_VITS")
        self.TreeWidget_Catalogue_DAT_VITS.setStyleSheet(u"QTreeView {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"	background-color: transparent;\n"
"	padding: 2.4px;\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"QTreeView::item:selected {\n"
"    background-color: ;\n"
"}\n"
"\n"
"QTreeView::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeView::branch:open:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeView::branch:closed:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:adjoins-item {\n"
"    background-color: ;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: rgba(45, 45, 45, 135);\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"	background-color: r"
                        "gba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(90, 90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}")

        self.verticalLayout_9.addWidget(self.TreeWidget_Catalogue_DAT_VITS)


        self.gridLayout_8.addWidget(self.Widget_Left_DAT_VITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_DAT_VITS = QScrollArea(self.Subpage_DAT_VITS)
        self.ScrollArea_Middle_DAT_VITS.setObjectName(u"ScrollArea_Middle_DAT_VITS")
        self.ScrollArea_Middle_DAT_VITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_DAT_VITS.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollArea:hover {\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	"
                        "height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	borde"
                        "r-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")
        self.ScrollArea_Middle_DAT_VITS.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_DAT_VITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_DAT_VITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_DAT_VITS.setObjectName(u"ScrollArea_Middle_WidgetContents_DAT_VITS")
        self.ScrollArea_Middle_WidgetContents_DAT_VITS.setGeometry(QRect(0, 0, 591, 1566))
        self.verticalLayout_36 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.verticalLayout_36.setSpacing(12)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_DAT_VITS_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.GroupBox_DAT_VITS_InputParams.setObjectName(u"GroupBox_DAT_VITS_InputParams")
        self.GroupBox_DAT_VITS_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_111 = QVBoxLayout(self.GroupBox_DAT_VITS_InputParams)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_VITS_InputParams_BasicSettings = QFrame(self.GroupBox_DAT_VITS_InputParams)
        self.Frame_DAT_VITS_InputParams_BasicSettings.setObjectName(u"Frame_DAT_VITS_InputParams_BasicSettings")
        self.verticalLayout_29 = QVBoxLayout(self.Frame_DAT_VITS_InputParams_BasicSettings)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_AudioSpeakersDataPath = QFrame(self.Frame_DAT_VITS_InputParams_BasicSettings)
        self.Frame_DAT_VITS_AudioSpeakersDataPath.setObjectName(u"Frame_DAT_VITS_AudioSpeakersDataPath")
        self.Frame_DAT_VITS_AudioSpeakersDataPath.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_AudioSpeakersDataPath.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_46 = QGridLayout(self.Frame_DAT_VITS_AudioSpeakersDataPath)
        self.gridLayout_46.setSpacing(12)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_AudioSpeakersDataPath = QLabel(self.Frame_DAT_VITS_AudioSpeakersDataPath)
        self.Label_DAT_VITS_AudioSpeakersDataPath.setObjectName(u"Label_DAT_VITS_AudioSpeakersDataPath")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_AudioSpeakersDataPath.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_AudioSpeakersDataPath.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_AudioSpeakersDataPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_46.addWidget(self.Label_DAT_VITS_AudioSpeakersDataPath, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_InputParams = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_46.addItem(self.HorizontalSpacer_DAT_VITS_InputParams, 0, 1, 1, 1)

        self.Button_DAT_VITS_AudioSpeakersDataPath_Undo = QPushButton(self.Frame_DAT_VITS_AudioSpeakersDataPath)
        self.Button_DAT_VITS_AudioSpeakersDataPath_Undo.setObjectName(u"Button_DAT_VITS_AudioSpeakersDataPath_Undo")
        self.Button_DAT_VITS_AudioSpeakersDataPath_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_AudioSpeakersDataPath_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_AudioSpeakersDataPath_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_46.addWidget(self.Button_DAT_VITS_AudioSpeakersDataPath_Undo, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_AudioSpeakersDataPath = LineEditBase(self.Frame_DAT_VITS_AudioSpeakersDataPath)
        self.LineEdit_DAT_VITS_AudioSpeakersDataPath.setObjectName(u"LineEdit_DAT_VITS_AudioSpeakersDataPath")
        self.LineEdit_DAT_VITS_AudioSpeakersDataPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_46.addWidget(self.LineEdit_DAT_VITS_AudioSpeakersDataPath, 1, 0, 1, 3)


        self.verticalLayout_29.addWidget(self.Frame_DAT_VITS_AudioSpeakersDataPath)

        self.Frame_DAT_VITS_SRTDir = QFrame(self.Frame_DAT_VITS_InputParams_BasicSettings)
        self.Frame_DAT_VITS_SRTDir.setObjectName(u"Frame_DAT_VITS_SRTDir")
        self.Frame_DAT_VITS_SRTDir.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SRTDir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_47 = QGridLayout(self.Frame_DAT_VITS_SRTDir)
        self.gridLayout_47.setSpacing(12)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_SRTDir = QLabel(self.Frame_DAT_VITS_SRTDir)
        self.Label_DAT_VITS_SRTDir.setObjectName(u"Label_DAT_VITS_SRTDir")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_SRTDir.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_SRTDir.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_SRTDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_47.addWidget(self.Label_DAT_VITS_SRTDir, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_SRTDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_47.addItem(self.HorizontalSpacer_DAT_VITS_SRTDir, 0, 1, 1, 1)

        self.Button_DAT_VITS_SRTDir_Undo = QPushButton(self.Frame_DAT_VITS_SRTDir)
        self.Button_DAT_VITS_SRTDir_Undo.setObjectName(u"Button_DAT_VITS_SRTDir_Undo")
        self.Button_DAT_VITS_SRTDir_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_SRTDir_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_SRTDir_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_47.addWidget(self.Button_DAT_VITS_SRTDir_Undo, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_SRTDir = LineEditBase(self.Frame_DAT_VITS_SRTDir)
        self.LineEdit_DAT_VITS_SRTDir.setObjectName(u"LineEdit_DAT_VITS_SRTDir")
        self.LineEdit_DAT_VITS_SRTDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_47.addWidget(self.LineEdit_DAT_VITS_SRTDir, 1, 0, 1, 3)


        self.verticalLayout_29.addWidget(self.Frame_DAT_VITS_SRTDir)


        self.verticalLayout_111.addWidget(self.Frame_DAT_VITS_InputParams_BasicSettings)


        self.verticalLayout_36.addWidget(self.GroupBox_DAT_VITS_InputParams)

        self.GroupBox_DAT_VITS_VITSParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.GroupBox_DAT_VITS_VITSParams.setObjectName(u"GroupBox_DAT_VITS_VITSParams")
        self.GroupBox_DAT_VITS_VITSParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_115 = QVBoxLayout(self.GroupBox_DAT_VITS_VITSParams)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_VITS_VITSParams_BasicSettings = QFrame(self.GroupBox_DAT_VITS_VITSParams)
        self.Frame_DAT_VITS_VITSParams_BasicSettings.setObjectName(u"Frame_DAT_VITS_VITSParams_BasicSettings")
        self.verticalLayout_30 = QVBoxLayout(self.Frame_DAT_VITS_VITSParams_BasicSettings)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_DataFormat = QFrame(self.Frame_DAT_VITS_VITSParams_BasicSettings)
        self.Frame_DAT_VITS_DataFormat.setObjectName(u"Frame_DAT_VITS_DataFormat")
        self.Frame_DAT_VITS_DataFormat.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_DataFormat.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_76 = QGridLayout(self.Frame_DAT_VITS_DataFormat)
        self.gridLayout_76.setSpacing(12)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.gridLayout_76.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_DataFormat = QLabel(self.Frame_DAT_VITS_DataFormat)
        self.Label_DAT_VITS_DataFormat.setObjectName(u"Label_DAT_VITS_DataFormat")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_DataFormat.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_DataFormat.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_DataFormat.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_76.addWidget(self.Label_DAT_VITS_DataFormat, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_DataFormat = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_76.addItem(self.HorizontalSpacer_DAT_VITS_DataFormat, 0, 1, 1, 1)

        self.Button_DAT_VITS_DataFormat_Undo = QPushButton(self.Frame_DAT_VITS_DataFormat)
        self.Button_DAT_VITS_DataFormat_Undo.setObjectName(u"Button_DAT_VITS_DataFormat_Undo")
        self.Button_DAT_VITS_DataFormat_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_DataFormat_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_DataFormat_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_76.addWidget(self.Button_DAT_VITS_DataFormat_Undo, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_DataFormat = LineEditBase(self.Frame_DAT_VITS_DataFormat)
        self.LineEdit_DAT_VITS_DataFormat.setObjectName(u"LineEdit_DAT_VITS_DataFormat")
        self.LineEdit_DAT_VITS_DataFormat.setMinimumSize(QSize(0, 27))

        self.gridLayout_76.addWidget(self.LineEdit_DAT_VITS_DataFormat, 1, 0, 1, 3)


        self.verticalLayout_30.addWidget(self.Frame_DAT_VITS_DataFormat)

        self.Frame_DAT_VITS_AddAuxiliaryData = QFrame(self.Frame_DAT_VITS_VITSParams_BasicSettings)
        self.Frame_DAT_VITS_AddAuxiliaryData.setObjectName(u"Frame_DAT_VITS_AddAuxiliaryData")
        self.Frame_DAT_VITS_AddAuxiliaryData.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_AddAuxiliaryData.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_48 = QGridLayout(self.Frame_DAT_VITS_AddAuxiliaryData)
        self.gridLayout_48.setSpacing(12)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_AddAuxiliaryData = QLabel(self.Frame_DAT_VITS_AddAuxiliaryData)
        self.Label_DAT_VITS_AddAuxiliaryData.setObjectName(u"Label_DAT_VITS_AddAuxiliaryData")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_AddAuxiliaryData.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_AddAuxiliaryData.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_AddAuxiliaryData.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_48.addWidget(self.Label_DAT_VITS_AddAuxiliaryData, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_AddAuxiliaryData = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_48.addItem(self.HorizontalSpacer_DAT_VITS_AddAuxiliaryData, 0, 1, 1, 1)

        self.Button_DAT_VITS_AddAuxiliaryData_Undo = QPushButton(self.Frame_DAT_VITS_AddAuxiliaryData)
        self.Button_DAT_VITS_AddAuxiliaryData_Undo.setObjectName(u"Button_DAT_VITS_AddAuxiliaryData_Undo")
        self.Button_DAT_VITS_AddAuxiliaryData_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_AddAuxiliaryData_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_AddAuxiliaryData_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_48.addWidget(self.Button_DAT_VITS_AddAuxiliaryData_Undo, 0, 2, 1, 1)

        self.CheckBox_DAT_VITS_AddAuxiliaryData = QCheckBox(self.Frame_DAT_VITS_AddAuxiliaryData)
        self.CheckBox_DAT_VITS_AddAuxiliaryData.setObjectName(u"CheckBox_DAT_VITS_AddAuxiliaryData")
        self.CheckBox_DAT_VITS_AddAuxiliaryData.setMinimumSize(QSize(0, 27))
        self.CheckBox_DAT_VITS_AddAuxiliaryData.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_48.addWidget(self.CheckBox_DAT_VITS_AddAuxiliaryData, 1, 0, 1, 3)


        self.verticalLayout_30.addWidget(self.Frame_DAT_VITS_AddAuxiliaryData)

        self.Frame_DAT_VITS_AuxiliaryDataPath = QFrame(self.Frame_DAT_VITS_VITSParams_BasicSettings)
        self.Frame_DAT_VITS_AuxiliaryDataPath.setObjectName(u"Frame_DAT_VITS_AuxiliaryDataPath")
        self.Frame_DAT_VITS_AuxiliaryDataPath.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_AuxiliaryDataPath.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_53 = QGridLayout(self.Frame_DAT_VITS_AuxiliaryDataPath)
        self.gridLayout_53.setSpacing(12)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_AuxiliaryDataPath = QLabel(self.Frame_DAT_VITS_AuxiliaryDataPath)
        self.Label_DAT_VITS_AuxiliaryDataPath.setObjectName(u"Label_DAT_VITS_AuxiliaryDataPath")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_AuxiliaryDataPath.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_AuxiliaryDataPath.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_AuxiliaryDataPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_53.addWidget(self.Label_DAT_VITS_AuxiliaryDataPath, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_AuxiliaryDataPath = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.HorizontalSpacer_DAT_VITS_AuxiliaryDataPath, 0, 1, 1, 1)

        self.Button_DAT_VITS_AuxiliaryDataPath_Undo = QPushButton(self.Frame_DAT_VITS_AuxiliaryDataPath)
        self.Button_DAT_VITS_AuxiliaryDataPath_Undo.setObjectName(u"Button_DAT_VITS_AuxiliaryDataPath_Undo")
        self.Button_DAT_VITS_AuxiliaryDataPath_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_AuxiliaryDataPath_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_AuxiliaryDataPath_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_53.addWidget(self.Button_DAT_VITS_AuxiliaryDataPath_Undo, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_AuxiliaryDataPath = LineEditBase(self.Frame_DAT_VITS_AuxiliaryDataPath)
        self.LineEdit_DAT_VITS_AuxiliaryDataPath.setObjectName(u"LineEdit_DAT_VITS_AuxiliaryDataPath")
        self.LineEdit_DAT_VITS_AuxiliaryDataPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_53.addWidget(self.LineEdit_DAT_VITS_AuxiliaryDataPath, 1, 0, 1, 3)


        self.verticalLayout_30.addWidget(self.Frame_DAT_VITS_AuxiliaryDataPath)


        self.verticalLayout_115.addWidget(self.Frame_DAT_VITS_VITSParams_BasicSettings)

        self.CheckBox_DAT_VITS_VITSParams_Toggle_AdvanceSettings = QCheckBox(self.GroupBox_DAT_VITS_VITSParams)
        self.CheckBox_DAT_VITS_VITSParams_Toggle_AdvanceSettings.setObjectName(u"CheckBox_DAT_VITS_VITSParams_Toggle_AdvanceSettings")
        self.CheckBox_DAT_VITS_VITSParams_Toggle_AdvanceSettings.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	font-weight: 630;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding-top: 9px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"    background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: transparent;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/RightCaret.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/DownCaret.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_115.addWidget(self.CheckBox_DAT_VITS_VITSParams_Toggle_AdvanceSettings)

        self.Frame_DAT_VITS_VITSParams_AdvanceSettings = QFrame(self.GroupBox_DAT_VITS_VITSParams)
        self.Frame_DAT_VITS_VITSParams_AdvanceSettings.setObjectName(u"Frame_DAT_VITS_VITSParams_AdvanceSettings")
        self.Frame_DAT_VITS_VITSParams_AdvanceSettings.setFrameShape(QFrame.StyledPanel)
        self.Frame_DAT_VITS_VITSParams_AdvanceSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.Frame_DAT_VITS_VITSParams_AdvanceSettings)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_TrainRatio = QFrame(self.Frame_DAT_VITS_VITSParams_AdvanceSettings)
        self.Frame_DAT_VITS_TrainRatio.setObjectName(u"Frame_DAT_VITS_TrainRatio")
        self.Frame_DAT_VITS_TrainRatio.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_TrainRatio.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_49 = QGridLayout(self.Frame_DAT_VITS_TrainRatio)
        self.gridLayout_49.setSpacing(12)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_TrainRatio = QLabel(self.Frame_DAT_VITS_TrainRatio)
        self.Label_DAT_VITS_TrainRatio.setObjectName(u"Label_DAT_VITS_TrainRatio")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_TrainRatio.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_TrainRatio.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_TrainRatio.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_49.addWidget(self.Label_DAT_VITS_TrainRatio, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_TrainRatio = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_49.addItem(self.HorizontalSpacer_DAT_VITS_TrainRatio, 0, 1, 1, 1)

        self.Button_DAT_VITS_TrainRatio_Undo = QPushButton(self.Frame_DAT_VITS_TrainRatio)
        self.Button_DAT_VITS_TrainRatio_Undo.setObjectName(u"Button_DAT_VITS_TrainRatio_Undo")
        self.Button_DAT_VITS_TrainRatio_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_TrainRatio_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_TrainRatio_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_49.addWidget(self.Button_DAT_VITS_TrainRatio_Undo, 0, 2, 1, 1)

        self.DoubleSpinBox_DAT_VITS_TrainRatio = QDoubleSpinBox(self.Frame_DAT_VITS_TrainRatio)
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setObjectName(u"DoubleSpinBox_DAT_VITS_TrainRatio")
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setEnabled(True)
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setStyleSheet(u"QDoubleSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	/*height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::down-arr"
                        "ow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setMaximum(999999.000000000000000)

        self.gridLayout_49.addWidget(self.DoubleSpinBox_DAT_VITS_TrainRatio, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_TrainRatio)

        self.Frame_DAT_VITS_SampleRate = QFrame(self.Frame_DAT_VITS_VITSParams_AdvanceSettings)
        self.Frame_DAT_VITS_SampleRate.setObjectName(u"Frame_DAT_VITS_SampleRate")
        self.Frame_DAT_VITS_SampleRate.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SampleRate.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_50 = QGridLayout(self.Frame_DAT_VITS_SampleRate)
        self.gridLayout_50.setSpacing(12)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_SampleRate = QLabel(self.Frame_DAT_VITS_SampleRate)
        self.Label_DAT_VITS_SampleRate.setObjectName(u"Label_DAT_VITS_SampleRate")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_SampleRate.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_SampleRate.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_SampleRate.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_50.addWidget(self.Label_DAT_VITS_SampleRate, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_SampleRate = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_50.addItem(self.HorizontalSpacer_DAT_VITS_SampleRate, 0, 1, 1, 1)

        self.Button_DAT_VITS_SampleRate_Undo = QPushButton(self.Frame_DAT_VITS_SampleRate)
        self.Button_DAT_VITS_SampleRate_Undo.setObjectName(u"Button_DAT_VITS_SampleRate_Undo")
        self.Button_DAT_VITS_SampleRate_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleRate_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleRate_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_50.addWidget(self.Button_DAT_VITS_SampleRate_Undo, 0, 2, 1, 1)

        self.ComboBox_DAT_VITS_SampleRate = QComboBox(self.Frame_DAT_VITS_SampleRate)
        self.ComboBox_DAT_VITS_SampleRate.setObjectName(u"ComboBox_DAT_VITS_SampleRate")
        self.ComboBox_DAT_VITS_SampleRate.setMinimumSize(QSize(0, 27))
        self.ComboBox_DAT_VITS_SampleRate.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QComboBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	/*width: 12px;\n"
"	height: 12px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	margin-right: 6px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"	border-image: url(:/ComboBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"\n"
"QCom"
                        "boBox QAbstractItemView::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
""
                        "	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:vertical, QComboBox QAbstractScrollArea QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	borde"
                        "r-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:horizontal, QComboBox QAbstractScrollArea QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	"
                        "border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_50.addWidget(self.ComboBox_DAT_VITS_SampleRate, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_SampleRate)

        self.Frame_DAT_VITS_SampleWidth = QFrame(self.Frame_DAT_VITS_VITSParams_AdvanceSettings)
        self.Frame_DAT_VITS_SampleWidth.setObjectName(u"Frame_DAT_VITS_SampleWidth")
        self.Frame_DAT_VITS_SampleWidth.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SampleWidth.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_51 = QGridLayout(self.Frame_DAT_VITS_SampleWidth)
        self.gridLayout_51.setSpacing(12)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_SampleWidth = QLabel(self.Frame_DAT_VITS_SampleWidth)
        self.Label_DAT_VITS_SampleWidth.setObjectName(u"Label_DAT_VITS_SampleWidth")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_SampleWidth.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_SampleWidth.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_SampleWidth.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_51.addWidget(self.Label_DAT_VITS_SampleWidth, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_SampleWidth = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_51.addItem(self.HorizontalSpacer_DAT_VITS_SampleWidth, 0, 1, 1, 1)

        self.Button_DAT_VITS_SampleWidth_Undo = QPushButton(self.Frame_DAT_VITS_SampleWidth)
        self.Button_DAT_VITS_SampleWidth_Undo.setObjectName(u"Button_DAT_VITS_SampleWidth_Undo")
        self.Button_DAT_VITS_SampleWidth_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleWidth_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleWidth_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_51.addWidget(self.Button_DAT_VITS_SampleWidth_Undo, 0, 2, 1, 1)

        self.ComboBox_DAT_VITS_SampleWidth = QComboBox(self.Frame_DAT_VITS_SampleWidth)
        self.ComboBox_DAT_VITS_SampleWidth.setObjectName(u"ComboBox_DAT_VITS_SampleWidth")
        self.ComboBox_DAT_VITS_SampleWidth.setMinimumSize(QSize(0, 27))
        self.ComboBox_DAT_VITS_SampleWidth.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QComboBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	/*width: 12px;\n"
"	height: 12px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	margin-right: 6px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"	border-image: url(:/ComboBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"\n"
"QCom"
                        "boBox QAbstractItemView::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
""
                        "	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:vertical, QComboBox QAbstractScrollArea QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	borde"
                        "r-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:horizontal, QComboBox QAbstractScrollArea QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	"
                        "border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_51.addWidget(self.ComboBox_DAT_VITS_SampleWidth, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_SampleWidth)

        self.Frame_DAT_VITS_ToMono = QFrame(self.Frame_DAT_VITS_VITSParams_AdvanceSettings)
        self.Frame_DAT_VITS_ToMono.setObjectName(u"Frame_DAT_VITS_ToMono")
        self.Frame_DAT_VITS_ToMono.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_ToMono.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_52 = QGridLayout(self.Frame_DAT_VITS_ToMono)
        self.gridLayout_52.setSpacing(12)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_ToMono = QLabel(self.Frame_DAT_VITS_ToMono)
        self.Label_DAT_VITS_ToMono.setObjectName(u"Label_DAT_VITS_ToMono")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_ToMono.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_ToMono.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_ToMono.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_52.addWidget(self.Label_DAT_VITS_ToMono, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_ToMono = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_52.addItem(self.HorizontalSpacer_DAT_VITS_ToMono, 0, 1, 1, 1)

        self.Button_DAT_VITS_ToMono_Undo = QPushButton(self.Frame_DAT_VITS_ToMono)
        self.Button_DAT_VITS_ToMono_Undo.setObjectName(u"Button_DAT_VITS_ToMono_Undo")
        self.Button_DAT_VITS_ToMono_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_ToMono_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_ToMono_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_52.addWidget(self.Button_DAT_VITS_ToMono_Undo, 0, 2, 1, 1)

        self.CheckBox_DAT_VITS_ToMono = QCheckBox(self.Frame_DAT_VITS_ToMono)
        self.CheckBox_DAT_VITS_ToMono.setObjectName(u"CheckBox_DAT_VITS_ToMono")
        self.CheckBox_DAT_VITS_ToMono.setMinimumSize(QSize(0, 27))
        self.CheckBox_DAT_VITS_ToMono.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_52.addWidget(self.CheckBox_DAT_VITS_ToMono, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_ToMono)


        self.verticalLayout_115.addWidget(self.Frame_DAT_VITS_VITSParams_AdvanceSettings)


        self.verticalLayout_36.addWidget(self.GroupBox_DAT_VITS_VITSParams)

        self.GroupBox_DAT_VITS_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.GroupBox_DAT_VITS_OutputParams.setObjectName(u"GroupBox_DAT_VITS_OutputParams")
        self.GroupBox_DAT_VITS_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_128 = QVBoxLayout(self.GroupBox_DAT_VITS_OutputParams)
        self.verticalLayout_128.setSpacing(0)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_VITS_OutputParams_BasicSettings = QFrame(self.GroupBox_DAT_VITS_OutputParams)
        self.Frame_DAT_VITS_OutputParams_BasicSettings.setObjectName(u"Frame_DAT_VITS_OutputParams_BasicSettings")
        self.verticalLayout_31 = QVBoxLayout(self.Frame_DAT_VITS_OutputParams_BasicSettings)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_ToStandaloneForm = QFrame(self.Frame_DAT_VITS_OutputParams_BasicSettings)
        self.Frame_DAT_VITS_ToStandaloneForm.setObjectName(u"Frame_DAT_VITS_ToStandaloneForm")
        self.Frame_DAT_VITS_ToStandaloneForm.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_ToStandaloneForm.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_78 = QGridLayout(self.Frame_DAT_VITS_ToStandaloneForm)
        self.gridLayout_78.setSpacing(12)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.gridLayout_78.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_ToStandaloneForm = QLabel(self.Frame_DAT_VITS_ToStandaloneForm)
        self.Label_DAT_VITS_ToStandaloneForm.setObjectName(u"Label_DAT_VITS_ToStandaloneForm")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_ToStandaloneForm.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_ToStandaloneForm.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_ToStandaloneForm.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_78.addWidget(self.Label_DAT_VITS_ToStandaloneForm, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_ToStandaloneForm = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_78.addItem(self.HorizontalSpacer_DAT_VITS_ToStandaloneForm, 0, 1, 1, 1)

        self.Button_DAT_VITS_ToStandaloneForm_Undo = QPushButton(self.Frame_DAT_VITS_ToStandaloneForm)
        self.Button_DAT_VITS_ToStandaloneForm_Undo.setObjectName(u"Button_DAT_VITS_ToStandaloneForm_Undo")
        self.Button_DAT_VITS_ToStandaloneForm_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_ToStandaloneForm_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_ToStandaloneForm_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_78.addWidget(self.Button_DAT_VITS_ToStandaloneForm_Undo, 0, 2, 1, 1)

        self.CheckBox_DAT_VITS_ToStandaloneForm = QCheckBox(self.Frame_DAT_VITS_ToStandaloneForm)
        self.CheckBox_DAT_VITS_ToStandaloneForm.setObjectName(u"CheckBox_DAT_VITS_ToStandaloneForm")
        self.CheckBox_DAT_VITS_ToStandaloneForm.setMinimumSize(QSize(0, 27))
        self.CheckBox_DAT_VITS_ToStandaloneForm.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_78.addWidget(self.CheckBox_DAT_VITS_ToStandaloneForm, 1, 0, 1, 3)


        self.verticalLayout_31.addWidget(self.Frame_DAT_VITS_ToStandaloneForm)

        self.Frame_DAT_VITS_WAVDirSplit = QFrame(self.Frame_DAT_VITS_OutputParams_BasicSettings)
        self.Frame_DAT_VITS_WAVDirSplit.setObjectName(u"Frame_DAT_VITS_WAVDirSplit")
        self.Frame_DAT_VITS_WAVDirSplit.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_WAVDirSplit.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_54 = QGridLayout(self.Frame_DAT_VITS_WAVDirSplit)
        self.gridLayout_54.setSpacing(12)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_WAVDirSplit = QLabel(self.Frame_DAT_VITS_WAVDirSplit)
        self.Label_DAT_VITS_WAVDirSplit.setObjectName(u"Label_DAT_VITS_WAVDirSplit")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_WAVDirSplit.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_WAVDirSplit.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_WAVDirSplit.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_54.addWidget(self.Label_DAT_VITS_WAVDirSplit, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_WAVDirSplit = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_54.addItem(self.HorizontalSpacer_DAT_VITS_WAVDirSplit, 0, 1, 1, 1)

        self.Button_DAT_VITS_WAVDirSplit_Undo = QPushButton(self.Frame_DAT_VITS_WAVDirSplit)
        self.Button_DAT_VITS_WAVDirSplit_Undo.setObjectName(u"Button_DAT_VITS_WAVDirSplit_Undo")
        self.Button_DAT_VITS_WAVDirSplit_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_WAVDirSplit_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_WAVDirSplit_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_54.addWidget(self.Button_DAT_VITS_WAVDirSplit_Undo, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_WAVDirSplit = LineEditBase(self.Frame_DAT_VITS_WAVDirSplit)
        self.LineEdit_DAT_VITS_WAVDirSplit.setObjectName(u"LineEdit_DAT_VITS_WAVDirSplit")
        self.LineEdit_DAT_VITS_WAVDirSplit.setMinimumSize(QSize(0, 27))

        self.gridLayout_54.addWidget(self.LineEdit_DAT_VITS_WAVDirSplit, 1, 0, 1, 3)


        self.verticalLayout_31.addWidget(self.Frame_DAT_VITS_WAVDirSplit)

        self.Frame_DAT_VITS_FileListPathTraining = QFrame(self.Frame_DAT_VITS_OutputParams_BasicSettings)
        self.Frame_DAT_VITS_FileListPathTraining.setObjectName(u"Frame_DAT_VITS_FileListPathTraining")
        self.Frame_DAT_VITS_FileListPathTraining.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_FileListPathTraining.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_55 = QGridLayout(self.Frame_DAT_VITS_FileListPathTraining)
        self.gridLayout_55.setSpacing(12)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(21, 12, 21, 12)
        self.Button_DAT_VITS_FileListPathTraining_Undo = QPushButton(self.Frame_DAT_VITS_FileListPathTraining)
        self.Button_DAT_VITS_FileListPathTraining_Undo.setObjectName(u"Button_DAT_VITS_FileListPathTraining_Undo")
        self.Button_DAT_VITS_FileListPathTraining_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListPathTraining_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListPathTraining_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_55.addWidget(self.Button_DAT_VITS_FileListPathTraining_Undo, 0, 2, 1, 1)

        self.Label_DAT_VITS_FileListPathTraining = QLabel(self.Frame_DAT_VITS_FileListPathTraining)
        self.Label_DAT_VITS_FileListPathTraining.setObjectName(u"Label_DAT_VITS_FileListPathTraining")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_FileListPathTraining.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_FileListPathTraining.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_FileListPathTraining.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_55.addWidget(self.Label_DAT_VITS_FileListPathTraining, 0, 0, 1, 1)

        self.LineEdit_DAT_VITS_FileListPathTraining = LineEditBase(self.Frame_DAT_VITS_FileListPathTraining)
        self.LineEdit_DAT_VITS_FileListPathTraining.setObjectName(u"LineEdit_DAT_VITS_FileListPathTraining")
        self.LineEdit_DAT_VITS_FileListPathTraining.setMinimumSize(QSize(0, 27))

        self.gridLayout_55.addWidget(self.LineEdit_DAT_VITS_FileListPathTraining, 1, 0, 1, 3)

        self.HorizontalSpacer_DAT_VITS_FileListPathTraining = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_55.addItem(self.HorizontalSpacer_DAT_VITS_FileListPathTraining, 0, 1, 1, 1)


        self.verticalLayout_31.addWidget(self.Frame_DAT_VITS_FileListPathTraining)

        self.Frame_DAT_VITS_FileListPathValidation = QFrame(self.Frame_DAT_VITS_OutputParams_BasicSettings)
        self.Frame_DAT_VITS_FileListPathValidation.setObjectName(u"Frame_DAT_VITS_FileListPathValidation")
        self.Frame_DAT_VITS_FileListPathValidation.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_FileListPathValidation.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_56 = QGridLayout(self.Frame_DAT_VITS_FileListPathValidation)
        self.gridLayout_56.setSpacing(12)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_FileListPathValidation = QLabel(self.Frame_DAT_VITS_FileListPathValidation)
        self.Label_DAT_VITS_FileListPathValidation.setObjectName(u"Label_DAT_VITS_FileListPathValidation")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_FileListPathValidation.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_FileListPathValidation.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_FileListPathValidation.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_56.addWidget(self.Label_DAT_VITS_FileListPathValidation, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_FileListPathValidation = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.HorizontalSpacer_DAT_VITS_FileListPathValidation, 0, 1, 1, 1)

        self.Button_DAT_VITS_FileListPathValidation_Undo = QPushButton(self.Frame_DAT_VITS_FileListPathValidation)
        self.Button_DAT_VITS_FileListPathValidation_Undo.setObjectName(u"Button_DAT_VITS_FileListPathValidation_Undo")
        self.Button_DAT_VITS_FileListPathValidation_Undo.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListPathValidation_Undo.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListPathValidation_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_56.addWidget(self.Button_DAT_VITS_FileListPathValidation_Undo, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_FileListPathValidation = LineEditBase(self.Frame_DAT_VITS_FileListPathValidation)
        self.LineEdit_DAT_VITS_FileListPathValidation.setObjectName(u"LineEdit_DAT_VITS_FileListPathValidation")
        self.LineEdit_DAT_VITS_FileListPathValidation.setMinimumSize(QSize(0, 27))

        self.gridLayout_56.addWidget(self.LineEdit_DAT_VITS_FileListPathValidation, 1, 0, 1, 3)


        self.verticalLayout_31.addWidget(self.Frame_DAT_VITS_FileListPathValidation)


        self.verticalLayout_128.addWidget(self.Frame_DAT_VITS_OutputParams_BasicSettings)


        self.verticalLayout_36.addWidget(self.GroupBox_DAT_VITS_OutputParams)

        self.VerticalSpacer_DAT_VITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.VerticalSpacer_DAT_VITS)

        self.ScrollArea_Middle_DAT_VITS.setWidget(self.ScrollArea_Middle_WidgetContents_DAT_VITS)

        self.gridLayout_8.addWidget(self.ScrollArea_Middle_DAT_VITS, 0, 1, 1, 1)

        self.Widget_Right_DAT_VITS = QWidget(self.Subpage_DAT_VITS)
        self.Widget_Right_DAT_VITS.setObjectName(u"Widget_Right_DAT_VITS")
        self.Widget_Right_DAT_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout_16 = QGridLayout(self.Widget_Right_DAT_VITS)
        self.gridLayout_16.setSpacing(12)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_DAT_VITS = QTextBrowser(self.Widget_Right_DAT_VITS)
        self.TextBrowser_Params_DAT_VITS.setObjectName(u"TextBrowser_Params_DAT_VITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_DAT_VITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_DAT_VITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_DAT_VITS.setStyleSheet(u"QTextBrowser {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	bord"
                        "er-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px"
                        ";\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_16.addWidget(self.TextBrowser_Params_DAT_VITS, 0, 0, 1, 2)

        self.Button_CheckOutput_DAT_VITS = QPushButton(self.Widget_Right_DAT_VITS)
        self.Button_CheckOutput_DAT_VITS.setObjectName(u"Button_CheckOutput_DAT_VITS")
        self.Button_CheckOutput_DAT_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 9.9px;\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_16.addWidget(self.Button_CheckOutput_DAT_VITS, 1, 0, 1, 2)


        self.gridLayout_8.addWidget(self.Widget_Right_DAT_VITS, 0, 2, 1, 1)

        self.ProgressBar_DAT_VITS = QProgressBar(self.Subpage_DAT_VITS)
        self.ProgressBar_DAT_VITS.setObjectName(u"ProgressBar_DAT_VITS")
        self.ProgressBar_DAT_VITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_DAT_VITS.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(60, 60, 60);\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(60, 60, 60), stop:1  rgb(123, 123, 123));\n"
"}")
        self.ProgressBar_DAT_VITS.setValue(0)
        self.ProgressBar_DAT_VITS.setTextVisible(False)
        self.horizontalLayout_37 = QHBoxLayout(self.ProgressBar_DAT_VITS)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_DAT_VITS = QStackedWidget(self.ProgressBar_DAT_VITS)
        self.StackedWidget_DAT_VITS.setObjectName(u"StackedWidget_DAT_VITS")
        self.StackedWidget_DAT_VITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_DAT_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_DAT_VITS_Execute = QWidget()
        self.Page_DAT_VITS_Execute.setObjectName(u"Page_DAT_VITS_Execute")
        self.verticalLayout_92 = QVBoxLayout(self.Page_DAT_VITS_Execute)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.Button_DAT_VITS_Execute = QPushButton(self.Page_DAT_VITS_Execute)
        self.Button_DAT_VITS_Execute.setObjectName(u"Button_DAT_VITS_Execute")
        sizePolicy3.setHeightForWidth(self.Button_DAT_VITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_DAT_VITS_Execute.setSizePolicy(sizePolicy3)
        self.Button_DAT_VITS_Execute.setMinimumSize(QSize(0, 30))
        self.Button_DAT_VITS_Execute.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_92.addWidget(self.Button_DAT_VITS_Execute)

        self.StackedWidget_DAT_VITS.addWidget(self.Page_DAT_VITS_Execute)
        self.Page_DAT_VITS_Terminate = QWidget()
        self.Page_DAT_VITS_Terminate.setObjectName(u"Page_DAT_VITS_Terminate")
        self.verticalLayout_93 = QVBoxLayout(self.Page_DAT_VITS_Terminate)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.Button_DAT_VITS_Terminate = QPushButton(self.Page_DAT_VITS_Terminate)
        self.Button_DAT_VITS_Terminate.setObjectName(u"Button_DAT_VITS_Terminate")
        sizePolicy3.setHeightForWidth(self.Button_DAT_VITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_DAT_VITS_Terminate.setSizePolicy(sizePolicy3)
        self.Button_DAT_VITS_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_DAT_VITS_Terminate.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_93.addWidget(self.Button_DAT_VITS_Terminate)

        self.StackedWidget_DAT_VITS.addWidget(self.Page_DAT_VITS_Terminate)

        self.horizontalLayout_37.addWidget(self.StackedWidget_DAT_VITS)


        self.gridLayout_8.addWidget(self.ProgressBar_DAT_VITS, 1, 0, 1, 3)

        self.gridLayout_8.setColumnStretch(0, 3)
        self.gridLayout_8.setColumnStretch(1, 10)
        self.gridLayout_8.setColumnStretch(2, 7)
        self.StackedWidget_Pages_Dataset.addWidget(self.Subpage_DAT_VITS)

        self.verticalLayout_39.addWidget(self.StackedWidget_Pages_Dataset)

        self.StackedWidget_Pages.addWidget(self.Page_Dataset)
        self.Page_Train = QWidget()
        self.Page_Train.setObjectName(u"Page_Train")
        self.verticalLayout_43 = QVBoxLayout(self.Page_Train)
        self.verticalLayout_43.setSpacing(21)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(21, 12, 21, 12)
        self.Frame_Train_Top = QFrame(self.Page_Train)
        self.Frame_Train_Top.setObjectName(u"Frame_Train_Top")
        self.Frame_Train_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Train_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_72 = QHBoxLayout(self.Frame_Train_Top)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_VoiceTrainer_Title = QToolButton(self.Frame_Train_Top)
        self.ToolButton_VoiceTrainer_Title.setObjectName(u"ToolButton_VoiceTrainer_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_VoiceTrainer_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_VoiceTrainer_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_VoiceTrainer_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color:"
                        " rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_72.addWidget(self.ToolButton_VoiceTrainer_Title)

        self.Frame_Train_Title_Spacer = QLabel(self.Frame_Train_Top)
        self.Frame_Train_Title_Spacer.setObjectName(u"Frame_Train_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_Train_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Train_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_Train_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;*/\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_72.addWidget(self.Frame_Train_Title_Spacer)


        self.verticalLayout_43.addWidget(self.Frame_Train_Top)

        self.StackedWidget_Pages_Train = QStackedWidget(self.Page_Train)
        self.StackedWidget_Pages_Train.setObjectName(u"StackedWidget_Pages_Train")
        self.StackedWidget_Pages_Train.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*\n"
"QTabWidget {\n"
"	background-color: transparent;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"}\n"
"QTabWidget::pane {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"	font-size: 18px;\n"
"	font-weight: 420;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 12px;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:selected {\n"
"	color: rgba(255, 255, 255, 255);\n"
"}\n"
"QTabBar::tab:hover:!selected {\n"
"}\n"
"\n"
"\n"
"QTabBar QToolButton {\n"
"}\n"
"QTabBar QToolButton:hover {\n"
"}\n"
"*/")
        self.Subpage_Train_VITS = QWidget()
        self.Subpage_Train_VITS.setObjectName(u"Subpage_Train_VITS")
        self.gridLayout_22 = QGridLayout(self.Subpage_Train_VITS)
        self.gridLayout_22.setSpacing(12)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.Widget_Right_Train_VITS = QWidget(self.Subpage_Train_VITS)
        self.Widget_Right_Train_VITS.setObjectName(u"Widget_Right_Train_VITS")
        self.Widget_Right_Train_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout = QGridLayout(self.Widget_Right_Train_VITS)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.Button_RunTensorboard_Train_VITS = QPushButton(self.Widget_Right_Train_VITS)
        self.Button_RunTensorboard_Train_VITS.setObjectName(u"Button_RunTensorboard_Train_VITS")
        self.Button_RunTensorboard_Train_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 9.9px;\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout.addWidget(self.Button_RunTensorboard_Train_VITS, 1, 0, 1, 2)

        self.TextBrowser_Params_Train_VITS = QTextBrowser(self.Widget_Right_Train_VITS)
        self.TextBrowser_Params_Train_VITS.setObjectName(u"TextBrowser_Params_Train_VITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Train_VITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Train_VITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Train_VITS.setStyleSheet(u"QTextBrowser {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	bord"
                        "er-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px"
                        ";\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout.addWidget(self.TextBrowser_Params_Train_VITS, 0, 0, 1, 2)

        self.Button_CheckOutput_Train_VITS = QPushButton(self.Widget_Right_Train_VITS)
        self.Button_CheckOutput_Train_VITS.setObjectName(u"Button_CheckOutput_Train_VITS")
        self.Button_CheckOutput_Train_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 9.9px;\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout.addWidget(self.Button_CheckOutput_Train_VITS, 2, 0, 1, 2)


        self.gridLayout_22.addWidget(self.Widget_Right_Train_VITS, 0, 2, 1, 1)

        self.Widget_Left_Train_VITS = QWidget(self.Subpage_Train_VITS)
        self.Widget_Left_Train_VITS.setObjectName(u"Widget_Left_Train_VITS")
        self.Widget_Left_Train_VITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_Train_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.Widget_Left_Train_VITS)
        self.verticalLayout_10.setSpacing(12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Train_VITS = QTreeWidget(self.Widget_Left_Train_VITS)
        __qtreewidgetitem4 = QTreeWidgetItem(self.TreeWidget_Catalogue_Train_VITS)
        QTreeWidgetItem(__qtreewidgetitem4)
        self.TreeWidget_Catalogue_Train_VITS.setObjectName(u"TreeWidget_Catalogue_Train_VITS")
        self.TreeWidget_Catalogue_Train_VITS.setStyleSheet(u"QTreeView {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"	background-color: transparent;\n"
"	padding: 2.4px;\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"QTreeView::item:selected {\n"
"    background-color: ;\n"
"}\n"
"\n"
"QTreeView::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeView::branch:open:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeView::branch:closed:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:adjoins-item {\n"
"    background-color: ;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: rgba(45, 45, 45, 135);\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"	background-color: r"
                        "gba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(90, 90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}")

        self.verticalLayout_10.addWidget(self.TreeWidget_Catalogue_Train_VITS)


        self.gridLayout_22.addWidget(self.Widget_Left_Train_VITS, 0, 0, 1, 1)

        self.ProgressBar_Train_VITS = QProgressBar(self.Subpage_Train_VITS)
        self.ProgressBar_Train_VITS.setObjectName(u"ProgressBar_Train_VITS")
        self.ProgressBar_Train_VITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Train_VITS.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(60, 60, 60);\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(60, 60, 60), stop:1  rgb(123, 123, 123));\n"
"}")
        self.ProgressBar_Train_VITS.setValue(0)
        self.ProgressBar_Train_VITS.setTextVisible(False)
        self.horizontalLayout_39 = QHBoxLayout(self.ProgressBar_Train_VITS)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Train_VITS = QStackedWidget(self.ProgressBar_Train_VITS)
        self.StackedWidget_Train_VITS.setObjectName(u"StackedWidget_Train_VITS")
        self.StackedWidget_Train_VITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_Train_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_Train_VITS_Execute = QWidget()
        self.Page_Train_VITS_Execute.setObjectName(u"Page_Train_VITS_Execute")
        self.verticalLayout_94 = QVBoxLayout(self.Page_Train_VITS_Execute)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.Button_Train_VITS_Execute = QPushButton(self.Page_Train_VITS_Execute)
        self.Button_Train_VITS_Execute.setObjectName(u"Button_Train_VITS_Execute")
        sizePolicy3.setHeightForWidth(self.Button_Train_VITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Train_VITS_Execute.setSizePolicy(sizePolicy3)
        self.Button_Train_VITS_Execute.setMinimumSize(QSize(0, 30))
        self.Button_Train_VITS_Execute.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_94.addWidget(self.Button_Train_VITS_Execute)

        self.StackedWidget_Train_VITS.addWidget(self.Page_Train_VITS_Execute)
        self.Page_Train_VITS_Terminate = QWidget()
        self.Page_Train_VITS_Terminate.setObjectName(u"Page_Train_VITS_Terminate")
        self.verticalLayout_95 = QVBoxLayout(self.Page_Train_VITS_Terminate)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.Button_Train_VITS_Terminate = QPushButton(self.Page_Train_VITS_Terminate)
        self.Button_Train_VITS_Terminate.setObjectName(u"Button_Train_VITS_Terminate")
        sizePolicy3.setHeightForWidth(self.Button_Train_VITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Train_VITS_Terminate.setSizePolicy(sizePolicy3)
        self.Button_Train_VITS_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_Train_VITS_Terminate.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_95.addWidget(self.Button_Train_VITS_Terminate)

        self.StackedWidget_Train_VITS.addWidget(self.Page_Train_VITS_Terminate)

        self.horizontalLayout_39.addWidget(self.StackedWidget_Train_VITS)


        self.gridLayout_22.addWidget(self.ProgressBar_Train_VITS, 1, 0, 1, 3)

        self.ScrollArea_Middle_Train_VITS = QScrollArea(self.Subpage_Train_VITS)
        self.ScrollArea_Middle_Train_VITS.setObjectName(u"ScrollArea_Middle_Train_VITS")
        self.ScrollArea_Middle_Train_VITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_Train_VITS.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollArea:hover {\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	"
                        "height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	borde"
                        "r-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")
        self.ScrollArea_Middle_Train_VITS.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Train_VITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_Train_VITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_Train_VITS.setObjectName(u"ScrollArea_Middle_WidgetContents_Train_VITS")
        self.ScrollArea_Middle_WidgetContents_Train_VITS.setGeometry(QRect(0, 0, 591, 1566))
        self.verticalLayout_28 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.verticalLayout_28.setSpacing(12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_Train_VITS_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.GroupBox_Train_VITS_InputParams.setObjectName(u"GroupBox_Train_VITS_InputParams")
        self.GroupBox_Train_VITS_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_116 = QVBoxLayout(self.GroupBox_Train_VITS_InputParams)
        self.verticalLayout_116.setSpacing(0)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 12, 0, 12)
        self.Frame_Train_VITS_InputParams_BasicSettings = QFrame(self.GroupBox_Train_VITS_InputParams)
        self.Frame_Train_VITS_InputParams_BasicSettings.setObjectName(u"Frame_Train_VITS_InputParams_BasicSettings")
        self.verticalLayout_18 = QVBoxLayout(self.Frame_Train_VITS_InputParams_BasicSettings)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_FileListPathTraining = QFrame(self.Frame_Train_VITS_InputParams_BasicSettings)
        self.Frame_Train_VITS_FileListPathTraining.setObjectName(u"Frame_Train_VITS_FileListPathTraining")
        self.Frame_Train_VITS_FileListPathTraining.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_FileListPathTraining.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_57 = QGridLayout(self.Frame_Train_VITS_FileListPathTraining)
        self.gridLayout_57.setSpacing(12)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_FileListPathTraining = QLabel(self.Frame_Train_VITS_FileListPathTraining)
        self.Label_Train_VITS_FileListPathTraining.setObjectName(u"Label_Train_VITS_FileListPathTraining")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_FileListPathTraining.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_FileListPathTraining.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_FileListPathTraining.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_57.addWidget(self.Label_Train_VITS_FileListPathTraining, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_FileListPathTraining = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_57.addItem(self.HorizontalSpacer_Train_VITS_FileListPathTraining, 0, 1, 1, 1)

        self.Button_Train_VITS_FileListPathTraining_Undo = QPushButton(self.Frame_Train_VITS_FileListPathTraining)
        self.Button_Train_VITS_FileListPathTraining_Undo.setObjectName(u"Button_Train_VITS_FileListPathTraining_Undo")
        self.Button_Train_VITS_FileListPathTraining_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathTraining_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathTraining_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_57.addWidget(self.Button_Train_VITS_FileListPathTraining_Undo, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_FileListPathTraining = LineEditBase(self.Frame_Train_VITS_FileListPathTraining)
        self.LineEdit_Train_VITS_FileListPathTraining.setObjectName(u"LineEdit_Train_VITS_FileListPathTraining")
        self.LineEdit_Train_VITS_FileListPathTraining.setMinimumSize(QSize(0, 27))

        self.gridLayout_57.addWidget(self.LineEdit_Train_VITS_FileListPathTraining, 1, 0, 1, 3)


        self.verticalLayout_18.addWidget(self.Frame_Train_VITS_FileListPathTraining)

        self.Frame_Train_VITS_FileListPathValidation = QFrame(self.Frame_Train_VITS_InputParams_BasicSettings)
        self.Frame_Train_VITS_FileListPathValidation.setObjectName(u"Frame_Train_VITS_FileListPathValidation")
        self.Frame_Train_VITS_FileListPathValidation.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_FileListPathValidation.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_58 = QGridLayout(self.Frame_Train_VITS_FileListPathValidation)
        self.gridLayout_58.setSpacing(12)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_FileListPathValidation = QLabel(self.Frame_Train_VITS_FileListPathValidation)
        self.Label_Train_VITS_FileListPathValidation.setObjectName(u"Label_Train_VITS_FileListPathValidation")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_FileListPathValidation.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_FileListPathValidation.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_FileListPathValidation.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_58.addWidget(self.Label_Train_VITS_FileListPathValidation, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_FileListPathValidation = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_58.addItem(self.HorizontalSpacer_Train_VITS_FileListPathValidation, 0, 1, 1, 1)

        self.Button_Train_VITS_FileListPathValidation_Undo = QPushButton(self.Frame_Train_VITS_FileListPathValidation)
        self.Button_Train_VITS_FileListPathValidation_Undo.setObjectName(u"Button_Train_VITS_FileListPathValidation_Undo")
        self.Button_Train_VITS_FileListPathValidation_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathValidation_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathValidation_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_58.addWidget(self.Button_Train_VITS_FileListPathValidation_Undo, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_FileListPathValidation = LineEditBase(self.Frame_Train_VITS_FileListPathValidation)
        self.LineEdit_Train_VITS_FileListPathValidation.setObjectName(u"LineEdit_Train_VITS_FileListPathValidation")
        self.LineEdit_Train_VITS_FileListPathValidation.setMinimumSize(QSize(0, 27))

        self.gridLayout_58.addWidget(self.LineEdit_Train_VITS_FileListPathValidation, 1, 0, 1, 3)


        self.verticalLayout_18.addWidget(self.Frame_Train_VITS_FileListPathValidation)


        self.verticalLayout_116.addWidget(self.Frame_Train_VITS_InputParams_BasicSettings)


        self.verticalLayout_28.addWidget(self.GroupBox_Train_VITS_InputParams)

        self.GroupBox_Train_VITS_VITSParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.GroupBox_Train_VITS_VITSParams.setObjectName(u"GroupBox_Train_VITS_VITSParams")
        self.GroupBox_Train_VITS_VITSParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_114 = QVBoxLayout(self.GroupBox_Train_VITS_VITSParams)
        self.verticalLayout_114.setSpacing(0)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 12, 0, 12)
        self.Frame_Train_VITS_VITSParams_BasicSettings = QFrame(self.GroupBox_Train_VITS_VITSParams)
        self.Frame_Train_VITS_VITSParams_BasicSettings.setObjectName(u"Frame_Train_VITS_VITSParams_BasicSettings")
        self.verticalLayout_17 = QVBoxLayout(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_Epochs = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_Epochs.setObjectName(u"Frame_Train_VITS_Epochs")
        self.Frame_Train_VITS_Epochs.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Epochs.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_59 = QGridLayout(self.Frame_Train_VITS_Epochs)
        self.gridLayout_59.setSpacing(12)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Epochs = QLabel(self.Frame_Train_VITS_Epochs)
        self.Label_Train_VITS_Epochs.setObjectName(u"Label_Train_VITS_Epochs")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_Epochs.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Epochs.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_Epochs.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_59.addWidget(self.Label_Train_VITS_Epochs, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_Epochs = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_59.addItem(self.HorizontalSpacer_Train_VITS_Epochs, 0, 1, 1, 1)

        self.Button_Train_VITS_Epochs_Undo = QPushButton(self.Frame_Train_VITS_Epochs)
        self.Button_Train_VITS_Epochs_Undo.setObjectName(u"Button_Train_VITS_Epochs_Undo")
        self.Button_Train_VITS_Epochs_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_Epochs_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_Epochs_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_59.addWidget(self.Button_Train_VITS_Epochs_Undo, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_Epochs = QSpinBox(self.Frame_Train_VITS_Epochs)
        self.SpinBox_Train_VITS_Epochs.setObjectName(u"SpinBox_Train_VITS_Epochs")
        self.SpinBox_Train_VITS_Epochs.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_Epochs.setStyleSheet(u"QSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"	border-image: url(:/(Double)"
                        "SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.SpinBox_Train_VITS_Epochs.setMinimum(-999999)
        self.SpinBox_Train_VITS_Epochs.setMaximum(999999)

        self.gridLayout_59.addWidget(self.SpinBox_Train_VITS_Epochs, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_Epochs)

        self.Frame_Train_VITS_BatchSize = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_BatchSize.setObjectName(u"Frame_Train_VITS_BatchSize")
        self.Frame_Train_VITS_BatchSize.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_BatchSize.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_60 = QGridLayout(self.Frame_Train_VITS_BatchSize)
        self.gridLayout_60.setSpacing(12)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_BatchSize = QLabel(self.Frame_Train_VITS_BatchSize)
        self.Label_Train_VITS_BatchSize.setObjectName(u"Label_Train_VITS_BatchSize")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_BatchSize.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_BatchSize.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_BatchSize.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_60.addWidget(self.Label_Train_VITS_BatchSize, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_BatchSize = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.HorizontalSpacer_Train_VITS_BatchSize, 0, 1, 1, 1)

        self.Button_Train_VITS_BatchSize_Undo = QPushButton(self.Frame_Train_VITS_BatchSize)
        self.Button_Train_VITS_BatchSize_Undo.setObjectName(u"Button_Train_VITS_BatchSize_Undo")
        self.Button_Train_VITS_BatchSize_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_BatchSize_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_BatchSize_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_60.addWidget(self.Button_Train_VITS_BatchSize_Undo, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_BatchSize = QSpinBox(self.Frame_Train_VITS_BatchSize)
        self.SpinBox_Train_VITS_BatchSize.setObjectName(u"SpinBox_Train_VITS_BatchSize")
        self.SpinBox_Train_VITS_BatchSize.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_BatchSize.setStyleSheet(u"QSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"	border-image: url(:/(Double)"
                        "SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.SpinBox_Train_VITS_BatchSize.setMinimum(-999999)
        self.SpinBox_Train_VITS_BatchSize.setMaximum(999999)

        self.gridLayout_60.addWidget(self.SpinBox_Train_VITS_BatchSize, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_BatchSize)

        self.Frame_Train_VITS_UsePretrainedModels = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_UsePretrainedModels.setObjectName(u"Frame_Train_VITS_UsePretrainedModels")
        self.Frame_Train_VITS_UsePretrainedModels.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_UsePretrainedModels.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_61 = QGridLayout(self.Frame_Train_VITS_UsePretrainedModels)
        self.gridLayout_61.setSpacing(12)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_UsePretrainedModels = QLabel(self.Frame_Train_VITS_UsePretrainedModels)
        self.Label_Train_VITS_UsePretrainedModels.setObjectName(u"Label_Train_VITS_UsePretrainedModels")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_UsePretrainedModels.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_UsePretrainedModels.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_UsePretrainedModels.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_61.addWidget(self.Label_Train_VITS_UsePretrainedModels, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_UsePretrainedModels = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_61.addItem(self.HorizontalSpacer_Train_VITS_UsePretrainedModels, 0, 1, 1, 1)

        self.Button_Train_VITS_UsePretrainedModels_Undo = QPushButton(self.Frame_Train_VITS_UsePretrainedModels)
        self.Button_Train_VITS_UsePretrainedModels_Undo.setObjectName(u"Button_Train_VITS_UsePretrainedModels_Undo")
        self.Button_Train_VITS_UsePretrainedModels_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_UsePretrainedModels_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_UsePretrainedModels_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_61.addWidget(self.Button_Train_VITS_UsePretrainedModels_Undo, 0, 2, 1, 1)

        self.CheckBox_Train_VITS_UsePretrainedModels = QCheckBox(self.Frame_Train_VITS_UsePretrainedModels)
        self.CheckBox_Train_VITS_UsePretrainedModels.setObjectName(u"CheckBox_Train_VITS_UsePretrainedModels")
        self.CheckBox_Train_VITS_UsePretrainedModels.setMinimumSize(QSize(0, 27))
        self.CheckBox_Train_VITS_UsePretrainedModels.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_61.addWidget(self.CheckBox_Train_VITS_UsePretrainedModels, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_UsePretrainedModels)

        self.Frame_Train_VITS_ModelPathPretrainedG = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_ModelPathPretrainedG.setObjectName(u"Frame_Train_VITS_ModelPathPretrainedG")
        self.Frame_Train_VITS_ModelPathPretrainedG.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_ModelPathPretrainedG.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_65 = QGridLayout(self.Frame_Train_VITS_ModelPathPretrainedG)
        self.gridLayout_65.setSpacing(12)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_ModelPathPretrainedG = QLabel(self.Frame_Train_VITS_ModelPathPretrainedG)
        self.Label_Train_VITS_ModelPathPretrainedG.setObjectName(u"Label_Train_VITS_ModelPathPretrainedG")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_ModelPathPretrainedG.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_ModelPathPretrainedG.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_ModelPathPretrainedG.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_65.addWidget(self.Label_Train_VITS_ModelPathPretrainedG, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_ModelPathPretrainedG = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_65.addItem(self.HorizontalSpacer_Train_VITS_ModelPathPretrainedG, 0, 1, 1, 1)

        self.Button_Train_VITS_ModelPathPretrainedG_Undo = QPushButton(self.Frame_Train_VITS_ModelPathPretrainedG)
        self.Button_Train_VITS_ModelPathPretrainedG_Undo.setObjectName(u"Button_Train_VITS_ModelPathPretrainedG_Undo")
        self.Button_Train_VITS_ModelPathPretrainedG_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedG_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedG_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_65.addWidget(self.Button_Train_VITS_ModelPathPretrainedG_Undo, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_ModelPathPretrainedG = LineEditBase(self.Frame_Train_VITS_ModelPathPretrainedG)
        self.LineEdit_Train_VITS_ModelPathPretrainedG.setObjectName(u"LineEdit_Train_VITS_ModelPathPretrainedG")
        self.LineEdit_Train_VITS_ModelPathPretrainedG.setMinimumSize(QSize(0, 27))

        self.gridLayout_65.addWidget(self.LineEdit_Train_VITS_ModelPathPretrainedG, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_ModelPathPretrainedG)

        self.Frame_Train_VITS_ModelPathPretrainedD = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_ModelPathPretrainedD.setObjectName(u"Frame_Train_VITS_ModelPathPretrainedD")
        self.Frame_Train_VITS_ModelPathPretrainedD.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_ModelPathPretrainedD.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_66 = QGridLayout(self.Frame_Train_VITS_ModelPathPretrainedD)
        self.gridLayout_66.setSpacing(12)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_66.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_ModelPathPretrainedD = QLabel(self.Frame_Train_VITS_ModelPathPretrainedD)
        self.Label_Train_VITS_ModelPathPretrainedD.setObjectName(u"Label_Train_VITS_ModelPathPretrainedD")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_ModelPathPretrainedD.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_ModelPathPretrainedD.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_ModelPathPretrainedD.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_66.addWidget(self.Label_Train_VITS_ModelPathPretrainedD, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_ModelPathPretrainedD = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_66.addItem(self.HorizontalSpacer_Train_VITS_ModelPathPretrainedD, 0, 1, 1, 1)

        self.Button_Train_VITS_ModelPathPretrainedD_Undo = QPushButton(self.Frame_Train_VITS_ModelPathPretrainedD)
        self.Button_Train_VITS_ModelPathPretrainedD_Undo.setObjectName(u"Button_Train_VITS_ModelPathPretrainedD_Undo")
        self.Button_Train_VITS_ModelPathPretrainedD_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedD_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedD_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_66.addWidget(self.Button_Train_VITS_ModelPathPretrainedD_Undo, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_ModelPathPretrainedD = LineEditBase(self.Frame_Train_VITS_ModelPathPretrainedD)
        self.LineEdit_Train_VITS_ModelPathPretrainedD.setObjectName(u"LineEdit_Train_VITS_ModelPathPretrainedD")
        self.LineEdit_Train_VITS_ModelPathPretrainedD.setMinimumSize(QSize(0, 27))

        self.gridLayout_66.addWidget(self.LineEdit_Train_VITS_ModelPathPretrainedD, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_ModelPathPretrainedD)

        self.Frame_Train_VITS_KeepOriginalSpeakers = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_KeepOriginalSpeakers.setObjectName(u"Frame_Train_VITS_KeepOriginalSpeakers")
        self.Frame_Train_VITS_KeepOriginalSpeakers.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_KeepOriginalSpeakers.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_67 = QGridLayout(self.Frame_Train_VITS_KeepOriginalSpeakers)
        self.gridLayout_67.setSpacing(12)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.gridLayout_67.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_KeepOriginalSpeakers = QLabel(self.Frame_Train_VITS_KeepOriginalSpeakers)
        self.Label_Train_VITS_KeepOriginalSpeakers.setObjectName(u"Label_Train_VITS_KeepOriginalSpeakers")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_KeepOriginalSpeakers.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_KeepOriginalSpeakers.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_KeepOriginalSpeakers.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_67.addWidget(self.Label_Train_VITS_KeepOriginalSpeakers, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_KeepOriginalSpeakers = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_67.addItem(self.HorizontalSpacer_Train_VITS_KeepOriginalSpeakers, 0, 1, 1, 1)

        self.Button_Train_VITS_KeepOriginalSpeakers_Undo = QPushButton(self.Frame_Train_VITS_KeepOriginalSpeakers)
        self.Button_Train_VITS_KeepOriginalSpeakers_Undo.setObjectName(u"Button_Train_VITS_KeepOriginalSpeakers_Undo")
        self.Button_Train_VITS_KeepOriginalSpeakers_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_KeepOriginalSpeakers_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_KeepOriginalSpeakers_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_67.addWidget(self.Button_Train_VITS_KeepOriginalSpeakers_Undo, 0, 2, 1, 1)

        self.CheckBox_Train_VITS_KeepOriginalSpeakers = QCheckBox(self.Frame_Train_VITS_KeepOriginalSpeakers)
        self.CheckBox_Train_VITS_KeepOriginalSpeakers.setObjectName(u"CheckBox_Train_VITS_KeepOriginalSpeakers")
        self.CheckBox_Train_VITS_KeepOriginalSpeakers.setMinimumSize(QSize(0, 27))
        self.CheckBox_Train_VITS_KeepOriginalSpeakers.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_67.addWidget(self.CheckBox_Train_VITS_KeepOriginalSpeakers, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_KeepOriginalSpeakers)

        self.Frame_Train_VITS_ConfigPathLoad = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_ConfigPathLoad.setObjectName(u"Frame_Train_VITS_ConfigPathLoad")
        self.Frame_Train_VITS_ConfigPathLoad.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_ConfigPathLoad.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_77 = QGridLayout(self.Frame_Train_VITS_ConfigPathLoad)
        self.gridLayout_77.setSpacing(12)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.gridLayout_77.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_ConfigPathLoad = QLabel(self.Frame_Train_VITS_ConfigPathLoad)
        self.Label_Train_VITS_ConfigPathLoad.setObjectName(u"Label_Train_VITS_ConfigPathLoad")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_ConfigPathLoad.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_ConfigPathLoad.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_ConfigPathLoad.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_77.addWidget(self.Label_Train_VITS_ConfigPathLoad, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_ConfigPathLoad = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_77.addItem(self.HorizontalSpacer_Train_VITS_ConfigPathLoad, 0, 1, 1, 1)

        self.Button_Train_VITS_ConfigPathLoad_Undo = QPushButton(self.Frame_Train_VITS_ConfigPathLoad)
        self.Button_Train_VITS_ConfigPathLoad_Undo.setObjectName(u"Button_Train_VITS_ConfigPathLoad_Undo")
        self.Button_Train_VITS_ConfigPathLoad_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_ConfigPathLoad_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_ConfigPathLoad_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_77.addWidget(self.Button_Train_VITS_ConfigPathLoad_Undo, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_ConfigPathLoad = LineEditBase(self.Frame_Train_VITS_ConfigPathLoad)
        self.LineEdit_Train_VITS_ConfigPathLoad.setObjectName(u"LineEdit_Train_VITS_ConfigPathLoad")
        self.LineEdit_Train_VITS_ConfigPathLoad.setMinimumSize(QSize(0, 27))

        self.gridLayout_77.addWidget(self.LineEdit_Train_VITS_ConfigPathLoad, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_ConfigPathLoad)


        self.verticalLayout_114.addWidget(self.Frame_Train_VITS_VITSParams_BasicSettings)

        self.CheckBox_Train_VITS_VITSParams_Toggle_AdvanceSettings = QCheckBox(self.GroupBox_Train_VITS_VITSParams)
        self.CheckBox_Train_VITS_VITSParams_Toggle_AdvanceSettings.setObjectName(u"CheckBox_Train_VITS_VITSParams_Toggle_AdvanceSettings")
        self.CheckBox_Train_VITS_VITSParams_Toggle_AdvanceSettings.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	font-weight: 630;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding-top: 9px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"    background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: transparent;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/RightCaret.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/DownCaret.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_114.addWidget(self.CheckBox_Train_VITS_VITSParams_Toggle_AdvanceSettings)

        self.Frame_Train_VITS_VITSParams_AdvanceSettings = QFrame(self.GroupBox_Train_VITS_VITSParams)
        self.Frame_Train_VITS_VITSParams_AdvanceSettings.setObjectName(u"Frame_Train_VITS_VITSParams_AdvanceSettings")
        self.Frame_Train_VITS_VITSParams_AdvanceSettings.setFrameShape(QFrame.StyledPanel)
        self.Frame_Train_VITS_VITSParams_AdvanceSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.Frame_Train_VITS_VITSParams_AdvanceSettings)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_NumWorkers = QFrame(self.Frame_Train_VITS_VITSParams_AdvanceSettings)
        self.Frame_Train_VITS_NumWorkers.setObjectName(u"Frame_Train_VITS_NumWorkers")
        self.Frame_Train_VITS_NumWorkers.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_NumWorkers.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_63 = QGridLayout(self.Frame_Train_VITS_NumWorkers)
        self.gridLayout_63.setSpacing(12)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.gridLayout_63.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_NumWorkers = QLabel(self.Frame_Train_VITS_NumWorkers)
        self.Label_Train_VITS_NumWorkers.setObjectName(u"Label_Train_VITS_NumWorkers")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_NumWorkers.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_NumWorkers.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_NumWorkers.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_63.addWidget(self.Label_Train_VITS_NumWorkers, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_NumWorkers = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_63.addItem(self.HorizontalSpacer_Train_VITS_NumWorkers, 0, 1, 1, 1)

        self.Button_Train_VITS_NumWorkers_Undo = QPushButton(self.Frame_Train_VITS_NumWorkers)
        self.Button_Train_VITS_NumWorkers_Undo.setObjectName(u"Button_Train_VITS_NumWorkers_Undo")
        self.Button_Train_VITS_NumWorkers_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_NumWorkers_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_NumWorkers_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_63.addWidget(self.Button_Train_VITS_NumWorkers_Undo, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_NumWorkers = QSpinBox(self.Frame_Train_VITS_NumWorkers)
        self.SpinBox_Train_VITS_NumWorkers.setObjectName(u"SpinBox_Train_VITS_NumWorkers")
        self.SpinBox_Train_VITS_NumWorkers.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_NumWorkers.setStyleSheet(u"QSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"	border-image: url(:/(Double)"
                        "SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.SpinBox_Train_VITS_NumWorkers.setMinimum(-999999)
        self.SpinBox_Train_VITS_NumWorkers.setMaximum(999999)

        self.gridLayout_63.addWidget(self.SpinBox_Train_VITS_NumWorkers, 1, 0, 1, 3)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_NumWorkers)

        self.Frame_Train_VITS_FP16Run = QFrame(self.Frame_Train_VITS_VITSParams_AdvanceSettings)
        self.Frame_Train_VITS_FP16Run.setObjectName(u"Frame_Train_VITS_FP16Run")
        self.Frame_Train_VITS_FP16Run.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_FP16Run.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_64 = QGridLayout(self.Frame_Train_VITS_FP16Run)
        self.gridLayout_64.setSpacing(12)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_64.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_FP16Run = QLabel(self.Frame_Train_VITS_FP16Run)
        self.Label_Train_VITS_FP16Run.setObjectName(u"Label_Train_VITS_FP16Run")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_FP16Run.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_FP16Run.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_FP16Run.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_64.addWidget(self.Label_Train_VITS_FP16Run, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_FP16Run = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_64.addItem(self.HorizontalSpacer_Train_VITS_FP16Run, 0, 1, 1, 1)

        self.Button_Train_VITS_FP16Run_Undo = QPushButton(self.Frame_Train_VITS_FP16Run)
        self.Button_Train_VITS_FP16Run_Undo.setObjectName(u"Button_Train_VITS_FP16Run_Undo")
        self.Button_Train_VITS_FP16Run_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_FP16Run_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_FP16Run_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_64.addWidget(self.Button_Train_VITS_FP16Run_Undo, 0, 2, 1, 1)

        self.CheckBox_Train_VITS_FP16Run = QCheckBox(self.Frame_Train_VITS_FP16Run)
        self.CheckBox_Train_VITS_FP16Run.setObjectName(u"CheckBox_Train_VITS_FP16Run")
        self.CheckBox_Train_VITS_FP16Run.setMinimumSize(QSize(0, 27))
        self.CheckBox_Train_VITS_FP16Run.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 24px;\n"
"	height: 24px;\n"
"    background-color: transparent;\n"
"	padding: 1.2px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_64.addWidget(self.CheckBox_Train_VITS_FP16Run, 1, 0, 1, 3)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_FP16Run)


        self.verticalLayout_114.addWidget(self.Frame_Train_VITS_VITSParams_AdvanceSettings)


        self.verticalLayout_28.addWidget(self.GroupBox_Train_VITS_VITSParams)

        self.GroupBox_Train_VITS_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.GroupBox_Train_VITS_OutputParams.setObjectName(u"GroupBox_Train_VITS_OutputParams")
        self.GroupBox_Train_VITS_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_145 = QVBoxLayout(self.GroupBox_Train_VITS_OutputParams)
        self.verticalLayout_145.setSpacing(0)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(0, 12, 0, 12)
        self.Frame_Train_VITS_OutputParams_BasicSettings = QFrame(self.GroupBox_Train_VITS_OutputParams)
        self.Frame_Train_VITS_OutputParams_BasicSettings.setObjectName(u"Frame_Train_VITS_OutputParams_BasicSettings")
        self.verticalLayout_26 = QVBoxLayout(self.Frame_Train_VITS_OutputParams_BasicSettings)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_EvalInterval = QFrame(self.Frame_Train_VITS_OutputParams_BasicSettings)
        self.Frame_Train_VITS_EvalInterval.setObjectName(u"Frame_Train_VITS_EvalInterval")
        self.Frame_Train_VITS_EvalInterval.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_EvalInterval.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_62 = QGridLayout(self.Frame_Train_VITS_EvalInterval)
        self.gridLayout_62.setSpacing(12)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_EvalInterval = QLabel(self.Frame_Train_VITS_EvalInterval)
        self.Label_Train_VITS_EvalInterval.setObjectName(u"Label_Train_VITS_EvalInterval")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_EvalInterval.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_EvalInterval.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_EvalInterval.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_62.addWidget(self.Label_Train_VITS_EvalInterval, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_EvalInterval = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_62.addItem(self.HorizontalSpacer_Train_VITS_EvalInterval, 0, 1, 1, 1)

        self.Button_Train_VITS_EvalInterval_Undo = QPushButton(self.Frame_Train_VITS_EvalInterval)
        self.Button_Train_VITS_EvalInterval_Undo.setObjectName(u"Button_Train_VITS_EvalInterval_Undo")
        self.Button_Train_VITS_EvalInterval_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_EvalInterval_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_EvalInterval_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_62.addWidget(self.Button_Train_VITS_EvalInterval_Undo, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_EvalInterval = QSpinBox(self.Frame_Train_VITS_EvalInterval)
        self.SpinBox_Train_VITS_EvalInterval.setObjectName(u"SpinBox_Train_VITS_EvalInterval")
        self.SpinBox_Train_VITS_EvalInterval.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_EvalInterval.setStyleSheet(u"QSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"	border-image: url(:/(Double)"
                        "SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.SpinBox_Train_VITS_EvalInterval.setMinimum(-999999)
        self.SpinBox_Train_VITS_EvalInterval.setMaximum(999999)

        self.gridLayout_62.addWidget(self.SpinBox_Train_VITS_EvalInterval, 1, 0, 1, 3)


        self.verticalLayout_26.addWidget(self.Frame_Train_VITS_EvalInterval)

        self.Frame_Train_VITS_OutputDir = QFrame(self.Frame_Train_VITS_OutputParams_BasicSettings)
        self.Frame_Train_VITS_OutputDir.setObjectName(u"Frame_Train_VITS_OutputDir")
        self.Frame_Train_VITS_OutputDir.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_OutputDir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_68 = QGridLayout(self.Frame_Train_VITS_OutputDir)
        self.gridLayout_68.setSpacing(12)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.gridLayout_68.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_OutputDir = QLabel(self.Frame_Train_VITS_OutputDir)
        self.Label_Train_VITS_OutputDir.setObjectName(u"Label_Train_VITS_OutputDir")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_OutputDir.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_OutputDir.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_OutputDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_68.addWidget(self.Label_Train_VITS_OutputDir, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_OutputDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_68.addItem(self.HorizontalSpacer_Train_VITS_OutputDir, 0, 1, 1, 1)

        self.Button_Train_VITS_OutputDir_Undo = QPushButton(self.Frame_Train_VITS_OutputDir)
        self.Button_Train_VITS_OutputDir_Undo.setObjectName(u"Button_Train_VITS_OutputDir_Undo")
        self.Button_Train_VITS_OutputDir_Undo.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_OutputDir_Undo.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_OutputDir_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_68.addWidget(self.Button_Train_VITS_OutputDir_Undo, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_OutputDir = LineEditBase(self.Frame_Train_VITS_OutputDir)
        self.LineEdit_Train_VITS_OutputDir.setObjectName(u"LineEdit_Train_VITS_OutputDir")
        self.LineEdit_Train_VITS_OutputDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_68.addWidget(self.LineEdit_Train_VITS_OutputDir, 1, 0, 1, 3)


        self.verticalLayout_26.addWidget(self.Frame_Train_VITS_OutputDir)


        self.verticalLayout_145.addWidget(self.Frame_Train_VITS_OutputParams_BasicSettings)


        self.verticalLayout_28.addWidget(self.GroupBox_Train_VITS_OutputParams)

        self.VerticalSpacer_Train_VITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.VerticalSpacer_Train_VITS)

        self.ScrollArea_Middle_Train_VITS.setWidget(self.ScrollArea_Middle_WidgetContents_Train_VITS)

        self.gridLayout_22.addWidget(self.ScrollArea_Middle_Train_VITS, 0, 1, 1, 1)

        self.gridLayout_22.setColumnStretch(0, 3)
        self.gridLayout_22.setColumnStretch(1, 10)
        self.gridLayout_22.setColumnStretch(2, 7)
        self.StackedWidget_Pages_Train.addWidget(self.Subpage_Train_VITS)

        self.verticalLayout_43.addWidget(self.StackedWidget_Pages_Train)

        self.StackedWidget_Pages.addWidget(self.Page_Train)
        self.Page_TTS = QWidget()
        self.Page_TTS.setObjectName(u"Page_TTS")
        self.verticalLayout_42 = QVBoxLayout(self.Page_TTS)
        self.verticalLayout_42.setSpacing(21)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(21, 12, 21, 12)
        self.Frame_TTS_Top = QFrame(self.Page_TTS)
        self.Frame_TTS_Top.setObjectName(u"Frame_TTS_Top")
        self.Frame_TTS_Top.setMinimumSize(QSize(0, 60))
        self.Frame_TTS_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_81 = QHBoxLayout(self.Frame_TTS_Top)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_VoiceConverter_Title = QToolButton(self.Frame_TTS_Top)
        self.ToolButton_VoiceConverter_Title.setObjectName(u"ToolButton_VoiceConverter_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_VoiceConverter_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_VoiceConverter_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_VoiceConverter_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color:"
                        " rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_81.addWidget(self.ToolButton_VoiceConverter_Title)

        self.Frame_TTS_Title_Spacer = QLabel(self.Frame_TTS_Top)
        self.Frame_TTS_Title_Spacer.setObjectName(u"Frame_TTS_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_TTS_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_TTS_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_TTS_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;*/\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_81.addWidget(self.Frame_TTS_Title_Spacer)


        self.verticalLayout_42.addWidget(self.Frame_TTS_Top)

        self.StackedWidget_Pages_TTS = QStackedWidget(self.Page_TTS)
        self.StackedWidget_Pages_TTS.setObjectName(u"StackedWidget_Pages_TTS")
        self.StackedWidget_Pages_TTS.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/*\n"
"QTabWidget {\n"
"	background-color: transparent;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"}\n"
"QTabWidget::pane {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"	font-size: 18px;\n"
"	font-weight: 420;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 12px;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:selected {\n"
"	color: rgba(255, 255, 255, 255);\n"
"}\n"
"QTabBar::tab:hover:!selected {\n"
"}\n"
"\n"
"\n"
"QTabBar QToolButton {\n"
"}\n"
"QTabBar QToolButton:hover {\n"
"}\n"
"*/")
        self.Subpage_TTS_VITS = QWidget()
        self.Subpage_TTS_VITS.setObjectName(u"Subpage_TTS_VITS")
        self.gridLayout_20 = QGridLayout(self.Subpage_TTS_VITS)
        self.gridLayout_20.setSpacing(12)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_TTS_VITS = QWidget(self.Subpage_TTS_VITS)
        self.Widget_Left_TTS_VITS.setObjectName(u"Widget_Left_TTS_VITS")
        self.Widget_Left_TTS_VITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_TTS_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.Widget_Left_TTS_VITS)
        self.verticalLayout_11.setSpacing(12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_TTS_VITS = QTreeWidget(self.Widget_Left_TTS_VITS)
        __qtreewidgetitem5 = QTreeWidgetItem(self.TreeWidget_Catalogue_TTS_VITS)
        QTreeWidgetItem(__qtreewidgetitem5)
        self.TreeWidget_Catalogue_TTS_VITS.setObjectName(u"TreeWidget_Catalogue_TTS_VITS")
        self.TreeWidget_Catalogue_TTS_VITS.setStyleSheet(u"QTreeView {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"	background-color: transparent;\n"
"	padding: 2.4px;\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"QTreeView::item:selected {\n"
"    background-color: ;\n"
"}\n"
"\n"
"QTreeView::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeView::branch:open:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeView::branch:closed:has-children {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:adjoins-item {\n"
"    background-color: ;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: rgba(45, 45, 45, 135);\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"	background-color: r"
                        "gba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"}\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-page, QScrollBar::add-page {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(90, 90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}")

        self.verticalLayout_11.addWidget(self.TreeWidget_Catalogue_TTS_VITS)


        self.gridLayout_20.addWidget(self.Widget_Left_TTS_VITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_TTS_VITS = QScrollArea(self.Subpage_TTS_VITS)
        self.ScrollArea_Middle_TTS_VITS.setObjectName(u"ScrollArea_Middle_TTS_VITS")
        self.ScrollArea_Middle_TTS_VITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_TTS_VITS.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollArea:hover {\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	"
                        "height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	borde"
                        "r-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")
        self.ScrollArea_Middle_TTS_VITS.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_TTS_VITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_TTS_VITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_TTS_VITS.setObjectName(u"ScrollArea_Middle_WidgetContents_TTS_VITS")
        self.ScrollArea_Middle_WidgetContents_TTS_VITS.setGeometry(QRect(0, 0, 591, 1261))
        self.verticalLayout_19 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.verticalLayout_19.setSpacing(12)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_TTS_VITS_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.GroupBox_TTS_VITS_InputParams.setObjectName(u"GroupBox_TTS_VITS_InputParams")
        self.GroupBox_TTS_VITS_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_120 = QVBoxLayout(self.GroupBox_TTS_VITS_InputParams)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 12, 0, 12)
        self.Frame_TTS_VITS_InputParams_BasicSettings = QFrame(self.GroupBox_TTS_VITS_InputParams)
        self.Frame_TTS_VITS_InputParams_BasicSettings.setObjectName(u"Frame_TTS_VITS_InputParams_BasicSettings")
        self.verticalLayout_132 = QVBoxLayout(self.Frame_TTS_VITS_InputParams_BasicSettings)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_VITS_ConfigPathLoad = QFrame(self.Frame_TTS_VITS_InputParams_BasicSettings)
        self.Frame_TTS_VITS_ConfigPathLoad.setObjectName(u"Frame_TTS_VITS_ConfigPathLoad")
        self.Frame_TTS_VITS_ConfigPathLoad.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_ConfigPathLoad.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_69 = QGridLayout(self.Frame_TTS_VITS_ConfigPathLoad)
        self.gridLayout_69.setSpacing(12)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.gridLayout_69.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_ConfigPathLoad = QLabel(self.Frame_TTS_VITS_ConfigPathLoad)
        self.Label_TTS_VITS_ConfigPathLoad.setObjectName(u"Label_TTS_VITS_ConfigPathLoad")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_ConfigPathLoad.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_ConfigPathLoad.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_ConfigPathLoad.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_69.addWidget(self.Label_TTS_VITS_ConfigPathLoad, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_ConfigPathLoad = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_69.addItem(self.HorizontalSpacer_TTS_VITS_ConfigPathLoad, 0, 1, 1, 1)

        self.Button_TTS_VITS_ConfigPathLoad_Undo = QPushButton(self.Frame_TTS_VITS_ConfigPathLoad)
        self.Button_TTS_VITS_ConfigPathLoad_Undo.setObjectName(u"Button_TTS_VITS_ConfigPathLoad_Undo")
        self.Button_TTS_VITS_ConfigPathLoad_Undo.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_ConfigPathLoad_Undo.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_ConfigPathLoad_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_69.addWidget(self.Button_TTS_VITS_ConfigPathLoad_Undo, 0, 2, 1, 1)

        self.LineEdit_TTS_VITS_ConfigPathLoad = LineEditBase(self.Frame_TTS_VITS_ConfigPathLoad)
        self.LineEdit_TTS_VITS_ConfigPathLoad.setObjectName(u"LineEdit_TTS_VITS_ConfigPathLoad")
        self.LineEdit_TTS_VITS_ConfigPathLoad.setMinimumSize(QSize(0, 27))

        self.gridLayout_69.addWidget(self.LineEdit_TTS_VITS_ConfigPathLoad, 1, 0, 1, 3)


        self.verticalLayout_132.addWidget(self.Frame_TTS_VITS_ConfigPathLoad)

        self.Frame_TTS_VITS_ModelPathLoad = QFrame(self.Frame_TTS_VITS_InputParams_BasicSettings)
        self.Frame_TTS_VITS_ModelPathLoad.setObjectName(u"Frame_TTS_VITS_ModelPathLoad")
        self.Frame_TTS_VITS_ModelPathLoad.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_ModelPathLoad.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_70 = QGridLayout(self.Frame_TTS_VITS_ModelPathLoad)
        self.gridLayout_70.setSpacing(12)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.gridLayout_70.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_ModelPathLoad = QLabel(self.Frame_TTS_VITS_ModelPathLoad)
        self.Label_TTS_VITS_ModelPathLoad.setObjectName(u"Label_TTS_VITS_ModelPathLoad")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_ModelPathLoad.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_ModelPathLoad.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_ModelPathLoad.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_70.addWidget(self.Label_TTS_VITS_ModelPathLoad, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_ModelPathLoad = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_70.addItem(self.HorizontalSpacer_TTS_VITS_ModelPathLoad, 0, 1, 1, 1)

        self.Button_TTS_VITS_ModelPathLoad_Undo = QPushButton(self.Frame_TTS_VITS_ModelPathLoad)
        self.Button_TTS_VITS_ModelPathLoad_Undo.setObjectName(u"Button_TTS_VITS_ModelPathLoad_Undo")
        self.Button_TTS_VITS_ModelPathLoad_Undo.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_ModelPathLoad_Undo.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_ModelPathLoad_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_70.addWidget(self.Button_TTS_VITS_ModelPathLoad_Undo, 0, 2, 1, 1)

        self.LineEdit_TTS_VITS_ModelPathLoad = LineEditBase(self.Frame_TTS_VITS_ModelPathLoad)
        self.LineEdit_TTS_VITS_ModelPathLoad.setObjectName(u"LineEdit_TTS_VITS_ModelPathLoad")
        self.LineEdit_TTS_VITS_ModelPathLoad.setMinimumSize(QSize(0, 27))

        self.gridLayout_70.addWidget(self.LineEdit_TTS_VITS_ModelPathLoad, 1, 0, 1, 3)


        self.verticalLayout_132.addWidget(self.Frame_TTS_VITS_ModelPathLoad)


        self.verticalLayout_120.addWidget(self.Frame_TTS_VITS_InputParams_BasicSettings)


        self.verticalLayout_19.addWidget(self.GroupBox_TTS_VITS_InputParams)

        self.GroupBox_TTS_VITS_VITSParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.GroupBox_TTS_VITS_VITSParams.setObjectName(u"GroupBox_TTS_VITS_VITSParams")
        self.GroupBox_TTS_VITS_VITSParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_117 = QVBoxLayout(self.GroupBox_TTS_VITS_VITSParams)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 12, 0, 12)
        self.Frame_TTS_VITS_VITSParams_BasicSettings = QFrame(self.GroupBox_TTS_VITS_VITSParams)
        self.Frame_TTS_VITS_VITSParams_BasicSettings.setObjectName(u"Frame_TTS_VITS_VITSParams_BasicSettings")
        self.verticalLayout_131 = QVBoxLayout(self.Frame_TTS_VITS_VITSParams_BasicSettings)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_VITS_Text = QFrame(self.Frame_TTS_VITS_VITSParams_BasicSettings)
        self.Frame_TTS_VITS_Text.setObjectName(u"Frame_TTS_VITS_Text")
        self.Frame_TTS_VITS_Text.setMinimumSize(QSize(0, 222))
        self.Frame_TTS_VITS_Text.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.verticalLayout_98 = QVBoxLayout(self.Frame_TTS_VITS_Text)
        self.verticalLayout_98.setSpacing(12)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Text = QLabel(self.Frame_TTS_VITS_Text)
        self.Label_TTS_VITS_Text.setObjectName(u"Label_TTS_VITS_Text")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_Text.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Text.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_Text.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_98.addWidget(self.Label_TTS_VITS_Text)

        self.PlainTextEdit_TTS_VITS_Text = QPlainTextEdit(self.Frame_TTS_VITS_Text)
        self.PlainTextEdit_TTS_VITS_Text.setObjectName(u"PlainTextEdit_TTS_VITS_Text")
        sizePolicy3.setHeightForWidth(self.PlainTextEdit_TTS_VITS_Text.sizePolicy().hasHeightForWidth())
        self.PlainTextEdit_TTS_VITS_Text.setSizePolicy(sizePolicy3)
        self.PlainTextEdit_TTS_VITS_Text.setStyleSheet(u"QPlainTextEdit {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
""
                        "}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color"
                        ": transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.verticalLayout_98.addWidget(self.PlainTextEdit_TTS_VITS_Text)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Text)

        self.Frame_TTS_VITS_Language = QFrame(self.Frame_TTS_VITS_VITSParams_BasicSettings)
        self.Frame_TTS_VITS_Language.setObjectName(u"Frame_TTS_VITS_Language")
        self.Frame_TTS_VITS_Language.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_Language.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_79 = QGridLayout(self.Frame_TTS_VITS_Language)
        self.gridLayout_79.setSpacing(12)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.gridLayout_79.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Language = QLabel(self.Frame_TTS_VITS_Language)
        self.Label_TTS_VITS_Language.setObjectName(u"Label_TTS_VITS_Language")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_Language.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Language.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_Language.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_79.addWidget(self.Label_TTS_VITS_Language, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_Language = QSpacerItem(415, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_79.addItem(self.HorizontalSpacer_TTS_VITS_Language, 0, 1, 1, 1)

        self.Button_TTS_VITS_Language_Undo = QPushButton(self.Frame_TTS_VITS_Language)
        self.Button_TTS_VITS_Language_Undo.setObjectName(u"Button_TTS_VITS_Language_Undo")
        self.Button_TTS_VITS_Language_Undo.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_Language_Undo.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_Language_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_79.addWidget(self.Button_TTS_VITS_Language_Undo, 0, 2, 1, 1)

        self.ComboBox_TTS_VITS_Language = QComboBox(self.Frame_TTS_VITS_Language)
        self.ComboBox_TTS_VITS_Language.setObjectName(u"ComboBox_TTS_VITS_Language")
        self.ComboBox_TTS_VITS_Language.setMinimumSize(QSize(0, 27))
        self.ComboBox_TTS_VITS_Language.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QComboBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	/*width: 12px;\n"
"	height: 12px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	margin-right: 6px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"	border-image: url(:/ComboBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"\n"
"QCom"
                        "boBox QAbstractItemView::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
""
                        "	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:vertical, QComboBox QAbstractScrollArea QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	borde"
                        "r-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:horizontal, QComboBox QAbstractScrollArea QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	"
                        "border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_79.addWidget(self.ComboBox_TTS_VITS_Language, 1, 0, 1, 3)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Language)

        self.Frame_TTS_VITS_Speaker = QFrame(self.Frame_TTS_VITS_VITSParams_BasicSettings)
        self.Frame_TTS_VITS_Speaker.setObjectName(u"Frame_TTS_VITS_Speaker")
        self.Frame_TTS_VITS_Speaker.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_Speaker.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.verticalLayout_104 = QVBoxLayout(self.Frame_TTS_VITS_Speaker)
        self.verticalLayout_104.setSpacing(12)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Speaker = QLabel(self.Frame_TTS_VITS_Speaker)
        self.Label_TTS_VITS_Speaker.setObjectName(u"Label_TTS_VITS_Speaker")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_Speaker.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Speaker.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_Speaker.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_104.addWidget(self.Label_TTS_VITS_Speaker)

        self.ComboBox_TTS_VITS_Speaker = QComboBox(self.Frame_TTS_VITS_Speaker)
        self.ComboBox_TTS_VITS_Speaker.setObjectName(u"ComboBox_TTS_VITS_Speaker")
        self.ComboBox_TTS_VITS_Speaker.setMinimumSize(QSize(0, 27))
        self.ComboBox_TTS_VITS_Speaker.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QComboBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	/*width: 12px;\n"
"	height: 12px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	margin-right: 6px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"	border-image: url(:/ComboBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"\n"
"QCom"
                        "boBox QAbstractItemView::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
""
                        "	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:vertical, QComboBox QAbstractScrollArea QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	borde"
                        "r-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:horizontal, QComboBox QAbstractScrollArea QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	"
                        "border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_104.addWidget(self.ComboBox_TTS_VITS_Speaker)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Speaker)


        self.verticalLayout_117.addWidget(self.Frame_TTS_VITS_VITSParams_BasicSettings)

        self.CheckBox_TTS_VITS_VITSParams_Toggle_AdvanceSettings = QCheckBox(self.GroupBox_TTS_VITS_VITSParams)
        self.CheckBox_TTS_VITS_VITSParams_Toggle_AdvanceSettings.setObjectName(u"CheckBox_TTS_VITS_VITSParams_Toggle_AdvanceSettings")
        self.CheckBox_TTS_VITS_VITSParams_Toggle_AdvanceSettings.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	font-weight: 630;\n"
"	spacing: 12px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding-top: 9px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"    background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: transparent;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/RightCaret.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/DownCaret.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_117.addWidget(self.CheckBox_TTS_VITS_VITSParams_Toggle_AdvanceSettings)

        self.Frame_TTS_VITS_VITSParams_AdvanceSettings = QFrame(self.GroupBox_TTS_VITS_VITSParams)
        self.Frame_TTS_VITS_VITSParams_AdvanceSettings.setObjectName(u"Frame_TTS_VITS_VITSParams_AdvanceSettings")
        self.verticalLayout_118 = QVBoxLayout(self.Frame_TTS_VITS_VITSParams_AdvanceSettings)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_VITS_EmotionStrength = QFrame(self.Frame_TTS_VITS_VITSParams_AdvanceSettings)
        self.Frame_TTS_VITS_EmotionStrength.setObjectName(u"Frame_TTS_VITS_EmotionStrength")
        self.Frame_TTS_VITS_EmotionStrength.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_EmotionStrength.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_71 = QGridLayout(self.Frame_TTS_VITS_EmotionStrength)
        self.gridLayout_71.setSpacing(12)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_71.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_EmotionStrength = QLabel(self.Frame_TTS_VITS_EmotionStrength)
        self.Label_TTS_VITS_EmotionStrength.setObjectName(u"Label_TTS_VITS_EmotionStrength")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_EmotionStrength.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_EmotionStrength.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_EmotionStrength.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_71.addWidget(self.Label_TTS_VITS_EmotionStrength, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_EmotionStrength = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_71.addItem(self.HorizontalSpacer_TTS_VITS_EmotionStrength, 0, 1, 1, 1)

        self.Button_TTS_VITS_EmotionStrength_Undo = QPushButton(self.Frame_TTS_VITS_EmotionStrength)
        self.Button_TTS_VITS_EmotionStrength_Undo.setObjectName(u"Button_TTS_VITS_EmotionStrength_Undo")
        self.Button_TTS_VITS_EmotionStrength_Undo.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_EmotionStrength_Undo.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_EmotionStrength_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_71.addWidget(self.Button_TTS_VITS_EmotionStrength_Undo, 0, 2, 1, 1)

        self.ChildFrame_TTS_VITS_EmotionStrength = QFrame(self.Frame_TTS_VITS_EmotionStrength)
        self.ChildFrame_TTS_VITS_EmotionStrength.setObjectName(u"ChildFrame_TTS_VITS_EmotionStrength")
        sizePolicy5.setHeightForWidth(self.ChildFrame_TTS_VITS_EmotionStrength.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_EmotionStrength.setSizePolicy(sizePolicy5)
        self.ChildFrame_TTS_VITS_EmotionStrength.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_43 = QHBoxLayout(self.ChildFrame_TTS_VITS_EmotionStrength)
        self.horizontalLayout_43.setSpacing(12)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSlider_TTS_VITS_EmotionStrength = QSlider(self.ChildFrame_TTS_VITS_EmotionStrength)
        self.HorizontalSlider_TTS_VITS_EmotionStrength.setObjectName(u"HorizontalSlider_TTS_VITS_EmotionStrength")
        self.HorizontalSlider_TTS_VITS_EmotionStrength.setMinimumSize(QSize(0, 27))
        self.HorizontalSlider_TTS_VITS_EmotionStrength.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	height: 1.2px;\n"
"	background-color: rgba(201, 210, 222, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	background-color: rgba(201, 210, 222, 210);\n"
"	margin-top: -6px;\n"
"	margin-bottom: -6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	/*border-color: rgba(201, 210, 222, 123);*/\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color: rgba(210, 222, 234, 234);\n"
"	/*border-color: rgba(201, 210, 222, 210);*/\n"
"}")
        self.HorizontalSlider_TTS_VITS_EmotionStrength.setOrientation(Qt.Horizontal)

        self.horizontalLayout_43.addWidget(self.HorizontalSlider_TTS_VITS_EmotionStrength)

        self.DoubleSpinBox_TTS_VITS_EmotionStrength = QDoubleSpinBox(self.ChildFrame_TTS_VITS_EmotionStrength)
        self.DoubleSpinBox_TTS_VITS_EmotionStrength.setObjectName(u"DoubleSpinBox_TTS_VITS_EmotionStrength")
        self.DoubleSpinBox_TTS_VITS_EmotionStrength.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_TTS_VITS_EmotionStrength.setStyleSheet(u"QDoubleSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	/*height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::down-arr"
                        "ow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_43.addWidget(self.DoubleSpinBox_TTS_VITS_EmotionStrength)


        self.gridLayout_71.addWidget(self.ChildFrame_TTS_VITS_EmotionStrength, 1, 0, 1, 3)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_EmotionStrength)

        self.Frame_TTS_VITS_PhonemeDuration = QFrame(self.Frame_TTS_VITS_VITSParams_AdvanceSettings)
        self.Frame_TTS_VITS_PhonemeDuration.setObjectName(u"Frame_TTS_VITS_PhonemeDuration")
        self.Frame_TTS_VITS_PhonemeDuration.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_PhonemeDuration.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_72 = QGridLayout(self.Frame_TTS_VITS_PhonemeDuration)
        self.gridLayout_72.setSpacing(12)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.gridLayout_72.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_PhonemeDuration = QLabel(self.Frame_TTS_VITS_PhonemeDuration)
        self.Label_TTS_VITS_PhonemeDuration.setObjectName(u"Label_TTS_VITS_PhonemeDuration")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_PhonemeDuration.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_PhonemeDuration.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_PhonemeDuration.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_72.addWidget(self.Label_TTS_VITS_PhonemeDuration, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_PhonemeDuration = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_72.addItem(self.HorizontalSpacer_TTS_VITS_PhonemeDuration, 0, 1, 1, 1)

        self.Button_TTS_VITS_PhonemeDuration_Undo = QPushButton(self.Frame_TTS_VITS_PhonemeDuration)
        self.Button_TTS_VITS_PhonemeDuration_Undo.setObjectName(u"Button_TTS_VITS_PhonemeDuration_Undo")
        self.Button_TTS_VITS_PhonemeDuration_Undo.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_PhonemeDuration_Undo.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_PhonemeDuration_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_72.addWidget(self.Button_TTS_VITS_PhonemeDuration_Undo, 0, 2, 1, 1)

        self.ChildFrame_TTS_VITS_PhonemeDuration = QFrame(self.Frame_TTS_VITS_PhonemeDuration)
        self.ChildFrame_TTS_VITS_PhonemeDuration.setObjectName(u"ChildFrame_TTS_VITS_PhonemeDuration")
        sizePolicy5.setHeightForWidth(self.ChildFrame_TTS_VITS_PhonemeDuration.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_PhonemeDuration.setSizePolicy(sizePolicy5)
        self.ChildFrame_TTS_VITS_PhonemeDuration.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_44 = QHBoxLayout(self.ChildFrame_TTS_VITS_PhonemeDuration)
        self.horizontalLayout_44.setSpacing(12)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSlider_TTS_VITS_PhonemeDuration = QSlider(self.ChildFrame_TTS_VITS_PhonemeDuration)
        self.HorizontalSlider_TTS_VITS_PhonemeDuration.setObjectName(u"HorizontalSlider_TTS_VITS_PhonemeDuration")
        self.HorizontalSlider_TTS_VITS_PhonemeDuration.setMinimumSize(QSize(0, 27))
        self.HorizontalSlider_TTS_VITS_PhonemeDuration.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	height: 1.2px;\n"
"	background-color: rgba(201, 210, 222, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	background-color: rgba(201, 210, 222, 210);\n"
"	margin-top: -6px;\n"
"	margin-bottom: -6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	/*border-color: rgba(201, 210, 222, 123);*/\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color: rgba(210, 222, 234, 234);\n"
"	/*border-color: rgba(201, 210, 222, 210);*/\n"
"}")
        self.HorizontalSlider_TTS_VITS_PhonemeDuration.setOrientation(Qt.Horizontal)

        self.horizontalLayout_44.addWidget(self.HorizontalSlider_TTS_VITS_PhonemeDuration)

        self.DoubleSpinBox_TTS_VITS_PhonemeDuration = QDoubleSpinBox(self.ChildFrame_TTS_VITS_PhonemeDuration)
        self.DoubleSpinBox_TTS_VITS_PhonemeDuration.setObjectName(u"DoubleSpinBox_TTS_VITS_PhonemeDuration")
        self.DoubleSpinBox_TTS_VITS_PhonemeDuration.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_TTS_VITS_PhonemeDuration.setStyleSheet(u"QDoubleSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	/*height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::down-arr"
                        "ow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_44.addWidget(self.DoubleSpinBox_TTS_VITS_PhonemeDuration)


        self.gridLayout_72.addWidget(self.ChildFrame_TTS_VITS_PhonemeDuration, 1, 0, 1, 3)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_PhonemeDuration)

        self.Frame_TTS_VITS_SpeechRate = QFrame(self.Frame_TTS_VITS_VITSParams_AdvanceSettings)
        self.Frame_TTS_VITS_SpeechRate.setObjectName(u"Frame_TTS_VITS_SpeechRate")
        self.Frame_TTS_VITS_SpeechRate.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_SpeechRate.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_73 = QGridLayout(self.Frame_TTS_VITS_SpeechRate)
        self.gridLayout_73.setSpacing(12)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.gridLayout_73.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_SpeechRate = QLabel(self.Frame_TTS_VITS_SpeechRate)
        self.Label_TTS_VITS_SpeechRate.setObjectName(u"Label_TTS_VITS_SpeechRate")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_SpeechRate.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_SpeechRate.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_SpeechRate.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_73.addWidget(self.Label_TTS_VITS_SpeechRate, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_SpeechRate = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_73.addItem(self.HorizontalSpacer_TTS_VITS_SpeechRate, 0, 1, 1, 1)

        self.Button_TTS_VITS_SpeechRate_Undo = QPushButton(self.Frame_TTS_VITS_SpeechRate)
        self.Button_TTS_VITS_SpeechRate_Undo.setObjectName(u"Button_TTS_VITS_SpeechRate_Undo")
        self.Button_TTS_VITS_SpeechRate_Undo.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_SpeechRate_Undo.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_SpeechRate_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_73.addWidget(self.Button_TTS_VITS_SpeechRate_Undo, 0, 2, 1, 1)

        self.ChildFrame_TTS_VITS_SpeechRate = QFrame(self.Frame_TTS_VITS_SpeechRate)
        self.ChildFrame_TTS_VITS_SpeechRate.setObjectName(u"ChildFrame_TTS_VITS_SpeechRate")
        sizePolicy5.setHeightForWidth(self.ChildFrame_TTS_VITS_SpeechRate.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_SpeechRate.setSizePolicy(sizePolicy5)
        self.ChildFrame_TTS_VITS_SpeechRate.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_45 = QHBoxLayout(self.ChildFrame_TTS_VITS_SpeechRate)
        self.horizontalLayout_45.setSpacing(12)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSlider_TTS_VITS_SpeechRate = QSlider(self.ChildFrame_TTS_VITS_SpeechRate)
        self.HorizontalSlider_TTS_VITS_SpeechRate.setObjectName(u"HorizontalSlider_TTS_VITS_SpeechRate")
        self.HorizontalSlider_TTS_VITS_SpeechRate.setMinimumSize(QSize(0, 27))
        self.HorizontalSlider_TTS_VITS_SpeechRate.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	height: 1.2px;\n"
"	background-color: rgba(201, 210, 222, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	background-color: rgba(201, 210, 222, 210);\n"
"	margin-top: -6px;\n"
"	margin-bottom: -6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	/*border-color: rgba(201, 210, 222, 123);*/\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color: rgba(210, 222, 234, 234);\n"
"	/*border-color: rgba(201, 210, 222, 210);*/\n"
"}")
        self.HorizontalSlider_TTS_VITS_SpeechRate.setOrientation(Qt.Horizontal)

        self.horizontalLayout_45.addWidget(self.HorizontalSlider_TTS_VITS_SpeechRate)

        self.DoubleSpinBox_TTS_VITS_SpeechRate = QDoubleSpinBox(self.ChildFrame_TTS_VITS_SpeechRate)
        self.DoubleSpinBox_TTS_VITS_SpeechRate.setObjectName(u"DoubleSpinBox_TTS_VITS_SpeechRate")
        self.DoubleSpinBox_TTS_VITS_SpeechRate.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_TTS_VITS_SpeechRate.setStyleSheet(u"QDoubleSpinBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	selection-background-color: darkgrey;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"	/*width: 9px;\n"
"	height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::up-arrow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"	/*width: 9px;\n"
"	/*height: 9px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: bottom right;\n"
"	margin-right: 4.5px;\n"
"	border-width: 0px;\n"
"}\n"
"QDoubleSpinBox::down-arr"
                        "ow {\n"
"	border-image: url(:/(Double)SpinBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_45.addWidget(self.DoubleSpinBox_TTS_VITS_SpeechRate)


        self.gridLayout_73.addWidget(self.ChildFrame_TTS_VITS_SpeechRate, 1, 0, 1, 3)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_SpeechRate)


        self.verticalLayout_117.addWidget(self.Frame_TTS_VITS_VITSParams_AdvanceSettings)


        self.verticalLayout_19.addWidget(self.GroupBox_TTS_VITS_VITSParams)

        self.GroupBox_TTS_VITS_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.GroupBox_TTS_VITS_OutputParams.setObjectName(u"GroupBox_TTS_VITS_OutputParams")
        self.GroupBox_TTS_VITS_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QGroupBox::title {\n"
"	left: 9px;\n"
"	margin-left: 0px;\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 3px;\n"
"}")
        self.verticalLayout_156 = QVBoxLayout(self.GroupBox_TTS_VITS_OutputParams)
        self.verticalLayout_156.setSpacing(0)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(0, 12, 0, 12)
        self.Frame_TTS_VITS_OutputParams_BasicSettings = QFrame(self.GroupBox_TTS_VITS_OutputParams)
        self.Frame_TTS_VITS_OutputParams_BasicSettings.setObjectName(u"Frame_TTS_VITS_OutputParams_BasicSettings")
        self.verticalLayout_158 = QVBoxLayout(self.Frame_TTS_VITS_OutputParams_BasicSettings)
        self.verticalLayout_158.setSpacing(0)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_VITS_AudioPathSave = QFrame(self.Frame_TTS_VITS_OutputParams_BasicSettings)
        self.Frame_TTS_VITS_AudioPathSave.setObjectName(u"Frame_TTS_VITS_AudioPathSave")
        self.Frame_TTS_VITS_AudioPathSave.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_AudioPathSave.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}")
        self.gridLayout_74 = QGridLayout(self.Frame_TTS_VITS_AudioPathSave)
        self.gridLayout_74.setSpacing(12)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.gridLayout_74.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_AudioPathSave = QLabel(self.Frame_TTS_VITS_AudioPathSave)
        self.Label_TTS_VITS_AudioPathSave.setObjectName(u"Label_TTS_VITS_AudioPathSave")
        sizePolicy5.setHeightForWidth(self.Label_TTS_VITS_AudioPathSave.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_AudioPathSave.setSizePolicy(sizePolicy5)
        self.Label_TTS_VITS_AudioPathSave.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_74.addWidget(self.Label_TTS_VITS_AudioPathSave, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_AudioPathSave = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_74.addItem(self.HorizontalSpacer_TTS_VITS_AudioPathSave, 0, 1, 1, 1)

        self.Button_TTS_VITS_AudioPathSave_Undo = QPushButton(self.Frame_TTS_VITS_AudioPathSave)
        self.Button_TTS_VITS_AudioPathSave_Undo.setObjectName(u"Button_TTS_VITS_AudioPathSave_Undo")
        self.Button_TTS_VITS_AudioPathSave_Undo.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_AudioPathSave_Undo.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_AudioPathSave_Undo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Undo.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_74.addWidget(self.Button_TTS_VITS_AudioPathSave_Undo, 0, 2, 1, 1)

        self.LineEdit_TTS_VITS_AudioPathSave = LineEditBase(self.Frame_TTS_VITS_AudioPathSave)
        self.LineEdit_TTS_VITS_AudioPathSave.setObjectName(u"LineEdit_TTS_VITS_AudioPathSave")
        self.LineEdit_TTS_VITS_AudioPathSave.setMinimumSize(QSize(0, 27))

        self.gridLayout_74.addWidget(self.LineEdit_TTS_VITS_AudioPathSave, 1, 0, 1, 3)


        self.verticalLayout_158.addWidget(self.Frame_TTS_VITS_AudioPathSave)


        self.verticalLayout_156.addWidget(self.Frame_TTS_VITS_OutputParams_BasicSettings)


        self.verticalLayout_19.addWidget(self.GroupBox_TTS_VITS_OutputParams)

        self.VerticalSpacer_TTS_VITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.VerticalSpacer_TTS_VITS)

        self.ScrollArea_Middle_TTS_VITS.setWidget(self.ScrollArea_Middle_WidgetContents_TTS_VITS)

        self.gridLayout_20.addWidget(self.ScrollArea_Middle_TTS_VITS, 0, 1, 1, 1)

        self.Widget_Right_TTS_VITS = QWidget(self.Subpage_TTS_VITS)
        self.Widget_Right_TTS_VITS.setObjectName(u"Widget_Right_TTS_VITS")
        self.Widget_Right_TTS_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout_18 = QGridLayout(self.Widget_Right_TTS_VITS)
        self.gridLayout_18.setSpacing(12)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_TTS_VITS = QTextBrowser(self.Widget_Right_TTS_VITS)
        self.TextBrowser_Params_TTS_VITS.setObjectName(u"TextBrowser_Params_TTS_VITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_TTS_VITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_TTS_VITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_TTS_VITS.setStyleSheet(u"QTextBrowser {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"	/*padding-top: 1.5px;*/\n"
"	/*padding-bottom: 1.5px;*/\n"
"	padding-left: 15px;\n"
"	padding-right: 6px;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color:transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	bord"
                        "er-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px"
                        ";\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_18.addWidget(self.TextBrowser_Params_TTS_VITS, 0, 0, 1, 1)

        self.Button_CheckOutput_TTS_VITS = QPushButton(self.Widget_Right_TTS_VITS)
        self.Button_CheckOutput_TTS_VITS.setObjectName(u"Button_CheckOutput_TTS_VITS")
        self.Button_CheckOutput_TTS_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 9.9px;\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_18.addWidget(self.Button_CheckOutput_TTS_VITS, 1, 0, 1, 1)


        self.gridLayout_20.addWidget(self.Widget_Right_TTS_VITS, 0, 2, 1, 1)

        self.ProgressBar_TTS_VITS = QProgressBar(self.Subpage_TTS_VITS)
        self.ProgressBar_TTS_VITS.setObjectName(u"ProgressBar_TTS_VITS")
        self.ProgressBar_TTS_VITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_TTS_VITS.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(60, 60, 60);\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(60, 60, 60), stop:1  rgb(123, 123, 123));\n"
"}")
        self.ProgressBar_TTS_VITS.setValue(0)
        self.ProgressBar_TTS_VITS.setTextVisible(False)
        self.horizontalLayout_48 = QHBoxLayout(self.ProgressBar_TTS_VITS)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_TTS_VITS = QStackedWidget(self.ProgressBar_TTS_VITS)
        self.StackedWidget_TTS_VITS.setObjectName(u"StackedWidget_TTS_VITS")
        self.StackedWidget_TTS_VITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_TTS_VITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_TTS_VITS_Execute = QWidget()
        self.Page_TTS_VITS_Execute.setObjectName(u"Page_TTS_VITS_Execute")
        self.verticalLayout_112 = QVBoxLayout(self.Page_TTS_VITS_Execute)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.Button_TTS_VITS_Execute = QPushButton(self.Page_TTS_VITS_Execute)
        self.Button_TTS_VITS_Execute.setObjectName(u"Button_TTS_VITS_Execute")
        sizePolicy3.setHeightForWidth(self.Button_TTS_VITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_TTS_VITS_Execute.setSizePolicy(sizePolicy3)
        self.Button_TTS_VITS_Execute.setMinimumSize(QSize(0, 30))
        self.Button_TTS_VITS_Execute.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_112.addWidget(self.Button_TTS_VITS_Execute)

        self.StackedWidget_TTS_VITS.addWidget(self.Page_TTS_VITS_Execute)
        self.Page_TTS_VITS_Terminate = QWidget()
        self.Page_TTS_VITS_Terminate.setObjectName(u"Page_TTS_VITS_Terminate")
        self.verticalLayout_113 = QVBoxLayout(self.Page_TTS_VITS_Terminate)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.Button_TTS_VITS_Terminate = QPushButton(self.Page_TTS_VITS_Terminate)
        self.Button_TTS_VITS_Terminate.setObjectName(u"Button_TTS_VITS_Terminate")
        sizePolicy3.setHeightForWidth(self.Button_TTS_VITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_TTS_VITS_Terminate.setSizePolicy(sizePolicy3)
        self.Button_TTS_VITS_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_TTS_VITS_Terminate.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgba(255, 255, 255, 240);\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_113.addWidget(self.Button_TTS_VITS_Terminate)

        self.StackedWidget_TTS_VITS.addWidget(self.Page_TTS_VITS_Terminate)

        self.horizontalLayout_48.addWidget(self.StackedWidget_TTS_VITS)


        self.gridLayout_20.addWidget(self.ProgressBar_TTS_VITS, 1, 0, 1, 3)

        self.gridLayout_20.setColumnStretch(0, 3)
        self.gridLayout_20.setColumnStretch(1, 10)
        self.gridLayout_20.setColumnStretch(2, 7)
        self.StackedWidget_Pages_TTS.addWidget(self.Subpage_TTS_VITS)

        self.verticalLayout_42.addWidget(self.StackedWidget_Pages_TTS)

        self.StackedWidget_Pages.addWidget(self.Page_TTS)
        self.Page_Settings = QWidget()
        self.Page_Settings.setObjectName(u"Page_Settings")
        self.verticalLayout_109 = QVBoxLayout(self.Page_Settings)
        self.verticalLayout_109.setSpacing(21)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(21, 12, 21, 12)
        self.Frame_Settings_Top = QFrame(self.Page_Settings)
        self.Frame_Settings_Top.setObjectName(u"Frame_Settings_Top")
        self.Frame_Settings_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Settings_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.Frame_Settings_Top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_Settings_Title = QToolButton(self.Frame_Settings_Top)
        self.ToolButton_Settings_Title.setObjectName(u"ToolButton_Settings_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_Settings_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_Settings_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_Settings_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}/*\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}*/\n"
"\n"
"QToolTip {\n"
"	co"
                        "lor: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_4.addWidget(self.ToolButton_Settings_Title)

        self.Frame_Settings_Title_Spacer = QLabel(self.Frame_Settings_Top)
        self.Frame_Settings_Title_Spacer.setObjectName(u"Frame_Settings_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_Settings_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Settings_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_Settings_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;*/\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_4.addWidget(self.Frame_Settings_Title_Spacer)


        self.verticalLayout_109.addWidget(self.Frame_Settings_Top)

        self.Frame_Settings_Middle = QFrame(self.Page_Settings)
        self.Frame_Settings_Middle.setObjectName(u"Frame_Settings_Middle")
        self.Frame_Settings_Middle.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.Frame_Settings_Middle)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Frame_Setting_Language = QFrame(self.Frame_Settings_Middle)
        self.Frame_Setting_Language.setObjectName(u"Frame_Setting_Language")
        self.Frame_Setting_Language.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_Language.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.horizontalLayout_66 = QHBoxLayout(self.Frame_Setting_Language)
        self.horizontalLayout_66.setSpacing(12)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_Language = QLabel(self.Frame_Setting_Language)
        self.Label_Setting_Language.setObjectName(u"Label_Setting_Language")
        self.Label_Setting_Language.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_66.addWidget(self.Label_Setting_Language)

        self.HorizontalSpacer_Setting_Language = QSpacerItem(969, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_66.addItem(self.HorizontalSpacer_Setting_Language)

        self.ComboBox_Setting_Language = QComboBox(self.Frame_Setting_Language)
        self.ComboBox_Setting_Language.setObjectName(u"ComboBox_Setting_Language")
        self.ComboBox_Setting_Language.setMinimumSize(QSize(123, 0))
        self.ComboBox_Setting_Language.setMaximumSize(QSize(123, 16777215))
        self.ComboBox_Setting_Language.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"QComboBox:hover {\n"
"	border-color: rgba(201, 210, 222, 210);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	/*width: 12px;\n"
"	height: 12px;*/\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	margin-right: 6px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"	border-image: url(:/ComboBox_Icon/Sources/UpArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgba(201, 210, 222, 123);\n"
"}\n"
"\n"
"QCom"
                        "boBox QAbstractItemView::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-top: 3px;\n"
"	padding-left: 6px;\n"
"	padding-bottom: 3px;\n"
"	padding-right: 6px;\n"
"	border: none;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
""
                        "	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:vertical, QComboBox QAbstractScrollArea QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	borde"
                        "r-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-page:horizontal, QComboBox QAbstractScrollArea QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	"
                        "border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_66.addWidget(self.ComboBox_Setting_Language)


        self.verticalLayout_13.addWidget(self.Frame_Setting_Language)

        self.Frame_Setting_AutoUpdate = QFrame(self.Frame_Settings_Middle)
        self.Frame_Setting_AutoUpdate.setObjectName(u"Frame_Setting_AutoUpdate")
        self.Frame_Setting_AutoUpdate.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_AutoUpdate.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.horizontalLayout_65 = QHBoxLayout(self.Frame_Setting_AutoUpdate)
        self.horizontalLayout_65.setSpacing(12)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_AutoUpdate = QLabel(self.Frame_Setting_AutoUpdate)
        self.Label_Setting_AutoUpdate.setObjectName(u"Label_Setting_AutoUpdate")
        self.Label_Setting_AutoUpdate.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_65.addWidget(self.Label_Setting_AutoUpdate)

        self.HorizontalSpacer_Setting_AutoUpdate = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_65.addItem(self.HorizontalSpacer_Setting_AutoUpdate)

        self.CheckBox_Setting_AutoUpdate = QCheckBox(self.Frame_Setting_AutoUpdate)
        self.CheckBox_Setting_AutoUpdate.setObjectName(u"CheckBox_Setting_AutoUpdate")
        sizePolicy5.setHeightForWidth(self.CheckBox_Setting_AutoUpdate.sizePolicy().hasHeightForWidth())
        self.CheckBox_Setting_AutoUpdate.setSizePolicy(sizePolicy5)
        self.CheckBox_Setting_AutoUpdate.setMinimumSize(QSize(123, 0))
        self.CheckBox_Setting_AutoUpdate.setMaximumSize(QSize(123, 16777215))
        self.CheckBox_Setting_AutoUpdate.setStyleSheet(u"QCheckBox {\n"
"	font-size: 15px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 30px;\n"
"	height: 30px;\n"
"    background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_65.addWidget(self.CheckBox_Setting_AutoUpdate)


        self.verticalLayout_13.addWidget(self.Frame_Setting_AutoUpdate)

        self.Frame_Setting_Synchronizer = QFrame(self.Frame_Settings_Middle)
        self.Frame_Setting_Synchronizer.setObjectName(u"Frame_Setting_Synchronizer")
        self.Frame_Setting_Synchronizer.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_Synchronizer.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.horizontalLayout_67 = QHBoxLayout(self.Frame_Setting_Synchronizer)
        self.horizontalLayout_67.setSpacing(12)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_Synchronizer = QLabel(self.Frame_Setting_Synchronizer)
        self.Label_Setting_Synchronizer.setObjectName(u"Label_Setting_Synchronizer")
        self.Label_Setting_Synchronizer.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_67.addWidget(self.Label_Setting_Synchronizer)

        self.HorizontalSpacer_Setting_Synchronizer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_67.addItem(self.HorizontalSpacer_Setting_Synchronizer)

        self.CheckBox_Setting_Synchronizer = QCheckBox(self.Frame_Setting_Synchronizer)
        self.CheckBox_Setting_Synchronizer.setObjectName(u"CheckBox_Setting_Synchronizer")
        sizePolicy5.setHeightForWidth(self.CheckBox_Setting_Synchronizer.sizePolicy().hasHeightForWidth())
        self.CheckBox_Setting_Synchronizer.setSizePolicy(sizePolicy5)
        self.CheckBox_Setting_Synchronizer.setMinimumSize(QSize(123, 0))
        self.CheckBox_Setting_Synchronizer.setMaximumSize(QSize(123, 16777215))
        self.CheckBox_Setting_Synchronizer.setStyleSheet(u"QCheckBox {\n"
"	font-size: 15px;\n"
"	spacing: 12.3px;\n"
"	color: rgba(255, 255, 255, 210);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 30px;\n"
"	height: 30px;\n"
"    background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 21);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOff.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/ToggleOn.png);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_67.addWidget(self.CheckBox_Setting_Synchronizer)


        self.verticalLayout_13.addWidget(self.Frame_Setting_Synchronizer)

        self.Frame_Setting_Operation = QFrame(self.Frame_Settings_Middle)
        self.Frame_Setting_Operation.setObjectName(u"Frame_Setting_Operation")
        self.Frame_Setting_Operation.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_Operation.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.Frame_Setting_Operation)
        self.horizontalLayout_6.setSpacing(42)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(21, 12, 21, 12)
        self.Button_Setting_ClientRebooter = QPushButton(self.Frame_Setting_Operation)
        self.Button_Setting_ClientRebooter.setObjectName(u"Button_Setting_ClientRebooter")
        self.Button_Setting_ClientRebooter.setMinimumSize(QSize(123, 0))
        self.Button_Setting_ClientRebooter.setMaximumSize(QSize(123, 16777215))
        self.Button_Setting_ClientRebooter.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 12px;\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_6.addWidget(self.Button_Setting_ClientRebooter)

        self.Button_Setting_IntegrityChecker = QPushButton(self.Frame_Setting_Operation)
        self.Button_Setting_IntegrityChecker.setObjectName(u"Button_Setting_IntegrityChecker")
        self.Button_Setting_IntegrityChecker.setMinimumSize(QSize(123, 0))
        self.Button_Setting_IntegrityChecker.setMaximumSize(QSize(123, 16777215))
        self.Button_Setting_IntegrityChecker.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 12px;\n"
"	border-width: 1.5px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_6.addWidget(self.Button_Setting_IntegrityChecker)

        self.HorizontalSpacer_Setting_Operation = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.HorizontalSpacer_Setting_Operation)


        self.verticalLayout_13.addWidget(self.Frame_Setting_Operation)


        self.verticalLayout_109.addWidget(self.Frame_Settings_Middle)

        self.VerticalSpacer_Settings = QSpacerItem(20, 378, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_109.addItem(self.VerticalSpacer_Settings)

        self.StackedWidget_Pages.addWidget(self.Page_Settings)
        self.Page_Info = QWidget()
        self.Page_Info.setObjectName(u"Page_Info")
        self.verticalLayout_25 = QVBoxLayout(self.Page_Info)
        self.verticalLayout_25.setSpacing(21)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(21, 12, 21, 12)
        self.Frame_Info_Top = QFrame(self.Page_Info)
        self.Frame_Info_Top.setObjectName(u"Frame_Info_Top")
        self.Frame_Info_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Info_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_29 = QHBoxLayout(self.Frame_Info_Top)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_Info_Title = QToolButton(self.Frame_Info_Top)
        self.ToolButton_Info_Title.setObjectName(u"ToolButton_Info_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_Info_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_Info_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_Info_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
"	color: rgba(201, 210, 222, 210);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}/*\n"
"QToolButton:hover {\n"
"	color: rgba(210, 222, 234, 234);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	color: rgba(210, 222, 234, 255);\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}*/\n"
"\n"
"QToolTip {\n"
"	co"
                        "lor: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_29.addWidget(self.ToolButton_Info_Title)

        self.Frame_Info_Title_Spacer = QLabel(self.Frame_Info_Top)
        self.Frame_Info_Title_Spacer.setObjectName(u"Frame_Info_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_Info_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Info_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_Info_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;*/\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_29.addWidget(self.Frame_Info_Title_Spacer)


        self.verticalLayout_25.addWidget(self.Frame_Info_Top)

        self.Frame_Info_Middle = QFrame(self.Page_Info)
        self.Frame_Info_Middle.setObjectName(u"Frame_Info_Middle")
        self.Frame_Info_Middle.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.Frame_Info_Middle)
        self.verticalLayout_22.setSpacing(21)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(12, 0, 12, 0)
        self.TextBrowser_Text_Info = QTextBrowser(self.Frame_Info_Middle)
        self.TextBrowser_Text_Info.setObjectName(u"TextBrowser_Text_Info")
        self.TextBrowser_Text_Info.setStyleSheet(u"QTextBrowser {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"	border-radius: 6px;\n"
"}\n"
"QTextBrowser:hover {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-ra"
                        "dius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:hori"
                        "zontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: rgb(90, 90, 90);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")

        self.verticalLayout_22.addWidget(self.TextBrowser_Text_Info)


        self.verticalLayout_25.addWidget(self.Frame_Info_Middle)

        self.StackedWidget_Pages.addWidget(self.Page_Info)

        self.verticalLayout_5.addWidget(self.StackedWidget_Pages)

        self.Frame_Console = QFrame(self.Frame_Pages)
        self.Frame_Console.setObjectName(u"Frame_Console")
        self.Frame_Console.setMaximumSize(QSize(16777215, 0))
        self.Frame_Console.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(33, 33, 33, 99);\n"
"	border-width: 1.2px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}")
        self.verticalLayout_23 = QVBoxLayout(self.Frame_Console)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.Frame_Console_Top = QFrame(self.Frame_Console)
        self.Frame_Console_Top.setObjectName(u"Frame_Console_Top")
        self.Frame_Console_Top.setMinimumSize(QSize(0, 24))
        self.Frame_Console_Top.setMaximumSize(QSize(16777215, 24))
        self.Frame_Console_Top.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_14 = QHBoxLayout(self.Frame_Console_Top)
        self.horizontalLayout_14.setSpacing(21)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(21, 0, 21, 0)
        self.Button_Console_Title = QPushButton(self.Frame_Console_Top)
        self.Button_Console_Title.setObjectName(u"Button_Console_Title")
        self.Button_Console_Title.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_14.addWidget(self.Button_Console_Title)

        self.horizontalSpacer = QSpacerItem(826, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.Button_Console_Copy = QPushButton(self.Frame_Console_Top)
        self.Button_Console_Copy.setObjectName(u"Button_Console_Copy")
        self.Button_Console_Copy.setMaximumSize(QSize(24, 24))
        self.Button_Console_Copy.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/Clipboard.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
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

        self.horizontalLayout_14.addWidget(self.Button_Console_Copy)

        self.Button_Console_Clear = QPushButton(self.Frame_Console_Top)
        self.Button_Console_Clear.setObjectName(u"Button_Console_Clear")
        self.Button_Console_Clear.setMaximumSize(QSize(24, 24))
        self.Button_Console_Clear.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/Sources/TrashCan.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
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

        self.horizontalLayout_14.addWidget(self.Button_Console_Clear)

        self.Button_Console_Fold = QPushButton(self.Frame_Console_Top)
        self.Button_Console_Fold.setObjectName(u"Button_Console_Fold")
        self.Button_Console_Fold.setMaximumSize(QSize(24, 24))
        self.Button_Console_Fold.setStyleSheet(u"QPushButton {\n"
"	image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
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

        self.horizontalLayout_14.addWidget(self.Button_Console_Fold)


        self.verticalLayout_23.addWidget(self.Frame_Console_Top)

        self.ScrollArea_Console = QScrollArea(self.Frame_Console)
        self.ScrollArea_Console.setObjectName(u"ScrollArea_Console")
        self.ScrollArea_Console.setStyleSheet(u"QScrollArea QWidget {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-col"
                        "or: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	border-radius: 0p"
                        "x;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}")
        self.ScrollArea_Console.setWidgetResizable(True)
        self.ScrollAreaWidgetContents_Console = QWidget()
        self.ScrollAreaWidgetContents_Console.setObjectName(u"ScrollAreaWidgetContents_Console")
        self.ScrollAreaWidgetContents_Console.setGeometry(QRect(0, 0, 1057, 35))
        self.verticalLayout_50 = QVBoxLayout(self.ScrollAreaWidgetContents_Console)
        self.verticalLayout_50.setSpacing(21)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(21, 0, 21, 0)
        self.PlainTextEdit_Console = QPlainTextEdit(self.ScrollAreaWidgetContents_Console)
        self.PlainTextEdit_Console.setObjectName(u"PlainTextEdit_Console")
        self.PlainTextEdit_Console.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: transparent;\n"
"	padding: 1.5px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_50.addWidget(self.PlainTextEdit_Console)

        self.ScrollArea_Console.setWidget(self.ScrollAreaWidgetContents_Console)

        self.verticalLayout_23.addWidget(self.ScrollArea_Console)


        self.verticalLayout_5.addWidget(self.Frame_Console)


        self.horizontalLayout_2.addWidget(self.Frame_Pages)


        self.verticalLayout.addWidget(self.Content)

        self.StatusBar = QFrame(self.CentralWidget)
        self.StatusBar.setObjectName(u"StatusBar")
        self.StatusBar.setMinimumSize(QSize(0, 24))
        self.StatusBar.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_52 = QHBoxLayout(self.StatusBar)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.Frame_Bottom_Toggle_Console = QFrame(self.StatusBar)
        self.Frame_Bottom_Toggle_Console.setObjectName(u"Frame_Bottom_Toggle_Console")
        self.Frame_Bottom_Toggle_Console.setMinimumSize(QSize(48, 0))
        self.Frame_Bottom_Toggle_Console.setMaximumSize(QSize(48, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.Frame_Bottom_Toggle_Console)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Button_Toggle_Console = QPushButton(self.Frame_Bottom_Toggle_Console)
        self.Button_Toggle_Console.setObjectName(u"Button_Toggle_Console")
        sizePolicy.setHeightForWidth(self.Button_Toggle_Console.sizePolicy().hasHeightForWidth())
        self.Button_Toggle_Console.setSizePolicy(sizePolicy)
        self.Button_Toggle_Console.setStyleSheet(u"QPushButton {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	image: url(:/Button_Icon/Sources/Console.png);\n"
"	/*background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;*/\n"
"	background-color: transparent;\n"
"	border-width: 1.5px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}\n"
"QPushButton:checked {\n"
"	/*background-color: rgb(45, 45, 45);*/\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 255, 210);\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_6.addWidget(self.Button_Toggle_Console)


        self.horizontalLayout_52.addWidget(self.Frame_Bottom_Toggle_Console)

        self.Frame_Bottom_Left = QFrame(self.StatusBar)
        self.Frame_Bottom_Left.setObjectName(u"Frame_Bottom_Left")
        self.horizontalLayout = QHBoxLayout(self.Frame_Bottom_Left)
        self.horizontalLayout.setSpacing(21)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 0, 0, 0)
        self.Label_ToolsStatus = QLabel(self.Frame_Bottom_Left)
        self.Label_ToolsStatus.setObjectName(u"Label_ToolsStatus")
        self.Label_ToolsStatus.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	/*text-align: center;*/\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_49 = QHBoxLayout(self.Label_ToolsStatus)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(60, 0, 0, 0)

        self.horizontalLayout.addWidget(self.Label_ToolsStatus)

        self.HorizontalSpacer_Bottom_Left = QSpacerItem(182, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.HorizontalSpacer_Bottom_Left)


        self.horizontalLayout_52.addWidget(self.Frame_Bottom_Left)

        self.Frame_Bottom_Others = QFrame(self.StatusBar)
        self.Frame_Bottom_Others.setObjectName(u"Frame_Bottom_Others")
        self.Frame_Bottom_Others.setMinimumSize(QSize(666, 0))

        self.horizontalLayout_52.addWidget(self.Frame_Bottom_Others)

        self.Frame_Bottom_Right = QFrame(self.StatusBar)
        self.Frame_Bottom_Right.setObjectName(u"Frame_Bottom_Right")
        self.horizontalLayout_50 = QHBoxLayout(self.Frame_Bottom_Right)
        self.horizontalLayout_50.setSpacing(21)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 30, 0)
        self.Label_Usage_CPU = QLabel(self.Frame_Bottom_Right)
        self.Label_Usage_CPU.setObjectName(u"Label_Usage_CPU")
        self.Label_Usage_CPU.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	/*text-align: center;*/\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_62 = QHBoxLayout(self.Label_Usage_CPU)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(90, 0, 0, 0)

        self.horizontalLayout_50.addWidget(self.Label_Usage_CPU)

        self.Label_Usage_GPU = QLabel(self.Frame_Bottom_Right)
        self.Label_Usage_GPU.setObjectName(u"Label_Usage_GPU")
        self.Label_Usage_GPU.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	/*text-align: center;*/\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_64 = QHBoxLayout(self.Label_Usage_GPU)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(90, 0, 0, 0)

        self.horizontalLayout_50.addWidget(self.Label_Usage_GPU)

        self.Label_Version = QLabel(self.Frame_Bottom_Right)
        self.Label_Version.setObjectName(u"Label_Version")
        self.Label_Version.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	/*text-align: center;*/\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_51 = QHBoxLayout(self.Label_Version)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(90, 0, 0, 0)

        self.horizontalLayout_50.addWidget(self.Label_Version)


        self.horizontalLayout_52.addWidget(self.Frame_Bottom_Right)


        self.verticalLayout.addWidget(self.StatusBar)

        MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MainWindow)

        self.StackedWidget_Pages.setCurrentIndex(0)
        self.StackedWidget_Pages_Models.setCurrentIndex(0)
        self.StackedWidget_Pages_Process.setCurrentIndex(0)
        self.StackedWidget_Pages_ASR.setCurrentIndex(0)
        self.StackedWidget_Pages_STT.setCurrentIndex(0)
        self.StackedWidget_Pages_Dataset.setCurrentIndex(0)
        self.StackedWidget_DAT_VITS.setCurrentIndex(0)
        self.StackedWidget_Pages_Train.setCurrentIndex(0)
        self.StackedWidget_Train_VITS.setCurrentIndex(0)
        self.StackedWidget_Pages_TTS.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.Label_Title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Home_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Env_Install_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Models_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Process_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_ASR_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_STT_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Dataset_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Train_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_TTS_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Settings_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Info_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Demo_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Server_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Repo_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Donate_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_Env_Install_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Label_Env_Install_Aria2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_Aria2_Status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_FFmpeg.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_FFmpeg_Status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_Python.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_Python_Status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_PyReqs.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_PyReqs_Status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_Pytorch.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_Pytorch_Status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_Models_ASR_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_Models_STT_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_Models_TTS_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.TabWidget_Models_ASR.setTabText(self.TabWidget_Models_ASR.indexOf(self.Tab_Models_ASR_VPR), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabWidget_Models_STT.setTabText(self.TabWidget_Models_STT.indexOf(self.Tab_Models_STT_Whisper), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabWidget_Models_TTS.setTabText(self.TabWidget_Models_TTS.indexOf(self.Tab_Models_TTS_VITS), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.ToolButton_AudioProcessor_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem = self.TreeWidget_Catalogue_Process.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled = self.TreeWidget_Catalogue_Process.isSortingEnabled()
        self.TreeWidget_Catalogue_Process.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.TreeWidget_Catalogue_Process.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Process.setSortingEnabled(__sortingEnabled)

        self.GroupBox_Process_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_Process_MediaDirInput.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Process_AudioSlicerParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_Process_SliceAudio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Process_SliceAudio.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.CheckBox_Process_AudioSlicerParams_Toggle_AdvanceSettings.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Process_RMSThreshold.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_AudioLengthMin.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_SilentIntervalMin.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_HopSize.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_SilenceKeptMax.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Process_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_Process_MediaFormatOutput.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_MediaDirOutput.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Process_OutputParams_Toggle_AdvanceSettings.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Process_SampleRate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_SampleWidth.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_ToMono.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Process_ToMono.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolButton_VoiceIdentifier_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem3 = self.TreeWidget_Catalogue_ASR_VPR.headerItem()
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled1 = self.TreeWidget_Catalogue_ASR_VPR.isSortingEnabled()
        self.TreeWidget_Catalogue_ASR_VPR.setSortingEnabled(False)
        ___qtreewidgetitem4 = self.TreeWidget_Catalogue_ASR_VPR.topLevelItem(0)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_ASR_VPR.setSortingEnabled(__sortingEnabled1)

        self.GroupBox_ASR_VPR_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_ASR_VPR_AudioDirInput.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_StdAudioSpeaker.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_ASR_VPR_VPRParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_ASR_VPR_DecisionThreshold.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_ModelPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_ASR_VPR_VPRParams_Toggle_AdvanceSettings.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_ASR_VPR_ModelType.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_FeatureMethod.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_DurationOfAudio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_ASR_VPR_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_ASR_VPR_AudioSpeakersDataPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_VoiceTranscriber_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem6 = self.TreeWidget_Catalogue_STT_Whisper.headerItem()
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled2 = self.TreeWidget_Catalogue_STT_Whisper.isSortingEnabled()
        self.TreeWidget_Catalogue_STT_Whisper.setSortingEnabled(False)
        ___qtreewidgetitem7 = self.TreeWidget_Catalogue_STT_Whisper.topLevelItem(0)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_STT_Whisper.setSortingEnabled(__sortingEnabled2)

        self.GroupBox_STT_Whisper_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_STT_Whisper_AudioDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_STT_Whisper_WhisperParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_STT_Whisper_AddLanguageInfo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_STT_Whisper_AddLanguageInfo.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_STT_Whisper_ModelPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_STT_Whisper_WhisperParams_Toggle_AdvanceSettings.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_STT_Whisper_fp16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_STT_Whisper_fp16.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.CheckBox_STT_Whisper_ConditionOnPreviousText.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_STT_Whisper_ConditionOnPreviousText.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_STT_Whisper_Verbose.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_STT_Whisper_Verbose.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_STT_Whisper_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_STT_Whisper_SRTDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_DatasetCreator_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem9 = self.TreeWidget_Catalogue_DAT_VITS.headerItem()
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled3 = self.TreeWidget_Catalogue_DAT_VITS.isSortingEnabled()
        self.TreeWidget_Catalogue_DAT_VITS.setSortingEnabled(False)
        ___qtreewidgetitem10 = self.TreeWidget_Catalogue_DAT_VITS.topLevelItem(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_DAT_VITS.setSortingEnabled(__sortingEnabled3)

        self.GroupBox_DAT_VITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_DAT_VITS_AudioSpeakersDataPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_SRTDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_DAT_VITS_VITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_DAT_VITS_DataFormat.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_AddAuxiliaryData.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_DAT_VITS_AddAuxiliaryData.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_DAT_VITS_AuxiliaryDataPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_DAT_VITS_VITSParams_Toggle_AdvanceSettings.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_DAT_VITS_TrainRatio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_SampleRate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_SampleWidth.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_ToMono.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_DAT_VITS_ToMono.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_DAT_VITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_DAT_VITS_ToStandaloneForm.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_DAT_VITS_ToStandaloneForm.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_DAT_VITS_WAVDirSplit.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_FileListPathTraining.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_FileListPathValidation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_VoiceTrainer_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem12 = self.TreeWidget_Catalogue_Train_VITS.headerItem()
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled4 = self.TreeWidget_Catalogue_Train_VITS.isSortingEnabled()
        self.TreeWidget_Catalogue_Train_VITS.setSortingEnabled(False)
        ___qtreewidgetitem13 = self.TreeWidget_Catalogue_Train_VITS.topLevelItem(0)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Train_VITS.setSortingEnabled(__sortingEnabled4)

        self.GroupBox_Train_VITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_Train_VITS_FileListPathTraining.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_FileListPathValidation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Train_VITS_VITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_Train_VITS_Epochs.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_BatchSize.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_UsePretrainedModels.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_VITS_UsePretrainedModels.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Train_VITS_ModelPathPretrainedG.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_ModelPathPretrainedD.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_KeepOriginalSpeakers.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_VITS_KeepOriginalSpeakers.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Train_VITS_ConfigPathLoad.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_VITS_VITSParams_Toggle_AdvanceSettings.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Train_VITS_NumWorkers.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_VITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_Train_VITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_Train_VITS_EvalInterval.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_OutputDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_VoiceConverter_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem15 = self.TreeWidget_Catalogue_TTS_VITS.headerItem()
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled5 = self.TreeWidget_Catalogue_TTS_VITS.isSortingEnabled()
        self.TreeWidget_Catalogue_TTS_VITS.setSortingEnabled(False)
        ___qtreewidgetitem16 = self.TreeWidget_Catalogue_TTS_VITS.topLevelItem(0)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_TTS_VITS.setSortingEnabled(__sortingEnabled5)

        self.GroupBox_TTS_VITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_TTS_VITS_ConfigPathLoad.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_ModelPathLoad.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_TTS_VITS_VITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_TTS_VITS_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_Speaker.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_TTS_VITS_VITSParams_Toggle_AdvanceSettings.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_TTS_VITS_EmotionStrength.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_PhonemeDuration.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_SpeechRate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_TTS_VITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_TTS_VITS_AudioPathSave.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_Settings_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Label_Setting_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolButton_Info_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Console_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Label_ToolsStatus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Usage_CPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Usage_GPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        pass