from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QDoubleSpinBox, QFrame, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPlainTextEdit, QProgressBar, QToolButton, QPushButton, QScrollArea, QSizePolicy, QSlider, QSpacerItem, QSpinBox, QStackedWidget, QTreeWidget, QTreeWidgetItem, QTextBrowser, QWidget, QTabWidget)

from .Components import Table_ViewModels, Table_EditAudioSpeaker
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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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
        self.HorizontalSpacer_Left_Top = QSpacerItem(588, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.HorizontalSpacer_Right_Top = QSpacerItem(587, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
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
        self.Label_Menu_Download_Icon = QLabel(self.Button_Menu_Download)
        self.Label_Menu_Download_Icon.setObjectName(u"Label_Menu_Download_Icon")
        self.Label_Menu_Download_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Download_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Menu_Download_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Download.png);\n"
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

        self.horizontalLayout_7.addWidget(self.Label_Menu_Download_Icon)

        self.Label_Menu_Download_Text = QLabel(self.Button_Menu_Download)
        self.Label_Menu_Download_Text.setObjectName(u"Label_Menu_Download_Text")
        sizePolicy2.setHeightForWidth(self.Label_Menu_Download_Text.sizePolicy().hasHeightForWidth())
        self.Label_Menu_Download_Text.setSizePolicy(sizePolicy2)
        self.Label_Menu_Download_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_7.addWidget(self.Label_Menu_Download_Text)


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

        self.VerticalSpacer_Menu = QSpacerItem(20, 522, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
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
        self.Label_Demo_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Demo_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Demo_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Play.png);\n"
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


        self.horizontalLayout_5.addWidget(self.Button_Demo)

        self.HorizontalSpacer_Low_Home_1 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.Label_Server_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Server_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Server_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Server.png);\n"
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


        self.horizontalLayout_5.addWidget(self.Button_Server)

        self.HorizontalSpacer_Low_Home_2 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.Label_Repo_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Repo_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Repo_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/GitHub.png);\n"
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


        self.horizontalLayout_5.addWidget(self.Button_Repo)

        self.HorizontalSpacer_Low_Home_3 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.Label_Donate_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Donate_Icon.setMaximumSize(QSize(48, 48))
        self.Label_Donate_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Heart.png);\n"
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


        self.horizontalLayout_5.addWidget(self.Button_Donate)


        self.verticalLayout_99.addWidget(self.Frame_Low_Home)

        self.StackedWidget_Pages.addWidget(self.Page_Home)
        self.Page_Download = QWidget()
        self.Page_Download.setObjectName(u"Page_Download")
        self.verticalLayout_81 = QVBoxLayout(self.Page_Download)
        self.verticalLayout_81.setSpacing(21)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(21, 12, 21, 12)
        self.Frame_Download_Top = QFrame(self.Page_Download)
        self.Frame_Download_Top.setObjectName(u"Frame_Download_Top")
        self.Frame_Download_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Download_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.Frame_Download_Top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_Download_Title = QToolButton(self.Frame_Download_Top)
        self.ToolButton_Download_Title.setObjectName(u"ToolButton_Download_Title")
        sizePolicy1.setHeightForWidth(self.ToolButton_Download_Title.sizePolicy().hasHeightForWidth())
        self.ToolButton_Download_Title.setSizePolicy(sizePolicy1)
        self.ToolButton_Download_Title.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_3.addWidget(self.ToolButton_Download_Title)

        self.Frame_Download_Title_Spacer = QLabel(self.Frame_Download_Top)
        self.Frame_Download_Title_Spacer.setObjectName(u"Frame_Download_Title_Spacer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Frame_Download_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Download_Title_Spacer.setSizePolicy(sizePolicy4)
        self.Frame_Download_Title_Spacer.setStyleSheet(u"QLabel {\n"
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

        self.horizontalLayout_3.addWidget(self.Frame_Download_Title_Spacer)


        self.verticalLayout_81.addWidget(self.Frame_Download_Top)

        self.Frame_Download_Middle = QFrame(self.Page_Download)
        self.Frame_Download_Middle.setObjectName(u"Frame_Download_Middle")
        self.Frame_Download_Middle.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 36, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.verticalLayout_134 = QVBoxLayout(self.Frame_Download_Middle)
        self.verticalLayout_134.setSpacing(0)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.Frame_Download_FFmpeg = QFrame(self.Frame_Download_Middle)
        self.Frame_Download_FFmpeg.setObjectName(u"Frame_Download_FFmpeg")
        self.Frame_Download_FFmpeg.setMinimumSize(QSize(0, 99))
        self.Frame_Download_FFmpeg.setMaximumSize(QSize(16777215, 99))
        self.Frame_Download_FFmpeg.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.Frame_Download_FFmpeg)
        self.gridLayout_2.setSpacing(12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(21, 12, 21, 12)
        self.Label_Download_FFmpeg = QLabel(self.Frame_Download_FFmpeg)
        self.Label_Download_FFmpeg.setObjectName(u"Label_Download_FFmpeg")
        self.Label_Download_FFmpeg.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_2.addWidget(self.Label_Download_FFmpeg, 0, 0, 1, 1)

        self.HorizontalSpacer_Download_FFmpeg = QSpacerItem(969, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.HorizontalSpacer_Download_FFmpeg, 0, 1, 1, 1)

        self.Button_Install_FFmpeg = QPushButton(self.Frame_Download_FFmpeg)
        self.Button_Install_FFmpeg.setObjectName(u"Button_Install_FFmpeg")
        self.Button_Install_FFmpeg.setMaximumSize(QSize(33, 33))
        self.Button_Install_FFmpeg.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url(:/Button_Icon/Sources/RepeatArrow.png);\n"
"	background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1px;\n"
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

        self.ProgressBar_Download_FFmpeg = QProgressBar(self.Frame_Download_FFmpeg)
        self.ProgressBar_Download_FFmpeg.setObjectName(u"ProgressBar_Download_FFmpeg")
        self.ProgressBar_Download_FFmpeg.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Download_FFmpeg.setStyleSheet(u"QProgressBar {\n"
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

        self.gridLayout_2.addWidget(self.ProgressBar_Download_FFmpeg, 1, 0, 1, 2)

        self.Label_Download_FFmpeg_Status = QLabel(self.Frame_Download_FFmpeg)
        self.Label_Download_FFmpeg_Status.setObjectName(u"Label_Download_FFmpeg_Status")
        self.Label_Download_FFmpeg_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_2.addWidget(self.Label_Download_FFmpeg_Status, 2, 0, 1, 1)


        self.verticalLayout_134.addWidget(self.Frame_Download_FFmpeg)

        self.Frame_Download_Python = QFrame(self.Frame_Download_Middle)
        self.Frame_Download_Python.setObjectName(u"Frame_Download_Python")
        self.Frame_Download_Python.setMinimumSize(QSize(0, 99))
        self.Frame_Download_Python.setMaximumSize(QSize(16777215, 99))
        self.Frame_Download_Python.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.Frame_Download_Python)
        self.gridLayout_3.setSpacing(12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(21, 12, 21, 12)
        self.Label_Download_Python = QLabel(self.Frame_Download_Python)
        self.Label_Download_Python.setObjectName(u"Label_Download_Python")
        self.Label_Download_Python.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_3.addWidget(self.Label_Download_Python, 0, 0, 1, 1)

        self.HorizontalSpacer_Download_Python = QSpacerItem(969, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.HorizontalSpacer_Download_Python, 0, 1, 1, 1)

        self.Button_Install_Python = QPushButton(self.Frame_Download_Python)
        self.Button_Install_Python.setObjectName(u"Button_Install_Python")
        self.Button_Install_Python.setMaximumSize(QSize(33, 33))
        self.Button_Install_Python.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url(:/Button_Icon/Sources/RepeatArrow.png);\n"
"	background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1px;\n"
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

        self.ProgressBar_Download_Python = QProgressBar(self.Frame_Download_Python)
        self.ProgressBar_Download_Python.setObjectName(u"ProgressBar_Download_Python")
        self.ProgressBar_Download_Python.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Download_Python.setStyleSheet(u"QProgressBar {\n"
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

        self.gridLayout_3.addWidget(self.ProgressBar_Download_Python, 1, 0, 1, 2)

        self.Label_Download_Python_Status = QLabel(self.Frame_Download_Python)
        self.Label_Download_Python_Status.setObjectName(u"Label_Download_Python_Status")
        self.Label_Download_Python_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_3.addWidget(self.Label_Download_Python_Status, 2, 0, 1, 1)


        self.verticalLayout_134.addWidget(self.Frame_Download_Python)

        self.Frame_Download_PyReqs = QFrame(self.Frame_Download_Middle)
        self.Frame_Download_PyReqs.setObjectName(u"Frame_Download_PyReqs")
        self.Frame_Download_PyReqs.setMinimumSize(QSize(0, 99))
        self.Frame_Download_PyReqs.setMaximumSize(QSize(16777215, 99))
        self.Frame_Download_PyReqs.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.Frame_Download_PyReqs)
        self.gridLayout_4.setSpacing(12)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(21, 12, 21, 12)
        self.Label_Download_PyReqs = QLabel(self.Frame_Download_PyReqs)
        self.Label_Download_PyReqs.setObjectName(u"Label_Download_PyReqs")
        self.Label_Download_PyReqs.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_4.addWidget(self.Label_Download_PyReqs, 0, 0, 1, 1)

        self.HorizontalSpacer_Download_PyReqs = QSpacerItem(969, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.HorizontalSpacer_Download_PyReqs, 0, 1, 1, 1)

        self.Button_Install_PyReqs = QPushButton(self.Frame_Download_PyReqs)
        self.Button_Install_PyReqs.setObjectName(u"Button_Install_PyReqs")
        self.Button_Install_PyReqs.setMaximumSize(QSize(33, 33))
        self.Button_Install_PyReqs.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url(:/Button_Icon/Sources/RepeatArrow.png);\n"
"	background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1px;\n"
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

        self.ProgressBar_Download_PyReqs = QProgressBar(self.Frame_Download_PyReqs)
        self.ProgressBar_Download_PyReqs.setObjectName(u"ProgressBar_Download_PyReqs")
        self.ProgressBar_Download_PyReqs.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Download_PyReqs.setStyleSheet(u"QProgressBar {\n"
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

        self.gridLayout_4.addWidget(self.ProgressBar_Download_PyReqs, 1, 0, 1, 2)

        self.Label_Download_PyReqs_Status = QLabel(self.Frame_Download_PyReqs)
        self.Label_Download_PyReqs_Status.setObjectName(u"Label_Download_PyReqs_Status")
        self.Label_Download_PyReqs_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_4.addWidget(self.Label_Download_PyReqs_Status, 2, 0, 1, 1)


        self.verticalLayout_134.addWidget(self.Frame_Download_PyReqs)

        self.Frame_Download_Pytorch = QFrame(self.Frame_Download_Middle)
        self.Frame_Download_Pytorch.setObjectName(u"Frame_Download_Pytorch")
        self.Frame_Download_Pytorch.setMinimumSize(QSize(0, 99))
        self.Frame_Download_Pytorch.setMaximumSize(QSize(16777215, 99))
        self.Frame_Download_Pytorch.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.gridLayout_5 = QGridLayout(self.Frame_Download_Pytorch)
        self.gridLayout_5.setSpacing(12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(21, 12, 21, 12)
        self.Label_Download_Pytorch = QLabel(self.Frame_Download_Pytorch)
        self.Label_Download_Pytorch.setObjectName(u"Label_Download_Pytorch")
        self.Label_Download_Pytorch.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_5.addWidget(self.Label_Download_Pytorch, 0, 0, 1, 1)

        self.HorizontalSpacer_Download_Pytorch = QSpacerItem(969, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.HorizontalSpacer_Download_Pytorch, 0, 1, 1, 1)

        self.Button_Install_Pytorch = QPushButton(self.Frame_Download_Pytorch)
        self.Button_Install_Pytorch.setObjectName(u"Button_Install_Pytorch")
        self.Button_Install_Pytorch.setMaximumSize(QSize(33, 33))
        self.Button_Install_Pytorch.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url(:/Button_Icon/Sources/RepeatArrow.png);\n"
"	background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: center;\n"
"	background-color: transparent;\n"
"	padding: 4.5px;\n"
"	border-width: 1px;\n"
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

        self.ProgressBar_Download_Pytorch = QProgressBar(self.Frame_Download_Pytorch)
        self.ProgressBar_Download_Pytorch.setObjectName(u"ProgressBar_Download_Pytorch")
        self.ProgressBar_Download_Pytorch.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Download_Pytorch.setStyleSheet(u"QProgressBar {\n"
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

        self.gridLayout_5.addWidget(self.ProgressBar_Download_Pytorch, 1, 0, 1, 2)

        self.Label_Download_Pytorch_Status = QLabel(self.Frame_Download_Pytorch)
        self.Label_Download_Pytorch_Status.setObjectName(u"Label_Download_Pytorch_Status")
        self.Label_Download_Pytorch_Status.setStyleSheet(u"QLabel {\n"
"	font-size: 9.9px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_5.addWidget(self.Label_Download_Pytorch_Status, 2, 0, 1, 1)


        self.verticalLayout_134.addWidget(self.Frame_Download_Pytorch)


        self.verticalLayout_81.addWidget(self.Frame_Download_Middle)

        self.VerticalSpacer_Download = QSpacerItem(17, 198, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        self.verticalLayout_27.setSpacing(3)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 3, 0, 3)
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
        self.verticalLayout_46.setSpacing(3)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 3, 0, 3)
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
        self.verticalLayout_38.setSpacing(3)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 3, 0, 3)
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
        self.Widget_Left_Process.setMaximumSize(QSize(210, 16777215))
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
        self.TreeWidget_Catalogue_Process.setStyleSheet(u"QTreeWidget {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"	background-color: transparent;\n"
"	padding: 1.2px;\n"
"}\n"
"\n"
"QTreeWidget::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeWidget::branch:open:has-children:has-siblings,\n"
"QTreeWidget::branch:open:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:closed:has-children:has-siblings,\n"
"QTreeWidget::branch:closed:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:!has-children:has-siblings:adjoins-item,\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    image: ;\n"
"}\n"
"\n"
"\n"
"QTreeView {\n"
"}\n"
"\n"
"QTreeView::item{\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
""
                        "QTreeView::item:selected:active{\n"
"    background-color: ;\n"
"}\n"
"QTreeView::item:selected:!active {\n"
"    background-color: ;\n"
"}\n"
"\n"
"/*\n"
"QHeaderView {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QHeaderView:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: transparent;\n"
"}\n"
"QHeaderView::section:checked {\n"
"	background-color: ;\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}*/\n"
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
"	background-color: rgba(33, 3"
                        "3, 33, 99);\n"
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
"	border"
                        "-radius: 6px;\n"
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
"	backgro"
                        "und-color: rgb(120, 120, 120);\n"
"}")

        self.verticalLayout_162.addWidget(self.TreeWidget_Catalogue_Process)


        self.gridLayout_6.addWidget(self.Widget_Left_Process, 0, 0, 1, 1)

        self.ScrollArea_Middle_Process = QScrollArea(self.Subpage_Process)
        self.ScrollArea_Middle_Process.setObjectName(u"ScrollArea_Middle_Process")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ScrollArea_Middle_Process.sizePolicy().hasHeightForWidth())
        self.ScrollArea_Middle_Process.setSizePolicy(sizePolicy5)
        self.ScrollArea_Middle_Process.setMinimumSize(QSize(630, 0))
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
        self.ScrollArea_Middle_WidgetContents_Process.setGeometry(QRect(0, 0, 621, 1384))
        self.verticalLayout_14 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_Process)
        self.verticalLayout_14.setSpacing(12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_Process = QGroupBox(self.ScrollArea_Middle_WidgetContents_Process)
        self.GroupBox_EssentialParams_Process.setObjectName(u"GroupBox_EssentialParams_Process")
        self.GroupBox_EssentialParams_Process.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_150 = QVBoxLayout(self.GroupBox_EssentialParams_Process)
        self.verticalLayout_150.setSpacing(0)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_Process = QCheckBox(self.GroupBox_EssentialParams_Process)
        self.CheckBox_Toggle_BasicSettings_Process.setObjectName(u"CheckBox_Toggle_BasicSettings_Process")
        self.CheckBox_Toggle_BasicSettings_Process.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_150.addWidget(self.CheckBox_Toggle_BasicSettings_Process)

        self.Frame_BasicSettings_Process = QFrame(self.GroupBox_EssentialParams_Process)
        self.Frame_BasicSettings_Process.setObjectName(u"Frame_BasicSettings_Process")
        self.verticalLayout_20 = QVBoxLayout(self.Frame_BasicSettings_Process)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.Frame_Process_Media_Dir_Input = QFrame(self.Frame_BasicSettings_Process)
        self.Frame_Process_Media_Dir_Input.setObjectName(u"Frame_Process_Media_Dir_Input")
        self.Frame_Process_Media_Dir_Input.setMinimumSize(QSize(0, 105))
        self.Frame_Process_Media_Dir_Input.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_152 = QVBoxLayout(self.Frame_Process_Media_Dir_Input)
        self.verticalLayout_152.setSpacing(12)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.verticalLayout_152.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_Media_Dir_Input = QLabel(self.Frame_Process_Media_Dir_Input)
        self.Label_Process_Media_Dir_Input.setObjectName(u"Label_Process_Media_Dir_Input")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Label_Process_Media_Dir_Input.sizePolicy().hasHeightForWidth())
        self.Label_Process_Media_Dir_Input.setSizePolicy(sizePolicy6)
        self.Label_Process_Media_Dir_Input.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_152.addWidget(self.Label_Process_Media_Dir_Input)

        self.ChildFrame_Process_Media_Dir_Input = QFrame(self.Frame_Process_Media_Dir_Input)
        self.ChildFrame_Process_Media_Dir_Input.setObjectName(u"ChildFrame_Process_Media_Dir_Input")
        sizePolicy6.setHeightForWidth(self.ChildFrame_Process_Media_Dir_Input.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Process_Media_Dir_Input.setSizePolicy(sizePolicy6)
        self.ChildFrame_Process_Media_Dir_Input.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_77 = QHBoxLayout(self.ChildFrame_Process_Media_Dir_Input)
        self.horizontalLayout_77.setSpacing(12)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Process_Media_Dir_Input = QLineEdit(self.ChildFrame_Process_Media_Dir_Input)
        self.LineEdit_Process_Media_Dir_Input.setObjectName(u"LineEdit_Process_Media_Dir_Input")
        self.LineEdit_Process_Media_Dir_Input.setMinimumSize(QSize(0, 27))
        self.LineEdit_Process_Media_Dir_Input.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_77.addWidget(self.LineEdit_Process_Media_Dir_Input)

        self.Button_Process_Media_Dir_Input = QPushButton(self.ChildFrame_Process_Media_Dir_Input)
        self.Button_Process_Media_Dir_Input.setObjectName(u"Button_Process_Media_Dir_Input")
        self.Button_Process_Media_Dir_Input.setMinimumSize(QSize(27, 27))
        self.Button_Process_Media_Dir_Input.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_77.addWidget(self.Button_Process_Media_Dir_Input)


        self.verticalLayout_152.addWidget(self.ChildFrame_Process_Media_Dir_Input)


        self.verticalLayout_20.addWidget(self.Frame_Process_Media_Dir_Input)

        self.Frame_Process_Media_Format_Output = QFrame(self.Frame_BasicSettings_Process)
        self.Frame_Process_Media_Format_Output.setObjectName(u"Frame_Process_Media_Format_Output")
        self.Frame_Process_Media_Format_Output.setMinimumSize(QSize(0, 105))
        self.Frame_Process_Media_Format_Output.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_153 = QVBoxLayout(self.Frame_Process_Media_Format_Output)
        self.verticalLayout_153.setSpacing(12)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.verticalLayout_153.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_Media_Format_Output = QLabel(self.Frame_Process_Media_Format_Output)
        self.Label_Process_Media_Format_Output.setObjectName(u"Label_Process_Media_Format_Output")
        sizePolicy6.setHeightForWidth(self.Label_Process_Media_Format_Output.sizePolicy().hasHeightForWidth())
        self.Label_Process_Media_Format_Output.setSizePolicy(sizePolicy6)
        self.Label_Process_Media_Format_Output.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_153.addWidget(self.Label_Process_Media_Format_Output)

        self.ComboBox_Process_Media_Format_Output = QComboBox(self.Frame_Process_Media_Format_Output)
        self.ComboBox_Process_Media_Format_Output.setObjectName(u"ComboBox_Process_Media_Format_Output")
        self.ComboBox_Process_Media_Format_Output.setMinimumSize(QSize(0, 27))
        self.ComboBox_Process_Media_Format_Output.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
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
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding-left: -15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemV"
                        "iew::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-left: 15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120. 120, 120, 120)\n"
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
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
""
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
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:"
                        "hover {\n"
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
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScro"
                        "llArea QScrollBar::handle:horizontal:hover {\n"
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

        self.verticalLayout_153.addWidget(self.ComboBox_Process_Media_Format_Output)


        self.verticalLayout_20.addWidget(self.Frame_Process_Media_Format_Output)

        self.Frame_Process_Slice_Audio = QFrame(self.Frame_BasicSettings_Process)
        self.Frame_Process_Slice_Audio.setObjectName(u"Frame_Process_Slice_Audio")
        self.Frame_Process_Slice_Audio.setMinimumSize(QSize(0, 105))
        self.Frame_Process_Slice_Audio.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_120 = QVBoxLayout(self.Frame_Process_Slice_Audio)
        self.verticalLayout_120.setSpacing(12)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_Slice_Audio = QLabel(self.Frame_Process_Slice_Audio)
        self.Label_Process_Slice_Audio.setObjectName(u"Label_Process_Slice_Audio")
        sizePolicy6.setHeightForWidth(self.Label_Process_Slice_Audio.sizePolicy().hasHeightForWidth())
        self.Label_Process_Slice_Audio.setSizePolicy(sizePolicy6)
        self.Label_Process_Slice_Audio.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_120.addWidget(self.Label_Process_Slice_Audio)

        self.CheckBox_Process_Slice_Audio = QCheckBox(self.Frame_Process_Slice_Audio)
        self.CheckBox_Process_Slice_Audio.setObjectName(u"CheckBox_Process_Slice_Audio")
        self.CheckBox_Process_Slice_Audio.setMinimumSize(QSize(0, 27))
        self.CheckBox_Process_Slice_Audio.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_120.addWidget(self.CheckBox_Process_Slice_Audio)


        self.verticalLayout_20.addWidget(self.Frame_Process_Slice_Audio)

        self.Frame_Process_Media_Dir_Output = QFrame(self.Frame_BasicSettings_Process)
        self.Frame_Process_Media_Dir_Output.setObjectName(u"Frame_Process_Media_Dir_Output")
        self.Frame_Process_Media_Dir_Output.setMinimumSize(QSize(0, 105))
        self.Frame_Process_Media_Dir_Output.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_154 = QVBoxLayout(self.Frame_Process_Media_Dir_Output)
        self.verticalLayout_154.setSpacing(12)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_Media_Dir_Output = QLabel(self.Frame_Process_Media_Dir_Output)
        self.Label_Process_Media_Dir_Output.setObjectName(u"Label_Process_Media_Dir_Output")
        sizePolicy6.setHeightForWidth(self.Label_Process_Media_Dir_Output.sizePolicy().hasHeightForWidth())
        self.Label_Process_Media_Dir_Output.setSizePolicy(sizePolicy6)
        self.Label_Process_Media_Dir_Output.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_154.addWidget(self.Label_Process_Media_Dir_Output)

        self.ChildFrame_Process_Media_Dir_Output = QFrame(self.Frame_Process_Media_Dir_Output)
        self.ChildFrame_Process_Media_Dir_Output.setObjectName(u"ChildFrame_Process_Media_Dir_Output")
        sizePolicy6.setHeightForWidth(self.ChildFrame_Process_Media_Dir_Output.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Process_Media_Dir_Output.setSizePolicy(sizePolicy6)
        self.ChildFrame_Process_Media_Dir_Output.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_78 = QHBoxLayout(self.ChildFrame_Process_Media_Dir_Output)
        self.horizontalLayout_78.setSpacing(12)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Process_Media_Dir_Output = QLineEdit(self.ChildFrame_Process_Media_Dir_Output)
        self.LineEdit_Process_Media_Dir_Output.setObjectName(u"LineEdit_Process_Media_Dir_Output")
        self.LineEdit_Process_Media_Dir_Output.setMinimumSize(QSize(0, 27))
        self.LineEdit_Process_Media_Dir_Output.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_78.addWidget(self.LineEdit_Process_Media_Dir_Output)

        self.Button_Process_Media_Dir_Output = QPushButton(self.ChildFrame_Process_Media_Dir_Output)
        self.Button_Process_Media_Dir_Output.setObjectName(u"Button_Process_Media_Dir_Output")
        self.Button_Process_Media_Dir_Output.setMinimumSize(QSize(27, 27))
        self.Button_Process_Media_Dir_Output.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_78.addWidget(self.Button_Process_Media_Dir_Output)


        self.verticalLayout_154.addWidget(self.ChildFrame_Process_Media_Dir_Output)


        self.verticalLayout_20.addWidget(self.Frame_Process_Media_Dir_Output)


        self.verticalLayout_150.addWidget(self.Frame_BasicSettings_Process)

        self.CheckBox_Toggle_AdvanceSettings_Process = QCheckBox(self.GroupBox_EssentialParams_Process)
        self.CheckBox_Toggle_AdvanceSettings_Process.setObjectName(u"CheckBox_Toggle_AdvanceSettings_Process")
        self.CheckBox_Toggle_AdvanceSettings_Process.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_150.addWidget(self.CheckBox_Toggle_AdvanceSettings_Process)

        self.Frame_AdvanceSettings_Process = QFrame(self.GroupBox_EssentialParams_Process)
        self.Frame_AdvanceSettings_Process.setObjectName(u"Frame_AdvanceSettings_Process")
        self.verticalLayout_21 = QVBoxLayout(self.Frame_AdvanceSettings_Process)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Frame_Process_RMS_Threshold = QFrame(self.Frame_AdvanceSettings_Process)
        self.Frame_Process_RMS_Threshold.setObjectName(u"Frame_Process_RMS_Threshold")
        self.Frame_Process_RMS_Threshold.setMinimumSize(QSize(0, 105))
        self.Frame_Process_RMS_Threshold.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_156 = QVBoxLayout(self.Frame_Process_RMS_Threshold)
        self.verticalLayout_156.setSpacing(12)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_RMS_Threshold = QLabel(self.Frame_Process_RMS_Threshold)
        self.Label_Process_RMS_Threshold.setObjectName(u"Label_Process_RMS_Threshold")
        sizePolicy6.setHeightForWidth(self.Label_Process_RMS_Threshold.sizePolicy().hasHeightForWidth())
        self.Label_Process_RMS_Threshold.setSizePolicy(sizePolicy6)
        self.Label_Process_RMS_Threshold.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_156.addWidget(self.Label_Process_RMS_Threshold)

        self.DoubleSpinBox_Process_RMS_Threshold = QDoubleSpinBox(self.Frame_Process_RMS_Threshold)
        self.DoubleSpinBox_Process_RMS_Threshold.setObjectName(u"DoubleSpinBox_Process_RMS_Threshold")
        self.DoubleSpinBox_Process_RMS_Threshold.setEnabled(True)
        self.DoubleSpinBox_Process_RMS_Threshold.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_Process_RMS_Threshold.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.DoubleSpinBox_Process_RMS_Threshold.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_Process_RMS_Threshold.setMaximum(999999.000000000000000)

        self.verticalLayout_156.addWidget(self.DoubleSpinBox_Process_RMS_Threshold)


        self.verticalLayout_21.addWidget(self.Frame_Process_RMS_Threshold)

        self.Frame_Process_Audio_Length_Min = QFrame(self.Frame_AdvanceSettings_Process)
        self.Frame_Process_Audio_Length_Min.setObjectName(u"Frame_Process_Audio_Length_Min")
        self.Frame_Process_Audio_Length_Min.setMinimumSize(QSize(0, 105))
        self.Frame_Process_Audio_Length_Min.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_157 = QVBoxLayout(self.Frame_Process_Audio_Length_Min)
        self.verticalLayout_157.setSpacing(12)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalLayout_157.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_Audio_Length_Min = QLabel(self.Frame_Process_Audio_Length_Min)
        self.Label_Process_Audio_Length_Min.setObjectName(u"Label_Process_Audio_Length_Min")
        sizePolicy6.setHeightForWidth(self.Label_Process_Audio_Length_Min.sizePolicy().hasHeightForWidth())
        self.Label_Process_Audio_Length_Min.setSizePolicy(sizePolicy6)
        self.Label_Process_Audio_Length_Min.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_157.addWidget(self.Label_Process_Audio_Length_Min)

        self.SpinBox_Process_Audio_Length_Min = QSpinBox(self.Frame_Process_Audio_Length_Min)
        self.SpinBox_Process_Audio_Length_Min.setObjectName(u"SpinBox_Process_Audio_Length_Min")
        self.SpinBox_Process_Audio_Length_Min.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_Audio_Length_Min.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Process_Audio_Length_Min.setMinimum(-999999)
        self.SpinBox_Process_Audio_Length_Min.setMaximum(999999)

        self.verticalLayout_157.addWidget(self.SpinBox_Process_Audio_Length_Min)


        self.verticalLayout_21.addWidget(self.Frame_Process_Audio_Length_Min)

        self.Frame_Process_Silent_Interval_Min = QFrame(self.Frame_AdvanceSettings_Process)
        self.Frame_Process_Silent_Interval_Min.setObjectName(u"Frame_Process_Silent_Interval_Min")
        self.Frame_Process_Silent_Interval_Min.setMinimumSize(QSize(0, 105))
        self.Frame_Process_Silent_Interval_Min.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_158 = QVBoxLayout(self.Frame_Process_Silent_Interval_Min)
        self.verticalLayout_158.setSpacing(12)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_Silent_Interval_Min = QLabel(self.Frame_Process_Silent_Interval_Min)
        self.Label_Process_Silent_Interval_Min.setObjectName(u"Label_Process_Silent_Interval_Min")
        sizePolicy6.setHeightForWidth(self.Label_Process_Silent_Interval_Min.sizePolicy().hasHeightForWidth())
        self.Label_Process_Silent_Interval_Min.setSizePolicy(sizePolicy6)
        self.Label_Process_Silent_Interval_Min.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_158.addWidget(self.Label_Process_Silent_Interval_Min)

        self.SpinBox_Process_Silent_Interval_Min = QSpinBox(self.Frame_Process_Silent_Interval_Min)
        self.SpinBox_Process_Silent_Interval_Min.setObjectName(u"SpinBox_Process_Silent_Interval_Min")
        self.SpinBox_Process_Silent_Interval_Min.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_Silent_Interval_Min.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Process_Silent_Interval_Min.setMinimum(-999999)
        self.SpinBox_Process_Silent_Interval_Min.setMaximum(999999)

        self.verticalLayout_158.addWidget(self.SpinBox_Process_Silent_Interval_Min)


        self.verticalLayout_21.addWidget(self.Frame_Process_Silent_Interval_Min)

        self.Frame_Process_Hop_Size = QFrame(self.Frame_AdvanceSettings_Process)
        self.Frame_Process_Hop_Size.setObjectName(u"Frame_Process_Hop_Size")
        self.Frame_Process_Hop_Size.setMinimumSize(QSize(0, 105))
        self.Frame_Process_Hop_Size.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_159 = QVBoxLayout(self.Frame_Process_Hop_Size)
        self.verticalLayout_159.setSpacing(12)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.verticalLayout_159.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_Hop_Size = QLabel(self.Frame_Process_Hop_Size)
        self.Label_Process_Hop_Size.setObjectName(u"Label_Process_Hop_Size")
        sizePolicy6.setHeightForWidth(self.Label_Process_Hop_Size.sizePolicy().hasHeightForWidth())
        self.Label_Process_Hop_Size.setSizePolicy(sizePolicy6)
        self.Label_Process_Hop_Size.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_159.addWidget(self.Label_Process_Hop_Size)

        self.SpinBox_Process_Hop_Size = QSpinBox(self.Frame_Process_Hop_Size)
        self.SpinBox_Process_Hop_Size.setObjectName(u"SpinBox_Process_Hop_Size")
        self.SpinBox_Process_Hop_Size.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_Hop_Size.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Process_Hop_Size.setMinimum(-999999)
        self.SpinBox_Process_Hop_Size.setMaximum(999999)

        self.verticalLayout_159.addWidget(self.SpinBox_Process_Hop_Size)


        self.verticalLayout_21.addWidget(self.Frame_Process_Hop_Size)

        self.Frame_Process_Silence_Kept_Max = QFrame(self.Frame_AdvanceSettings_Process)
        self.Frame_Process_Silence_Kept_Max.setObjectName(u"Frame_Process_Silence_Kept_Max")
        self.Frame_Process_Silence_Kept_Max.setMinimumSize(QSize(0, 105))
        self.Frame_Process_Silence_Kept_Max.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_160 = QVBoxLayout(self.Frame_Process_Silence_Kept_Max)
        self.verticalLayout_160.setSpacing(12)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.verticalLayout_160.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_Silence_Kept_Max = QLabel(self.Frame_Process_Silence_Kept_Max)
        self.Label_Process_Silence_Kept_Max.setObjectName(u"Label_Process_Silence_Kept_Max")
        sizePolicy6.setHeightForWidth(self.Label_Process_Silence_Kept_Max.sizePolicy().hasHeightForWidth())
        self.Label_Process_Silence_Kept_Max.setSizePolicy(sizePolicy6)
        self.Label_Process_Silence_Kept_Max.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_160.addWidget(self.Label_Process_Silence_Kept_Max)

        self.SpinBox_Process_Silence_Kept_Max = QSpinBox(self.Frame_Process_Silence_Kept_Max)
        self.SpinBox_Process_Silence_Kept_Max.setObjectName(u"SpinBox_Process_Silence_Kept_Max")
        self.SpinBox_Process_Silence_Kept_Max.setMinimumSize(QSize(0, 27))
        self.SpinBox_Process_Silence_Kept_Max.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Process_Silence_Kept_Max.setMinimum(-999999)
        self.SpinBox_Process_Silence_Kept_Max.setMaximum(999999)

        self.verticalLayout_160.addWidget(self.SpinBox_Process_Silence_Kept_Max)


        self.verticalLayout_21.addWidget(self.Frame_Process_Silence_Kept_Max)

        self.Frame_Process_SampleRate = QFrame(self.Frame_AdvanceSettings_Process)
        self.Frame_Process_SampleRate.setObjectName(u"Frame_Process_SampleRate")
        self.Frame_Process_SampleRate.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SampleRate.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_161 = QVBoxLayout(self.Frame_Process_SampleRate)
        self.verticalLayout_161.setSpacing(12)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_SampleRate = QLabel(self.Frame_Process_SampleRate)
        self.Label_Process_SampleRate.setObjectName(u"Label_Process_SampleRate")
        sizePolicy6.setHeightForWidth(self.Label_Process_SampleRate.sizePolicy().hasHeightForWidth())
        self.Label_Process_SampleRate.setSizePolicy(sizePolicy6)
        self.Label_Process_SampleRate.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_161.addWidget(self.Label_Process_SampleRate)

        self.ComboBox_Process_SampleRate = QComboBox(self.Frame_Process_SampleRate)
        self.ComboBox_Process_SampleRate.setObjectName(u"ComboBox_Process_SampleRate")
        self.ComboBox_Process_SampleRate.setMinimumSize(QSize(0, 27))
        self.ComboBox_Process_SampleRate.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
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
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding-left: -15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemV"
                        "iew::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-left: 15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120. 120, 120, 120)\n"
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
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
""
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
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:"
                        "hover {\n"
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
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScro"
                        "llArea QScrollBar::handle:horizontal:hover {\n"
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

        self.verticalLayout_161.addWidget(self.ComboBox_Process_SampleRate)


        self.verticalLayout_21.addWidget(self.Frame_Process_SampleRate)

        self.Frame_Process_SampleWidth = QFrame(self.Frame_AdvanceSettings_Process)
        self.Frame_Process_SampleWidth.setObjectName(u"Frame_Process_SampleWidth")
        self.Frame_Process_SampleWidth.setMinimumSize(QSize(0, 105))
        self.Frame_Process_SampleWidth.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_163 = QVBoxLayout(self.Frame_Process_SampleWidth)
        self.verticalLayout_163.setSpacing(12)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_SampleWidth = QLabel(self.Frame_Process_SampleWidth)
        self.Label_Process_SampleWidth.setObjectName(u"Label_Process_SampleWidth")
        sizePolicy6.setHeightForWidth(self.Label_Process_SampleWidth.sizePolicy().hasHeightForWidth())
        self.Label_Process_SampleWidth.setSizePolicy(sizePolicy6)
        self.Label_Process_SampleWidth.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_163.addWidget(self.Label_Process_SampleWidth)

        self.ComboBox_Process_SampleWidth = QComboBox(self.Frame_Process_SampleWidth)
        self.ComboBox_Process_SampleWidth.setObjectName(u"ComboBox_Process_SampleWidth")
        self.ComboBox_Process_SampleWidth.setMinimumSize(QSize(0, 27))
        self.ComboBox_Process_SampleWidth.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
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
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding-left: -15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemV"
                        "iew::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-left: 15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120. 120, 120, 120)\n"
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
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
""
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
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:"
                        "hover {\n"
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
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScro"
                        "llArea QScrollBar::handle:horizontal:hover {\n"
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

        self.verticalLayout_163.addWidget(self.ComboBox_Process_SampleWidth)


        self.verticalLayout_21.addWidget(self.Frame_Process_SampleWidth)

        self.Frame_Process_ToMono = QFrame(self.Frame_AdvanceSettings_Process)
        self.Frame_Process_ToMono.setObjectName(u"Frame_Process_ToMono")
        self.Frame_Process_ToMono.setMinimumSize(QSize(0, 105))
        self.Frame_Process_ToMono.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_123 = QVBoxLayout(self.Frame_Process_ToMono)
        self.verticalLayout_123.setSpacing(12)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(21, 12, 21, 12)
        self.Label_Process_ToMono = QLabel(self.Frame_Process_ToMono)
        self.Label_Process_ToMono.setObjectName(u"Label_Process_ToMono")
        sizePolicy6.setHeightForWidth(self.Label_Process_ToMono.sizePolicy().hasHeightForWidth())
        self.Label_Process_ToMono.setSizePolicy(sizePolicy6)
        self.Label_Process_ToMono.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_123.addWidget(self.Label_Process_ToMono)

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

        self.verticalLayout_123.addWidget(self.CheckBox_Process_ToMono)


        self.verticalLayout_21.addWidget(self.Frame_Process_ToMono)


        self.verticalLayout_150.addWidget(self.Frame_AdvanceSettings_Process)


        self.verticalLayout_14.addWidget(self.GroupBox_EssentialParams_Process)

        self.VerticalSpacer_Process = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.VerticalSpacer_Process)

        self.ScrollArea_Middle_Process.setWidget(self.ScrollArea_Middle_WidgetContents_Process)

        self.gridLayout_6.addWidget(self.ScrollArea_Middle_Process, 0, 1, 1, 1)

        self.Widget_Right_Process = QWidget(self.Subpage_Process)
        self.Widget_Right_Process.setObjectName(u"Widget_Right_Process")
        self.Widget_Right_Process.setMinimumSize(QSize(210, 0))
        self.Widget_Right_Process.setMaximumSize(QSize(420, 16777215))
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
"	background-color: rgb(33, 33, 33);\n"
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
"	border-st"
                        "yle: solid;\n"
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
"	width: 0px;\n"
""
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
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Button_Process_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Process_Execute.setSizePolicy(sizePolicy7)
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
        sizePolicy7.setHeightForWidth(self.Button_Process_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Process_Terminate.setSizePolicy(sizePolicy7)
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
        self.Widget_Left_ASR_VPR.setMaximumSize(QSize(210, 16777215))
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
        self.TreeWidget_Catalogue_ASR_VPR.setStyleSheet(u"QTreeWidget {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"	background-color: transparent;\n"
"	padding: 1.2px;\n"
"}\n"
"\n"
"QTreeWidget::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeWidget::branch:open:has-children:has-siblings,\n"
"QTreeWidget::branch:open:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:closed:has-children:has-siblings,\n"
"QTreeWidget::branch:closed:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:!has-children:has-siblings:adjoins-item,\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    image: ;\n"
"}\n"
"\n"
"\n"
"QTreeView {\n"
"}\n"
"\n"
"QTreeView::item{\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
""
                        "QTreeView::item:selected:active{\n"
"    background-color: ;\n"
"}\n"
"QTreeView::item:selected:!active {\n"
"    background-color: ;\n"
"}\n"
"\n"
"/*\n"
"QHeaderView {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QHeaderView:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: transparent;\n"
"}\n"
"QHeaderView::section:checked {\n"
"	background-color: ;\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}*/\n"
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
"	background-color: rgba(33, 3"
                        "3, 33, 99);\n"
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
"	border"
                        "-radius: 6px;\n"
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
"	backgro"
                        "und-color: rgb(120, 120, 120);\n"
"}")

        self.verticalLayout_4.addWidget(self.TreeWidget_Catalogue_ASR_VPR)


        self.gridLayout_21.addWidget(self.Widget_Left_ASR_VPR, 0, 0, 1, 1)

        self.ScrollArea_Middle_ASR_VPR = QScrollArea(self.Subpage_ASR_VPR)
        self.ScrollArea_Middle_ASR_VPR.setObjectName(u"ScrollArea_Middle_ASR_VPR")
        sizePolicy5.setHeightForWidth(self.ScrollArea_Middle_ASR_VPR.sizePolicy().hasHeightForWidth())
        self.ScrollArea_Middle_ASR_VPR.setSizePolicy(sizePolicy5)
        self.ScrollArea_Middle_ASR_VPR.setMinimumSize(QSize(630, 0))
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
        self.ScrollArea_Middle_WidgetContents_ASR_VPR.setGeometry(QRect(0, 0, 621, 1081))
        self.verticalLayout_15 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_ASR_VPR)
        self.verticalLayout_15.setSpacing(12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_ASR_VPR = QGroupBox(self.ScrollArea_Middle_WidgetContents_ASR_VPR)
        self.GroupBox_EssentialParams_ASR_VPR.setObjectName(u"GroupBox_EssentialParams_ASR_VPR")
        self.GroupBox_EssentialParams_ASR_VPR.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_33 = QVBoxLayout(self.GroupBox_EssentialParams_ASR_VPR)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_ASR_VPR = QCheckBox(self.GroupBox_EssentialParams_ASR_VPR)
        self.CheckBox_Toggle_BasicSettings_ASR_VPR.setObjectName(u"CheckBox_Toggle_BasicSettings_ASR_VPR")
        self.CheckBox_Toggle_BasicSettings_ASR_VPR.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_33.addWidget(self.CheckBox_Toggle_BasicSettings_ASR_VPR)

        self.Frame_BasicSettings_ASR_VPR = QFrame(self.GroupBox_EssentialParams_ASR_VPR)
        self.Frame_BasicSettings_ASR_VPR.setObjectName(u"Frame_BasicSettings_ASR_VPR")
        self.verticalLayout_137 = QVBoxLayout(self.Frame_BasicSettings_ASR_VPR)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_VPR_Audio_Dir_Input = QFrame(self.Frame_BasicSettings_ASR_VPR)
        self.Frame_ASR_VPR_Audio_Dir_Input.setObjectName(u"Frame_ASR_VPR_Audio_Dir_Input")
        self.Frame_ASR_VPR_Audio_Dir_Input.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_Audio_Dir_Input.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_121 = QVBoxLayout(self.Frame_ASR_VPR_Audio_Dir_Input)
        self.verticalLayout_121.setSpacing(12)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_Audio_Dir_Input = QLabel(self.Frame_ASR_VPR_Audio_Dir_Input)
        self.Label_ASR_VPR_Audio_Dir_Input.setObjectName(u"Label_ASR_VPR_Audio_Dir_Input")
        sizePolicy6.setHeightForWidth(self.Label_ASR_VPR_Audio_Dir_Input.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_Audio_Dir_Input.setSizePolicy(sizePolicy6)
        self.Label_ASR_VPR_Audio_Dir_Input.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_121.addWidget(self.Label_ASR_VPR_Audio_Dir_Input)

        self.ChildFrame_ASR_VPR_Audio_Dir_Input = QFrame(self.Frame_ASR_VPR_Audio_Dir_Input)
        self.ChildFrame_ASR_VPR_Audio_Dir_Input.setObjectName(u"ChildFrame_ASR_VPR_Audio_Dir_Input")
        sizePolicy6.setHeightForWidth(self.ChildFrame_ASR_VPR_Audio_Dir_Input.sizePolicy().hasHeightForWidth())
        self.ChildFrame_ASR_VPR_Audio_Dir_Input.setSizePolicy(sizePolicy6)
        self.ChildFrame_ASR_VPR_Audio_Dir_Input.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_31 = QHBoxLayout(self.ChildFrame_ASR_VPR_Audio_Dir_Input)
        self.horizontalLayout_31.setSpacing(12)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_ASR_VPR_Audio_Dir_Input = QLineEdit(self.ChildFrame_ASR_VPR_Audio_Dir_Input)
        self.LineEdit_ASR_VPR_Audio_Dir_Input.setObjectName(u"LineEdit_ASR_VPR_Audio_Dir_Input")
        self.LineEdit_ASR_VPR_Audio_Dir_Input.setMinimumSize(QSize(0, 27))
        self.LineEdit_ASR_VPR_Audio_Dir_Input.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_31.addWidget(self.LineEdit_ASR_VPR_Audio_Dir_Input)

        self.Button_ASR_VPR_Audio_Dir_Input = QPushButton(self.ChildFrame_ASR_VPR_Audio_Dir_Input)
        self.Button_ASR_VPR_Audio_Dir_Input.setObjectName(u"Button_ASR_VPR_Audio_Dir_Input")
        self.Button_ASR_VPR_Audio_Dir_Input.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_Audio_Dir_Input.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_31.addWidget(self.Button_ASR_VPR_Audio_Dir_Input)


        self.verticalLayout_121.addWidget(self.ChildFrame_ASR_VPR_Audio_Dir_Input)


        self.verticalLayout_137.addWidget(self.Frame_ASR_VPR_Audio_Dir_Input)

        self.Frame_ASR_VPR_StdAudioSpeaker = QFrame(self.Frame_BasicSettings_ASR_VPR)
        self.Frame_ASR_VPR_StdAudioSpeaker.setObjectName(u"Frame_ASR_VPR_StdAudioSpeaker")
        self.Frame_ASR_VPR_StdAudioSpeaker.setMinimumSize(QSize(0, 222))
        self.Frame_ASR_VPR_StdAudioSpeaker.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.Frame_ASR_VPR_StdAudioSpeaker)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_StdAudioSpeaker = QLabel(self.Frame_ASR_VPR_StdAudioSpeaker)
        self.Label_ASR_VPR_StdAudioSpeaker.setObjectName(u"Label_ASR_VPR_StdAudioSpeaker")
        sizePolicy6.setHeightForWidth(self.Label_ASR_VPR_StdAudioSpeaker.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_StdAudioSpeaker.setSizePolicy(sizePolicy6)
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

        self.Frame_ASR_VPR_DecisionThreshold = QFrame(self.Frame_BasicSettings_ASR_VPR)
        self.Frame_ASR_VPR_DecisionThreshold.setObjectName(u"Frame_ASR_VPR_DecisionThreshold")
        self.Frame_ASR_VPR_DecisionThreshold.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_DecisionThreshold.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_140 = QVBoxLayout(self.Frame_ASR_VPR_DecisionThreshold)
        self.verticalLayout_140.setSpacing(12)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_DecisionThreshold = QLabel(self.Frame_ASR_VPR_DecisionThreshold)
        self.Label_ASR_VPR_DecisionThreshold.setObjectName(u"Label_ASR_VPR_DecisionThreshold")
        sizePolicy6.setHeightForWidth(self.Label_ASR_VPR_DecisionThreshold.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_DecisionThreshold.setSizePolicy(sizePolicy6)
        self.Label_ASR_VPR_DecisionThreshold.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_140.addWidget(self.Label_ASR_VPR_DecisionThreshold)

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

        self.verticalLayout_140.addWidget(self.DoubleSpinBox_ASR_VPR_DecisionThreshold)


        self.verticalLayout_137.addWidget(self.Frame_ASR_VPR_DecisionThreshold)

        self.Frame_ASR_VPR_Audio_Dir_Output = QFrame(self.Frame_BasicSettings_ASR_VPR)
        self.Frame_ASR_VPR_Audio_Dir_Output.setObjectName(u"Frame_ASR_VPR_Audio_Dir_Output")
        self.Frame_ASR_VPR_Audio_Dir_Output.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_Audio_Dir_Output.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_141 = QVBoxLayout(self.Frame_ASR_VPR_Audio_Dir_Output)
        self.verticalLayout_141.setSpacing(12)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_Audio_Dir_Output = QLabel(self.Frame_ASR_VPR_Audio_Dir_Output)
        self.Label_ASR_VPR_Audio_Dir_Output.setObjectName(u"Label_ASR_VPR_Audio_Dir_Output")
        sizePolicy6.setHeightForWidth(self.Label_ASR_VPR_Audio_Dir_Output.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_Audio_Dir_Output.setSizePolicy(sizePolicy6)
        self.Label_ASR_VPR_Audio_Dir_Output.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_141.addWidget(self.Label_ASR_VPR_Audio_Dir_Output)

        self.ChildFrame_ASR_VPR_Audio_Dir_Output = QFrame(self.Frame_ASR_VPR_Audio_Dir_Output)
        self.ChildFrame_ASR_VPR_Audio_Dir_Output.setObjectName(u"ChildFrame_ASR_VPR_Audio_Dir_Output")
        sizePolicy6.setHeightForWidth(self.ChildFrame_ASR_VPR_Audio_Dir_Output.sizePolicy().hasHeightForWidth())
        self.ChildFrame_ASR_VPR_Audio_Dir_Output.setSizePolicy(sizePolicy6)
        self.ChildFrame_ASR_VPR_Audio_Dir_Output.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_74 = QHBoxLayout(self.ChildFrame_ASR_VPR_Audio_Dir_Output)
        self.horizontalLayout_74.setSpacing(12)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_ASR_VPR_Audio_Dir_Output = QLineEdit(self.ChildFrame_ASR_VPR_Audio_Dir_Output)
        self.LineEdit_ASR_VPR_Audio_Dir_Output.setObjectName(u"LineEdit_ASR_VPR_Audio_Dir_Output")
        self.LineEdit_ASR_VPR_Audio_Dir_Output.setMinimumSize(QSize(0, 27))
        self.LineEdit_ASR_VPR_Audio_Dir_Output.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_74.addWidget(self.LineEdit_ASR_VPR_Audio_Dir_Output)

        self.Button_ASR_VPR_Audio_Dir_Output = QPushButton(self.ChildFrame_ASR_VPR_Audio_Dir_Output)
        self.Button_ASR_VPR_Audio_Dir_Output.setObjectName(u"Button_ASR_VPR_Audio_Dir_Output")
        self.Button_ASR_VPR_Audio_Dir_Output.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_Audio_Dir_Output.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_74.addWidget(self.Button_ASR_VPR_Audio_Dir_Output)


        self.verticalLayout_141.addWidget(self.ChildFrame_ASR_VPR_Audio_Dir_Output)


        self.verticalLayout_137.addWidget(self.Frame_ASR_VPR_Audio_Dir_Output)


        self.verticalLayout_33.addWidget(self.Frame_BasicSettings_ASR_VPR)

        self.CheckBox_Toggle_AdvanceSettings_ASR_VPR = QCheckBox(self.GroupBox_EssentialParams_ASR_VPR)
        self.CheckBox_Toggle_AdvanceSettings_ASR_VPR.setObjectName(u"CheckBox_Toggle_AdvanceSettings_ASR_VPR")
        self.CheckBox_Toggle_AdvanceSettings_ASR_VPR.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_33.addWidget(self.CheckBox_Toggle_AdvanceSettings_ASR_VPR)

        self.Frame_AdvanceSettings_ASR_VPR = QFrame(self.GroupBox_EssentialParams_ASR_VPR)
        self.Frame_AdvanceSettings_ASR_VPR.setObjectName(u"Frame_AdvanceSettings_ASR_VPR")
        self.verticalLayout_7 = QVBoxLayout(self.Frame_AdvanceSettings_ASR_VPR)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Frame_ASR_VPR_Model_Path = QFrame(self.Frame_AdvanceSettings_ASR_VPR)
        self.Frame_ASR_VPR_Model_Path.setObjectName(u"Frame_ASR_VPR_Model_Path")
        self.Frame_ASR_VPR_Model_Path.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_Model_Path.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_142 = QVBoxLayout(self.Frame_ASR_VPR_Model_Path)
        self.verticalLayout_142.setSpacing(12)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_Model_Path = QLabel(self.Frame_ASR_VPR_Model_Path)
        self.Label_ASR_VPR_Model_Path.setObjectName(u"Label_ASR_VPR_Model_Path")
        sizePolicy6.setHeightForWidth(self.Label_ASR_VPR_Model_Path.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_Model_Path.setSizePolicy(sizePolicy6)
        self.Label_ASR_VPR_Model_Path.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_142.addWidget(self.Label_ASR_VPR_Model_Path)

        self.ChildFrame_ASR_VPR_Model_Path = QFrame(self.Frame_ASR_VPR_Model_Path)
        self.ChildFrame_ASR_VPR_Model_Path.setObjectName(u"ChildFrame_ASR_VPR_Model_Path")
        sizePolicy6.setHeightForWidth(self.ChildFrame_ASR_VPR_Model_Path.sizePolicy().hasHeightForWidth())
        self.ChildFrame_ASR_VPR_Model_Path.setSizePolicy(sizePolicy6)
        self.ChildFrame_ASR_VPR_Model_Path.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_75 = QHBoxLayout(self.ChildFrame_ASR_VPR_Model_Path)
        self.horizontalLayout_75.setSpacing(12)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_ASR_VPR_Model_Path = QLineEdit(self.ChildFrame_ASR_VPR_Model_Path)
        self.LineEdit_ASR_VPR_Model_Path.setObjectName(u"LineEdit_ASR_VPR_Model_Path")
        self.LineEdit_ASR_VPR_Model_Path.setMinimumSize(QSize(0, 27))
        self.LineEdit_ASR_VPR_Model_Path.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_75.addWidget(self.LineEdit_ASR_VPR_Model_Path)

        self.Button_ASR_VPR_Model_Path = QPushButton(self.ChildFrame_ASR_VPR_Model_Path)
        self.Button_ASR_VPR_Model_Path.setObjectName(u"Button_ASR_VPR_Model_Path")
        self.Button_ASR_VPR_Model_Path.setMinimumSize(QSize(27, 27))
        self.Button_ASR_VPR_Model_Path.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_75.addWidget(self.Button_ASR_VPR_Model_Path)


        self.verticalLayout_142.addWidget(self.ChildFrame_ASR_VPR_Model_Path)


        self.verticalLayout_7.addWidget(self.Frame_ASR_VPR_Model_Path)

        self.Frame_ASR_VPR_Model_Type = QFrame(self.Frame_AdvanceSettings_ASR_VPR)
        self.Frame_ASR_VPR_Model_Type.setObjectName(u"Frame_ASR_VPR_Model_Type")
        self.Frame_ASR_VPR_Model_Type.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_Model_Type.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_143 = QVBoxLayout(self.Frame_ASR_VPR_Model_Type)
        self.verticalLayout_143.setSpacing(12)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_Model_Type = QLabel(self.Frame_ASR_VPR_Model_Type)
        self.Label_ASR_VPR_Model_Type.setObjectName(u"Label_ASR_VPR_Model_Type")
        sizePolicy6.setHeightForWidth(self.Label_ASR_VPR_Model_Type.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_Model_Type.setSizePolicy(sizePolicy6)
        self.Label_ASR_VPR_Model_Type.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_143.addWidget(self.Label_ASR_VPR_Model_Type)

        self.ComboBox_ASR_VPR_Model_Type = QComboBox(self.Frame_ASR_VPR_Model_Type)
        self.ComboBox_ASR_VPR_Model_Type.setObjectName(u"ComboBox_ASR_VPR_Model_Type")
        self.ComboBox_ASR_VPR_Model_Type.setMinimumSize(QSize(0, 27))
        self.ComboBox_ASR_VPR_Model_Type.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
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
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding-left: -15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemV"
                        "iew::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-left: 15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120. 120, 120, 120)\n"
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
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
""
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
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:"
                        "hover {\n"
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
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScro"
                        "llArea QScrollBar::handle:horizontal:hover {\n"
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

        self.verticalLayout_143.addWidget(self.ComboBox_ASR_VPR_Model_Type)


        self.verticalLayout_7.addWidget(self.Frame_ASR_VPR_Model_Type)

        self.Frame_ASR_VPR_Feature_Method = QFrame(self.Frame_AdvanceSettings_ASR_VPR)
        self.Frame_ASR_VPR_Feature_Method.setObjectName(u"Frame_ASR_VPR_Feature_Method")
        self.Frame_ASR_VPR_Feature_Method.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_Feature_Method.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_145 = QVBoxLayout(self.Frame_ASR_VPR_Feature_Method)
        self.verticalLayout_145.setSpacing(12)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_Feature_Method = QLabel(self.Frame_ASR_VPR_Feature_Method)
        self.Label_ASR_VPR_Feature_Method.setObjectName(u"Label_ASR_VPR_Feature_Method")
        sizePolicy6.setHeightForWidth(self.Label_ASR_VPR_Feature_Method.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_Feature_Method.setSizePolicy(sizePolicy6)
        self.Label_ASR_VPR_Feature_Method.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_145.addWidget(self.Label_ASR_VPR_Feature_Method)

        self.ComboBox_ASR_VPR_Feature_Method = QComboBox(self.Frame_ASR_VPR_Feature_Method)
        self.ComboBox_ASR_VPR_Feature_Method.setObjectName(u"ComboBox_ASR_VPR_Feature_Method")
        self.ComboBox_ASR_VPR_Feature_Method.setMinimumSize(QSize(0, 27))
        self.ComboBox_ASR_VPR_Feature_Method.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
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
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding-left: -15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemV"
                        "iew::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-left: 15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120. 120, 120, 120)\n"
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
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
""
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
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:"
                        "hover {\n"
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
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScro"
                        "llArea QScrollBar::handle:horizontal:hover {\n"
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

        self.verticalLayout_145.addWidget(self.ComboBox_ASR_VPR_Feature_Method)


        self.verticalLayout_7.addWidget(self.Frame_ASR_VPR_Feature_Method)

        self.Frame_ASR_VPR_Duration_of_Audio = QFrame(self.Frame_AdvanceSettings_ASR_VPR)
        self.Frame_ASR_VPR_Duration_of_Audio.setObjectName(u"Frame_ASR_VPR_Duration_of_Audio")
        self.Frame_ASR_VPR_Duration_of_Audio.setMinimumSize(QSize(0, 105))
        self.Frame_ASR_VPR_Duration_of_Audio.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_146 = QVBoxLayout(self.Frame_ASR_VPR_Duration_of_Audio)
        self.verticalLayout_146.setSpacing(12)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.verticalLayout_146.setContentsMargins(21, 12, 21, 12)
        self.Label_ASR_VPR_Duration_of_Audio = QLabel(self.Frame_ASR_VPR_Duration_of_Audio)
        self.Label_ASR_VPR_Duration_of_Audio.setObjectName(u"Label_ASR_VPR_Duration_of_Audio")
        sizePolicy6.setHeightForWidth(self.Label_ASR_VPR_Duration_of_Audio.sizePolicy().hasHeightForWidth())
        self.Label_ASR_VPR_Duration_of_Audio.setSizePolicy(sizePolicy6)
        self.Label_ASR_VPR_Duration_of_Audio.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_146.addWidget(self.Label_ASR_VPR_Duration_of_Audio)

        self.DoubleSpinBox_ASR_VPR_Duration_of_Audio = QDoubleSpinBox(self.Frame_ASR_VPR_Duration_of_Audio)
        self.DoubleSpinBox_ASR_VPR_Duration_of_Audio.setObjectName(u"DoubleSpinBox_ASR_VPR_Duration_of_Audio")
        self.DoubleSpinBox_ASR_VPR_Duration_of_Audio.setEnabled(True)
        self.DoubleSpinBox_ASR_VPR_Duration_of_Audio.setMinimumSize(QSize(0, 27))
        self.DoubleSpinBox_ASR_VPR_Duration_of_Audio.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.DoubleSpinBox_ASR_VPR_Duration_of_Audio.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_ASR_VPR_Duration_of_Audio.setMaximum(999999.000000000000000)

        self.verticalLayout_146.addWidget(self.DoubleSpinBox_ASR_VPR_Duration_of_Audio)


        self.verticalLayout_7.addWidget(self.Frame_ASR_VPR_Duration_of_Audio)


        self.verticalLayout_33.addWidget(self.Frame_AdvanceSettings_ASR_VPR)


        self.verticalLayout_15.addWidget(self.GroupBox_EssentialParams_ASR_VPR)

        self.VerticalSpacer_ASR_VPR = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.VerticalSpacer_ASR_VPR)

        self.ScrollArea_Middle_ASR_VPR.setWidget(self.ScrollArea_Middle_WidgetContents_ASR_VPR)

        self.gridLayout_21.addWidget(self.ScrollArea_Middle_ASR_VPR, 0, 1, 1, 1)

        self.Widget_Right_ASR_VPR = QWidget(self.Subpage_ASR_VPR)
        self.Widget_Right_ASR_VPR.setObjectName(u"Widget_Right_ASR_VPR")
        self.Widget_Right_ASR_VPR.setMinimumSize(QSize(210, 0))
        self.Widget_Right_ASR_VPR.setMaximumSize(QSize(420, 16777215))
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
"	background-color: rgb(33, 33, 33);\n"
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
"	border-st"
                        "yle: solid;\n"
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
"	width: 0px;\n"
""
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

        self.Button_SyncParams_ASR_VPR = QPushButton(self.Widget_Right_ASR_VPR)
        self.Button_SyncParams_ASR_VPR.setObjectName(u"Button_SyncParams_ASR_VPR")
        self.Button_SyncParams_ASR_VPR.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_14.addWidget(self.Button_SyncParams_ASR_VPR, 1, 0, 1, 1)

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

        self.gridLayout_14.addWidget(self.Button_CheckOutput_ASR_VPR, 1, 1, 1, 1)


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
        sizePolicy7.setHeightForWidth(self.Button_ASR_VPR_Execute.sizePolicy().hasHeightForWidth())
        self.Button_ASR_VPR_Execute.setSizePolicy(sizePolicy7)
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
        sizePolicy7.setHeightForWidth(self.Button_ASR_VPR_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_ASR_VPR_Terminate.setSizePolicy(sizePolicy7)
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
        self.Widget_Left_STT_Whisper.setMaximumSize(QSize(210, 16777215))
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
        self.TreeWidget_Catalogue_STT_Whisper.setStyleSheet(u"QTreeWidget {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"	background-color: transparent;\n"
"	padding: 1.2px;\n"
"}\n"
"\n"
"QTreeWidget::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeWidget::branch:open:has-children:has-siblings,\n"
"QTreeWidget::branch:open:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:closed:has-children:has-siblings,\n"
"QTreeWidget::branch:closed:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:!has-children:has-siblings:adjoins-item,\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    image: ;\n"
"}\n"
"\n"
"\n"
"QTreeView {\n"
"}\n"
"\n"
"QTreeView::item{\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
""
                        "QTreeView::item:selected:active{\n"
"    background-color: ;\n"
"}\n"
"QTreeView::item:selected:!active {\n"
"    background-color: ;\n"
"}\n"
"\n"
"/*\n"
"QHeaderView {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QHeaderView:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: transparent;\n"
"}\n"
"QHeaderView::section:checked {\n"
"	background-color: ;\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}*/\n"
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
"	background-color: rgba(33, 3"
                        "3, 33, 99);\n"
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
"	border"
                        "-radius: 6px;\n"
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
"	backgro"
                        "und-color: rgb(120, 120, 120);\n"
"}")

        self.verticalLayout_8.addWidget(self.TreeWidget_Catalogue_STT_Whisper)


        self.gridLayout_19.addWidget(self.Widget_Left_STT_Whisper, 0, 0, 1, 1)

        self.ScrollArea_Middle_STT_Whisper = QScrollArea(self.Subpage_STT_Whisper)
        self.ScrollArea_Middle_STT_Whisper.setObjectName(u"ScrollArea_Middle_STT_Whisper")
        sizePolicy5.setHeightForWidth(self.ScrollArea_Middle_STT_Whisper.sizePolicy().hasHeightForWidth())
        self.ScrollArea_Middle_STT_Whisper.setSizePolicy(sizePolicy5)
        self.ScrollArea_Middle_STT_Whisper.setMinimumSize(QSize(630, 0))
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
        self.ScrollArea_Middle_WidgetContents_STT_Whisper.setGeometry(QRect(0, 0, 621, 909))
        self.verticalLayout_16 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_STT_Whisper)
        self.verticalLayout_16.setSpacing(12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_STT_Whisper = QGroupBox(self.ScrollArea_Middle_WidgetContents_STT_Whisper)
        self.GroupBox_EssentialParams_STT_Whisper.setObjectName(u"GroupBox_EssentialParams_STT_Whisper")
        self.GroupBox_EssentialParams_STT_Whisper.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_32 = QVBoxLayout(self.GroupBox_EssentialParams_STT_Whisper)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_STT_Whisper = QCheckBox(self.GroupBox_EssentialParams_STT_Whisper)
        self.CheckBox_Toggle_BasicSettings_STT_Whisper.setObjectName(u"CheckBox_Toggle_BasicSettings_STT_Whisper")
        self.CheckBox_Toggle_BasicSettings_STT_Whisper.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_32.addWidget(self.CheckBox_Toggle_BasicSettings_STT_Whisper)

        self.Frame_BasicSettings_STT_Whisper = QFrame(self.GroupBox_EssentialParams_STT_Whisper)
        self.Frame_BasicSettings_STT_Whisper.setObjectName(u"Frame_BasicSettings_STT_Whisper")
        self.verticalLayout_129 = QVBoxLayout(self.Frame_BasicSettings_STT_Whisper)
        self.verticalLayout_129.setSpacing(0)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.Frame_STT_Whisper_WAV_Dir = QFrame(self.Frame_BasicSettings_STT_Whisper)
        self.Frame_STT_Whisper_WAV_Dir.setObjectName(u"Frame_STT_Whisper_WAV_Dir")
        self.Frame_STT_Whisper_WAV_Dir.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_WAV_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_52 = QVBoxLayout(self.Frame_STT_Whisper_WAV_Dir)
        self.verticalLayout_52.setSpacing(12)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_WAV_Dir = QLabel(self.Frame_STT_Whisper_WAV_Dir)
        self.Label_STT_Whisper_WAV_Dir.setObjectName(u"Label_STT_Whisper_WAV_Dir")
        sizePolicy6.setHeightForWidth(self.Label_STT_Whisper_WAV_Dir.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_WAV_Dir.setSizePolicy(sizePolicy6)
        self.Label_STT_Whisper_WAV_Dir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_52.addWidget(self.Label_STT_Whisper_WAV_Dir)

        self.ChildFrame_STT_Whisper_WAV_Dir = QFrame(self.Frame_STT_Whisper_WAV_Dir)
        self.ChildFrame_STT_Whisper_WAV_Dir.setObjectName(u"ChildFrame_STT_Whisper_WAV_Dir")
        sizePolicy6.setHeightForWidth(self.ChildFrame_STT_Whisper_WAV_Dir.sizePolicy().hasHeightForWidth())
        self.ChildFrame_STT_Whisper_WAV_Dir.setSizePolicy(sizePolicy6)
        self.ChildFrame_STT_Whisper_WAV_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_14 = QHBoxLayout(self.ChildFrame_STT_Whisper_WAV_Dir)
        self.horizontalLayout_14.setSpacing(12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_STT_Whisper_WAV_Dir = QLineEdit(self.ChildFrame_STT_Whisper_WAV_Dir)
        self.LineEdit_STT_Whisper_WAV_Dir.setObjectName(u"LineEdit_STT_Whisper_WAV_Dir")
        self.LineEdit_STT_Whisper_WAV_Dir.setMinimumSize(QSize(0, 27))
        self.LineEdit_STT_Whisper_WAV_Dir.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_14.addWidget(self.LineEdit_STT_Whisper_WAV_Dir)

        self.Button_STT_Whisper_WAV_Dir = QPushButton(self.ChildFrame_STT_Whisper_WAV_Dir)
        self.Button_STT_Whisper_WAV_Dir.setObjectName(u"Button_STT_Whisper_WAV_Dir")
        self.Button_STT_Whisper_WAV_Dir.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_WAV_Dir.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_14.addWidget(self.Button_STT_Whisper_WAV_Dir)


        self.verticalLayout_52.addWidget(self.ChildFrame_STT_Whisper_WAV_Dir)


        self.verticalLayout_129.addWidget(self.Frame_STT_Whisper_WAV_Dir)

        self.Frame_STT_Whisper_SRT_Dir = QFrame(self.Frame_BasicSettings_STT_Whisper)
        self.Frame_STT_Whisper_SRT_Dir.setObjectName(u"Frame_STT_Whisper_SRT_Dir")
        self.Frame_STT_Whisper_SRT_Dir.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_SRT_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_58 = QVBoxLayout(self.Frame_STT_Whisper_SRT_Dir)
        self.verticalLayout_58.setSpacing(12)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_SRT_Dir = QLabel(self.Frame_STT_Whisper_SRT_Dir)
        self.Label_STT_Whisper_SRT_Dir.setObjectName(u"Label_STT_Whisper_SRT_Dir")
        sizePolicy6.setHeightForWidth(self.Label_STT_Whisper_SRT_Dir.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_SRT_Dir.setSizePolicy(sizePolicy6)
        self.Label_STT_Whisper_SRT_Dir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_58.addWidget(self.Label_STT_Whisper_SRT_Dir)

        self.ChildFrame_STT_Whisper_SRT_Dir = QFrame(self.Frame_STT_Whisper_SRT_Dir)
        self.ChildFrame_STT_Whisper_SRT_Dir.setObjectName(u"ChildFrame_STT_Whisper_SRT_Dir")
        sizePolicy6.setHeightForWidth(self.ChildFrame_STT_Whisper_SRT_Dir.sizePolicy().hasHeightForWidth())
        self.ChildFrame_STT_Whisper_SRT_Dir.setSizePolicy(sizePolicy6)
        self.ChildFrame_STT_Whisper_SRT_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.ChildFrame_STT_Whisper_SRT_Dir)
        self.horizontalLayout_16.setSpacing(12)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_STT_Whisper_SRT_Dir = QLineEdit(self.ChildFrame_STT_Whisper_SRT_Dir)
        self.LineEdit_STT_Whisper_SRT_Dir.setObjectName(u"LineEdit_STT_Whisper_SRT_Dir")
        self.LineEdit_STT_Whisper_SRT_Dir.setMinimumSize(QSize(0, 27))
        self.LineEdit_STT_Whisper_SRT_Dir.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_16.addWidget(self.LineEdit_STT_Whisper_SRT_Dir)

        self.Button_STT_Whisper_SRT_Dir = QPushButton(self.ChildFrame_STT_Whisper_SRT_Dir)
        self.Button_STT_Whisper_SRT_Dir.setObjectName(u"Button_STT_Whisper_SRT_Dir")
        self.Button_STT_Whisper_SRT_Dir.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_SRT_Dir.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_16.addWidget(self.Button_STT_Whisper_SRT_Dir)


        self.verticalLayout_58.addWidget(self.ChildFrame_STT_Whisper_SRT_Dir)


        self.verticalLayout_129.addWidget(self.Frame_STT_Whisper_SRT_Dir)


        self.verticalLayout_32.addWidget(self.Frame_BasicSettings_STT_Whisper)

        self.CheckBox_Toggle_AdvanceSettings_STT_Whisper = QCheckBox(self.GroupBox_EssentialParams_STT_Whisper)
        self.CheckBox_Toggle_AdvanceSettings_STT_Whisper.setObjectName(u"CheckBox_Toggle_AdvanceSettings_STT_Whisper")
        self.CheckBox_Toggle_AdvanceSettings_STT_Whisper.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_32.addWidget(self.CheckBox_Toggle_AdvanceSettings_STT_Whisper)

        self.Frame_AdvanceSettings_STT_Whisper = QFrame(self.GroupBox_EssentialParams_STT_Whisper)
        self.Frame_AdvanceSettings_STT_Whisper.setObjectName(u"Frame_AdvanceSettings_STT_Whisper")
        self.verticalLayout_30 = QVBoxLayout(self.Frame_AdvanceSettings_STT_Whisper)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.Frame_STT_Whisper_Model_Path = QFrame(self.Frame_AdvanceSettings_STT_Whisper)
        self.Frame_STT_Whisper_Model_Path.setObjectName(u"Frame_STT_Whisper_Model_Path")
        self.Frame_STT_Whisper_Model_Path.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_Model_Path.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_53 = QVBoxLayout(self.Frame_STT_Whisper_Model_Path)
        self.verticalLayout_53.setSpacing(12)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_Model_Path = QLabel(self.Frame_STT_Whisper_Model_Path)
        self.Label_STT_Whisper_Model_Path.setObjectName(u"Label_STT_Whisper_Model_Path")
        sizePolicy6.setHeightForWidth(self.Label_STT_Whisper_Model_Path.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_Model_Path.setSizePolicy(sizePolicy6)
        self.Label_STT_Whisper_Model_Path.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_53.addWidget(self.Label_STT_Whisper_Model_Path)

        self.ChildFrame_STT_Whisper_Model_Path = QFrame(self.Frame_STT_Whisper_Model_Path)
        self.ChildFrame_STT_Whisper_Model_Path.setObjectName(u"ChildFrame_STT_Whisper_Model_Path")
        sizePolicy6.setHeightForWidth(self.ChildFrame_STT_Whisper_Model_Path.sizePolicy().hasHeightForWidth())
        self.ChildFrame_STT_Whisper_Model_Path.setSizePolicy(sizePolicy6)
        self.ChildFrame_STT_Whisper_Model_Path.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.ChildFrame_STT_Whisper_Model_Path)
        self.horizontalLayout_15.setSpacing(12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_STT_Whisper_Model_Path = QLineEdit(self.ChildFrame_STT_Whisper_Model_Path)
        self.LineEdit_STT_Whisper_Model_Path.setObjectName(u"LineEdit_STT_Whisper_Model_Path")
        self.LineEdit_STT_Whisper_Model_Path.setMinimumSize(QSize(0, 27))
        self.LineEdit_STT_Whisper_Model_Path.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_15.addWidget(self.LineEdit_STT_Whisper_Model_Path)

        self.Button_STT_Whisper_Model_Path = QPushButton(self.ChildFrame_STT_Whisper_Model_Path)
        self.Button_STT_Whisper_Model_Path.setObjectName(u"Button_STT_Whisper_Model_Path")
        self.Button_STT_Whisper_Model_Path.setMinimumSize(QSize(27, 27))
        self.Button_STT_Whisper_Model_Path.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_15.addWidget(self.Button_STT_Whisper_Model_Path)


        self.verticalLayout_53.addWidget(self.ChildFrame_STT_Whisper_Model_Path)


        self.verticalLayout_30.addWidget(self.Frame_STT_Whisper_Model_Path)

        self.Frame_STT_Whisper_Verbose = QFrame(self.Frame_AdvanceSettings_STT_Whisper)
        self.Frame_STT_Whisper_Verbose.setObjectName(u"Frame_STT_Whisper_Verbose")
        self.Frame_STT_Whisper_Verbose.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_Verbose.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_55 = QVBoxLayout(self.Frame_STT_Whisper_Verbose)
        self.verticalLayout_55.setSpacing(12)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_Verbose = QLabel(self.Frame_STT_Whisper_Verbose)
        self.Label_STT_Whisper_Verbose.setObjectName(u"Label_STT_Whisper_Verbose")
        sizePolicy6.setHeightForWidth(self.Label_STT_Whisper_Verbose.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_Verbose.setSizePolicy(sizePolicy6)
        self.Label_STT_Whisper_Verbose.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_55.addWidget(self.Label_STT_Whisper_Verbose)

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

        self.verticalLayout_55.addWidget(self.CheckBox_STT_Whisper_Verbose)


        self.verticalLayout_30.addWidget(self.Frame_STT_Whisper_Verbose)

        self.Frame_STT_Whisper_Condition_on_Previous_Text = QFrame(self.Frame_AdvanceSettings_STT_Whisper)
        self.Frame_STT_Whisper_Condition_on_Previous_Text.setObjectName(u"Frame_STT_Whisper_Condition_on_Previous_Text")
        self.Frame_STT_Whisper_Condition_on_Previous_Text.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_Condition_on_Previous_Text.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_56 = QVBoxLayout(self.Frame_STT_Whisper_Condition_on_Previous_Text)
        self.verticalLayout_56.setSpacing(12)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_Condition_on_Previous_Text = QLabel(self.Frame_STT_Whisper_Condition_on_Previous_Text)
        self.Label_STT_Whisper_Condition_on_Previous_Text.setObjectName(u"Label_STT_Whisper_Condition_on_Previous_Text")
        sizePolicy6.setHeightForWidth(self.Label_STT_Whisper_Condition_on_Previous_Text.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_Condition_on_Previous_Text.setSizePolicy(sizePolicy6)
        self.Label_STT_Whisper_Condition_on_Previous_Text.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_56.addWidget(self.Label_STT_Whisper_Condition_on_Previous_Text)

        self.CheckBox_STT_Whisper_Condition_on_Previous_Text = QCheckBox(self.Frame_STT_Whisper_Condition_on_Previous_Text)
        self.CheckBox_STT_Whisper_Condition_on_Previous_Text.setObjectName(u"CheckBox_STT_Whisper_Condition_on_Previous_Text")
        self.CheckBox_STT_Whisper_Condition_on_Previous_Text.setMinimumSize(QSize(0, 27))
        self.CheckBox_STT_Whisper_Condition_on_Previous_Text.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_56.addWidget(self.CheckBox_STT_Whisper_Condition_on_Previous_Text)


        self.verticalLayout_30.addWidget(self.Frame_STT_Whisper_Condition_on_Previous_Text)

        self.Frame_STT_Whisper_fp16 = QFrame(self.Frame_AdvanceSettings_STT_Whisper)
        self.Frame_STT_Whisper_fp16.setObjectName(u"Frame_STT_Whisper_fp16")
        self.Frame_STT_Whisper_fp16.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_fp16.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_57 = QVBoxLayout(self.Frame_STT_Whisper_fp16)
        self.verticalLayout_57.setSpacing(12)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_fp16 = QLabel(self.Frame_STT_Whisper_fp16)
        self.Label_STT_Whisper_fp16.setObjectName(u"Label_STT_Whisper_fp16")
        sizePolicy6.setHeightForWidth(self.Label_STT_Whisper_fp16.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_fp16.setSizePolicy(sizePolicy6)
        self.Label_STT_Whisper_fp16.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_57.addWidget(self.Label_STT_Whisper_fp16)

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

        self.verticalLayout_57.addWidget(self.CheckBox_STT_Whisper_fp16)


        self.verticalLayout_30.addWidget(self.Frame_STT_Whisper_fp16)


        self.verticalLayout_32.addWidget(self.Frame_AdvanceSettings_STT_Whisper)


        self.verticalLayout_16.addWidget(self.GroupBox_EssentialParams_STT_Whisper)

        self.GroupBox_OptionalParams_STT_Whisper = QGroupBox(self.ScrollArea_Middle_WidgetContents_STT_Whisper)
        self.GroupBox_OptionalParams_STT_Whisper.setObjectName(u"GroupBox_OptionalParams_STT_Whisper")
        self.GroupBox_OptionalParams_STT_Whisper.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_31 = QVBoxLayout(self.GroupBox_OptionalParams_STT_Whisper)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 12, 0, 12)
        self.Frame_OptionalSettings_STT_Whisper = QFrame(self.GroupBox_OptionalParams_STT_Whisper)
        self.Frame_OptionalSettings_STT_Whisper.setObjectName(u"Frame_OptionalSettings_STT_Whisper")
        self.verticalLayout_133 = QVBoxLayout(self.Frame_OptionalSettings_STT_Whisper)
        self.verticalLayout_133.setSpacing(0)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.Frame_STT_Whisper_Language = QFrame(self.Frame_OptionalSettings_STT_Whisper)
        self.Frame_STT_Whisper_Language.setObjectName(u"Frame_STT_Whisper_Language")
        self.Frame_STT_Whisper_Language.setMinimumSize(QSize(0, 105))
        self.Frame_STT_Whisper_Language.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_59 = QVBoxLayout(self.Frame_STT_Whisper_Language)
        self.verticalLayout_59.setSpacing(12)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(21, 12, 21, 12)
        self.Label_STT_Whisper_Language = QLabel(self.Frame_STT_Whisper_Language)
        self.Label_STT_Whisper_Language.setObjectName(u"Label_STT_Whisper_Language")
        sizePolicy6.setHeightForWidth(self.Label_STT_Whisper_Language.sizePolicy().hasHeightForWidth())
        self.Label_STT_Whisper_Language.setSizePolicy(sizePolicy6)
        self.Label_STT_Whisper_Language.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_59.addWidget(self.Label_STT_Whisper_Language)

        self.ComboBox_STT_Whisper_Language = QComboBox(self.Frame_STT_Whisper_Language)
        self.ComboBox_STT_Whisper_Language.setObjectName(u"ComboBox_STT_Whisper_Language")
        self.ComboBox_STT_Whisper_Language.setMinimumSize(QSize(0, 27))
        self.ComboBox_STT_Whisper_Language.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
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
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding-left: -15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemV"
                        "iew::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-left: 15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120. 120, 120, 120)\n"
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
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
""
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
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:"
                        "hover {\n"
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
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScro"
                        "llArea QScrollBar::handle:horizontal:hover {\n"
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

        self.verticalLayout_59.addWidget(self.ComboBox_STT_Whisper_Language)


        self.verticalLayout_133.addWidget(self.Frame_STT_Whisper_Language)


        self.verticalLayout_31.addWidget(self.Frame_OptionalSettings_STT_Whisper)


        self.verticalLayout_16.addWidget(self.GroupBox_OptionalParams_STT_Whisper)

        self.VerticalSpacer_STT_Whisper = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.VerticalSpacer_STT_Whisper)

        self.ScrollArea_Middle_STT_Whisper.setWidget(self.ScrollArea_Middle_WidgetContents_STT_Whisper)

        self.gridLayout_19.addWidget(self.ScrollArea_Middle_STT_Whisper, 0, 1, 1, 1)

        self.Widget_Right_STT_Whisper = QWidget(self.Subpage_STT_Whisper)
        self.Widget_Right_STT_Whisper.setObjectName(u"Widget_Right_STT_Whisper")
        self.Widget_Right_STT_Whisper.setMinimumSize(QSize(210, 0))
        self.Widget_Right_STT_Whisper.setMaximumSize(QSize(420, 16777215))
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
"	background-color: rgb(33, 33, 33);\n"
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
"	border-st"
                        "yle: solid;\n"
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
"	width: 0px;\n"
""
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

        self.Button_SyncParams_STT_Whisper = QPushButton(self.Widget_Right_STT_Whisper)
        self.Button_SyncParams_STT_Whisper.setObjectName(u"Button_SyncParams_STT_Whisper")
        self.Button_SyncParams_STT_Whisper.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_15.addWidget(self.Button_SyncParams_STT_Whisper, 1, 0, 1, 1)

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

        self.gridLayout_15.addWidget(self.Button_CheckOutput_STT_Whisper, 1, 1, 1, 1)


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
        sizePolicy7.setHeightForWidth(self.Button_STT_Whisper_Execute.sizePolicy().hasHeightForWidth())
        self.Button_STT_Whisper_Execute.setSizePolicy(sizePolicy7)
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
        sizePolicy7.setHeightForWidth(self.Button_STT_Whisper_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_STT_Whisper_Terminate.setSizePolicy(sizePolicy7)
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
        self.Widget_Left_DAT_VITS.setMaximumSize(QSize(210, 16777215))
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
        self.TreeWidget_Catalogue_DAT_VITS.setStyleSheet(u"QTreeWidget {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"	background-color: transparent;\n"
"	padding: 1.2px;\n"
"}\n"
"\n"
"QTreeWidget::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeWidget::branch:open:has-children:has-siblings,\n"
"QTreeWidget::branch:open:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:closed:has-children:has-siblings,\n"
"QTreeWidget::branch:closed:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:!has-children:has-siblings:adjoins-item,\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    image: ;\n"
"}\n"
"\n"
"\n"
"QTreeView {\n"
"}\n"
"\n"
"QTreeView::item{\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
""
                        "QTreeView::item:selected:active{\n"
"    background-color: ;\n"
"}\n"
"QTreeView::item:selected:!active {\n"
"    background-color: ;\n"
"}\n"
"\n"
"/*\n"
"QHeaderView {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QHeaderView:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: transparent;\n"
"}\n"
"QHeaderView::section:checked {\n"
"	background-color: ;\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}*/\n"
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
"	background-color: rgba(33, 3"
                        "3, 33, 99);\n"
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
"	border"
                        "-radius: 6px;\n"
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
"	backgro"
                        "und-color: rgb(120, 120, 120);\n"
"}")

        self.verticalLayout_9.addWidget(self.TreeWidget_Catalogue_DAT_VITS)


        self.gridLayout_8.addWidget(self.Widget_Left_DAT_VITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_DAT_VITS = QScrollArea(self.Subpage_DAT_VITS)
        self.ScrollArea_Middle_DAT_VITS.setObjectName(u"ScrollArea_Middle_DAT_VITS")
        sizePolicy5.setHeightForWidth(self.ScrollArea_Middle_DAT_VITS.sizePolicy().hasHeightForWidth())
        self.ScrollArea_Middle_DAT_VITS.setSizePolicy(sizePolicy5)
        self.ScrollArea_Middle_DAT_VITS.setMinimumSize(QSize(630, 0))
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
        self.ScrollArea_Middle_WidgetContents_DAT_VITS.setGeometry(QRect(0, 0, 621, 1281))
        self.verticalLayout_36 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.verticalLayout_36.setSpacing(12)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_DAT_VITS = QGroupBox(self.ScrollArea_Middle_WidgetContents_DAT_VITS)
        self.GroupBox_EssentialParams_DAT_VITS.setObjectName(u"GroupBox_EssentialParams_DAT_VITS")
        self.GroupBox_EssentialParams_DAT_VITS.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_111 = QVBoxLayout(self.GroupBox_EssentialParams_DAT_VITS)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_DAT_VITS = QCheckBox(self.GroupBox_EssentialParams_DAT_VITS)
        self.CheckBox_Toggle_BasicSettings_DAT_VITS.setObjectName(u"CheckBox_Toggle_BasicSettings_DAT_VITS")
        self.CheckBox_Toggle_BasicSettings_DAT_VITS.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_111.addWidget(self.CheckBox_Toggle_BasicSettings_DAT_VITS)

        self.Frame_BasicSettings_DAT_VITS = QFrame(self.GroupBox_EssentialParams_DAT_VITS)
        self.Frame_BasicSettings_DAT_VITS.setObjectName(u"Frame_BasicSettings_DAT_VITS")
        self.verticalLayout_29 = QVBoxLayout(self.Frame_BasicSettings_DAT_VITS)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_WAV_Dir = QFrame(self.Frame_BasicSettings_DAT_VITS)
        self.Frame_DAT_VITS_WAV_Dir.setObjectName(u"Frame_DAT_VITS_WAV_Dir")
        self.Frame_DAT_VITS_WAV_Dir.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_WAV_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_60 = QVBoxLayout(self.Frame_DAT_VITS_WAV_Dir)
        self.verticalLayout_60.setSpacing(12)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_WAV_Dir = QLabel(self.Frame_DAT_VITS_WAV_Dir)
        self.Label_DAT_VITS_WAV_Dir.setObjectName(u"Label_DAT_VITS_WAV_Dir")
        sizePolicy6.setHeightForWidth(self.Label_DAT_VITS_WAV_Dir.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_WAV_Dir.setSizePolicy(sizePolicy6)
        self.Label_DAT_VITS_WAV_Dir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_60.addWidget(self.Label_DAT_VITS_WAV_Dir)

        self.ChildFrame_DAT_VITS_WAV_Dir = QFrame(self.Frame_DAT_VITS_WAV_Dir)
        self.ChildFrame_DAT_VITS_WAV_Dir.setObjectName(u"ChildFrame_DAT_VITS_WAV_Dir")
        sizePolicy6.setHeightForWidth(self.ChildFrame_DAT_VITS_WAV_Dir.sizePolicy().hasHeightForWidth())
        self.ChildFrame_DAT_VITS_WAV_Dir.setSizePolicy(sizePolicy6)
        self.ChildFrame_DAT_VITS_WAV_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_17 = QHBoxLayout(self.ChildFrame_DAT_VITS_WAV_Dir)
        self.horizontalLayout_17.setSpacing(12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_DAT_VITS_WAV_Dir = QLineEdit(self.ChildFrame_DAT_VITS_WAV_Dir)
        self.LineEdit_DAT_VITS_WAV_Dir.setObjectName(u"LineEdit_DAT_VITS_WAV_Dir")
        self.LineEdit_DAT_VITS_WAV_Dir.setMinimumSize(QSize(0, 27))
        self.LineEdit_DAT_VITS_WAV_Dir.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_17.addWidget(self.LineEdit_DAT_VITS_WAV_Dir)

        self.Button_DAT_VITS_WAV_Dir = QPushButton(self.ChildFrame_DAT_VITS_WAV_Dir)
        self.Button_DAT_VITS_WAV_Dir.setObjectName(u"Button_DAT_VITS_WAV_Dir")
        self.Button_DAT_VITS_WAV_Dir.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_WAV_Dir.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_17.addWidget(self.Button_DAT_VITS_WAV_Dir)


        self.verticalLayout_60.addWidget(self.ChildFrame_DAT_VITS_WAV_Dir)


        self.verticalLayout_29.addWidget(self.Frame_DAT_VITS_WAV_Dir)

        self.Frame_DAT_VITS_SRT_Dir = QFrame(self.Frame_BasicSettings_DAT_VITS)
        self.Frame_DAT_VITS_SRT_Dir.setObjectName(u"Frame_DAT_VITS_SRT_Dir")
        self.Frame_DAT_VITS_SRT_Dir.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SRT_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_64 = QVBoxLayout(self.Frame_DAT_VITS_SRT_Dir)
        self.verticalLayout_64.setSpacing(12)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_SRT_Dir = QLabel(self.Frame_DAT_VITS_SRT_Dir)
        self.Label_DAT_VITS_SRT_Dir.setObjectName(u"Label_DAT_VITS_SRT_Dir")
        sizePolicy6.setHeightForWidth(self.Label_DAT_VITS_SRT_Dir.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_SRT_Dir.setSizePolicy(sizePolicy6)
        self.Label_DAT_VITS_SRT_Dir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_64.addWidget(self.Label_DAT_VITS_SRT_Dir)

        self.ChildFrame_DAT_VITS_SRT_Dir = QFrame(self.Frame_DAT_VITS_SRT_Dir)
        self.ChildFrame_DAT_VITS_SRT_Dir.setObjectName(u"ChildFrame_DAT_VITS_SRT_Dir")
        sizePolicy6.setHeightForWidth(self.ChildFrame_DAT_VITS_SRT_Dir.sizePolicy().hasHeightForWidth())
        self.ChildFrame_DAT_VITS_SRT_Dir.setSizePolicy(sizePolicy6)
        self.ChildFrame_DAT_VITS_SRT_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_19 = QHBoxLayout(self.ChildFrame_DAT_VITS_SRT_Dir)
        self.horizontalLayout_19.setSpacing(12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_DAT_VITS_SRT_Dir = QLineEdit(self.ChildFrame_DAT_VITS_SRT_Dir)
        self.LineEdit_DAT_VITS_SRT_Dir.setObjectName(u"LineEdit_DAT_VITS_SRT_Dir")
        self.LineEdit_DAT_VITS_SRT_Dir.setMinimumSize(QSize(0, 27))
        self.LineEdit_DAT_VITS_SRT_Dir.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_19.addWidget(self.LineEdit_DAT_VITS_SRT_Dir)

        self.Button_DAT_VITS_SRT_Dir = QPushButton(self.ChildFrame_DAT_VITS_SRT_Dir)
        self.Button_DAT_VITS_SRT_Dir.setObjectName(u"Button_DAT_VITS_SRT_Dir")
        self.Button_DAT_VITS_SRT_Dir.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_SRT_Dir.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_19.addWidget(self.Button_DAT_VITS_SRT_Dir)


        self.verticalLayout_64.addWidget(self.ChildFrame_DAT_VITS_SRT_Dir)


        self.verticalLayout_29.addWidget(self.Frame_DAT_VITS_SRT_Dir)

        self.Frame_DAT_VITS_Add_AuxiliaryData = QFrame(self.Frame_BasicSettings_DAT_VITS)
        self.Frame_DAT_VITS_Add_AuxiliaryData.setObjectName(u"Frame_DAT_VITS_Add_AuxiliaryData")
        self.Frame_DAT_VITS_Add_AuxiliaryData.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_Add_AuxiliaryData.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_124 = QVBoxLayout(self.Frame_DAT_VITS_Add_AuxiliaryData)
        self.verticalLayout_124.setSpacing(12)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_Add_AuxiliaryData = QLabel(self.Frame_DAT_VITS_Add_AuxiliaryData)
        self.Label_DAT_VITS_Add_AuxiliaryData.setObjectName(u"Label_DAT_VITS_Add_AuxiliaryData")
        sizePolicy6.setHeightForWidth(self.Label_DAT_VITS_Add_AuxiliaryData.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_Add_AuxiliaryData.setSizePolicy(sizePolicy6)
        self.Label_DAT_VITS_Add_AuxiliaryData.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_124.addWidget(self.Label_DAT_VITS_Add_AuxiliaryData)

        self.CheckBox_DAT_VITS_Add_AuxiliaryData = QCheckBox(self.Frame_DAT_VITS_Add_AuxiliaryData)
        self.CheckBox_DAT_VITS_Add_AuxiliaryData.setObjectName(u"CheckBox_DAT_VITS_Add_AuxiliaryData")
        self.CheckBox_DAT_VITS_Add_AuxiliaryData.setMinimumSize(QSize(0, 27))
        self.CheckBox_DAT_VITS_Add_AuxiliaryData.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_124.addWidget(self.CheckBox_DAT_VITS_Add_AuxiliaryData)


        self.verticalLayout_29.addWidget(self.Frame_DAT_VITS_Add_AuxiliaryData)

        self.Frame_DAT_VITS_WAV_Dir_Split = QFrame(self.Frame_BasicSettings_DAT_VITS)
        self.Frame_DAT_VITS_WAV_Dir_Split.setObjectName(u"Frame_DAT_VITS_WAV_Dir_Split")
        self.Frame_DAT_VITS_WAV_Dir_Split.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_WAV_Dir_Split.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_63 = QVBoxLayout(self.Frame_DAT_VITS_WAV_Dir_Split)
        self.verticalLayout_63.setSpacing(12)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_WAV_Dir_Split = QLabel(self.Frame_DAT_VITS_WAV_Dir_Split)
        self.Label_DAT_VITS_WAV_Dir_Split.setObjectName(u"Label_DAT_VITS_WAV_Dir_Split")
        sizePolicy6.setHeightForWidth(self.Label_DAT_VITS_WAV_Dir_Split.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_WAV_Dir_Split.setSizePolicy(sizePolicy6)
        self.Label_DAT_VITS_WAV_Dir_Split.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_63.addWidget(self.Label_DAT_VITS_WAV_Dir_Split)

        self.ChildFrame_DAT_VITS_WAV_Dir_Split = QFrame(self.Frame_DAT_VITS_WAV_Dir_Split)
        self.ChildFrame_DAT_VITS_WAV_Dir_Split.setObjectName(u"ChildFrame_DAT_VITS_WAV_Dir_Split")
        sizePolicy6.setHeightForWidth(self.ChildFrame_DAT_VITS_WAV_Dir_Split.sizePolicy().hasHeightForWidth())
        self.ChildFrame_DAT_VITS_WAV_Dir_Split.setSizePolicy(sizePolicy6)
        self.ChildFrame_DAT_VITS_WAV_Dir_Split.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.ChildFrame_DAT_VITS_WAV_Dir_Split)
        self.horizontalLayout_18.setSpacing(12)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_DAT_VITS_WAV_Dir_Split = QLineEdit(self.ChildFrame_DAT_VITS_WAV_Dir_Split)
        self.LineEdit_DAT_VITS_WAV_Dir_Split.setObjectName(u"LineEdit_DAT_VITS_WAV_Dir_Split")
        self.LineEdit_DAT_VITS_WAV_Dir_Split.setMinimumSize(QSize(0, 27))
        self.LineEdit_DAT_VITS_WAV_Dir_Split.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_18.addWidget(self.LineEdit_DAT_VITS_WAV_Dir_Split)

        self.Button_DAT_VITS_WAV_Dir_Split = QPushButton(self.ChildFrame_DAT_VITS_WAV_Dir_Split)
        self.Button_DAT_VITS_WAV_Dir_Split.setObjectName(u"Button_DAT_VITS_WAV_Dir_Split")
        self.Button_DAT_VITS_WAV_Dir_Split.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_WAV_Dir_Split.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_18.addWidget(self.Button_DAT_VITS_WAV_Dir_Split)


        self.verticalLayout_63.addWidget(self.ChildFrame_DAT_VITS_WAV_Dir_Split)


        self.verticalLayout_29.addWidget(self.Frame_DAT_VITS_WAV_Dir_Split)

        self.Frame_DAT_VITS_FileList_Path_Training = QFrame(self.Frame_BasicSettings_DAT_VITS)
        self.Frame_DAT_VITS_FileList_Path_Training.setObjectName(u"Frame_DAT_VITS_FileList_Path_Training")
        self.Frame_DAT_VITS_FileList_Path_Training.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_FileList_Path_Training.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_66 = QVBoxLayout(self.Frame_DAT_VITS_FileList_Path_Training)
        self.verticalLayout_66.setSpacing(12)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_FileList_Path_Training = QLabel(self.Frame_DAT_VITS_FileList_Path_Training)
        self.Label_DAT_VITS_FileList_Path_Training.setObjectName(u"Label_DAT_VITS_FileList_Path_Training")
        sizePolicy6.setHeightForWidth(self.Label_DAT_VITS_FileList_Path_Training.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_FileList_Path_Training.setSizePolicy(sizePolicy6)
        self.Label_DAT_VITS_FileList_Path_Training.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_66.addWidget(self.Label_DAT_VITS_FileList_Path_Training)

        self.ChildFrame_DAT_VITS_FileList_Path_Training = QFrame(self.Frame_DAT_VITS_FileList_Path_Training)
        self.ChildFrame_DAT_VITS_FileList_Path_Training.setObjectName(u"ChildFrame_DAT_VITS_FileList_Path_Training")
        sizePolicy6.setHeightForWidth(self.ChildFrame_DAT_VITS_FileList_Path_Training.sizePolicy().hasHeightForWidth())
        self.ChildFrame_DAT_VITS_FileList_Path_Training.setSizePolicy(sizePolicy6)
        self.ChildFrame_DAT_VITS_FileList_Path_Training.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_20 = QHBoxLayout(self.ChildFrame_DAT_VITS_FileList_Path_Training)
        self.horizontalLayout_20.setSpacing(12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_DAT_VITS_FileList_Path_Training = QLineEdit(self.ChildFrame_DAT_VITS_FileList_Path_Training)
        self.LineEdit_DAT_VITS_FileList_Path_Training.setObjectName(u"LineEdit_DAT_VITS_FileList_Path_Training")
        self.LineEdit_DAT_VITS_FileList_Path_Training.setMinimumSize(QSize(0, 27))
        self.LineEdit_DAT_VITS_FileList_Path_Training.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_20.addWidget(self.LineEdit_DAT_VITS_FileList_Path_Training)

        self.Button_DAT_VITS_FileList_Path_Training = QPushButton(self.ChildFrame_DAT_VITS_FileList_Path_Training)
        self.Button_DAT_VITS_FileList_Path_Training.setObjectName(u"Button_DAT_VITS_FileList_Path_Training")
        self.Button_DAT_VITS_FileList_Path_Training.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileList_Path_Training.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_20.addWidget(self.Button_DAT_VITS_FileList_Path_Training)


        self.verticalLayout_66.addWidget(self.ChildFrame_DAT_VITS_FileList_Path_Training)


        self.verticalLayout_29.addWidget(self.Frame_DAT_VITS_FileList_Path_Training)

        self.Frame_DAT_VITS_FileList_Path_Validation = QFrame(self.Frame_BasicSettings_DAT_VITS)
        self.Frame_DAT_VITS_FileList_Path_Validation.setObjectName(u"Frame_DAT_VITS_FileList_Path_Validation")
        self.Frame_DAT_VITS_FileList_Path_Validation.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_FileList_Path_Validation.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_65 = QVBoxLayout(self.Frame_DAT_VITS_FileList_Path_Validation)
        self.verticalLayout_65.setSpacing(12)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_FileList_Path_Validation = QLabel(self.Frame_DAT_VITS_FileList_Path_Validation)
        self.Label_DAT_VITS_FileList_Path_Validation.setObjectName(u"Label_DAT_VITS_FileList_Path_Validation")
        sizePolicy6.setHeightForWidth(self.Label_DAT_VITS_FileList_Path_Validation.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_FileList_Path_Validation.setSizePolicy(sizePolicy6)
        self.Label_DAT_VITS_FileList_Path_Validation.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_65.addWidget(self.Label_DAT_VITS_FileList_Path_Validation)

        self.ChildFrame_DAT_VITS_FileList_Path_Validation = QFrame(self.Frame_DAT_VITS_FileList_Path_Validation)
        self.ChildFrame_DAT_VITS_FileList_Path_Validation.setObjectName(u"ChildFrame_DAT_VITS_FileList_Path_Validation")
        sizePolicy6.setHeightForWidth(self.ChildFrame_DAT_VITS_FileList_Path_Validation.sizePolicy().hasHeightForWidth())
        self.ChildFrame_DAT_VITS_FileList_Path_Validation.setSizePolicy(sizePolicy6)
        self.ChildFrame_DAT_VITS_FileList_Path_Validation.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_21 = QHBoxLayout(self.ChildFrame_DAT_VITS_FileList_Path_Validation)
        self.horizontalLayout_21.setSpacing(12)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_DAT_VITS_FileList_Path_Validation = QLineEdit(self.ChildFrame_DAT_VITS_FileList_Path_Validation)
        self.LineEdit_DAT_VITS_FileList_Path_Validation.setObjectName(u"LineEdit_DAT_VITS_FileList_Path_Validation")
        self.LineEdit_DAT_VITS_FileList_Path_Validation.setMinimumSize(QSize(0, 27))
        self.LineEdit_DAT_VITS_FileList_Path_Validation.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_21.addWidget(self.LineEdit_DAT_VITS_FileList_Path_Validation)

        self.Button_DAT_VITS_FileList_Path_Validation = QPushButton(self.ChildFrame_DAT_VITS_FileList_Path_Validation)
        self.Button_DAT_VITS_FileList_Path_Validation.setObjectName(u"Button_DAT_VITS_FileList_Path_Validation")
        self.Button_DAT_VITS_FileList_Path_Validation.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_FileList_Path_Validation.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_21.addWidget(self.Button_DAT_VITS_FileList_Path_Validation)


        self.verticalLayout_65.addWidget(self.ChildFrame_DAT_VITS_FileList_Path_Validation)


        self.verticalLayout_29.addWidget(self.Frame_DAT_VITS_FileList_Path_Validation)


        self.verticalLayout_111.addWidget(self.Frame_BasicSettings_DAT_VITS)

        self.CheckBox_Toggle_AdvanceSettings_DAT_VITS = QCheckBox(self.GroupBox_EssentialParams_DAT_VITS)
        self.CheckBox_Toggle_AdvanceSettings_DAT_VITS.setObjectName(u"CheckBox_Toggle_AdvanceSettings_DAT_VITS")
        self.CheckBox_Toggle_AdvanceSettings_DAT_VITS.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_111.addWidget(self.CheckBox_Toggle_AdvanceSettings_DAT_VITS)

        self.Frame_AdvanceSettings_DAT_VITS = QFrame(self.GroupBox_EssentialParams_DAT_VITS)
        self.Frame_AdvanceSettings_DAT_VITS.setObjectName(u"Frame_AdvanceSettings_DAT_VITS")
        self.Frame_AdvanceSettings_DAT_VITS.setFrameShape(QFrame.StyledPanel)
        self.Frame_AdvanceSettings_DAT_VITS.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.Frame_AdvanceSettings_DAT_VITS)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.Frame_DAT_VITS_TrainRatio = QFrame(self.Frame_AdvanceSettings_DAT_VITS)
        self.Frame_DAT_VITS_TrainRatio.setObjectName(u"Frame_DAT_VITS_TrainRatio")
        self.Frame_DAT_VITS_TrainRatio.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_TrainRatio.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_108 = QVBoxLayout(self.Frame_DAT_VITS_TrainRatio)
        self.verticalLayout_108.setSpacing(12)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_TrainRatio = QLabel(self.Frame_DAT_VITS_TrainRatio)
        self.Label_DAT_VITS_TrainRatio.setObjectName(u"Label_DAT_VITS_TrainRatio")
        sizePolicy6.setHeightForWidth(self.Label_DAT_VITS_TrainRatio.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_TrainRatio.setSizePolicy(sizePolicy6)
        self.Label_DAT_VITS_TrainRatio.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_108.addWidget(self.Label_DAT_VITS_TrainRatio)

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

        self.verticalLayout_108.addWidget(self.DoubleSpinBox_DAT_VITS_TrainRatio)


        self.verticalLayout_37.addWidget(self.Frame_DAT_VITS_TrainRatio)

        self.Frame_DAT_VITS_SampleRate = QFrame(self.Frame_AdvanceSettings_DAT_VITS)
        self.Frame_DAT_VITS_SampleRate.setObjectName(u"Frame_DAT_VITS_SampleRate")
        self.Frame_DAT_VITS_SampleRate.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SampleRate.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_165 = QVBoxLayout(self.Frame_DAT_VITS_SampleRate)
        self.verticalLayout_165.setSpacing(12)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.verticalLayout_165.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_SampleRate = QLabel(self.Frame_DAT_VITS_SampleRate)
        self.Label_DAT_VITS_SampleRate.setObjectName(u"Label_DAT_VITS_SampleRate")
        sizePolicy6.setHeightForWidth(self.Label_DAT_VITS_SampleRate.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_SampleRate.setSizePolicy(sizePolicy6)
        self.Label_DAT_VITS_SampleRate.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_165.addWidget(self.Label_DAT_VITS_SampleRate)

        self.ComboBox_DAT_VITS_SampleRate = QComboBox(self.Frame_DAT_VITS_SampleRate)
        self.ComboBox_DAT_VITS_SampleRate.setObjectName(u"ComboBox_DAT_VITS_SampleRate")
        self.ComboBox_DAT_VITS_SampleRate.setMinimumSize(QSize(0, 27))
        self.ComboBox_DAT_VITS_SampleRate.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
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
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding-left: -15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemV"
                        "iew::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-left: 15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120. 120, 120, 120)\n"
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
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
""
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
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:"
                        "hover {\n"
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
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScro"
                        "llArea QScrollBar::handle:horizontal:hover {\n"
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

        self.verticalLayout_165.addWidget(self.ComboBox_DAT_VITS_SampleRate)


        self.verticalLayout_37.addWidget(self.Frame_DAT_VITS_SampleRate)

        self.Frame_DAT_VITS_SampleWidth = QFrame(self.Frame_AdvanceSettings_DAT_VITS)
        self.Frame_DAT_VITS_SampleWidth.setObjectName(u"Frame_DAT_VITS_SampleWidth")
        self.Frame_DAT_VITS_SampleWidth.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_SampleWidth.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_62 = QVBoxLayout(self.Frame_DAT_VITS_SampleWidth)
        self.verticalLayout_62.setSpacing(12)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_SampleWidth = QLabel(self.Frame_DAT_VITS_SampleWidth)
        self.Label_DAT_VITS_SampleWidth.setObjectName(u"Label_DAT_VITS_SampleWidth")
        sizePolicy6.setHeightForWidth(self.Label_DAT_VITS_SampleWidth.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_SampleWidth.setSizePolicy(sizePolicy6)
        self.Label_DAT_VITS_SampleWidth.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_62.addWidget(self.Label_DAT_VITS_SampleWidth)

        self.ComboBox_DAT_VITS_SampleWidth = QComboBox(self.Frame_DAT_VITS_SampleWidth)
        self.ComboBox_DAT_VITS_SampleWidth.setObjectName(u"ComboBox_DAT_VITS_SampleWidth")
        self.ComboBox_DAT_VITS_SampleWidth.setMinimumSize(QSize(0, 27))
        self.ComboBox_DAT_VITS_SampleWidth.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
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
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding-left: -15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemV"
                        "iew::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-left: 15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120. 120, 120, 120)\n"
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
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
""
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
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:"
                        "hover {\n"
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
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScro"
                        "llArea QScrollBar::handle:horizontal:hover {\n"
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

        self.verticalLayout_62.addWidget(self.ComboBox_DAT_VITS_SampleWidth)


        self.verticalLayout_37.addWidget(self.Frame_DAT_VITS_SampleWidth)

        self.Frame_DAT_VITS_ToMono = QFrame(self.Frame_AdvanceSettings_DAT_VITS)
        self.Frame_DAT_VITS_ToMono.setObjectName(u"Frame_DAT_VITS_ToMono")
        self.Frame_DAT_VITS_ToMono.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_ToMono.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_122 = QVBoxLayout(self.Frame_DAT_VITS_ToMono)
        self.verticalLayout_122.setSpacing(12)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_ToMono = QLabel(self.Frame_DAT_VITS_ToMono)
        self.Label_DAT_VITS_ToMono.setObjectName(u"Label_DAT_VITS_ToMono")
        sizePolicy6.setHeightForWidth(self.Label_DAT_VITS_ToMono.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_ToMono.setSizePolicy(sizePolicy6)
        self.Label_DAT_VITS_ToMono.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_122.addWidget(self.Label_DAT_VITS_ToMono)

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

        self.verticalLayout_122.addWidget(self.CheckBox_DAT_VITS_ToMono)


        self.verticalLayout_37.addWidget(self.Frame_DAT_VITS_ToMono)

        self.Frame_DAT_VITS_AuxiliaryData_Path = QFrame(self.Frame_AdvanceSettings_DAT_VITS)
        self.Frame_DAT_VITS_AuxiliaryData_Path.setObjectName(u"Frame_DAT_VITS_AuxiliaryData_Path")
        self.Frame_DAT_VITS_AuxiliaryData_Path.setMinimumSize(QSize(0, 105))
        self.Frame_DAT_VITS_AuxiliaryData_Path.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_164 = QVBoxLayout(self.Frame_DAT_VITS_AuxiliaryData_Path)
        self.verticalLayout_164.setSpacing(12)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.verticalLayout_164.setContentsMargins(21, 12, 21, 12)
        self.Label_DAT_VITS_AuxiliaryData_Path = QLabel(self.Frame_DAT_VITS_AuxiliaryData_Path)
        self.Label_DAT_VITS_AuxiliaryData_Path.setObjectName(u"Label_DAT_VITS_AuxiliaryData_Path")
        sizePolicy6.setHeightForWidth(self.Label_DAT_VITS_AuxiliaryData_Path.sizePolicy().hasHeightForWidth())
        self.Label_DAT_VITS_AuxiliaryData_Path.setSizePolicy(sizePolicy6)
        self.Label_DAT_VITS_AuxiliaryData_Path.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_164.addWidget(self.Label_DAT_VITS_AuxiliaryData_Path)

        self.ChildFrame_DAT_VITS_AuxiliaryData_Path = QFrame(self.Frame_DAT_VITS_AuxiliaryData_Path)
        self.ChildFrame_DAT_VITS_AuxiliaryData_Path.setObjectName(u"ChildFrame_DAT_VITS_AuxiliaryData_Path")
        sizePolicy6.setHeightForWidth(self.ChildFrame_DAT_VITS_AuxiliaryData_Path.sizePolicy().hasHeightForWidth())
        self.ChildFrame_DAT_VITS_AuxiliaryData_Path.setSizePolicy(sizePolicy6)
        self.ChildFrame_DAT_VITS_AuxiliaryData_Path.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_80 = QHBoxLayout(self.ChildFrame_DAT_VITS_AuxiliaryData_Path)
        self.horizontalLayout_80.setSpacing(12)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_DAT_VITS_AuxiliaryData_Path = QLineEdit(self.ChildFrame_DAT_VITS_AuxiliaryData_Path)
        self.LineEdit_DAT_VITS_AuxiliaryData_Path.setObjectName(u"LineEdit_DAT_VITS_AuxiliaryData_Path")
        self.LineEdit_DAT_VITS_AuxiliaryData_Path.setMinimumSize(QSize(0, 27))
        self.LineEdit_DAT_VITS_AuxiliaryData_Path.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_80.addWidget(self.LineEdit_DAT_VITS_AuxiliaryData_Path)

        self.Button_DAT_VITS_AuxiliaryData_Path = QPushButton(self.ChildFrame_DAT_VITS_AuxiliaryData_Path)
        self.Button_DAT_VITS_AuxiliaryData_Path.setObjectName(u"Button_DAT_VITS_AuxiliaryData_Path")
        self.Button_DAT_VITS_AuxiliaryData_Path.setMinimumSize(QSize(27, 27))
        self.Button_DAT_VITS_AuxiliaryData_Path.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_80.addWidget(self.Button_DAT_VITS_AuxiliaryData_Path)


        self.verticalLayout_164.addWidget(self.ChildFrame_DAT_VITS_AuxiliaryData_Path)


        self.verticalLayout_37.addWidget(self.Frame_DAT_VITS_AuxiliaryData_Path)


        self.verticalLayout_111.addWidget(self.Frame_AdvanceSettings_DAT_VITS)


        self.verticalLayout_36.addWidget(self.GroupBox_EssentialParams_DAT_VITS)

        self.VerticalSpacer_DAT_VITS = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.VerticalSpacer_DAT_VITS)

        self.ScrollArea_Middle_DAT_VITS.setWidget(self.ScrollArea_Middle_WidgetContents_DAT_VITS)

        self.gridLayout_8.addWidget(self.ScrollArea_Middle_DAT_VITS, 0, 1, 1, 1)

        self.Widget_Right_DAT_VITS = QWidget(self.Subpage_DAT_VITS)
        self.Widget_Right_DAT_VITS.setObjectName(u"Widget_Right_DAT_VITS")
        self.Widget_Right_DAT_VITS.setMinimumSize(QSize(210, 0))
        self.Widget_Right_DAT_VITS.setMaximumSize(QSize(420, 16777215))
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
"	background-color: rgb(33, 33, 33);\n"
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
"	border-st"
                        "yle: solid;\n"
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
"	width: 0px;\n"
""
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

        self.Button_SyncParams_DAT_VITS = QPushButton(self.Widget_Right_DAT_VITS)
        self.Button_SyncParams_DAT_VITS.setObjectName(u"Button_SyncParams_DAT_VITS")
        self.Button_SyncParams_DAT_VITS.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_16.addWidget(self.Button_SyncParams_DAT_VITS, 1, 0, 1, 1)

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

        self.gridLayout_16.addWidget(self.Button_CheckOutput_DAT_VITS, 1, 1, 1, 1)


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
        sizePolicy7.setHeightForWidth(self.Button_DAT_VITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_DAT_VITS_Execute.setSizePolicy(sizePolicy7)
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
        sizePolicy7.setHeightForWidth(self.Button_DAT_VITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_DAT_VITS_Terminate.setSizePolicy(sizePolicy7)
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
        self.Widget_Left_Train_VITS = QWidget(self.Subpage_Train_VITS)
        self.Widget_Left_Train_VITS.setObjectName(u"Widget_Left_Train_VITS")
        self.Widget_Left_Train_VITS.setMinimumSize(QSize(150, 0))
        self.Widget_Left_Train_VITS.setMaximumSize(QSize(210, 16777215))
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
        self.TreeWidget_Catalogue_Train_VITS.setStyleSheet(u"QTreeWidget {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"	background-color: transparent;\n"
"	padding: 1.2px;\n"
"}\n"
"\n"
"QTreeWidget::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeWidget::branch:open:has-children:has-siblings,\n"
"QTreeWidget::branch:open:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:closed:has-children:has-siblings,\n"
"QTreeWidget::branch:closed:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:!has-children:has-siblings:adjoins-item,\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    image: ;\n"
"}\n"
"\n"
"\n"
"QTreeView {\n"
"}\n"
"\n"
"QTreeView::item{\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
""
                        "QTreeView::item:selected:active{\n"
"    background-color: ;\n"
"}\n"
"QTreeView::item:selected:!active {\n"
"    background-color: ;\n"
"}\n"
"\n"
"/*\n"
"QHeaderView {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QHeaderView:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: transparent;\n"
"}\n"
"QHeaderView::section:checked {\n"
"	background-color: ;\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}*/\n"
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
"	background-color: rgba(33, 3"
                        "3, 33, 99);\n"
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
"	border"
                        "-radius: 6px;\n"
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
"	backgro"
                        "und-color: rgb(120, 120, 120);\n"
"}")

        self.verticalLayout_10.addWidget(self.TreeWidget_Catalogue_Train_VITS)


        self.gridLayout_22.addWidget(self.Widget_Left_Train_VITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_Train_VITS = QScrollArea(self.Subpage_Train_VITS)
        self.ScrollArea_Middle_Train_VITS.setObjectName(u"ScrollArea_Middle_Train_VITS")
        sizePolicy5.setHeightForWidth(self.ScrollArea_Middle_Train_VITS.sizePolicy().hasHeightForWidth())
        self.ScrollArea_Middle_Train_VITS.setSizePolicy(sizePolicy5)
        self.ScrollArea_Middle_Train_VITS.setMinimumSize(QSize(630, 0))
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
        self.ScrollArea_Middle_WidgetContents_Train_VITS.setGeometry(QRect(0, 0, 621, 1543))
        self.verticalLayout_18 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.verticalLayout_18.setSpacing(12)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_Train_VITS = QGroupBox(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.GroupBox_EssentialParams_Train_VITS.setObjectName(u"GroupBox_EssentialParams_Train_VITS")
        self.GroupBox_EssentialParams_Train_VITS.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_114 = QVBoxLayout(self.GroupBox_EssentialParams_Train_VITS)
        self.verticalLayout_114.setSpacing(0)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_Train_VITS = QCheckBox(self.GroupBox_EssentialParams_Train_VITS)
        self.CheckBox_Toggle_BasicSettings_Train_VITS.setObjectName(u"CheckBox_Toggle_BasicSettings_Train_VITS")
        self.CheckBox_Toggle_BasicSettings_Train_VITS.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_114.addWidget(self.CheckBox_Toggle_BasicSettings_Train_VITS)

        self.Frame_BasicSettings_Train_VITS = QFrame(self.GroupBox_EssentialParams_Train_VITS)
        self.Frame_BasicSettings_Train_VITS.setObjectName(u"Frame_BasicSettings_Train_VITS")
        self.verticalLayout_17 = QVBoxLayout(self.Frame_BasicSettings_Train_VITS)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_FileList_Path_Training = QFrame(self.Frame_BasicSettings_Train_VITS)
        self.Frame_Train_VITS_FileList_Path_Training.setObjectName(u"Frame_Train_VITS_FileList_Path_Training")
        self.Frame_Train_VITS_FileList_Path_Training.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_FileList_Path_Training.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_69 = QVBoxLayout(self.Frame_Train_VITS_FileList_Path_Training)
        self.verticalLayout_69.setSpacing(12)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_FileList_Path_Training = QLabel(self.Frame_Train_VITS_FileList_Path_Training)
        self.Label_Train_VITS_FileList_Path_Training.setObjectName(u"Label_Train_VITS_FileList_Path_Training")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_FileList_Path_Training.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_FileList_Path_Training.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_FileList_Path_Training.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_69.addWidget(self.Label_Train_VITS_FileList_Path_Training)

        self.ChildFrame_Train_VITS_FileList_Path_Training = QFrame(self.Frame_Train_VITS_FileList_Path_Training)
        self.ChildFrame_Train_VITS_FileList_Path_Training.setObjectName(u"ChildFrame_Train_VITS_FileList_Path_Training")
        sizePolicy6.setHeightForWidth(self.ChildFrame_Train_VITS_FileList_Path_Training.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Train_VITS_FileList_Path_Training.setSizePolicy(sizePolicy6)
        self.ChildFrame_Train_VITS_FileList_Path_Training.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_22 = QHBoxLayout(self.ChildFrame_Train_VITS_FileList_Path_Training)
        self.horizontalLayout_22.setSpacing(12)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Train_VITS_FileList_Path_Training = QLineEdit(self.ChildFrame_Train_VITS_FileList_Path_Training)
        self.LineEdit_Train_VITS_FileList_Path_Training.setObjectName(u"LineEdit_Train_VITS_FileList_Path_Training")
        self.LineEdit_Train_VITS_FileList_Path_Training.setMinimumSize(QSize(0, 27))
        self.LineEdit_Train_VITS_FileList_Path_Training.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_22.addWidget(self.LineEdit_Train_VITS_FileList_Path_Training)

        self.Button_Train_VITS_FileList_Path_Training = QPushButton(self.ChildFrame_Train_VITS_FileList_Path_Training)
        self.Button_Train_VITS_FileList_Path_Training.setObjectName(u"Button_Train_VITS_FileList_Path_Training")
        self.Button_Train_VITS_FileList_Path_Training.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_FileList_Path_Training.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_22.addWidget(self.Button_Train_VITS_FileList_Path_Training)


        self.verticalLayout_69.addWidget(self.ChildFrame_Train_VITS_FileList_Path_Training)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_FileList_Path_Training)

        self.Frame_Train_VITS_FileList_Path_Validation = QFrame(self.Frame_BasicSettings_Train_VITS)
        self.Frame_Train_VITS_FileList_Path_Validation.setObjectName(u"Frame_Train_VITS_FileList_Path_Validation")
        self.Frame_Train_VITS_FileList_Path_Validation.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_FileList_Path_Validation.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_70 = QVBoxLayout(self.Frame_Train_VITS_FileList_Path_Validation)
        self.verticalLayout_70.setSpacing(12)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_FileList_Path_Validation = QLabel(self.Frame_Train_VITS_FileList_Path_Validation)
        self.Label_Train_VITS_FileList_Path_Validation.setObjectName(u"Label_Train_VITS_FileList_Path_Validation")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_FileList_Path_Validation.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_FileList_Path_Validation.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_FileList_Path_Validation.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_70.addWidget(self.Label_Train_VITS_FileList_Path_Validation)

        self.ChildFrame_Train_VITS_FileList_Path_Validation = QFrame(self.Frame_Train_VITS_FileList_Path_Validation)
        self.ChildFrame_Train_VITS_FileList_Path_Validation.setObjectName(u"ChildFrame_Train_VITS_FileList_Path_Validation")
        sizePolicy6.setHeightForWidth(self.ChildFrame_Train_VITS_FileList_Path_Validation.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Train_VITS_FileList_Path_Validation.setSizePolicy(sizePolicy6)
        self.ChildFrame_Train_VITS_FileList_Path_Validation.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_23 = QHBoxLayout(self.ChildFrame_Train_VITS_FileList_Path_Validation)
        self.horizontalLayout_23.setSpacing(12)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Train_VITS_FileList_Path_Validation = QLineEdit(self.ChildFrame_Train_VITS_FileList_Path_Validation)
        self.LineEdit_Train_VITS_FileList_Path_Validation.setObjectName(u"LineEdit_Train_VITS_FileList_Path_Validation")
        self.LineEdit_Train_VITS_FileList_Path_Validation.setMinimumSize(QSize(0, 27))
        self.LineEdit_Train_VITS_FileList_Path_Validation.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_23.addWidget(self.LineEdit_Train_VITS_FileList_Path_Validation)

        self.Button_Train_VITS_FileList_Path_Validation = QPushButton(self.ChildFrame_Train_VITS_FileList_Path_Validation)
        self.Button_Train_VITS_FileList_Path_Validation.setObjectName(u"Button_Train_VITS_FileList_Path_Validation")
        self.Button_Train_VITS_FileList_Path_Validation.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_FileList_Path_Validation.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_23.addWidget(self.Button_Train_VITS_FileList_Path_Validation)


        self.verticalLayout_70.addWidget(self.ChildFrame_Train_VITS_FileList_Path_Validation)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_FileList_Path_Validation)

        self.Frame_Train_VITS_Epochs = QFrame(self.Frame_BasicSettings_Train_VITS)
        self.Frame_Train_VITS_Epochs.setObjectName(u"Frame_Train_VITS_Epochs")
        self.Frame_Train_VITS_Epochs.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Epochs.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_73 = QVBoxLayout(self.Frame_Train_VITS_Epochs)
        self.verticalLayout_73.setSpacing(2)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Epochs = QLabel(self.Frame_Train_VITS_Epochs)
        self.Label_Train_VITS_Epochs.setObjectName(u"Label_Train_VITS_Epochs")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_Epochs.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Epochs.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_Epochs.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_73.addWidget(self.Label_Train_VITS_Epochs)

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

        self.verticalLayout_73.addWidget(self.SpinBox_Train_VITS_Epochs)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_Epochs)

        self.Frame_Train_VITS_Batch_Size = QFrame(self.Frame_BasicSettings_Train_VITS)
        self.Frame_Train_VITS_Batch_Size.setObjectName(u"Frame_Train_VITS_Batch_Size")
        self.Frame_Train_VITS_Batch_Size.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Batch_Size.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_74 = QVBoxLayout(self.Frame_Train_VITS_Batch_Size)
        self.verticalLayout_74.setSpacing(12)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Batch_Size = QLabel(self.Frame_Train_VITS_Batch_Size)
        self.Label_Train_VITS_Batch_Size.setObjectName(u"Label_Train_VITS_Batch_Size")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_Batch_Size.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Batch_Size.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_Batch_Size.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_74.addWidget(self.Label_Train_VITS_Batch_Size)

        self.SpinBox_Train_VITS_Batch_Size = QSpinBox(self.Frame_Train_VITS_Batch_Size)
        self.SpinBox_Train_VITS_Batch_Size.setObjectName(u"SpinBox_Train_VITS_Batch_Size")
        self.SpinBox_Train_VITS_Batch_Size.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_Batch_Size.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Train_VITS_Batch_Size.setMinimum(-999999)
        self.SpinBox_Train_VITS_Batch_Size.setMaximum(999999)

        self.verticalLayout_74.addWidget(self.SpinBox_Train_VITS_Batch_Size)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_Batch_Size)

        self.Frame_Train_VITS_Use_PretrainedModels = QFrame(self.Frame_BasicSettings_Train_VITS)
        self.Frame_Train_VITS_Use_PretrainedModels.setObjectName(u"Frame_Train_VITS_Use_PretrainedModels")
        self.Frame_Train_VITS_Use_PretrainedModels.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Use_PretrainedModels.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_45 = QVBoxLayout(self.Frame_Train_VITS_Use_PretrainedModels)
        self.verticalLayout_45.setSpacing(12)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Use_PretrainedModels = QLabel(self.Frame_Train_VITS_Use_PretrainedModels)
        self.Label_Train_VITS_Use_PretrainedModels.setObjectName(u"Label_Train_VITS_Use_PretrainedModels")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_Use_PretrainedModels.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Use_PretrainedModels.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_Use_PretrainedModels.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_45.addWidget(self.Label_Train_VITS_Use_PretrainedModels)

        self.CheckBox_Train_VITS_Use_PretrainedModels = QCheckBox(self.Frame_Train_VITS_Use_PretrainedModels)
        self.CheckBox_Train_VITS_Use_PretrainedModels.setObjectName(u"CheckBox_Train_VITS_Use_PretrainedModels")
        self.CheckBox_Train_VITS_Use_PretrainedModels.setMinimumSize(QSize(0, 27))
        self.CheckBox_Train_VITS_Use_PretrainedModels.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_45.addWidget(self.CheckBox_Train_VITS_Use_PretrainedModels)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_Use_PretrainedModels)

        self.Frame_Train_VITS_Output_Dir = QFrame(self.Frame_BasicSettings_Train_VITS)
        self.Frame_Train_VITS_Output_Dir.setObjectName(u"Frame_Train_VITS_Output_Dir")
        self.Frame_Train_VITS_Output_Dir.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Output_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_82 = QVBoxLayout(self.Frame_Train_VITS_Output_Dir)
        self.verticalLayout_82.setSpacing(12)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Output_Dir = QLabel(self.Frame_Train_VITS_Output_Dir)
        self.Label_Train_VITS_Output_Dir.setObjectName(u"Label_Train_VITS_Output_Dir")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_Output_Dir.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Output_Dir.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_Output_Dir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_82.addWidget(self.Label_Train_VITS_Output_Dir)

        self.ChildFrame_Train_VITS_Output_Dir = QFrame(self.Frame_Train_VITS_Output_Dir)
        self.ChildFrame_Train_VITS_Output_Dir.setObjectName(u"ChildFrame_Train_VITS_Output_Dir")
        sizePolicy6.setHeightForWidth(self.ChildFrame_Train_VITS_Output_Dir.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Train_VITS_Output_Dir.setSizePolicy(sizePolicy6)
        self.ChildFrame_Train_VITS_Output_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_25 = QHBoxLayout(self.ChildFrame_Train_VITS_Output_Dir)
        self.horizontalLayout_25.setSpacing(12)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Train_VITS_Output_Dir = QLineEdit(self.ChildFrame_Train_VITS_Output_Dir)
        self.LineEdit_Train_VITS_Output_Dir.setObjectName(u"LineEdit_Train_VITS_Output_Dir")
        self.LineEdit_Train_VITS_Output_Dir.setMinimumSize(QSize(0, 27))
        self.LineEdit_Train_VITS_Output_Dir.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_25.addWidget(self.LineEdit_Train_VITS_Output_Dir)

        self.Button_Train_VITS_Output_Dir = QPushButton(self.ChildFrame_Train_VITS_Output_Dir)
        self.Button_Train_VITS_Output_Dir.setObjectName(u"Button_Train_VITS_Output_Dir")
        self.Button_Train_VITS_Output_Dir.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_Output_Dir.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_25.addWidget(self.Button_Train_VITS_Output_Dir)


        self.verticalLayout_82.addWidget(self.ChildFrame_Train_VITS_Output_Dir)


        self.verticalLayout_17.addWidget(self.Frame_Train_VITS_Output_Dir)


        self.verticalLayout_114.addWidget(self.Frame_BasicSettings_Train_VITS)

        self.CheckBox_Toggle_AdvanceSettings_Train_VITS = QCheckBox(self.GroupBox_EssentialParams_Train_VITS)
        self.CheckBox_Toggle_AdvanceSettings_Train_VITS.setObjectName(u"CheckBox_Toggle_AdvanceSettings_Train_VITS")
        self.CheckBox_Toggle_AdvanceSettings_Train_VITS.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_114.addWidget(self.CheckBox_Toggle_AdvanceSettings_Train_VITS)

        self.Frame_AdvanceSettings_Train_VITS = QFrame(self.GroupBox_EssentialParams_Train_VITS)
        self.Frame_AdvanceSettings_Train_VITS.setObjectName(u"Frame_AdvanceSettings_Train_VITS")
        self.Frame_AdvanceSettings_Train_VITS.setFrameShape(QFrame.StyledPanel)
        self.Frame_AdvanceSettings_Train_VITS.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.Frame_AdvanceSettings_Train_VITS)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_Eval_Interval = QFrame(self.Frame_AdvanceSettings_Train_VITS)
        self.Frame_Train_VITS_Eval_Interval.setObjectName(u"Frame_Train_VITS_Eval_Interval")
        self.Frame_Train_VITS_Eval_Interval.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Eval_Interval.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_72 = QVBoxLayout(self.Frame_Train_VITS_Eval_Interval)
        self.verticalLayout_72.setSpacing(12)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Eval_Interval = QLabel(self.Frame_Train_VITS_Eval_Interval)
        self.Label_Train_VITS_Eval_Interval.setObjectName(u"Label_Train_VITS_Eval_Interval")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_Eval_Interval.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Eval_Interval.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_Eval_Interval.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_72.addWidget(self.Label_Train_VITS_Eval_Interval)

        self.SpinBox_Train_VITS_Eval_Interval = QSpinBox(self.Frame_Train_VITS_Eval_Interval)
        self.SpinBox_Train_VITS_Eval_Interval.setObjectName(u"SpinBox_Train_VITS_Eval_Interval")
        self.SpinBox_Train_VITS_Eval_Interval.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_Eval_Interval.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Train_VITS_Eval_Interval.setMinimum(-999999)
        self.SpinBox_Train_VITS_Eval_Interval.setMaximum(999999)

        self.verticalLayout_72.addWidget(self.SpinBox_Train_VITS_Eval_Interval)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_Eval_Interval)

        self.Frame_Train_VITS_Num_Workers = QFrame(self.Frame_AdvanceSettings_Train_VITS)
        self.Frame_Train_VITS_Num_Workers.setObjectName(u"Frame_Train_VITS_Num_Workers")
        self.Frame_Train_VITS_Num_Workers.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Num_Workers.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_75 = QVBoxLayout(self.Frame_Train_VITS_Num_Workers)
        self.verticalLayout_75.setSpacing(12)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Num_Workers = QLabel(self.Frame_Train_VITS_Num_Workers)
        self.Label_Train_VITS_Num_Workers.setObjectName(u"Label_Train_VITS_Num_Workers")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_Num_Workers.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Num_Workers.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_Num_Workers.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_75.addWidget(self.Label_Train_VITS_Num_Workers)

        self.SpinBox_Train_VITS_Num_Workers = QSpinBox(self.Frame_Train_VITS_Num_Workers)
        self.SpinBox_Train_VITS_Num_Workers.setObjectName(u"SpinBox_Train_VITS_Num_Workers")
        self.SpinBox_Train_VITS_Num_Workers.setMinimumSize(QSize(0, 27))
        self.SpinBox_Train_VITS_Num_Workers.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Train_VITS_Num_Workers.setMinimum(-999999)
        self.SpinBox_Train_VITS_Num_Workers.setMaximum(999999)

        self.verticalLayout_75.addWidget(self.SpinBox_Train_VITS_Num_Workers)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_Num_Workers)

        self.Frame_Train_VITS_FP16_Run = QFrame(self.Frame_AdvanceSettings_Train_VITS)
        self.Frame_Train_VITS_FP16_Run.setObjectName(u"Frame_Train_VITS_FP16_Run")
        self.Frame_Train_VITS_FP16_Run.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_FP16_Run.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_76 = QVBoxLayout(self.Frame_Train_VITS_FP16_Run)
        self.verticalLayout_76.setSpacing(12)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_FP16_Run = QLabel(self.Frame_Train_VITS_FP16_Run)
        self.Label_Train_VITS_FP16_Run.setObjectName(u"Label_Train_VITS_FP16_Run")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_FP16_Run.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_FP16_Run.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_FP16_Run.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_76.addWidget(self.Label_Train_VITS_FP16_Run)

        self.CheckBox_Train_VITS_FP16_Run = QCheckBox(self.Frame_Train_VITS_FP16_Run)
        self.CheckBox_Train_VITS_FP16_Run.setObjectName(u"CheckBox_Train_VITS_FP16_Run")
        self.CheckBox_Train_VITS_FP16_Run.setMinimumSize(QSize(0, 27))
        self.CheckBox_Train_VITS_FP16_Run.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_76.addWidget(self.CheckBox_Train_VITS_FP16_Run)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_FP16_Run)

        self.Frame_Train_VITS_Model_Path_Pretrained_G = QFrame(self.Frame_AdvanceSettings_Train_VITS)
        self.Frame_Train_VITS_Model_Path_Pretrained_G.setObjectName(u"Frame_Train_VITS_Model_Path_Pretrained_G")
        self.Frame_Train_VITS_Model_Path_Pretrained_G.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Model_Path_Pretrained_G.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_84 = QVBoxLayout(self.Frame_Train_VITS_Model_Path_Pretrained_G)
        self.verticalLayout_84.setSpacing(12)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Model_Path_Pretrained_G = QLabel(self.Frame_Train_VITS_Model_Path_Pretrained_G)
        self.Label_Train_VITS_Model_Path_Pretrained_G.setObjectName(u"Label_Train_VITS_Model_Path_Pretrained_G")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_Model_Path_Pretrained_G.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Model_Path_Pretrained_G.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_Model_Path_Pretrained_G.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_84.addWidget(self.Label_Train_VITS_Model_Path_Pretrained_G)

        self.ChildFrame_Train_VITS_Model_Path_Pretrained_G = QFrame(self.Frame_Train_VITS_Model_Path_Pretrained_G)
        self.ChildFrame_Train_VITS_Model_Path_Pretrained_G.setObjectName(u"ChildFrame_Train_VITS_Model_Path_Pretrained_G")
        sizePolicy6.setHeightForWidth(self.ChildFrame_Train_VITS_Model_Path_Pretrained_G.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Train_VITS_Model_Path_Pretrained_G.setSizePolicy(sizePolicy6)
        self.ChildFrame_Train_VITS_Model_Path_Pretrained_G.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_27 = QHBoxLayout(self.ChildFrame_Train_VITS_Model_Path_Pretrained_G)
        self.horizontalLayout_27.setSpacing(12)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Train_VITS_Model_Path_Pretrained_G = QLineEdit(self.ChildFrame_Train_VITS_Model_Path_Pretrained_G)
        self.LineEdit_Train_VITS_Model_Path_Pretrained_G.setObjectName(u"LineEdit_Train_VITS_Model_Path_Pretrained_G")
        self.LineEdit_Train_VITS_Model_Path_Pretrained_G.setMinimumSize(QSize(0, 27))
        self.LineEdit_Train_VITS_Model_Path_Pretrained_G.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_27.addWidget(self.LineEdit_Train_VITS_Model_Path_Pretrained_G)

        self.Button_Train_VITS_Model_Path_Pretrained_G = QPushButton(self.ChildFrame_Train_VITS_Model_Path_Pretrained_G)
        self.Button_Train_VITS_Model_Path_Pretrained_G.setObjectName(u"Button_Train_VITS_Model_Path_Pretrained_G")
        self.Button_Train_VITS_Model_Path_Pretrained_G.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_Model_Path_Pretrained_G.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_27.addWidget(self.Button_Train_VITS_Model_Path_Pretrained_G)


        self.verticalLayout_84.addWidget(self.ChildFrame_Train_VITS_Model_Path_Pretrained_G)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_Model_Path_Pretrained_G)

        self.Frame_Train_VITS_Model_Path_Pretrained_D = QFrame(self.Frame_AdvanceSettings_Train_VITS)
        self.Frame_Train_VITS_Model_Path_Pretrained_D.setObjectName(u"Frame_Train_VITS_Model_Path_Pretrained_D")
        self.Frame_Train_VITS_Model_Path_Pretrained_D.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Model_Path_Pretrained_D.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_85 = QVBoxLayout(self.Frame_Train_VITS_Model_Path_Pretrained_D)
        self.verticalLayout_85.setSpacing(12)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Model_Path_Pretrained_D = QLabel(self.Frame_Train_VITS_Model_Path_Pretrained_D)
        self.Label_Train_VITS_Model_Path_Pretrained_D.setObjectName(u"Label_Train_VITS_Model_Path_Pretrained_D")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_Model_Path_Pretrained_D.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Model_Path_Pretrained_D.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_Model_Path_Pretrained_D.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_85.addWidget(self.Label_Train_VITS_Model_Path_Pretrained_D)

        self.ChildFrame_Train_VITS_Model_Path_Pretrained_D = QFrame(self.Frame_Train_VITS_Model_Path_Pretrained_D)
        self.ChildFrame_Train_VITS_Model_Path_Pretrained_D.setObjectName(u"ChildFrame_Train_VITS_Model_Path_Pretrained_D")
        sizePolicy6.setHeightForWidth(self.ChildFrame_Train_VITS_Model_Path_Pretrained_D.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Train_VITS_Model_Path_Pretrained_D.setSizePolicy(sizePolicy6)
        self.ChildFrame_Train_VITS_Model_Path_Pretrained_D.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_28 = QHBoxLayout(self.ChildFrame_Train_VITS_Model_Path_Pretrained_D)
        self.horizontalLayout_28.setSpacing(12)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Train_VITS_Model_Path_Pretrained_D = QLineEdit(self.ChildFrame_Train_VITS_Model_Path_Pretrained_D)
        self.LineEdit_Train_VITS_Model_Path_Pretrained_D.setObjectName(u"LineEdit_Train_VITS_Model_Path_Pretrained_D")
        self.LineEdit_Train_VITS_Model_Path_Pretrained_D.setMinimumSize(QSize(0, 27))
        self.LineEdit_Train_VITS_Model_Path_Pretrained_D.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_28.addWidget(self.LineEdit_Train_VITS_Model_Path_Pretrained_D)

        self.Button_Train_VITS_Model_Path_Pretrained_D = QPushButton(self.ChildFrame_Train_VITS_Model_Path_Pretrained_D)
        self.Button_Train_VITS_Model_Path_Pretrained_D.setObjectName(u"Button_Train_VITS_Model_Path_Pretrained_D")
        self.Button_Train_VITS_Model_Path_Pretrained_D.setMinimumSize(QSize(27, 27))
        self.Button_Train_VITS_Model_Path_Pretrained_D.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_28.addWidget(self.Button_Train_VITS_Model_Path_Pretrained_D)


        self.verticalLayout_85.addWidget(self.ChildFrame_Train_VITS_Model_Path_Pretrained_D)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_Model_Path_Pretrained_D)

        self.Frame_Train_VITS_Keep_Original_Speakers = QFrame(self.Frame_AdvanceSettings_Train_VITS)
        self.Frame_Train_VITS_Keep_Original_Speakers.setObjectName(u"Frame_Train_VITS_Keep_Original_Speakers")
        self.Frame_Train_VITS_Keep_Original_Speakers.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Keep_Original_Speakers.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_26 = QVBoxLayout(self.Frame_Train_VITS_Keep_Original_Speakers)
        self.verticalLayout_26.setSpacing(12)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Keep_Original_Speakers = QLabel(self.Frame_Train_VITS_Keep_Original_Speakers)
        self.Label_Train_VITS_Keep_Original_Speakers.setObjectName(u"Label_Train_VITS_Keep_Original_Speakers")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_Keep_Original_Speakers.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Keep_Original_Speakers.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_Keep_Original_Speakers.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_26.addWidget(self.Label_Train_VITS_Keep_Original_Speakers)

        self.CheckBox_Train_VITS_Keep_Original_Speakers = QCheckBox(self.Frame_Train_VITS_Keep_Original_Speakers)
        self.CheckBox_Train_VITS_Keep_Original_Speakers.setObjectName(u"CheckBox_Train_VITS_Keep_Original_Speakers")
        self.CheckBox_Train_VITS_Keep_Original_Speakers.setMinimumSize(QSize(0, 27))
        self.CheckBox_Train_VITS_Keep_Original_Speakers.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_26.addWidget(self.CheckBox_Train_VITS_Keep_Original_Speakers)


        self.verticalLayout_35.addWidget(self.Frame_Train_VITS_Keep_Original_Speakers)


        self.verticalLayout_114.addWidget(self.Frame_AdvanceSettings_Train_VITS)


        self.verticalLayout_18.addWidget(self.GroupBox_EssentialParams_Train_VITS)

        self.GroupBox_OptionalParams_Train_VITS = QGroupBox(self.ScrollArea_Middle_WidgetContents_Train_VITS)
        self.GroupBox_OptionalParams_Train_VITS.setObjectName(u"GroupBox_OptionalParams_Train_VITS")
        self.GroupBox_OptionalParams_Train_VITS.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_34 = QVBoxLayout(self.GroupBox_OptionalParams_Train_VITS)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 12, 0, 12)
        self.Frame_OptionalSettings_Train_VITS = QFrame(self.GroupBox_OptionalParams_Train_VITS)
        self.Frame_OptionalSettings_Train_VITS.setObjectName(u"Frame_OptionalSettings_Train_VITS")
        self.Frame_OptionalSettings_Train_VITS.setFrameShape(QFrame.StyledPanel)
        self.Frame_OptionalSettings_Train_VITS.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.Frame_OptionalSettings_Train_VITS)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.Frame_Train_VITS_Speakers = QFrame(self.Frame_OptionalSettings_Train_VITS)
        self.Frame_Train_VITS_Speakers.setObjectName(u"Frame_Train_VITS_Speakers")
        self.Frame_Train_VITS_Speakers.setMinimumSize(QSize(0, 105))
        self.Frame_Train_VITS_Speakers.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_88 = QVBoxLayout(self.Frame_Train_VITS_Speakers)
        self.verticalLayout_88.setSpacing(12)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(21, 12, 21, 12)
        self.Label_Train_VITS_Speakers = QLabel(self.Frame_Train_VITS_Speakers)
        self.Label_Train_VITS_Speakers.setObjectName(u"Label_Train_VITS_Speakers")
        sizePolicy6.setHeightForWidth(self.Label_Train_VITS_Speakers.sizePolicy().hasHeightForWidth())
        self.Label_Train_VITS_Speakers.setSizePolicy(sizePolicy6)
        self.Label_Train_VITS_Speakers.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_88.addWidget(self.Label_Train_VITS_Speakers)

        self.ChildFrame_Train_VITS_Speakers = QFrame(self.Frame_Train_VITS_Speakers)
        self.ChildFrame_Train_VITS_Speakers.setObjectName(u"ChildFrame_Train_VITS_Speakers")
        sizePolicy6.setHeightForWidth(self.ChildFrame_Train_VITS_Speakers.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Train_VITS_Speakers.setSizePolicy(sizePolicy6)
        self.ChildFrame_Train_VITS_Speakers.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_32 = QHBoxLayout(self.ChildFrame_Train_VITS_Speakers)
        self.horizontalLayout_32.setSpacing(12)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Train_VITS_Speakers = QLineEdit(self.ChildFrame_Train_VITS_Speakers)
        self.LineEdit_Train_VITS_Speakers.setObjectName(u"LineEdit_Train_VITS_Speakers")
        self.LineEdit_Train_VITS_Speakers.setMinimumSize(QSize(0, 27))
        self.LineEdit_Train_VITS_Speakers.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_32.addWidget(self.LineEdit_Train_VITS_Speakers)


        self.verticalLayout_88.addWidget(self.ChildFrame_Train_VITS_Speakers)


        self.verticalLayout_28.addWidget(self.Frame_Train_VITS_Speakers)


        self.verticalLayout_34.addWidget(self.Frame_OptionalSettings_Train_VITS)


        self.verticalLayout_18.addWidget(self.GroupBox_OptionalParams_Train_VITS)

        self.VerticalSpacer_Train_VITS = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.VerticalSpacer_Train_VITS)

        self.ScrollArea_Middle_Train_VITS.setWidget(self.ScrollArea_Middle_WidgetContents_Train_VITS)

        self.gridLayout_22.addWidget(self.ScrollArea_Middle_Train_VITS, 0, 1, 1, 1)

        self.Widget_Right_Train_VITS = QWidget(self.Subpage_Train_VITS)
        self.Widget_Right_Train_VITS.setObjectName(u"Widget_Right_Train_VITS")
        self.Widget_Right_Train_VITS.setMinimumSize(QSize(210, 0))
        self.Widget_Right_Train_VITS.setMaximumSize(QSize(420, 16777215))
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

        self.gridLayout.addWidget(self.Button_CheckOutput_Train_VITS, 2, 1, 1, 1)

        self.Button_SyncParams_Train_VITS = QPushButton(self.Widget_Right_Train_VITS)
        self.Button_SyncParams_Train_VITS.setObjectName(u"Button_SyncParams_Train_VITS")
        self.Button_SyncParams_Train_VITS.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.Button_SyncParams_Train_VITS, 2, 0, 1, 1)

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
"	background-color: rgb(33, 33, 33);\n"
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
"	border-st"
                        "yle: solid;\n"
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
"	width: 0px;\n"
""
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


        self.gridLayout_22.addWidget(self.Widget_Right_Train_VITS, 0, 2, 1, 1)

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
        sizePolicy7.setHeightForWidth(self.Button_Train_VITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Train_VITS_Execute.setSizePolicy(sizePolicy7)
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
        sizePolicy7.setHeightForWidth(self.Button_Train_VITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Train_VITS_Terminate.setSizePolicy(sizePolicy7)
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
        self.Widget_Left_TTS_VITS.setMaximumSize(QSize(210, 16777215))
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
        self.TreeWidget_Catalogue_TTS_VITS.setStyleSheet(u"QTreeWidget {\n"
"	/*font-size: 12px;\n"
"	text-align: center;*/\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"	background-color: transparent;\n"
"	padding: 1.2px;\n"
"}\n"
"\n"
"QTreeWidget::branch {\n"
"    background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QTreeWidget::branch:open:has-children:has-siblings,\n"
"QTreeWidget::branch:open:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:closed:has-children:has-siblings,\n"
"QTreeWidget::branch:closed:has-children:!has-siblings {\n"
"    image: ;\n"
"}\n"
"QTreeWidget::branch:!has-children:has-siblings:adjoins-item,\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    image: ;\n"
"}\n"
"\n"
"\n"
"QTreeView {\n"
"}\n"
"\n"
"QTreeView::item{\n"
"}\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
""
                        "QTreeView::item:selected:active{\n"
"    background-color: ;\n"
"}\n"
"QTreeView::item:selected:!active {\n"
"    background-color: ;\n"
"}\n"
"\n"
"/*\n"
"QHeaderView {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	margin: 0px;\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QHeaderView:hover {\n"
"    background-color: rgba(66, 66, 66, 198);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: transparent;\n"
"}\n"
"QHeaderView::section:checked {\n"
"	background-color: ;\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"	position: ;\n"
"	image: ;\n"
"}*/\n"
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
"	background-color: rgba(33, 3"
                        "3, 33, 99);\n"
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
"	border"
                        "-radius: 6px;\n"
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
"	backgro"
                        "und-color: rgb(120, 120, 120);\n"
"}")

        self.verticalLayout_11.addWidget(self.TreeWidget_Catalogue_TTS_VITS)


        self.gridLayout_20.addWidget(self.Widget_Left_TTS_VITS, 0, 0, 1, 1)

        self.ScrollArea_Middle_TTS_VITS = QScrollArea(self.Subpage_TTS_VITS)
        self.ScrollArea_Middle_TTS_VITS.setObjectName(u"ScrollArea_Middle_TTS_VITS")
        sizePolicy5.setHeightForWidth(self.ScrollArea_Middle_TTS_VITS.sizePolicy().hasHeightForWidth())
        self.ScrollArea_Middle_TTS_VITS.setSizePolicy(sizePolicy5)
        self.ScrollArea_Middle_TTS_VITS.setMinimumSize(QSize(630, 0))
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
        self.ScrollArea_Middle_WidgetContents_TTS_VITS.setGeometry(QRect(0, 0, 621, 1186))
        self.verticalLayout_19 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.verticalLayout_19.setSpacing(12)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_TTS_VITS = QGroupBox(self.ScrollArea_Middle_WidgetContents_TTS_VITS)
        self.GroupBox_EssentialParams_TTS_VITS.setObjectName(u"GroupBox_EssentialParams_TTS_VITS")
        self.GroupBox_EssentialParams_TTS_VITS.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_117 = QVBoxLayout(self.GroupBox_EssentialParams_TTS_VITS)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_TTS_VITS = QCheckBox(self.GroupBox_EssentialParams_TTS_VITS)
        self.CheckBox_Toggle_BasicSettings_TTS_VITS.setObjectName(u"CheckBox_Toggle_BasicSettings_TTS_VITS")
        self.CheckBox_Toggle_BasicSettings_TTS_VITS.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_117.addWidget(self.CheckBox_Toggle_BasicSettings_TTS_VITS)

        self.Frame_BasicSettings_TTS_VITS = QFrame(self.GroupBox_EssentialParams_TTS_VITS)
        self.Frame_BasicSettings_TTS_VITS.setObjectName(u"Frame_BasicSettings_TTS_VITS")
        self.verticalLayout_131 = QVBoxLayout(self.Frame_BasicSettings_TTS_VITS)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_VITS_Config_Path_Load = QFrame(self.Frame_BasicSettings_TTS_VITS)
        self.Frame_TTS_VITS_Config_Path_Load.setObjectName(u"Frame_TTS_VITS_Config_Path_Load")
        self.Frame_TTS_VITS_Config_Path_Load.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_Config_Path_Load.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_78 = QVBoxLayout(self.Frame_TTS_VITS_Config_Path_Load)
        self.verticalLayout_78.setSpacing(12)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Config_Path_Load = QLabel(self.Frame_TTS_VITS_Config_Path_Load)
        self.Label_TTS_VITS_Config_Path_Load.setObjectName(u"Label_TTS_VITS_Config_Path_Load")
        sizePolicy6.setHeightForWidth(self.Label_TTS_VITS_Config_Path_Load.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Config_Path_Load.setSizePolicy(sizePolicy6)
        self.Label_TTS_VITS_Config_Path_Load.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_78.addWidget(self.Label_TTS_VITS_Config_Path_Load)

        self.ChildFrame_TTS_VITS_Config_Path_Load = QFrame(self.Frame_TTS_VITS_Config_Path_Load)
        self.ChildFrame_TTS_VITS_Config_Path_Load.setObjectName(u"ChildFrame_TTS_VITS_Config_Path_Load")
        sizePolicy6.setHeightForWidth(self.ChildFrame_TTS_VITS_Config_Path_Load.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_Config_Path_Load.setSizePolicy(sizePolicy6)
        self.ChildFrame_TTS_VITS_Config_Path_Load.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_41 = QHBoxLayout(self.ChildFrame_TTS_VITS_Config_Path_Load)
        self.horizontalLayout_41.setSpacing(12)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_TTS_VITS_Config_Path_Load = QLineEdit(self.ChildFrame_TTS_VITS_Config_Path_Load)
        self.LineEdit_TTS_VITS_Config_Path_Load.setObjectName(u"LineEdit_TTS_VITS_Config_Path_Load")
        self.LineEdit_TTS_VITS_Config_Path_Load.setMinimumSize(QSize(0, 27))
        self.LineEdit_TTS_VITS_Config_Path_Load.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_41.addWidget(self.LineEdit_TTS_VITS_Config_Path_Load)

        self.Button_TTS_VITS_Config_Path_Load = QPushButton(self.ChildFrame_TTS_VITS_Config_Path_Load)
        self.Button_TTS_VITS_Config_Path_Load.setObjectName(u"Button_TTS_VITS_Config_Path_Load")
        self.Button_TTS_VITS_Config_Path_Load.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_Config_Path_Load.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_41.addWidget(self.Button_TTS_VITS_Config_Path_Load)


        self.verticalLayout_78.addWidget(self.ChildFrame_TTS_VITS_Config_Path_Load)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Config_Path_Load)

        self.Frame_TTS_VITS_Model_Path_Load = QFrame(self.Frame_BasicSettings_TTS_VITS)
        self.Frame_TTS_VITS_Model_Path_Load.setObjectName(u"Frame_TTS_VITS_Model_Path_Load")
        self.Frame_TTS_VITS_Model_Path_Load.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_Model_Path_Load.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_96 = QVBoxLayout(self.Frame_TTS_VITS_Model_Path_Load)
        self.verticalLayout_96.setSpacing(12)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Model_Path_Load = QLabel(self.Frame_TTS_VITS_Model_Path_Load)
        self.Label_TTS_VITS_Model_Path_Load.setObjectName(u"Label_TTS_VITS_Model_Path_Load")
        sizePolicy6.setHeightForWidth(self.Label_TTS_VITS_Model_Path_Load.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Model_Path_Load.setSizePolicy(sizePolicy6)
        self.Label_TTS_VITS_Model_Path_Load.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_96.addWidget(self.Label_TTS_VITS_Model_Path_Load)

        self.ChildFrame_TTS_VITS_Model_Path_Load = QFrame(self.Frame_TTS_VITS_Model_Path_Load)
        self.ChildFrame_TTS_VITS_Model_Path_Load.setObjectName(u"ChildFrame_TTS_VITS_Model_Path_Load")
        sizePolicy6.setHeightForWidth(self.ChildFrame_TTS_VITS_Model_Path_Load.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_Model_Path_Load.setSizePolicy(sizePolicy6)
        self.ChildFrame_TTS_VITS_Model_Path_Load.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_42 = QHBoxLayout(self.ChildFrame_TTS_VITS_Model_Path_Load)
        self.horizontalLayout_42.setSpacing(12)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_TTS_VITS_Model_Path_Load = QLineEdit(self.ChildFrame_TTS_VITS_Model_Path_Load)
        self.LineEdit_TTS_VITS_Model_Path_Load.setObjectName(u"LineEdit_TTS_VITS_Model_Path_Load")
        self.LineEdit_TTS_VITS_Model_Path_Load.setMinimumSize(QSize(0, 27))
        self.LineEdit_TTS_VITS_Model_Path_Load.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_42.addWidget(self.LineEdit_TTS_VITS_Model_Path_Load)

        self.Button_TTS_VITS_Model_Path_Load = QPushButton(self.ChildFrame_TTS_VITS_Model_Path_Load)
        self.Button_TTS_VITS_Model_Path_Load.setObjectName(u"Button_TTS_VITS_Model_Path_Load")
        self.Button_TTS_VITS_Model_Path_Load.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_Model_Path_Load.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_42.addWidget(self.Button_TTS_VITS_Model_Path_Load)


        self.verticalLayout_96.addWidget(self.ChildFrame_TTS_VITS_Model_Path_Load)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Model_Path_Load)

        self.Frame_TTS_VITS_Text = QFrame(self.Frame_BasicSettings_TTS_VITS)
        self.Frame_TTS_VITS_Text.setObjectName(u"Frame_TTS_VITS_Text")
        self.Frame_TTS_VITS_Text.setMinimumSize(QSize(0, 222))
        self.Frame_TTS_VITS_Text.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_98 = QVBoxLayout(self.Frame_TTS_VITS_Text)
        self.verticalLayout_98.setSpacing(12)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Text = QLabel(self.Frame_TTS_VITS_Text)
        self.Label_TTS_VITS_Text.setObjectName(u"Label_TTS_VITS_Text")
        sizePolicy6.setHeightForWidth(self.Label_TTS_VITS_Text.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Text.setSizePolicy(sizePolicy6)
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
        sizePolicy7.setHeightForWidth(self.PlainTextEdit_TTS_VITS_Text.sizePolicy().hasHeightForWidth())
        self.PlainTextEdit_TTS_VITS_Text.setSizePolicy(sizePolicy7)
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

        self.Frame_TTS_VITS_Language = QFrame(self.Frame_BasicSettings_TTS_VITS)
        self.Frame_TTS_VITS_Language.setObjectName(u"Frame_TTS_VITS_Language")
        self.Frame_TTS_VITS_Language.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_Language.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_97 = QVBoxLayout(self.Frame_TTS_VITS_Language)
        self.verticalLayout_97.setSpacing(12)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Language = QLabel(self.Frame_TTS_VITS_Language)
        self.Label_TTS_VITS_Language.setObjectName(u"Label_TTS_VITS_Language")
        sizePolicy6.setHeightForWidth(self.Label_TTS_VITS_Language.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Language.setSizePolicy(sizePolicy6)
        self.Label_TTS_VITS_Language.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_97.addWidget(self.Label_TTS_VITS_Language)

        self.ComboBox_TTS_VITS_Language = QComboBox(self.Frame_TTS_VITS_Language)
        self.ComboBox_TTS_VITS_Language.setObjectName(u"ComboBox_TTS_VITS_Language")
        self.ComboBox_TTS_VITS_Language.setMinimumSize(QSize(0, 27))
        self.ComboBox_TTS_VITS_Language.setStyleSheet(u"QComboBox {\n"
"	/*font-size: 12px;*/\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
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
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding-left: -15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemV"
                        "iew::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-left: 15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120. 120, 120, 120)\n"
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
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
""
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
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:"
                        "hover {\n"
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
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScro"
                        "llArea QScrollBar::handle:horizontal:hover {\n"
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

        self.verticalLayout_97.addWidget(self.ComboBox_TTS_VITS_Language)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Language)

        self.Frame_TTS_VITS_Speaker = QFrame(self.Frame_BasicSettings_TTS_VITS)
        self.Frame_TTS_VITS_Speaker.setObjectName(u"Frame_TTS_VITS_Speaker")
        self.Frame_TTS_VITS_Speaker.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_Speaker.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_104 = QVBoxLayout(self.Frame_TTS_VITS_Speaker)
        self.verticalLayout_104.setSpacing(12)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Speaker = QLabel(self.Frame_TTS_VITS_Speaker)
        self.Label_TTS_VITS_Speaker.setObjectName(u"Label_TTS_VITS_Speaker")
        sizePolicy6.setHeightForWidth(self.Label_TTS_VITS_Speaker.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Speaker.setSizePolicy(sizePolicy6)
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
"	color: rgb(255, 255, 255);\n"
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
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	padding-left: -15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemV"
                        "iew::item {\n"
"	/* height: 30px; */\n"
"	background-color: transparent;\n"
"	padding-left: 15px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: rgba(120. 120, 120, 120)\n"
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
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
""
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
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:"
                        "hover {\n"
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
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScro"
                        "llArea QScrollBar::handle:horizontal:hover {\n"
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

        self.Frame_TTS_VITS_Audio_Dir_Save = QFrame(self.Frame_BasicSettings_TTS_VITS)
        self.Frame_TTS_VITS_Audio_Dir_Save.setObjectName(u"Frame_TTS_VITS_Audio_Dir_Save")
        self.Frame_TTS_VITS_Audio_Dir_Save.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_Audio_Dir_Save.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_107 = QVBoxLayout(self.Frame_TTS_VITS_Audio_Dir_Save)
        self.verticalLayout_107.setSpacing(12)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_Audio_Dir_Save = QLabel(self.Frame_TTS_VITS_Audio_Dir_Save)
        self.Label_TTS_VITS_Audio_Dir_Save.setObjectName(u"Label_TTS_VITS_Audio_Dir_Save")
        sizePolicy6.setHeightForWidth(self.Label_TTS_VITS_Audio_Dir_Save.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_Audio_Dir_Save.setSizePolicy(sizePolicy6)
        self.Label_TTS_VITS_Audio_Dir_Save.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_107.addWidget(self.Label_TTS_VITS_Audio_Dir_Save)

        self.ChildFrame_TTS_VITS_Audio_Dir_Save = QFrame(self.Frame_TTS_VITS_Audio_Dir_Save)
        self.ChildFrame_TTS_VITS_Audio_Dir_Save.setObjectName(u"ChildFrame_TTS_VITS_Audio_Dir_Save")
        sizePolicy6.setHeightForWidth(self.ChildFrame_TTS_VITS_Audio_Dir_Save.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_Audio_Dir_Save.setSizePolicy(sizePolicy6)
        self.ChildFrame_TTS_VITS_Audio_Dir_Save.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_46 = QHBoxLayout(self.ChildFrame_TTS_VITS_Audio_Dir_Save)
        self.horizontalLayout_46.setSpacing(12)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_TTS_VITS_Audio_Dir_Save = QLineEdit(self.ChildFrame_TTS_VITS_Audio_Dir_Save)
        self.LineEdit_TTS_VITS_Audio_Dir_Save.setObjectName(u"LineEdit_TTS_VITS_Audio_Dir_Save")
        self.LineEdit_TTS_VITS_Audio_Dir_Save.setMinimumSize(QSize(0, 27))
        self.LineEdit_TTS_VITS_Audio_Dir_Save.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit:hover {\n"
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

        self.horizontalLayout_46.addWidget(self.LineEdit_TTS_VITS_Audio_Dir_Save)

        self.Button_TTS_VITS_Audio_Dir_Save = QPushButton(self.ChildFrame_TTS_VITS_Audio_Dir_Save)
        self.Button_TTS_VITS_Audio_Dir_Save.setObjectName(u"Button_TTS_VITS_Audio_Dir_Save")
        self.Button_TTS_VITS_Audio_Dir_Save.setMinimumSize(QSize(27, 27))
        self.Button_TTS_VITS_Audio_Dir_Save.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
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

        self.horizontalLayout_46.addWidget(self.Button_TTS_VITS_Audio_Dir_Save)


        self.verticalLayout_107.addWidget(self.ChildFrame_TTS_VITS_Audio_Dir_Save)


        self.verticalLayout_131.addWidget(self.Frame_TTS_VITS_Audio_Dir_Save)


        self.verticalLayout_117.addWidget(self.Frame_BasicSettings_TTS_VITS)

        self.CheckBox_Toggle_AdvanceSettings_TTS_VITS = QCheckBox(self.GroupBox_EssentialParams_TTS_VITS)
        self.CheckBox_Toggle_AdvanceSettings_TTS_VITS.setObjectName(u"CheckBox_Toggle_AdvanceSettings_TTS_VITS")
        self.CheckBox_Toggle_AdvanceSettings_TTS_VITS.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_117.addWidget(self.CheckBox_Toggle_AdvanceSettings_TTS_VITS)

        self.Frame_AdvanceSettings_TTS_VITS = QFrame(self.GroupBox_EssentialParams_TTS_VITS)
        self.Frame_AdvanceSettings_TTS_VITS.setObjectName(u"Frame_AdvanceSettings_TTS_VITS")
        self.verticalLayout_118 = QVBoxLayout(self.Frame_AdvanceSettings_TTS_VITS)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.Frame_TTS_VITS_EmotionStrength = QFrame(self.Frame_AdvanceSettings_TTS_VITS)
        self.Frame_TTS_VITS_EmotionStrength.setObjectName(u"Frame_TTS_VITS_EmotionStrength")
        self.Frame_TTS_VITS_EmotionStrength.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_EmotionStrength.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_103 = QVBoxLayout(self.Frame_TTS_VITS_EmotionStrength)
        self.verticalLayout_103.setSpacing(12)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_EmotionStrength = QLabel(self.Frame_TTS_VITS_EmotionStrength)
        self.Label_TTS_VITS_EmotionStrength.setObjectName(u"Label_TTS_VITS_EmotionStrength")
        sizePolicy6.setHeightForWidth(self.Label_TTS_VITS_EmotionStrength.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_EmotionStrength.setSizePolicy(sizePolicy6)
        self.Label_TTS_VITS_EmotionStrength.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_103.addWidget(self.Label_TTS_VITS_EmotionStrength)

        self.ChildFrame_TTS_VITS_EmotionStrength = QFrame(self.Frame_TTS_VITS_EmotionStrength)
        self.ChildFrame_TTS_VITS_EmotionStrength.setObjectName(u"ChildFrame_TTS_VITS_EmotionStrength")
        sizePolicy6.setHeightForWidth(self.ChildFrame_TTS_VITS_EmotionStrength.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_EmotionStrength.setSizePolicy(sizePolicy6)
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


        self.verticalLayout_103.addWidget(self.ChildFrame_TTS_VITS_EmotionStrength)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_EmotionStrength)

        self.Frame_TTS_VITS_PhonemeDuration = QFrame(self.Frame_AdvanceSettings_TTS_VITS)
        self.Frame_TTS_VITS_PhonemeDuration.setObjectName(u"Frame_TTS_VITS_PhonemeDuration")
        self.Frame_TTS_VITS_PhonemeDuration.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_PhonemeDuration.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_105 = QVBoxLayout(self.Frame_TTS_VITS_PhonemeDuration)
        self.verticalLayout_105.setSpacing(12)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_PhonemeDuration = QLabel(self.Frame_TTS_VITS_PhonemeDuration)
        self.Label_TTS_VITS_PhonemeDuration.setObjectName(u"Label_TTS_VITS_PhonemeDuration")
        sizePolicy6.setHeightForWidth(self.Label_TTS_VITS_PhonemeDuration.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_PhonemeDuration.setSizePolicy(sizePolicy6)
        self.Label_TTS_VITS_PhonemeDuration.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_105.addWidget(self.Label_TTS_VITS_PhonemeDuration)

        self.ChildFrame_TTS_VITS_PhonemeDuration = QFrame(self.Frame_TTS_VITS_PhonemeDuration)
        self.ChildFrame_TTS_VITS_PhonemeDuration.setObjectName(u"ChildFrame_TTS_VITS_PhonemeDuration")
        sizePolicy6.setHeightForWidth(self.ChildFrame_TTS_VITS_PhonemeDuration.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_PhonemeDuration.setSizePolicy(sizePolicy6)
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


        self.verticalLayout_105.addWidget(self.ChildFrame_TTS_VITS_PhonemeDuration)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_PhonemeDuration)

        self.Frame_TTS_VITS_SpeechRate = QFrame(self.Frame_AdvanceSettings_TTS_VITS)
        self.Frame_TTS_VITS_SpeechRate.setObjectName(u"Frame_TTS_VITS_SpeechRate")
        self.Frame_TTS_VITS_SpeechRate.setMinimumSize(QSize(0, 105))
        self.Frame_TTS_VITS_SpeechRate.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_106 = QVBoxLayout(self.Frame_TTS_VITS_SpeechRate)
        self.verticalLayout_106.setSpacing(12)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(21, 12, 21, 12)
        self.Label_TTS_VITS_SpeechRate = QLabel(self.Frame_TTS_VITS_SpeechRate)
        self.Label_TTS_VITS_SpeechRate.setObjectName(u"Label_TTS_VITS_SpeechRate")
        sizePolicy6.setHeightForWidth(self.Label_TTS_VITS_SpeechRate.sizePolicy().hasHeightForWidth())
        self.Label_TTS_VITS_SpeechRate.setSizePolicy(sizePolicy6)
        self.Label_TTS_VITS_SpeechRate.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_106.addWidget(self.Label_TTS_VITS_SpeechRate)

        self.ChildFrame_TTS_VITS_SpeechRate = QFrame(self.Frame_TTS_VITS_SpeechRate)
        self.ChildFrame_TTS_VITS_SpeechRate.setObjectName(u"ChildFrame_TTS_VITS_SpeechRate")
        sizePolicy6.setHeightForWidth(self.ChildFrame_TTS_VITS_SpeechRate.sizePolicy().hasHeightForWidth())
        self.ChildFrame_TTS_VITS_SpeechRate.setSizePolicy(sizePolicy6)
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


        self.verticalLayout_106.addWidget(self.ChildFrame_TTS_VITS_SpeechRate)


        self.verticalLayout_118.addWidget(self.Frame_TTS_VITS_SpeechRate)


        self.verticalLayout_117.addWidget(self.Frame_AdvanceSettings_TTS_VITS)


        self.verticalLayout_19.addWidget(self.GroupBox_EssentialParams_TTS_VITS)

        self.VerticalSpacer_TTS_VITS = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.VerticalSpacer_TTS_VITS)

        self.ScrollArea_Middle_TTS_VITS.setWidget(self.ScrollArea_Middle_WidgetContents_TTS_VITS)

        self.gridLayout_20.addWidget(self.ScrollArea_Middle_TTS_VITS, 0, 1, 1, 1)

        self.Widget_Right_TTS_VITS = QWidget(self.Subpage_TTS_VITS)
        self.Widget_Right_TTS_VITS.setObjectName(u"Widget_Right_TTS_VITS")
        self.Widget_Right_TTS_VITS.setMinimumSize(QSize(210, 0))
        self.Widget_Right_TTS_VITS.setMaximumSize(QSize(420, 16777215))
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
"	background-color: rgb(33, 33, 33);\n"
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
"	border-st"
                        "yle: solid;\n"
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
"	width: 0px;\n"
""
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
        sizePolicy7.setHeightForWidth(self.Button_TTS_VITS_Execute.sizePolicy().hasHeightForWidth())
        self.Button_TTS_VITS_Execute.setSizePolicy(sizePolicy7)
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
        sizePolicy7.setHeightForWidth(self.Button_TTS_VITS_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_TTS_VITS_Terminate.setSizePolicy(sizePolicy7)
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

        self.HorizontalSpacer_Setting_Language = QSpacerItem(969, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.HorizontalSpacer_Setting_Language)

        self.ComboBox_Setting_Language = QComboBox(self.Frame_Setting_Language)
        self.ComboBox_Setting_Language.setObjectName(u"ComboBox_Setting_Language")
        self.ComboBox_Setting_Language.setMinimumSize(QSize(123, 0))
        self.ComboBox_Setting_Language.setMaximumSize(QSize(123, 16777215))
        self.ComboBox_Setting_Language.setStyleSheet(u"QComboBox {\n"
"	font-size: 15px;\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(90, 90, 90);\n"
"	padding: 1.5px;\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	margin-right: 3px;\n"
"	border-width: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border-image: url(:/ComboBox_Icon/Sources/DownArrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(90, 90, 90);\n"
"	padding: -1.5px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"	/* height: 30px; */\n"
"	background-color: rgb(90, 90, 90);\n"
"	padding: 1.5px;\n"
"	border-width: 0px;\n"
"	bord"
                        "er-radius: 6px;\n"
"	border-style: solid;\n"
"	border-color: rgb(90, 90, 90);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	background-color: darkgrey;\n"
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
"	border-style: solid;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	background-color: transparent;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"	border-width: 0px;\n"
"	"
                        "border-radius: 0px;\n"
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
"	border-color: transparent;\n"
"	margin: 0px;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::horizontal:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::add-line:horizontal {\n"
"	width: 0px;\n"
""
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
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:horizontal:hover {\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	color: rgba(255, 255, 25"
                        "5, 210);\n"
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

        self.HorizontalSpacer_Setting_AutoUpdate = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.HorizontalSpacer_Setting_AutoUpdate)

        self.CheckBox_Setting_AutoUpdate = QCheckBox(self.Frame_Setting_AutoUpdate)
        self.CheckBox_Setting_AutoUpdate.setObjectName(u"CheckBox_Setting_AutoUpdate")
        sizePolicy6.setHeightForWidth(self.CheckBox_Setting_AutoUpdate.sizePolicy().hasHeightForWidth())
        self.CheckBox_Setting_AutoUpdate.setSizePolicy(sizePolicy6)
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

        self.HorizontalSpacer_Setting_Synchronizer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_67.addItem(self.HorizontalSpacer_Setting_Synchronizer)

        self.CheckBox_Setting_Synchronizer = QCheckBox(self.Frame_Setting_Synchronizer)
        self.CheckBox_Setting_Synchronizer.setObjectName(u"CheckBox_Setting_Synchronizer")
        sizePolicy6.setHeightForWidth(self.CheckBox_Setting_Synchronizer.sizePolicy().hasHeightForWidth())
        self.CheckBox_Setting_Synchronizer.setSizePolicy(sizePolicy6)
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

        self.HorizontalSpacer_Setting_Operation = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.HorizontalSpacer_Setting_Operation)


        self.verticalLayout_13.addWidget(self.Frame_Setting_Operation)


        self.verticalLayout_109.addWidget(self.Frame_Settings_Middle)

        self.VerticalSpacer_Settings = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
"	border-width: 1px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}")
        self.verticalLayout_23 = QVBoxLayout(self.Frame_Console)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(21, 0, 21, 0)
        self.PlainTextEdit_Console = QPlainTextEdit(self.Frame_Console)
        self.PlainTextEdit_Console.setObjectName(u"PlainTextEdit_Console")
        self.PlainTextEdit_Console.setStyleSheet(u"QPlainTextEdit {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QPlainTextEdit:hover {\n"
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
"	border-"
                        "style: solid;\n"
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
"	width: 0px;\n"
""
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

        self.verticalLayout_23.addWidget(self.PlainTextEdit_Console)


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

        self.HorizontalSpacer_Bottom_Left = QSpacerItem(182, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.Label_Menu_Download_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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
        self.ToolButton_Download_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Label_Download_FFmpeg.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_FFmpeg_Status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_Python.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_Python_Status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_PyReqs.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_PyReqs_Status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_Pytorch.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_Pytorch_Status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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

        self.GroupBox_EssentialParams_Process.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_Process.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_Process_Media_Dir_Input.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Process_Media_Dir_Input.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Process_Media_Format_Output.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_Slice_Audio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Process_Slice_Audio.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Process_Media_Dir_Output.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Process_Media_Dir_Output.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_Process.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Process_RMS_Threshold.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_Audio_Length_Min.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_Silent_Interval_Min.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_Hop_Size.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Process_Silence_Kept_Max.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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

        self.GroupBox_EssentialParams_ASR_VPR.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_ASR_VPR.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_ASR_VPR_Audio_Dir_Input.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_ASR_VPR_Audio_Dir_Input.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_ASR_VPR_StdAudioSpeaker.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_DecisionThreshold.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_Audio_Dir_Output.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_ASR_VPR_Audio_Dir_Output.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_ASR_VPR.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_ASR_VPR_Model_Path.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_ASR_VPR_Model_Path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_ASR_VPR_Model_Type.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_Feature_Method.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_ASR_VPR_Duration_of_Audio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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

        self.GroupBox_EssentialParams_STT_Whisper.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_STT_Whisper.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_STT_Whisper_WAV_Dir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_STT_Whisper_WAV_Dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_STT_Whisper_SRT_Dir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_STT_Whisper_SRT_Dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_STT_Whisper.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_STT_Whisper_Model_Path.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_STT_Whisper_Model_Path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_STT_Whisper_Verbose.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_STT_Whisper_Verbose.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_STT_Whisper_Condition_on_Previous_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_STT_Whisper_Condition_on_Previous_Text.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_STT_Whisper_fp16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_STT_Whisper_fp16.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_OptionalParams_STT_Whisper.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_STT_Whisper_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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

        self.GroupBox_EssentialParams_DAT_VITS.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_DAT_VITS.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_DAT_VITS_WAV_Dir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_DAT_VITS_WAV_Dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_DAT_VITS_SRT_Dir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_DAT_VITS_SRT_Dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_DAT_VITS_Add_AuxiliaryData.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_DAT_VITS_Add_AuxiliaryData.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_DAT_VITS_WAV_Dir_Split.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_DAT_VITS_WAV_Dir_Split.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_DAT_VITS_FileList_Path_Training.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_DAT_VITS_FileList_Path_Training.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_DAT_VITS_FileList_Path_Validation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_DAT_VITS_FileList_Path_Validation.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_DAT_VITS.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_DAT_VITS_TrainRatio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_SampleRate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_SampleWidth.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_DAT_VITS_ToMono.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_DAT_VITS_ToMono.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_DAT_VITS_AuxiliaryData_Path.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_DAT_VITS_AuxiliaryData_Path.setText(QCoreApplication.translate("MainWindow", u"...", None))
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

        self.GroupBox_EssentialParams_Train_VITS.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_Train_VITS.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_Train_VITS_FileList_Path_Training.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Train_VITS_FileList_Path_Training.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Train_VITS_FileList_Path_Validation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Train_VITS_FileList_Path_Validation.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Train_VITS_Epochs.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_Batch_Size.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_Use_PretrainedModels.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_VITS_Use_PretrainedModels.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Train_VITS_Output_Dir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Train_VITS_Output_Dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_Train_VITS.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Train_VITS_Eval_Interval.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_Num_Workers.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Train_VITS_FP16_Run.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_VITS_FP16_Run.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Train_VITS_Model_Path_Pretrained_G.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Train_VITS_Model_Path_Pretrained_G.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Train_VITS_Model_Path_Pretrained_D.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Train_VITS_Model_Path_Pretrained_D.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Train_VITS_Keep_Original_Speakers.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Train_VITS_Keep_Original_Speakers.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_OptionalParams_Train_VITS.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.Label_Train_VITS_Speakers.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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

        self.GroupBox_EssentialParams_TTS_VITS.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_TTS_VITS.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_TTS_VITS_Config_Path_Load.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_TTS_VITS_Config_Path_Load.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_TTS_VITS_Model_Path_Load.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_TTS_VITS_Model_Path_Load.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_TTS_VITS_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_Speaker.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_Audio_Dir_Save.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_TTS_VITS_Audio_Dir_Save.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_TTS_VITS.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_TTS_VITS_EmotionStrength.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_PhonemeDuration.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_TTS_VITS_SpeechRate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_Settings_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Label_Setting_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.ToolButton_Info_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Label_ToolsStatus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Usage_CPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Usage_GPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        pass