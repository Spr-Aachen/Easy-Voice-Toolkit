from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtWidgets import *

from .Components import WidgetBase, MenuButton, LabelBase, LineEditBase, ComboBoxBase, SpinBoxBase, DoubleSpinBoxBase, ToolBoxBase, ScrollAreaBase, Table_ViewModels, Table_EditAudioSpeaker
from . import Sources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
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
"}")

        self.verticalLayout_2.addWidget(self.Button_Toggle_Menu)


        self.horizontalLayout_30.addWidget(self.Frame_Top_Toggle_Menu)

        self.Frame_Top = QFrame(self.TitleBar)
        self.Frame_Top.setObjectName(u"Frame_Top")
        self.horizontalLayout_11 = QHBoxLayout(self.Frame_Top)
        self.horizontalLayout_11.setSpacing(21)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSpacer_Right_Top = QSpacerItem(587, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.HorizontalSpacer_Right_Top)

        self.CheckBox_SwitchTheme = QCheckBox(self.Frame_Top)
        self.CheckBox_SwitchTheme.setObjectName(u"CheckBox_SwitchTheme")
        self.CheckBox_SwitchTheme.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 16.8px;\n"
"	height: 16.8px;\n"
"    background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"	background-color: rgba(255, 255, 255, 24);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/Moon.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/CheckBox_Icon/Sources/Sun.png);\n"
"}")

        self.horizontalLayout_11.addWidget(self.CheckBox_SwitchTheme)

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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_8.addWidget(self.Label_Menu_Home_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Home)

        self.Button_Menu_Env = QToolButton(self.Frame_Menu)
        self.Button_Menu_Env.setObjectName(u"Button_Menu_Env")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Env.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Env.setSizePolicy(sizePolicy1)
        self.Button_Menu_Env.setMinimumSize(QSize(0, 48))
        self.Button_Menu_Env.setStyleSheet(u"QToolButton {\n"
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
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.Button_Menu_Env)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Env_Install_Icon = QLabel(self.Button_Menu_Env)
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

        self.Label_Menu_Env_Install_Text = QLabel(self.Button_Menu_Env)
        self.Label_Menu_Env_Install_Text.setObjectName(u"Label_Menu_Env_Install_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_Env_Install_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_Env_Install_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_Env_Install_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_7.addWidget(self.Label_Menu_Env_Install_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Env)

        self.Button_Menu_Models = QToolButton(self.Frame_Menu)
        self.Button_Menu_Models.setObjectName(u"Button_Menu_Models")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Models.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Models.setSizePolicy(sizePolicy1)
        self.Button_Menu_Models.setMinimumSize(QSize(0, 48))
        self.Button_Menu_Models.setStyleSheet(u"QToolButton {\n"
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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.verticalLayout_100 = QVBoxLayout(self.Frame_High_Home)
        self.verticalLayout_100.setSpacing(21)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(12, 0, 12, 0)
        self.Label_Cover_Home = LabelBase(self.Frame_High_Home)
        self.Label_Cover_Home.setObjectName(u"Label_Cover_Home")
        sizePolicy.setHeightForWidth(self.Label_Cover_Home.sizePolicy().hasHeightForWidth())
        self.Label_Cover_Home.setSizePolicy(sizePolicy)
        self.Label_Cover_Home.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: grey;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QLabel:hover {\n"
"}")

        self.verticalLayout_100.addWidget(self.Label_Cover_Home)

        self.TextBrowser_Text_Home = QTextBrowser(self.Frame_High_Home)
        self.TextBrowser_Text_Home.setObjectName(u"TextBrowser_Text_Home")
        self.TextBrowser_Text_Home.setStyleSheet(u"QTextBrowser {\n"
"	/*text-align: center;*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"	border-radius: 6px;\n"
"}\n"
"QTextBrowser:hover {\n"
"}\n"
"\n"
"\n"
"QScrollBar::vertical {\n"
"	width: 9px;\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::vertical:hover {\n"
"	background-color: transparent;\n"
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
""
                        "	width: 0px;\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgba(120, 120, 120, 120);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgba(120, 120, 120, 210);\n"
"}\n"
"\n"
"\n"
"QScrollBar::horizontal {\n"
"	height: 9px;\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar::horizontal:hover {\n"
"	background-color: transparent;\n"
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
"	subcontrol-o"
                        "rigin: margin;\n"
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
"	background-color: rgba(120, 120, 120, 120);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgba(120, 120, 120, 210);\n"
"}")

        self.verticalLayout_100.addWidget(self.TextBrowser_Text_Home)


        self.verticalLayout_99.addWidget(self.Frame_High_Home)

        self.Frame_Low_Home = QFrame(self.Page_Home)
        self.Frame_Low_Home.setObjectName(u"Frame_Low_Home")
        self.Frame_Low_Home.setMinimumSize(QSize(0, 90))
        self.Frame_Low_Home.setStyleSheet(u"QFrame {\n"
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
        self.Page_Env = QWidget()
        self.Page_Env.setObjectName(u"Page_Env")
        self.verticalLayout_128 = QVBoxLayout(self.Page_Env)
        self.verticalLayout_128.setSpacing(21)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(21, 12, 21, 12)
        self.Frame_Env_Install_Top = QFrame(self.Page_Env)
        self.Frame_Env_Install_Top.setObjectName(u"Frame_Env_Install_Top")
        self.Frame_Env_Install_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Env_Install_Top.setStyleSheet(u"QFrame {\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
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
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")

        self.horizontalLayout_3.addWidget(self.Frame_Env_Install_Title_Spacer)


        self.verticalLayout_128.addWidget(self.Frame_Env_Install_Top)

        self.StackedWidget_Pages_Env = QStackedWidget(self.Page_Env)
        self.StackedWidget_Pages_Env.setObjectName(u"StackedWidget_Pages_Env")
        self.StackedWidget_Pages_Env.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.SubPage_Env_Install = QWidget()
        self.SubPage_Env_Install.setObjectName(u"SubPage_Env_Install")
        self.gridLayout_103 = QGridLayout(self.SubPage_Env_Install)
        self.gridLayout_103.setSpacing(12)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.gridLayout_103.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea_Env_Install = ScrollAreaBase(self.SubPage_Env_Install)
        self.ScrollArea_Env_Install.setObjectName(u"ScrollArea_Env_Install")
        self.ScrollArea_Env_Install.setWidgetResizable(True)
        self.ScrollAreaWidgetContents_Env_Install = QWidget()
        self.ScrollAreaWidgetContents_Env_Install.setObjectName(u"ScrollAreaWidgetContents_Env_Install")
        self.ScrollAreaWidgetContents_Env_Install.setGeometry(QRect(0, 0, 1026, 559))
        self.verticalLayout_130 = QVBoxLayout(self.ScrollAreaWidgetContents_Env_Install)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.Frame_Env_Install_Middle = QFrame(self.ScrollAreaWidgetContents_Env_Install)
        self.Frame_Env_Install_Middle.setObjectName(u"Frame_Env_Install_Middle")
        self.Frame_Env_Install_Middle.setStyleSheet(u"QFrame {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.verticalLayout_127 = QVBoxLayout(self.Frame_Env_Install_Middle)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.Frame_Env_Install_Aria2 = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_Aria2.setObjectName(u"Frame_Env_Install_Aria2")
        self.Frame_Env_Install_Aria2.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_Aria2.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_Aria2.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_118 = QGridLayout(self.Frame_Env_Install_Aria2)
        self.gridLayout_118.setSpacing(12)
        self.gridLayout_118.setObjectName(u"gridLayout_118")
        self.gridLayout_118.setContentsMargins(21, 12, 21, 12)
        self.Button_Install_Aria2 = QPushButton(self.Frame_Env_Install_Aria2)
        self.Button_Install_Aria2.setObjectName(u"Button_Install_Aria2")
        self.Button_Install_Aria2.setMaximumSize(QSize(33, 33))
        self.Button_Install_Aria2.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	image: url(:/Button_Icon/Sources/Refresh.png);\n"
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

        self.gridLayout_118.addWidget(self.Button_Install_Aria2, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_Aria2 = QProgressBar(self.Frame_Env_Install_Aria2)
        self.ProgressBar_Env_Install_Aria2.setObjectName(u"ProgressBar_Env_Install_Aria2")
        self.ProgressBar_Env_Install_Aria2.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Env_Install_Aria2.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
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

        self.gridLayout_118.addWidget(self.ProgressBar_Env_Install_Aria2, 1, 0, 1, 2)

        self.Label_Env_Install_Aria2_Status = QLabel(self.Frame_Env_Install_Aria2)
        self.Label_Env_Install_Aria2_Status.setObjectName(u"Label_Env_Install_Aria2_Status")
        sizePolicy2.setHeightForWidth(self.Label_Env_Install_Aria2_Status.sizePolicy().hasHeightForWidth())
        self.Label_Env_Install_Aria2_Status.setSizePolicy(sizePolicy2)
        self.Label_Env_Install_Aria2_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_118.addWidget(self.Label_Env_Install_Aria2_Status, 2, 0, 1, 2)

        self.Label_Env_Install_Aria2 = QLabel(self.Frame_Env_Install_Aria2)
        self.Label_Env_Install_Aria2.setObjectName(u"Label_Env_Install_Aria2")
        self.Label_Env_Install_Aria2.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_118.addWidget(self.Label_Env_Install_Aria2, 0, 0, 1, 2)


        self.verticalLayout_127.addWidget(self.Frame_Env_Install_Aria2)

        self.Frame_Env_Install_FFmpeg = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_FFmpeg.setObjectName(u"Frame_Env_Install_FFmpeg")
        self.Frame_Env_Install_FFmpeg.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_FFmpeg.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_FFmpeg.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_119 = QGridLayout(self.Frame_Env_Install_FFmpeg)
        self.gridLayout_119.setSpacing(12)
        self.gridLayout_119.setObjectName(u"gridLayout_119")
        self.gridLayout_119.setContentsMargins(21, 12, 21, 12)
        self.Button_Install_FFmpeg = QPushButton(self.Frame_Env_Install_FFmpeg)
        self.Button_Install_FFmpeg.setObjectName(u"Button_Install_FFmpeg")
        self.Button_Install_FFmpeg.setMaximumSize(QSize(33, 33))
        self.Button_Install_FFmpeg.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	image: url(:/Button_Icon/Sources/Refresh.png);\n"
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

        self.gridLayout_119.addWidget(self.Button_Install_FFmpeg, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_FFmpeg = QProgressBar(self.Frame_Env_Install_FFmpeg)
        self.ProgressBar_Env_Install_FFmpeg.setObjectName(u"ProgressBar_Env_Install_FFmpeg")
        self.ProgressBar_Env_Install_FFmpeg.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Env_Install_FFmpeg.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
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

        self.gridLayout_119.addWidget(self.ProgressBar_Env_Install_FFmpeg, 1, 0, 1, 2)

        self.Label_Env_Install_FFmpeg_Status = QLabel(self.Frame_Env_Install_FFmpeg)
        self.Label_Env_Install_FFmpeg_Status.setObjectName(u"Label_Env_Install_FFmpeg_Status")
        sizePolicy2.setHeightForWidth(self.Label_Env_Install_FFmpeg_Status.sizePolicy().hasHeightForWidth())
        self.Label_Env_Install_FFmpeg_Status.setSizePolicy(sizePolicy2)
        self.Label_Env_Install_FFmpeg_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_119.addWidget(self.Label_Env_Install_FFmpeg_Status, 2, 0, 1, 2)

        self.Label_Env_Install_FFmpeg = QLabel(self.Frame_Env_Install_FFmpeg)
        self.Label_Env_Install_FFmpeg.setObjectName(u"Label_Env_Install_FFmpeg")
        self.Label_Env_Install_FFmpeg.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_119.addWidget(self.Label_Env_Install_FFmpeg, 0, 0, 1, 2)


        self.verticalLayout_127.addWidget(self.Frame_Env_Install_FFmpeg)

        self.Frame_Env_Install_Python = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_Python.setObjectName(u"Frame_Env_Install_Python")
        self.Frame_Env_Install_Python.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_Python.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_Python.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_120 = QGridLayout(self.Frame_Env_Install_Python)
        self.gridLayout_120.setSpacing(12)
        self.gridLayout_120.setObjectName(u"gridLayout_120")
        self.gridLayout_120.setContentsMargins(21, 12, 21, 12)
        self.Button_Install_Python = QPushButton(self.Frame_Env_Install_Python)
        self.Button_Install_Python.setObjectName(u"Button_Install_Python")
        self.Button_Install_Python.setMaximumSize(QSize(33, 33))
        self.Button_Install_Python.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	image: url(:/Button_Icon/Sources/Refresh.png);\n"
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

        self.gridLayout_120.addWidget(self.Button_Install_Python, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_Python = QProgressBar(self.Frame_Env_Install_Python)
        self.ProgressBar_Env_Install_Python.setObjectName(u"ProgressBar_Env_Install_Python")
        self.ProgressBar_Env_Install_Python.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Env_Install_Python.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
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

        self.gridLayout_120.addWidget(self.ProgressBar_Env_Install_Python, 1, 0, 1, 2)

        self.Label_Env_Install_Python_Status = QLabel(self.Frame_Env_Install_Python)
        self.Label_Env_Install_Python_Status.setObjectName(u"Label_Env_Install_Python_Status")
        sizePolicy2.setHeightForWidth(self.Label_Env_Install_Python_Status.sizePolicy().hasHeightForWidth())
        self.Label_Env_Install_Python_Status.setSizePolicy(sizePolicy2)
        self.Label_Env_Install_Python_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_120.addWidget(self.Label_Env_Install_Python_Status, 2, 0, 1, 2)

        self.Label_Env_Install_Python = QLabel(self.Frame_Env_Install_Python)
        self.Label_Env_Install_Python.setObjectName(u"Label_Env_Install_Python")
        self.Label_Env_Install_Python.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_120.addWidget(self.Label_Env_Install_Python, 0, 0, 1, 2)


        self.verticalLayout_127.addWidget(self.Frame_Env_Install_Python)

        self.Frame_Env_Install_PyReqs = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_PyReqs.setObjectName(u"Frame_Env_Install_PyReqs")
        self.Frame_Env_Install_PyReqs.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_PyReqs.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_PyReqs.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_121 = QGridLayout(self.Frame_Env_Install_PyReqs)
        self.gridLayout_121.setSpacing(12)
        self.gridLayout_121.setObjectName(u"gridLayout_121")
        self.gridLayout_121.setContentsMargins(21, 12, 21, 12)
        self.Button_Install_PyReqs = QPushButton(self.Frame_Env_Install_PyReqs)
        self.Button_Install_PyReqs.setObjectName(u"Button_Install_PyReqs")
        self.Button_Install_PyReqs.setMaximumSize(QSize(33, 33))
        self.Button_Install_PyReqs.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	image: url(:/Button_Icon/Sources/Refresh.png);\n"
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

        self.gridLayout_121.addWidget(self.Button_Install_PyReqs, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_PyReqs = QProgressBar(self.Frame_Env_Install_PyReqs)
        self.ProgressBar_Env_Install_PyReqs.setObjectName(u"ProgressBar_Env_Install_PyReqs")
        self.ProgressBar_Env_Install_PyReqs.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Env_Install_PyReqs.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
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

        self.gridLayout_121.addWidget(self.ProgressBar_Env_Install_PyReqs, 1, 0, 1, 2)

        self.Label_Env_Install_PyReqs_Status = QLabel(self.Frame_Env_Install_PyReqs)
        self.Label_Env_Install_PyReqs_Status.setObjectName(u"Label_Env_Install_PyReqs_Status")
        sizePolicy2.setHeightForWidth(self.Label_Env_Install_PyReqs_Status.sizePolicy().hasHeightForWidth())
        self.Label_Env_Install_PyReqs_Status.setSizePolicy(sizePolicy2)
        self.Label_Env_Install_PyReqs_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_121.addWidget(self.Label_Env_Install_PyReqs_Status, 2, 0, 1, 2)

        self.Label_Env_Install_PyReqs = QLabel(self.Frame_Env_Install_PyReqs)
        self.Label_Env_Install_PyReqs.setObjectName(u"Label_Env_Install_PyReqs")
        self.Label_Env_Install_PyReqs.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_121.addWidget(self.Label_Env_Install_PyReqs, 0, 0, 1, 2)


        self.verticalLayout_127.addWidget(self.Frame_Env_Install_PyReqs)

        self.Frame_Env_Install_Pytorch = QFrame(self.Frame_Env_Install_Middle)
        self.Frame_Env_Install_Pytorch.setObjectName(u"Frame_Env_Install_Pytorch")
        self.Frame_Env_Install_Pytorch.setMinimumSize(QSize(0, 99))
        self.Frame_Env_Install_Pytorch.setMaximumSize(QSize(16777215, 99))
        self.Frame_Env_Install_Pytorch.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_122 = QGridLayout(self.Frame_Env_Install_Pytorch)
        self.gridLayout_122.setSpacing(12)
        self.gridLayout_122.setObjectName(u"gridLayout_122")
        self.gridLayout_122.setContentsMargins(21, 12, 21, 12)
        self.Button_Install_Pytorch = QPushButton(self.Frame_Env_Install_Pytorch)
        self.Button_Install_Pytorch.setObjectName(u"Button_Install_Pytorch")
        self.Button_Install_Pytorch.setMaximumSize(QSize(33, 33))
        self.Button_Install_Pytorch.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	image: url(:/Button_Icon/Sources/Refresh.png);\n"
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

        self.gridLayout_122.addWidget(self.Button_Install_Pytorch, 0, 2, 3, 1)

        self.ProgressBar_Env_Install_Pytorch = QProgressBar(self.Frame_Env_Install_Pytorch)
        self.ProgressBar_Env_Install_Pytorch.setObjectName(u"ProgressBar_Env_Install_Pytorch")
        self.ProgressBar_Env_Install_Pytorch.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Env_Install_Pytorch.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
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

        self.gridLayout_122.addWidget(self.ProgressBar_Env_Install_Pytorch, 1, 0, 1, 2)

        self.Label_Env_Install_Pytorch_Status = QLabel(self.Frame_Env_Install_Pytorch)
        self.Label_Env_Install_Pytorch_Status.setObjectName(u"Label_Env_Install_Pytorch_Status")
        sizePolicy2.setHeightForWidth(self.Label_Env_Install_Pytorch_Status.sizePolicy().hasHeightForWidth())
        self.Label_Env_Install_Pytorch_Status.setSizePolicy(sizePolicy2)
        self.Label_Env_Install_Pytorch_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_122.addWidget(self.Label_Env_Install_Pytorch_Status, 2, 0, 1, 2)

        self.Label_Env_Install_Pytorch = QLabel(self.Frame_Env_Install_Pytorch)
        self.Label_Env_Install_Pytorch.setObjectName(u"Label_Env_Install_Pytorch")
        self.Label_Env_Install_Pytorch.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_122.addWidget(self.Label_Env_Install_Pytorch, 0, 0, 1, 2)


        self.verticalLayout_127.addWidget(self.Frame_Env_Install_Pytorch)


        self.verticalLayout_130.addWidget(self.Frame_Env_Install_Middle)

        self.VerticalSpacer_Env_Install = QSpacerItem(17, 84, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_130.addItem(self.VerticalSpacer_Env_Install)

        self.ScrollArea_Env_Install.setWidget(self.ScrollAreaWidgetContents_Env_Install)

        self.gridLayout_103.addWidget(self.ScrollArea_Env_Install, 0, 0, 1, 1)

        self.StackedWidget_Pages_Env.addWidget(self.SubPage_Env_Install)
        self.SubPage_Env_Manage = QWidget()
        self.SubPage_Env_Manage.setObjectName(u"SubPage_Env_Manage")
        self.gridLayout_113 = QGridLayout(self.SubPage_Env_Manage)
        self.gridLayout_113.setSpacing(12)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.gridLayout_113.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea_Env_Manage = ScrollAreaBase(self.SubPage_Env_Manage)
        self.ScrollArea_Env_Manage.setObjectName(u"ScrollArea_Env_Manage")
        self.ScrollArea_Env_Manage.setWidgetResizable(True)
        self.ScrollAreaWidgetContents_Env_Manage = QWidget()
        self.ScrollAreaWidgetContents_Env_Manage.setObjectName(u"ScrollAreaWidgetContents_Env_Manage")
        self.ScrollAreaWidgetContents_Env_Manage.setGeometry(QRect(0, 0, 246, 218))
        self.verticalLayout_81 = QVBoxLayout(self.ScrollAreaWidgetContents_Env_Manage)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.GroupBox_Env_Manage_Pytorch = QGroupBox(self.ScrollAreaWidgetContents_Env_Manage)
        self.GroupBox_Env_Manage_Pytorch.setObjectName(u"GroupBox_Env_Manage_Pytorch")
        self.GroupBox_Env_Manage_Pytorch.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_105 = QVBoxLayout(self.GroupBox_Env_Manage_Pytorch)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 12, 0, 12)
        self.Frame_Env_Manage_Pytorch_Version = QFrame(self.GroupBox_Env_Manage_Pytorch)
        self.Frame_Env_Manage_Pytorch_Version.setObjectName(u"Frame_Env_Manage_Pytorch_Version")
        self.Frame_Env_Manage_Pytorch_Version.setMinimumSize(QSize(0, 90))
        self.Frame_Env_Manage_Pytorch_Version.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_67 = QHBoxLayout(self.Frame_Env_Manage_Pytorch_Version)
        self.horizontalLayout_67.setSpacing(12)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(21, 12, 21, 12)
        self.Label_Env_Manage_Pytorch_Version = QLabel(self.Frame_Env_Manage_Pytorch_Version)
        self.Label_Env_Manage_Pytorch_Version.setObjectName(u"Label_Env_Manage_Pytorch_Version")
        sizePolicy4.setHeightForWidth(self.Label_Env_Manage_Pytorch_Version.sizePolicy().hasHeightForWidth())
        self.Label_Env_Manage_Pytorch_Version.setSizePolicy(sizePolicy4)
        self.Label_Env_Manage_Pytorch_Version.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_67.addWidget(self.Label_Env_Manage_Pytorch_Version)

        self.ComboBox_Env_Manage_Pytorch_Version = ComboBoxBase(self.Frame_Env_Manage_Pytorch_Version)
        self.ComboBox_Env_Manage_Pytorch_Version.setObjectName(u"ComboBox_Env_Manage_Pytorch_Version")
        self.ComboBox_Env_Manage_Pytorch_Version.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_67.addWidget(self.ComboBox_Env_Manage_Pytorch_Version)


        self.verticalLayout_105.addWidget(self.Frame_Env_Manage_Pytorch_Version)

        self.Frame_Env_Manage_Pytorch_Install = QFrame(self.GroupBox_Env_Manage_Pytorch)
        self.Frame_Env_Manage_Pytorch_Install.setObjectName(u"Frame_Env_Manage_Pytorch_Install")
        self.Frame_Env_Manage_Pytorch_Install.setMinimumSize(QSize(0, 90))
        self.Frame_Env_Manage_Pytorch_Install.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_26 = QHBoxLayout(self.Frame_Env_Manage_Pytorch_Install)
        self.horizontalLayout_26.setSpacing(12)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(21, 12, 21, 12)
        self.HorizontalSpacer_Env_Manage_Pytorch_Install = QSpacerItem(844, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.HorizontalSpacer_Env_Manage_Pytorch_Install)

        self.Button_Env_Manage_Pytorch_Install = QPushButton(self.Frame_Env_Manage_Pytorch_Install)
        self.Button_Env_Manage_Pytorch_Install.setObjectName(u"Button_Env_Manage_Pytorch_Install")
        self.Button_Env_Manage_Pytorch_Install.setMinimumSize(QSize(123, 0))
        self.Button_Env_Manage_Pytorch_Install.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.horizontalLayout_26.addWidget(self.Button_Env_Manage_Pytorch_Install)


        self.verticalLayout_105.addWidget(self.Frame_Env_Manage_Pytorch_Install)


        self.verticalLayout_81.addWidget(self.GroupBox_Env_Manage_Pytorch)

        self.VerticalSpacer_Env_Manage = QSpacerItem(17, 250, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_81.addItem(self.VerticalSpacer_Env_Manage)

        self.ScrollArea_Env_Manage.setWidget(self.ScrollAreaWidgetContents_Env_Manage)

        self.gridLayout_113.addWidget(self.ScrollArea_Env_Manage, 0, 0, 1, 1)

        self.StackedWidget_Pages_Env.addWidget(self.SubPage_Env_Manage)

        self.verticalLayout_128.addWidget(self.StackedWidget_Pages_Env)

        self.StackedWidget_Pages.addWidget(self.Page_Env)
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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.Frame_Models_Top)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_Models_Process_Title = QToolButton(self.Frame_Models_Top)
        self.ToolButton_Models_Process_Title.setObjectName(u"ToolButton_Models_Process_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_Models_Process_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_Models_Process_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_Models_Process_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_18.addWidget(self.ToolButton_Models_Process_Title)

        self.ToolButton_Models_ASR_Title = QToolButton(self.Frame_Models_Top)
        self.ToolButton_Models_ASR_Title.setObjectName(u"ToolButton_Models_ASR_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_Models_ASR_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_Models_ASR_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_Models_ASR_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_18.addWidget(self.ToolButton_Models_ASR_Title)

        self.ToolButton_Models_STT_Title = QToolButton(self.Frame_Models_Top)
        self.ToolButton_Models_STT_Title.setObjectName(u"ToolButton_Models_STT_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_Models_STT_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_Models_STT_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_Models_STT_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_18.addWidget(self.ToolButton_Models_STT_Title)

        self.ToolButton_Models_TTS_Title = QToolButton(self.Frame_Models_Top)
        self.ToolButton_Models_TTS_Title.setObjectName(u"ToolButton_Models_TTS_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_Models_TTS_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_Models_TTS_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_Models_TTS_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_18.addWidget(self.ToolButton_Models_TTS_Title)

        self.Frame_Models_Title_Spacer = QFrame(self.Frame_Models_Top)
        self.Frame_Models_Title_Spacer.setObjectName(u"Frame_Models_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_Models_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Models_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_Models_Title_Spacer.setStyleSheet(u"QFrame {\n"
"	/*font-size: 24px;\n"
"	text-align: center;\n"
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
        self.horizontalLayout_27 = QHBoxLayout(self.Frame_Models_Title_Spacer)
        self.horizontalLayout_27.setSpacing(12)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSpacer_Models_Title_Spacer = QSpacerItem(549, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.HorizontalSpacer_Models_Title_Spacer)

        self.Button_Models_Refresh = QPushButton(self.Frame_Models_Title_Spacer)
        self.Button_Models_Refresh.setObjectName(u"Button_Models_Refresh")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Button_Models_Refresh.sizePolicy().hasHeightForWidth())
        self.Button_Models_Refresh.setSizePolicy(sizePolicy5)
        self.Button_Models_Refresh.setMinimumSize(QSize(84, 0))
        self.Button_Models_Refresh.setStyleSheet(u"QPushButton {\n"
"	font-size: 12pt;\n"
"	text-align: right;\n"
"	image-position: left;\n"
"	image: url(:/Button_Icon/Sources/Refresh.png);\n"
"	padding: 12px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(201, 210, 222, 33);\n"
"}")

        self.horizontalLayout_27.addWidget(self.Button_Models_Refresh)

        self.Button_Models_Append = QPushButton(self.Frame_Models_Title_Spacer)
        self.Button_Models_Append.setObjectName(u"Button_Models_Append")
        sizePolicy5.setHeightForWidth(self.Button_Models_Append.sizePolicy().hasHeightForWidth())
        self.Button_Models_Append.setSizePolicy(sizePolicy5)
        self.Button_Models_Append.setMinimumSize(QSize(84, 0))
        self.Button_Models_Append.setStyleSheet(u"QPushButton {\n"
"	font-size: 12pt;\n"
"	text-align: right;\n"
"	image-position: left;\n"
"	image: url(:/Button_Icon/Sources/Plus.png);\n"
"	padding: 12px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(201, 210, 222, 33);\n"
"}")

        self.horizontalLayout_27.addWidget(self.Button_Models_Append)


        self.horizontalLayout_18.addWidget(self.Frame_Models_Title_Spacer)


        self.verticalLayout_244.addWidget(self.Frame_Models_Top)

        self.StackedWidget_Pages_Models = QStackedWidget(self.Page_Models)
        self.StackedWidget_Pages_Models.setObjectName(u"StackedWidget_Pages_Models")
        self.StackedWidget_Pages_Models.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.SubPage_Models_Process = QWidget()
        self.SubPage_Models_Process.setObjectName(u"SubPage_Models_Process")
        self.gridLayout_102 = QGridLayout(self.SubPage_Models_Process)
        self.gridLayout_102.setSpacing(12)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.gridLayout_102.setContentsMargins(0, 0, 0, 0)
        self.TabWidget_Models_Process = QTabWidget(self.SubPage_Models_Process)
        self.TabWidget_Models_Process.setObjectName(u"TabWidget_Models_Process")
        self.TabWidget_Models_Process.setStyleSheet(u"QTabBar::tab {\n"
"    min-width: 84px;\n"
"	min-height: 42px;\n"
"	font-size: 21px;\n"
"	/*text-align: center;*/\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:hover, QTabBar::tab:selected {\n"
"	background-color: rgba(36, 36, 36, 36);\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"QTabWidget::pane {\n"
"	background: transparent;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}")
        self.Tab_Models_Process_UVR = QWidget()
        self.Tab_Models_Process_UVR.setObjectName(u"Tab_Models_Process_UVR")
        self.verticalLayout_75 = QVBoxLayout(self.Tab_Models_Process_UVR)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_Process_UVR = Table_ViewModels(self.Tab_Models_Process_UVR)
        self.Table_Models_Process_UVR.setObjectName(u"Table_Models_Process_UVR")

        self.verticalLayout_75.addWidget(self.Table_Models_Process_UVR)

        self.TabWidget_Models_Process.addTab(self.Tab_Models_Process_UVR, "")

        self.gridLayout_102.addWidget(self.TabWidget_Models_Process, 0, 0, 1, 1)

        self.StackedWidget_Pages_Models.addWidget(self.SubPage_Models_Process)
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
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:hover, QTabBar::tab:selected {\n"
"	background-color: rgba(36, 36, 36, 36);\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"QTabWidget::pane {\n"
"	background: transparent;\n"
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
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:hover, QTabBar::tab:selected {\n"
"	background-color: rgba(36, 36, 36, 36);\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"QTabWidget::pane {\n"
"	background: transparent;\n"
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
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
"	background-color: transparent;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}\n"
"QTabBar::tab:hover, QTabBar::tab:selected {\n"
"	background-color: rgba(36, 36, 36, 36);\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"QTabWidget::pane {\n"
"	background: transparent;\n"
"    border-width: 1.2px;\n"
"	border-style: solid;\n"
"	border-color: rgba(123, 123, 123, 123);\n"
"}")
        self.Tab_Models_TTS_GPTSoVITS = QWidget()
        self.Tab_Models_TTS_GPTSoVITS.setObjectName(u"Tab_Models_TTS_GPTSoVITS")
        self.verticalLayout_72 = QVBoxLayout(self.Tab_Models_TTS_GPTSoVITS)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_TTS_GPTSoVITS = Table_ViewModels(self.Tab_Models_TTS_GPTSoVITS)
        self.Table_Models_TTS_GPTSoVITS.setObjectName(u"Table_Models_TTS_GPTSoVITS")

        self.verticalLayout_72.addWidget(self.Table_Models_TTS_GPTSoVITS)

        self.TabWidget_Models_TTS.addTab(self.Tab_Models_TTS_GPTSoVITS, "")
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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_32 = QHBoxLayout(self.Frame_Process_Top)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_AudioProcessor_Title = QToolButton(self.Frame_Process_Top)
        self.ToolButton_AudioProcessor_Title.setObjectName(u"ToolButton_AudioProcessor_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_AudioProcessor_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_AudioProcessor_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_AudioProcessor_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_32.addWidget(self.ToolButton_AudioProcessor_Title)

        self.Frame_AudioProcessor_Title = QFrame(self.Frame_Process_Top)
        self.Frame_AudioProcessor_Title.setObjectName(u"Frame_AudioProcessor_Title")
        self.Frame_AudioProcessor_Title.setStyleSheet(u"QFrame {\n"
"	/*font-size: 24px;\n"
"	text-align: center;\n"
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
        self.horizontalLayout_31 = QHBoxLayout(self.Frame_AudioProcessor_Title)
        self.horizontalLayout_31.setSpacing(12)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSpacer_AudioProcessor_Title = QSpacerItem(549, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.HorizontalSpacer_AudioProcessor_Title)


        self.horizontalLayout_32.addWidget(self.Frame_AudioProcessor_Title)


        self.verticalLayout_40.addWidget(self.Frame_Process_Top)

        self.StackedWidget_Pages_Process = QStackedWidget(self.Page_Process)
        self.StackedWidget_Pages_Process.setObjectName(u"StackedWidget_Pages_Process")
        self.StackedWidget_Pages_Process.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
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
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal "
                        "{\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"}")

        self.verticalLayout_162.addWidget(self.TreeWidget_Catalogue_Process)


        self.gridLayout_6.addWidget(self.Widget_Left_Process, 0, 0, 1, 1)

        self.ScrollArea_Middle_Process = ScrollAreaBase(self.Subpage_Process)
        self.ScrollArea_Middle_Process.setObjectName(u"ScrollArea_Middle_Process")
        self.ScrollArea_Middle_Process.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_Process.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Process.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_Process = QWidget()
        self.ScrollArea_Middle_WidgetContents_Process.setObjectName(u"ScrollArea_Middle_WidgetContents_Process")
        self.ScrollArea_Middle_WidgetContents_Process.setGeometry(QRect(0, 0, 581, 1157))
        self.verticalLayout_14 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_Process)
        self.verticalLayout_14.setSpacing(12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_Process_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Process)
        self.GroupBox_Process_InputParams.setObjectName(u"GroupBox_Process_InputParams")
        self.GroupBox_Process_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_12 = QGridLayout(self.Frame_Process_MediaDirInput)
        self.gridLayout_12.setSpacing(12)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_MediaDirInput = QLabel(self.Frame_Process_MediaDirInput)
        self.Label_Process_MediaDirInput.setObjectName(u"Label_Process_MediaDirInput")
        sizePolicy5.setHeightForWidth(self.Label_Process_MediaDirInput.sizePolicy().hasHeightForWidth())
        self.Label_Process_MediaDirInput.setSizePolicy(sizePolicy5)
        self.Label_Process_MediaDirInput.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_12.addWidget(self.Label_Process_MediaDirInput, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_MediaDirInput = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.HorizontalSpacer_Process_MediaDirInput, 0, 1, 1, 1)

        self.Button_Process_MediaDirInput_MoreActions = MenuButton(self.Frame_Process_MediaDirInput)
        self.Button_Process_MediaDirInput_MoreActions.setObjectName(u"Button_Process_MediaDirInput_MoreActions")
        self.Button_Process_MediaDirInput_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_MediaDirInput_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_MediaDirInput_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_12.addWidget(self.Button_Process_MediaDirInput_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Process_MediaDirInput = LineEditBase(self.Frame_Process_MediaDirInput)
        self.LineEdit_Process_MediaDirInput.setObjectName(u"LineEdit_Process_MediaDirInput")
        self.LineEdit_Process_MediaDirInput.setMinimumSize(QSize(0, 27))

        self.gridLayout_12.addWidget(self.LineEdit_Process_MediaDirInput, 1, 0, 1, 3)


        self.verticalLayout_20.addWidget(self.Frame_Process_MediaDirInput)


        self.verticalLayout_150.addWidget(self.Frame_Process_InputParams_BasicSettings)


        self.verticalLayout_14.addWidget(self.GroupBox_Process_InputParams)

        self.GroupBox_Process_DenoiserParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Process)
        self.GroupBox_Process_DenoiserParams.setObjectName(u"GroupBox_Process_DenoiserParams")
        self.GroupBox_Process_DenoiserParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_74 = QVBoxLayout(self.GroupBox_Process_DenoiserParams)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 12, 0, 12)
        self.Frame_Process_DenoiserParams_BasicSettings = QFrame(self.GroupBox_Process_DenoiserParams)
        self.Frame_Process_DenoiserParams_BasicSettings.setObjectName(u"Frame_Process_DenoiserParams_BasicSettings")
        self.verticalLayout_73 = QVBoxLayout(self.Frame_Process_DenoiserParams_BasicSettings)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.Frame_Process_DenoiseAudio = QFrame(self.Frame_Process_DenoiserParams_BasicSettings)
        self.Frame_Process_DenoiseAudio.setObjectName(u"Frame_Process_DenoiseAudio")
        self.Frame_Process_DenoiseAudio.setMinimumSize(QSize(0, 105))
        self.Frame_Process_DenoiseAudio.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_90 = QGridLayout(self.Frame_Process_DenoiseAudio)
        self.gridLayout_90.setSpacing(12)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.gridLayout_90.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_DenoiseAudio = QLabel(self.Frame_Process_DenoiseAudio)
        self.Label_Process_DenoiseAudio.setObjectName(u"Label_Process_DenoiseAudio")
        sizePolicy5.setHeightForWidth(self.Label_Process_DenoiseAudio.sizePolicy().hasHeightForWidth())
        self.Label_Process_DenoiseAudio.setSizePolicy(sizePolicy5)
        self.Label_Process_DenoiseAudio.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_90.addWidget(self.Label_Process_DenoiseAudio, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_DenoiseAudio = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_90.addItem(self.HorizontalSpacer_Process_DenoiseAudio, 0, 1, 1, 1)

        self.Button_Process_DenoiseAudio_MoreActions = MenuButton(self.Frame_Process_DenoiseAudio)
        self.Button_Process_DenoiseAudio_MoreActions.setObjectName(u"Button_Process_DenoiseAudio_MoreActions")
        self.Button_Process_DenoiseAudio_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_DenoiseAudio_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_DenoiseAudio_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_90.addWidget(self.Button_Process_DenoiseAudio_MoreActions, 0, 2, 1, 1)

        self.CheckBox_Process_DenoiseAudio = QCheckBox(self.Frame_Process_DenoiseAudio)
        self.CheckBox_Process_DenoiseAudio.setObjectName(u"CheckBox_Process_DenoiseAudio")
        self.CheckBox_Process_DenoiseAudio.setMinimumSize(QSize(0, 27))
        self.CheckBox_Process_DenoiseAudio.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_90.addWidget(self.CheckBox_Process_DenoiseAudio, 1, 0, 1, 3)


        self.verticalLayout_73.addWidget(self.Frame_Process_DenoiseAudio)

        self.Frame_Process_DenoiseModelPath = QFrame(self.Frame_Process_DenoiserParams_BasicSettings)
        self.Frame_Process_DenoiseModelPath.setObjectName(u"Frame_Process_DenoiseModelPath")
        self.Frame_Process_DenoiseModelPath.setMinimumSize(QSize(0, 105))
        self.Frame_Process_DenoiseModelPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_92 = QGridLayout(self.Frame_Process_DenoiseModelPath)
        self.gridLayout_92.setSpacing(12)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.gridLayout_92.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_DenoiseModelPath = QLabel(self.Frame_Process_DenoiseModelPath)
        self.Label_Process_DenoiseModelPath.setObjectName(u"Label_Process_DenoiseModelPath")
        sizePolicy5.setHeightForWidth(self.Label_Process_DenoiseModelPath.sizePolicy().hasHeightForWidth())
        self.Label_Process_DenoiseModelPath.setSizePolicy(sizePolicy5)
        self.Label_Process_DenoiseModelPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_92.addWidget(self.Label_Process_DenoiseModelPath, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_DenoiseModelPath = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_92.addItem(self.HorizontalSpacer_Process_DenoiseModelPath, 0, 1, 1, 1)

        self.Button_Process_DenoiseModelPath_MoreActions = MenuButton(self.Frame_Process_DenoiseModelPath)
        self.Button_Process_DenoiseModelPath_MoreActions.setObjectName(u"Button_Process_DenoiseModelPath_MoreActions")
        self.Button_Process_DenoiseModelPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_DenoiseModelPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_DenoiseModelPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_92.addWidget(self.Button_Process_DenoiseModelPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Process_DenoiseModelPath = LineEditBase(self.Frame_Process_DenoiseModelPath)
        self.LineEdit_Process_DenoiseModelPath.setObjectName(u"LineEdit_Process_DenoiseModelPath")
        self.LineEdit_Process_DenoiseModelPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_92.addWidget(self.LineEdit_Process_DenoiseModelPath, 1, 0, 1, 3)


        self.verticalLayout_73.addWidget(self.Frame_Process_DenoiseModelPath)

        self.Frame_Process_DenoiseTarget = QFrame(self.Frame_Process_DenoiserParams_BasicSettings)
        self.Frame_Process_DenoiseTarget.setObjectName(u"Frame_Process_DenoiseTarget")
        self.Frame_Process_DenoiseTarget.setMinimumSize(QSize(0, 105))
        self.Frame_Process_DenoiseTarget.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_94 = QGridLayout(self.Frame_Process_DenoiseTarget)
        self.gridLayout_94.setSpacing(12)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.gridLayout_94.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_DenoiseTarget = QLabel(self.Frame_Process_DenoiseTarget)
        self.Label_Process_DenoiseTarget.setObjectName(u"Label_Process_DenoiseTarget")
        sizePolicy5.setHeightForWidth(self.Label_Process_DenoiseTarget.sizePolicy().hasHeightForWidth())
        self.Label_Process_DenoiseTarget.setSizePolicy(sizePolicy5)
        self.Label_Process_DenoiseTarget.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_94.addWidget(self.Label_Process_DenoiseTarget, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_DenoiseTarget = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_94.addItem(self.HorizontalSpacer_Process_DenoiseTarget, 0, 1, 1, 1)

        self.Button_Process_DenoiseTarget_MoreActions = MenuButton(self.Frame_Process_DenoiseTarget)
        self.Button_Process_DenoiseTarget_MoreActions.setObjectName(u"Button_Process_DenoiseTarget_MoreActions")
        self.Button_Process_DenoiseTarget_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_DenoiseTarget_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_DenoiseTarget_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_94.addWidget(self.Button_Process_DenoiseTarget_MoreActions, 0, 2, 1, 1)

        self.ComboBox_Process_DenoiseTarget = ComboBoxBase(self.Frame_Process_DenoiseTarget)
        self.ComboBox_Process_DenoiseTarget.setObjectName(u"ComboBox_Process_DenoiseTarget")
        self.ComboBox_Process_DenoiseTarget.setMinimumSize(QSize(0, 27))

        self.gridLayout_94.addWidget(self.ComboBox_Process_DenoiseTarget, 1, 0, 1, 3)


        self.verticalLayout_73.addWidget(self.Frame_Process_DenoiseTarget)


        self.verticalLayout_74.addWidget(self.Frame_Process_DenoiserParams_BasicSettings)


        self.verticalLayout_14.addWidget(self.GroupBox_Process_DenoiserParams)

        self.GroupBox_Process_SlicerParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Process)
        self.GroupBox_Process_SlicerParams.setObjectName(u"GroupBox_Process_SlicerParams")
        self.GroupBox_Process_SlicerParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_186 = QVBoxLayout(self.GroupBox_Process_SlicerParams)
        self.verticalLayout_186.setSpacing(0)
        self.verticalLayout_186.setObjectName(u"verticalLayout_186")
        self.verticalLayout_186.setContentsMargins(0, 12, 0, 12)
        self.Frame_Process_SlicerParams_BasicSettings = QFrame(self.GroupBox_Process_SlicerParams)
        self.Frame_Process_SlicerParams_BasicSettings.setObjectName(u"Frame_Process_SlicerParams_BasicSettings")
        self.verticalLayout_51 = QVBoxLayout(self.Frame_Process_SlicerParams_BasicSettings)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.Frame_Process_SliceAudio = QFrame(self.Frame_Process_SlicerParams_BasicSettings)
        self.Frame_Process_SliceAudio.setObjectName(u"Frame_Process_SliceAudio")
        self.Frame_Process_SliceAudio.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SliceAudio.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_13.addWidget(self.Label_Process_SliceAudio, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_SliceAudio = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.HorizontalSpacer_Process_SliceAudio, 0, 1, 1, 1)

        self.Button_Process_SliceAudio_MoreActions = MenuButton(self.Frame_Process_SliceAudio)
        self.Button_Process_SliceAudio_MoreActions.setObjectName(u"Button_Process_SliceAudio_MoreActions")
        self.Button_Process_SliceAudio_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_SliceAudio_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_SliceAudio_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_13.addWidget(self.Button_Process_SliceAudio_MoreActions, 0, 2, 1, 1)

        self.CheckBox_Process_SliceAudio = QCheckBox(self.Frame_Process_SliceAudio)
        self.CheckBox_Process_SliceAudio.setObjectName(u"CheckBox_Process_SliceAudio")
        self.CheckBox_Process_SliceAudio.setMinimumSize(QSize(0, 27))
        self.CheckBox_Process_SliceAudio.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_13.addWidget(self.CheckBox_Process_SliceAudio, 1, 0, 1, 3)


        self.verticalLayout_51.addWidget(self.Frame_Process_SliceAudio)


        self.verticalLayout_186.addWidget(self.Frame_Process_SlicerParams_BasicSettings)

        self.ToolBox_Process_SlicerParams_AdvanceSettings = ToolBoxBase(self.GroupBox_Process_SlicerParams)
        self.ToolBox_Process_SlicerParams_AdvanceSettings.setObjectName(u"ToolBox_Process_SlicerParams_AdvanceSettings")
        self.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content")
        self.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 538, 525))
        self.verticalLayout_54 = QVBoxLayout(self.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.Frame_Process_RMSThreshold = QFrame(self.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content)
        self.Frame_Process_RMSThreshold.setObjectName(u"Frame_Process_RMSThreshold")
        self.Frame_Process_RMSThreshold.setMinimumSize(QSize(0, 105))
        self.Frame_Process_RMSThreshold.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_17.addWidget(self.Label_Process_RMSThreshold, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_RMSThreshold = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.HorizontalSpacer_Process_RMSThreshold, 0, 1, 1, 1)

        self.Button_Process_RMSThreshold_MoreActions = MenuButton(self.Frame_Process_RMSThreshold)
        self.Button_Process_RMSThreshold_MoreActions.setObjectName(u"Button_Process_RMSThreshold_MoreActions")
        self.Button_Process_RMSThreshold_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_RMSThreshold_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_RMSThreshold_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_17.addWidget(self.Button_Process_RMSThreshold_MoreActions, 0, 2, 1, 1)

        self.DoubleSpinBox_Process_RMSThreshold = DoubleSpinBoxBase(self.Frame_Process_RMSThreshold)
        self.DoubleSpinBox_Process_RMSThreshold.setObjectName(u"DoubleSpinBox_Process_RMSThreshold")
        self.DoubleSpinBox_Process_RMSThreshold.setEnabled(True)
        self.DoubleSpinBox_Process_RMSThreshold.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_Process_RMSThreshold.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_Process_RMSThreshold.setMaximum(999999.000000000000000)

        self.gridLayout_17.addWidget(self.DoubleSpinBox_Process_RMSThreshold, 1, 0, 1, 3)


        self.verticalLayout_54.addWidget(self.Frame_Process_RMSThreshold)

        self.Frame_Process_AudioLengthMin = QFrame(self.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content)
        self.Frame_Process_AudioLengthMin.setObjectName(u"Frame_Process_AudioLengthMin")
        self.Frame_Process_AudioLengthMin.setMinimumSize(QSize(0, 105))
        self.Frame_Process_AudioLengthMin.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_23.addWidget(self.Label_Process_AudioLengthMin, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_AudioLengthMin = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.HorizontalSpacer_Process_AudioLengthMin, 0, 1, 1, 1)

        self.Button_Process_AudioLengthMin_MoreActions = MenuButton(self.Frame_Process_AudioLengthMin)
        self.Button_Process_AudioLengthMin_MoreActions.setObjectName(u"Button_Process_AudioLengthMin_MoreActions")
        self.Button_Process_AudioLengthMin_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_AudioLengthMin_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_AudioLengthMin_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_23.addWidget(self.Button_Process_AudioLengthMin_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Process_AudioLengthMin = SpinBoxBase(self.Frame_Process_AudioLengthMin)
        self.SpinBox_Process_AudioLengthMin.setObjectName(u"SpinBox_Process_AudioLengthMin")
        self.SpinBox_Process_AudioLengthMin.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_AudioLengthMin.setMinimum(-999999)
        self.SpinBox_Process_AudioLengthMin.setMaximum(999999)

        self.gridLayout_23.addWidget(self.SpinBox_Process_AudioLengthMin, 1, 0, 1, 3)


        self.verticalLayout_54.addWidget(self.Frame_Process_AudioLengthMin)

        self.Frame_Process_SilentIntervalMin = QFrame(self.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content)
        self.Frame_Process_SilentIntervalMin.setObjectName(u"Frame_Process_SilentIntervalMin")
        self.Frame_Process_SilentIntervalMin.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SilentIntervalMin.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_24.addWidget(self.Label_Process_SilentIntervalMin, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_SilentIntervalMin = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_24.addItem(self.HorizontalSpacer_Process_SilentIntervalMin, 0, 1, 1, 1)

        self.Button_Process_SilentIntervalMin_MoreActions = MenuButton(self.Frame_Process_SilentIntervalMin)
        self.Button_Process_SilentIntervalMin_MoreActions.setObjectName(u"Button_Process_SilentIntervalMin_MoreActions")
        self.Button_Process_SilentIntervalMin_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_SilentIntervalMin_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_SilentIntervalMin_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_24.addWidget(self.Button_Process_SilentIntervalMin_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Process_SilentIntervalMin = SpinBoxBase(self.Frame_Process_SilentIntervalMin)
        self.SpinBox_Process_SilentIntervalMin.setObjectName(u"SpinBox_Process_SilentIntervalMin")
        self.SpinBox_Process_SilentIntervalMin.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_SilentIntervalMin.setMinimum(-999999)
        self.SpinBox_Process_SilentIntervalMin.setMaximum(999999)

        self.gridLayout_24.addWidget(self.SpinBox_Process_SilentIntervalMin, 1, 0, 1, 3)


        self.verticalLayout_54.addWidget(self.Frame_Process_SilentIntervalMin)

        self.Frame_Process_HopSize = QFrame(self.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content)
        self.Frame_Process_HopSize.setObjectName(u"Frame_Process_HopSize")
        self.Frame_Process_HopSize.setMinimumSize(QSize(0, 105))
        self.Frame_Process_HopSize.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_25.addWidget(self.Label_Process_HopSize, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_HopSize = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.HorizontalSpacer_Process_HopSize, 0, 1, 1, 1)

        self.Button_Process_HopSize_MoreActions = MenuButton(self.Frame_Process_HopSize)
        self.Button_Process_HopSize_MoreActions.setObjectName(u"Button_Process_HopSize_MoreActions")
        self.Button_Process_HopSize_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_HopSize_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_HopSize_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_25.addWidget(self.Button_Process_HopSize_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Process_HopSize = SpinBoxBase(self.Frame_Process_HopSize)
        self.SpinBox_Process_HopSize.setObjectName(u"SpinBox_Process_HopSize")
        self.SpinBox_Process_HopSize.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_HopSize.setMinimum(-999999)
        self.SpinBox_Process_HopSize.setMaximum(999999)

        self.gridLayout_25.addWidget(self.SpinBox_Process_HopSize, 1, 0, 1, 3)


        self.verticalLayout_54.addWidget(self.Frame_Process_HopSize)

        self.Frame_Process_SilenceKeptMax = QFrame(self.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content)
        self.Frame_Process_SilenceKeptMax.setObjectName(u"Frame_Process_SilenceKeptMax")
        self.Frame_Process_SilenceKeptMax.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SilenceKeptMax.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_26.addWidget(self.Label_Process_SilenceKeptMax, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_SilenceKeptMax = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.HorizontalSpacer_Process_SilenceKeptMax, 0, 1, 1, 1)

        self.Button_Process_SilenceKeptMax_MoreActions = MenuButton(self.Frame_Process_SilenceKeptMax)
        self.Button_Process_SilenceKeptMax_MoreActions.setObjectName(u"Button_Process_SilenceKeptMax_MoreActions")
        self.Button_Process_SilenceKeptMax_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_SilenceKeptMax_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_SilenceKeptMax_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_26.addWidget(self.Button_Process_SilenceKeptMax_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Process_SilenceKeptMax = SpinBoxBase(self.Frame_Process_SilenceKeptMax)
        self.SpinBox_Process_SilenceKeptMax.setObjectName(u"SpinBox_Process_SilenceKeptMax")
        self.SpinBox_Process_SilenceKeptMax.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_SilenceKeptMax.setMinimum(-999999)
        self.SpinBox_Process_SilenceKeptMax.setMaximum(999999)

        self.gridLayout_26.addWidget(self.SpinBox_Process_SilenceKeptMax, 1, 0, 1, 3)


        self.verticalLayout_54.addWidget(self.Frame_Process_SilenceKeptMax)

        self.ToolBox_Process_SlicerParams_AdvanceSettings.addItem(self.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_186.addWidget(self.ToolBox_Process_SlicerParams_AdvanceSettings)


        self.verticalLayout_14.addWidget(self.GroupBox_Process_SlicerParams)

        self.GroupBox_Process_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Process)
        self.GroupBox_Process_OutputParams.setObjectName(u"GroupBox_Process_OutputParams")
        self.GroupBox_Process_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_27.addWidget(self.Label_Process_MediaFormatOutput, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_MediaFormatOutput = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.HorizontalSpacer_Process_MediaFormatOutput, 0, 1, 1, 1)

        self.Button_Process_MediaFormatOutput_MoreActions = MenuButton(self.Frame_Process_MediaFormatOutput)
        self.Button_Process_MediaFormatOutput_MoreActions.setObjectName(u"Button_Process_MediaFormatOutput_MoreActions")
        self.Button_Process_MediaFormatOutput_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_MediaFormatOutput_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_MediaFormatOutput_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_27.addWidget(self.Button_Process_MediaFormatOutput_MoreActions, 0, 2, 1, 1)

        self.ComboBox_Process_MediaFormatOutput = ComboBoxBase(self.Frame_Process_MediaFormatOutput)
        self.ComboBox_Process_MediaFormatOutput.setObjectName(u"ComboBox_Process_MediaFormatOutput")
        self.ComboBox_Process_MediaFormatOutput.setMinimumSize(QSize(0, 27))

        self.gridLayout_27.addWidget(self.ComboBox_Process_MediaFormatOutput, 1, 0, 1, 3)


        self.verticalLayout_61.addWidget(self.Frame_Process_MediaFormatOutput)

        self.Frame_Process_OutputDirName = QFrame(self.Frame_Process_OutputParams_BasicSettings)
        self.Frame_Process_OutputDirName.setObjectName(u"Frame_Process_OutputDirName")
        self.Frame_Process_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_Process_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_28 = QGridLayout(self.Frame_Process_OutputDirName)
        self.gridLayout_28.setSpacing(12)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_OutputDirName = QLabel(self.Frame_Process_OutputDirName)
        self.Label_Process_OutputDirName.setObjectName(u"Label_Process_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_Process_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_Process_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_Process_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_28.addWidget(self.Label_Process_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_OutputDirName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.HorizontalSpacer_Process_OutputDirName, 0, 1, 1, 1)

        self.Button_Process_OutputDirName_MoreActions = MenuButton(self.Frame_Process_OutputDirName)
        self.Button_Process_OutputDirName_MoreActions.setObjectName(u"Button_Process_OutputDirName_MoreActions")
        self.Button_Process_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_28.addWidget(self.Button_Process_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Process_OutputDirName = LineEditBase(self.Frame_Process_OutputDirName)
        self.LineEdit_Process_OutputDirName.setObjectName(u"LineEdit_Process_OutputDirName")
        self.LineEdit_Process_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_28.addWidget(self.LineEdit_Process_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_61.addWidget(self.Frame_Process_OutputDirName)


        self.verticalLayout_197.addWidget(self.Frame_Process_OutputParams_BasicSettings)

        self.ToolBox_Process_OutputParams_AdvanceSettings = ToolBoxBase(self.GroupBox_Process_OutputParams)
        self.ToolBox_Process_OutputParams_AdvanceSettings.setObjectName(u"ToolBox_Process_OutputParams_AdvanceSettings")
        self.ToolBox_Process_OutputParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_Process_OutputParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_Process_OutputParams_AdvanceSettings_Page1Content")
        self.ToolBox_Process_OutputParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 538, 315))
        self.verticalLayout_67 = QVBoxLayout(self.ToolBox_Process_OutputParams_AdvanceSettings_Page1Content)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.Frame_Process_SampleRate = QFrame(self.ToolBox_Process_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_Process_SampleRate.setObjectName(u"Frame_Process_SampleRate")
        self.Frame_Process_SampleRate.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SampleRate.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_29.addWidget(self.Label_Process_SampleRate, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_SampleRate = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.HorizontalSpacer_Process_SampleRate, 0, 1, 1, 1)

        self.Button_Process_SampleRate_MoreActions = MenuButton(self.Frame_Process_SampleRate)
        self.Button_Process_SampleRate_MoreActions.setObjectName(u"Button_Process_SampleRate_MoreActions")
        self.Button_Process_SampleRate_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_SampleRate_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_SampleRate_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_29.addWidget(self.Button_Process_SampleRate_MoreActions, 0, 2, 1, 1)

        self.ComboBox_Process_SampleRate = ComboBoxBase(self.Frame_Process_SampleRate)
        self.ComboBox_Process_SampleRate.setObjectName(u"ComboBox_Process_SampleRate")
        self.ComboBox_Process_SampleRate.setMinimumSize(QSize(0, 27))

        self.gridLayout_29.addWidget(self.ComboBox_Process_SampleRate, 1, 0, 1, 3)


        self.verticalLayout_67.addWidget(self.Frame_Process_SampleRate)

        self.Frame_Process_SampleWidth = QFrame(self.ToolBox_Process_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_Process_SampleWidth.setObjectName(u"Frame_Process_SampleWidth")
        self.Frame_Process_SampleWidth.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SampleWidth.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_30.addWidget(self.Label_Process_SampleWidth, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_SampleWidth = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.HorizontalSpacer_Process_SampleWidth, 0, 1, 1, 1)

        self.Button_Process_SampleWidth_MoreActions = MenuButton(self.Frame_Process_SampleWidth)
        self.Button_Process_SampleWidth_MoreActions.setObjectName(u"Button_Process_SampleWidth_MoreActions")
        self.Button_Process_SampleWidth_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_SampleWidth_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_SampleWidth_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_30.addWidget(self.Button_Process_SampleWidth_MoreActions, 0, 2, 1, 1)

        self.ComboBox_Process_SampleWidth = ComboBoxBase(self.Frame_Process_SampleWidth)
        self.ComboBox_Process_SampleWidth.setObjectName(u"ComboBox_Process_SampleWidth")
        self.ComboBox_Process_SampleWidth.setMinimumSize(QSize(0, 27))

        self.gridLayout_30.addWidget(self.ComboBox_Process_SampleWidth, 1, 0, 1, 3)


        self.verticalLayout_67.addWidget(self.Frame_Process_SampleWidth)

        self.Frame_Process_ToMono = QFrame(self.ToolBox_Process_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_Process_ToMono.setObjectName(u"Frame_Process_ToMono")
        self.Frame_Process_ToMono.setMinimumSize(QSize(0, 105))
        self.Frame_Process_ToMono.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_31.addWidget(self.Label_Process_ToMono, 0, 0, 1, 1)

        self.HorizontalSpacer_Process_ToMono = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.HorizontalSpacer_Process_ToMono, 0, 1, 1, 1)

        self.Button_Process_ToMono_MoreActions = MenuButton(self.Frame_Process_ToMono)
        self.Button_Process_ToMono_MoreActions.setObjectName(u"Button_Process_ToMono_MoreActions")
        self.Button_Process_ToMono_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Process_ToMono_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Process_ToMono_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_31.addWidget(self.Button_Process_ToMono_MoreActions, 0, 2, 1, 1)

        self.CheckBox_Process_ToMono = QCheckBox(self.Frame_Process_ToMono)
        self.CheckBox_Process_ToMono.setObjectName(u"CheckBox_Process_ToMono")
        self.CheckBox_Process_ToMono.setMinimumSize(QSize(0, 27))
        self.CheckBox_Process_ToMono.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_31.addWidget(self.CheckBox_Process_ToMono, 1, 0, 1, 3)


        self.verticalLayout_67.addWidget(self.Frame_Process_ToMono)

        self.ToolBox_Process_OutputParams_AdvanceSettings.addItem(self.ToolBox_Process_OutputParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_197.addWidget(self.ToolBox_Process_OutputParams_AdvanceSettings)


        self.verticalLayout_14.addWidget(self.GroupBox_Process_OutputParams)

        self.VerticalSpacer_Process = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.VerticalSpacer_Process)

        self.ScrollArea_Middle_Process.setWidget(self.ScrollArea_Middle_WidgetContents_Process)

        self.gridLayout_6.addWidget(self.ScrollArea_Middle_Process, 0, 1, 1, 1)

        self.Widget_Right_Process = QWidget(self.Subpage_Process)
        self.Widget_Right_Process.setObjectName(u"Widget_Right_Process")
        self.Widget_Right_Process.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.Widget_Right_Process)
        self.gridLayout_3.setSpacing(12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Process = QTextBrowser(self.Widget_Right_Process)
        self.TextBrowser_Params_Process.setObjectName(u"TextBrowser_Params_Process")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Process.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Process.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Process.setStyleSheet(u"QTextBrowser {\n"
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
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_3.addWidget(self.TextBrowser_Params_Process, 0, 0, 1, 3)

        self.Button_ResetSettings_Process = QPushButton(self.Widget_Right_Process)
        self.Button_ResetSettings_Process.setObjectName(u"Button_ResetSettings_Process")
        self.Button_ResetSettings_Process.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_3.addWidget(self.Button_ResetSettings_Process, 1, 0, 1, 1)

        self.Button_ImportSettings_Process = QPushButton(self.Widget_Right_Process)
        self.Button_ImportSettings_Process.setObjectName(u"Button_ImportSettings_Process")
        self.Button_ImportSettings_Process.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_3.addWidget(self.Button_ImportSettings_Process, 1, 1, 1, 1)

        self.Button_ExportSettings_Process = QPushButton(self.Widget_Right_Process)
        self.Button_ExportSettings_Process.setObjectName(u"Button_ExportSettings_Process")
        self.Button_ExportSettings_Process.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_3.addWidget(self.Button_ExportSettings_Process, 1, 2, 1, 1)

        self.Button_CheckOutput_Process = QPushButton(self.Widget_Right_Process)
        self.Button_CheckOutput_Process.setObjectName(u"Button_CheckOutput_Process")
        self.Button_CheckOutput_Process.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_3.addWidget(self.Button_CheckOutput_Process, 2, 0, 1, 3)


        self.gridLayout_6.addWidget(self.Widget_Right_Process, 0, 2, 1, 1)

        self.ProgressBar_Process = QProgressBar(self.Subpage_Process)
        self.ProgressBar_Process.setObjectName(u"ProgressBar_Process")
        self.ProgressBar_Process.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Process.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	background-color: transparent;\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgba(123, 123, 123, 123));\n"
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
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
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
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
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
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 6px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_53 = QHBoxLayout(self.Frame_ASR_Top)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_VoiceIdentifier_Title = QToolButton(self.Frame_ASR_Top)
        self.ToolButton_VoiceIdentifier_Title.setObjectName(u"ToolButton_VoiceIdentifier_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_VoiceIdentifier_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_VoiceIdentifier_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_VoiceIdentifier_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_53.addWidget(self.ToolButton_VoiceIdentifier_Title)

        self.Frame_VoiceIdentifier_Title = QFrame(self.Frame_ASR_Top)
        self.Frame_VoiceIdentifier_Title.setObjectName(u"Frame_VoiceIdentifier_Title")
        self.Frame_VoiceIdentifier_Title.setStyleSheet(u"QFrame {\n"
"	/*font-size: 24px;\n"
"	text-align: center;\n"
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
        self.horizontalLayout_46 = QHBoxLayout(self.Frame_VoiceIdentifier_Title)
        self.horizontalLayout_46.setSpacing(12)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSpacer_VoiceIdentifier_Title = QSpacerItem(549, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.HorizontalSpacer_VoiceIdentifier_Title)


        self.horizontalLayout_53.addWidget(self.Frame_VoiceIdentifier_Title)


        self.verticalLayout_44.addWidget(self.Frame_ASR_Top)

        self.StackedWidget_Pages_ASR = QStackedWidget(self.Page_ASR)
        self.StackedWidget_Pages_ASR.setObjectName(u"StackedWidget_Pages_ASR")
        self.StackedWidget_Pages_ASR.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
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
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal "
                        "{\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"}")

        self.verticalLayout_4.addWidget(self.TreeWidget_Catalogue_ASR_VPR)


        self.gridLayout_21.addWidget(self.Widget_Left_ASR_VPR, 0, 0, 1, 1)

        self.ScrollArea_Middle_ASR_VPR = ScrollAreaBase(self.Subpage_ASR_VPR)
        self.ScrollArea_Middle_ASR_VPR.setObjectName(u"ScrollArea_Middle_ASR_VPR")
        self.ScrollArea_Middle_ASR_VPR.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_ASR_VPR.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_ASR_VPR.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_ASR_VPR = QWidget()
        self.ScrollArea_Middle_WidgetContents_ASR_VPR.setObjectName(u"ScrollArea_Middle_WidgetContents_ASR_VPR")
        self.ScrollArea_Middle_WidgetContents_ASR_VPR.setGeometry(QRect(0, 0, 581, 1004))
        self.verticalLayout_7 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_ASR_VPR)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_ASR_VPR_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_ASR_VPR)
        self.GroupBox_ASR_VPR_InputParams.setObjectName(u"GroupBox_ASR_VPR_InputParams")
        self.GroupBox_ASR_VPR_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_32.addWidget(self.Label_ASR_VPR_AudioDirInput, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_AudioDirInput = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.HorizontalSpacer_ASR_VPR_AudioDirInput, 0, 1, 1, 1)

        self.Button_ASR_VPR_AudioDirInput_MoreActions = MenuButton(self.Frame_ASR_VPR_AudioDirInput)
        self.Button_ASR_VPR_AudioDirInput_MoreActions.setObjectName(u"Button_ASR_VPR_AudioDirInput_MoreActions")
        self.Button_ASR_VPR_AudioDirInput_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_AudioDirInput_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_AudioDirInput_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_32.addWidget(self.Button_ASR_VPR_AudioDirInput_MoreActions, 0, 2, 1, 1)

        self.LineEdit_ASR_VPR_AudioDirInput = LineEditBase(self.Frame_ASR_VPR_AudioDirInput)
        self.LineEdit_ASR_VPR_AudioDirInput.setObjectName(u"LineEdit_ASR_VPR_AudioDirInput")
        self.LineEdit_ASR_VPR_AudioDirInput.setMinimumSize(QSize(0, 27))

        self.gridLayout_32.addWidget(self.LineEdit_ASR_VPR_AudioDirInput, 1, 0, 1, 3)


        self.verticalLayout_137.addWidget(self.Frame_ASR_VPR_AudioDirInput)

        self.Frame_ASR_VPR_StdAudioSpeaker = QFrame(self.Frame_ASR_VPR_InputParams_BasicSettings)
        self.Frame_ASR_VPR_StdAudioSpeaker.setObjectName(u"Frame_ASR_VPR_StdAudioSpeaker")
        self.Frame_ASR_VPR_StdAudioSpeaker.setMinimumSize(QSize(0, 222))
        self.Frame_ASR_VPR_StdAudioSpeaker.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_33.addWidget(self.Label_ASR_VPR_DecisionThreshold, 0, 0, 1, 1)

        self.DoubleSpinBox_ASR_VPR_DecisionThreshold = DoubleSpinBoxBase(self.Frame_ASR_VPR_DecisionThreshold)
        self.DoubleSpinBox_ASR_VPR_DecisionThreshold.setObjectName(u"DoubleSpinBox_ASR_VPR_DecisionThreshold")
        self.DoubleSpinBox_ASR_VPR_DecisionThreshold.setEnabled(True)
        self.DoubleSpinBox_ASR_VPR_DecisionThreshold.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_ASR_VPR_DecisionThreshold.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_ASR_VPR_DecisionThreshold.setMaximum(999999.000000000000000)

        self.gridLayout_33.addWidget(self.DoubleSpinBox_ASR_VPR_DecisionThreshold, 1, 0, 1, 3)

        self.Button_ASR_VPR_DecisionThreshold_MoreActions = MenuButton(self.Frame_ASR_VPR_DecisionThreshold)
        self.Button_ASR_VPR_DecisionThreshold_MoreActions.setObjectName(u"Button_ASR_VPR_DecisionThreshold_MoreActions")
        self.Button_ASR_VPR_DecisionThreshold_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_DecisionThreshold_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_DecisionThreshold_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_33.addWidget(self.Button_ASR_VPR_DecisionThreshold_MoreActions, 0, 2, 1, 1)

        self.HorizontalSpacer_ASR_VPR_DecisionThreshold = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_33.addItem(self.HorizontalSpacer_ASR_VPR_DecisionThreshold, 0, 1, 1, 1)


        self.verticalLayout_45.addWidget(self.Frame_ASR_VPR_DecisionThreshold)

        self.Frame_ASR_VPR_ModelPath = QFrame(self.Frame_ASR_VPR_VPRParams_BasicSettings)
        self.Frame_ASR_VPR_ModelPath.setObjectName(u"Frame_ASR_VPR_ModelPath")
        self.Frame_ASR_VPR_ModelPath.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_ModelPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_34.addWidget(self.Label_ASR_VPR_ModelPath, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_ModelPath = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_34.addItem(self.HorizontalSpacer_ASR_VPR_ModelPath, 0, 1, 1, 1)

        self.Button_ASR_VPR_ModelPath_MoreActions = MenuButton(self.Frame_ASR_VPR_ModelPath)
        self.Button_ASR_VPR_ModelPath_MoreActions.setObjectName(u"Button_ASR_VPR_ModelPath_MoreActions")
        self.Button_ASR_VPR_ModelPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_ModelPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_ModelPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_34.addWidget(self.Button_ASR_VPR_ModelPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_ASR_VPR_ModelPath = LineEditBase(self.Frame_ASR_VPR_ModelPath)
        self.LineEdit_ASR_VPR_ModelPath.setObjectName(u"LineEdit_ASR_VPR_ModelPath")
        self.LineEdit_ASR_VPR_ModelPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_34.addWidget(self.LineEdit_ASR_VPR_ModelPath, 1, 0, 1, 3)


        self.verticalLayout_45.addWidget(self.Frame_ASR_VPR_ModelPath)


        self.verticalLayout_47.addWidget(self.Frame_ASR_VPR_VPRParams_BasicSettings)

        self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings = ToolBoxBase(self.GroupBox_ASR_VPR_VPRParams)
        self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings.setObjectName(u"ToolBox_ASR_VPR_VPRParams_AdvanceSettings")
        self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_ASR_VPR_VPRParams_AdvanceSettings_Page1Content")
        self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 538, 315))
        self.verticalLayout_21 = QVBoxLayout(self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings_Page1Content)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_VPR_ModelType = QFrame(self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings_Page1Content)
        self.Frame_ASR_VPR_ModelType.setObjectName(u"Frame_ASR_VPR_ModelType")
        self.Frame_ASR_VPR_ModelType.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_ModelType.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_35.addWidget(self.Label_ASR_VPR_ModelType, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_ModelType = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_35.addItem(self.HorizontalSpacer_ASR_VPR_ModelType, 0, 1, 1, 1)

        self.Button_ASR_VPR_ModelType_MoreActions = MenuButton(self.Frame_ASR_VPR_ModelType)
        self.Button_ASR_VPR_ModelType_MoreActions.setObjectName(u"Button_ASR_VPR_ModelType_MoreActions")
        self.Button_ASR_VPR_ModelType_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_ModelType_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_ModelType_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_35.addWidget(self.Button_ASR_VPR_ModelType_MoreActions, 0, 2, 1, 1)

        self.ComboBox_ASR_VPR_ModelType = ComboBoxBase(self.Frame_ASR_VPR_ModelType)
        self.ComboBox_ASR_VPR_ModelType.setObjectName(u"ComboBox_ASR_VPR_ModelType")
        self.ComboBox_ASR_VPR_ModelType.setMinimumSize(QSize(0, 27))

        self.gridLayout_35.addWidget(self.ComboBox_ASR_VPR_ModelType, 1, 0, 1, 3)


        self.verticalLayout_21.addWidget(self.Frame_ASR_VPR_ModelType)

        self.Frame_ASR_VPR_FeatureMethod = QFrame(self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings_Page1Content)
        self.Frame_ASR_VPR_FeatureMethod.setObjectName(u"Frame_ASR_VPR_FeatureMethod")
        self.Frame_ASR_VPR_FeatureMethod.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_FeatureMethod.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_36.addWidget(self.Label_ASR_VPR_FeatureMethod, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_FeatureMethod = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_36.addItem(self.HorizontalSpacer_ASR_VPR_FeatureMethod, 0, 1, 1, 1)

        self.Button_ASR_VPR_FeatureMethod_MoreActions = MenuButton(self.Frame_ASR_VPR_FeatureMethod)
        self.Button_ASR_VPR_FeatureMethod_MoreActions.setObjectName(u"Button_ASR_VPR_FeatureMethod_MoreActions")
        self.Button_ASR_VPR_FeatureMethod_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_FeatureMethod_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_FeatureMethod_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_36.addWidget(self.Button_ASR_VPR_FeatureMethod_MoreActions, 0, 2, 1, 1)

        self.ComboBox_ASR_VPR_FeatureMethod = ComboBoxBase(self.Frame_ASR_VPR_FeatureMethod)
        self.ComboBox_ASR_VPR_FeatureMethod.setObjectName(u"ComboBox_ASR_VPR_FeatureMethod")
        self.ComboBox_ASR_VPR_FeatureMethod.setMinimumSize(QSize(0, 27))

        self.gridLayout_36.addWidget(self.ComboBox_ASR_VPR_FeatureMethod, 1, 0, 1, 3)


        self.verticalLayout_21.addWidget(self.Frame_ASR_VPR_FeatureMethod)

        self.Frame_ASR_VPR_DurationOfAudio = QFrame(self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings_Page1Content)
        self.Frame_ASR_VPR_DurationOfAudio.setObjectName(u"Frame_ASR_VPR_DurationOfAudio")
        self.Frame_ASR_VPR_DurationOfAudio.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_DurationOfAudio.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_37.addWidget(self.Label_ASR_VPR_DurationOfAudio, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_DurationOfAudio = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_37.addItem(self.HorizontalSpacer_ASR_VPR_DurationOfAudio, 0, 1, 1, 1)

        self.Button_ASR_VPR_DurationOfAudio_MoreActions = MenuButton(self.Frame_ASR_VPR_DurationOfAudio)
        self.Button_ASR_VPR_DurationOfAudio_MoreActions.setObjectName(u"Button_ASR_VPR_DurationOfAudio_MoreActions")
        self.Button_ASR_VPR_DurationOfAudio_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_DurationOfAudio_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_DurationOfAudio_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_37.addWidget(self.Button_ASR_VPR_DurationOfAudio_MoreActions, 0, 2, 1, 1)

        self.DoubleSpinBox_ASR_VPR_DurationOfAudio = DoubleSpinBoxBase(self.Frame_ASR_VPR_DurationOfAudio)
        self.DoubleSpinBox_ASR_VPR_DurationOfAudio.setObjectName(u"DoubleSpinBox_ASR_VPR_DurationOfAudio")
        self.DoubleSpinBox_ASR_VPR_DurationOfAudio.setEnabled(True)
        self.DoubleSpinBox_ASR_VPR_DurationOfAudio.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_ASR_VPR_DurationOfAudio.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_ASR_VPR_DurationOfAudio.setMaximum(999999.000000000000000)

        self.gridLayout_37.addWidget(self.DoubleSpinBox_ASR_VPR_DurationOfAudio, 1, 0, 1, 3)


        self.verticalLayout_21.addWidget(self.Frame_ASR_VPR_DurationOfAudio)

        self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings.addItem(self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_47.addWidget(self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings)


        self.verticalLayout_7.addWidget(self.GroupBox_ASR_VPR_VPRParams)

        self.GroupBox_ASR_VPR_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_ASR_VPR)
        self.GroupBox_ASR_VPR_OutputParams.setObjectName(u"GroupBox_ASR_VPR_OutputParams")
        self.GroupBox_ASR_VPR_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.Frame_ASR_VPR_OutputDirName = QFrame(self.Frame_ASR_VPR_OutputParams_BasicSettings)
        self.Frame_ASR_VPR_OutputDirName.setObjectName(u"Frame_ASR_VPR_OutputDirName")
        self.Frame_ASR_VPR_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_38 = QGridLayout(self.Frame_ASR_VPR_OutputDirName)
        self.gridLayout_38.setSpacing(12)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_OutputDirName = QLabel(self.Frame_ASR_VPR_OutputDirName)
        self.Label_ASR_VPR_OutputDirName.setObjectName(u"Label_ASR_VPR_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_ASR_VPR_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_ASR_VPR_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_38.addWidget(self.Label_ASR_VPR_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_ASR_VPR_OutputDirName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_38.addItem(self.HorizontalSpacer_ASR_VPR_OutputDirName, 0, 1, 1, 1)

        self.Button_ASR_VPR_OutputDirName_MoreActions = MenuButton(self.Frame_ASR_VPR_OutputDirName)
        self.Button_ASR_VPR_OutputDirName_MoreActions.setObjectName(u"Button_ASR_VPR_OutputDirName_MoreActions")
        self.Button_ASR_VPR_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_38.addWidget(self.Button_ASR_VPR_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_ASR_VPR_OutputDirName = LineEditBase(self.Frame_ASR_VPR_OutputDirName)
        self.LineEdit_ASR_VPR_OutputDirName.setObjectName(u"LineEdit_ASR_VPR_OutputDirName")
        self.LineEdit_ASR_VPR_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_38.addWidget(self.LineEdit_ASR_VPR_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_139.addWidget(self.Frame_ASR_VPR_OutputDirName)


        self.verticalLayout_48.addWidget(self.Frame_ASR_VPR_OutputParams_BasicSettings)

        self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings = ToolBoxBase(self.GroupBox_ASR_VPR_OutputParams)
        self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings.setObjectName(u"ToolBox_ASR_VPR_OutputParams_AdvanceSettings")
        self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings.setFrameShape(QFrame.StyledPanel)
        self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings.setFrameShadow(QFrame.Raised)
        self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_ASR_VPR_OutputParams_AdvanceSettings_Page1Content")
        self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 536, 105))
        self.verticalLayout_110 = QVBoxLayout(self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings_Page1Content)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_VPR_AudioSpeakersDataName = QFrame(self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_ASR_VPR_AudioSpeakersDataName.setObjectName(u"Frame_ASR_VPR_AudioSpeakersDataName")
        self.Frame_ASR_VPR_AudioSpeakersDataName.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_AudioSpeakersDataName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_112 = QGridLayout(self.Frame_ASR_VPR_AudioSpeakersDataName)
        self.gridLayout_112.setSpacing(12)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.gridLayout_112.setContentsMargins(21, 12, 21, 12)
        self.Button_ASR_VPR_AudioSpeakersDataName_MoreActions = MenuButton(self.Frame_ASR_VPR_AudioSpeakersDataName)
        self.Button_ASR_VPR_AudioSpeakersDataName_MoreActions.setObjectName(u"Button_ASR_VPR_AudioSpeakersDataName_MoreActions")
        self.Button_ASR_VPR_AudioSpeakersDataName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_AudioSpeakersDataName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_ASR_VPR_AudioSpeakersDataName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_112.addWidget(self.Button_ASR_VPR_AudioSpeakersDataName_MoreActions, 0, 2, 1, 1)

        self.Label_ASR_VPR_AudioSpeakersDataName = QLabel(self.Frame_ASR_VPR_AudioSpeakersDataName)
        self.Label_ASR_VPR_AudioSpeakersDataName.setObjectName(u"Label_ASR_VPR_AudioSpeakersDataName")
        sizePolicy5.setHeightForWidth(self.Label_ASR_VPR_AudioSpeakersDataName.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_AudioSpeakersDataName.setSizePolicy(sizePolicy5)
        self.Label_ASR_VPR_AudioSpeakersDataName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_112.addWidget(self.Label_ASR_VPR_AudioSpeakersDataName, 0, 0, 1, 1)

        self.LineEdit_ASR_VPR_AudioSpeakersDataName = LineEditBase(self.Frame_ASR_VPR_AudioSpeakersDataName)
        self.LineEdit_ASR_VPR_AudioSpeakersDataName.setObjectName(u"LineEdit_ASR_VPR_AudioSpeakersDataName")
        self.LineEdit_ASR_VPR_AudioSpeakersDataName.setMinimumSize(QSize(0, 27))

        self.gridLayout_112.addWidget(self.LineEdit_ASR_VPR_AudioSpeakersDataName, 1, 0, 1, 3)

        self.HorizontalSpacer_ASR_VPR_AudioSpeakersDataName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_112.addItem(self.HorizontalSpacer_ASR_VPR_AudioSpeakersDataName, 0, 1, 1, 1)


        self.verticalLayout_110.addWidget(self.Frame_ASR_VPR_AudioSpeakersDataName)

        self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings.addItem(self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_48.addWidget(self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings)


        self.verticalLayout_7.addWidget(self.GroupBox_ASR_VPR_OutputParams)

        self.ScrollArea_Middle_ASR_VPR.setWidget(self.ScrollArea_Middle_WidgetContents_ASR_VPR)

        self.gridLayout_21.addWidget(self.ScrollArea_Middle_ASR_VPR, 0, 1, 1, 1)

        self.Widget_Right_ASR_VPR = QWidget(self.Subpage_ASR_VPR)
        self.Widget_Right_ASR_VPR.setObjectName(u"Widget_Right_ASR_VPR")
        self.Widget_Right_ASR_VPR.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.Widget_Right_ASR_VPR)
        self.gridLayout_2.setSpacing(12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_ASR_VPR = QTextBrowser(self.Widget_Right_ASR_VPR)
        self.TextBrowser_Params_ASR_VPR.setObjectName(u"TextBrowser_Params_ASR_VPR")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_ASR_VPR.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_ASR_VPR.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_ASR_VPR.setStyleSheet(u"QTextBrowser {\n"
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
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_2.addWidget(self.TextBrowser_Params_ASR_VPR, 0, 0, 1, 3)

        self.Button_ResetSettings_ASR_VPR = QPushButton(self.Widget_Right_ASR_VPR)
        self.Button_ResetSettings_ASR_VPR.setObjectName(u"Button_ResetSettings_ASR_VPR")
        self.Button_ResetSettings_ASR_VPR.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_2.addWidget(self.Button_ResetSettings_ASR_VPR, 1, 0, 1, 1)

        self.Button_ImportSettings_ASR_VPR = QPushButton(self.Widget_Right_ASR_VPR)
        self.Button_ImportSettings_ASR_VPR.setObjectName(u"Button_ImportSettings_ASR_VPR")
        self.Button_ImportSettings_ASR_VPR.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_2.addWidget(self.Button_ImportSettings_ASR_VPR, 1, 1, 1, 1)

        self.Button_ExportSettings_ASR_VPR = QPushButton(self.Widget_Right_ASR_VPR)
        self.Button_ExportSettings_ASR_VPR.setObjectName(u"Button_ExportSettings_ASR_VPR")
        self.Button_ExportSettings_ASR_VPR.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_2.addWidget(self.Button_ExportSettings_ASR_VPR, 1, 2, 1, 1)

        self.Button_EditResult_ASR_VPR = QPushButton(self.Widget_Right_ASR_VPR)
        self.Button_EditResult_ASR_VPR.setObjectName(u"Button_EditResult_ASR_VPR")
        self.Button_EditResult_ASR_VPR.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_2.addWidget(self.Button_EditResult_ASR_VPR, 2, 0, 1, 3)

        self.Button_CheckOutput_ASR_VPR = QPushButton(self.Widget_Right_ASR_VPR)
        self.Button_CheckOutput_ASR_VPR.setObjectName(u"Button_CheckOutput_ASR_VPR")
        self.Button_CheckOutput_ASR_VPR.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_2.addWidget(self.Button_CheckOutput_ASR_VPR, 3, 0, 1, 3)


        self.gridLayout_21.addWidget(self.Widget_Right_ASR_VPR, 0, 2, 1, 1)

        self.ProgressBar_ASR_VPR = QProgressBar(self.Subpage_ASR_VPR)
        self.ProgressBar_ASR_VPR.setObjectName(u"ProgressBar_ASR_VPR")
        self.ProgressBar_ASR_VPR.setMinimumSize(QSize(0, 30))
        self.ProgressBar_ASR_VPR.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	background-color: transparent;\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgba(123, 123, 123, 123));\n"
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
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
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
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
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
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_55 = QHBoxLayout(self.Frame_STT_Top)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_VoiceTranscriber_Title = QToolButton(self.Frame_STT_Top)
        self.ToolButton_VoiceTranscriber_Title.setObjectName(u"ToolButton_VoiceTranscriber_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_VoiceTranscriber_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_VoiceTranscriber_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_VoiceTranscriber_Title.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_55.addWidget(self.ToolButton_VoiceTranscriber_Title)

        self.Frame_VoiceTranscriber_Title = QFrame(self.Frame_STT_Top)
        self.Frame_VoiceTranscriber_Title.setObjectName(u"Frame_VoiceTranscriber_Title")
        self.Frame_VoiceTranscriber_Title.setStyleSheet(u"QFrame {\n"
"	/*font-size: 24px;\n"
"	text-align: center;\n"
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
        self.horizontalLayout_54 = QHBoxLayout(self.Frame_VoiceTranscriber_Title)
        self.horizontalLayout_54.setSpacing(12)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSpacer_VoiceTranscriber_Title = QSpacerItem(549, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_54.addItem(self.HorizontalSpacer_VoiceTranscriber_Title)


        self.horizontalLayout_55.addWidget(self.Frame_VoiceTranscriber_Title)


        self.verticalLayout_41.addWidget(self.Frame_STT_Top)

        self.StackedWidget_Pages_STT = QStackedWidget(self.Page_STT)
        self.StackedWidget_Pages_STT.setObjectName(u"StackedWidget_Pages_STT")
        self.StackedWidget_Pages_STT.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
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
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal "
                        "{\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"}")

        self.verticalLayout_8.addWidget(self.TreeWidget_Catalogue_STT_Whisper)


        self.gridLayout_19.addWidget(self.Widget_Left_STT_Whisper, 0, 0, 1, 1)

        self.ScrollArea_Middle_STT_Whisper = ScrollAreaBase(self.Subpage_STT_Whisper)
        self.ScrollArea_Middle_STT_Whisper.setObjectName(u"ScrollArea_Middle_STT_Whisper")
        self.ScrollArea_Middle_STT_Whisper.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_STT_Whisper.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_STT_Whisper.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_STT_Whisper = QWidget()
        self.ScrollArea_Middle_WidgetContents_STT_Whisper.setObjectName(u"ScrollArea_Middle_WidgetContents_STT_Whisper")
        self.ScrollArea_Middle_WidgetContents_STT_Whisper.setGeometry(QRect(0, 0, 581, 693))
        self.verticalLayout_16 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_STT_Whisper)
        self.verticalLayout_16.setSpacing(12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_STT_Whisper_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_STT_Whisper)
        self.GroupBox_STT_Whisper_InputParams.setObjectName(u"GroupBox_STT_Whisper_InputParams")
        self.GroupBox_STT_Whisper_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_39.addWidget(self.Label_STT_Whisper_AudioDir, 0, 0, 1, 1)

        self.HorizontalSpacer_STT_Whisper_AudioDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_39.addItem(self.HorizontalSpacer_STT_Whisper_AudioDir, 0, 1, 1, 1)

        self.Button_STT_Whisper_AudioDir_MoreActions = MenuButton(self.Frame_STT_Whisper_AudioDir)
        self.Button_STT_Whisper_AudioDir_MoreActions.setObjectName(u"Button_STT_Whisper_AudioDir_MoreActions")
        self.Button_STT_Whisper_AudioDir_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_AudioDir_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_AudioDir_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_39.addWidget(self.Button_STT_Whisper_AudioDir_MoreActions, 0, 2, 1, 1)

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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_40.addWidget(self.Label_STT_Whisper_AddLanguageInfo, 0, 0, 1, 1)

        self.HorizontalSpacer_STT_Whisper_AddLanguageInfo = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_40.addItem(self.HorizontalSpacer_STT_Whisper_AddLanguageInfo, 0, 1, 1, 1)

        self.Button_STT_Whisper_AddLanguageInfo_MoreActions = MenuButton(self.Frame_STT_Whisper_AddLanguageInfo)
        self.Button_STT_Whisper_AddLanguageInfo_MoreActions.setObjectName(u"Button_STT_Whisper_AddLanguageInfo_MoreActions")
        self.Button_STT_Whisper_AddLanguageInfo_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_AddLanguageInfo_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_AddLanguageInfo_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_40.addWidget(self.Button_STT_Whisper_AddLanguageInfo_MoreActions, 0, 2, 1, 1)

        self.CheckBox_STT_Whisper_AddLanguageInfo = QCheckBox(self.Frame_STT_Whisper_AddLanguageInfo)
        self.CheckBox_STT_Whisper_AddLanguageInfo.setObjectName(u"CheckBox_STT_Whisper_AddLanguageInfo")
        self.CheckBox_STT_Whisper_AddLanguageInfo.setMinimumSize(QSize(0, 27))
        self.CheckBox_STT_Whisper_AddLanguageInfo.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_40.addWidget(self.CheckBox_STT_Whisper_AddLanguageInfo, 1, 0, 1, 3)


        self.verticalLayout_37.addWidget(self.Frame_STT_Whisper_AddLanguageInfo)

        self.Frame_STT_Whisper_ModelPath = QFrame(self.Frame_STT_Whisper_WhisperParams_BasicSettings)
        self.Frame_STT_Whisper_ModelPath.setObjectName(u"Frame_STT_Whisper_ModelPath")
        self.Frame_STT_Whisper_ModelPath.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_ModelPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_41.addWidget(self.Label_STT_Whisper_ModelPath, 0, 0, 1, 1)

        self.HorizontalSpacer_STT_Whisper_ModelPath = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_41.addItem(self.HorizontalSpacer_STT_Whisper_ModelPath, 0, 1, 1, 1)

        self.Button_STT_Whisper_ModelPath_MoreActions = MenuButton(self.Frame_STT_Whisper_ModelPath)
        self.Button_STT_Whisper_ModelPath_MoreActions.setObjectName(u"Button_STT_Whisper_ModelPath_MoreActions")
        self.Button_STT_Whisper_ModelPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_ModelPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_ModelPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_41.addWidget(self.Button_STT_Whisper_ModelPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_STT_Whisper_ModelPath = LineEditBase(self.Frame_STT_Whisper_ModelPath)
        self.LineEdit_STT_Whisper_ModelPath.setObjectName(u"LineEdit_STT_Whisper_ModelPath")
        self.LineEdit_STT_Whisper_ModelPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_41.addWidget(self.LineEdit_STT_Whisper_ModelPath, 1, 0, 1, 3)


        self.verticalLayout_37.addWidget(self.Frame_STT_Whisper_ModelPath)


        self.verticalLayout_49.addWidget(self.Frame_STT_Whisper_WhisperParams_BasicSettings)

        self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings = ToolBoxBase(self.GroupBox_STT_Whisper_WhisperParams)
        self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings.setObjectName(u"ToolBox_STT_Whisper_WhisperParams_AdvanceSettings")
        self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_STT_Whisper_WhisperParams_AdvanceSettings_Page1Content")
        self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 538, 315))
        self.verticalLayout_15 = QVBoxLayout(self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings_Page1Content)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Frame_STT_Whisper_fp16 = QFrame(self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings_Page1Content)
        self.Frame_STT_Whisper_fp16.setObjectName(u"Frame_STT_Whisper_fp16")
        self.Frame_STT_Whisper_fp16.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_fp16.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_44.addWidget(self.CheckBox_STT_Whisper_fp16, 1, 0, 1, 3)

        self.Button_STT_Whisper_fp16_MoreActions = MenuButton(self.Frame_STT_Whisper_fp16)
        self.Button_STT_Whisper_fp16_MoreActions.setObjectName(u"Button_STT_Whisper_fp16_MoreActions")
        self.Button_STT_Whisper_fp16_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_fp16_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_fp16_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_44.addWidget(self.Button_STT_Whisper_fp16_MoreActions, 0, 2, 1, 1)


        self.verticalLayout_15.addWidget(self.Frame_STT_Whisper_fp16)

        self.Frame_STT_Whisper_ConditionOnPreviousText = QFrame(self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings_Page1Content)
        self.Frame_STT_Whisper_ConditionOnPreviousText.setObjectName(u"Frame_STT_Whisper_ConditionOnPreviousText")
        self.Frame_STT_Whisper_ConditionOnPreviousText.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_ConditionOnPreviousText.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_43.addWidget(self.CheckBox_STT_Whisper_ConditionOnPreviousText, 1, 0, 1, 3)

        self.HorizontalSpacer_STT_Whisper_ConditionOnPreviousText = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_43.addItem(self.HorizontalSpacer_STT_Whisper_ConditionOnPreviousText, 0, 1, 1, 1)

        self.Button_STT_Whisper_ConditionOnPreviousText_MoreActions = MenuButton(self.Frame_STT_Whisper_ConditionOnPreviousText)
        self.Button_STT_Whisper_ConditionOnPreviousText_MoreActions.setObjectName(u"Button_STT_Whisper_ConditionOnPreviousText_MoreActions")
        self.Button_STT_Whisper_ConditionOnPreviousText_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_ConditionOnPreviousText_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_ConditionOnPreviousText_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_43.addWidget(self.Button_STT_Whisper_ConditionOnPreviousText_MoreActions, 0, 2, 1, 1)

        self.Label_STT_Whisper_ConditionOnPreviousText = QLabel(self.Frame_STT_Whisper_ConditionOnPreviousText)
        self.Label_STT_Whisper_ConditionOnPreviousText.setObjectName(u"Label_STT_Whisper_ConditionOnPreviousText")
        sizePolicy5.setHeightForWidth(self.Label_STT_Whisper_ConditionOnPreviousText.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_ConditionOnPreviousText.setSizePolicy(sizePolicy5)
        self.Label_STT_Whisper_ConditionOnPreviousText.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_43.addWidget(self.Label_STT_Whisper_ConditionOnPreviousText, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.Frame_STT_Whisper_ConditionOnPreviousText)

        self.Frame_STT_Whisper_Verbose = QFrame(self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings_Page1Content)
        self.Frame_STT_Whisper_Verbose.setObjectName(u"Frame_STT_Whisper_Verbose")
        self.Frame_STT_Whisper_Verbose.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_Verbose.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_42.addWidget(self.CheckBox_STT_Whisper_Verbose, 1, 0, 1, 3)

        self.Button_STT_Whisper_Verbose_MoreActions = MenuButton(self.Frame_STT_Whisper_Verbose)
        self.Button_STT_Whisper_Verbose_MoreActions.setObjectName(u"Button_STT_Whisper_Verbose_MoreActions")
        self.Button_STT_Whisper_Verbose_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_Verbose_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_Verbose_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_42.addWidget(self.Button_STT_Whisper_Verbose_MoreActions, 0, 2, 1, 1)


        self.verticalLayout_15.addWidget(self.Frame_STT_Whisper_Verbose)

        self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings.addItem(self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_49.addWidget(self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings)


        self.verticalLayout_16.addWidget(self.GroupBox_STT_Whisper_WhisperParams)

        self.GroupBox_STT_Whisper_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_STT_Whisper)
        self.GroupBox_STT_Whisper_OutputParams.setObjectName(u"GroupBox_STT_Whisper_OutputParams")
        self.GroupBox_STT_Whisper_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.Frame_STT_Whisper_OutputDirName = QFrame(self.Frame_STT_Whisper_OutputParams_BasicSettings)
        self.Frame_STT_Whisper_OutputDirName.setObjectName(u"Frame_STT_Whisper_OutputDirName")
        self.Frame_STT_Whisper_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_45 = QGridLayout(self.Frame_STT_Whisper_OutputDirName)
        self.gridLayout_45.setSpacing(12)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_OutputDirName = QLabel(self.Frame_STT_Whisper_OutputDirName)
        self.Label_STT_Whisper_OutputDirName.setObjectName(u"Label_STT_Whisper_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_STT_Whisper_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_STT_Whisper_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_45.addWidget(self.Label_STT_Whisper_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_STT_Whisper_OutputDirName = QSpacerItem(481, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_45.addItem(self.HorizontalSpacer_STT_Whisper_OutputDirName, 0, 1, 1, 1)

        self.Button_STT_Whisper_OutputDirName_MoreActions = MenuButton(self.Frame_STT_Whisper_OutputDirName)
        self.Button_STT_Whisper_OutputDirName_MoreActions.setObjectName(u"Button_STT_Whisper_OutputDirName_MoreActions")
        self.Button_STT_Whisper_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_STT_Whisper_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_45.addWidget(self.Button_STT_Whisper_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_STT_Whisper_OutputDirName = LineEditBase(self.Frame_STT_Whisper_OutputDirName)
        self.LineEdit_STT_Whisper_OutputDirName.setObjectName(u"LineEdit_STT_Whisper_OutputDirName")
        self.LineEdit_STT_Whisper_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_45.addWidget(self.LineEdit_STT_Whisper_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_135.addWidget(self.Frame_STT_Whisper_OutputDirName)


        self.verticalLayout_89.addWidget(self.Frame_STT_Whisper_OutputParams_BasicSettings)


        self.verticalLayout_16.addWidget(self.GroupBox_STT_Whisper_OutputParams)

        self.VerticalSpacer_STT_Whisper = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.VerticalSpacer_STT_Whisper)

        self.ScrollArea_Middle_STT_Whisper.setWidget(self.ScrollArea_Middle_WidgetContents_STT_Whisper)

        self.gridLayout_19.addWidget(self.ScrollArea_Middle_STT_Whisper, 0, 1, 1, 1)

        self.Widget_Right_STT_Whisper = QWidget(self.Subpage_STT_Whisper)
        self.Widget_Right_STT_Whisper.setObjectName(u"Widget_Right_STT_Whisper")
        self.Widget_Right_STT_Whisper.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.Widget_Right_STT_Whisper)
        self.gridLayout_4.setSpacing(12)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_STT_Whisper = QTextBrowser(self.Widget_Right_STT_Whisper)
        self.TextBrowser_Params_STT_Whisper.setObjectName(u"TextBrowser_Params_STT_Whisper")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_STT_Whisper.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_STT_Whisper.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_STT_Whisper.setStyleSheet(u"QTextBrowser {\n"
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
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_4.addWidget(self.TextBrowser_Params_STT_Whisper, 0, 0, 1, 3)

        self.Button_ResetSettings_STT_Whisper = QPushButton(self.Widget_Right_STT_Whisper)
        self.Button_ResetSettings_STT_Whisper.setObjectName(u"Button_ResetSettings_STT_Whisper")
        self.Button_ResetSettings_STT_Whisper.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_4.addWidget(self.Button_ResetSettings_STT_Whisper, 1, 0, 1, 1)

        self.Button_ImportSettings_STT_Whisper = QPushButton(self.Widget_Right_STT_Whisper)
        self.Button_ImportSettings_STT_Whisper.setObjectName(u"Button_ImportSettings_STT_Whisper")
        self.Button_ImportSettings_STT_Whisper.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_4.addWidget(self.Button_ImportSettings_STT_Whisper, 1, 1, 1, 1)

        self.Button_ExportSettings_STT_Whisper = QPushButton(self.Widget_Right_STT_Whisper)
        self.Button_ExportSettings_STT_Whisper.setObjectName(u"Button_ExportSettings_STT_Whisper")
        self.Button_ExportSettings_STT_Whisper.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_4.addWidget(self.Button_ExportSettings_STT_Whisper, 1, 2, 1, 1)

        self.Button_CheckOutput_STT_Whisper = QPushButton(self.Widget_Right_STT_Whisper)
        self.Button_CheckOutput_STT_Whisper.setObjectName(u"Button_CheckOutput_STT_Whisper")
        self.Button_CheckOutput_STT_Whisper.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_4.addWidget(self.Button_CheckOutput_STT_Whisper, 2, 0, 1, 3)


        self.gridLayout_19.addWidget(self.Widget_Right_STT_Whisper, 0, 2, 1, 1)

        self.ProgressBar_STT_Whisper = QProgressBar(self.Subpage_STT_Whisper)
        self.ProgressBar_STT_Whisper.setObjectName(u"ProgressBar_STT_Whisper")
        self.ProgressBar_STT_Whisper.setMinimumSize(QSize(0, 30))
        self.ProgressBar_STT_Whisper.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	background-color: transparent;\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgba(123, 123, 123, 123));\n"
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
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
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
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
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
"	/*background-color: rgba(90, 90, 90, 45);*/\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	/*background-color: rgba(120, 120, 120, 60);*/\n"
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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_17 = QHBoxLayout(self.Frame_Dataset_Top)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_DatasetCreator_Title_GPTSoVITS = QToolButton(self.Frame_Dataset_Top)
        self.ToolButton_DatasetCreator_Title_GPTSoVITS.setObjectName(u"ToolButton_DatasetCreator_Title_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.ToolButton_DatasetCreator_Title_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.ToolButton_DatasetCreator_Title_GPTSoVITS.setSizePolicy(sizePolicy1)
        self.ToolButton_DatasetCreator_Title_GPTSoVITS.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_17.addWidget(self.ToolButton_DatasetCreator_Title_GPTSoVITS)

        self.ToolButton_DatasetCreator_Title_VITS = QToolButton(self.Frame_Dataset_Top)
        self.ToolButton_DatasetCreator_Title_VITS.setObjectName(u"ToolButton_DatasetCreator_Title_VITS")
        sizePolicy1.setHeightForWidth(self.ToolButton_DatasetCreator_Title_VITS.sizePolicy().hasHeightForWidth())
        self.ToolButton_DatasetCreator_Title_VITS.setSizePolicy(sizePolicy1)
        self.ToolButton_DatasetCreator_Title_VITS.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_17.addWidget(self.ToolButton_DatasetCreator_Title_VITS)

        self.Frame_DatasetCreator_Title = QFrame(self.Frame_Dataset_Top)
        self.Frame_DatasetCreator_Title.setObjectName(u"Frame_DatasetCreator_Title")
        self.Frame_DatasetCreator_Title.setStyleSheet(u"QFrame {\n"
"	/*font-size: 24px;\n"
"	text-align: center;\n"
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
        self.horizontalLayout_57 = QHBoxLayout(self.Frame_DatasetCreator_Title)
        self.horizontalLayout_57.setSpacing(12)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSpacer_DatasetCreator_Title = QSpacerItem(549, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.HorizontalSpacer_DatasetCreator_Title)


        self.horizontalLayout_17.addWidget(self.Frame_DatasetCreator_Title)


        self.verticalLayout_39.addWidget(self.Frame_Dataset_Top)

        self.StackedWidget_Pages_Dataset = QStackedWidget(self.Page_Dataset)
        self.StackedWidget_Pages_Dataset.setObjectName(u"StackedWidget_Pages_Dataset")
        self.StackedWidget_Pages_Dataset.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.Subpage_DAT_GPTSoVITS = QWidget()
        self.Subpage_DAT_GPTSoVITS.setObjectName(u"Subpage_DAT_GPTSoVITS")
        self.gridLayout_108 = QGridLayout(self.Subpage_DAT_GPTSoVITS)
        self.gridLayout_108.setSpacing(12)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.gridLayout_108.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_DAT_GPTSoVITS = QWidget(self.Subpage_DAT_GPTSoVITS)
        self.Widget_Left_DAT_GPTSoVITS.setObjectName(u"Widget_Left_DAT_GPTSoVITS")
        self.Widget_Left_DAT_GPTSoVITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_DAT_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_62 = QVBoxLayout(self.Widget_Left_DAT_GPTSoVITS)
        self.verticalLayout_62.setSpacing(12)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_DAT_GPTSoVITS = QTreeWidget(self.Widget_Left_DAT_GPTSoVITS)
        __qtreewidgetitem3 = QTreeWidgetItem(self.TreeWidget_Catalogue_DAT_GPTSoVITS)
        QTreeWidgetItem(__qtreewidgetitem3)
        self.TreeWidget_Catalogue_DAT_GPTSoVITS.setObjectName(u"TreeWidget_Catalogue_DAT_GPTSoVITS")
        self.TreeWidget_Catalogue_DAT_GPTSoVITS.setStyleSheet(u"QTreeView {\n"
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
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal "
                        "{\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"}")

        self.verticalLayout_62.addWidget(self.TreeWidget_Catalogue_DAT_GPTSoVITS)


        self.gridLayout_108.addWidget(self.Widget_Left_DAT_GPTSoVITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_DAT_GPTSoVITS = ScrollAreaBase(self.Subpage_DAT_GPTSoVITS)
        self.ScrollArea_Middle_DAT_GPTSoVITS.setObjectName(u"ScrollArea_Middle_DAT_GPTSoVITS")
        self.ScrollArea_Middle_DAT_GPTSoVITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_DAT_GPTSoVITS.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_DAT_GPTSoVITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS.setObjectName(u"ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS")
        self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS.setGeometry(QRect(0, 0, 581, 695))
        self.verticalLayout_63 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS)
        self.verticalLayout_63.setSpacing(12)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_DAT_GPTSoVITS_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS)
        self.GroupBox_DAT_GPTSoVITS_InputParams.setObjectName(u"GroupBox_DAT_GPTSoVITS_InputParams")
        self.GroupBox_DAT_GPTSoVITS_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_123 = QVBoxLayout(self.GroupBox_DAT_GPTSoVITS_InputParams)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings = QFrame(self.GroupBox_DAT_GPTSoVITS_InputParams)
        self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings.setObjectName(u"Frame_DAT_GPTSoVITS_InputParams_BasicSettings")
        self.verticalLayout_64 = QVBoxLayout(self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath = QFrame(self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath.setObjectName(u"Frame_DAT_GPTSoVITS_AudioSpeakersDataPath")
        self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_82 = QGridLayout(self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath)
        self.gridLayout_82.setSpacing(12)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.gridLayout_82.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath = QLabel(self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath)
        self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath.setObjectName(u"Label_DAT_GPTSoVITS_AudioSpeakersDataPath")
        sizePolicy5.setHeightForWidth(self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath.setSizePolicy(sizePolicy5)
        self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_82.addWidget(self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_GPTSoVITS_InputParams = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_82.addItem(self.HorizontalSpacer_DAT_GPTSoVITS_InputParams, 0, 1, 1, 1)

        self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath)
        self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions")
        self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_82.addWidget(self.Button_DAT_GPTSoVITS_AudioSpeakersDataPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath = LineEditBase(self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath)
        self.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.setObjectName(u"LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath")
        self.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_82.addWidget(self.LineEdit_DAT_GPTSoVITS_AudioSpeakersDataPath, 1, 0, 1, 3)


        self.verticalLayout_64.addWidget(self.Frame_DAT_GPTSoVITS_AudioSpeakersDataPath)

        self.Frame_DAT_GPTSoVITS_SRTDir = QFrame(self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_DAT_GPTSoVITS_SRTDir.setObjectName(u"Frame_DAT_GPTSoVITS_SRTDir")
        self.Frame_DAT_GPTSoVITS_SRTDir.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_GPTSoVITS_SRTDir.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_83 = QGridLayout(self.Frame_DAT_GPTSoVITS_SRTDir)
        self.gridLayout_83.setSpacing(12)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.gridLayout_83.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_GPTSoVITS_SRTDir = QLabel(self.Frame_DAT_GPTSoVITS_SRTDir)
        self.Label_DAT_GPTSoVITS_SRTDir.setObjectName(u"Label_DAT_GPTSoVITS_SRTDir")
        sizePolicy5.setHeightForWidth(self.Label_DAT_GPTSoVITS_SRTDir.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_SRTDir.setSizePolicy(sizePolicy5)
        self.Label_DAT_GPTSoVITS_SRTDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_83.addWidget(self.Label_DAT_GPTSoVITS_SRTDir, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_GPTSoVITS_SRTDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_83.addItem(self.HorizontalSpacer_DAT_GPTSoVITS_SRTDir, 0, 1, 1, 1)

        self.Button_DAT_GPTSoVITS_SRTDir_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_SRTDir)
        self.Button_DAT_GPTSoVITS_SRTDir_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_SRTDir_MoreActions")
        self.Button_DAT_GPTSoVITS_SRTDir_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_SRTDir_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_SRTDir_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_83.addWidget(self.Button_DAT_GPTSoVITS_SRTDir_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_GPTSoVITS_SRTDir = LineEditBase(self.Frame_DAT_GPTSoVITS_SRTDir)
        self.LineEdit_DAT_GPTSoVITS_SRTDir.setObjectName(u"LineEdit_DAT_GPTSoVITS_SRTDir")
        self.LineEdit_DAT_GPTSoVITS_SRTDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_83.addWidget(self.LineEdit_DAT_GPTSoVITS_SRTDir, 1, 0, 1, 3)


        self.verticalLayout_64.addWidget(self.Frame_DAT_GPTSoVITS_SRTDir)


        self.verticalLayout_123.addWidget(self.Frame_DAT_GPTSoVITS_InputParams_BasicSettings)


        self.verticalLayout_63.addWidget(self.GroupBox_DAT_GPTSoVITS_InputParams)

        self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS)
        self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams.setObjectName(u"GroupBox_DAT_GPTSoVITS_GPTSoVITSParams")
        self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_124 = QVBoxLayout(self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings = QFrame(self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams)
        self.Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings.setObjectName(u"Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings")
        self.verticalLayout_65 = QVBoxLayout(self.Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_GPTSoVITS_DataFormat = QFrame(self.Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_DAT_GPTSoVITS_DataFormat.setObjectName(u"Frame_DAT_GPTSoVITS_DataFormat")
        self.Frame_DAT_GPTSoVITS_DataFormat.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_GPTSoVITS_DataFormat.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_84 = QGridLayout(self.Frame_DAT_GPTSoVITS_DataFormat)
        self.gridLayout_84.setSpacing(12)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.gridLayout_84.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_GPTSoVITS_DataFormat = QLabel(self.Frame_DAT_GPTSoVITS_DataFormat)
        self.Label_DAT_GPTSoVITS_DataFormat.setObjectName(u"Label_DAT_GPTSoVITS_DataFormat")
        sizePolicy5.setHeightForWidth(self.Label_DAT_GPTSoVITS_DataFormat.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_DataFormat.setSizePolicy(sizePolicy5)
        self.Label_DAT_GPTSoVITS_DataFormat.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_84.addWidget(self.Label_DAT_GPTSoVITS_DataFormat, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_GPTSoVITS_DataFormat = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_84.addItem(self.HorizontalSpacer_DAT_GPTSoVITS_DataFormat, 0, 1, 1, 1)

        self.Button_DAT_GPTSoVITS_DataFormat_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_DataFormat)
        self.Button_DAT_GPTSoVITS_DataFormat_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_DataFormat_MoreActions")
        self.Button_DAT_GPTSoVITS_DataFormat_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_DataFormat_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_DataFormat_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_84.addWidget(self.Button_DAT_GPTSoVITS_DataFormat_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_GPTSoVITS_DataFormat = LineEditBase(self.Frame_DAT_GPTSoVITS_DataFormat)
        self.LineEdit_DAT_GPTSoVITS_DataFormat.setObjectName(u"LineEdit_DAT_GPTSoVITS_DataFormat")
        self.LineEdit_DAT_GPTSoVITS_DataFormat.setMinimumSize(QSize(0, 27))

        self.gridLayout_84.addWidget(self.LineEdit_DAT_GPTSoVITS_DataFormat, 1, 0, 1, 3)


        self.verticalLayout_65.addWidget(self.Frame_DAT_GPTSoVITS_DataFormat)


        self.verticalLayout_124.addWidget(self.Frame_DAT_GPTSoVITS_GPTSoVITSParams_BasicSettings)


        self.verticalLayout_63.addWidget(self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams)

        self.GroupBox_DAT_GPTSoVITS_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS)
        self.GroupBox_DAT_GPTSoVITS_OutputParams.setObjectName(u"GroupBox_DAT_GPTSoVITS_OutputParams")
        self.GroupBox_DAT_GPTSoVITS_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_109 = QVBoxLayout(self.GroupBox_DAT_GPTSoVITS_OutputParams)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_GPTSoVITS_OutputParams_BasicSettings = QFrame(self.GroupBox_DAT_GPTSoVITS_OutputParams)
        self.Frame_DAT_GPTSoVITS_OutputParams_BasicSettings.setObjectName(u"Frame_DAT_GPTSoVITS_OutputParams_BasicSettings")
        self.verticalLayout_68 = QVBoxLayout(self.Frame_DAT_GPTSoVITS_OutputParams_BasicSettings)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_GPTSoVITS_OutputDirName = QFrame(self.Frame_DAT_GPTSoVITS_OutputParams_BasicSettings)
        self.Frame_DAT_GPTSoVITS_OutputDirName.setObjectName(u"Frame_DAT_GPTSoVITS_OutputDirName")
        self.Frame_DAT_GPTSoVITS_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_GPTSoVITS_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_104 = QGridLayout(self.Frame_DAT_GPTSoVITS_OutputDirName)
        self.gridLayout_104.setSpacing(12)
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.gridLayout_104.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_GPTSoVITS_OutputDirName = QLabel(self.Frame_DAT_GPTSoVITS_OutputDirName)
        self.Label_DAT_GPTSoVITS_OutputDirName.setObjectName(u"Label_DAT_GPTSoVITS_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_DAT_GPTSoVITS_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_DAT_GPTSoVITS_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_104.addWidget(self.Label_DAT_GPTSoVITS_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_GPTSoVITS_OutputDirName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_104.addItem(self.HorizontalSpacer_DAT_GPTSoVITS_OutputDirName, 0, 1, 1, 1)

        self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_OutputDirName)
        self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_OutputDirName_MoreActions")
        self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_104.addWidget(self.Button_DAT_GPTSoVITS_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_GPTSoVITS_OutputDirName = LineEditBase(self.Frame_DAT_GPTSoVITS_OutputDirName)
        self.LineEdit_DAT_GPTSoVITS_OutputDirName.setObjectName(u"LineEdit_DAT_GPTSoVITS_OutputDirName")
        self.LineEdit_DAT_GPTSoVITS_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_104.addWidget(self.LineEdit_DAT_GPTSoVITS_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_68.addWidget(self.Frame_DAT_GPTSoVITS_OutputDirName)


        self.verticalLayout_109.addWidget(self.Frame_DAT_GPTSoVITS_OutputParams_BasicSettings)

        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings = ToolBoxBase(self.GroupBox_DAT_GPTSoVITS_OutputParams)
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.setObjectName(u"ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings")
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.setFrameShape(QFrame.StyledPanel)
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.setFrameShadow(QFrame.Raised)
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content")
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 536, 105))
        self.verticalLayout_108 = QVBoxLayout(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_GPTSoVITS_FileListName = QFrame(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_GPTSoVITS_FileListName.setObjectName(u"Frame_DAT_GPTSoVITS_FileListName")
        self.Frame_DAT_GPTSoVITS_FileListName.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_GPTSoVITS_FileListName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_105 = QGridLayout(self.Frame_DAT_GPTSoVITS_FileListName)
        self.gridLayout_105.setSpacing(12)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.gridLayout_105.setContentsMargins(21, 12, 21, 12)
        self.Button_DAT_GPTSoVITS_FileListName_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_FileListName)
        self.Button_DAT_GPTSoVITS_FileListName_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_FileListName_MoreActions")
        self.Button_DAT_GPTSoVITS_FileListName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_FileListName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_GPTSoVITS_FileListName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_105.addWidget(self.Button_DAT_GPTSoVITS_FileListName_MoreActions, 0, 2, 1, 1)

        self.Label_DAT_GPTSoVITS_FileListName = QLabel(self.Frame_DAT_GPTSoVITS_FileListName)
        self.Label_DAT_GPTSoVITS_FileListName.setObjectName(u"Label_DAT_GPTSoVITS_FileListName")
        sizePolicy5.setHeightForWidth(self.Label_DAT_GPTSoVITS_FileListName.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_FileListName.setSizePolicy(sizePolicy5)
        self.Label_DAT_GPTSoVITS_FileListName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_105.addWidget(self.Label_DAT_GPTSoVITS_FileListName, 0, 0, 1, 1)

        self.LineEdit_DAT_GPTSoVITS_FileListName = LineEditBase(self.Frame_DAT_GPTSoVITS_FileListName)
        self.LineEdit_DAT_GPTSoVITS_FileListName.setObjectName(u"LineEdit_DAT_GPTSoVITS_FileListName")
        self.LineEdit_DAT_GPTSoVITS_FileListName.setMinimumSize(QSize(0, 27))

        self.gridLayout_105.addWidget(self.LineEdit_DAT_GPTSoVITS_FileListName, 1, 0, 1, 3)

        self.HorizontalSpacer_DAT_GPTSoVITS_FileListName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_105.addItem(self.HorizontalSpacer_DAT_GPTSoVITS_FileListName, 0, 1, 1, 1)


        self.verticalLayout_108.addWidget(self.Frame_DAT_GPTSoVITS_FileListName)

        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.addItem(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_109.addWidget(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings)


        self.verticalLayout_63.addWidget(self.GroupBox_DAT_GPTSoVITS_OutputParams)

        self.VerticalSpacer_DAT_GPTSoVITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_63.addItem(self.VerticalSpacer_DAT_GPTSoVITS)

        self.ScrollArea_Middle_DAT_GPTSoVITS.setWidget(self.ScrollArea_Middle_WidgetContents_DAT_GPTSoVITS)

        self.gridLayout_108.addWidget(self.ScrollArea_Middle_DAT_GPTSoVITS, 0, 1, 1, 1)

        self.Widget_Right_DAT_GPTSoVITS = QWidget(self.Subpage_DAT_GPTSoVITS)
        self.Widget_Right_DAT_GPTSoVITS.setObjectName(u"Widget_Right_DAT_GPTSoVITS")
        self.Widget_Right_DAT_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_5 = QGridLayout(self.Widget_Right_DAT_GPTSoVITS)
        self.gridLayout_5.setSpacing(12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_DAT_GPTSoVITS = QTextBrowser(self.Widget_Right_DAT_GPTSoVITS)
        self.TextBrowser_Params_DAT_GPTSoVITS.setObjectName(u"TextBrowser_Params_DAT_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_DAT_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_DAT_GPTSoVITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_DAT_GPTSoVITS.setStyleSheet(u"QTextBrowser {\n"
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
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_5.addWidget(self.TextBrowser_Params_DAT_GPTSoVITS, 0, 0, 1, 3)

        self.Button_ResetSettings_DAT_GPTSoVITS = QPushButton(self.Widget_Right_DAT_GPTSoVITS)
        self.Button_ResetSettings_DAT_GPTSoVITS.setObjectName(u"Button_ResetSettings_DAT_GPTSoVITS")
        self.Button_ResetSettings_DAT_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_5.addWidget(self.Button_ResetSettings_DAT_GPTSoVITS, 1, 0, 1, 1)

        self.Button_ImportSettings_DAT_GPTSoVITS = QPushButton(self.Widget_Right_DAT_GPTSoVITS)
        self.Button_ImportSettings_DAT_GPTSoVITS.setObjectName(u"Button_ImportSettings_DAT_GPTSoVITS")
        self.Button_ImportSettings_DAT_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_5.addWidget(self.Button_ImportSettings_DAT_GPTSoVITS, 1, 1, 1, 1)

        self.Button_ExportSettings_DAT_GPTSoVITS = QPushButton(self.Widget_Right_DAT_GPTSoVITS)
        self.Button_ExportSettings_DAT_GPTSoVITS.setObjectName(u"Button_ExportSettings_DAT_GPTSoVITS")
        self.Button_ExportSettings_DAT_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_5.addWidget(self.Button_ExportSettings_DAT_GPTSoVITS, 1, 2, 1, 1)

        self.Button_CheckOutput_DAT_GPTSoVITS = QPushButton(self.Widget_Right_DAT_GPTSoVITS)
        self.Button_CheckOutput_DAT_GPTSoVITS.setObjectName(u"Button_CheckOutput_DAT_GPTSoVITS")
        self.Button_CheckOutput_DAT_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_5.addWidget(self.Button_CheckOutput_DAT_GPTSoVITS, 2, 0, 1, 3)


        self.gridLayout_108.addWidget(self.Widget_Right_DAT_GPTSoVITS, 0, 2, 1, 1)

        self.ProgressBar_DAT_GPTSoVITS = QProgressBar(self.Subpage_DAT_GPTSoVITS)
        self.ProgressBar_DAT_GPTSoVITS.setObjectName(u"ProgressBar_DAT_GPTSoVITS")
        self.ProgressBar_DAT_GPTSoVITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_DAT_GPTSoVITS.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	background-color: transparent;\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgba(123, 123, 123, 123));\n"
"}")
        self.ProgressBar_DAT_GPTSoVITS.setValue(0)
        self.ProgressBar_DAT_GPTSoVITS.setTextVisible(False)
        self.horizontalLayout_42 = QHBoxLayout(self.ProgressBar_DAT_GPTSoVITS)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_DAT_GPTSoVITS = QStackedWidget(self.ProgressBar_DAT_GPTSoVITS)
        self.StackedWidget_DAT_GPTSoVITS.setObjectName(u"StackedWidget_DAT_GPTSoVITS")
        self.StackedWidget_DAT_GPTSoVITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_DAT_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
"}")
        self.Page_DAT_GPTSoVITS_Execute = QWidget()
        self.Page_DAT_GPTSoVITS_Execute.setObjectName(u"Page_DAT_GPTSoVITS_Execute")
        self.verticalLayout_101 = QVBoxLayout(self.Page_DAT_GPTSoVITS_Execute)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.Button_DAT_GPTSoVITS_Execute = QPushButton(self.Page_DAT_GPTSoVITS_Execute)
        self.Button_DAT_GPTSoVITS_Execute.setObjectName(u"Button_DAT_GPTSoVITS_Execute")
        sizePolicy3.setHeightForWidth(self.Button_DAT_GPTSoVITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_DAT_GPTSoVITS_Execute.setSizePolicy(sizePolicy3)
        self.Button_DAT_GPTSoVITS_Execute.setMinimumSize(QSize(0, 30))
        self.Button_DAT_GPTSoVITS_Execute.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"}")

        self.verticalLayout_101.addWidget(self.Button_DAT_GPTSoVITS_Execute)

        self.StackedWidget_DAT_GPTSoVITS.addWidget(self.Page_DAT_GPTSoVITS_Execute)
        self.Page_DAT_GPTSoVITS_Terminate = QWidget()
        self.Page_DAT_GPTSoVITS_Terminate.setObjectName(u"Page_DAT_GPTSoVITS_Terminate")
        self.verticalLayout_103 = QVBoxLayout(self.Page_DAT_GPTSoVITS_Terminate)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.Button_DAT_GPTSoVITS_Terminate = QPushButton(self.Page_DAT_GPTSoVITS_Terminate)
        self.Button_DAT_GPTSoVITS_Terminate.setObjectName(u"Button_DAT_GPTSoVITS_Terminate")
        sizePolicy3.setHeightForWidth(self.Button_DAT_GPTSoVITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_DAT_GPTSoVITS_Terminate.setSizePolicy(sizePolicy3)
        self.Button_DAT_GPTSoVITS_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_DAT_GPTSoVITS_Terminate.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"}")

        self.verticalLayout_103.addWidget(self.Button_DAT_GPTSoVITS_Terminate)

        self.StackedWidget_DAT_GPTSoVITS.addWidget(self.Page_DAT_GPTSoVITS_Terminate)

        self.horizontalLayout_42.addWidget(self.StackedWidget_DAT_GPTSoVITS)


        self.gridLayout_108.addWidget(self.ProgressBar_DAT_GPTSoVITS, 1, 0, 1, 3)

        self.gridLayout_108.setColumnStretch(0, 3)
        self.gridLayout_108.setColumnStretch(1, 10)
        self.gridLayout_108.setColumnStretch(2, 7)
        self.StackedWidget_Pages_Dataset.addWidget(self.Subpage_DAT_GPTSoVITS)
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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.Widget_Left_DAT_VITS)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_DAT_VITS = QTreeWidget(self.Widget_Left_DAT_VITS)
        __qtreewidgetitem4 = QTreeWidgetItem(self.TreeWidget_Catalogue_DAT_VITS)
        QTreeWidgetItem(__qtreewidgetitem4)
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
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal "
                        "{\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"}")

        self.verticalLayout_9.addWidget(self.TreeWidget_Catalogue_DAT_VITS)


        self.gridLayout_8.addWidget(self.Widget_Left_DAT_VITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_DAT_VITS = ScrollAreaBase(self.Subpage_DAT_VITS)
        self.ScrollArea_Middle_DAT_VITS.setObjectName(u"ScrollArea_Middle_DAT_VITS")
        self.ScrollArea_Middle_DAT_VITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_DAT_VITS.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_DAT_VITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_DAT_VITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_DAT_VITS.setObjectName(u"ScrollArea_Middle_WidgetContents_DAT_VITS")
        self.ScrollArea_Middle_WidgetContents_DAT_VITS.setGeometry(QRect(0, 0, 581, 1006))
        self.verticalLayout_36 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.verticalLayout_36.setSpacing(12)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_DAT_VITS_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.GroupBox_DAT_VITS_InputParams.setObjectName(u"GroupBox_DAT_VITS_InputParams")
        self.GroupBox_DAT_VITS_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_46.addWidget(self.Label_DAT_VITS_AudioSpeakersDataPath, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_InputParams = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_46.addItem(self.HorizontalSpacer_DAT_VITS_InputParams, 0, 1, 1, 1)

        self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions = MenuButton(self.Frame_DAT_VITS_AudioSpeakersDataPath)
        self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions.setObjectName(u"Button_DAT_VITS_AudioSpeakersDataPath_MoreActions")
        self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_46.addWidget(self.Button_DAT_VITS_AudioSpeakersDataPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_AudioSpeakersDataPath = LineEditBase(self.Frame_DAT_VITS_AudioSpeakersDataPath)
        self.LineEdit_DAT_VITS_AudioSpeakersDataPath.setObjectName(u"LineEdit_DAT_VITS_AudioSpeakersDataPath")
        self.LineEdit_DAT_VITS_AudioSpeakersDataPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_46.addWidget(self.LineEdit_DAT_VITS_AudioSpeakersDataPath, 1, 0, 1, 3)


        self.verticalLayout_29.addWidget(self.Frame_DAT_VITS_AudioSpeakersDataPath)

        self.Frame_DAT_VITS_SRTDir = QFrame(self.Frame_DAT_VITS_InputParams_BasicSettings)
        self.Frame_DAT_VITS_SRTDir.setObjectName(u"Frame_DAT_VITS_SRTDir")
        self.Frame_DAT_VITS_SRTDir.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SRTDir.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_47.addWidget(self.Label_DAT_VITS_SRTDir, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_SRTDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_47.addItem(self.HorizontalSpacer_DAT_VITS_SRTDir, 0, 1, 1, 1)

        self.Button_DAT_VITS_SRTDir_MoreActions = MenuButton(self.Frame_DAT_VITS_SRTDir)
        self.Button_DAT_VITS_SRTDir_MoreActions.setObjectName(u"Button_DAT_VITS_SRTDir_MoreActions")
        self.Button_DAT_VITS_SRTDir_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_SRTDir_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_SRTDir_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_47.addWidget(self.Button_DAT_VITS_SRTDir_MoreActions, 0, 2, 1, 1)

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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_76.addWidget(self.Label_DAT_VITS_DataFormat, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_DataFormat = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_76.addItem(self.HorizontalSpacer_DAT_VITS_DataFormat, 0, 1, 1, 1)

        self.Button_DAT_VITS_DataFormat_MoreActions = MenuButton(self.Frame_DAT_VITS_DataFormat)
        self.Button_DAT_VITS_DataFormat_MoreActions.setObjectName(u"Button_DAT_VITS_DataFormat_MoreActions")
        self.Button_DAT_VITS_DataFormat_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_DataFormat_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_DataFormat_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_76.addWidget(self.Button_DAT_VITS_DataFormat_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_DataFormat = LineEditBase(self.Frame_DAT_VITS_DataFormat)
        self.LineEdit_DAT_VITS_DataFormat.setObjectName(u"LineEdit_DAT_VITS_DataFormat")
        self.LineEdit_DAT_VITS_DataFormat.setMinimumSize(QSize(0, 27))

        self.gridLayout_76.addWidget(self.LineEdit_DAT_VITS_DataFormat, 1, 0, 1, 3)


        self.verticalLayout_30.addWidget(self.Frame_DAT_VITS_DataFormat)

        self.Frame_DAT_VITS_AddAuxiliaryData = QFrame(self.Frame_DAT_VITS_VITSParams_BasicSettings)
        self.Frame_DAT_VITS_AddAuxiliaryData.setObjectName(u"Frame_DAT_VITS_AddAuxiliaryData")
        self.Frame_DAT_VITS_AddAuxiliaryData.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_AddAuxiliaryData.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_48.addWidget(self.Label_DAT_VITS_AddAuxiliaryData, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_AddAuxiliaryData = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_48.addItem(self.HorizontalSpacer_DAT_VITS_AddAuxiliaryData, 0, 1, 1, 1)

        self.Button_DAT_VITS_AddAuxiliaryData_MoreActions = MenuButton(self.Frame_DAT_VITS_AddAuxiliaryData)
        self.Button_DAT_VITS_AddAuxiliaryData_MoreActions.setObjectName(u"Button_DAT_VITS_AddAuxiliaryData_MoreActions")
        self.Button_DAT_VITS_AddAuxiliaryData_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_AddAuxiliaryData_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_AddAuxiliaryData_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_48.addWidget(self.Button_DAT_VITS_AddAuxiliaryData_MoreActions, 0, 2, 1, 1)

        self.CheckBox_DAT_VITS_AddAuxiliaryData = QCheckBox(self.Frame_DAT_VITS_AddAuxiliaryData)
        self.CheckBox_DAT_VITS_AddAuxiliaryData.setObjectName(u"CheckBox_DAT_VITS_AddAuxiliaryData")
        self.CheckBox_DAT_VITS_AddAuxiliaryData.setMinimumSize(QSize(0, 27))
        self.CheckBox_DAT_VITS_AddAuxiliaryData.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_48.addWidget(self.CheckBox_DAT_VITS_AddAuxiliaryData, 1, 0, 1, 3)


        self.verticalLayout_30.addWidget(self.Frame_DAT_VITS_AddAuxiliaryData)

        self.Frame_DAT_VITS_AuxiliaryDataPath = QFrame(self.Frame_DAT_VITS_VITSParams_BasicSettings)
        self.Frame_DAT_VITS_AuxiliaryDataPath.setObjectName(u"Frame_DAT_VITS_AuxiliaryDataPath")
        self.Frame_DAT_VITS_AuxiliaryDataPath.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_AuxiliaryDataPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_53.addWidget(self.Label_DAT_VITS_AuxiliaryDataPath, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_AuxiliaryDataPath = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.HorizontalSpacer_DAT_VITS_AuxiliaryDataPath, 0, 1, 1, 1)

        self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions = MenuButton(self.Frame_DAT_VITS_AuxiliaryDataPath)
        self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions.setObjectName(u"Button_DAT_VITS_AuxiliaryDataPath_MoreActions")
        self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_53.addWidget(self.Button_DAT_VITS_AuxiliaryDataPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_AuxiliaryDataPath = LineEditBase(self.Frame_DAT_VITS_AuxiliaryDataPath)
        self.LineEdit_DAT_VITS_AuxiliaryDataPath.setObjectName(u"LineEdit_DAT_VITS_AuxiliaryDataPath")
        self.LineEdit_DAT_VITS_AuxiliaryDataPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_53.addWidget(self.LineEdit_DAT_VITS_AuxiliaryDataPath, 1, 0, 1, 3)


        self.verticalLayout_30.addWidget(self.Frame_DAT_VITS_AuxiliaryDataPath)


        self.verticalLayout_115.addWidget(self.Frame_DAT_VITS_VITSParams_BasicSettings)

        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings = ToolBoxBase(self.GroupBox_DAT_VITS_VITSParams)
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.setObjectName(u"ToolBox_DAT_VITS_VITSParams_AdvanceSettings")
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.setFrameShape(QFrame.StyledPanel)
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.setFrameShadow(QFrame.Raised)
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content")
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 420))
        self.verticalLayout_53 = QVBoxLayout(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_TrainRatio = QFrame(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_TrainRatio.setObjectName(u"Frame_DAT_VITS_TrainRatio")
        self.Frame_DAT_VITS_TrainRatio.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_TrainRatio.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_49.addWidget(self.Label_DAT_VITS_TrainRatio, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_TrainRatio = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_49.addItem(self.HorizontalSpacer_DAT_VITS_TrainRatio, 0, 1, 1, 1)

        self.Button_DAT_VITS_TrainRatio_MoreActions = MenuButton(self.Frame_DAT_VITS_TrainRatio)
        self.Button_DAT_VITS_TrainRatio_MoreActions.setObjectName(u"Button_DAT_VITS_TrainRatio_MoreActions")
        self.Button_DAT_VITS_TrainRatio_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_TrainRatio_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_TrainRatio_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_49.addWidget(self.Button_DAT_VITS_TrainRatio_MoreActions, 0, 2, 1, 1)

        self.DoubleSpinBox_DAT_VITS_TrainRatio = DoubleSpinBoxBase(self.Frame_DAT_VITS_TrainRatio)
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setObjectName(u"DoubleSpinBox_DAT_VITS_TrainRatio")
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setEnabled(True)
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_DAT_VITS_TrainRatio.setMaximum(999999.000000000000000)

        self.gridLayout_49.addWidget(self.DoubleSpinBox_DAT_VITS_TrainRatio, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_TrainRatio)

        self.Frame_DAT_VITS_SampleRate = QFrame(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_SampleRate.setObjectName(u"Frame_DAT_VITS_SampleRate")
        self.Frame_DAT_VITS_SampleRate.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SampleRate.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_50.addWidget(self.Label_DAT_VITS_SampleRate, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_SampleRate = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_50.addItem(self.HorizontalSpacer_DAT_VITS_SampleRate, 0, 1, 1, 1)

        self.Button_DAT_VITS_SampleRate_MoreActions = MenuButton(self.Frame_DAT_VITS_SampleRate)
        self.Button_DAT_VITS_SampleRate_MoreActions.setObjectName(u"Button_DAT_VITS_SampleRate_MoreActions")
        self.Button_DAT_VITS_SampleRate_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleRate_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleRate_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_50.addWidget(self.Button_DAT_VITS_SampleRate_MoreActions, 0, 2, 1, 1)

        self.ComboBox_DAT_VITS_SampleRate = ComboBoxBase(self.Frame_DAT_VITS_SampleRate)
        self.ComboBox_DAT_VITS_SampleRate.setObjectName(u"ComboBox_DAT_VITS_SampleRate")
        self.ComboBox_DAT_VITS_SampleRate.setMinimumSize(QSize(0, 27))

        self.gridLayout_50.addWidget(self.ComboBox_DAT_VITS_SampleRate, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_SampleRate)

        self.Frame_DAT_VITS_SampleWidth = QFrame(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_SampleWidth.setObjectName(u"Frame_DAT_VITS_SampleWidth")
        self.Frame_DAT_VITS_SampleWidth.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SampleWidth.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_51.addWidget(self.Label_DAT_VITS_SampleWidth, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_SampleWidth = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_51.addItem(self.HorizontalSpacer_DAT_VITS_SampleWidth, 0, 1, 1, 1)

        self.Button_DAT_VITS_SampleWidth_MoreActions = MenuButton(self.Frame_DAT_VITS_SampleWidth)
        self.Button_DAT_VITS_SampleWidth_MoreActions.setObjectName(u"Button_DAT_VITS_SampleWidth_MoreActions")
        self.Button_DAT_VITS_SampleWidth_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleWidth_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_SampleWidth_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_51.addWidget(self.Button_DAT_VITS_SampleWidth_MoreActions, 0, 2, 1, 1)

        self.ComboBox_DAT_VITS_SampleWidth = ComboBoxBase(self.Frame_DAT_VITS_SampleWidth)
        self.ComboBox_DAT_VITS_SampleWidth.setObjectName(u"ComboBox_DAT_VITS_SampleWidth")
        self.ComboBox_DAT_VITS_SampleWidth.setMinimumSize(QSize(0, 27))

        self.gridLayout_51.addWidget(self.ComboBox_DAT_VITS_SampleWidth, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_SampleWidth)

        self.Frame_DAT_VITS_ToMono = QFrame(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_ToMono.setObjectName(u"Frame_DAT_VITS_ToMono")
        self.Frame_DAT_VITS_ToMono.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_ToMono.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_52.addWidget(self.Label_DAT_VITS_ToMono, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_ToMono = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_52.addItem(self.HorizontalSpacer_DAT_VITS_ToMono, 0, 1, 1, 1)

        self.Button_DAT_VITS_ToMono_MoreActions = MenuButton(self.Frame_DAT_VITS_ToMono)
        self.Button_DAT_VITS_ToMono_MoreActions.setObjectName(u"Button_DAT_VITS_ToMono_MoreActions")
        self.Button_DAT_VITS_ToMono_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_ToMono_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_ToMono_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_52.addWidget(self.Button_DAT_VITS_ToMono_MoreActions, 0, 2, 1, 1)

        self.CheckBox_DAT_VITS_ToMono = QCheckBox(self.Frame_DAT_VITS_ToMono)
        self.CheckBox_DAT_VITS_ToMono.setObjectName(u"CheckBox_DAT_VITS_ToMono")
        self.CheckBox_DAT_VITS_ToMono.setMinimumSize(QSize(0, 27))
        self.CheckBox_DAT_VITS_ToMono.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_52.addWidget(self.CheckBox_DAT_VITS_ToMono, 1, 0, 1, 3)


        self.verticalLayout_53.addWidget(self.Frame_DAT_VITS_ToMono)

        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.addItem(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_115.addWidget(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings)


        self.verticalLayout_36.addWidget(self.GroupBox_DAT_VITS_VITSParams)

        self.GroupBox_DAT_VITS_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.GroupBox_DAT_VITS_OutputParams.setObjectName(u"GroupBox_DAT_VITS_OutputParams")
        self.GroupBox_DAT_VITS_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_107 = QVBoxLayout(self.GroupBox_DAT_VITS_OutputParams)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 12, 0, 12)
        self.Frame_DAT_VITS_OutputParams_BasicSettings = QFrame(self.GroupBox_DAT_VITS_OutputParams)
        self.Frame_DAT_VITS_OutputParams_BasicSettings.setObjectName(u"Frame_DAT_VITS_OutputParams_BasicSettings")
        self.verticalLayout_31 = QVBoxLayout(self.Frame_DAT_VITS_OutputParams_BasicSettings)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_OutputDirName = QFrame(self.Frame_DAT_VITS_OutputParams_BasicSettings)
        self.Frame_DAT_VITS_OutputDirName.setObjectName(u"Frame_DAT_VITS_OutputDirName")
        self.Frame_DAT_VITS_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_54 = QGridLayout(self.Frame_DAT_VITS_OutputDirName)
        self.gridLayout_54.setSpacing(12)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_OutputDirName = QLabel(self.Frame_DAT_VITS_OutputDirName)
        self.Label_DAT_VITS_OutputDirName.setObjectName(u"Label_DAT_VITS_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_54.addWidget(self.Label_DAT_VITS_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_OutputDirName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_54.addItem(self.HorizontalSpacer_DAT_VITS_OutputDirName, 0, 1, 1, 1)

        self.Button_DAT_VITS_OutputDirName_MoreActions = MenuButton(self.Frame_DAT_VITS_OutputDirName)
        self.Button_DAT_VITS_OutputDirName_MoreActions.setObjectName(u"Button_DAT_VITS_OutputDirName_MoreActions")
        self.Button_DAT_VITS_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_54.addWidget(self.Button_DAT_VITS_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_OutputDirName = LineEditBase(self.Frame_DAT_VITS_OutputDirName)
        self.LineEdit_DAT_VITS_OutputDirName.setObjectName(u"LineEdit_DAT_VITS_OutputDirName")
        self.LineEdit_DAT_VITS_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_54.addWidget(self.LineEdit_DAT_VITS_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_31.addWidget(self.Frame_DAT_VITS_OutputDirName)


        self.verticalLayout_107.addWidget(self.Frame_DAT_VITS_OutputParams_BasicSettings)

        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings = ToolBoxBase(self.GroupBox_DAT_VITS_OutputParams)
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.setObjectName(u"ToolBox_DAT_VITS_OutputParams_AdvanceSettings")
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.setFrameShape(QFrame.StyledPanel)
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.setFrameShadow(QFrame.Raised)
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content")
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 210))
        self.verticalLayout_88 = QVBoxLayout(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_FileListNameTraining = QFrame(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_FileListNameTraining.setObjectName(u"Frame_DAT_VITS_FileListNameTraining")
        self.Frame_DAT_VITS_FileListNameTraining.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_FileListNameTraining.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_55 = QGridLayout(self.Frame_DAT_VITS_FileListNameTraining)
        self.gridLayout_55.setSpacing(12)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(21, 12, 21, 12)
        self.Button_DAT_VITS_FileListNameTraining_MoreActions = MenuButton(self.Frame_DAT_VITS_FileListNameTraining)
        self.Button_DAT_VITS_FileListNameTraining_MoreActions.setObjectName(u"Button_DAT_VITS_FileListNameTraining_MoreActions")
        self.Button_DAT_VITS_FileListNameTraining_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListNameTraining_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListNameTraining_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_55.addWidget(self.Button_DAT_VITS_FileListNameTraining_MoreActions, 0, 2, 1, 1)

        self.Label_DAT_VITS_FileListNameTraining = QLabel(self.Frame_DAT_VITS_FileListNameTraining)
        self.Label_DAT_VITS_FileListNameTraining.setObjectName(u"Label_DAT_VITS_FileListNameTraining")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_FileListNameTraining.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_FileListNameTraining.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_FileListNameTraining.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_55.addWidget(self.Label_DAT_VITS_FileListNameTraining, 0, 0, 1, 1)

        self.LineEdit_DAT_VITS_FileListNameTraining = LineEditBase(self.Frame_DAT_VITS_FileListNameTraining)
        self.LineEdit_DAT_VITS_FileListNameTraining.setObjectName(u"LineEdit_DAT_VITS_FileListNameTraining")
        self.LineEdit_DAT_VITS_FileListNameTraining.setMinimumSize(QSize(0, 27))

        self.gridLayout_55.addWidget(self.LineEdit_DAT_VITS_FileListNameTraining, 1, 0, 1, 3)

        self.HorizontalSpacer_DAT_VITS_FileListNameTraining = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_55.addItem(self.HorizontalSpacer_DAT_VITS_FileListNameTraining, 0, 1, 1, 1)


        self.verticalLayout_88.addWidget(self.Frame_DAT_VITS_FileListNameTraining)

        self.Frame_DAT_VITS_FileListNameValidation = QFrame(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_DAT_VITS_FileListNameValidation.setObjectName(u"Frame_DAT_VITS_FileListNameValidation")
        self.Frame_DAT_VITS_FileListNameValidation.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_FileListNameValidation.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_56 = QGridLayout(self.Frame_DAT_VITS_FileListNameValidation)
        self.gridLayout_56.setSpacing(12)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_FileListNameValidation = QLabel(self.Frame_DAT_VITS_FileListNameValidation)
        self.Label_DAT_VITS_FileListNameValidation.setObjectName(u"Label_DAT_VITS_FileListNameValidation")
        sizePolicy5.setHeightForWidth(self.Label_DAT_VITS_FileListNameValidation.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_FileListNameValidation.setSizePolicy(sizePolicy5)
        self.Label_DAT_VITS_FileListNameValidation.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_56.addWidget(self.Label_DAT_VITS_FileListNameValidation, 0, 0, 1, 1)

        self.HorizontalSpacer_DAT_VITS_FileListNameValidation = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.HorizontalSpacer_DAT_VITS_FileListNameValidation, 0, 1, 1, 1)

        self.Button_DAT_VITS_FileListNameValidation_MoreActions = MenuButton(self.Frame_DAT_VITS_FileListNameValidation)
        self.Button_DAT_VITS_FileListNameValidation_MoreActions.setObjectName(u"Button_DAT_VITS_FileListNameValidation_MoreActions")
        self.Button_DAT_VITS_FileListNameValidation_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListNameValidation_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileListNameValidation_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_56.addWidget(self.Button_DAT_VITS_FileListNameValidation_MoreActions, 0, 2, 1, 1)

        self.LineEdit_DAT_VITS_FileListNameValidation = LineEditBase(self.Frame_DAT_VITS_FileListNameValidation)
        self.LineEdit_DAT_VITS_FileListNameValidation.setObjectName(u"LineEdit_DAT_VITS_FileListNameValidation")
        self.LineEdit_DAT_VITS_FileListNameValidation.setMinimumSize(QSize(0, 27))

        self.gridLayout_56.addWidget(self.LineEdit_DAT_VITS_FileListNameValidation, 1, 0, 1, 3)


        self.verticalLayout_88.addWidget(self.Frame_DAT_VITS_FileListNameValidation)

        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.addItem(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_107.addWidget(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings)


        self.verticalLayout_36.addWidget(self.GroupBox_DAT_VITS_OutputParams)

        self.VerticalSpacer_DAT_VITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.VerticalSpacer_DAT_VITS)

        self.ScrollArea_Middle_DAT_VITS.setWidget(self.ScrollArea_Middle_WidgetContents_DAT_VITS)

        self.gridLayout_8.addWidget(self.ScrollArea_Middle_DAT_VITS, 0, 1, 1, 1)

        self.Widget_Right_DAT_VITS = QWidget(self.Subpage_DAT_VITS)
        self.Widget_Right_DAT_VITS.setObjectName(u"Widget_Right_DAT_VITS")
        self.Widget_Right_DAT_VITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_9 = QGridLayout(self.Widget_Right_DAT_VITS)
        self.gridLayout_9.setSpacing(12)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_DAT_VITS = QTextBrowser(self.Widget_Right_DAT_VITS)
        self.TextBrowser_Params_DAT_VITS.setObjectName(u"TextBrowser_Params_DAT_VITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_DAT_VITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_DAT_VITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_DAT_VITS.setStyleSheet(u"QTextBrowser {\n"
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
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_9.addWidget(self.TextBrowser_Params_DAT_VITS, 0, 0, 1, 3)

        self.Button_ResetSettings_DAT_VITS = QPushButton(self.Widget_Right_DAT_VITS)
        self.Button_ResetSettings_DAT_VITS.setObjectName(u"Button_ResetSettings_DAT_VITS")
        self.Button_ResetSettings_DAT_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_9.addWidget(self.Button_ResetSettings_DAT_VITS, 1, 0, 1, 1)

        self.Button_ImportSettings_DAT_VITS = QPushButton(self.Widget_Right_DAT_VITS)
        self.Button_ImportSettings_DAT_VITS.setObjectName(u"Button_ImportSettings_DAT_VITS")
        self.Button_ImportSettings_DAT_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_9.addWidget(self.Button_ImportSettings_DAT_VITS, 1, 1, 1, 1)

        self.Button_ExportSettings_DAT_VITS = QPushButton(self.Widget_Right_DAT_VITS)
        self.Button_ExportSettings_DAT_VITS.setObjectName(u"Button_ExportSettings_DAT_VITS")
        self.Button_ExportSettings_DAT_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_9.addWidget(self.Button_ExportSettings_DAT_VITS, 1, 2, 1, 1)

        self.Button_CheckOutput_DAT_VITS = QPushButton(self.Widget_Right_DAT_VITS)
        self.Button_CheckOutput_DAT_VITS.setObjectName(u"Button_CheckOutput_DAT_VITS")
        self.Button_CheckOutput_DAT_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_9.addWidget(self.Button_CheckOutput_DAT_VITS, 2, 0, 1, 3)


        self.gridLayout_8.addWidget(self.Widget_Right_DAT_VITS, 0, 2, 1, 1)

        self.ProgressBar_DAT_VITS = QProgressBar(self.Subpage_DAT_VITS)
        self.ProgressBar_DAT_VITS.setObjectName(u"ProgressBar_DAT_VITS")
        self.ProgressBar_DAT_VITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_DAT_VITS.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	background-color: transparent;\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgba(123, 123, 123, 123));\n"
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
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
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
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
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
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.Frame_Train_Top)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_VoiceTrainer_Title_GPTSoVITS = QToolButton(self.Frame_Train_Top)
        self.ToolButton_VoiceTrainer_Title_GPTSoVITS.setObjectName(u"ToolButton_VoiceTrainer_Title_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.ToolButton_VoiceTrainer_Title_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.ToolButton_VoiceTrainer_Title_GPTSoVITS.setSizePolicy(sizePolicy1)
        self.ToolButton_VoiceTrainer_Title_GPTSoVITS.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_15.addWidget(self.ToolButton_VoiceTrainer_Title_GPTSoVITS)

        self.ToolButton_VoiceTrainer_Title_VITS = QToolButton(self.Frame_Train_Top)
        self.ToolButton_VoiceTrainer_Title_VITS.setObjectName(u"ToolButton_VoiceTrainer_Title_VITS")
        sizePolicy1.setHeightForWidth(self.ToolButton_VoiceTrainer_Title_VITS.sizePolicy().hasHeightForWidth())
        self.ToolButton_VoiceTrainer_Title_VITS.setSizePolicy(sizePolicy1)
        self.ToolButton_VoiceTrainer_Title_VITS.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_15.addWidget(self.ToolButton_VoiceTrainer_Title_VITS)

        self.Frame_VoiceTrainer_Title = QFrame(self.Frame_Train_Top)
        self.Frame_VoiceTrainer_Title.setObjectName(u"Frame_VoiceTrainer_Title")
        self.Frame_VoiceTrainer_Title.setStyleSheet(u"QFrame {\n"
"	/*font-size: 24px;\n"
"	text-align: center;\n"
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
        self.horizontalLayout_58 = QHBoxLayout(self.Frame_VoiceTrainer_Title)
        self.horizontalLayout_58.setSpacing(12)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSpacer_VoiceTrainer_Title = QSpacerItem(549, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_58.addItem(self.HorizontalSpacer_VoiceTrainer_Title)


        self.horizontalLayout_15.addWidget(self.Frame_VoiceTrainer_Title)


        self.verticalLayout_43.addWidget(self.Frame_Train_Top)

        self.StackedWidget_Pages_Train = QStackedWidget(self.Page_Train)
        self.StackedWidget_Pages_Train.setObjectName(u"StackedWidget_Pages_Train")
        self.StackedWidget_Pages_Train.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.Subpage_Train_GPTSoVITS = QWidget()
        self.Subpage_Train_GPTSoVITS.setObjectName(u"Subpage_Train_GPTSoVITS")
        self.gridLayout_85 = QGridLayout(self.Subpage_Train_GPTSoVITS)
        self.gridLayout_85.setSpacing(12)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.gridLayout_85.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_Train_GPTSoVITS = QWidget(self.Subpage_Train_GPTSoVITS)
        self.Widget_Left_Train_GPTSoVITS.setObjectName(u"Widget_Left_Train_GPTSoVITS")
        self.Widget_Left_Train_GPTSoVITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_Train_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_59 = QVBoxLayout(self.Widget_Left_Train_GPTSoVITS)
        self.verticalLayout_59.setSpacing(12)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Train_GPTSoVITS = QTreeWidget(self.Widget_Left_Train_GPTSoVITS)
        __qtreewidgetitem5 = QTreeWidgetItem(self.TreeWidget_Catalogue_Train_GPTSoVITS)
        QTreeWidgetItem(__qtreewidgetitem5)
        self.TreeWidget_Catalogue_Train_GPTSoVITS.setObjectName(u"TreeWidget_Catalogue_Train_GPTSoVITS")
        self.TreeWidget_Catalogue_Train_GPTSoVITS.setStyleSheet(u"QTreeView {\n"
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
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal "
                        "{\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"}")

        self.verticalLayout_59.addWidget(self.TreeWidget_Catalogue_Train_GPTSoVITS)


        self.gridLayout_85.addWidget(self.Widget_Left_Train_GPTSoVITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_Train_GPTSoVITS = ScrollAreaBase(self.Subpage_Train_GPTSoVITS)
        self.ScrollArea_Middle_Train_GPTSoVITS.setObjectName(u"ScrollArea_Middle_Train_GPTSoVITS")
        self.ScrollArea_Middle_Train_GPTSoVITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_Train_GPTSoVITS.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Train_GPTSoVITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS.setObjectName(u"ScrollArea_Middle_WidgetContents_Train_GPTSoVITS")
        self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS.setGeometry(QRect(0, 0, 581, 1109))
        self.verticalLayout_52 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS)
        self.verticalLayout_52.setSpacing(12)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_Train_GPTSoVITS_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS)
        self.GroupBox_Train_GPTSoVITS_InputParams.setObjectName(u"GroupBox_Train_GPTSoVITS_InputParams")
        self.GroupBox_Train_GPTSoVITS_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_121 = QVBoxLayout(self.GroupBox_Train_GPTSoVITS_InputParams)
        self.verticalLayout_121.setSpacing(0)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 12, 0, 12)
        self.Frame_Train_GPTSoVITS_InputParams_BasicSettings = QFrame(self.GroupBox_Train_GPTSoVITS_InputParams)
        self.Frame_Train_GPTSoVITS_InputParams_BasicSettings.setObjectName(u"Frame_Train_GPTSoVITS_InputParams_BasicSettings")
        self.verticalLayout_55 = QVBoxLayout(self.Frame_Train_GPTSoVITS_InputParams_BasicSettings)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_GPTSoVITS_FileListPath = QFrame(self.Frame_Train_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_FileListPath.setObjectName(u"Frame_Train_GPTSoVITS_FileListPath")
        self.Frame_Train_GPTSoVITS_FileListPath.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_FileListPath.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_81 = QGridLayout(self.Frame_Train_GPTSoVITS_FileListPath)
        self.gridLayout_81.setSpacing(12)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.gridLayout_81.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_FileListPath = QLabel(self.Frame_Train_GPTSoVITS_FileListPath)
        self.Label_Train_GPTSoVITS_FileListPath.setObjectName(u"Label_Train_GPTSoVITS_FileListPath")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_FileListPath.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_FileListPath.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_FileListPath.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_81.addWidget(self.Label_Train_GPTSoVITS_FileListPath, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_FileListPath = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_81.addItem(self.HorizontalSpacer_Train_GPTSoVITS_FileListPath, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_FileListPath_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_FileListPath)
        self.Button_Train_GPTSoVITS_FileListPath_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_FileListPath_MoreActions")
        self.Button_Train_GPTSoVITS_FileListPath_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_FileListPath_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_FileListPath_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_81.addWidget(self.Button_Train_GPTSoVITS_FileListPath_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_FileListPath = LineEditBase(self.Frame_Train_GPTSoVITS_FileListPath)
        self.LineEdit_Train_GPTSoVITS_FileListPath.setObjectName(u"LineEdit_Train_GPTSoVITS_FileListPath")
        self.LineEdit_Train_GPTSoVITS_FileListPath.setMinimumSize(QSize(0, 27))

        self.gridLayout_81.addWidget(self.LineEdit_Train_GPTSoVITS_FileListPath, 1, 0, 1, 3)


        self.verticalLayout_55.addWidget(self.Frame_Train_GPTSoVITS_FileListPath)


        self.verticalLayout_121.addWidget(self.Frame_Train_GPTSoVITS_InputParams_BasicSettings)


        self.verticalLayout_52.addWidget(self.GroupBox_Train_GPTSoVITS_InputParams)

        self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS)
        self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams.setObjectName(u"GroupBox_Train_GPTSoVITS_GPTSoVITSParams")
        self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_122 = QVBoxLayout(self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 12, 0, 12)
        self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings = QFrame(self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams)
        self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings.setObjectName(u"Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings")
        self.verticalLayout_56 = QVBoxLayout(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1 = QFrame(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1.setObjectName(u"Frame_Train_GPTSoVITS_ModelPathPretrainedS1")
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_88 = QGridLayout(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1)
        self.gridLayout_88.setSpacing(12)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.gridLayout_88.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS1 = QLabel(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS1.setObjectName(u"Label_Train_GPTSoVITS_ModelPathPretrainedS1")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_ModelPathPretrainedS1.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS1.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS1.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_88.addWidget(self.Label_Train_GPTSoVITS_ModelPathPretrainedS1, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS1 = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_88.addItem(self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS1, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1)
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions")
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_88.addWidget(self.Button_Train_GPTSoVITS_ModelPathPretrainedS1_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1 = LineEditBase(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1)
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1.setObjectName(u"LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1")
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1.setMinimumSize(QSize(0, 27))

        self.gridLayout_88.addWidget(self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS1, 1, 0, 1, 3)


        self.verticalLayout_56.addWidget(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS1)

        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G = QFrame(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G.setObjectName(u"Frame_Train_GPTSoVITS_ModelPathPretrainedS2G")
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_86 = QGridLayout(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G)
        self.gridLayout_86.setSpacing(12)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.gridLayout_86.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G = QLabel(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G.setObjectName(u"Label_Train_GPTSoVITS_ModelPathPretrainedS2G")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_86.addWidget(self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS2G = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_86.addItem(self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS2G, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G)
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions")
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_86.addWidget(self.Button_Train_GPTSoVITS_ModelPathPretrainedS2G_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G = LineEditBase(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G)
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G.setObjectName(u"LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G")
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G.setMinimumSize(QSize(0, 27))

        self.gridLayout_86.addWidget(self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2G, 1, 0, 1, 3)


        self.verticalLayout_56.addWidget(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2G)

        self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert = QFrame(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert.setObjectName(u"Frame_Train_GPTSoVITS_ModelDirPretrainedBert")
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_89 = QGridLayout(self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert)
        self.gridLayout_89.setSpacing(12)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.gridLayout_89.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedBert = QLabel(self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedBert.setObjectName(u"Label_Train_GPTSoVITS_ModelDirPretrainedBert")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_ModelDirPretrainedBert.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_ModelDirPretrainedBert.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedBert.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_89.addWidget(self.Label_Train_GPTSoVITS_ModelDirPretrainedBert, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_ModelDirPretrainedBert = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_89.addItem(self.HorizontalSpacer_Train_GPTSoVITS_ModelDirPretrainedBert, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert)
        self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions")
        self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_89.addWidget(self.Button_Train_GPTSoVITS_ModelDirPretrainedBert_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert = LineEditBase(self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert)
        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert.setObjectName(u"LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert")
        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert.setMinimumSize(QSize(0, 27))

        self.gridLayout_89.addWidget(self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedBert, 1, 0, 1, 3)


        self.verticalLayout_56.addWidget(self.Frame_Train_GPTSoVITS_ModelDirPretrainedBert)

        self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL = QFrame(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL.setObjectName(u"Frame_Train_GPTSoVITS_ModelDirPretrainedSSL")
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_95 = QGridLayout(self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL)
        self.gridLayout_95.setSpacing(12)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.gridLayout_95.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL = QLabel(self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL.setObjectName(u"Label_Train_GPTSoVITS_ModelDirPretrainedSSL")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_95.addWidget(self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_ModelDirPretrainedSSL = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_95.addItem(self.HorizontalSpacer_Train_GPTSoVITS_ModelDirPretrainedSSL, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL)
        self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions")
        self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_95.addWidget(self.Button_Train_GPTSoVITS_ModelDirPretrainedSSL_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL = LineEditBase(self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL)
        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL.setObjectName(u"LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL")
        self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL.setMinimumSize(QSize(0, 27))

        self.gridLayout_95.addWidget(self.LineEdit_Train_GPTSoVITS_ModelDirPretrainedSSL, 1, 0, 1, 3)


        self.verticalLayout_56.addWidget(self.Frame_Train_GPTSoVITS_ModelDirPretrainedSSL)

        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D = QFrame(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D.setObjectName(u"Frame_Train_GPTSoVITS_ModelPathPretrainedS2D")
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_87 = QGridLayout(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D)
        self.gridLayout_87.setSpacing(12)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.gridLayout_87.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D = QLabel(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D.setObjectName(u"Label_Train_GPTSoVITS_ModelPathPretrainedS2D")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_87.addWidget(self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS2D = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_87.addItem(self.HorizontalSpacer_Train_GPTSoVITS_ModelPathPretrainedS2D, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D)
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions")
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_87.addWidget(self.Button_Train_GPTSoVITS_ModelPathPretrainedS2D_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D = LineEditBase(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D)
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D.setObjectName(u"LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D")
        self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D.setMinimumSize(QSize(0, 27))

        self.gridLayout_87.addWidget(self.LineEdit_Train_GPTSoVITS_ModelPathPretrainedS2D, 1, 0, 1, 3)


        self.verticalLayout_56.addWidget(self.Frame_Train_GPTSoVITS_ModelPathPretrainedS2D)


        self.verticalLayout_122.addWidget(self.Frame_Train_GPTSoVITS_GPTSoVITSParams_BasicSettings)

        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings = ToolBoxBase(self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams)
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.setObjectName(u"ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings")
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.setFrameShape(QFrame.StyledPanel)
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.setFrameShadow(QFrame.Raised)
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content")
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 536, 105))
        self.verticalLayout_57 = QVBoxLayout(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_GPTSoVITS_FP16Run = QFrame(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content)
        self.Frame_Train_GPTSoVITS_FP16Run.setObjectName(u"Frame_Train_GPTSoVITS_FP16Run")
        self.Frame_Train_GPTSoVITS_FP16Run.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_FP16Run.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_91 = QGridLayout(self.Frame_Train_GPTSoVITS_FP16Run)
        self.gridLayout_91.setSpacing(12)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.gridLayout_91.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_FP16Run = QLabel(self.Frame_Train_GPTSoVITS_FP16Run)
        self.Label_Train_GPTSoVITS_FP16Run.setObjectName(u"Label_Train_GPTSoVITS_FP16Run")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_FP16Run.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_FP16Run.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_FP16Run.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_91.addWidget(self.Label_Train_GPTSoVITS_FP16Run, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_FP16Run = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_91.addItem(self.HorizontalSpacer_Train_GPTSoVITS_FP16Run, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_FP16Run_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_FP16Run)
        self.Button_Train_GPTSoVITS_FP16Run_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_FP16Run_MoreActions")
        self.Button_Train_GPTSoVITS_FP16Run_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_FP16Run_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_FP16Run_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_91.addWidget(self.Button_Train_GPTSoVITS_FP16Run_MoreActions, 0, 2, 1, 1)

        self.CheckBox_Train_GPTSoVITS_FP16Run = QCheckBox(self.Frame_Train_GPTSoVITS_FP16Run)
        self.CheckBox_Train_GPTSoVITS_FP16Run.setObjectName(u"CheckBox_Train_GPTSoVITS_FP16Run")
        self.CheckBox_Train_GPTSoVITS_FP16Run.setMinimumSize(QSize(0, 27))
        self.CheckBox_Train_GPTSoVITS_FP16Run.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_91.addWidget(self.CheckBox_Train_GPTSoVITS_FP16Run, 1, 0, 1, 3)


        self.verticalLayout_57.addWidget(self.Frame_Train_GPTSoVITS_FP16Run)

        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.addItem(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_122.addWidget(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings)


        self.verticalLayout_52.addWidget(self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams)

        self.GroupBox_Train_GPTSoVITS_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS)
        self.GroupBox_Train_GPTSoVITS_OutputParams.setObjectName(u"GroupBox_Train_GPTSoVITS_OutputParams")
        self.GroupBox_Train_GPTSoVITS_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_77 = QVBoxLayout(self.GroupBox_Train_GPTSoVITS_OutputParams)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 12, 0, 12)
        self.Frame_Train_GPTSoVITS_OutputParams_BasicSettings = QFrame(self.GroupBox_Train_GPTSoVITS_OutputParams)
        self.Frame_Train_GPTSoVITS_OutputParams_BasicSettings.setObjectName(u"Frame_Train_GPTSoVITS_OutputParams_BasicSettings")
        self.verticalLayout_58 = QVBoxLayout(self.Frame_Train_GPTSoVITS_OutputParams_BasicSettings)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_GPTSoVITS_OutputDirName = QFrame(self.Frame_Train_GPTSoVITS_OutputParams_BasicSettings)
        self.Frame_Train_GPTSoVITS_OutputDirName.setObjectName(u"Frame_Train_GPTSoVITS_OutputDirName")
        self.Frame_Train_GPTSoVITS_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_98 = QGridLayout(self.Frame_Train_GPTSoVITS_OutputDirName)
        self.gridLayout_98.setSpacing(12)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.gridLayout_98.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_OutputDirName = QLabel(self.Frame_Train_GPTSoVITS_OutputDirName)
        self.Label_Train_GPTSoVITS_OutputDirName.setObjectName(u"Label_Train_GPTSoVITS_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_98.addWidget(self.Label_Train_GPTSoVITS_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_OutputDirName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_98.addItem(self.HorizontalSpacer_Train_GPTSoVITS_OutputDirName, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_OutputDirName_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_OutputDirName)
        self.Button_Train_GPTSoVITS_OutputDirName_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_OutputDirName_MoreActions")
        self.Button_Train_GPTSoVITS_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_98.addWidget(self.Button_Train_GPTSoVITS_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_OutputDirName = LineEditBase(self.Frame_Train_GPTSoVITS_OutputDirName)
        self.LineEdit_Train_GPTSoVITS_OutputDirName.setObjectName(u"LineEdit_Train_GPTSoVITS_OutputDirName")
        self.LineEdit_Train_GPTSoVITS_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_98.addWidget(self.LineEdit_Train_GPTSoVITS_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_58.addWidget(self.Frame_Train_GPTSoVITS_OutputDirName)


        self.verticalLayout_77.addWidget(self.Frame_Train_GPTSoVITS_OutputParams_BasicSettings)

        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings = ToolBoxBase(self.GroupBox_Train_GPTSoVITS_OutputParams)
        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.setObjectName(u"ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings")
        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content")
        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 538, 105))
        self.verticalLayout_60 = QVBoxLayout(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_GPTSoVITS_LogDir = QFrame(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_Train_GPTSoVITS_LogDir.setObjectName(u"Frame_Train_GPTSoVITS_LogDir")
        self.Frame_Train_GPTSoVITS_LogDir.setMinimumSize(QSize(0, 105))
        self.Frame_Train_GPTSoVITS_LogDir.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_110 = QGridLayout(self.Frame_Train_GPTSoVITS_LogDir)
        self.gridLayout_110.setSpacing(12)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.gridLayout_110.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_LogDir = QLabel(self.Frame_Train_GPTSoVITS_LogDir)
        self.Label_Train_GPTSoVITS_LogDir.setObjectName(u"Label_Train_GPTSoVITS_LogDir")
        sizePolicy5.setHeightForWidth(self.Label_Train_GPTSoVITS_LogDir.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_LogDir.setSizePolicy(sizePolicy5)
        self.Label_Train_GPTSoVITS_LogDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_110.addWidget(self.Label_Train_GPTSoVITS_LogDir, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_GPTSoVITS_LogDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_110.addItem(self.HorizontalSpacer_Train_GPTSoVITS_LogDir, 0, 1, 1, 1)

        self.Button_Train_GPTSoVITS_LogDir_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_LogDir)
        self.Button_Train_GPTSoVITS_LogDir_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_LogDir_MoreActions")
        self.Button_Train_GPTSoVITS_LogDir_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_LogDir_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_GPTSoVITS_LogDir_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_110.addWidget(self.Button_Train_GPTSoVITS_LogDir_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_GPTSoVITS_LogDir = LineEditBase(self.Frame_Train_GPTSoVITS_LogDir)
        self.LineEdit_Train_GPTSoVITS_LogDir.setObjectName(u"LineEdit_Train_GPTSoVITS_LogDir")
        self.LineEdit_Train_GPTSoVITS_LogDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_110.addWidget(self.LineEdit_Train_GPTSoVITS_LogDir, 1, 0, 1, 3)


        self.verticalLayout_60.addWidget(self.Frame_Train_GPTSoVITS_LogDir)

        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.addItem(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_77.addWidget(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings)


        self.verticalLayout_52.addWidget(self.GroupBox_Train_GPTSoVITS_OutputParams)

        self.VerticalSpacer_Train_GPTSoVITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_52.addItem(self.VerticalSpacer_Train_GPTSoVITS)

        self.ScrollArea_Middle_Train_GPTSoVITS.setWidget(self.ScrollArea_Middle_WidgetContents_Train_GPTSoVITS)

        self.gridLayout_85.addWidget(self.ScrollArea_Middle_Train_GPTSoVITS, 0, 1, 1, 1)

        self.Widget_Right_Train_GPTSoVITS = QWidget(self.Subpage_Train_GPTSoVITS)
        self.Widget_Right_Train_GPTSoVITS.setObjectName(u"Widget_Right_Train_GPTSoVITS")
        self.Widget_Right_Train_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_14 = QGridLayout(self.Widget_Right_Train_GPTSoVITS)
        self.gridLayout_14.setSpacing(12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Train_GPTSoVITS = QTextBrowser(self.Widget_Right_Train_GPTSoVITS)
        self.TextBrowser_Params_Train_GPTSoVITS.setObjectName(u"TextBrowser_Params_Train_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Train_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Train_GPTSoVITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Train_GPTSoVITS.setStyleSheet(u"QTextBrowser {\n"
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
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_14.addWidget(self.TextBrowser_Params_Train_GPTSoVITS, 0, 0, 1, 3)

        self.Button_ResetSettings_Train_GPTSoVITS = QPushButton(self.Widget_Right_Train_GPTSoVITS)
        self.Button_ResetSettings_Train_GPTSoVITS.setObjectName(u"Button_ResetSettings_Train_GPTSoVITS")
        self.Button_ResetSettings_Train_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_14.addWidget(self.Button_ResetSettings_Train_GPTSoVITS, 1, 0, 1, 1)

        self.Button_ImportSettings_Train_GPTSoVITS = QPushButton(self.Widget_Right_Train_GPTSoVITS)
        self.Button_ImportSettings_Train_GPTSoVITS.setObjectName(u"Button_ImportSettings_Train_GPTSoVITS")
        self.Button_ImportSettings_Train_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_14.addWidget(self.Button_ImportSettings_Train_GPTSoVITS, 1, 1, 1, 1)

        self.Button_ExportSettings_Train_GPTSoVITS = QPushButton(self.Widget_Right_Train_GPTSoVITS)
        self.Button_ExportSettings_Train_GPTSoVITS.setObjectName(u"Button_ExportSettings_Train_GPTSoVITS")
        self.Button_ExportSettings_Train_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_14.addWidget(self.Button_ExportSettings_Train_GPTSoVITS, 1, 2, 1, 1)

        self.Button_RunTensorboard_Train_GPTSoVITS = QPushButton(self.Widget_Right_Train_GPTSoVITS)
        self.Button_RunTensorboard_Train_GPTSoVITS.setObjectName(u"Button_RunTensorboard_Train_GPTSoVITS")
        self.Button_RunTensorboard_Train_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_14.addWidget(self.Button_RunTensorboard_Train_GPTSoVITS, 2, 0, 1, 3)

        self.Button_CheckOutput_Train_GPTSoVITS = QPushButton(self.Widget_Right_Train_GPTSoVITS)
        self.Button_CheckOutput_Train_GPTSoVITS.setObjectName(u"Button_CheckOutput_Train_GPTSoVITS")
        self.Button_CheckOutput_Train_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_14.addWidget(self.Button_CheckOutput_Train_GPTSoVITS, 3, 0, 1, 3)


        self.gridLayout_85.addWidget(self.Widget_Right_Train_GPTSoVITS, 0, 2, 1, 1)

        self.ProgressBar_Train_GPTSoVITS = QProgressBar(self.Subpage_Train_GPTSoVITS)
        self.ProgressBar_Train_GPTSoVITS.setObjectName(u"ProgressBar_Train_GPTSoVITS")
        self.ProgressBar_Train_GPTSoVITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Train_GPTSoVITS.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	background-color: transparent;\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgba(123, 123, 123, 123));\n"
"}")
        self.ProgressBar_Train_GPTSoVITS.setValue(0)
        self.ProgressBar_Train_GPTSoVITS.setTextVisible(False)
        self.horizontalLayout_41 = QHBoxLayout(self.ProgressBar_Train_GPTSoVITS)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Train_GPTSoVITS = QStackedWidget(self.ProgressBar_Train_GPTSoVITS)
        self.StackedWidget_Train_GPTSoVITS.setObjectName(u"StackedWidget_Train_GPTSoVITS")
        self.StackedWidget_Train_GPTSoVITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_Train_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
"}")
        self.Page_Train_GPTSoVITS_Execute = QWidget()
        self.Page_Train_GPTSoVITS_Execute.setObjectName(u"Page_Train_GPTSoVITS_Execute")
        self.verticalLayout_96 = QVBoxLayout(self.Page_Train_GPTSoVITS_Execute)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.Button_Train_GPTSoVITS_Execute = QPushButton(self.Page_Train_GPTSoVITS_Execute)
        self.Button_Train_GPTSoVITS_Execute.setObjectName(u"Button_Train_GPTSoVITS_Execute")
        sizePolicy3.setHeightForWidth(self.Button_Train_GPTSoVITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Train_GPTSoVITS_Execute.setSizePolicy(sizePolicy3)
        self.Button_Train_GPTSoVITS_Execute.setMinimumSize(QSize(0, 30))
        self.Button_Train_GPTSoVITS_Execute.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"}")

        self.verticalLayout_96.addWidget(self.Button_Train_GPTSoVITS_Execute)

        self.StackedWidget_Train_GPTSoVITS.addWidget(self.Page_Train_GPTSoVITS_Execute)
        self.Page_Train_GPTSoVITS_Terminate = QWidget()
        self.Page_Train_GPTSoVITS_Terminate.setObjectName(u"Page_Train_GPTSoVITS_Terminate")
        self.verticalLayout_97 = QVBoxLayout(self.Page_Train_GPTSoVITS_Terminate)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.Button_Train_GPTSoVITS_Terminate = QPushButton(self.Page_Train_GPTSoVITS_Terminate)
        self.Button_Train_GPTSoVITS_Terminate.setObjectName(u"Button_Train_GPTSoVITS_Terminate")
        sizePolicy3.setHeightForWidth(self.Button_Train_GPTSoVITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Train_GPTSoVITS_Terminate.setSizePolicy(sizePolicy3)
        self.Button_Train_GPTSoVITS_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_Train_GPTSoVITS_Terminate.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"}")

        self.verticalLayout_97.addWidget(self.Button_Train_GPTSoVITS_Terminate)

        self.StackedWidget_Train_GPTSoVITS.addWidget(self.Page_Train_GPTSoVITS_Terminate)

        self.horizontalLayout_41.addWidget(self.StackedWidget_Train_GPTSoVITS)


        self.gridLayout_85.addWidget(self.ProgressBar_Train_GPTSoVITS, 1, 0, 1, 3)

        self.gridLayout_85.setColumnStretch(0, 3)
        self.gridLayout_85.setColumnStretch(1, 10)
        self.gridLayout_85.setColumnStretch(2, 7)
        self.StackedWidget_Pages_Train.addWidget(self.Subpage_Train_GPTSoVITS)
        self.Subpage_Train_VITS = QWidget()
        self.Subpage_Train_VITS.setObjectName(u"Subpage_Train_VITS")
        self.gridLayout_22 = QGridLayout(self.Subpage_Train_VITS)
        self.gridLayout_22.setSpacing(12)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.Widget_Right_Train_VITS = QWidget(self.Subpage_Train_VITS)
        self.Widget_Right_Train_VITS.setObjectName(u"Widget_Right_Train_VITS")
        self.Widget_Right_Train_VITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout = QGridLayout(self.Widget_Right_Train_VITS)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Train_VITS = QTextBrowser(self.Widget_Right_Train_VITS)
        self.TextBrowser_Params_Train_VITS.setObjectName(u"TextBrowser_Params_Train_VITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Train_VITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Train_VITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Train_VITS.setStyleSheet(u"QTextBrowser {\n"
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
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout.addWidget(self.TextBrowser_Params_Train_VITS, 0, 0, 1, 3)

        self.Button_ResetSettings_Train_VITS = QPushButton(self.Widget_Right_Train_VITS)
        self.Button_ResetSettings_Train_VITS.setObjectName(u"Button_ResetSettings_Train_VITS")
        self.Button_ResetSettings_Train_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout.addWidget(self.Button_ResetSettings_Train_VITS, 1, 0, 1, 1)

        self.Button_ImportSettings_Train_VITS = QPushButton(self.Widget_Right_Train_VITS)
        self.Button_ImportSettings_Train_VITS.setObjectName(u"Button_ImportSettings_Train_VITS")
        self.Button_ImportSettings_Train_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout.addWidget(self.Button_ImportSettings_Train_VITS, 1, 1, 1, 1)

        self.Button_ExportSettings_Train_VITS = QPushButton(self.Widget_Right_Train_VITS)
        self.Button_ExportSettings_Train_VITS.setObjectName(u"Button_ExportSettings_Train_VITS")
        self.Button_ExportSettings_Train_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout.addWidget(self.Button_ExportSettings_Train_VITS, 1, 2, 1, 1)

        self.Button_RunTensorboard_Train_VITS = QPushButton(self.Widget_Right_Train_VITS)
        self.Button_RunTensorboard_Train_VITS.setObjectName(u"Button_RunTensorboard_Train_VITS")
        self.Button_RunTensorboard_Train_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout.addWidget(self.Button_RunTensorboard_Train_VITS, 2, 0, 1, 3)

        self.Button_CheckOutput_Train_VITS = QPushButton(self.Widget_Right_Train_VITS)
        self.Button_CheckOutput_Train_VITS.setObjectName(u"Button_CheckOutput_Train_VITS")
        self.Button_CheckOutput_Train_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout.addWidget(self.Button_CheckOutput_Train_VITS, 3, 0, 1, 3)


        self.gridLayout_22.addWidget(self.Widget_Right_Train_VITS, 0, 2, 1, 1)

        self.Widget_Left_Train_VITS = QWidget(self.Subpage_Train_VITS)
        self.Widget_Left_Train_VITS.setObjectName(u"Widget_Left_Train_VITS")
        self.Widget_Left_Train_VITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_Train_VITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.Widget_Left_Train_VITS)
        self.verticalLayout_10.setSpacing(12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Train_VITS = QTreeWidget(self.Widget_Left_Train_VITS)
        __qtreewidgetitem6 = QTreeWidgetItem(self.TreeWidget_Catalogue_Train_VITS)
        QTreeWidgetItem(__qtreewidgetitem6)
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
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal "
                        "{\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"}")

        self.verticalLayout_10.addWidget(self.TreeWidget_Catalogue_Train_VITS)


        self.gridLayout_22.addWidget(self.Widget_Left_Train_VITS, 0, 0, 1, 1)

        self.ProgressBar_Train_VITS = QProgressBar(self.Subpage_Train_VITS)
        self.ProgressBar_Train_VITS.setObjectName(u"ProgressBar_Train_VITS")
        self.ProgressBar_Train_VITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Train_VITS.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	background-color: transparent;\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgba(123, 123, 123, 123));\n"
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
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
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
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
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
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"}")

        self.verticalLayout_95.addWidget(self.Button_Train_VITS_Terminate)

        self.StackedWidget_Train_VITS.addWidget(self.Page_Train_VITS_Terminate)

        self.horizontalLayout_39.addWidget(self.StackedWidget_Train_VITS)


        self.gridLayout_22.addWidget(self.ProgressBar_Train_VITS, 1, 0, 1, 3)

        self.ScrollArea_Middle_Train_VITS = ScrollAreaBase(self.Subpage_Train_VITS)
        self.ScrollArea_Middle_Train_VITS.setObjectName(u"ScrollArea_Middle_Train_VITS")
        self.ScrollArea_Middle_Train_VITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_Train_VITS.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Train_VITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_Train_VITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_Train_VITS.setObjectName(u"ScrollArea_Middle_WidgetContents_Train_VITS")
        self.ScrollArea_Middle_WidgetContents_Train_VITS.setGeometry(QRect(0, 0, 581, 1529))
        self.verticalLayout_28 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.verticalLayout_28.setSpacing(12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_Train_VITS_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.GroupBox_Train_VITS_InputParams.setObjectName(u"GroupBox_Train_VITS_InputParams")
        self.GroupBox_Train_VITS_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_57.addWidget(self.Label_Train_VITS_FileListPathTraining, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_FileListPathTraining = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_57.addItem(self.HorizontalSpacer_Train_VITS_FileListPathTraining, 0, 1, 1, 1)

        self.Button_Train_VITS_FileListPathTraining_MoreActions = MenuButton(self.Frame_Train_VITS_FileListPathTraining)
        self.Button_Train_VITS_FileListPathTraining_MoreActions.setObjectName(u"Button_Train_VITS_FileListPathTraining_MoreActions")
        self.Button_Train_VITS_FileListPathTraining_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathTraining_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathTraining_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_57.addWidget(self.Button_Train_VITS_FileListPathTraining_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_FileListPathTraining = LineEditBase(self.Frame_Train_VITS_FileListPathTraining)
        self.LineEdit_Train_VITS_FileListPathTraining.setObjectName(u"LineEdit_Train_VITS_FileListPathTraining")
        self.LineEdit_Train_VITS_FileListPathTraining.setMinimumSize(QSize(0, 27))

        self.gridLayout_57.addWidget(self.LineEdit_Train_VITS_FileListPathTraining, 1, 0, 1, 3)


        self.verticalLayout_18.addWidget(self.Frame_Train_VITS_FileListPathTraining)

        self.Frame_Train_VITS_FileListPathValidation = QFrame(self.Frame_Train_VITS_InputParams_BasicSettings)
        self.Frame_Train_VITS_FileListPathValidation.setObjectName(u"Frame_Train_VITS_FileListPathValidation")
        self.Frame_Train_VITS_FileListPathValidation.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_FileListPathValidation.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_58.addWidget(self.Label_Train_VITS_FileListPathValidation, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_FileListPathValidation = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_58.addItem(self.HorizontalSpacer_Train_VITS_FileListPathValidation, 0, 1, 1, 1)

        self.Button_Train_VITS_FileListPathValidation_MoreActions = MenuButton(self.Frame_Train_VITS_FileListPathValidation)
        self.Button_Train_VITS_FileListPathValidation_MoreActions.setObjectName(u"Button_Train_VITS_FileListPathValidation_MoreActions")
        self.Button_Train_VITS_FileListPathValidation_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathValidation_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_FileListPathValidation_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_58.addWidget(self.Button_Train_VITS_FileListPathValidation_MoreActions, 0, 2, 1, 1)

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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_59.addWidget(self.Label_Train_VITS_Epochs, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_Epochs = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_59.addItem(self.HorizontalSpacer_Train_VITS_Epochs, 0, 1, 1, 1)

        self.Button_Train_VITS_Epochs_MoreActions = MenuButton(self.Frame_Train_VITS_Epochs)
        self.Button_Train_VITS_Epochs_MoreActions.setObjectName(u"Button_Train_VITS_Epochs_MoreActions")
        self.Button_Train_VITS_Epochs_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_Epochs_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_Epochs_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_59.addWidget(self.Button_Train_VITS_Epochs_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_Epochs = SpinBoxBase(self.Frame_Train_VITS_Epochs)
        self.SpinBox_Train_VITS_Epochs.setObjectName(u"SpinBox_Train_VITS_Epochs")
        self.SpinBox_Train_VITS_Epochs.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_Epochs.setMinimum(-999999)
        self.SpinBox_Train_VITS_Epochs.setMaximum(999999)

        self.gridLayout_59.addWidget(self.SpinBox_Train_VITS_Epochs, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_Epochs)

        self.Frame_Train_VITS_BatchSize = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_BatchSize.setObjectName(u"Frame_Train_VITS_BatchSize")
        self.Frame_Train_VITS_BatchSize.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_BatchSize.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_60.addWidget(self.Label_Train_VITS_BatchSize, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_BatchSize = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.HorizontalSpacer_Train_VITS_BatchSize, 0, 1, 1, 1)

        self.Button_Train_VITS_BatchSize_MoreActions = MenuButton(self.Frame_Train_VITS_BatchSize)
        self.Button_Train_VITS_BatchSize_MoreActions.setObjectName(u"Button_Train_VITS_BatchSize_MoreActions")
        self.Button_Train_VITS_BatchSize_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_BatchSize_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_BatchSize_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_60.addWidget(self.Button_Train_VITS_BatchSize_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_BatchSize = SpinBoxBase(self.Frame_Train_VITS_BatchSize)
        self.SpinBox_Train_VITS_BatchSize.setObjectName(u"SpinBox_Train_VITS_BatchSize")
        self.SpinBox_Train_VITS_BatchSize.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_BatchSize.setMinimum(-999999)
        self.SpinBox_Train_VITS_BatchSize.setMaximum(999999)

        self.gridLayout_60.addWidget(self.SpinBox_Train_VITS_BatchSize, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_BatchSize)

        self.Frame_Train_VITS_UsePretrainedModels = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_UsePretrainedModels.setObjectName(u"Frame_Train_VITS_UsePretrainedModels")
        self.Frame_Train_VITS_UsePretrainedModels.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_UsePretrainedModels.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_61.addWidget(self.Label_Train_VITS_UsePretrainedModels, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_UsePretrainedModels = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_61.addItem(self.HorizontalSpacer_Train_VITS_UsePretrainedModels, 0, 1, 1, 1)

        self.Button_Train_VITS_UsePretrainedModels_MoreActions = MenuButton(self.Frame_Train_VITS_UsePretrainedModels)
        self.Button_Train_VITS_UsePretrainedModels_MoreActions.setObjectName(u"Button_Train_VITS_UsePretrainedModels_MoreActions")
        self.Button_Train_VITS_UsePretrainedModels_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_UsePretrainedModels_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_UsePretrainedModels_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_61.addWidget(self.Button_Train_VITS_UsePretrainedModels_MoreActions, 0, 2, 1, 1)

        self.CheckBox_Train_VITS_UsePretrainedModels = QCheckBox(self.Frame_Train_VITS_UsePretrainedModels)
        self.CheckBox_Train_VITS_UsePretrainedModels.setObjectName(u"CheckBox_Train_VITS_UsePretrainedModels")
        self.CheckBox_Train_VITS_UsePretrainedModels.setMinimumSize(QSize(0, 27))
        self.CheckBox_Train_VITS_UsePretrainedModels.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_61.addWidget(self.CheckBox_Train_VITS_UsePretrainedModels, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_UsePretrainedModels)

        self.Frame_Train_VITS_ModelPathPretrainedG = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_ModelPathPretrainedG.setObjectName(u"Frame_Train_VITS_ModelPathPretrainedG")
        self.Frame_Train_VITS_ModelPathPretrainedG.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_ModelPathPretrainedG.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_65.addWidget(self.Label_Train_VITS_ModelPathPretrainedG, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_ModelPathPretrainedG = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_65.addItem(self.HorizontalSpacer_Train_VITS_ModelPathPretrainedG, 0, 1, 1, 1)

        self.Button_Train_VITS_ModelPathPretrainedG_MoreActions = MenuButton(self.Frame_Train_VITS_ModelPathPretrainedG)
        self.Button_Train_VITS_ModelPathPretrainedG_MoreActions.setObjectName(u"Button_Train_VITS_ModelPathPretrainedG_MoreActions")
        self.Button_Train_VITS_ModelPathPretrainedG_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedG_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedG_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_65.addWidget(self.Button_Train_VITS_ModelPathPretrainedG_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_ModelPathPretrainedG = LineEditBase(self.Frame_Train_VITS_ModelPathPretrainedG)
        self.LineEdit_Train_VITS_ModelPathPretrainedG.setObjectName(u"LineEdit_Train_VITS_ModelPathPretrainedG")
        self.LineEdit_Train_VITS_ModelPathPretrainedG.setMinimumSize(QSize(0, 27))

        self.gridLayout_65.addWidget(self.LineEdit_Train_VITS_ModelPathPretrainedG, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_ModelPathPretrainedG)

        self.Frame_Train_VITS_ModelPathPretrainedD = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_ModelPathPretrainedD.setObjectName(u"Frame_Train_VITS_ModelPathPretrainedD")
        self.Frame_Train_VITS_ModelPathPretrainedD.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_ModelPathPretrainedD.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_66.addWidget(self.Label_Train_VITS_ModelPathPretrainedD, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_ModelPathPretrainedD = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_66.addItem(self.HorizontalSpacer_Train_VITS_ModelPathPretrainedD, 0, 1, 1, 1)

        self.Button_Train_VITS_ModelPathPretrainedD_MoreActions = MenuButton(self.Frame_Train_VITS_ModelPathPretrainedD)
        self.Button_Train_VITS_ModelPathPretrainedD_MoreActions.setObjectName(u"Button_Train_VITS_ModelPathPretrainedD_MoreActions")
        self.Button_Train_VITS_ModelPathPretrainedD_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedD_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_ModelPathPretrainedD_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_66.addWidget(self.Button_Train_VITS_ModelPathPretrainedD_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_ModelPathPretrainedD = LineEditBase(self.Frame_Train_VITS_ModelPathPretrainedD)
        self.LineEdit_Train_VITS_ModelPathPretrainedD.setObjectName(u"LineEdit_Train_VITS_ModelPathPretrainedD")
        self.LineEdit_Train_VITS_ModelPathPretrainedD.setMinimumSize(QSize(0, 27))

        self.gridLayout_66.addWidget(self.LineEdit_Train_VITS_ModelPathPretrainedD, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_ModelPathPretrainedD)

        self.Frame_Train_VITS_KeepOriginalSpeakers = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_KeepOriginalSpeakers.setObjectName(u"Frame_Train_VITS_KeepOriginalSpeakers")
        self.Frame_Train_VITS_KeepOriginalSpeakers.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_KeepOriginalSpeakers.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_67.addWidget(self.Label_Train_VITS_KeepOriginalSpeakers, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_KeepOriginalSpeakers = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_67.addItem(self.HorizontalSpacer_Train_VITS_KeepOriginalSpeakers, 0, 1, 1, 1)

        self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions = MenuButton(self.Frame_Train_VITS_KeepOriginalSpeakers)
        self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions.setObjectName(u"Button_Train_VITS_KeepOriginalSpeakers_MoreActions")
        self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_67.addWidget(self.Button_Train_VITS_KeepOriginalSpeakers_MoreActions, 0, 2, 1, 1)

        self.CheckBox_Train_VITS_KeepOriginalSpeakers = QCheckBox(self.Frame_Train_VITS_KeepOriginalSpeakers)
        self.CheckBox_Train_VITS_KeepOriginalSpeakers.setObjectName(u"CheckBox_Train_VITS_KeepOriginalSpeakers")
        self.CheckBox_Train_VITS_KeepOriginalSpeakers.setMinimumSize(QSize(0, 27))
        self.CheckBox_Train_VITS_KeepOriginalSpeakers.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_67.addWidget(self.CheckBox_Train_VITS_KeepOriginalSpeakers, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_KeepOriginalSpeakers)

        self.Frame_Train_VITS_ConfigPathLoad = QFrame(self.Frame_Train_VITS_VITSParams_BasicSettings)
        self.Frame_Train_VITS_ConfigPathLoad.setObjectName(u"Frame_Train_VITS_ConfigPathLoad")
        self.Frame_Train_VITS_ConfigPathLoad.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_ConfigPathLoad.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_77.addWidget(self.Label_Train_VITS_ConfigPathLoad, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_ConfigPathLoad = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_77.addItem(self.HorizontalSpacer_Train_VITS_ConfigPathLoad, 0, 1, 1, 1)

        self.Button_Train_VITS_ConfigPathLoad_MoreActions = MenuButton(self.Frame_Train_VITS_ConfigPathLoad)
        self.Button_Train_VITS_ConfigPathLoad_MoreActions.setObjectName(u"Button_Train_VITS_ConfigPathLoad_MoreActions")
        self.Button_Train_VITS_ConfigPathLoad_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_ConfigPathLoad_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_ConfigPathLoad_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_77.addWidget(self.Button_Train_VITS_ConfigPathLoad_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_ConfigPathLoad = LineEditBase(self.Frame_Train_VITS_ConfigPathLoad)
        self.LineEdit_Train_VITS_ConfigPathLoad.setObjectName(u"LineEdit_Train_VITS_ConfigPathLoad")
        self.LineEdit_Train_VITS_ConfigPathLoad.setMinimumSize(QSize(0, 27))

        self.gridLayout_77.addWidget(self.LineEdit_Train_VITS_ConfigPathLoad, 1, 0, 1, 3)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_ConfigPathLoad)


        self.verticalLayout_114.addWidget(self.Frame_Train_VITS_VITSParams_BasicSettings)

        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings = ToolBoxBase(self.GroupBox_Train_VITS_VITSParams)
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.setObjectName(u"ToolBox_Train_VITS_VITSParams_AdvanceSettings")
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.setFrameShape(QFrame.StyledPanel)
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.setFrameShadow(QFrame.Raised)
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content")
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 210))
        self.verticalLayout_35 = QVBoxLayout(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_NumWorkers = QFrame(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_Train_VITS_NumWorkers.setObjectName(u"Frame_Train_VITS_NumWorkers")
        self.Frame_Train_VITS_NumWorkers.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_NumWorkers.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_63.addWidget(self.Label_Train_VITS_NumWorkers, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_NumWorkers = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_63.addItem(self.HorizontalSpacer_Train_VITS_NumWorkers, 0, 1, 1, 1)

        self.Button_Train_VITS_NumWorkers_MoreActions = MenuButton(self.Frame_Train_VITS_NumWorkers)
        self.Button_Train_VITS_NumWorkers_MoreActions.setObjectName(u"Button_Train_VITS_NumWorkers_MoreActions")
        self.Button_Train_VITS_NumWorkers_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_NumWorkers_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_NumWorkers_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_63.addWidget(self.Button_Train_VITS_NumWorkers_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_NumWorkers = SpinBoxBase(self.Frame_Train_VITS_NumWorkers)
        self.SpinBox_Train_VITS_NumWorkers.setObjectName(u"SpinBox_Train_VITS_NumWorkers")
        self.SpinBox_Train_VITS_NumWorkers.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_NumWorkers.setMinimum(-999999)
        self.SpinBox_Train_VITS_NumWorkers.setMaximum(999999)

        self.gridLayout_63.addWidget(self.SpinBox_Train_VITS_NumWorkers, 1, 0, 1, 3)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_NumWorkers)

        self.Frame_Train_VITS_FP16Run = QFrame(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_Train_VITS_FP16Run.setObjectName(u"Frame_Train_VITS_FP16Run")
        self.Frame_Train_VITS_FP16Run.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_FP16Run.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_64.addWidget(self.Label_Train_VITS_FP16Run, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_FP16Run = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_64.addItem(self.HorizontalSpacer_Train_VITS_FP16Run, 0, 1, 1, 1)

        self.Button_Train_VITS_FP16Run_MoreActions = MenuButton(self.Frame_Train_VITS_FP16Run)
        self.Button_Train_VITS_FP16Run_MoreActions.setObjectName(u"Button_Train_VITS_FP16Run_MoreActions")
        self.Button_Train_VITS_FP16Run_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_FP16Run_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_FP16Run_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_64.addWidget(self.Button_Train_VITS_FP16Run_MoreActions, 0, 2, 1, 1)

        self.CheckBox_Train_VITS_FP16Run = QCheckBox(self.Frame_Train_VITS_FP16Run)
        self.CheckBox_Train_VITS_FP16Run.setObjectName(u"CheckBox_Train_VITS_FP16Run")
        self.CheckBox_Train_VITS_FP16Run.setMinimumSize(QSize(0, 27))
        self.CheckBox_Train_VITS_FP16Run.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_64.addWidget(self.CheckBox_Train_VITS_FP16Run, 1, 0, 1, 3)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_FP16Run)

        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.addItem(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_114.addWidget(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings)


        self.verticalLayout_28.addWidget(self.GroupBox_Train_VITS_VITSParams)

        self.GroupBox_Train_VITS_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.GroupBox_Train_VITS_OutputParams.setObjectName(u"GroupBox_Train_VITS_OutputParams")
        self.GroupBox_Train_VITS_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_80 = QVBoxLayout(self.GroupBox_Train_VITS_OutputParams)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_62.addWidget(self.Label_Train_VITS_EvalInterval, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_EvalInterval = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_62.addItem(self.HorizontalSpacer_Train_VITS_EvalInterval, 0, 1, 1, 1)

        self.Button_Train_VITS_EvalInterval_MoreActions = MenuButton(self.Frame_Train_VITS_EvalInterval)
        self.Button_Train_VITS_EvalInterval_MoreActions.setObjectName(u"Button_Train_VITS_EvalInterval_MoreActions")
        self.Button_Train_VITS_EvalInterval_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_EvalInterval_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_EvalInterval_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_62.addWidget(self.Button_Train_VITS_EvalInterval_MoreActions, 0, 2, 1, 1)

        self.SpinBox_Train_VITS_EvalInterval = SpinBoxBase(self.Frame_Train_VITS_EvalInterval)
        self.SpinBox_Train_VITS_EvalInterval.setObjectName(u"SpinBox_Train_VITS_EvalInterval")
        self.SpinBox_Train_VITS_EvalInterval.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_EvalInterval.setMinimum(-999999)
        self.SpinBox_Train_VITS_EvalInterval.setMaximum(999999)

        self.gridLayout_62.addWidget(self.SpinBox_Train_VITS_EvalInterval, 1, 0, 1, 3)


        self.verticalLayout_26.addWidget(self.Frame_Train_VITS_EvalInterval)

        self.Frame_Train_VITS_OutputDirName = QFrame(self.Frame_Train_VITS_OutputParams_BasicSettings)
        self.Frame_Train_VITS_OutputDirName.setObjectName(u"Frame_Train_VITS_OutputDirName")
        self.Frame_Train_VITS_OutputDirName.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_OutputDirName.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_68 = QGridLayout(self.Frame_Train_VITS_OutputDirName)
        self.gridLayout_68.setSpacing(12)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.gridLayout_68.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_OutputDirName = QLabel(self.Frame_Train_VITS_OutputDirName)
        self.Label_Train_VITS_OutputDirName.setObjectName(u"Label_Train_VITS_OutputDirName")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_OutputDirName.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_OutputDirName.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_OutputDirName.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_68.addWidget(self.Label_Train_VITS_OutputDirName, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_OutputDirName = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_68.addItem(self.HorizontalSpacer_Train_VITS_OutputDirName, 0, 1, 1, 1)

        self.Button_Train_VITS_OutputDirName_MoreActions = MenuButton(self.Frame_Train_VITS_OutputDirName)
        self.Button_Train_VITS_OutputDirName_MoreActions.setObjectName(u"Button_Train_VITS_OutputDirName_MoreActions")
        self.Button_Train_VITS_OutputDirName_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_OutputDirName_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_OutputDirName_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_68.addWidget(self.Button_Train_VITS_OutputDirName_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_OutputDirName = LineEditBase(self.Frame_Train_VITS_OutputDirName)
        self.LineEdit_Train_VITS_OutputDirName.setObjectName(u"LineEdit_Train_VITS_OutputDirName")
        self.LineEdit_Train_VITS_OutputDirName.setMinimumSize(QSize(0, 27))

        self.gridLayout_68.addWidget(self.LineEdit_Train_VITS_OutputDirName, 1, 0, 1, 3)


        self.verticalLayout_26.addWidget(self.Frame_Train_VITS_OutputDirName)


        self.verticalLayout_80.addWidget(self.Frame_Train_VITS_OutputParams_BasicSettings)

        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings = ToolBoxBase(self.GroupBox_Train_VITS_OutputParams)
        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings.setObjectName(u"ToolBox_Train_VITS_OutputParams_AdvanceSettings")
        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content")
        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 105))
        self.verticalLayout_79 = QVBoxLayout(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_LogDir = QFrame(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content)
        self.Frame_Train_VITS_LogDir.setObjectName(u"Frame_Train_VITS_LogDir")
        self.Frame_Train_VITS_LogDir.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_LogDir.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_111 = QGridLayout(self.Frame_Train_VITS_LogDir)
        self.gridLayout_111.setSpacing(12)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.gridLayout_111.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_LogDir = QLabel(self.Frame_Train_VITS_LogDir)
        self.Label_Train_VITS_LogDir.setObjectName(u"Label_Train_VITS_LogDir")
        sizePolicy5.setHeightForWidth(self.Label_Train_VITS_LogDir.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_LogDir.setSizePolicy(sizePolicy5)
        self.Label_Train_VITS_LogDir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_111.addWidget(self.Label_Train_VITS_LogDir, 0, 0, 1, 1)

        self.HorizontalSpacer_Train_VITS_LogDir = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_111.addItem(self.HorizontalSpacer_Train_VITS_LogDir, 0, 1, 1, 1)

        self.Button_Train_VITS_LogDir_MoreActions = MenuButton(self.Frame_Train_VITS_LogDir)
        self.Button_Train_VITS_LogDir_MoreActions.setObjectName(u"Button_Train_VITS_LogDir_MoreActions")
        self.Button_Train_VITS_LogDir_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_LogDir_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_Train_VITS_LogDir_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_111.addWidget(self.Button_Train_VITS_LogDir_MoreActions, 0, 2, 1, 1)

        self.LineEdit_Train_VITS_LogDir = LineEditBase(self.Frame_Train_VITS_LogDir)
        self.LineEdit_Train_VITS_LogDir.setObjectName(u"LineEdit_Train_VITS_LogDir")
        self.LineEdit_Train_VITS_LogDir.setMinimumSize(QSize(0, 27))

        self.gridLayout_111.addWidget(self.LineEdit_Train_VITS_LogDir, 1, 0, 1, 3)


        self.verticalLayout_79.addWidget(self.Frame_Train_VITS_LogDir)

        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings.addItem(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_80.addWidget(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings)


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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.Frame_TTS_Top)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_VoiceConverter_Title_GPTSoVITS = QToolButton(self.Frame_TTS_Top)
        self.ToolButton_VoiceConverter_Title_GPTSoVITS.setObjectName(u"ToolButton_VoiceConverter_Title_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.ToolButton_VoiceConverter_Title_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.ToolButton_VoiceConverter_Title_GPTSoVITS.setSizePolicy(sizePolicy1)
        self.ToolButton_VoiceConverter_Title_GPTSoVITS.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_16.addWidget(self.ToolButton_VoiceConverter_Title_GPTSoVITS)

        self.ToolButton_VoiceConverter_Title_VITS = QToolButton(self.Frame_TTS_Top)
        self.ToolButton_VoiceConverter_Title_VITS.setObjectName(u"ToolButton_VoiceConverter_Title_VITS")
        sizePolicy1.setHeightForWidth(self.ToolButton_VoiceConverter_Title_VITS.sizePolicy().hasHeightForWidth())
        self.ToolButton_VoiceConverter_Title_VITS.setSizePolicy(sizePolicy1)
        self.ToolButton_VoiceConverter_Title_VITS.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_16.addWidget(self.ToolButton_VoiceConverter_Title_VITS)

        self.Frame_VoiceConverter_Title = QFrame(self.Frame_TTS_Top)
        self.Frame_VoiceConverter_Title.setObjectName(u"Frame_VoiceConverter_Title")
        self.Frame_VoiceConverter_Title.setStyleSheet(u"QFrame {\n"
"	/*font-size: 24px;\n"
"	text-align: center;\n"
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
        self.horizontalLayout_59 = QHBoxLayout(self.Frame_VoiceConverter_Title)
        self.horizontalLayout_59.setSpacing(12)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSpacer_VoiceConverter_Title = QSpacerItem(549, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_59.addItem(self.HorizontalSpacer_VoiceConverter_Title)


        self.horizontalLayout_16.addWidget(self.Frame_VoiceConverter_Title)


        self.verticalLayout_42.addWidget(self.Frame_TTS_Top)

        self.StackedWidget_Pages_TTS = QStackedWidget(self.Page_TTS)
        self.StackedWidget_Pages_TTS.setObjectName(u"StackedWidget_Pages_TTS")
        self.StackedWidget_Pages_TTS.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.Subpage_TTS_GPTSoVITS = QWidget()
        self.Subpage_TTS_GPTSoVITS.setObjectName(u"Subpage_TTS_GPTSoVITS")
        self.gridLayout_109 = QGridLayout(self.Subpage_TTS_GPTSoVITS)
        self.gridLayout_109.setSpacing(12)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.gridLayout_109.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_TTS_GPTSoVITS = QWidget(self.Subpage_TTS_GPTSoVITS)
        self.Widget_Left_TTS_GPTSoVITS.setObjectName(u"Widget_Left_TTS_GPTSoVITS")
        self.Widget_Left_TTS_GPTSoVITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_TTS_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_69 = QVBoxLayout(self.Widget_Left_TTS_GPTSoVITS)
        self.verticalLayout_69.setSpacing(12)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_TTS_GPTSoVITS = QTreeWidget(self.Widget_Left_TTS_GPTSoVITS)
        __qtreewidgetitem7 = QTreeWidgetItem(self.TreeWidget_Catalogue_TTS_GPTSoVITS)
        QTreeWidgetItem(__qtreewidgetitem7)
        self.TreeWidget_Catalogue_TTS_GPTSoVITS.setObjectName(u"TreeWidget_Catalogue_TTS_GPTSoVITS")
        self.TreeWidget_Catalogue_TTS_GPTSoVITS.setStyleSheet(u"QTreeView {\n"
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
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal "
                        "{\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"}")

        self.verticalLayout_69.addWidget(self.TreeWidget_Catalogue_TTS_GPTSoVITS)


        self.gridLayout_109.addWidget(self.Widget_Left_TTS_GPTSoVITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_TTS_GPTSoVITS = ScrollAreaBase(self.Subpage_TTS_GPTSoVITS)
        self.ScrollArea_Middle_TTS_GPTSoVITS.setObjectName(u"ScrollArea_Middle_TTS_GPTSoVITS")
        self.ScrollArea_Middle_TTS_GPTSoVITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_TTS_GPTSoVITS.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_TTS_GPTSoVITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS.setObjectName(u"ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS")
        self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS.setGeometry(QRect(0, 0, 581, 649))
        self.verticalLayout_66 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS)
        self.verticalLayout_66.setSpacing(12)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_TTS_GPTSoVITS_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS)
        self.GroupBox_TTS_GPTSoVITS_InputParams.setObjectName(u"GroupBox_TTS_GPTSoVITS_InputParams")
        self.GroupBox_TTS_GPTSoVITS_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_125 = QVBoxLayout(self.GroupBox_TTS_GPTSoVITS_InputParams)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 12, 0, 12)
        self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings = QFrame(self.GroupBox_TTS_GPTSoVITS_InputParams)
        self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings.setObjectName(u"Frame_TTS_GPTSoVITS_InputParams_BasicSettings")
        self.verticalLayout_71 = QVBoxLayout(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS1 = QFrame(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS1.setObjectName(u"Frame_TTS_GPTSoVITS_ModelPathLoadS1")
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS1.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS1.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_97 = QGridLayout(self.Frame_TTS_GPTSoVITS_ModelPathLoadS1)
        self.gridLayout_97.setSpacing(12)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.gridLayout_97.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS1 = QLabel(self.Frame_TTS_GPTSoVITS_ModelPathLoadS1)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS1.setObjectName(u"Label_TTS_GPTSoVITS_ModelPathLoadS1")
        sizePolicy5.setHeightForWidth(self.Label_TTS_GPTSoVITS_ModelPathLoadS1.sizePolicy().hasHeightForWidth())
        self.Label_TTS_GPTSoVITS_ModelPathLoadS1.setSizePolicy(sizePolicy5)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS1.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_97.addWidget(self.Label_TTS_GPTSoVITS_ModelPathLoadS1, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_GPTSoVITS_ModelPathLoadS1 = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_97.addItem(self.HorizontalSpacer_TTS_GPTSoVITS_ModelPathLoadS1, 0, 1, 1, 1)

        self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions = MenuButton(self.Frame_TTS_GPTSoVITS_ModelPathLoadS1)
        self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions.setObjectName(u"Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions")
        self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_97.addWidget(self.Button_TTS_GPTSoVITS_ModelPathLoadS1_MoreActions, 0, 2, 1, 1)

        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1 = LineEditBase(self.Frame_TTS_GPTSoVITS_ModelPathLoadS1)
        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1.setObjectName(u"LineEdit_TTS_GPTSoVITS_ModelPathLoadS1")
        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1.setMinimumSize(QSize(0, 27))

        self.gridLayout_97.addWidget(self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS1, 1, 0, 1, 3)


        self.verticalLayout_71.addWidget(self.Frame_TTS_GPTSoVITS_ModelPathLoadS1)

        self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G = QFrame(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G.setObjectName(u"Frame_TTS_GPTSoVITS_ModelPathLoadS2G")
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_99 = QGridLayout(self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G)
        self.gridLayout_99.setSpacing(12)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.gridLayout_99.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS2G = QLabel(self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS2G.setObjectName(u"Label_TTS_GPTSoVITS_ModelPathLoadS2G")
        sizePolicy5.setHeightForWidth(self.Label_TTS_GPTSoVITS_ModelPathLoadS2G.sizePolicy().hasHeightForWidth())
        self.Label_TTS_GPTSoVITS_ModelPathLoadS2G.setSizePolicy(sizePolicy5)
        self.Label_TTS_GPTSoVITS_ModelPathLoadS2G.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_99.addWidget(self.Label_TTS_GPTSoVITS_ModelPathLoadS2G, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_GPTSoVITS_ModelPathLoadS2G = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_99.addItem(self.HorizontalSpacer_TTS_GPTSoVITS_ModelPathLoadS2G, 0, 1, 1, 1)

        self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions = MenuButton(self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G)
        self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions.setObjectName(u"Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions")
        self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_99.addWidget(self.Button_TTS_GPTSoVITS_ModelPathLoadS2G_MoreActions, 0, 2, 1, 1)

        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G = LineEditBase(self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G)
        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G.setObjectName(u"LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G")
        self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G.setMinimumSize(QSize(0, 27))

        self.gridLayout_99.addWidget(self.LineEdit_TTS_GPTSoVITS_ModelPathLoadS2G, 1, 0, 1, 3)


        self.verticalLayout_71.addWidget(self.Frame_TTS_GPTSoVITS_ModelPathLoadS2G)

        self.Frame_TTS_GPTSoVITS_ModelDirLoadBert = QFrame(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_TTS_GPTSoVITS_ModelDirLoadBert.setObjectName(u"Frame_TTS_GPTSoVITS_ModelDirLoadBert")
        self.Frame_TTS_GPTSoVITS_ModelDirLoadBert.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_GPTSoVITS_ModelDirLoadBert.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_100 = QGridLayout(self.Frame_TTS_GPTSoVITS_ModelDirLoadBert)
        self.gridLayout_100.setSpacing(12)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.gridLayout_100.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_GPTSoVITS_ModelDirLoadBert = QLabel(self.Frame_TTS_GPTSoVITS_ModelDirLoadBert)
        self.Label_TTS_GPTSoVITS_ModelDirLoadBert.setObjectName(u"Label_TTS_GPTSoVITS_ModelDirLoadBert")
        sizePolicy5.setHeightForWidth(self.Label_TTS_GPTSoVITS_ModelDirLoadBert.sizePolicy().hasHeightForWidth())
        self.Label_TTS_GPTSoVITS_ModelDirLoadBert.setSizePolicy(sizePolicy5)
        self.Label_TTS_GPTSoVITS_ModelDirLoadBert.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_100.addWidget(self.Label_TTS_GPTSoVITS_ModelDirLoadBert, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_GPTSoVITS_ModelDirLoadBert = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_100.addItem(self.HorizontalSpacer_TTS_GPTSoVITS_ModelDirLoadBert, 0, 1, 1, 1)

        self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions = MenuButton(self.Frame_TTS_GPTSoVITS_ModelDirLoadBert)
        self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions.setObjectName(u"Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions")
        self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_100.addWidget(self.Button_TTS_GPTSoVITS_ModelDirLoadBert_MoreActions, 0, 2, 1, 1)

        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert = LineEditBase(self.Frame_TTS_GPTSoVITS_ModelDirLoadBert)
        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert.setObjectName(u"LineEdit_TTS_GPTSoVITS_ModelDirLoadBert")
        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert.setMinimumSize(QSize(0, 27))

        self.gridLayout_100.addWidget(self.LineEdit_TTS_GPTSoVITS_ModelDirLoadBert, 1, 0, 1, 3)


        self.verticalLayout_71.addWidget(self.Frame_TTS_GPTSoVITS_ModelDirLoadBert)

        self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL = QFrame(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)
        self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL.setObjectName(u"Frame_TTS_GPTSoVITS_ModelDirLoadSSL")
        self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_101 = QGridLayout(self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL)
        self.gridLayout_101.setSpacing(12)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.gridLayout_101.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_GPTSoVITS_ModelDirLoadSSL = QLabel(self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL)
        self.Label_TTS_GPTSoVITS_ModelDirLoadSSL.setObjectName(u"Label_TTS_GPTSoVITS_ModelDirLoadSSL")
        sizePolicy5.setHeightForWidth(self.Label_TTS_GPTSoVITS_ModelDirLoadSSL.sizePolicy().hasHeightForWidth())
        self.Label_TTS_GPTSoVITS_ModelDirLoadSSL.setSizePolicy(sizePolicy5)
        self.Label_TTS_GPTSoVITS_ModelDirLoadSSL.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_101.addWidget(self.Label_TTS_GPTSoVITS_ModelDirLoadSSL, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_GPTSoVITS_ModelDirLoadSSL = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_101.addItem(self.HorizontalSpacer_TTS_GPTSoVITS_ModelDirLoadSSL, 0, 1, 1, 1)

        self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions = MenuButton(self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL)
        self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions.setObjectName(u"Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions")
        self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_101.addWidget(self.Button_TTS_GPTSoVITS_ModelDirLoadSSL_MoreActions, 0, 2, 1, 1)

        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL = LineEditBase(self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL)
        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL.setObjectName(u"LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL")
        self.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL.setMinimumSize(QSize(0, 27))

        self.gridLayout_101.addWidget(self.LineEdit_TTS_GPTSoVITS_ModelDirLoadSSL, 1, 0, 1, 3)


        self.verticalLayout_71.addWidget(self.Frame_TTS_GPTSoVITS_ModelDirLoadSSL)


        self.verticalLayout_125.addWidget(self.Frame_TTS_GPTSoVITS_InputParams_BasicSettings)


        self.verticalLayout_66.addWidget(self.GroupBox_TTS_GPTSoVITS_InputParams)

        self.GroupBox_TTS_GPTSoVITS_GPTSoVITSParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS)
        self.GroupBox_TTS_GPTSoVITS_GPTSoVITSParams.setObjectName(u"GroupBox_TTS_GPTSoVITS_GPTSoVITSParams")
        self.GroupBox_TTS_GPTSoVITS_GPTSoVITSParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_126 = QVBoxLayout(self.GroupBox_TTS_GPTSoVITS_GPTSoVITSParams)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 12, 0, 12)
        self.Frame_TTS_GPTSoVITS_GPTSoVITSParams_BasicSettings = QFrame(self.GroupBox_TTS_GPTSoVITS_GPTSoVITSParams)
        self.Frame_TTS_GPTSoVITS_GPTSoVITSParams_BasicSettings.setObjectName(u"Frame_TTS_GPTSoVITS_GPTSoVITSParams_BasicSettings")
        self.verticalLayout_70 = QVBoxLayout(self.Frame_TTS_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_GPTSoVITS_FP16Run = QFrame(self.Frame_TTS_GPTSoVITS_GPTSoVITSParams_BasicSettings)
        self.Frame_TTS_GPTSoVITS_FP16Run.setObjectName(u"Frame_TTS_GPTSoVITS_FP16Run")
        self.Frame_TTS_GPTSoVITS_FP16Run.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_GPTSoVITS_FP16Run.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.gridLayout_96 = QGridLayout(self.Frame_TTS_GPTSoVITS_FP16Run)
        self.gridLayout_96.setSpacing(12)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.gridLayout_96.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_GPTSoVITS_FP16Run = QLabel(self.Frame_TTS_GPTSoVITS_FP16Run)
        self.Label_TTS_GPTSoVITS_FP16Run.setObjectName(u"Label_TTS_GPTSoVITS_FP16Run")
        sizePolicy5.setHeightForWidth(self.Label_TTS_GPTSoVITS_FP16Run.sizePolicy().hasHeightForWidth())
        self.Label_TTS_GPTSoVITS_FP16Run.setSizePolicy(sizePolicy5)
        self.Label_TTS_GPTSoVITS_FP16Run.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_96.addWidget(self.Label_TTS_GPTSoVITS_FP16Run, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_GPTSoVITS_FP16Run = QSpacerItem(443, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_96.addItem(self.HorizontalSpacer_TTS_GPTSoVITS_FP16Run, 0, 1, 1, 1)

        self.Button_TTS_GPTSoVITS_FP16Run_MoreActions = MenuButton(self.Frame_TTS_GPTSoVITS_FP16Run)
        self.Button_TTS_GPTSoVITS_FP16Run_MoreActions.setObjectName(u"Button_TTS_GPTSoVITS_FP16Run_MoreActions")
        self.Button_TTS_GPTSoVITS_FP16Run_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_FP16Run_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_GPTSoVITS_FP16Run_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_96.addWidget(self.Button_TTS_GPTSoVITS_FP16Run_MoreActions, 0, 2, 1, 1)

        self.CheckBox_TTS_GPTSoVITS_FP16Run = QCheckBox(self.Frame_TTS_GPTSoVITS_FP16Run)
        self.CheckBox_TTS_GPTSoVITS_FP16Run.setObjectName(u"CheckBox_TTS_GPTSoVITS_FP16Run")
        self.CheckBox_TTS_GPTSoVITS_FP16Run.setMinimumSize(QSize(0, 27))
        self.CheckBox_TTS_GPTSoVITS_FP16Run.setStyleSheet(u"QCheckBox {\n"
"	font-size: 12px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.gridLayout_96.addWidget(self.CheckBox_TTS_GPTSoVITS_FP16Run, 1, 0, 1, 3)


        self.verticalLayout_70.addWidget(self.Frame_TTS_GPTSoVITS_FP16Run)


        self.verticalLayout_126.addWidget(self.Frame_TTS_GPTSoVITS_GPTSoVITSParams_BasicSettings)


        self.verticalLayout_66.addWidget(self.GroupBox_TTS_GPTSoVITS_GPTSoVITSParams)

        self.VerticalSpacer_TTS_GPTSoVITS = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_66.addItem(self.VerticalSpacer_TTS_GPTSoVITS)

        self.ScrollArea_Middle_TTS_GPTSoVITS.setWidget(self.ScrollArea_Middle_WidgetContents_TTS_GPTSoVITS)

        self.gridLayout_109.addWidget(self.ScrollArea_Middle_TTS_GPTSoVITS, 0, 1, 1, 1)

        self.Widget_Right_TTS_GPTSoVITS = QWidget(self.Subpage_TTS_GPTSoVITS)
        self.Widget_Right_TTS_GPTSoVITS.setObjectName(u"Widget_Right_TTS_GPTSoVITS")
        self.Widget_Right_TTS_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_15 = QGridLayout(self.Widget_Right_TTS_GPTSoVITS)
        self.gridLayout_15.setSpacing(12)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_TTS_GPTSoVITS = QTextBrowser(self.Widget_Right_TTS_GPTSoVITS)
        self.TextBrowser_Params_TTS_GPTSoVITS.setObjectName(u"TextBrowser_Params_TTS_GPTSoVITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_TTS_GPTSoVITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_TTS_GPTSoVITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_TTS_GPTSoVITS.setStyleSheet(u"QTextBrowser {\n"
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
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_15.addWidget(self.TextBrowser_Params_TTS_GPTSoVITS, 0, 0, 1, 3)

        self.Button_ResetSettings_TTS_GPTSoVITS = QPushButton(self.Widget_Right_TTS_GPTSoVITS)
        self.Button_ResetSettings_TTS_GPTSoVITS.setObjectName(u"Button_ResetSettings_TTS_GPTSoVITS")
        self.Button_ResetSettings_TTS_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_15.addWidget(self.Button_ResetSettings_TTS_GPTSoVITS, 1, 0, 1, 1)

        self.Button_ImportSettings_TTS_GPTSoVITS = QPushButton(self.Widget_Right_TTS_GPTSoVITS)
        self.Button_ImportSettings_TTS_GPTSoVITS.setObjectName(u"Button_ImportSettings_TTS_GPTSoVITS")
        self.Button_ImportSettings_TTS_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_15.addWidget(self.Button_ImportSettings_TTS_GPTSoVITS, 1, 1, 1, 1)

        self.Button_ExportSettings_TTS_GPTSoVITS = QPushButton(self.Widget_Right_TTS_GPTSoVITS)
        self.Button_ExportSettings_TTS_GPTSoVITS.setObjectName(u"Button_ExportSettings_TTS_GPTSoVITS")
        self.Button_ExportSettings_TTS_GPTSoVITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_15.addWidget(self.Button_ExportSettings_TTS_GPTSoVITS, 1, 2, 1, 1)


        self.gridLayout_109.addWidget(self.Widget_Right_TTS_GPTSoVITS, 0, 2, 1, 1)

        self.ProgressBar_TTS_GPTSoVITS = QProgressBar(self.Subpage_TTS_GPTSoVITS)
        self.ProgressBar_TTS_GPTSoVITS.setObjectName(u"ProgressBar_TTS_GPTSoVITS")
        self.ProgressBar_TTS_GPTSoVITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_TTS_GPTSoVITS.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	background-color: transparent;\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgba(123, 123, 123, 123));\n"
"}")
        self.ProgressBar_TTS_GPTSoVITS.setValue(0)
        self.ProgressBar_TTS_GPTSoVITS.setTextVisible(False)
        self.horizontalLayout_56 = QHBoxLayout(self.ProgressBar_TTS_GPTSoVITS)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_TTS_GPTSoVITS = QStackedWidget(self.ProgressBar_TTS_GPTSoVITS)
        self.StackedWidget_TTS_GPTSoVITS.setObjectName(u"StackedWidget_TTS_GPTSoVITS")
        self.StackedWidget_TTS_GPTSoVITS.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_TTS_GPTSoVITS.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
"}")
        self.Page_TTS_GPTSoVITS_Execute = QWidget()
        self.Page_TTS_GPTSoVITS_Execute.setObjectName(u"Page_TTS_GPTSoVITS_Execute")
        self.verticalLayout_136 = QVBoxLayout(self.Page_TTS_GPTSoVITS_Execute)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.Button_TTS_GPTSoVITS_Execute = QPushButton(self.Page_TTS_GPTSoVITS_Execute)
        self.Button_TTS_GPTSoVITS_Execute.setObjectName(u"Button_TTS_GPTSoVITS_Execute")
        sizePolicy3.setHeightForWidth(self.Button_TTS_GPTSoVITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_TTS_GPTSoVITS_Execute.setSizePolicy(sizePolicy3)
        self.Button_TTS_GPTSoVITS_Execute.setMinimumSize(QSize(0, 30))
        self.Button_TTS_GPTSoVITS_Execute.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"}")

        self.verticalLayout_136.addWidget(self.Button_TTS_GPTSoVITS_Execute)

        self.StackedWidget_TTS_GPTSoVITS.addWidget(self.Page_TTS_GPTSoVITS_Execute)
        self.Page_TTS_GPTSoVITS_Terminate = QWidget()
        self.Page_TTS_GPTSoVITS_Terminate.setObjectName(u"Page_TTS_GPTSoVITS_Terminate")
        self.verticalLayout_138 = QVBoxLayout(self.Page_TTS_GPTSoVITS_Terminate)
        self.verticalLayout_138.setSpacing(0)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.Button_TTS_GPTSoVITS_Terminate = QPushButton(self.Page_TTS_GPTSoVITS_Terminate)
        self.Button_TTS_GPTSoVITS_Terminate.setObjectName(u"Button_TTS_GPTSoVITS_Terminate")
        sizePolicy3.setHeightForWidth(self.Button_TTS_GPTSoVITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_TTS_GPTSoVITS_Terminate.setSizePolicy(sizePolicy3)
        self.Button_TTS_GPTSoVITS_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_TTS_GPTSoVITS_Terminate.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"}")

        self.verticalLayout_138.addWidget(self.Button_TTS_GPTSoVITS_Terminate)

        self.StackedWidget_TTS_GPTSoVITS.addWidget(self.Page_TTS_GPTSoVITS_Terminate)

        self.horizontalLayout_56.addWidget(self.StackedWidget_TTS_GPTSoVITS)


        self.gridLayout_109.addWidget(self.ProgressBar_TTS_GPTSoVITS, 1, 0, 1, 3)

        self.gridLayout_109.setColumnStretch(0, 3)
        self.gridLayout_109.setColumnStretch(1, 10)
        self.gridLayout_109.setColumnStretch(2, 7)
        self.StackedWidget_Pages_TTS.addWidget(self.Subpage_TTS_GPTSoVITS)
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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.Widget_Left_TTS_VITS)
        self.verticalLayout_11.setSpacing(12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_TTS_VITS = QTreeWidget(self.Widget_Left_TTS_VITS)
        __qtreewidgetitem8 = QTreeWidgetItem(self.TreeWidget_Catalogue_TTS_VITS)
        QTreeWidgetItem(__qtreewidgetitem8)
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
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"}\n"
"\n"
"QScrollBar::horizontal "
                        "{\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"}")

        self.verticalLayout_11.addWidget(self.TreeWidget_Catalogue_TTS_VITS)


        self.gridLayout_20.addWidget(self.Widget_Left_TTS_VITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_TTS_VITS = ScrollAreaBase(self.Subpage_TTS_VITS)
        self.ScrollArea_Middle_TTS_VITS.setObjectName(u"ScrollArea_Middle_TTS_VITS")
        self.ScrollArea_Middle_TTS_VITS.setMinimumSize(QSize(600, 0))
        self.ScrollArea_Middle_TTS_VITS.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_TTS_VITS.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_TTS_VITS = QWidget()
        self.ScrollArea_Middle_WidgetContents_TTS_VITS.setObjectName(u"ScrollArea_Middle_WidgetContents_TTS_VITS")
        self.ScrollArea_Middle_WidgetContents_TTS_VITS.setGeometry(QRect(0, 0, 581, 1020))
        self.verticalLayout_19 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.verticalLayout_19.setSpacing(12)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_TTS_VITS_InputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.GroupBox_TTS_VITS_InputParams.setObjectName(u"GroupBox_TTS_VITS_InputParams")
        self.GroupBox_TTS_VITS_InputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_69.addWidget(self.Label_TTS_VITS_ConfigPathLoad, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_ConfigPathLoad = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_69.addItem(self.HorizontalSpacer_TTS_VITS_ConfigPathLoad, 0, 1, 1, 1)

        self.Button_TTS_VITS_ConfigPathLoad_MoreActions = MenuButton(self.Frame_TTS_VITS_ConfigPathLoad)
        self.Button_TTS_VITS_ConfigPathLoad_MoreActions.setObjectName(u"Button_TTS_VITS_ConfigPathLoad_MoreActions")
        self.Button_TTS_VITS_ConfigPathLoad_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_ConfigPathLoad_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_ConfigPathLoad_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_69.addWidget(self.Button_TTS_VITS_ConfigPathLoad_MoreActions, 0, 2, 1, 1)

        self.LineEdit_TTS_VITS_ConfigPathLoad = LineEditBase(self.Frame_TTS_VITS_ConfigPathLoad)
        self.LineEdit_TTS_VITS_ConfigPathLoad.setObjectName(u"LineEdit_TTS_VITS_ConfigPathLoad")
        self.LineEdit_TTS_VITS_ConfigPathLoad.setMinimumSize(QSize(0, 27))

        self.gridLayout_69.addWidget(self.LineEdit_TTS_VITS_ConfigPathLoad, 1, 0, 1, 3)


        self.verticalLayout_132.addWidget(self.Frame_TTS_VITS_ConfigPathLoad)

        self.Frame_TTS_VITS_ModelPathLoad = QFrame(self.Frame_TTS_VITS_InputParams_BasicSettings)
        self.Frame_TTS_VITS_ModelPathLoad.setObjectName(u"Frame_TTS_VITS_ModelPathLoad")
        self.Frame_TTS_VITS_ModelPathLoad.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_ModelPathLoad.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_70.addWidget(self.Label_TTS_VITS_ModelPathLoad, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_ModelPathLoad = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_70.addItem(self.HorizontalSpacer_TTS_VITS_ModelPathLoad, 0, 1, 1, 1)

        self.Button_TTS_VITS_ModelPathLoad_MoreActions = MenuButton(self.Frame_TTS_VITS_ModelPathLoad)
        self.Button_TTS_VITS_ModelPathLoad_MoreActions.setObjectName(u"Button_TTS_VITS_ModelPathLoad_MoreActions")
        self.Button_TTS_VITS_ModelPathLoad_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_ModelPathLoad_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_ModelPathLoad_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_70.addWidget(self.Button_TTS_VITS_ModelPathLoad_MoreActions, 0, 2, 1, 1)

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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	border-color: rgba(201, 210, 222, 246);\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
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
"	background-co"
                        "lor: transparent;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 210);\n"
"}")

        self.verticalLayout_98.addWidget(self.PlainTextEdit_TTS_VITS_Text)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Text)

        self.Frame_TTS_VITS_Language = QFrame(self.Frame_TTS_VITS_VITSParams_BasicSettings)
        self.Frame_TTS_VITS_Language.setObjectName(u"Frame_TTS_VITS_Language")
        self.Frame_TTS_VITS_Language.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_Language.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_79.addWidget(self.Label_TTS_VITS_Language, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_Language = QSpacerItem(415, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_79.addItem(self.HorizontalSpacer_TTS_VITS_Language, 0, 1, 1, 1)

        self.Button_TTS_VITS_Language_MoreActions = MenuButton(self.Frame_TTS_VITS_Language)
        self.Button_TTS_VITS_Language_MoreActions.setObjectName(u"Button_TTS_VITS_Language_MoreActions")
        self.Button_TTS_VITS_Language_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_Language_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_Language_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_79.addWidget(self.Button_TTS_VITS_Language_MoreActions, 0, 2, 1, 1)

        self.ComboBox_TTS_VITS_Language = ComboBoxBase(self.Frame_TTS_VITS_Language)
        self.ComboBox_TTS_VITS_Language.setObjectName(u"ComboBox_TTS_VITS_Language")
        self.ComboBox_TTS_VITS_Language.setMinimumSize(QSize(0, 27))

        self.gridLayout_79.addWidget(self.ComboBox_TTS_VITS_Language, 1, 0, 1, 3)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Language)

        self.Frame_TTS_VITS_Speaker = QFrame(self.Frame_TTS_VITS_VITSParams_BasicSettings)
        self.Frame_TTS_VITS_Speaker.setObjectName(u"Frame_TTS_VITS_Speaker")
        self.Frame_TTS_VITS_Speaker.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_Speaker.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_104.addWidget(self.Label_TTS_VITS_Speaker)

        self.ComboBox_TTS_VITS_Speaker = ComboBoxBase(self.Frame_TTS_VITS_Speaker)
        self.ComboBox_TTS_VITS_Speaker.setObjectName(u"ComboBox_TTS_VITS_Speaker")
        self.ComboBox_TTS_VITS_Speaker.setMinimumSize(QSize(0, 27))

        self.verticalLayout_104.addWidget(self.ComboBox_TTS_VITS_Speaker)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Speaker)


        self.verticalLayout_117.addWidget(self.Frame_TTS_VITS_VITSParams_BasicSettings)

        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings = ToolBoxBase(self.GroupBox_TTS_VITS_VITSParams)
        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.setObjectName(u"ToolBox_TTS_VITS_VITSParams_AdvanceSettings")
        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content = WidgetBase()
        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content.setObjectName(u"ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content")
        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content.setGeometry(QRect(0, 0, 147, 315))
        self.verticalLayout_118 = QVBoxLayout(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_VITS_EmotionStrength = QFrame(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_TTS_VITS_EmotionStrength.setObjectName(u"Frame_TTS_VITS_EmotionStrength")
        self.Frame_TTS_VITS_EmotionStrength.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_EmotionStrength.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_71.addWidget(self.Label_TTS_VITS_EmotionStrength, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_EmotionStrength = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_71.addItem(self.HorizontalSpacer_TTS_VITS_EmotionStrength, 0, 1, 1, 1)

        self.Button_TTS_VITS_EmotionStrength_MoreActions = MenuButton(self.Frame_TTS_VITS_EmotionStrength)
        self.Button_TTS_VITS_EmotionStrength_MoreActions.setObjectName(u"Button_TTS_VITS_EmotionStrength_MoreActions")
        self.Button_TTS_VITS_EmotionStrength_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_EmotionStrength_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_EmotionStrength_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_71.addWidget(self.Button_TTS_VITS_EmotionStrength_MoreActions, 0, 2, 1, 1)

        self.ChildFrame_TTS_VITS_EmotionStrength = QFrame(self.Frame_TTS_VITS_EmotionStrength)
        self.ChildFrame_TTS_VITS_EmotionStrength.setObjectName(u"ChildFrame_TTS_VITS_EmotionStrength")
        sizePolicy5.setHeightForWidth(self.ChildFrame_TTS_VITS_EmotionStrength.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_EmotionStrength.setSizePolicy(sizePolicy5)
        self.ChildFrame_TTS_VITS_EmotionStrength.setStyleSheet(u"QFrame {\n"
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

        self.DoubleSpinBox_TTS_VITS_EmotionStrength = DoubleSpinBoxBase(self.ChildFrame_TTS_VITS_EmotionStrength)
        self.DoubleSpinBox_TTS_VITS_EmotionStrength.setObjectName(u"DoubleSpinBox_TTS_VITS_EmotionStrength")
        self.DoubleSpinBox_TTS_VITS_EmotionStrength.setMinimumSize(QSize(0, 27))

        self.horizontalLayout_43.addWidget(self.DoubleSpinBox_TTS_VITS_EmotionStrength)


        self.gridLayout_71.addWidget(self.ChildFrame_TTS_VITS_EmotionStrength, 1, 0, 1, 3)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_EmotionStrength)

        self.Frame_TTS_VITS_PhonemeDuration = QFrame(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_TTS_VITS_PhonemeDuration.setObjectName(u"Frame_TTS_VITS_PhonemeDuration")
        self.Frame_TTS_VITS_PhonemeDuration.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_PhonemeDuration.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_72.addWidget(self.Label_TTS_VITS_PhonemeDuration, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_PhonemeDuration = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_72.addItem(self.HorizontalSpacer_TTS_VITS_PhonemeDuration, 0, 1, 1, 1)

        self.Button_TTS_VITS_PhonemeDuration_MoreActions = MenuButton(self.Frame_TTS_VITS_PhonemeDuration)
        self.Button_TTS_VITS_PhonemeDuration_MoreActions.setObjectName(u"Button_TTS_VITS_PhonemeDuration_MoreActions")
        self.Button_TTS_VITS_PhonemeDuration_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_PhonemeDuration_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_PhonemeDuration_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_72.addWidget(self.Button_TTS_VITS_PhonemeDuration_MoreActions, 0, 2, 1, 1)

        self.ChildFrame_TTS_VITS_PhonemeDuration = QFrame(self.Frame_TTS_VITS_PhonemeDuration)
        self.ChildFrame_TTS_VITS_PhonemeDuration.setObjectName(u"ChildFrame_TTS_VITS_PhonemeDuration")
        sizePolicy5.setHeightForWidth(self.ChildFrame_TTS_VITS_PhonemeDuration.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_PhonemeDuration.setSizePolicy(sizePolicy5)
        self.ChildFrame_TTS_VITS_PhonemeDuration.setStyleSheet(u"QFrame {\n"
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

        self.DoubleSpinBox_TTS_VITS_PhonemeDuration = DoubleSpinBoxBase(self.ChildFrame_TTS_VITS_PhonemeDuration)
        self.DoubleSpinBox_TTS_VITS_PhonemeDuration.setObjectName(u"DoubleSpinBox_TTS_VITS_PhonemeDuration")
        self.DoubleSpinBox_TTS_VITS_PhonemeDuration.setMinimumSize(QSize(0, 27))

        self.horizontalLayout_44.addWidget(self.DoubleSpinBox_TTS_VITS_PhonemeDuration)


        self.gridLayout_72.addWidget(self.ChildFrame_TTS_VITS_PhonemeDuration, 1, 0, 1, 3)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_PhonemeDuration)

        self.Frame_TTS_VITS_SpeechRate = QFrame(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content)
        self.Frame_TTS_VITS_SpeechRate.setObjectName(u"Frame_TTS_VITS_SpeechRate")
        self.Frame_TTS_VITS_SpeechRate.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_SpeechRate.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_73.addWidget(self.Label_TTS_VITS_SpeechRate, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_SpeechRate = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_73.addItem(self.HorizontalSpacer_TTS_VITS_SpeechRate, 0, 1, 1, 1)

        self.Button_TTS_VITS_SpeechRate_MoreActions = MenuButton(self.Frame_TTS_VITS_SpeechRate)
        self.Button_TTS_VITS_SpeechRate_MoreActions.setObjectName(u"Button_TTS_VITS_SpeechRate_MoreActions")
        self.Button_TTS_VITS_SpeechRate_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_SpeechRate_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_SpeechRate_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_73.addWidget(self.Button_TTS_VITS_SpeechRate_MoreActions, 0, 2, 1, 1)

        self.ChildFrame_TTS_VITS_SpeechRate = QFrame(self.Frame_TTS_VITS_SpeechRate)
        self.ChildFrame_TTS_VITS_SpeechRate.setObjectName(u"ChildFrame_TTS_VITS_SpeechRate")
        sizePolicy5.setHeightForWidth(self.ChildFrame_TTS_VITS_SpeechRate.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_SpeechRate.setSizePolicy(sizePolicy5)
        self.ChildFrame_TTS_VITS_SpeechRate.setStyleSheet(u"QFrame {\n"
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

        self.DoubleSpinBox_TTS_VITS_SpeechRate = DoubleSpinBoxBase(self.ChildFrame_TTS_VITS_SpeechRate)
        self.DoubleSpinBox_TTS_VITS_SpeechRate.setObjectName(u"DoubleSpinBox_TTS_VITS_SpeechRate")
        self.DoubleSpinBox_TTS_VITS_SpeechRate.setMinimumSize(QSize(0, 27))

        self.horizontalLayout_45.addWidget(self.DoubleSpinBox_TTS_VITS_SpeechRate)


        self.gridLayout_73.addWidget(self.ChildFrame_TTS_VITS_SpeechRate, 1, 0, 1, 3)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_SpeechRate)

        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.addItem(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content, u"")

        self.verticalLayout_117.addWidget(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings)


        self.verticalLayout_19.addWidget(self.GroupBox_TTS_VITS_VITSParams)

        self.GroupBox_TTS_VITS_OutputParams = QGroupBox(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.GroupBox_TTS_VITS_OutputParams.setObjectName(u"GroupBox_TTS_VITS_OutputParams")
        self.GroupBox_TTS_VITS_OutputParams.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
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
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_74.addWidget(self.Label_TTS_VITS_AudioPathSave, 0, 0, 1, 1)

        self.HorizontalSpacer_TTS_VITS_AudioPathSave = QSpacerItem(445, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_74.addItem(self.HorizontalSpacer_TTS_VITS_AudioPathSave, 0, 1, 1, 1)

        self.Button_TTS_VITS_AudioPathSave_MoreActions = MenuButton(self.Frame_TTS_VITS_AudioPathSave)
        self.Button_TTS_VITS_AudioPathSave_MoreActions.setObjectName(u"Button_TTS_VITS_AudioPathSave_MoreActions")
        self.Button_TTS_VITS_AudioPathSave_MoreActions.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_AudioPathSave_MoreActions.setMaximumSize(QSize(27, 27))
        self.Button_TTS_VITS_AudioPathSave_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.gridLayout_74.addWidget(self.Button_TTS_VITS_AudioPathSave_MoreActions, 0, 2, 1, 1)

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
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(36, 36, 36, 3);\n"
"}")
        self.gridLayout_16 = QGridLayout(self.Widget_Right_TTS_VITS)
        self.gridLayout_16.setSpacing(12)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_TTS_VITS = QTextBrowser(self.Widget_Right_TTS_VITS)
        self.TextBrowser_Params_TTS_VITS.setObjectName(u"TextBrowser_Params_TTS_VITS")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_TTS_VITS.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_TTS_VITS.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_TTS_VITS.setStyleSheet(u"QTextBrowser {\n"
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
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color"
                        ": rgba(123, 123, 123, 210);\n"
"}")

        self.gridLayout_16.addWidget(self.TextBrowser_Params_TTS_VITS, 0, 0, 1, 3)

        self.Button_ResetSettings_TTS_VITS = QPushButton(self.Widget_Right_TTS_VITS)
        self.Button_ResetSettings_TTS_VITS.setObjectName(u"Button_ResetSettings_TTS_VITS")
        self.Button_ResetSettings_TTS_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_16.addWidget(self.Button_ResetSettings_TTS_VITS, 1, 0, 1, 1)

        self.Button_ImportSettings_TTS_VITS = QPushButton(self.Widget_Right_TTS_VITS)
        self.Button_ImportSettings_TTS_VITS.setObjectName(u"Button_ImportSettings_TTS_VITS")
        self.Button_ImportSettings_TTS_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_16.addWidget(self.Button_ImportSettings_TTS_VITS, 1, 1, 1, 1)

        self.Button_ExportSettings_TTS_VITS = QPushButton(self.Widget_Right_TTS_VITS)
        self.Button_ExportSettings_TTS_VITS.setObjectName(u"Button_ExportSettings_TTS_VITS")
        self.Button_ExportSettings_TTS_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_16.addWidget(self.Button_ExportSettings_TTS_VITS, 1, 2, 1, 1)

        self.Button_CheckOutput_TTS_VITS = QPushButton(self.Widget_Right_TTS_VITS)
        self.Button_CheckOutput_TTS_VITS.setObjectName(u"Button_CheckOutput_TTS_VITS")
        self.Button_CheckOutput_TTS_VITS.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 12px;\n"
"	background-color: transparent;\n"
"	padding: 6.6px;\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
"	border-color: rgb(120, 120, 120);\n"
"}")

        self.gridLayout_16.addWidget(self.Button_CheckOutput_TTS_VITS, 2, 0, 1, 3)


        self.gridLayout_20.addWidget(self.Widget_Right_TTS_VITS, 0, 2, 1, 1)

        self.ProgressBar_TTS_VITS = QProgressBar(self.Subpage_TTS_VITS)
        self.ProgressBar_TTS_VITS.setObjectName(u"ProgressBar_TTS_VITS")
        self.ProgressBar_TTS_VITS.setMinimumSize(QSize(0, 30))
        self.ProgressBar_TTS_VITS.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	background-color: transparent;\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgba(123, 123, 123, 123));\n"
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
"	background-color: rgba(123, 123, 123, 24);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(123, 123, 123, 48);\n"
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
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
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
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:hover {\n"
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
        self.verticalLayout_78 = QVBoxLayout(self.Page_Settings)
        self.verticalLayout_78.setSpacing(21)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(21, 12, 21, 12)
        self.Frame_Settings_Top = QFrame(self.Page_Settings)
        self.Frame_Settings_Top.setObjectName(u"Frame_Settings_Top")
        self.Frame_Settings_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Settings_Top.setStyleSheet(u"QFrame {\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.Frame_Settings_Top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_Settings_Title_Client = QToolButton(self.Frame_Settings_Top)
        self.ToolButton_Settings_Title_Client.setObjectName(u"ToolButton_Settings_Title_Client")
        sizePolicy1.setHeightForWidth(self.ToolButton_Settings_Title_Client.sizePolicy().hasHeightForWidth())
        self.ToolButton_Settings_Title_Client.setSizePolicy(sizePolicy1)
        self.ToolButton_Settings_Title_Client.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_4.addWidget(self.ToolButton_Settings_Title_Client)

        self.ToolButton_Settings_Title_Tools = QToolButton(self.Frame_Settings_Top)
        self.ToolButton_Settings_Title_Tools.setObjectName(u"ToolButton_Settings_Title_Tools")
        sizePolicy1.setHeightForWidth(self.ToolButton_Settings_Title_Tools.sizePolicy().hasHeightForWidth())
        self.ToolButton_Settings_Title_Tools.setSizePolicy(sizePolicy1)
        self.ToolButton_Settings_Title_Tools.setStyleSheet(u"QToolButton {\n"
"	font-size: 24px;\n"
"	/*text-align: center;*/\n"
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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_4.addWidget(self.ToolButton_Settings_Title_Tools)

        self.Frame_Settings_Title_Spacer = QLabel(self.Frame_Settings_Top)
        self.Frame_Settings_Title_Spacer.setObjectName(u"Frame_Settings_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_Settings_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Settings_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_Settings_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
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


        self.verticalLayout_78.addWidget(self.Frame_Settings_Top)

        self.StackedWidget_Pages_Settings = QStackedWidget(self.Page_Settings)
        self.StackedWidget_Pages_Settings.setObjectName(u"StackedWidget_Pages_Settings")
        self.StackedWidget_Pages_Settings.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.SubPage_Settings_Client = QWidget()
        self.SubPage_Settings_Client.setObjectName(u"SubPage_Settings_Client")
        self.gridLayout_80 = QGridLayout(self.SubPage_Settings_Client)
        self.gridLayout_80.setSpacing(12)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.gridLayout_80.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea_Settings_Client = ScrollAreaBase(self.SubPage_Settings_Client)
        self.ScrollArea_Settings_Client.setObjectName(u"ScrollArea_Settings_Client")
        self.ScrollArea_Settings_Client.setWidgetResizable(True)
        self.ScrollAreaWidgetContents_Settings_Client = QWidget()
        self.ScrollAreaWidgetContents_Settings_Client.setObjectName(u"ScrollAreaWidgetContents_Settings_Client")
        self.ScrollAreaWidgetContents_Settings_Client.setGeometry(QRect(0, 0, 1026, 559))
        self.verticalLayout_106 = QVBoxLayout(self.ScrollAreaWidgetContents_Settings_Client)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.GroupBox_Settings_Client_Outlook = QGroupBox(self.ScrollAreaWidgetContents_Settings_Client)
        self.GroupBox_Settings_Client_Outlook.setObjectName(u"GroupBox_Settings_Client_Outlook")
        self.GroupBox_Settings_Client_Outlook.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_13 = QVBoxLayout(self.GroupBox_Settings_Client_Outlook)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 12, 0, 12)
        self.Frame_Setting_Theme = QFrame(self.GroupBox_Settings_Client_Outlook)
        self.Frame_Setting_Theme.setObjectName(u"Frame_Setting_Theme")
        self.Frame_Setting_Theme.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_Theme.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_72 = QHBoxLayout(self.Frame_Setting_Theme)
        self.horizontalLayout_72.setSpacing(12)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_Theme = QLabel(self.Frame_Setting_Theme)
        self.Label_Setting_Theme.setObjectName(u"Label_Setting_Theme")
        sizePolicy4.setHeightForWidth(self.Label_Setting_Theme.sizePolicy().hasHeightForWidth())
        self.Label_Setting_Theme.setSizePolicy(sizePolicy4)
        self.Label_Setting_Theme.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_72.addWidget(self.Label_Setting_Theme)

        self.ComboBox_Setting_Theme = ComboBoxBase(self.Frame_Setting_Theme)
        self.ComboBox_Setting_Theme.setObjectName(u"ComboBox_Setting_Theme")
        self.ComboBox_Setting_Theme.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_72.addWidget(self.ComboBox_Setting_Theme)


        self.verticalLayout_13.addWidget(self.Frame_Setting_Theme)

        self.Frame_Setting_Language = QFrame(self.GroupBox_Settings_Client_Outlook)
        self.Frame_Setting_Language.setObjectName(u"Frame_Setting_Language")
        self.Frame_Setting_Language.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_Language.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_66 = QHBoxLayout(self.Frame_Setting_Language)
        self.horizontalLayout_66.setSpacing(12)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_Language = QLabel(self.Frame_Setting_Language)
        self.Label_Setting_Language.setObjectName(u"Label_Setting_Language")
        sizePolicy4.setHeightForWidth(self.Label_Setting_Language.sizePolicy().hasHeightForWidth())
        self.Label_Setting_Language.setSizePolicy(sizePolicy4)
        self.Label_Setting_Language.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_66.addWidget(self.Label_Setting_Language)

        self.ComboBox_Setting_Language = ComboBoxBase(self.Frame_Setting_Language)
        self.ComboBox_Setting_Language.setObjectName(u"ComboBox_Setting_Language")
        self.ComboBox_Setting_Language.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_66.addWidget(self.ComboBox_Setting_Language)


        self.verticalLayout_13.addWidget(self.Frame_Setting_Language)


        self.verticalLayout_106.addWidget(self.GroupBox_Settings_Client_Outlook)

        self.GroupBox_Settings_Client_Function = QGroupBox(self.ScrollAreaWidgetContents_Settings_Client)
        self.GroupBox_Settings_Client_Function.setObjectName(u"GroupBox_Settings_Client_Function")
        self.GroupBox_Settings_Client_Function.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_84 = QVBoxLayout(self.GroupBox_Settings_Client_Function)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 12, 0, 12)
        self.Frame_Setting_AutoUpdate = QFrame(self.GroupBox_Settings_Client_Function)
        self.Frame_Setting_AutoUpdate.setObjectName(u"Frame_Setting_AutoUpdate")
        self.Frame_Setting_AutoUpdate.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_AutoUpdate.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_65 = QHBoxLayout(self.Frame_Setting_AutoUpdate)
        self.horizontalLayout_65.setSpacing(12)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_AutoUpdate = QLabel(self.Frame_Setting_AutoUpdate)
        self.Label_Setting_AutoUpdate.setObjectName(u"Label_Setting_AutoUpdate")
        sizePolicy4.setHeightForWidth(self.Label_Setting_AutoUpdate.sizePolicy().hasHeightForWidth())
        self.Label_Setting_AutoUpdate.setSizePolicy(sizePolicy4)
        self.Label_Setting_AutoUpdate.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_65.addWidget(self.Label_Setting_AutoUpdate)

        self.CheckBox_Setting_AutoUpdate = QCheckBox(self.Frame_Setting_AutoUpdate)
        self.CheckBox_Setting_AutoUpdate.setObjectName(u"CheckBox_Setting_AutoUpdate")
        sizePolicy5.setHeightForWidth(self.CheckBox_Setting_AutoUpdate.sizePolicy().hasHeightForWidth())
        self.CheckBox_Setting_AutoUpdate.setSizePolicy(sizePolicy5)
        self.CheckBox_Setting_AutoUpdate.setMinimumSize(QSize(0, 30))
        self.CheckBox_Setting_AutoUpdate.setStyleSheet(u"QCheckBox {\n"
"	font-size: 15px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.horizontalLayout_65.addWidget(self.CheckBox_Setting_AutoUpdate)


        self.verticalLayout_84.addWidget(self.Frame_Setting_AutoUpdate)


        self.verticalLayout_106.addWidget(self.GroupBox_Settings_Client_Function)

        self.GroupBox_Settings_Client_Operation = QGroupBox(self.ScrollAreaWidgetContents_Settings_Client)
        self.GroupBox_Settings_Client_Operation.setObjectName(u"GroupBox_Settings_Client_Operation")
        self.GroupBox_Settings_Client_Operation.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_85 = QVBoxLayout(self.GroupBox_Settings_Client_Operation)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 12, 0, 12)
        self.Frame_Setting_Operation = QFrame(self.GroupBox_Settings_Client_Operation)
        self.Frame_Setting_Operation.setObjectName(u"Frame_Setting_Operation")
        self.Frame_Setting_Operation.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_Operation.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
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
"}")

        self.horizontalLayout_6.addWidget(self.Button_Setting_ClientRebooter)

        self.Button_Setting_IntegrityChecker = QPushButton(self.Frame_Setting_Operation)
        self.Button_Setting_IntegrityChecker.setObjectName(u"Button_Setting_IntegrityChecker")
        self.Button_Setting_IntegrityChecker.setMinimumSize(QSize(123, 0))
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
"}")

        self.horizontalLayout_6.addWidget(self.Button_Setting_IntegrityChecker)

        self.HorizontalSpacer_Setting_Operation = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.HorizontalSpacer_Setting_Operation)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 6)

        self.verticalLayout_85.addWidget(self.Frame_Setting_Operation)


        self.verticalLayout_106.addWidget(self.GroupBox_Settings_Client_Operation)

        self.VerticalSpacer_Settings_Client = QSpacerItem(20, 174, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_106.addItem(self.VerticalSpacer_Settings_Client)

        self.ScrollArea_Settings_Client.setWidget(self.ScrollAreaWidgetContents_Settings_Client)

        self.gridLayout_80.addWidget(self.ScrollArea_Settings_Client, 0, 0, 1, 1)

        self.StackedWidget_Pages_Settings.addWidget(self.SubPage_Settings_Client)
        self.SubPage_Settings_Tools = QWidget()
        self.SubPage_Settings_Tools.setObjectName(u"SubPage_Settings_Tools")
        self.gridLayout_93 = QGridLayout(self.SubPage_Settings_Tools)
        self.gridLayout_93.setSpacing(12)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.gridLayout_93.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea_Settings_Tools = ScrollAreaBase(self.SubPage_Settings_Tools)
        self.ScrollArea_Settings_Tools.setObjectName(u"ScrollArea_Settings_Tools")
        self.ScrollArea_Settings_Tools.setWidgetResizable(True)
        self.ScrollAreaWidgetContents_Settings_Tools = QWidget()
        self.ScrollAreaWidgetContents_Settings_Tools.setObjectName(u"ScrollAreaWidgetContents_Settings_Tools")
        self.ScrollAreaWidgetContents_Settings_Tools.setGeometry(QRect(0, 0, 235, 811))
        self.verticalLayout_34 = QVBoxLayout(self.ScrollAreaWidgetContents_Settings_Tools)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.GroupBox_Settings_Tools_Path = QGroupBox(self.ScrollAreaWidgetContents_Settings_Tools)
        self.GroupBox_Settings_Tools_Path.setObjectName(u"GroupBox_Settings_Tools_Path")
        self.GroupBox_Settings_Tools_Path.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_83 = QVBoxLayout(self.GroupBox_Settings_Tools_Path)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 12, 0, 12)
        self.Frame_Process_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_Process_OutputRoot.setObjectName(u"Frame_Process_OutputRoot")
        self.Frame_Process_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_Process_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_19 = QHBoxLayout(self.Frame_Process_OutputRoot)
        self.horizontalLayout_19.setSpacing(12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_OutputRoot = QLabel(self.Frame_Process_OutputRoot)
        self.Label_Process_OutputRoot.setObjectName(u"Label_Process_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_Process_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_Process_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_Process_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_19.addWidget(self.Label_Process_OutputRoot)

        self.LineEdit_Process_OutputRoot = LineEditBase(self.Frame_Process_OutputRoot)
        self.LineEdit_Process_OutputRoot.setObjectName(u"LineEdit_Process_OutputRoot")
        self.LineEdit_Process_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_19.addWidget(self.LineEdit_Process_OutputRoot)

        self.Button_Process_OutputRoot_MoreActions = MenuButton(self.Frame_Process_OutputRoot)
        self.Button_Process_OutputRoot_MoreActions.setObjectName(u"Button_Process_OutputRoot_MoreActions")
        self.Button_Process_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_Process_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_19.addWidget(self.Button_Process_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_Process_OutputRoot)

        self.Frame_ASR_VPR_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_ASR_VPR_OutputRoot.setObjectName(u"Frame_ASR_VPR_OutputRoot")
        self.Frame_ASR_VPR_OutputRoot.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_25 = QHBoxLayout(self.Frame_ASR_VPR_OutputRoot)
        self.horizontalLayout_25.setSpacing(12)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_OutputRoot = QLabel(self.Frame_ASR_VPR_OutputRoot)
        self.Label_ASR_VPR_OutputRoot.setObjectName(u"Label_ASR_VPR_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_ASR_VPR_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_ASR_VPR_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_25.addWidget(self.Label_ASR_VPR_OutputRoot)

        self.LineEdit_ASR_VPR_OutputRoot = LineEditBase(self.Frame_ASR_VPR_OutputRoot)
        self.LineEdit_ASR_VPR_OutputRoot.setObjectName(u"LineEdit_ASR_VPR_OutputRoot")
        self.LineEdit_ASR_VPR_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_25.addWidget(self.LineEdit_ASR_VPR_OutputRoot)

        self.Button_ASR_VPR_OutputRoot_MoreActions = MenuButton(self.Frame_ASR_VPR_OutputRoot)
        self.Button_ASR_VPR_OutputRoot_MoreActions.setObjectName(u"Button_ASR_VPR_OutputRoot_MoreActions")
        self.Button_ASR_VPR_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_ASR_VPR_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_25.addWidget(self.Button_ASR_VPR_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_ASR_VPR_OutputRoot)

        self.Frame_STT_Whisper_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_STT_Whisper_OutputRoot.setObjectName(u"Frame_STT_Whisper_OutputRoot")
        self.Frame_STT_Whisper_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_STT_Whisper_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_20 = QHBoxLayout(self.Frame_STT_Whisper_OutputRoot)
        self.horizontalLayout_20.setSpacing(12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_OutputRoot = QLabel(self.Frame_STT_Whisper_OutputRoot)
        self.Label_STT_Whisper_OutputRoot.setObjectName(u"Label_STT_Whisper_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_STT_Whisper_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_STT_Whisper_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_20.addWidget(self.Label_STT_Whisper_OutputRoot)

        self.LineEdit_STT_Whisper_OutputRoot = LineEditBase(self.Frame_STT_Whisper_OutputRoot)
        self.LineEdit_STT_Whisper_OutputRoot.setObjectName(u"LineEdit_STT_Whisper_OutputRoot")
        self.LineEdit_STT_Whisper_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_20.addWidget(self.LineEdit_STT_Whisper_OutputRoot)

        self.Button_STT_Whisper_OutputRoot_MoreActions = MenuButton(self.Frame_STT_Whisper_OutputRoot)
        self.Button_STT_Whisper_OutputRoot_MoreActions.setObjectName(u"Button_STT_Whisper_OutputRoot_MoreActions")
        self.Button_STT_Whisper_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_STT_Whisper_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_20.addWidget(self.Button_STT_Whisper_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_STT_Whisper_OutputRoot)

        self.Frame_DAT_GPTSoVITS_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_DAT_GPTSoVITS_OutputRoot.setObjectName(u"Frame_DAT_GPTSoVITS_OutputRoot")
        self.Frame_DAT_GPTSoVITS_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_DAT_GPTSoVITS_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_21 = QHBoxLayout(self.Frame_DAT_GPTSoVITS_OutputRoot)
        self.horizontalLayout_21.setSpacing(12)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_GPTSoVITS_OutputRoot = QLabel(self.Frame_DAT_GPTSoVITS_OutputRoot)
        self.Label_DAT_GPTSoVITS_OutputRoot.setObjectName(u"Label_DAT_GPTSoVITS_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_DAT_GPTSoVITS_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_DAT_GPTSoVITS_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_DAT_GPTSoVITS_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_21.addWidget(self.Label_DAT_GPTSoVITS_OutputRoot)

        self.LineEdit_DAT_GPTSoVITS_OutputRoot = LineEditBase(self.Frame_DAT_GPTSoVITS_OutputRoot)
        self.LineEdit_DAT_GPTSoVITS_OutputRoot.setObjectName(u"LineEdit_DAT_GPTSoVITS_OutputRoot")
        self.LineEdit_DAT_GPTSoVITS_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_21.addWidget(self.LineEdit_DAT_GPTSoVITS_OutputRoot)

        self.Button_DAT_GPTSoVITS_OutputRoot_MoreActions = MenuButton(self.Frame_DAT_GPTSoVITS_OutputRoot)
        self.Button_DAT_GPTSoVITS_OutputRoot_MoreActions.setObjectName(u"Button_DAT_GPTSoVITS_OutputRoot_MoreActions")
        self.Button_DAT_GPTSoVITS_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_DAT_GPTSoVITS_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_21.addWidget(self.Button_DAT_GPTSoVITS_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_DAT_GPTSoVITS_OutputRoot)

        self.Frame_DAT_VITS_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_DAT_VITS_OutputRoot.setObjectName(u"Frame_DAT_VITS_OutputRoot")
        self.Frame_DAT_VITS_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_DAT_VITS_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_22 = QHBoxLayout(self.Frame_DAT_VITS_OutputRoot)
        self.horizontalLayout_22.setSpacing(12)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_OutputRoot = QLabel(self.Frame_DAT_VITS_OutputRoot)
        self.Label_DAT_VITS_OutputRoot.setObjectName(u"Label_DAT_VITS_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_DAT_VITS_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_DAT_VITS_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_22.addWidget(self.Label_DAT_VITS_OutputRoot)

        self.LineEdit_DAT_VITS_OutputRoot = LineEditBase(self.Frame_DAT_VITS_OutputRoot)
        self.LineEdit_DAT_VITS_OutputRoot.setObjectName(u"LineEdit_DAT_VITS_OutputRoot")
        self.LineEdit_DAT_VITS_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_22.addWidget(self.LineEdit_DAT_VITS_OutputRoot)

        self.Button_DAT_VITS_OutputRoot_MoreActions = MenuButton(self.Frame_DAT_VITS_OutputRoot)
        self.Button_DAT_VITS_OutputRoot_MoreActions.setObjectName(u"Button_DAT_VITS_OutputRoot_MoreActions")
        self.Button_DAT_VITS_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_DAT_VITS_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_22.addWidget(self.Button_DAT_VITS_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_DAT_VITS_OutputRoot)

        self.Frame_Train_GPTSoVITS_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_Train_GPTSoVITS_OutputRoot.setObjectName(u"Frame_Train_GPTSoVITS_OutputRoot")
        self.Frame_Train_GPTSoVITS_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_Train_GPTSoVITS_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_23 = QHBoxLayout(self.Frame_Train_GPTSoVITS_OutputRoot)
        self.horizontalLayout_23.setSpacing(12)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_GPTSoVITS_OutputRoot = QLabel(self.Frame_Train_GPTSoVITS_OutputRoot)
        self.Label_Train_GPTSoVITS_OutputRoot.setObjectName(u"Label_Train_GPTSoVITS_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_Train_GPTSoVITS_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_Train_GPTSoVITS_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_Train_GPTSoVITS_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_23.addWidget(self.Label_Train_GPTSoVITS_OutputRoot)

        self.LineEdit_Train_GPTSoVITS_OutputRoot = LineEditBase(self.Frame_Train_GPTSoVITS_OutputRoot)
        self.LineEdit_Train_GPTSoVITS_OutputRoot.setObjectName(u"LineEdit_Train_GPTSoVITS_OutputRoot")
        self.LineEdit_Train_GPTSoVITS_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_23.addWidget(self.LineEdit_Train_GPTSoVITS_OutputRoot)

        self.Button_Train_GPTSoVITS_OutputRoot_MoreActions = MenuButton(self.Frame_Train_GPTSoVITS_OutputRoot)
        self.Button_Train_GPTSoVITS_OutputRoot_MoreActions.setObjectName(u"Button_Train_GPTSoVITS_OutputRoot_MoreActions")
        self.Button_Train_GPTSoVITS_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_Train_GPTSoVITS_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_23.addWidget(self.Button_Train_GPTSoVITS_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_Train_GPTSoVITS_OutputRoot)

        self.Frame_Train_VITS_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_Train_VITS_OutputRoot.setObjectName(u"Frame_Train_VITS_OutputRoot")
        self.Frame_Train_VITS_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_Train_VITS_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_24 = QHBoxLayout(self.Frame_Train_VITS_OutputRoot)
        self.horizontalLayout_24.setSpacing(12)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_OutputRoot = QLabel(self.Frame_Train_VITS_OutputRoot)
        self.Label_Train_VITS_OutputRoot.setObjectName(u"Label_Train_VITS_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_Train_VITS_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_Train_VITS_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_24.addWidget(self.Label_Train_VITS_OutputRoot)

        self.LineEdit_Train_VITS_OutputRoot = LineEditBase(self.Frame_Train_VITS_OutputRoot)
        self.LineEdit_Train_VITS_OutputRoot.setObjectName(u"LineEdit_Train_VITS_OutputRoot")
        self.LineEdit_Train_VITS_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_24.addWidget(self.LineEdit_Train_VITS_OutputRoot)

        self.Button_Train_VITS_OutputRoot_MoreActions = MenuButton(self.Frame_Train_VITS_OutputRoot)
        self.Button_Train_VITS_OutputRoot_MoreActions.setObjectName(u"Button_Train_VITS_OutputRoot_MoreActions")
        self.Button_Train_VITS_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_Train_VITS_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_24.addWidget(self.Button_Train_VITS_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_Train_VITS_OutputRoot)


        self.verticalLayout_34.addWidget(self.GroupBox_Settings_Tools_Path)

        self.VerticalSpacer_Settings_Tools = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_34.addItem(self.VerticalSpacer_Settings_Tools)

        self.GroupBox_Settings_Tools_Function = QGroupBox(self.ScrollAreaWidgetContents_Settings_Tools)
        self.GroupBox_Settings_Tools_Function.setObjectName(u"GroupBox_Settings_Tools_Function")
        self.GroupBox_Settings_Tools_Function.setStyleSheet(u"QGroupBox {\n"
"	font-size: 15px;\n"
"	margin-top: 1.5ex;\n"
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
        self.verticalLayout_82 = QVBoxLayout(self.GroupBox_Settings_Tools_Function)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 12, 0, 12)
        self.Frame_Setting_Synchronizer = QFrame(self.GroupBox_Settings_Tools_Function)
        self.Frame_Setting_Synchronizer.setObjectName(u"Frame_Setting_Synchronizer")
        self.Frame_Setting_Synchronizer.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_Synchronizer.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_74 = QHBoxLayout(self.Frame_Setting_Synchronizer)
        self.horizontalLayout_74.setSpacing(12)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_Synchronizer = QLabel(self.Frame_Setting_Synchronizer)
        self.Label_Setting_Synchronizer.setObjectName(u"Label_Setting_Synchronizer")
        sizePolicy4.setHeightForWidth(self.Label_Setting_Synchronizer.sizePolicy().hasHeightForWidth())
        self.Label_Setting_Synchronizer.setSizePolicy(sizePolicy4)
        self.Label_Setting_Synchronizer.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_74.addWidget(self.Label_Setting_Synchronizer)

        self.CheckBox_Setting_Synchronizer = QCheckBox(self.Frame_Setting_Synchronizer)
        self.CheckBox_Setting_Synchronizer.setObjectName(u"CheckBox_Setting_Synchronizer")
        sizePolicy5.setHeightForWidth(self.CheckBox_Setting_Synchronizer.sizePolicy().hasHeightForWidth())
        self.CheckBox_Setting_Synchronizer.setSizePolicy(sizePolicy5)
        self.CheckBox_Setting_Synchronizer.setMinimumSize(QSize(0, 30))
        self.CheckBox_Setting_Synchronizer.setStyleSheet(u"QCheckBox {\n"
"	font-size: 15px;\n"
"	spacing: 12.3px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"}\n"
"QCheckBox:hover {\n"
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
"}")

        self.horizontalLayout_74.addWidget(self.CheckBox_Setting_Synchronizer)


        self.verticalLayout_82.addWidget(self.Frame_Setting_Synchronizer)


        self.verticalLayout_34.addWidget(self.GroupBox_Settings_Tools_Function)

        self.ScrollArea_Settings_Tools.setWidget(self.ScrollAreaWidgetContents_Settings_Tools)

        self.gridLayout_93.addWidget(self.ScrollArea_Settings_Tools, 0, 0, 1, 1)

        self.StackedWidget_Pages_Settings.addWidget(self.SubPage_Settings_Tools)

        self.verticalLayout_78.addWidget(self.StackedWidget_Pages_Settings)

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
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 123);\n"
"}\n"
"QToolButton:checked {\n"
"	background-color: transparent;\n"
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(120, 180, 240, 210);\n"
"}")

        self.horizontalLayout_29.addWidget(self.ToolButton_Info_Title)

        self.Frame_Info_Title_Spacer = QLabel(self.Frame_Info_Top)
        self.Frame_Info_Title_Spacer.setObjectName(u"Frame_Info_Title_Spacer")
        sizePolicy4.setHeightForWidth(self.Frame_Info_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Info_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_Info_Title_Spacer.setStyleSheet(u"QLabel {\n"
"	font-size: 24px;\n"
"	/*text-align: center;\n"
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
"	border-radius: 0px;\n"
"	border-style: solid;"
                        "\n"
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
"QScrollBar::sub-line:horizontal {\n"
"	width: 0px;\n"
"	backg"
                        "round-color: transparent;\n"
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
"	background-color: transparent;\n"
"	border-width: 1.2px 0px 0px 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: rgba(45, 45, 45, 135);\n"
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
"	background-color: rgba(36, 36, 36, 12);\n"
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
"}")

        self.horizontalLayout_14.addWidget(self.Button_Console_Fold)


        self.verticalLayout_23.addWidget(self.Frame_Console_Top)

        self.ScrollArea_Console = QScrollArea(self.Frame_Console)
        self.ScrollArea_Console.setObjectName(u"ScrollArea_Console")
        self.ScrollArea_Console.setStyleSheet(u"QScrollArea, QScrollArea QWidget {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"	background-color: rgba(210, 210, 210, 123);\n"
"	border-width: 1.2px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QScrollBar:hover {\n"
"	background-color: rgba(210, 210, 210, 210);\n"
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
"	background-color: rgba(123, 123, 123, 123);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"	background-color: rgba(123, 123, 123, 21"
                        "0);\n"
"}")
        self.ScrollArea_Console.setWidgetResizable(True)
        self.ScrollAreaWidgetContents_Console = QWidget()
        self.ScrollAreaWidgetContents_Console.setObjectName(u"ScrollAreaWidgetContents_Console")
        self.ScrollAreaWidgetContents_Console.setGeometry(QRect(0, 0, 1061, 31))
        self.verticalLayout_50 = QVBoxLayout(self.ScrollAreaWidgetContents_Console)
        self.verticalLayout_50.setSpacing(21)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(21, 0, 21, 0)
        self.PlainTextEdit_Console = QPlainTextEdit(self.ScrollAreaWidgetContents_Console)
        self.PlainTextEdit_Console.setObjectName(u"PlainTextEdit_Console")
        self.PlainTextEdit_Console.setStyleSheet(u"QPlainTextEdit {\n"
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
        self.StackedWidget_Pages_Env.setCurrentIndex(0)
        self.StackedWidget_Pages_Models.setCurrentIndex(0)
        self.StackedWidget_Pages_Process.setCurrentIndex(0)
        self.StackedWidget_Pages_ASR.setCurrentIndex(0)
        self.StackedWidget_Pages_STT.setCurrentIndex(0)
        self.StackedWidget_Pages_Dataset.setCurrentIndex(0)
        self.StackedWidget_DAT_GPTSoVITS.setCurrentIndex(0)
        self.StackedWidget_DAT_VITS.setCurrentIndex(0)
        self.StackedWidget_Pages_Train.setCurrentIndex(0)
        self.StackedWidget_Train_GPTSoVITS.setCurrentIndex(0)
        self.StackedWidget_Train_VITS.setCurrentIndex(0)
        self.StackedWidget_Pages_TTS.setCurrentIndex(0)
        self.StackedWidget_Pages_Settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
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
        self.Label_Env_Install_Aria2_Status.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Env_Install_Aria2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_FFmpeg_Status.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Env_Install_FFmpeg.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_Python_Status.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Env_Install_Python.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_PyReqs_Status.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Env_Install_PyReqs.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Env_Install_Pytorch_Status.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Env_Install_Pytorch.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Env_Manage_Pytorch.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Env_Manage_Pytorch_Version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_Models_Process_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_Models_ASR_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_Models_STT_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_Models_TTS_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.TabWidget_Models_Process.setTabText(self.TabWidget_Models_Process.indexOf(self.Tab_Models_Process_UVR), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabWidget_Models_ASR.setTabText(self.TabWidget_Models_ASR.indexOf(self.Tab_Models_ASR_VPR), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabWidget_Models_STT.setTabText(self.TabWidget_Models_STT.indexOf(self.Tab_Models_STT_Whisper), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabWidget_Models_TTS.setTabText(self.TabWidget_Models_TTS.indexOf(self.Tab_Models_TTS_GPTSoVITS), QCoreApplication.translate("MainWindow", u"\u9875", None))
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
        self.GroupBox_Process_DenoiserParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_Process_DenoiseAudio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Process_DenoiseAudio.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Process_DenoiseModelPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_DenoiseTarget.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Process_SlicerParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_Process_SliceAudio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Process_SliceAudio.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Process_RMSThreshold.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_AudioLengthMin.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_SilentIntervalMin.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_HopSize.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_SilenceKeptMax.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_Process_SlicerParams_AdvanceSettings.setItemText(self.ToolBox_Process_SlicerParams_AdvanceSettings.indexOf(self.ToolBox_Process_SlicerParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_Process_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_Process_MediaFormatOutput.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_SampleRate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_SampleWidth.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_ToMono.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Process_ToMono.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolBox_Process_OutputParams_AdvanceSettings.setItemText(self.ToolBox_Process_OutputParams_AdvanceSettings.indexOf(self.ToolBox_Process_OutputParams_AdvanceSettings_Page1Content), "")
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
        self.Label_ASR_VPR_ModelType.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_FeatureMethod.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_DurationOfAudio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings.setItemText(self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings.indexOf(self.ToolBox_ASR_VPR_VPRParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_ASR_VPR_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_ASR_VPR_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_AudioSpeakersDataName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings.setItemText(self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings.indexOf(self.ToolBox_ASR_VPR_OutputParams_AdvanceSettings_Page1Content), "")
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
        self.Label_STT_Whisper_fp16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_STT_Whisper_fp16.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.CheckBox_STT_Whisper_ConditionOnPreviousText.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_STT_Whisper_ConditionOnPreviousText.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_STT_Whisper_Verbose.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_STT_Whisper_Verbose.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings.setItemText(self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings.indexOf(self.ToolBox_STT_Whisper_WhisperParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_STT_Whisper_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_STT_Whisper_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_DatasetCreator_Title_GPTSoVITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_DatasetCreator_Title_VITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem9 = self.TreeWidget_Catalogue_DAT_GPTSoVITS.headerItem()
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled3 = self.TreeWidget_Catalogue_DAT_GPTSoVITS.isSortingEnabled()
        self.TreeWidget_Catalogue_DAT_GPTSoVITS.setSortingEnabled(False)
        ___qtreewidgetitem10 = self.TreeWidget_Catalogue_DAT_GPTSoVITS.topLevelItem(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_DAT_GPTSoVITS.setSortingEnabled(__sortingEnabled3)

        self.GroupBox_DAT_GPTSoVITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_DAT_GPTSoVITS_AudioSpeakersDataPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_GPTSoVITS_SRTDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_DAT_GPTSoVITS_GPTSoVITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_DAT_GPTSoVITS_DataFormat.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_DAT_GPTSoVITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_DAT_GPTSoVITS_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_GPTSoVITS_FileListName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.setItemText(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings.indexOf(self.ToolBox_DAT_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content), "")
        ___qtreewidgetitem12 = self.TreeWidget_Catalogue_DAT_VITS.headerItem()
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled4 = self.TreeWidget_Catalogue_DAT_VITS.isSortingEnabled()
        self.TreeWidget_Catalogue_DAT_VITS.setSortingEnabled(False)
        ___qtreewidgetitem13 = self.TreeWidget_Catalogue_DAT_VITS.topLevelItem(0)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_DAT_VITS.setSortingEnabled(__sortingEnabled4)

        self.GroupBox_DAT_VITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_DAT_VITS_AudioSpeakersDataPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_SRTDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_DAT_VITS_VITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_DAT_VITS_DataFormat.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_AddAuxiliaryData.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_DAT_VITS_AddAuxiliaryData.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_DAT_VITS_AuxiliaryDataPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_TrainRatio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_SampleRate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_SampleWidth.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_ToMono.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_DAT_VITS_ToMono.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.setItemText(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings.indexOf(self.ToolBox_DAT_VITS_VITSParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_DAT_VITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_DAT_VITS_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_FileListNameTraining.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_FileListNameValidation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.setItemText(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings.indexOf(self.ToolBox_DAT_VITS_OutputParams_AdvanceSettings_Page1Content), "")
        self.ToolButton_VoiceTrainer_Title_GPTSoVITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_VoiceTrainer_Title_VITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem15 = self.TreeWidget_Catalogue_Train_GPTSoVITS.headerItem()
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled5 = self.TreeWidget_Catalogue_Train_GPTSoVITS.isSortingEnabled()
        self.TreeWidget_Catalogue_Train_GPTSoVITS.setSortingEnabled(False)
        ___qtreewidgetitem16 = self.TreeWidget_Catalogue_Train_GPTSoVITS.topLevelItem(0)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Train_GPTSoVITS.setSortingEnabled(__sortingEnabled5)

        self.GroupBox_Train_GPTSoVITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_Train_GPTSoVITS_FileListPath.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Train_GPTSoVITS_GPTSoVITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2G.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_ModelDirPretrainedBert.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_ModelDirPretrainedSSL.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_ModelPathPretrainedS2D.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_GPTSoVITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.setItemText(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings.indexOf(self.ToolBox_Train_GPTSoVITS_GPTSoVITSParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_Train_GPTSoVITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_Train_GPTSoVITS_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_LogDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.setItemText(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings.indexOf(self.ToolBox_Train_GPTSoVITS_OutputParams_AdvanceSettings_Page1Content), "")
        ___qtreewidgetitem18 = self.TreeWidget_Catalogue_Train_VITS.headerItem()
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled6 = self.TreeWidget_Catalogue_Train_VITS.isSortingEnabled()
        self.TreeWidget_Catalogue_Train_VITS.setSortingEnabled(False)
        ___qtreewidgetitem19 = self.TreeWidget_Catalogue_Train_VITS.topLevelItem(0)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem19.child(0)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Train_VITS.setSortingEnabled(__sortingEnabled6)

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
        self.Label_Train_VITS_NumWorkers.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_VITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.setItemText(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings.indexOf(self.ToolBox_Train_VITS_VITSParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_Train_VITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_Train_VITS_EvalInterval.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_OutputDirName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_LogDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_Train_VITS_OutputParams_AdvanceSettings.setItemText(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings.indexOf(self.ToolBox_Train_VITS_OutputParams_AdvanceSettings_Page1Content), "")
        self.ToolButton_VoiceConverter_Title_GPTSoVITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_VoiceConverter_Title_VITS.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem21 = self.TreeWidget_Catalogue_TTS_GPTSoVITS.headerItem()
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled7 = self.TreeWidget_Catalogue_TTS_GPTSoVITS.isSortingEnabled()
        self.TreeWidget_Catalogue_TTS_GPTSoVITS.setSortingEnabled(False)
        ___qtreewidgetitem22 = self.TreeWidget_Catalogue_TTS_GPTSoVITS.topLevelItem(0)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem22.child(0)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_TTS_GPTSoVITS.setSortingEnabled(__sortingEnabled7)

        self.GroupBox_TTS_GPTSoVITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_TTS_GPTSoVITS_ModelPathLoadS1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_GPTSoVITS_ModelPathLoadS2G.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_GPTSoVITS_ModelDirLoadBert.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_GPTSoVITS_ModelDirLoadSSL.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_TTS_GPTSoVITS_GPTSoVITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_TTS_GPTSoVITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_TTS_GPTSoVITS_FP16Run.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        ___qtreewidgetitem24 = self.TreeWidget_Catalogue_TTS_VITS.headerItem()
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled8 = self.TreeWidget_Catalogue_TTS_VITS.isSortingEnabled()
        self.TreeWidget_Catalogue_TTS_VITS.setSortingEnabled(False)
        ___qtreewidgetitem25 = self.TreeWidget_Catalogue_TTS_VITS.topLevelItem(0)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem25.child(0)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_TTS_VITS.setSortingEnabled(__sortingEnabled8)

        self.GroupBox_TTS_VITS_InputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.Label_TTS_VITS_ConfigPathLoad.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_ModelPathLoad.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_TTS_VITS_VITSParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_TTS_VITS_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_Speaker.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_EmotionStrength.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_PhonemeDuration.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_SpeechRate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.setItemText(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings.indexOf(self.ToolBox_TTS_VITS_VITSParams_AdvanceSettings_Page1Content), "")
        self.GroupBox_TTS_VITS_OutputParams.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox3", None))
        self.Label_TTS_VITS_AudioPathSave.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_Settings_Title_Client.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_Settings_Title_Tools.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.GroupBox_Settings_Client_Outlook.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Setting_Theme.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Setting_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Settings_Client_Function.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_Settings_Client_Operation.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.GroupBox_Settings_Tools_Path.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Process_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_STT_Whisper_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_GPTSoVITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Settings_Tools_Function.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolButton_Info_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Console_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Label_ToolsStatus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Usage_CPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Usage_GPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        pass