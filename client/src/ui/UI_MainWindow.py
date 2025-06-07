from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, QRect, QSize)
from PySide6.QtGui import (QIcon, QFont)
from PySide6.QtWidgets import *

from components import ButtonBase, NavigationButton, HollowButton, MenuButton, CheckBoxBase, LabelBase, LineEditBase, TextEditBase, TextBrowserBase, ComboBoxBase, GroupBoxBase, ScrollAreaBase, TabWidgetBase, Table_ViewModels
from views import EnvPage, ToolPage


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
"	image: url(:/Button_Icon/images/icons/Menu.png);\n"
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

        self.CheckBox_SwitchTheme = CheckBoxBase(self.Frame_Top)
        self.CheckBox_SwitchTheme.setObjectName(u"CheckBox_SwitchTheme")

        self.horizontalLayout_11.addWidget(self.CheckBox_SwitchTheme)

        self.Frame_Top_Control_Window = QFrame(self.Frame_Top)
        self.Frame_Top_Control_Window.setObjectName(u"Frame_Top_Control_Window")
        self.Frame_Top_Control_Window.setMinimumSize(QSize(144, 0))
        self.Frame_Top_Control_Window.setMaximumSize(QSize(144, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.Frame_Top_Control_Window)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Button_Minimize_Window = ButtonBase(self.Frame_Top_Control_Window)
        self.Button_Minimize_Window.setObjectName(u"Button_Minimize_Window")
        sizePolicy.setHeightForWidth(self.Button_Minimize_Window.sizePolicy().hasHeightForWidth())
        self.Button_Minimize_Window.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.Button_Minimize_Window)

        self.Button_Maximize_Window = ButtonBase(self.Frame_Top_Control_Window)
        self.Button_Maximize_Window.setObjectName(u"Button_Maximize_Window")
        sizePolicy.setHeightForWidth(self.Button_Maximize_Window.sizePolicy().hasHeightForWidth())
        self.Button_Maximize_Window.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.Button_Maximize_Window)

        self.Button_Close_Window = ButtonBase(self.Frame_Top_Control_Window)
        self.Button_Close_Window.setObjectName(u"Button_Close_Window")
        sizePolicy.setHeightForWidth(self.Button_Close_Window.sizePolicy().hasHeightForWidth())
        self.Button_Close_Window.setSizePolicy(sizePolicy)

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
        self.Button_Menu_Home = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Home.setObjectName(u"Button_Menu_Home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Button_Menu_Home.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Home.setSizePolicy(sizePolicy1)
        self.Button_Menu_Home.setMinimumSize(QSize(0, 48))
        icon = QIcon()
        icon.addFile(u":/Button_Icon/images/icons/Home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Home.setIcon(icon)
        self.Button_Menu_Home.setIconSize(QSize(24, 24))
        self.horizontalLayout_8 = QHBoxLayout(self.Button_Menu_Home)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Home)

        self.Button_Menu_Env = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Env.setObjectName(u"Button_Menu_Env")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Env.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Env.setSizePolicy(sizePolicy1)
        self.Button_Menu_Env.setMinimumSize(QSize(0, 48))
        icon1 = QIcon()
        icon1.addFile(u":/Button_Icon/images/icons/Box.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Env.setIcon(icon1)
        self.Button_Menu_Env.setIconSize(QSize(24, 24))
        self.horizontalLayout_7 = QHBoxLayout(self.Button_Menu_Env)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Env)

        self.Button_Menu_Models = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Models.setObjectName(u"Button_Menu_Models")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Models.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Models.setSizePolicy(sizePolicy1)
        self.Button_Menu_Models.setMinimumSize(QSize(0, 48))
        icon2 = QIcon()
        icon2.addFile(u":/Button_Icon/images/icons/Boxes.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Models.setIcon(icon2)
        self.Button_Menu_Models.setIconSize(QSize(24, 24))
        self.horizontalLayout_34 = QHBoxLayout(self.Button_Menu_Models)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Models)

        self.Button_Menu_Process = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Process.setObjectName(u"Button_Menu_Process")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Process.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Process.setSizePolicy(sizePolicy1)
        self.Button_Menu_Process.setMinimumSize(QSize(0, 48))
        icon3 = QIcon()
        icon3.addFile(u":/Button_Icon/images/icons/Audio.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Process.setIcon(icon3)
        self.Button_Menu_Process.setIconSize(QSize(24, 24))
        self.horizontalLayout_33 = QHBoxLayout(self.Button_Menu_Process)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Process)

        self.Button_Menu_VPR = NavigationButton(self.Frame_Menu)
        self.Button_Menu_VPR.setObjectName(u"Button_Menu_VPR")
        sizePolicy1.setHeightForWidth(self.Button_Menu_VPR.sizePolicy().hasHeightForWidth())
        self.Button_Menu_VPR.setSizePolicy(sizePolicy1)
        self.Button_Menu_VPR.setMinimumSize(QSize(0, 48))
        icon4 = QIcon()
        icon4.addFile(u":/Button_Icon/images/icons/VPR.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_VPR.setIcon(icon4)
        self.Button_Menu_VPR.setIconSize(QSize(24, 24))
        self.horizontalLayout_10 = QHBoxLayout(self.Button_Menu_VPR)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_VPR)

        self.Button_Menu_ASR = NavigationButton(self.Frame_Menu)
        self.Button_Menu_ASR.setObjectName(u"Button_Menu_ASR")
        sizePolicy1.setHeightForWidth(self.Button_Menu_ASR.sizePolicy().hasHeightForWidth())
        self.Button_Menu_ASR.setSizePolicy(sizePolicy1)
        self.Button_Menu_ASR.setMinimumSize(QSize(0, 48))
        icon5 = QIcon()
        icon5.addFile(u":/Button_Icon/images/icons/ASR.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_ASR.setIcon(icon5)
        self.Button_Menu_ASR.setIconSize(QSize(24, 24))
        self.horizontalLayout_36 = QHBoxLayout(self.Button_Menu_ASR)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_ASR)

        self.Button_Menu_Dataset = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Dataset.setObjectName(u"Button_Menu_Dataset")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Dataset.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Dataset.setSizePolicy(sizePolicy1)
        self.Button_Menu_Dataset.setMinimumSize(QSize(0, 48))
        icon6 = QIcon()
        icon6.addFile(u":/Button_Icon/images/icons/Dataset.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Dataset.setIcon(icon6)
        self.Button_Menu_Dataset.setIconSize(QSize(24, 24))
        self.horizontalLayout_38 = QHBoxLayout(self.Button_Menu_Dataset)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Dataset)

        self.Button_Menu_Train = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Train.setObjectName(u"Button_Menu_Train")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Train.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Train.setSizePolicy(sizePolicy1)
        self.Button_Menu_Train.setMinimumSize(QSize(0, 48))
        icon7 = QIcon()
        icon7.addFile(u":/Button_Icon/images/icons/HDD.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Train.setIcon(icon7)
        self.Button_Menu_Train.setIconSize(QSize(24, 24))
        self.horizontalLayout_40 = QHBoxLayout(self.Button_Menu_Train)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Train)

        self.Button_Menu_TTS = NavigationButton(self.Frame_Menu)
        self.Button_Menu_TTS.setObjectName(u"Button_Menu_TTS")
        sizePolicy1.setHeightForWidth(self.Button_Menu_TTS.sizePolicy().hasHeightForWidth())
        self.Button_Menu_TTS.setSizePolicy(sizePolicy1)
        self.Button_Menu_TTS.setMinimumSize(QSize(0, 48))
        icon8 = QIcon()
        icon8.addFile(u":/Button_Icon/images/icons/TTS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_TTS.setIcon(icon8)
        self.Button_Menu_TTS.setIconSize(QSize(24, 24))
        self.horizontalLayout_47 = QHBoxLayout(self.Button_Menu_TTS)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_TTS)

        self.VerticalSpacer_Menu = QSpacerItem(20, 522, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.VerticalSpacer_Menu)

        self.Button_Menu_Settings = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Settings.setObjectName(u"Button_Menu_Settings")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Settings.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Settings.setSizePolicy(sizePolicy1)
        self.Button_Menu_Settings.setMinimumSize(QSize(0, 48))
        icon9 = QIcon()
        icon9.addFile(u":/Button_Icon/images/icons/Settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Settings.setIcon(icon9)
        self.Button_Menu_Settings.setIconSize(QSize(24, 24))
        self.horizontalLayout_9 = QHBoxLayout(self.Button_Menu_Settings)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Settings)

        self.Button_Menu_Info = NavigationButton(self.Frame_Menu)
        self.Button_Menu_Info.setObjectName(u"Button_Menu_Info")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Info.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Info.setSizePolicy(sizePolicy1)
        self.Button_Menu_Info.setMinimumSize(QSize(0, 48))
        icon10 = QIcon()
        icon10.addFile(u":/Button_Icon/images/icons/Info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu_Info.setIcon(icon10)
        self.Button_Menu_Info.setIconSize(QSize(24, 24))
        self.horizontalLayout_13 = QHBoxLayout(self.Button_Menu_Info)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.Button_Menu_Info)


        self.horizontalLayout_2.addWidget(self.Frame_Menu)

        self.Frame_Pages = QFrame(self.Content)
        self.Frame_Pages.setObjectName(u"Frame_Pages")
        self.verticalLayout_5 = QVBoxLayout(self.Frame_Pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Splitter_Pages = QSplitter(self.Frame_Pages)
        self.Splitter_Pages.setObjectName(u"Splitter_Pages")
        self.Splitter_Pages.setOrientation(Qt.Orientation.Vertical)
        self.Splitter_Pages.setHandleWidth(0)
        self.Splitter_Pages.setChildrenCollapsible(False)
        self.StackedWidget_Pages = QStackedWidget(self.Splitter_Pages)
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

        self.TextBrowser_Text_Home = TextBrowserBase(self.Frame_High_Home)
        self.TextBrowser_Text_Home.setObjectName(u"TextBrowser_Text_Home")

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
        self.Button_Demo = HollowButton(self.Frame_Low_Home)
        self.Button_Demo.setObjectName(u"Button_Demo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Button_Demo.sizePolicy().hasHeightForWidth())
        self.Button_Demo.setSizePolicy(sizePolicy2)
        self.Button_Demo.setMinimumSize(QSize(210, 75))
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
"	image: url(:/Button_Icon/images/icons/Play.png);\n"
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

        self.Label_Demo_Text = LabelBase(self.Button_Demo)
        self.Label_Demo_Text.setObjectName(u"Label_Demo_Text")

        self.horizontalLayout_70.addWidget(self.Label_Demo_Text)

        self.horizontalLayout_70.setStretch(0, 2)
        self.horizontalLayout_70.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.Button_Demo)

        self.HorizontalSpacer_Low_Home_1 = QSpacerItem(107, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.HorizontalSpacer_Low_Home_1)

        self.Button_Server = HollowButton(self.Frame_Low_Home)
        self.Button_Server.setObjectName(u"Button_Server")
        sizePolicy2.setHeightForWidth(self.Button_Server.sizePolicy().hasHeightForWidth())
        self.Button_Server.setSizePolicy(sizePolicy2)
        self.Button_Server.setMinimumSize(QSize(210, 75))
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
"	image: url(:/Button_Icon/images/icons/Server.png);\n"
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

        self.Label_Server_Text = LabelBase(self.Button_Server)
        self.Label_Server_Text.setObjectName(u"Label_Server_Text")

        self.horizontalLayout_71.addWidget(self.Label_Server_Text)

        self.horizontalLayout_71.setStretch(0, 2)
        self.horizontalLayout_71.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.Button_Server)

        self.HorizontalSpacer_Low_Home_2 = QSpacerItem(106, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.HorizontalSpacer_Low_Home_2)

        self.Button_Repo = HollowButton(self.Frame_Low_Home)
        self.Button_Repo.setObjectName(u"Button_Repo")
        sizePolicy2.setHeightForWidth(self.Button_Repo.sizePolicy().hasHeightForWidth())
        self.Button_Repo.setSizePolicy(sizePolicy2)
        self.Button_Repo.setMinimumSize(QSize(210, 75))
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
"	image: url(:/Button_Icon/images/icons/GitHub.png);\n"
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

        self.Label_Repo_Text = LabelBase(self.Button_Repo)
        self.Label_Repo_Text.setObjectName(u"Label_Repo_Text")

        self.horizontalLayout_76.addWidget(self.Label_Repo_Text)

        self.horizontalLayout_76.setStretch(0, 2)
        self.horizontalLayout_76.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.Button_Repo)

        self.HorizontalSpacer_Low_Home_3 = QSpacerItem(107, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.HorizontalSpacer_Low_Home_3)

        self.Button_Donate = HollowButton(self.Frame_Low_Home)
        self.Button_Donate.setObjectName(u"Button_Donate")
        sizePolicy2.setHeightForWidth(self.Button_Donate.sizePolicy().hasHeightForWidth())
        self.Button_Donate.setSizePolicy(sizePolicy2)
        self.Button_Donate.setMinimumSize(QSize(210, 75))
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
"	image: url(:/Button_Icon/images/icons/Heart.png);\n"
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

        self.Label_Donate_Text = LabelBase(self.Button_Donate)
        self.Label_Donate_Text.setObjectName(u"Label_Donate_Text")

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
        self.Page_Env = EnvPage()
        self.Page_Env.setObjectName(u"Page_Env")
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
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.Frame_Models_Top)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.Button_Models_Process_Title = NavigationButton(self.Frame_Models_Top)
        self.Button_Models_Process_Title.setObjectName(u"Button_Models_Process_Title")
        sizePolicy1.setHeightForWidth(self.Button_Models_Process_Title.sizePolicy().hasHeightForWidth())
        self.Button_Models_Process_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.Button_Models_Process_Title)

        self.Button_Models_VPR_Title = NavigationButton(self.Frame_Models_Top)
        self.Button_Models_VPR_Title.setObjectName(u"Button_Models_VPR_Title")
        sizePolicy1.setHeightForWidth(self.Button_Models_VPR_Title.sizePolicy().hasHeightForWidth())
        self.Button_Models_VPR_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.Button_Models_VPR_Title)

        self.Button_Models_ASR_Title = NavigationButton(self.Frame_Models_Top)
        self.Button_Models_ASR_Title.setObjectName(u"Button_Models_ASR_Title")
        sizePolicy1.setHeightForWidth(self.Button_Models_ASR_Title.sizePolicy().hasHeightForWidth())
        self.Button_Models_ASR_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.Button_Models_ASR_Title)

        self.Button_Models_TTS_Title = NavigationButton(self.Frame_Models_Top)
        self.Button_Models_TTS_Title.setObjectName(u"Button_Models_TTS_Title")
        sizePolicy1.setHeightForWidth(self.Button_Models_TTS_Title.sizePolicy().hasHeightForWidth())
        self.Button_Models_TTS_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.Button_Models_TTS_Title)

        self.HorizontalSpacer_Models_Title = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.HorizontalSpacer_Models_Title)

        self.Button_Models_Refresh = ButtonBase(self.Frame_Models_Top)
        self.Button_Models_Refresh.setObjectName(u"Button_Models_Refresh")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Button_Models_Refresh.sizePolicy().hasHeightForWidth())
        self.Button_Models_Refresh.setSizePolicy(sizePolicy3)
        self.Button_Models_Refresh.setMinimumSize(QSize(84, 0))
        icon11 = QIcon()
        icon11.addFile(u":/Button_Icon/images/icons/Refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Models_Refresh.setIcon(icon11)
        self.Button_Models_Refresh.setIconSize(QSize(21, 21))

        self.horizontalLayout_18.addWidget(self.Button_Models_Refresh)

        self.Button_Models_Append = ButtonBase(self.Frame_Models_Top)
        self.Button_Models_Append.setObjectName(u"Button_Models_Append")
        sizePolicy3.setHeightForWidth(self.Button_Models_Append.sizePolicy().hasHeightForWidth())
        self.Button_Models_Append.setSizePolicy(sizePolicy3)
        self.Button_Models_Append.setMinimumSize(QSize(84, 0))
        icon12 = QIcon()
        icon12.addFile(u":/Button_Icon/images/icons/Plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Models_Append.setIcon(icon12)
        self.Button_Models_Append.setIconSize(QSize(21, 21))

        self.horizontalLayout_18.addWidget(self.Button_Models_Append)


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
        self.TabWidget_Models_Process = TabWidgetBase(self.SubPage_Models_Process)
        self.TabWidget_Models_Process.setObjectName(u"TabWidget_Models_Process")
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
        self.SubPage_Models_VPR = QWidget()
        self.SubPage_Models_VPR.setObjectName(u"SubPage_Models_VPR")
        self.gridLayout_7 = QGridLayout(self.SubPage_Models_VPR)
        self.gridLayout_7.setSpacing(12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.TabWidget_Models_VPR = TabWidgetBase(self.SubPage_Models_VPR)
        self.TabWidget_Models_VPR.setObjectName(u"TabWidget_Models_VPR")
        self.Tab_Models_VPR_TDNN = QWidget()
        self.Tab_Models_VPR_TDNN.setObjectName(u"Tab_Models_VPR_TDNN")
        self.verticalLayout_27 = QVBoxLayout(self.Tab_Models_VPR_TDNN)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_VPR_TDNN = Table_ViewModels(self.Tab_Models_VPR_TDNN)
        self.Table_Models_VPR_TDNN.setObjectName(u"Table_Models_VPR_TDNN")

        self.verticalLayout_27.addWidget(self.Table_Models_VPR_TDNN)

        self.TabWidget_Models_VPR.addTab(self.Tab_Models_VPR_TDNN, "")

        self.gridLayout_7.addWidget(self.TabWidget_Models_VPR, 0, 0, 1, 1)

        self.StackedWidget_Pages_Models.addWidget(self.SubPage_Models_VPR)
        self.SubPage_Models_ASR = QWidget()
        self.SubPage_Models_ASR.setObjectName(u"SubPage_Models_ASR")
        self.gridLayout_11 = QGridLayout(self.SubPage_Models_ASR)
        self.gridLayout_11.setSpacing(12)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.TabWidget_Models_ASR = TabWidgetBase(self.SubPage_Models_ASR)
        self.TabWidget_Models_ASR.setObjectName(u"TabWidget_Models_ASR")
        self.Tab_Models_ASR_Whisper = QWidget()
        self.Tab_Models_ASR_Whisper.setObjectName(u"Tab_Models_ASR_Whisper")
        self.verticalLayout_46 = QVBoxLayout(self.Tab_Models_ASR_Whisper)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.Table_Models_ASR_Whisper = Table_ViewModels(self.Tab_Models_ASR_Whisper)
        self.Table_Models_ASR_Whisper.setObjectName(u"Table_Models_ASR_Whisper")

        self.verticalLayout_46.addWidget(self.Table_Models_ASR_Whisper)

        self.TabWidget_Models_ASR.addTab(self.Tab_Models_ASR_Whisper, "")

        self.gridLayout_11.addWidget(self.TabWidget_Models_ASR, 0, 0, 1, 1)

        self.StackedWidget_Pages_Models.addWidget(self.SubPage_Models_ASR)
        self.SubPage_Models_TTS = QWidget()
        self.SubPage_Models_TTS.setObjectName(u"SubPage_Models_TTS")
        self.gridLayout_10 = QGridLayout(self.SubPage_Models_TTS)
        self.gridLayout_10.setSpacing(12)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.TabWidget_Models_TTS = TabWidgetBase(self.SubPage_Models_TTS)
        self.TabWidget_Models_TTS.setObjectName(u"TabWidget_Models_TTS")
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
        self.Page_Process = ToolPage()
        self.Page_Process.setObjectName(u"Page_Process")
        self.StackedWidget_Pages.addWidget(self.Page_Process)
        self.Page_VPR = ToolPage()
        self.Page_VPR.setObjectName(u"Page_VPR")
        self.StackedWidget_Pages.addWidget(self.Page_VPR)
        self.Page_ASR = ToolPage()
        self.Page_ASR.setObjectName(u"Page_ASR")
        self.StackedWidget_Pages.addWidget(self.Page_ASR)
        self.Page_Dataset = ToolPage()
        self.Page_Dataset.setObjectName(u"Page_Dataset")
        self.StackedWidget_Pages.addWidget(self.Page_Dataset)
        self.Page_Train = ToolPage()
        self.Page_Train.setObjectName(u"Page_Train")
        self.StackedWidget_Pages.addWidget(self.Page_Train)
        self.Page_TTS = ToolPage()
        self.Page_TTS.setObjectName(u"Page_TTS")
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
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.Frame_Settings_Top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Button_Settings_Title_Client = NavigationButton(self.Frame_Settings_Top)
        self.Button_Settings_Title_Client.setObjectName(u"Button_Settings_Title_Client")
        sizePolicy1.setHeightForWidth(self.Button_Settings_Title_Client.sizePolicy().hasHeightForWidth())
        self.Button_Settings_Title_Client.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.Button_Settings_Title_Client)

        self.Button_Settings_Title_Tools = NavigationButton(self.Frame_Settings_Top)
        self.Button_Settings_Title_Tools.setObjectName(u"Button_Settings_Title_Tools")
        sizePolicy1.setHeightForWidth(self.Button_Settings_Title_Tools.sizePolicy().hasHeightForWidth())
        self.Button_Settings_Title_Tools.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.Button_Settings_Title_Tools)

        self.Frame_Settings_Title_Spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.Frame_Settings_Title_Spacer)


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
        self.ScrollAreaWidgetContents_Settings_Client.setGeometry(QRect(0, 0, 246, 483))
        self.verticalLayout_106 = QVBoxLayout(self.ScrollAreaWidgetContents_Settings_Client)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.GroupBox_Settings_Client_Outlook = GroupBoxBase(self.ScrollAreaWidgetContents_Settings_Client)
        self.GroupBox_Settings_Client_Outlook.setObjectName(u"GroupBox_Settings_Client_Outlook")
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
        self.Label_Setting_Theme = LabelBase(self.Frame_Setting_Theme)
        self.Label_Setting_Theme.setObjectName(u"Label_Setting_Theme")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
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
        self.Label_Setting_Language = LabelBase(self.Frame_Setting_Language)
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

        self.GroupBox_Settings_Client_Function = GroupBoxBase(self.ScrollAreaWidgetContents_Settings_Client)
        self.GroupBox_Settings_Client_Function.setObjectName(u"GroupBox_Settings_Client_Function")
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
        self.Label_Setting_AutoUpdate = LabelBase(self.Frame_Setting_AutoUpdate)
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

        self.CheckBox_Setting_AutoUpdate = CheckBoxBase(self.Frame_Setting_AutoUpdate)
        self.CheckBox_Setting_AutoUpdate.setObjectName(u"CheckBox_Setting_AutoUpdate")
        self.CheckBox_Setting_AutoUpdate.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_65.addWidget(self.CheckBox_Setting_AutoUpdate)


        self.verticalLayout_84.addWidget(self.Frame_Setting_AutoUpdate)


        self.verticalLayout_106.addWidget(self.GroupBox_Settings_Client_Function)

        self.GroupBox_Settings_Client_Operation = GroupBoxBase(self.ScrollAreaWidgetContents_Settings_Client)
        self.GroupBox_Settings_Client_Operation.setObjectName(u"GroupBox_Settings_Client_Operation")
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
        self.Button_Setting_IntegrityChecker = HollowButton(self.Frame_Setting_Operation)
        self.Button_Setting_IntegrityChecker.setObjectName(u"Button_Setting_IntegrityChecker")

        self.horizontalLayout_6.addWidget(self.Button_Setting_IntegrityChecker)

        self.HorizontalSpacer_Setting_Operation = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.HorizontalSpacer_Setting_Operation)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 6)

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
        self.ScrollAreaWidgetContents_Settings_Tools.setGeometry(QRect(0, 0, 246, 907))
        self.verticalLayout_34 = QVBoxLayout(self.ScrollAreaWidgetContents_Settings_Tools)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.GroupBox_Settings_Tools_Function = GroupBoxBase(self.ScrollAreaWidgetContents_Settings_Tools)
        self.GroupBox_Settings_Tools_Function.setObjectName(u"GroupBox_Settings_Tools_Function")
        self.verticalLayout_76 = QVBoxLayout(self.GroupBox_Settings_Tools_Function)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 12, 0, 12)
        self.Frame_Setting_AutoReset = QFrame(self.GroupBox_Settings_Tools_Function)
        self.Frame_Setting_AutoReset.setObjectName(u"Frame_Setting_AutoReset")
        self.Frame_Setting_AutoReset.setMinimumSize(QSize(0, 90))
        self.Frame_Setting_AutoReset.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_75 = QHBoxLayout(self.Frame_Setting_AutoReset)
        self.horizontalLayout_75.setSpacing(12)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(21, 12, 21, 12)
        self.Label_Setting_AutoReset = LabelBase(self.Frame_Setting_AutoReset)
        self.Label_Setting_AutoReset.setObjectName(u"Label_Setting_AutoReset")
        sizePolicy4.setHeightForWidth(self.Label_Setting_AutoReset.sizePolicy().hasHeightForWidth())
        self.Label_Setting_AutoReset.setSizePolicy(sizePolicy4)
        self.Label_Setting_AutoReset.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_75.addWidget(self.Label_Setting_AutoReset)

        self.CheckBox_Setting_AutoReset = CheckBoxBase(self.Frame_Setting_AutoReset)
        self.CheckBox_Setting_AutoReset.setObjectName(u"CheckBox_Setting_AutoReset")
        self.CheckBox_Setting_AutoReset.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_75.addWidget(self.CheckBox_Setting_AutoReset)


        self.verticalLayout_76.addWidget(self.Frame_Setting_AutoReset)

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
        self.Label_Setting_Synchronizer = LabelBase(self.Frame_Setting_Synchronizer)
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

        self.CheckBox_Setting_Synchronizer = CheckBoxBase(self.Frame_Setting_Synchronizer)
        self.CheckBox_Setting_Synchronizer.setObjectName(u"CheckBox_Setting_Synchronizer")
        self.CheckBox_Setting_Synchronizer.setMinimumSize(QSize(123, 30))

        self.horizontalLayout_74.addWidget(self.CheckBox_Setting_Synchronizer)


        self.verticalLayout_76.addWidget(self.Frame_Setting_Synchronizer)


        self.verticalLayout_34.addWidget(self.GroupBox_Settings_Tools_Function)

        self.GroupBox_Settings_Tools_Path = GroupBoxBase(self.ScrollAreaWidgetContents_Settings_Tools)
        self.GroupBox_Settings_Tools_Path.setObjectName(u"GroupBox_Settings_Tools_Path")
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
        self.Label_Process_OutputRoot = LabelBase(self.Frame_Process_OutputRoot)
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

        self.Frame_VPR_TDNN_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_VPR_TDNN_OutputRoot.setObjectName(u"Frame_VPR_TDNN_OutputRoot")
        self.Frame_VPR_TDNN_OutputRoot.setMinimumSize(QSize(0, 105))
        self.Frame_VPR_TDNN_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_25 = QHBoxLayout(self.Frame_VPR_TDNN_OutputRoot)
        self.horizontalLayout_25.setSpacing(12)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(21, 12, 21, 12)
        self.Label_VPR_TDNN_OutputRoot = LabelBase(self.Frame_VPR_TDNN_OutputRoot)
        self.Label_VPR_TDNN_OutputRoot.setObjectName(u"Label_VPR_TDNN_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_VPR_TDNN_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_VPR_TDNN_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_VPR_TDNN_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_25.addWidget(self.Label_VPR_TDNN_OutputRoot)

        self.LineEdit_VPR_TDNN_OutputRoot = LineEditBase(self.Frame_VPR_TDNN_OutputRoot)
        self.LineEdit_VPR_TDNN_OutputRoot.setObjectName(u"LineEdit_VPR_TDNN_OutputRoot")
        self.LineEdit_VPR_TDNN_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_25.addWidget(self.LineEdit_VPR_TDNN_OutputRoot)

        self.Button_VPR_TDNN_OutputRoot_MoreActions = MenuButton(self.Frame_VPR_TDNN_OutputRoot)
        self.Button_VPR_TDNN_OutputRoot_MoreActions.setObjectName(u"Button_VPR_TDNN_OutputRoot_MoreActions")
        self.Button_VPR_TDNN_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_VPR_TDNN_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_25.addWidget(self.Button_VPR_TDNN_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_VPR_TDNN_OutputRoot)

        self.Frame_ASR_Whisper_OutputRoot = QFrame(self.GroupBox_Settings_Tools_Path)
        self.Frame_ASR_Whisper_OutputRoot.setObjectName(u"Frame_ASR_Whisper_OutputRoot")
        self.Frame_ASR_Whisper_OutputRoot.setMinimumSize(QSize(0, 90))
        self.Frame_ASR_Whisper_OutputRoot.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgba(36, 36, 36, 12);\n"
"}")
        self.horizontalLayout_20 = QHBoxLayout(self.Frame_ASR_Whisper_OutputRoot)
        self.horizontalLayout_20.setSpacing(12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_Whisper_OutputRoot = LabelBase(self.Frame_ASR_Whisper_OutputRoot)
        self.Label_ASR_Whisper_OutputRoot.setObjectName(u"Label_ASR_Whisper_OutputRoot")
        sizePolicy4.setHeightForWidth(self.Label_ASR_Whisper_OutputRoot.sizePolicy().hasHeightForWidth())
        self.Label_ASR_Whisper_OutputRoot.setSizePolicy(sizePolicy4)
        self.Label_ASR_Whisper_OutputRoot.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_20.addWidget(self.Label_ASR_Whisper_OutputRoot)

        self.LineEdit_ASR_Whisper_OutputRoot = LineEditBase(self.Frame_ASR_Whisper_OutputRoot)
        self.LineEdit_ASR_Whisper_OutputRoot.setObjectName(u"LineEdit_ASR_Whisper_OutputRoot")
        self.LineEdit_ASR_Whisper_OutputRoot.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_20.addWidget(self.LineEdit_ASR_Whisper_OutputRoot)

        self.Button_ASR_Whisper_OutputRoot_MoreActions = MenuButton(self.Frame_ASR_Whisper_OutputRoot)
        self.Button_ASR_Whisper_OutputRoot_MoreActions.setObjectName(u"Button_ASR_Whisper_OutputRoot_MoreActions")
        self.Button_ASR_Whisper_OutputRoot_MoreActions.setMaximumSize(QSize(30, 30))
        self.Button_ASR_Whisper_OutputRoot_MoreActions.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(123, 123, 123);\n"
"}")

        self.horizontalLayout_20.addWidget(self.Button_ASR_Whisper_OutputRoot_MoreActions)


        self.verticalLayout_83.addWidget(self.Frame_ASR_Whisper_OutputRoot)

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
        self.Label_DAT_GPTSoVITS_OutputRoot = LabelBase(self.Frame_DAT_GPTSoVITS_OutputRoot)
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
        self.Label_DAT_VITS_OutputRoot = LabelBase(self.Frame_DAT_VITS_OutputRoot)
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
        self.Label_Train_GPTSoVITS_OutputRoot = LabelBase(self.Frame_Train_GPTSoVITS_OutputRoot)
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
        self.Label_Train_VITS_OutputRoot = LabelBase(self.Frame_Train_VITS_OutputRoot)
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
"	border-top-width: 0px;\n"
"	border-right-width: 0px;\n"
"	border-bottom-width: 3px;\n"
"	border-left-width: 0px;\n"
"	border-style: solid;\n"
"	border-bottom-color: rgba(123, 123, 123, 123);\n"
"}")
        self.horizontalLayout_29 = QHBoxLayout(self.Frame_Info_Top)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.Button_Info_Title = NavigationButton(self.Frame_Info_Top)
        self.Button_Info_Title.setObjectName(u"Button_Info_Title")
        sizePolicy1.setHeightForWidth(self.Button_Info_Title.sizePolicy().hasHeightForWidth())
        self.Button_Info_Title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_29.addWidget(self.Button_Info_Title)

        self.Frame_Info_Title_Spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.Frame_Info_Title_Spacer)


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
        self.TextBrowser_Text_Info = TextBrowserBase(self.Frame_Info_Middle)
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
        self.Splitter_Pages.addWidget(self.StackedWidget_Pages)
        self.Frame_Console = QFrame(self.Splitter_Pages)
        self.Frame_Console.setObjectName(u"Frame_Console")
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
        self.horizontalLayout_14 = QHBoxLayout(self.Frame_Console_Top)
        self.horizontalLayout_14.setSpacing(21)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(21, 0, 21, 0)
        self.Button_Console_Title = ButtonBase(self.Frame_Console_Top)
        self.Button_Console_Title.setObjectName(u"Button_Console_Title")

        self.horizontalLayout_14.addWidget(self.Button_Console_Title)

        self.horizontalSpacer = QSpacerItem(826, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.Button_Console_Copy = QPushButton(self.Frame_Console_Top)
        self.Button_Console_Copy.setObjectName(u"Button_Console_Copy")
        self.Button_Console_Copy.setMaximumSize(QSize(24, 24))
        self.Button_Console_Copy.setStyleSheet(u"QPushButton {\n"
"	image: url(:/Button_Icon/images/icons/Clipboard.png);\n"
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
"	image: url(:/Button_Icon/images/icons/TrashCan.png);\n"
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
"	image: url(:/Button_Icon/images/icons/DownArrow.png);\n"
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
        self.ScrollAreaWidgetContents_Console.setGeometry(QRect(0, 0, 1070, 187))
        self.verticalLayout_50 = QVBoxLayout(self.ScrollAreaWidgetContents_Console)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.PlainTextEdit_Console = TextEditBase(self.ScrollAreaWidgetContents_Console)
        self.PlainTextEdit_Console.setObjectName(u"PlainTextEdit_Console")

        self.verticalLayout_50.addWidget(self.PlainTextEdit_Console)

        self.ScrollArea_Console.setWidget(self.ScrollAreaWidgetContents_Console)

        self.verticalLayout_23.addWidget(self.ScrollArea_Console)

        self.Splitter_Pages.addWidget(self.Frame_Console)

        self.verticalLayout_5.addWidget(self.Splitter_Pages)


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
"	image: url(:/Button_Icon/images/icons/Console.png);\n"
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
        self.Label_ToolsStatus = LabelBase(self.Frame_Bottom_Left)
        self.Label_ToolsStatus.setObjectName(u"Label_ToolsStatus")
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
        self.Label_Usage_CPU = LabelBase(self.Frame_Bottom_Right)
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

        self.Label_Usage_GPU = LabelBase(self.Frame_Bottom_Right)
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

        self.Label_Version = LabelBase(self.Frame_Bottom_Right)
        self.Label_Version.setObjectName(u"Label_Version")
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
        self.StackedWidget_Pages_Settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
#if QT_CONFIG(tooltip)
        self.Button_Toggle_Menu.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u4ee5\u5c55\u5f00/\u6298\u53e0\u83dc\u5355", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Button_Menu_Home.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Env.setToolTip(QCoreApplication.translate("MainWindow", u"\u73af\u5883\u914d\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Env.setText(QCoreApplication.translate("MainWindow", u"\u73af\u5883", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Models.setToolTip(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7ba1\u7406", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Models.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Process.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u97f3\u9891\u5904\u7406", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Process.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_VPR.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u8bed\u97f3\u8bc6\u522b", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_VPR.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_ASR.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u8bed\u97f3\u8f6c\u6587\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_ASR.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5f55", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Dataset.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u6570\u636e\u96c6\u5236\u4f5c", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Dataset.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Train.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u6a21\u578b\u8bad\u7ec3", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Train.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_TTS.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\uff1a\u8bed\u97f3\u5408\u6210", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_TTS.setText(QCoreApplication.translate("MainWindow", u"\u5408\u6210", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Settings.setToolTip(QCoreApplication.translate("MainWindow", u"\u5ba2\u6237\u7aef\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.Button_Menu_Info.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u672c\u8f6f\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.Button_Menu_Info.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.TextBrowser_Text_Home.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:840;\">\u4ecb\u7ecd</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:420;\"><br />\u4e00\u4e2a\u57fa\u4e8eWhisper\u3001VITS\u7b49\u9879\u76ee\u5b9e\u73b0\u7684\u7b80\u6613\u8bed\u97f3\u5de5\u5177\u7bb1\uff0c\u63d0\u4f9b"
                        "\u4e86\u5305\u62ec\u8bed\u97f3\u6a21\u578b\u8bad\u7ec3\u5728\u5185\u7684\u591a\u79cd\u81ea\u52a8\u5316\u97f3\u9891\u5de5\u5177<br /><br />\u5de5\u5177\u7bb1\u76ee\u524d\u5305 \u542b\u4ee5\u4e0b\u529f\u80fd\uff1a<br />\u97f3\u9891\u5904\u7406<br />\u8bed\u97f3\u8bc6\u522b<br />\u8bed\u97f3\u8f6c\u5f55<br />\u6570\u636e\u96c6\u5236\u4f5c<br />\u6a21\u578b\u8bad\u7ec3<br />\u8bed\u97f3\u5408\u6210<br /><br />\u8fd9\u4e9b\u529f\u80fd\u5f7c\u6b64\u4e4b\u95f4\u76f8\u4e92\u72ec\u7acb\uff0c\u4f46\u53c8\u80fd\u65e0\u7f1d\u8854\u63a5\u5730\u5f62\u6210\u4e00\u5957\u5b8c\u6574\u7684\u5de5\u4f5c\u6d41<br />\u7528\u6237\u53ef\u4ee5\u6839\u636e\u81ea\u5df1\u7684\u9700\u6c42\u6709\u9009\u62e9\u6027\u5730\u4f7f\u7528\uff0c\u4ea6\u6216\u8005\u4f9d\u6b21\u901a\u8fc7\u8fd9\u4e9b\u5de5\u5177\u5c06\u672a\u7ecf\u5904\u7406\u7684\u8bed\u97f3\u6587\u4ef6\u9010\u6b65\u53d8\u4e3a\u7406\u60f3\u7684\u8bed\u97f3\u6a21\u578b<br /></span></p></body></html>", None))
        self.Label_Demo_Text.setText(QCoreApplication.translate("MainWindow", u"<font size=4>\u89c6\u9891\u6f14\u793a</font>", None))
        self.Label_Server_Text.setText(QCoreApplication.translate("MainWindow", u"<font size=4>\u4e91\u7aef\u7248\u672c</font>", None))
        self.Label_Repo_Text.setText(QCoreApplication.translate("MainWindow", u"<font size=4>\u9879\u76ee\u4ed3\u5e93</font>", None))
        self.Label_Donate_Text.setText(QCoreApplication.translate("MainWindow", u"<font size=4>\u8d5e\u52a9\u4f5c\u8005</font>", None))
        self.Button_Models_Process_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Models_VPR_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Models_ASR_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Models_TTS_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.TabWidget_Models_Process.setTabText(self.TabWidget_Models_Process.indexOf(self.Tab_Models_Process_UVR), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabWidget_Models_VPR.setTabText(self.TabWidget_Models_VPR.indexOf(self.Tab_Models_VPR_TDNN), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabWidget_Models_ASR.setTabText(self.TabWidget_Models_ASR.indexOf(self.Tab_Models_ASR_Whisper), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.TabWidget_Models_TTS.setTabText(self.TabWidget_Models_TTS.indexOf(self.Tab_Models_TTS_GPTSoVITS), QCoreApplication.translate("MainWindow", u"\u9875", None))
        self.TabWidget_Models_TTS.setTabText(self.TabWidget_Models_TTS.indexOf(self.Tab_Models_TTS_VITS), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.Button_Settings_Title_Client.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Settings_Title_Tools.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.GroupBox_Settings_Client_Outlook.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Setting_Theme.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Setting_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GroupBox_Settings_Client_Function.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_Settings_Client_Operation.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.GroupBox_Settings_Tools_Function.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Setting_AutoReset.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_AutoReset.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_Settings_Tools_Path.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Label_Process_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_VPR_TDNN_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_Whisper_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_GPTSoVITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_GPTSoVITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_OutputRoot.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Info_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Button_Console_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Label_ToolsStatus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Usage_CPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Usage_GPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        pass
    # retranslateUi