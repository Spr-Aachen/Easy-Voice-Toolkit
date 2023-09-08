from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QDoubleSpinBox, QFrame, QGroupBox, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPlainTextEdit, QProgressBar, QToolButton, QPushButton, QScrollArea, QSizePolicy, QSlider, QSpacerItem, QSpinBox, QStackedWidget, QTreeWidget, QTreeWidgetItem, QTextBrowser, QVBoxLayout, QWidget)

from . import Sources


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
        self.TitleBar.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(12, 12, 12, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
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
        self.horizontalLayout_56 = QHBoxLayout(self.Frame_Top)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSpacer_Left_Top = QSpacerItem(588, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.HorizontalSpacer_Left_Top)

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

        self.horizontalLayout_56.addWidget(self.Label_Title)

        self.HorizontalSpacer_Right_Top = QSpacerItem(587, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.HorizontalSpacer_Right_Top)


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
        self.Frame_Menu.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(12, 12, 12, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.Frame_Menu)
        self.verticalLayout_3.setSpacing(3)
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
"	background-color: rgba(66, 66, 66, 198);\n"
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
        self.horizontalLayout_54 = QHBoxLayout(self.Button_Menu_Home)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Home_Icon = QLabel(self.Button_Menu_Home)
        self.Label_Menu_Home_Icon.setObjectName(u"Label_Menu_Home_Icon")
        self.Label_Menu_Home_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Home_Icon.setMaximumSize(QSize(48, 16777215))
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

        self.horizontalLayout_54.addWidget(self.Label_Menu_Home_Icon)

        self.Label_Menu_Home_Text = QLabel(self.Button_Menu_Home)
        self.Label_Menu_Home_Text.setObjectName(u"Label_Menu_Home_Text")
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

        self.horizontalLayout_54.addWidget(self.Label_Menu_Home_Text)


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
"	background-color: rgba(66, 66, 66, 198);\n"
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
        self.horizontalLayout_53 = QHBoxLayout(self.Button_Menu_Download)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Download_Icon = QLabel(self.Button_Menu_Download)
        self.Label_Menu_Download_Icon.setObjectName(u"Label_Menu_Download_Icon")
        self.Label_Menu_Download_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Download_Icon.setMaximumSize(QSize(48, 16777215))
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

        self.horizontalLayout_53.addWidget(self.Label_Menu_Download_Icon)

        self.Label_Menu_Download_Text = QLabel(self.Button_Menu_Download)
        self.Label_Menu_Download_Text.setObjectName(u"Label_Menu_Download_Text")
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

        self.horizontalLayout_53.addWidget(self.Label_Menu_Download_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Download)

        self.Button_Menu_Tools = QToolButton(self.Frame_Menu)
        self.Button_Menu_Tools.setObjectName(u"Button_Menu_Tools")
        sizePolicy1.setHeightForWidth(self.Button_Menu_Tools.sizePolicy().hasHeightForWidth())
        self.Button_Menu_Tools.setSizePolicy(sizePolicy1)
        self.Button_Menu_Tools.setMinimumSize(QSize(0, 48))
        self.Button_Menu_Tools.setStyleSheet(u"QToolButton {\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: rgba(66, 66, 66, 198);\n"
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
        self.horizontalLayout_68 = QHBoxLayout(self.Button_Menu_Tools)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Tools_Icon = QLabel(self.Button_Menu_Tools)
        self.Label_Menu_Tools_Icon.setObjectName(u"Label_Menu_Tools_Icon")
        self.Label_Menu_Tools_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Tools_Icon.setMaximumSize(QSize(48, 16777215))
        self.Label_Menu_Tools_Icon.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;\n"
"	font-size: 15px;*/\n"
"	margin: 12px;\n"
"	border-image: url(:/Button_Icon/Sources/Tools.png);\n"
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

        self.horizontalLayout_68.addWidget(self.Label_Menu_Tools_Icon)

        self.Label_Menu_Tools_Text = QLabel(self.Button_Menu_Tools)
        self.Label_Menu_Tools_Text.setObjectName(u"Label_Menu_Tools_Text")
        self.Label_Menu_Tools_Text.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	text-align: center;\n"
"	color: rgb(210, 222, 234);\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.horizontalLayout_68.addWidget(self.Label_Menu_Tools_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Tools)

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
"	background-color: rgba(66, 66, 66, 198);\n"
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
        self.horizontalLayout_69 = QHBoxLayout(self.Button_Menu_Settings)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.Label_Menu_Settings_Icon = QLabel(self.Button_Menu_Settings)
        self.Label_Menu_Settings_Icon.setObjectName(u"Label_Menu_Settings_Icon")
        self.Label_Menu_Settings_Icon.setMinimumSize(QSize(48, 48))
        self.Label_Menu_Settings_Icon.setMaximumSize(QSize(48, 16777215))
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

        self.horizontalLayout_69.addWidget(self.Label_Menu_Settings_Icon)

        self.Label_Menu_Settings_Text = QLabel(self.Button_Menu_Settings)
        self.Label_Menu_Settings_Text.setObjectName(u"Label_Menu_Settings_Text")
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

        self.horizontalLayout_69.addWidget(self.Label_Menu_Settings_Text)


        self.verticalLayout_3.addWidget(self.Button_Menu_Settings)


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
"	background-image: url(:/TextBrowser_Image/Sources/Easy Voice Toolkit - Cover.png);\n"
"	background-size: cover;\n"
"	background-repeat: no-repeat;\n"
"	background-position: center 0px;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 6px;\n"
"	border-style: solid;\n"
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
""
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
"	background-color: transparent;\n"
"	subcontrol-position: left;\n"
""
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
        self.horizontalLayout_29 = QHBoxLayout(self.Frame_Low_Home)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(12, 0, 12, 0)
        self.Button_Demo = QToolButton(self.Frame_Low_Home)
        self.Button_Demo.setObjectName(u"Button_Demo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Button_Demo.sizePolicy().hasHeightForWidth())
        self.Button_Demo.setSizePolicy(sizePolicy2)
        self.Button_Demo.setMinimumSize(QSize(210, 75))
        self.Button_Demo.setStyleSheet(u"QToolButton {\n"
"	text-align: right;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url(:/Button_Icon/Sources/Play.png);\n"
"	background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: left;\n"
"	background-color: transparent;\n"
"	padding: 12px 60px;\n"
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

        self.horizontalLayout_29.addWidget(self.Button_Demo)

        self.HorizontalSpacer_Low_Home_1 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.HorizontalSpacer_Low_Home_1)

        self.Button_Server = QToolButton(self.Frame_Low_Home)
        self.Button_Server.setObjectName(u"Button_Server")
        sizePolicy2.setHeightForWidth(self.Button_Server.sizePolicy().hasHeightForWidth())
        self.Button_Server.setSizePolicy(sizePolicy2)
        self.Button_Server.setMinimumSize(QSize(210, 75))
        self.Button_Server.setStyleSheet(u"QToolButton {\n"
"	text-align: right;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url(:/Button_Icon/Sources/Server.png);\n"
"	background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: left;\n"
"	background-color: transparent;\n"
"	padding: 12px 60px;\n"
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

        self.horizontalLayout_29.addWidget(self.Button_Server)

        self.HorizontalSpacer_Low_Home_2 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.HorizontalSpacer_Low_Home_2)

        self.Button_Repo = QToolButton(self.Frame_Low_Home)
        self.Button_Repo.setObjectName(u"Button_Repo")
        sizePolicy2.setHeightForWidth(self.Button_Repo.sizePolicy().hasHeightForWidth())
        self.Button_Repo.setSizePolicy(sizePolicy2)
        self.Button_Repo.setMinimumSize(QSize(210, 75))
        self.Button_Repo.setStyleSheet(u"QToolButton {\n"
"	text-align: right;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url(:/Button_Icon/Sources/GitHub.png);\n"
"	background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: left;\n"
"	background-color: transparent;\n"
"	padding: 12px 60px;\n"
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

        self.horizontalLayout_29.addWidget(self.Button_Repo)

        self.HorizontalSpacer_Low_Home_3 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.HorizontalSpacer_Low_Home_3)

        self.Button_Donate = QToolButton(self.Frame_Low_Home)
        self.Button_Donate.setObjectName(u"Button_Donate")
        sizePolicy2.setHeightForWidth(self.Button_Donate.sizePolicy().hasHeightForWidth())
        self.Button_Donate.setSizePolicy(sizePolicy2)
        self.Button_Donate.setMinimumSize(QSize(210, 75))
        self.Button_Donate.setStyleSheet(u"QToolButton {\n"
"	text-align: right;\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url(:/Button_Icon/Sources/Heart.png);\n"
"	background-repeat: no-repeat;\n"
"	background-origin: content;\n"
"	background-position: left;\n"
"	background-color: transparent;\n"
"	padding: 12px 60px;\n"
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

        self.horizontalLayout_29.addWidget(self.Button_Donate)


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
"	background-color: rgb(36, 36, 36);\n"
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Frame_Download_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Download_Title_Spacer.setSizePolicy(sizePolicy3)
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
        self.verticalLayout_134 = QVBoxLayout(self.Frame_Download_Middle)
        self.verticalLayout_134.setSpacing(0)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.Frame_Download_FFmpeg = QFrame(self.Frame_Download_Middle)
        self.Frame_Download_FFmpeg.setObjectName(u"Frame_Download_FFmpeg")
        self.Frame_Download_FFmpeg.setMinimumSize(QSize(0, 90))
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

        self.gridLayout_2.addItem(self.HorizontalSpacer_Download_FFmpeg, 0, 1, 1, 2)

        self.ProgressBar_Download_FFmpeg = QProgressBar(self.Frame_Download_FFmpeg)
        self.ProgressBar_Download_FFmpeg.setObjectName(u"ProgressBar_Download_FFmpeg")
        self.ProgressBar_Download_FFmpeg.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Download_FFmpeg.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(123, 123, 123, 210);\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgb(120, 180, 240));\n"
"}")

        self.gridLayout_2.addWidget(self.ProgressBar_Download_FFmpeg, 1, 0, 1, 2)

        self.Button_Install_FFmpeg = QPushButton(self.Frame_Download_FFmpeg)
        self.Button_Install_FFmpeg.setObjectName(u"Button_Install_FFmpeg")
        self.Button_Install_FFmpeg.setMaximumSize(QSize(30, 30))
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

        self.gridLayout_2.addWidget(self.Button_Install_FFmpeg, 1, 2, 1, 1)


        self.verticalLayout_134.addWidget(self.Frame_Download_FFmpeg)

        self.Frame_Download_GCC = QFrame(self.Frame_Download_Middle)
        self.Frame_Download_GCC.setObjectName(u"Frame_Download_GCC")
        self.Frame_Download_GCC.setMinimumSize(QSize(0, 90))
        self.Frame_Download_GCC.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.gridLayout_5 = QGridLayout(self.Frame_Download_GCC)
        self.gridLayout_5.setSpacing(12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(21, 12, 21, 12)
        self.Label_Download_GCC = QLabel(self.Frame_Download_GCC)
        self.Label_Download_GCC.setObjectName(u"Label_Download_GCC")
        self.Label_Download_GCC.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_5.addWidget(self.Label_Download_GCC, 0, 0, 1, 1)

        self.HorizontalSpacer_Download_GCC = QSpacerItem(969, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.HorizontalSpacer_Download_GCC, 0, 1, 1, 2)

        self.ProgressBar_Download_GCC = QProgressBar(self.Frame_Download_GCC)
        self.ProgressBar_Download_GCC.setObjectName(u"ProgressBar_Download_GCC")
        self.ProgressBar_Download_GCC.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Download_GCC.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(123, 123, 123, 210);\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgb(120, 180, 240));\n"
"}")

        self.gridLayout_5.addWidget(self.ProgressBar_Download_GCC, 1, 0, 1, 2)

        self.Button_Install_GCC = QPushButton(self.Frame_Download_GCC)
        self.Button_Install_GCC.setObjectName(u"Button_Install_GCC")
        self.Button_Install_GCC.setMaximumSize(QSize(30, 30))
        self.Button_Install_GCC.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_5.addWidget(self.Button_Install_GCC, 1, 2, 1, 1)


        self.verticalLayout_134.addWidget(self.Frame_Download_GCC)

        self.Frame_Download_CMake = QFrame(self.Frame_Download_Middle)
        self.Frame_Download_CMake.setObjectName(u"Frame_Download_CMake")
        self.Frame_Download_CMake.setMinimumSize(QSize(0, 90))
        self.Frame_Download_CMake.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: rgb(45, 45, 45);\n"
"}\n"
"QFrame:hover {\n"
"	border-color: rgb(60, 60, 60);\n"
"}")
        self.gridLayout_6 = QGridLayout(self.Frame_Download_CMake)
        self.gridLayout_6.setSpacing(12)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(21, 12, 21, 12)
        self.Label_Download_CMake = QLabel(self.Frame_Download_CMake)
        self.Label_Download_CMake.setObjectName(u"Label_Download_CMake")
        self.Label_Download_CMake.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.gridLayout_6.addWidget(self.Label_Download_CMake, 0, 0, 1, 1)

        self.HorizontalSpacer_Download_CMake = QSpacerItem(969, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.HorizontalSpacer_Download_CMake, 0, 1, 1, 2)

        self.ProgressBar_Download_CMake = QProgressBar(self.Frame_Download_CMake)
        self.ProgressBar_Download_CMake.setObjectName(u"ProgressBar_Download_CMake")
        self.ProgressBar_Download_CMake.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Download_CMake.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(123, 123, 123, 210);\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgb(120, 180, 240));\n"
"}")

        self.gridLayout_6.addWidget(self.ProgressBar_Download_CMake, 1, 0, 1, 2)

        self.Button_Install_CMake = QPushButton(self.Frame_Download_CMake)
        self.Button_Install_CMake.setObjectName(u"Button_Install_CMake")
        self.Button_Install_CMake.setMaximumSize(QSize(30, 30))
        self.Button_Install_CMake.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_6.addWidget(self.Button_Install_CMake, 1, 2, 1, 1)


        self.verticalLayout_134.addWidget(self.Frame_Download_CMake)

        self.Frame_Download_Python = QFrame(self.Frame_Download_Middle)
        self.Frame_Download_Python.setObjectName(u"Frame_Download_Python")
        self.Frame_Download_Python.setMinimumSize(QSize(0, 90))
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
        self.gridLayout = QGridLayout(self.Frame_Download_Python)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(21, 12, 21, 12)
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

        self.gridLayout.addWidget(self.Label_Download_Python, 0, 0, 1, 1)

        self.HorizontalSpacer_Download_Python = QSpacerItem(969, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.HorizontalSpacer_Download_Python, 0, 1, 1, 2)

        self.ProgressBar_Download_Python = QProgressBar(self.Frame_Download_Python)
        self.ProgressBar_Download_Python.setObjectName(u"ProgressBar_Download_Python")
        self.ProgressBar_Download_Python.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Download_Python.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(123, 123, 123, 210);\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgb(120, 180, 240));\n"
"}")

        self.gridLayout.addWidget(self.ProgressBar_Download_Python, 1, 0, 1, 2)

        self.Button_Install_Python = QPushButton(self.Frame_Download_Python)
        self.Button_Install_Python.setObjectName(u"Button_Install_Python")
        self.Button_Install_Python.setMaximumSize(QSize(30, 30))
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

        self.gridLayout.addWidget(self.Button_Install_Python, 1, 2, 1, 1)


        self.verticalLayout_134.addWidget(self.Frame_Download_Python)

        self.Frame_Download_PyReqs = QFrame(self.Frame_Download_Middle)
        self.Frame_Download_PyReqs.setObjectName(u"Frame_Download_PyReqs")
        self.Frame_Download_PyReqs.setMinimumSize(QSize(0, 90))
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
        self.gridLayout_3 = QGridLayout(self.Frame_Download_PyReqs)
        self.gridLayout_3.setSpacing(12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(21, 12, 21, 12)
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

        self.gridLayout_3.addWidget(self.Label_Download_PyReqs, 0, 0, 1, 1)

        self.HorizontalSpacer_Download_PyReqs = QSpacerItem(969, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.HorizontalSpacer_Download_PyReqs, 0, 1, 1, 2)

        self.ProgressBar_Download_PyReqs = QProgressBar(self.Frame_Download_PyReqs)
        self.ProgressBar_Download_PyReqs.setObjectName(u"ProgressBar_Download_PyReqs")
        self.ProgressBar_Download_PyReqs.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Download_PyReqs.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(123, 123, 123, 210);\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgb(120, 180, 240));\n"
"}")

        self.gridLayout_3.addWidget(self.ProgressBar_Download_PyReqs, 1, 0, 1, 2)

        self.Button_Install_PyReqs = QPushButton(self.Frame_Download_PyReqs)
        self.Button_Install_PyReqs.setObjectName(u"Button_Install_PyReqs")
        self.Button_Install_PyReqs.setMaximumSize(QSize(30, 30))
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

        self.gridLayout_3.addWidget(self.Button_Install_PyReqs, 1, 2, 1, 1)


        self.verticalLayout_134.addWidget(self.Frame_Download_PyReqs)

        self.Frame_Download_Pytorch = QFrame(self.Frame_Download_Middle)
        self.Frame_Download_Pytorch.setObjectName(u"Frame_Download_Pytorch")
        self.Frame_Download_Pytorch.setMinimumSize(QSize(0, 90))
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
        self.gridLayout_4 = QGridLayout(self.Frame_Download_Pytorch)
        self.gridLayout_4.setSpacing(12)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(21, 12, 21, 12)
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

        self.gridLayout_4.addWidget(self.Label_Download_Pytorch, 0, 0, 1, 1)

        self.HorizontalSpacer_Download_Pytorch = QSpacerItem(969, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.HorizontalSpacer_Download_Pytorch, 0, 1, 1, 2)

        self.ProgressBar_Download_Pytorch = QProgressBar(self.Frame_Download_Pytorch)
        self.ProgressBar_Download_Pytorch.setObjectName(u"ProgressBar_Download_Pytorch")
        self.ProgressBar_Download_Pytorch.setMaximumSize(QSize(16777215, 3))
        self.ProgressBar_Download_Pytorch.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(123, 123, 123, 210);\n"
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
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 transparent, stop:1 rgb(120, 180, 240));\n"
"}")

        self.gridLayout_4.addWidget(self.ProgressBar_Download_Pytorch, 1, 0, 1, 2)

        self.Button_Install_Pytorch = QPushButton(self.Frame_Download_Pytorch)
        self.Button_Install_Pytorch.setObjectName(u"Button_Install_Pytorch")
        self.Button_Install_Pytorch.setMaximumSize(QSize(30, 30))
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

        self.gridLayout_4.addWidget(self.Button_Install_Pytorch, 1, 2, 1, 1)


        self.verticalLayout_134.addWidget(self.Frame_Download_Pytorch)


        self.verticalLayout_81.addWidget(self.Frame_Download_Middle)

        self.VerticalSpacer_Download = QSpacerItem(17, 198, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_81.addItem(self.VerticalSpacer_Download)

        self.StackedWidget_Pages.addWidget(self.Page_Download)
        self.Page_Tools = QWidget()
        self.Page_Tools.setObjectName(u"Page_Tools")
        self.verticalLayout_101 = QVBoxLayout(self.Page_Tools)
        self.verticalLayout_101.setSpacing(21)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(21, 12, 21, 12)
        self.Frame_Tools_Top = QFrame(self.Page_Tools)
        self.Frame_Tools_Top.setObjectName(u"Frame_Tools_Top")
        self.Frame_Tools_Top.setMinimumSize(QSize(0, 60))
        self.Frame_Tools_Top.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
        self.horizontalLayout_63 = QHBoxLayout(self.Frame_Tools_Top)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.ToolButton_Tools_Title_AudioProcessor = QToolButton(self.Frame_Tools_Top)
        self.ToolButton_Tools_Title_AudioProcessor.setObjectName(u"ToolButton_Tools_Title_AudioProcessor")
        sizePolicy1.setHeightForWidth(self.ToolButton_Tools_Title_AudioProcessor.sizePolicy().hasHeightForWidth())
        self.ToolButton_Tools_Title_AudioProcessor.setSizePolicy(sizePolicy1)
        self.ToolButton_Tools_Title_AudioProcessor.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_63.addWidget(self.ToolButton_Tools_Title_AudioProcessor)

        self.ToolButton_Tools_Title_VoiceIdentifier = QToolButton(self.Frame_Tools_Top)
        self.ToolButton_Tools_Title_VoiceIdentifier.setObjectName(u"ToolButton_Tools_Title_VoiceIdentifier")
        sizePolicy1.setHeightForWidth(self.ToolButton_Tools_Title_VoiceIdentifier.sizePolicy().hasHeightForWidth())
        self.ToolButton_Tools_Title_VoiceIdentifier.setSizePolicy(sizePolicy1)
        self.ToolButton_Tools_Title_VoiceIdentifier.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_63.addWidget(self.ToolButton_Tools_Title_VoiceIdentifier)

        self.ToolButton_Tools_Title_VoiceTranscriber = QToolButton(self.Frame_Tools_Top)
        self.ToolButton_Tools_Title_VoiceTranscriber.setObjectName(u"ToolButton_Tools_Title_VoiceTranscriber")
        sizePolicy1.setHeightForWidth(self.ToolButton_Tools_Title_VoiceTranscriber.sizePolicy().hasHeightForWidth())
        self.ToolButton_Tools_Title_VoiceTranscriber.setSizePolicy(sizePolicy1)
        self.ToolButton_Tools_Title_VoiceTranscriber.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_63.addWidget(self.ToolButton_Tools_Title_VoiceTranscriber)

        self.ToolButton_Tools_Title_DatasetCreator = QToolButton(self.Frame_Tools_Top)
        self.ToolButton_Tools_Title_DatasetCreator.setObjectName(u"ToolButton_Tools_Title_DatasetCreator")
        sizePolicy1.setHeightForWidth(self.ToolButton_Tools_Title_DatasetCreator.sizePolicy().hasHeightForWidth())
        self.ToolButton_Tools_Title_DatasetCreator.setSizePolicy(sizePolicy1)
        self.ToolButton_Tools_Title_DatasetCreator.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_63.addWidget(self.ToolButton_Tools_Title_DatasetCreator)

        self.ToolButton_Tools_Title_VoiceTrainer = QToolButton(self.Frame_Tools_Top)
        self.ToolButton_Tools_Title_VoiceTrainer.setObjectName(u"ToolButton_Tools_Title_VoiceTrainer")
        sizePolicy1.setHeightForWidth(self.ToolButton_Tools_Title_VoiceTrainer.sizePolicy().hasHeightForWidth())
        self.ToolButton_Tools_Title_VoiceTrainer.setSizePolicy(sizePolicy1)
        self.ToolButton_Tools_Title_VoiceTrainer.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_63.addWidget(self.ToolButton_Tools_Title_VoiceTrainer)

        self.ToolButton_Tools_Title_VoiceConverter = QToolButton(self.Frame_Tools_Top)
        self.ToolButton_Tools_Title_VoiceConverter.setObjectName(u"ToolButton_Tools_Title_VoiceConverter")
        sizePolicy1.setHeightForWidth(self.ToolButton_Tools_Title_VoiceConverter.sizePolicy().hasHeightForWidth())
        self.ToolButton_Tools_Title_VoiceConverter.setSizePolicy(sizePolicy1)
        self.ToolButton_Tools_Title_VoiceConverter.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_63.addWidget(self.ToolButton_Tools_Title_VoiceConverter)

        self.Frame_Tools_Title_Spacer = QLabel(self.Frame_Tools_Top)
        self.Frame_Tools_Title_Spacer.setObjectName(u"Frame_Tools_Title_Spacer")
        sizePolicy3.setHeightForWidth(self.Frame_Tools_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Tools_Title_Spacer.setSizePolicy(sizePolicy3)
        self.Frame_Tools_Title_Spacer.setStyleSheet(u"QLabel {\n"
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

        self.horizontalLayout_63.addWidget(self.Frame_Tools_Title_Spacer)


        self.verticalLayout_101.addWidget(self.Frame_Tools_Top)

        self.StackedWidget_Pages_Tools = QStackedWidget(self.Page_Tools)
        self.StackedWidget_Pages_Tools.setObjectName(u"StackedWidget_Pages_Tools")
        self.StackedWidget_Pages_Tools.setStyleSheet(u"QWidget {\n"
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
        self.StackedWidget_Pages_Tool_AudioProcessor = QWidget()
        self.StackedWidget_Pages_Tool_AudioProcessor.setObjectName(u"StackedWidget_Pages_Tool_AudioProcessor")
        self.gridLayout_8 = QGridLayout(self.StackedWidget_Pages_Tool_AudioProcessor)
        self.gridLayout_8.setSpacing(12)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_Tool_AudioProcessor = QWidget(self.StackedWidget_Pages_Tool_AudioProcessor)
        self.Widget_Left_Tool_AudioProcessor.setObjectName(u"Widget_Left_Tool_AudioProcessor")
        self.Widget_Left_Tool_AudioProcessor.setMaximumSize(QSize(210, 16777215))
        self.Widget_Left_Tool_AudioProcessor.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_162 = QVBoxLayout(self.Widget_Left_Tool_AudioProcessor)
        self.verticalLayout_162.setSpacing(12)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Tool_AudioProcessor = QTreeWidget(self.Widget_Left_Tool_AudioProcessor)
        __qtreewidgetitem = QTreeWidgetItem(self.TreeWidget_Catalogue_Tool_AudioProcessor)
        QTreeWidgetItem(__qtreewidgetitem)
        self.TreeWidget_Catalogue_Tool_AudioProcessor.setObjectName(u"TreeWidget_Catalogue_Tool_AudioProcessor")
        self.TreeWidget_Catalogue_Tool_AudioProcessor.setStyleSheet(u"QTreeWidget {\n"
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
"}*/")

        self.verticalLayout_162.addWidget(self.TreeWidget_Catalogue_Tool_AudioProcessor)


        self.gridLayout_8.addWidget(self.Widget_Left_Tool_AudioProcessor, 0, 0, 1, 1)

        self.ScrollArea_Middle_Tool_AudioProcessor = QScrollArea(self.StackedWidget_Pages_Tool_AudioProcessor)
        self.ScrollArea_Middle_Tool_AudioProcessor.setObjectName(u"ScrollArea_Middle_Tool_AudioProcessor")
        self.ScrollArea_Middle_Tool_AudioProcessor.setMinimumSize(QSize(630, 0))
        self.ScrollArea_Middle_Tool_AudioProcessor.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgb(36, 36, 36);\n"
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
"	height"
                        ": 0px;\n"
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
"	border-widt"
                        "h: 0px;\n"
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
        self.ScrollArea_Middle_Tool_AudioProcessor.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Tool_AudioProcessor.setWidgetResizable(True)
        self.ScrollArea_Middle_WidgetContents_Tool_AudioProcessor = QWidget()
        self.ScrollArea_Middle_WidgetContents_Tool_AudioProcessor.setObjectName(u"ScrollArea_Middle_WidgetContents_Tool_AudioProcessor")
        self.ScrollArea_Middle_WidgetContents_Tool_AudioProcessor.setGeometry(QRect(0, 0, 621, 1096))
        self.ScrollArea_Middle_WidgetContents_Tool_AudioProcessor.setMinimumSize(QSize(0, 0))
        self.verticalLayout_149 = QVBoxLayout(self.ScrollArea_Middle_WidgetContents_Tool_AudioProcessor)
        self.verticalLayout_149.setSpacing(12)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_Tool_AudioProcessor = QGroupBox(self.ScrollArea_Middle_WidgetContents_Tool_AudioProcessor)
        self.GroupBox_EssentialParams_Tool_AudioProcessor.setObjectName(u"GroupBox_EssentialParams_Tool_AudioProcessor")
        self.GroupBox_EssentialParams_Tool_AudioProcessor.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_150 = QVBoxLayout(self.GroupBox_EssentialParams_Tool_AudioProcessor)
        self.verticalLayout_150.setSpacing(0)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor = QCheckBox(self.GroupBox_EssentialParams_Tool_AudioProcessor)
        self.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor.setObjectName(u"CheckBox_Toggle_BasicSettings_Tool_AudioProcessor")
        self.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_150.addWidget(self.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor)

        self.Frame_BasicSettings_Tool_AudioProcessor = QFrame(self.GroupBox_EssentialParams_Tool_AudioProcessor)
        self.Frame_BasicSettings_Tool_AudioProcessor.setObjectName(u"Frame_BasicSettings_Tool_AudioProcessor")
        self.verticalLayout_151 = QVBoxLayout(self.Frame_BasicSettings_Tool_AudioProcessor)
        self.verticalLayout_151.setSpacing(0)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.verticalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_AudioProcessor_Media_Dir_Input = QFrame(self.Frame_BasicSettings_Tool_AudioProcessor)
        self.Frame_Tool_AudioProcessor_Media_Dir_Input.setObjectName(u"Frame_Tool_AudioProcessor_Media_Dir_Input")
        self.Frame_Tool_AudioProcessor_Media_Dir_Input.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_AudioProcessor_Media_Dir_Input.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_152 = QVBoxLayout(self.Frame_Tool_AudioProcessor_Media_Dir_Input)
        self.verticalLayout_152.setSpacing(12)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.verticalLayout_152.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_AudioProcessor_Media_Dir_Input = QLabel(self.Frame_Tool_AudioProcessor_Media_Dir_Input)
        self.Label_Tool_AudioProcessor_Media_Dir_Input.setObjectName(u"Label_Tool_AudioProcessor_Media_Dir_Input")
        self.Label_Tool_AudioProcessor_Media_Dir_Input.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_152.addWidget(self.Label_Tool_AudioProcessor_Media_Dir_Input)

        self.ChildFrame_Tool_AudioProcessor_Media_Dir_Input = QFrame(self.Frame_Tool_AudioProcessor_Media_Dir_Input)
        self.ChildFrame_Tool_AudioProcessor_Media_Dir_Input.setObjectName(u"ChildFrame_Tool_AudioProcessor_Media_Dir_Input")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_AudioProcessor_Media_Dir_Input.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_AudioProcessor_Media_Dir_Input.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_AudioProcessor_Media_Dir_Input.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_77 = QHBoxLayout(self.ChildFrame_Tool_AudioProcessor_Media_Dir_Input)
        self.horizontalLayout_77.setSpacing(12)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_AudioProcessor_Media_Dir_Input = QLineEdit(self.ChildFrame_Tool_AudioProcessor_Media_Dir_Input)
        self.LineEdit_Tool_AudioProcessor_Media_Dir_Input.setObjectName(u"LineEdit_Tool_AudioProcessor_Media_Dir_Input")
        self.LineEdit_Tool_AudioProcessor_Media_Dir_Input.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_77.addWidget(self.LineEdit_Tool_AudioProcessor_Media_Dir_Input)

        self.Button_Tool_AudioProcessor_Media_Dir_Input = QPushButton(self.ChildFrame_Tool_AudioProcessor_Media_Dir_Input)
        self.Button_Tool_AudioProcessor_Media_Dir_Input.setObjectName(u"Button_Tool_AudioProcessor_Media_Dir_Input")
        sizePolicy1.setHeightForWidth(self.Button_Tool_AudioProcessor_Media_Dir_Input.sizePolicy().hasHeightForWidth())
        self.Button_Tool_AudioProcessor_Media_Dir_Input.setSizePolicy(sizePolicy1)
        self.Button_Tool_AudioProcessor_Media_Dir_Input.setMaximumSize(QSize(24, 24))
        self.Button_Tool_AudioProcessor_Media_Dir_Input.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_77.addWidget(self.Button_Tool_AudioProcessor_Media_Dir_Input)


        self.verticalLayout_152.addWidget(self.ChildFrame_Tool_AudioProcessor_Media_Dir_Input)


        self.verticalLayout_151.addWidget(self.Frame_Tool_AudioProcessor_Media_Dir_Input)

        self.Frame_Tool_AudioProcessor_Media_Format_Output = QFrame(self.Frame_BasicSettings_Tool_AudioProcessor)
        self.Frame_Tool_AudioProcessor_Media_Format_Output.setObjectName(u"Frame_Tool_AudioProcessor_Media_Format_Output")
        self.Frame_Tool_AudioProcessor_Media_Format_Output.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_AudioProcessor_Media_Format_Output.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_153 = QVBoxLayout(self.Frame_Tool_AudioProcessor_Media_Format_Output)
        self.verticalLayout_153.setSpacing(12)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.verticalLayout_153.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_AudioProcessor_Media_Format_Output = QLabel(self.Frame_Tool_AudioProcessor_Media_Format_Output)
        self.Label_Tool_AudioProcessor_Media_Format_Output.setObjectName(u"Label_Tool_AudioProcessor_Media_Format_Output")
        self.Label_Tool_AudioProcessor_Media_Format_Output.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_153.addWidget(self.Label_Tool_AudioProcessor_Media_Format_Output)

        self.ComboBox_Tool_AudioProcessor_Media_Format_Output = QComboBox(self.Frame_Tool_AudioProcessor_Media_Format_Output)
        self.ComboBox_Tool_AudioProcessor_Media_Format_Output.setObjectName(u"ComboBox_Tool_AudioProcessor_Media_Format_Output")
        self.ComboBox_Tool_AudioProcessor_Media_Format_Output.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_153.addWidget(self.ComboBox_Tool_AudioProcessor_Media_Format_Output)


        self.verticalLayout_151.addWidget(self.Frame_Tool_AudioProcessor_Media_Format_Output)

        self.Frame_Tool_AudioProcessor_Media_Dir_Output = QFrame(self.Frame_BasicSettings_Tool_AudioProcessor)
        self.Frame_Tool_AudioProcessor_Media_Dir_Output.setObjectName(u"Frame_Tool_AudioProcessor_Media_Dir_Output")
        self.Frame_Tool_AudioProcessor_Media_Dir_Output.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_AudioProcessor_Media_Dir_Output.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_154 = QVBoxLayout(self.Frame_Tool_AudioProcessor_Media_Dir_Output)
        self.verticalLayout_154.setSpacing(12)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_AudioProcessor_Media_Dir_Output = QLabel(self.Frame_Tool_AudioProcessor_Media_Dir_Output)
        self.Label_Tool_AudioProcessor_Media_Dir_Output.setObjectName(u"Label_Tool_AudioProcessor_Media_Dir_Output")
        self.Label_Tool_AudioProcessor_Media_Dir_Output.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_154.addWidget(self.Label_Tool_AudioProcessor_Media_Dir_Output)

        self.ChildFrame_Tool_AudioProcessor_Media_Dir_Output = QFrame(self.Frame_Tool_AudioProcessor_Media_Dir_Output)
        self.ChildFrame_Tool_AudioProcessor_Media_Dir_Output.setObjectName(u"ChildFrame_Tool_AudioProcessor_Media_Dir_Output")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_AudioProcessor_Media_Dir_Output.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_AudioProcessor_Media_Dir_Output.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_AudioProcessor_Media_Dir_Output.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_78 = QHBoxLayout(self.ChildFrame_Tool_AudioProcessor_Media_Dir_Output)
        self.horizontalLayout_78.setSpacing(12)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_AudioProcessor_Media_Dir_Output = QLineEdit(self.ChildFrame_Tool_AudioProcessor_Media_Dir_Output)
        self.LineEdit_Tool_AudioProcessor_Media_Dir_Output.setObjectName(u"LineEdit_Tool_AudioProcessor_Media_Dir_Output")
        self.LineEdit_Tool_AudioProcessor_Media_Dir_Output.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_78.addWidget(self.LineEdit_Tool_AudioProcessor_Media_Dir_Output)

        self.Button_Tool_AudioProcessor_Media_Dir_Output = QPushButton(self.ChildFrame_Tool_AudioProcessor_Media_Dir_Output)
        self.Button_Tool_AudioProcessor_Media_Dir_Output.setObjectName(u"Button_Tool_AudioProcessor_Media_Dir_Output")
        sizePolicy1.setHeightForWidth(self.Button_Tool_AudioProcessor_Media_Dir_Output.sizePolicy().hasHeightForWidth())
        self.Button_Tool_AudioProcessor_Media_Dir_Output.setSizePolicy(sizePolicy1)
        self.Button_Tool_AudioProcessor_Media_Dir_Output.setMaximumSize(QSize(24, 24))
        self.Button_Tool_AudioProcessor_Media_Dir_Output.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_78.addWidget(self.Button_Tool_AudioProcessor_Media_Dir_Output)


        self.verticalLayout_154.addWidget(self.ChildFrame_Tool_AudioProcessor_Media_Dir_Output)


        self.verticalLayout_151.addWidget(self.Frame_Tool_AudioProcessor_Media_Dir_Output)


        self.verticalLayout_150.addWidget(self.Frame_BasicSettings_Tool_AudioProcessor)

        self.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor = QCheckBox(self.GroupBox_EssentialParams_Tool_AudioProcessor)
        self.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor.setObjectName(u"CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor")
        self.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_150.addWidget(self.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor)

        self.Frame_AdvanceSettings_Tool_AudioProcessor = QFrame(self.GroupBox_EssentialParams_Tool_AudioProcessor)
        self.Frame_AdvanceSettings_Tool_AudioProcessor.setObjectName(u"Frame_AdvanceSettings_Tool_AudioProcessor")
        self.verticalLayout_155 = QVBoxLayout(self.Frame_AdvanceSettings_Tool_AudioProcessor)
        self.verticalLayout_155.setSpacing(0)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.verticalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_AudioProcessor_RMS_Threshold = QFrame(self.Frame_AdvanceSettings_Tool_AudioProcessor)
        self.Frame_Tool_AudioProcessor_RMS_Threshold.setObjectName(u"Frame_Tool_AudioProcessor_RMS_Threshold")
        self.Frame_Tool_AudioProcessor_RMS_Threshold.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_AudioProcessor_RMS_Threshold.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_156 = QVBoxLayout(self.Frame_Tool_AudioProcessor_RMS_Threshold)
        self.verticalLayout_156.setSpacing(12)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_AudioProcessor_RMS_Threshold = QLabel(self.Frame_Tool_AudioProcessor_RMS_Threshold)
        self.Label_Tool_AudioProcessor_RMS_Threshold.setObjectName(u"Label_Tool_AudioProcessor_RMS_Threshold")
        self.Label_Tool_AudioProcessor_RMS_Threshold.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_156.addWidget(self.Label_Tool_AudioProcessor_RMS_Threshold)

        self.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold = QDoubleSpinBox(self.Frame_Tool_AudioProcessor_RMS_Threshold)
        self.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setObjectName(u"DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold")
        self.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setEnabled(True)
        self.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold.setMaximum(999999.000000000000000)

        self.verticalLayout_156.addWidget(self.DoubleSpinBox_Tool_AudioProcessor_RMS_Threshold)


        self.verticalLayout_155.addWidget(self.Frame_Tool_AudioProcessor_RMS_Threshold)

        self.Frame_Tool_AudioProcessor_Audio_Length_Min = QFrame(self.Frame_AdvanceSettings_Tool_AudioProcessor)
        self.Frame_Tool_AudioProcessor_Audio_Length_Min.setObjectName(u"Frame_Tool_AudioProcessor_Audio_Length_Min")
        self.Frame_Tool_AudioProcessor_Audio_Length_Min.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_AudioProcessor_Audio_Length_Min.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_157 = QVBoxLayout(self.Frame_Tool_AudioProcessor_Audio_Length_Min)
        self.verticalLayout_157.setSpacing(12)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalLayout_157.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_AudioProcessor_Audio_Length_Min = QLabel(self.Frame_Tool_AudioProcessor_Audio_Length_Min)
        self.Label_Tool_AudioProcessor_Audio_Length_Min.setObjectName(u"Label_Tool_AudioProcessor_Audio_Length_Min")
        self.Label_Tool_AudioProcessor_Audio_Length_Min.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_157.addWidget(self.Label_Tool_AudioProcessor_Audio_Length_Min)

        self.SpinBox_Tool_AudioProcessor_Audio_Length_Min = QSpinBox(self.Frame_Tool_AudioProcessor_Audio_Length_Min)
        self.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setObjectName(u"SpinBox_Tool_AudioProcessor_Audio_Length_Min")
        self.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setMinimum(-999999)
        self.SpinBox_Tool_AudioProcessor_Audio_Length_Min.setMaximum(999999)

        self.verticalLayout_157.addWidget(self.SpinBox_Tool_AudioProcessor_Audio_Length_Min)


        self.verticalLayout_155.addWidget(self.Frame_Tool_AudioProcessor_Audio_Length_Min)

        self.Frame_Tool_AudioProcessor_Silent_Interval_Min = QFrame(self.Frame_AdvanceSettings_Tool_AudioProcessor)
        self.Frame_Tool_AudioProcessor_Silent_Interval_Min.setObjectName(u"Frame_Tool_AudioProcessor_Silent_Interval_Min")
        self.Frame_Tool_AudioProcessor_Silent_Interval_Min.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_AudioProcessor_Silent_Interval_Min.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_158 = QVBoxLayout(self.Frame_Tool_AudioProcessor_Silent_Interval_Min)
        self.verticalLayout_158.setSpacing(12)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_AudioProcessor_Silent_Interval_Min = QLabel(self.Frame_Tool_AudioProcessor_Silent_Interval_Min)
        self.Label_Tool_AudioProcessor_Silent_Interval_Min.setObjectName(u"Label_Tool_AudioProcessor_Silent_Interval_Min")
        self.Label_Tool_AudioProcessor_Silent_Interval_Min.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_158.addWidget(self.Label_Tool_AudioProcessor_Silent_Interval_Min)

        self.SpinBox_Tool_AudioProcessor_Silent_Interval_Min = QSpinBox(self.Frame_Tool_AudioProcessor_Silent_Interval_Min)
        self.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setObjectName(u"SpinBox_Tool_AudioProcessor_Silent_Interval_Min")
        self.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setMinimum(-999999)
        self.SpinBox_Tool_AudioProcessor_Silent_Interval_Min.setMaximum(999999)

        self.verticalLayout_158.addWidget(self.SpinBox_Tool_AudioProcessor_Silent_Interval_Min)


        self.verticalLayout_155.addWidget(self.Frame_Tool_AudioProcessor_Silent_Interval_Min)

        self.Frame_Tool_AudioProcessor_Hop_Size = QFrame(self.Frame_AdvanceSettings_Tool_AudioProcessor)
        self.Frame_Tool_AudioProcessor_Hop_Size.setObjectName(u"Frame_Tool_AudioProcessor_Hop_Size")
        self.Frame_Tool_AudioProcessor_Hop_Size.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_AudioProcessor_Hop_Size.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_159 = QVBoxLayout(self.Frame_Tool_AudioProcessor_Hop_Size)
        self.verticalLayout_159.setSpacing(12)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.verticalLayout_159.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_AudioProcessor_Hop_Size = QLabel(self.Frame_Tool_AudioProcessor_Hop_Size)
        self.Label_Tool_AudioProcessor_Hop_Size.setObjectName(u"Label_Tool_AudioProcessor_Hop_Size")
        self.Label_Tool_AudioProcessor_Hop_Size.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_159.addWidget(self.Label_Tool_AudioProcessor_Hop_Size)

        self.SpinBox_Tool_AudioProcessor_Hop_Size = QSpinBox(self.Frame_Tool_AudioProcessor_Hop_Size)
        self.SpinBox_Tool_AudioProcessor_Hop_Size.setObjectName(u"SpinBox_Tool_AudioProcessor_Hop_Size")
        self.SpinBox_Tool_AudioProcessor_Hop_Size.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Tool_AudioProcessor_Hop_Size.setMinimum(-999999)
        self.SpinBox_Tool_AudioProcessor_Hop_Size.setMaximum(999999)

        self.verticalLayout_159.addWidget(self.SpinBox_Tool_AudioProcessor_Hop_Size)


        self.verticalLayout_155.addWidget(self.Frame_Tool_AudioProcessor_Hop_Size)

        self.Frame_Tool_AudioProcessor_Silence_Kept_Max = QFrame(self.Frame_AdvanceSettings_Tool_AudioProcessor)
        self.Frame_Tool_AudioProcessor_Silence_Kept_Max.setObjectName(u"Frame_Tool_AudioProcessor_Silence_Kept_Max")
        self.Frame_Tool_AudioProcessor_Silence_Kept_Max.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_AudioProcessor_Silence_Kept_Max.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_160 = QVBoxLayout(self.Frame_Tool_AudioProcessor_Silence_Kept_Max)
        self.verticalLayout_160.setSpacing(12)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.verticalLayout_160.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_AudioProcessor_Silence_Kept_Max = QLabel(self.Frame_Tool_AudioProcessor_Silence_Kept_Max)
        self.Label_Tool_AudioProcessor_Silence_Kept_Max.setObjectName(u"Label_Tool_AudioProcessor_Silence_Kept_Max")
        self.Label_Tool_AudioProcessor_Silence_Kept_Max.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_160.addWidget(self.Label_Tool_AudioProcessor_Silence_Kept_Max)

        self.SpinBox_Tool_AudioProcessor_Silence_Kept_Max = QSpinBox(self.Frame_Tool_AudioProcessor_Silence_Kept_Max)
        self.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setObjectName(u"SpinBox_Tool_AudioProcessor_Silence_Kept_Max")
        self.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setMinimum(-999999)
        self.SpinBox_Tool_AudioProcessor_Silence_Kept_Max.setMaximum(999999)

        self.verticalLayout_160.addWidget(self.SpinBox_Tool_AudioProcessor_Silence_Kept_Max)


        self.verticalLayout_155.addWidget(self.Frame_Tool_AudioProcessor_Silence_Kept_Max)


        self.verticalLayout_150.addWidget(self.Frame_AdvanceSettings_Tool_AudioProcessor)


        self.verticalLayout_149.addWidget(self.GroupBox_EssentialParams_Tool_AudioProcessor)

        self.ScrollArea_Middle_Tool_AudioProcessor.setWidget(self.ScrollArea_Middle_WidgetContents_Tool_AudioProcessor)

        self.gridLayout_8.addWidget(self.ScrollArea_Middle_Tool_AudioProcessor, 0, 1, 1, 1)

        self.Widget_Right_Tool_AudioProcessor = QWidget(self.StackedWidget_Pages_Tool_AudioProcessor)
        self.Widget_Right_Tool_AudioProcessor.setObjectName(u"Widget_Right_Tool_AudioProcessor")
        self.Widget_Right_Tool_AudioProcessor.setMaximumSize(QSize(420, 16777215))
        self.Widget_Right_Tool_AudioProcessor.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout_9 = QGridLayout(self.Widget_Right_Tool_AudioProcessor)
        self.gridLayout_9.setSpacing(12)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Tool_AudioProcessor = QTextBrowser(self.Widget_Right_Tool_AudioProcessor)
        self.TextBrowser_Params_Tool_AudioProcessor.setObjectName(u"TextBrowser_Params_Tool_AudioProcessor")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Tool_AudioProcessor.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Tool_AudioProcessor.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Tool_AudioProcessor.setStyleSheet(u"QTextBrowser {\n"
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

        self.gridLayout_9.addWidget(self.TextBrowser_Params_Tool_AudioProcessor, 0, 0, 1, 1)

        self.Button_CheckOutput_Tool_AudioProcessor = QPushButton(self.Widget_Right_Tool_AudioProcessor)
        self.Button_CheckOutput_Tool_AudioProcessor.setObjectName(u"Button_CheckOutput_Tool_AudioProcessor")
        self.Button_CheckOutput_Tool_AudioProcessor.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_9.addWidget(self.Button_CheckOutput_Tool_AudioProcessor, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.Widget_Right_Tool_AudioProcessor, 0, 2, 1, 1)

        self.ProgressBar_Tool_AudioProcessor = QProgressBar(self.StackedWidget_Pages_Tool_AudioProcessor)
        self.ProgressBar_Tool_AudioProcessor.setObjectName(u"ProgressBar_Tool_AudioProcessor")
        self.ProgressBar_Tool_AudioProcessor.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Tool_AudioProcessor.setStyleSheet(u"QProgressBar {\n"
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
        self.ProgressBar_Tool_AudioProcessor.setValue(0)
        self.ProgressBar_Tool_AudioProcessor.setTextVisible(False)
        self.verticalLayout_24 = QVBoxLayout(self.ProgressBar_Tool_AudioProcessor)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Tool_AudioProcessor = QStackedWidget(self.ProgressBar_Tool_AudioProcessor)
        self.StackedWidget_Tool_AudioProcessor.setObjectName(u"StackedWidget_Tool_AudioProcessor")
        self.StackedWidget_Tool_AudioProcessor.setMinimumSize(QSize(0, 30))
        self.StackedWidget_Tool_AudioProcessor.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_Tool_AudioProcessor.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_Tool_AudioProcessor_Execute = QWidget()
        self.Page_Tool_AudioProcessor_Execute.setObjectName(u"Page_Tool_AudioProcessor_Execute")
        self.verticalLayout_86 = QVBoxLayout(self.Page_Tool_AudioProcessor_Execute)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_AudioProcessor_Execute = QPushButton(self.Page_Tool_AudioProcessor_Execute)
        self.Button_Tool_AudioProcessor_Execute.setObjectName(u"Button_Tool_AudioProcessor_Execute")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Button_Tool_AudioProcessor_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Tool_AudioProcessor_Execute.setSizePolicy(sizePolicy5)
        self.Button_Tool_AudioProcessor_Execute.setMinimumSize(QSize(0, 30))
        self.Button_Tool_AudioProcessor_Execute.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_86.addWidget(self.Button_Tool_AudioProcessor_Execute)

        self.StackedWidget_Tool_AudioProcessor.addWidget(self.Page_Tool_AudioProcessor_Execute)
        self.Page_Tool_AudioProcessor_Terminate = QWidget()
        self.Page_Tool_AudioProcessor_Terminate.setObjectName(u"Page_Tool_AudioProcessor_Terminate")
        self.verticalLayout_87 = QVBoxLayout(self.Page_Tool_AudioProcessor_Terminate)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_AudioProcessor_Terminate = QPushButton(self.Page_Tool_AudioProcessor_Terminate)
        self.Button_Tool_AudioProcessor_Terminate.setObjectName(u"Button_Tool_AudioProcessor_Terminate")
        sizePolicy5.setHeightForWidth(self.Button_Tool_AudioProcessor_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Tool_AudioProcessor_Terminate.setSizePolicy(sizePolicy5)
        self.Button_Tool_AudioProcessor_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_Tool_AudioProcessor_Terminate.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_87.addWidget(self.Button_Tool_AudioProcessor_Terminate)

        self.StackedWidget_Tool_AudioProcessor.addWidget(self.Page_Tool_AudioProcessor_Terminate)

        self.verticalLayout_24.addWidget(self.StackedWidget_Tool_AudioProcessor)


        self.gridLayout_8.addWidget(self.ProgressBar_Tool_AudioProcessor, 1, 0, 1, 3)

        self.StackedWidget_Pages_Tools.addWidget(self.StackedWidget_Pages_Tool_AudioProcessor)
        self.StackedWidget_Pages_Tool_VoiceIdentifier = QWidget()
        self.StackedWidget_Pages_Tool_VoiceIdentifier.setObjectName(u"StackedWidget_Pages_Tool_VoiceIdentifier")
        self.gridLayout_7 = QGridLayout(self.StackedWidget_Pages_Tool_VoiceIdentifier)
        self.gridLayout_7.setSpacing(12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_Tool_VoiceIdentifier = QWidget(self.StackedWidget_Pages_Tool_VoiceIdentifier)
        self.Widget_Left_Tool_VoiceIdentifier.setObjectName(u"Widget_Left_Tool_VoiceIdentifier")
        self.Widget_Left_Tool_VoiceIdentifier.setMaximumSize(QSize(210, 16777215))
        self.Widget_Left_Tool_VoiceIdentifier.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.Widget_Left_Tool_VoiceIdentifier)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Tool_VoiceIdentifier = QTreeWidget(self.Widget_Left_Tool_VoiceIdentifier)
        __qtreewidgetitem1 = QTreeWidgetItem(self.TreeWidget_Catalogue_Tool_VoiceIdentifier)
        QTreeWidgetItem(__qtreewidgetitem1)
        self.TreeWidget_Catalogue_Tool_VoiceIdentifier.setObjectName(u"TreeWidget_Catalogue_Tool_VoiceIdentifier")
        self.TreeWidget_Catalogue_Tool_VoiceIdentifier.setStyleSheet(u"QTreeWidget {\n"
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
"}*/")

        self.verticalLayout_4.addWidget(self.TreeWidget_Catalogue_Tool_VoiceIdentifier)


        self.gridLayout_7.addWidget(self.Widget_Left_Tool_VoiceIdentifier, 0, 0, 1, 1)

        self.ScrollArea_Middle_Tool_VoiceIdentifier = QScrollArea(self.StackedWidget_Pages_Tool_VoiceIdentifier)
        self.ScrollArea_Middle_Tool_VoiceIdentifier.setObjectName(u"ScrollArea_Middle_Tool_VoiceIdentifier")
        self.ScrollArea_Middle_Tool_VoiceIdentifier.setMinimumSize(QSize(630, 0))
        self.ScrollArea_Middle_Tool_VoiceIdentifier.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgb(36, 36, 36);\n"
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
"	height"
                        ": 0px;\n"
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
"	border-widt"
                        "h: 0px;\n"
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
        self.ScrollArea_Middle_Tool_VoiceIdentifier.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Tool_VoiceIdentifier.setWidgetResizable(True)
        self.ScrollArea_Right_WidgetContents_Tool_VoiceIdentifier = QWidget()
        self.ScrollArea_Right_WidgetContents_Tool_VoiceIdentifier.setObjectName(u"ScrollArea_Right_WidgetContents_Tool_VoiceIdentifier")
        self.ScrollArea_Right_WidgetContents_Tool_VoiceIdentifier.setGeometry(QRect(0, 0, 621, 1342))
        self.ScrollArea_Right_WidgetContents_Tool_VoiceIdentifier.setMinimumSize(QSize(0, 0))
        self.verticalLayout_28 = QVBoxLayout(self.ScrollArea_Right_WidgetContents_Tool_VoiceIdentifier)
        self.verticalLayout_28.setSpacing(12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_Tool_VoiceIdentifier = QGroupBox(self.ScrollArea_Right_WidgetContents_Tool_VoiceIdentifier)
        self.GroupBox_EssentialParams_Tool_VoiceIdentifier.setObjectName(u"GroupBox_EssentialParams_Tool_VoiceIdentifier")
        self.GroupBox_EssentialParams_Tool_VoiceIdentifier.setMaximumSize(QSize(16777215, 16777215))
        self.GroupBox_EssentialParams_Tool_VoiceIdentifier.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_33 = QVBoxLayout(self.GroupBox_EssentialParams_Tool_VoiceIdentifier)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier = QCheckBox(self.GroupBox_EssentialParams_Tool_VoiceIdentifier)
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier.setObjectName(u"CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier")
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_33.addWidget(self.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier)

        self.Frame_BasicSettings_Tool_VoiceIdentifier = QFrame(self.GroupBox_EssentialParams_Tool_VoiceIdentifier)
        self.Frame_BasicSettings_Tool_VoiceIdentifier.setObjectName(u"Frame_BasicSettings_Tool_VoiceIdentifier")
        self.verticalLayout_137 = QVBoxLayout(self.Frame_BasicSettings_Tool_VoiceIdentifier)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_VoiceIdentifier_Audio_Dir_Input = QFrame(self.Frame_BasicSettings_Tool_VoiceIdentifier)
        self.Frame_Tool_VoiceIdentifier_Audio_Dir_Input.setObjectName(u"Frame_Tool_VoiceIdentifier_Audio_Dir_Input")
        self.Frame_Tool_VoiceIdentifier_Audio_Dir_Input.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceIdentifier_Audio_Dir_Input.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_121 = QVBoxLayout(self.Frame_Tool_VoiceIdentifier_Audio_Dir_Input)
        self.verticalLayout_121.setSpacing(12)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceIdentifier_Audio_Dir_Input = QLabel(self.Frame_Tool_VoiceIdentifier_Audio_Dir_Input)
        self.Label_Tool_VoiceIdentifier_Audio_Dir_Input.setObjectName(u"Label_Tool_VoiceIdentifier_Audio_Dir_Input")
        self.Label_Tool_VoiceIdentifier_Audio_Dir_Input.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_121.addWidget(self.Label_Tool_VoiceIdentifier_Audio_Dir_Input)

        self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Input = QFrame(self.Frame_Tool_VoiceIdentifier_Audio_Dir_Input)
        self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Input.setObjectName(u"ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Input")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Input.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Input.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Input.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_31 = QHBoxLayout(self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Input)
        self.horizontalLayout_31.setSpacing(12)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input = QLineEdit(self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Input)
        self.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input.setObjectName(u"LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input")
        self.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_31.addWidget(self.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Input)

        self.Button_Tool_VoiceIdentifier_Audio_Dir_Input = QPushButton(self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Input)
        self.Button_Tool_VoiceIdentifier_Audio_Dir_Input.setObjectName(u"Button_Tool_VoiceIdentifier_Audio_Dir_Input")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceIdentifier_Audio_Dir_Input.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceIdentifier_Audio_Dir_Input.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceIdentifier_Audio_Dir_Input.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceIdentifier_Audio_Dir_Input.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_31.addWidget(self.Button_Tool_VoiceIdentifier_Audio_Dir_Input)


        self.verticalLayout_121.addWidget(self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Input)


        self.verticalLayout_137.addWidget(self.Frame_Tool_VoiceIdentifier_Audio_Dir_Input)

        self.Frame_Tool_VoiceIdentifier_Audio_Path_Std = QFrame(self.Frame_BasicSettings_Tool_VoiceIdentifier)
        self.Frame_Tool_VoiceIdentifier_Audio_Path_Std.setObjectName(u"Frame_Tool_VoiceIdentifier_Audio_Path_Std")
        self.Frame_Tool_VoiceIdentifier_Audio_Path_Std.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceIdentifier_Audio_Path_Std.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_138 = QVBoxLayout(self.Frame_Tool_VoiceIdentifier_Audio_Path_Std)
        self.verticalLayout_138.setSpacing(12)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceIdentifier_Audio_Path_Std = QLabel(self.Frame_Tool_VoiceIdentifier_Audio_Path_Std)
        self.Label_Tool_VoiceIdentifier_Audio_Path_Std.setObjectName(u"Label_Tool_VoiceIdentifier_Audio_Path_Std")
        self.Label_Tool_VoiceIdentifier_Audio_Path_Std.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_138.addWidget(self.Label_Tool_VoiceIdentifier_Audio_Path_Std)

        self.ChildFrame_Tool_VoiceIdentifier_Audio_Path_Std = QFrame(self.Frame_Tool_VoiceIdentifier_Audio_Path_Std)
        self.ChildFrame_Tool_VoiceIdentifier_Audio_Path_Std.setObjectName(u"ChildFrame_Tool_VoiceIdentifier_Audio_Path_Std")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceIdentifier_Audio_Path_Std.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceIdentifier_Audio_Path_Std.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceIdentifier_Audio_Path_Std.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_32 = QHBoxLayout(self.ChildFrame_Tool_VoiceIdentifier_Audio_Path_Std)
        self.horizontalLayout_32.setSpacing(12)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceIdentifier_Audio_Path_Std = QLineEdit(self.ChildFrame_Tool_VoiceIdentifier_Audio_Path_Std)
        self.LineEdit_Tool_VoiceIdentifier_Audio_Path_Std.setObjectName(u"LineEdit_Tool_VoiceIdentifier_Audio_Path_Std")
        self.LineEdit_Tool_VoiceIdentifier_Audio_Path_Std.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_32.addWidget(self.LineEdit_Tool_VoiceIdentifier_Audio_Path_Std)

        self.Button_Tool_VoiceIdentifier_Audio_Path_Std = QPushButton(self.ChildFrame_Tool_VoiceIdentifier_Audio_Path_Std)
        self.Button_Tool_VoiceIdentifier_Audio_Path_Std.setObjectName(u"Button_Tool_VoiceIdentifier_Audio_Path_Std")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceIdentifier_Audio_Path_Std.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceIdentifier_Audio_Path_Std.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceIdentifier_Audio_Path_Std.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceIdentifier_Audio_Path_Std.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_32.addWidget(self.Button_Tool_VoiceIdentifier_Audio_Path_Std)


        self.verticalLayout_138.addWidget(self.ChildFrame_Tool_VoiceIdentifier_Audio_Path_Std)


        self.verticalLayout_137.addWidget(self.Frame_Tool_VoiceIdentifier_Audio_Path_Std)

        self.Frame_Tool_VoiceIdentifier_Speaker = QFrame(self.Frame_BasicSettings_Tool_VoiceIdentifier)
        self.Frame_Tool_VoiceIdentifier_Speaker.setObjectName(u"Frame_Tool_VoiceIdentifier_Speaker")
        self.Frame_Tool_VoiceIdentifier_Speaker.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceIdentifier_Speaker.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_139 = QVBoxLayout(self.Frame_Tool_VoiceIdentifier_Speaker)
        self.verticalLayout_139.setSpacing(12)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceIdentifier_Speaker = QLabel(self.Frame_Tool_VoiceIdentifier_Speaker)
        self.Label_Tool_VoiceIdentifier_Speaker.setObjectName(u"Label_Tool_VoiceIdentifier_Speaker")
        self.Label_Tool_VoiceIdentifier_Speaker.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_139.addWidget(self.Label_Tool_VoiceIdentifier_Speaker)

        self.LineEdit_Tool_VoiceIdentifier_Speaker = QLineEdit(self.Frame_Tool_VoiceIdentifier_Speaker)
        self.LineEdit_Tool_VoiceIdentifier_Speaker.setObjectName(u"LineEdit_Tool_VoiceIdentifier_Speaker")
        self.LineEdit_Tool_VoiceIdentifier_Speaker.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_139.addWidget(self.LineEdit_Tool_VoiceIdentifier_Speaker)


        self.verticalLayout_137.addWidget(self.Frame_Tool_VoiceIdentifier_Speaker)

        self.Frame_Tool_VoiceIdentifier_DecisionThreshold = QFrame(self.Frame_BasicSettings_Tool_VoiceIdentifier)
        self.Frame_Tool_VoiceIdentifier_DecisionThreshold.setObjectName(u"Frame_Tool_VoiceIdentifier_DecisionThreshold")
        self.Frame_Tool_VoiceIdentifier_DecisionThreshold.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceIdentifier_DecisionThreshold.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_140 = QVBoxLayout(self.Frame_Tool_VoiceIdentifier_DecisionThreshold)
        self.verticalLayout_140.setSpacing(12)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceIdentifier_DecisionThreshold = QLabel(self.Frame_Tool_VoiceIdentifier_DecisionThreshold)
        self.Label_Tool_VoiceIdentifier_DecisionThreshold.setObjectName(u"Label_Tool_VoiceIdentifier_DecisionThreshold")
        self.Label_Tool_VoiceIdentifier_DecisionThreshold.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_140.addWidget(self.Label_Tool_VoiceIdentifier_DecisionThreshold)

        self.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold = QDoubleSpinBox(self.Frame_Tool_VoiceIdentifier_DecisionThreshold)
        self.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setObjectName(u"DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold")
        self.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setEnabled(True)
        self.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold.setMaximum(999999.000000000000000)

        self.verticalLayout_140.addWidget(self.DoubleSpinBox_Tool_VoiceIdentifier_DecisionThreshold)


        self.verticalLayout_137.addWidget(self.Frame_Tool_VoiceIdentifier_DecisionThreshold)

        self.Frame_Tool_VoiceIdentifier_Audio_Dir_Output = QFrame(self.Frame_BasicSettings_Tool_VoiceIdentifier)
        self.Frame_Tool_VoiceIdentifier_Audio_Dir_Output.setObjectName(u"Frame_Tool_VoiceIdentifier_Audio_Dir_Output")
        self.Frame_Tool_VoiceIdentifier_Audio_Dir_Output.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceIdentifier_Audio_Dir_Output.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_141 = QVBoxLayout(self.Frame_Tool_VoiceIdentifier_Audio_Dir_Output)
        self.verticalLayout_141.setSpacing(12)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceIdentifier_Audio_Dir_Output = QLabel(self.Frame_Tool_VoiceIdentifier_Audio_Dir_Output)
        self.Label_Tool_VoiceIdentifier_Audio_Dir_Output.setObjectName(u"Label_Tool_VoiceIdentifier_Audio_Dir_Output")
        self.Label_Tool_VoiceIdentifier_Audio_Dir_Output.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_141.addWidget(self.Label_Tool_VoiceIdentifier_Audio_Dir_Output)

        self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Output = QFrame(self.Frame_Tool_VoiceIdentifier_Audio_Dir_Output)
        self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Output.setObjectName(u"ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Output")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Output.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Output.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Output.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_74 = QHBoxLayout(self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Output)
        self.horizontalLayout_74.setSpacing(12)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output = QLineEdit(self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Output)
        self.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output.setObjectName(u"LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output")
        self.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_74.addWidget(self.LineEdit_Tool_VoiceIdentifier_Audio_Dir_Output)

        self.Button_Tool_VoiceIdentifier_Audio_Dir_Output = QPushButton(self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Output)
        self.Button_Tool_VoiceIdentifier_Audio_Dir_Output.setObjectName(u"Button_Tool_VoiceIdentifier_Audio_Dir_Output")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceIdentifier_Audio_Dir_Output.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceIdentifier_Audio_Dir_Output.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceIdentifier_Audio_Dir_Output.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceIdentifier_Audio_Dir_Output.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_74.addWidget(self.Button_Tool_VoiceIdentifier_Audio_Dir_Output)


        self.verticalLayout_141.addWidget(self.ChildFrame_Tool_VoiceIdentifier_Audio_Dir_Output)


        self.verticalLayout_137.addWidget(self.Frame_Tool_VoiceIdentifier_Audio_Dir_Output)


        self.verticalLayout_33.addWidget(self.Frame_BasicSettings_Tool_VoiceIdentifier)

        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier = QCheckBox(self.GroupBox_EssentialParams_Tool_VoiceIdentifier)
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier.setObjectName(u"CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier")
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_33.addWidget(self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier)

        self.Frame_AdvanceSettings_Tool_VoiceIdentifier = QFrame(self.GroupBox_EssentialParams_Tool_VoiceIdentifier)
        self.Frame_AdvanceSettings_Tool_VoiceIdentifier.setObjectName(u"Frame_AdvanceSettings_Tool_VoiceIdentifier")
        self.verticalLayout_7 = QVBoxLayout(self.Frame_AdvanceSettings_Tool_VoiceIdentifier)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_VoiceIdentifier_Model_Dir = QFrame(self.Frame_AdvanceSettings_Tool_VoiceIdentifier)
        self.Frame_Tool_VoiceIdentifier_Model_Dir.setObjectName(u"Frame_Tool_VoiceIdentifier_Model_Dir")
        self.Frame_Tool_VoiceIdentifier_Model_Dir.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceIdentifier_Model_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_142 = QVBoxLayout(self.Frame_Tool_VoiceIdentifier_Model_Dir)
        self.verticalLayout_142.setSpacing(12)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceIdentifier_Model_Dir = QLabel(self.Frame_Tool_VoiceIdentifier_Model_Dir)
        self.Label_Tool_VoiceIdentifier_Model_Dir.setObjectName(u"Label_Tool_VoiceIdentifier_Model_Dir")
        self.Label_Tool_VoiceIdentifier_Model_Dir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_142.addWidget(self.Label_Tool_VoiceIdentifier_Model_Dir)

        self.ChildFrame_Tool_VoiceIdentifier_Model_Dir = QFrame(self.Frame_Tool_VoiceIdentifier_Model_Dir)
        self.ChildFrame_Tool_VoiceIdentifier_Model_Dir.setObjectName(u"ChildFrame_Tool_VoiceIdentifier_Model_Dir")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceIdentifier_Model_Dir.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceIdentifier_Model_Dir.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceIdentifier_Model_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_75 = QHBoxLayout(self.ChildFrame_Tool_VoiceIdentifier_Model_Dir)
        self.horizontalLayout_75.setSpacing(12)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceIdentifier_Model_Dir = QLineEdit(self.ChildFrame_Tool_VoiceIdentifier_Model_Dir)
        self.LineEdit_Tool_VoiceIdentifier_Model_Dir.setObjectName(u"LineEdit_Tool_VoiceIdentifier_Model_Dir")
        self.LineEdit_Tool_VoiceIdentifier_Model_Dir.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_75.addWidget(self.LineEdit_Tool_VoiceIdentifier_Model_Dir)

        self.Button_Tool_VoiceIdentifier_Model_Dir = QPushButton(self.ChildFrame_Tool_VoiceIdentifier_Model_Dir)
        self.Button_Tool_VoiceIdentifier_Model_Dir.setObjectName(u"Button_Tool_VoiceIdentifier_Model_Dir")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceIdentifier_Model_Dir.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceIdentifier_Model_Dir.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceIdentifier_Model_Dir.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceIdentifier_Model_Dir.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_75.addWidget(self.Button_Tool_VoiceIdentifier_Model_Dir)


        self.verticalLayout_142.addWidget(self.ChildFrame_Tool_VoiceIdentifier_Model_Dir)


        self.verticalLayout_7.addWidget(self.Frame_Tool_VoiceIdentifier_Model_Dir)

        self.Frame_Tool_VoiceIdentifier_Model_Type = QFrame(self.Frame_AdvanceSettings_Tool_VoiceIdentifier)
        self.Frame_Tool_VoiceIdentifier_Model_Type.setObjectName(u"Frame_Tool_VoiceIdentifier_Model_Type")
        self.Frame_Tool_VoiceIdentifier_Model_Type.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceIdentifier_Model_Type.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_143 = QVBoxLayout(self.Frame_Tool_VoiceIdentifier_Model_Type)
        self.verticalLayout_143.setSpacing(12)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceIdentifier_Model_Type = QLabel(self.Frame_Tool_VoiceIdentifier_Model_Type)
        self.Label_Tool_VoiceIdentifier_Model_Type.setObjectName(u"Label_Tool_VoiceIdentifier_Model_Type")
        self.Label_Tool_VoiceIdentifier_Model_Type.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_143.addWidget(self.Label_Tool_VoiceIdentifier_Model_Type)

        self.ComboBox_Tool_VoiceIdentifier_Model_Type = QComboBox(self.Frame_Tool_VoiceIdentifier_Model_Type)
        self.ComboBox_Tool_VoiceIdentifier_Model_Type.setObjectName(u"ComboBox_Tool_VoiceIdentifier_Model_Type")
        self.ComboBox_Tool_VoiceIdentifier_Model_Type.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_143.addWidget(self.ComboBox_Tool_VoiceIdentifier_Model_Type)


        self.verticalLayout_7.addWidget(self.Frame_Tool_VoiceIdentifier_Model_Type)

        self.Frame_Tool_VoiceIdentifier_Model_Name = QFrame(self.Frame_AdvanceSettings_Tool_VoiceIdentifier)
        self.Frame_Tool_VoiceIdentifier_Model_Name.setObjectName(u"Frame_Tool_VoiceIdentifier_Model_Name")
        self.Frame_Tool_VoiceIdentifier_Model_Name.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceIdentifier_Model_Name.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_144 = QVBoxLayout(self.Frame_Tool_VoiceIdentifier_Model_Name)
        self.verticalLayout_144.setSpacing(12)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceIdentifier_Model_Name = QLabel(self.Frame_Tool_VoiceIdentifier_Model_Name)
        self.Label_Tool_VoiceIdentifier_Model_Name.setObjectName(u"Label_Tool_VoiceIdentifier_Model_Name")
        self.Label_Tool_VoiceIdentifier_Model_Name.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_144.addWidget(self.Label_Tool_VoiceIdentifier_Model_Name)

        self.ComboBox_Tool_VoiceIdentifier_Model_Name = QComboBox(self.Frame_Tool_VoiceIdentifier_Model_Name)
        self.ComboBox_Tool_VoiceIdentifier_Model_Name.setObjectName(u"ComboBox_Tool_VoiceIdentifier_Model_Name")
        self.ComboBox_Tool_VoiceIdentifier_Model_Name.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_144.addWidget(self.ComboBox_Tool_VoiceIdentifier_Model_Name)


        self.verticalLayout_7.addWidget(self.Frame_Tool_VoiceIdentifier_Model_Name)

        self.Frame_Tool_VoiceIdentifier_Feature_Method = QFrame(self.Frame_AdvanceSettings_Tool_VoiceIdentifier)
        self.Frame_Tool_VoiceIdentifier_Feature_Method.setObjectName(u"Frame_Tool_VoiceIdentifier_Feature_Method")
        self.Frame_Tool_VoiceIdentifier_Feature_Method.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceIdentifier_Feature_Method.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_145 = QVBoxLayout(self.Frame_Tool_VoiceIdentifier_Feature_Method)
        self.verticalLayout_145.setSpacing(12)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceIdentifier_Feature_Method = QLabel(self.Frame_Tool_VoiceIdentifier_Feature_Method)
        self.Label_Tool_VoiceIdentifier_Feature_Method.setObjectName(u"Label_Tool_VoiceIdentifier_Feature_Method")
        self.Label_Tool_VoiceIdentifier_Feature_Method.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_145.addWidget(self.Label_Tool_VoiceIdentifier_Feature_Method)

        self.ComboBox_Tool_VoiceIdentifier_Feature_Method = QComboBox(self.Frame_Tool_VoiceIdentifier_Feature_Method)
        self.ComboBox_Tool_VoiceIdentifier_Feature_Method.setObjectName(u"ComboBox_Tool_VoiceIdentifier_Feature_Method")
        self.ComboBox_Tool_VoiceIdentifier_Feature_Method.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_145.addWidget(self.ComboBox_Tool_VoiceIdentifier_Feature_Method)


        self.verticalLayout_7.addWidget(self.Frame_Tool_VoiceIdentifier_Feature_Method)

        self.Frame_Tool_VoiceIdentifier_Duration_of_Audio = QFrame(self.Frame_AdvanceSettings_Tool_VoiceIdentifier)
        self.Frame_Tool_VoiceIdentifier_Duration_of_Audio.setObjectName(u"Frame_Tool_VoiceIdentifier_Duration_of_Audio")
        self.Frame_Tool_VoiceIdentifier_Duration_of_Audio.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceIdentifier_Duration_of_Audio.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_146 = QVBoxLayout(self.Frame_Tool_VoiceIdentifier_Duration_of_Audio)
        self.verticalLayout_146.setSpacing(12)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.verticalLayout_146.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceIdentifier_Duration_of_Audio = QLabel(self.Frame_Tool_VoiceIdentifier_Duration_of_Audio)
        self.Label_Tool_VoiceIdentifier_Duration_of_Audio.setObjectName(u"Label_Tool_VoiceIdentifier_Duration_of_Audio")
        self.Label_Tool_VoiceIdentifier_Duration_of_Audio.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_146.addWidget(self.Label_Tool_VoiceIdentifier_Duration_of_Audio)

        self.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio = QDoubleSpinBox(self.Frame_Tool_VoiceIdentifier_Duration_of_Audio)
        self.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setObjectName(u"DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio")
        self.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setEnabled(True)
        self.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio.setMaximum(999999.000000000000000)

        self.verticalLayout_146.addWidget(self.DoubleSpinBox_Tool_VoiceIdentifier_Duration_of_Audio)


        self.verticalLayout_7.addWidget(self.Frame_Tool_VoiceIdentifier_Duration_of_Audio)


        self.verticalLayout_33.addWidget(self.Frame_AdvanceSettings_Tool_VoiceIdentifier)


        self.verticalLayout_28.addWidget(self.GroupBox_EssentialParams_Tool_VoiceIdentifier)

        self.ScrollArea_Middle_Tool_VoiceIdentifier.setWidget(self.ScrollArea_Right_WidgetContents_Tool_VoiceIdentifier)

        self.gridLayout_7.addWidget(self.ScrollArea_Middle_Tool_VoiceIdentifier, 0, 1, 1, 1)

        self.Widget_Right_Tool_VoiceIdentifier = QWidget(self.StackedWidget_Pages_Tool_VoiceIdentifier)
        self.Widget_Right_Tool_VoiceIdentifier.setObjectName(u"Widget_Right_Tool_VoiceIdentifier")
        self.Widget_Right_Tool_VoiceIdentifier.setMaximumSize(QSize(420, 16777215))
        self.Widget_Right_Tool_VoiceIdentifier.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout_14 = QGridLayout(self.Widget_Right_Tool_VoiceIdentifier)
        self.gridLayout_14.setSpacing(12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Tool_VoiceIdentifier = QTextBrowser(self.Widget_Right_Tool_VoiceIdentifier)
        self.TextBrowser_Params_Tool_VoiceIdentifier.setObjectName(u"TextBrowser_Params_Tool_VoiceIdentifier")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Tool_VoiceIdentifier.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Tool_VoiceIdentifier.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Tool_VoiceIdentifier.setStyleSheet(u"QTextBrowser {\n"
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

        self.gridLayout_14.addWidget(self.TextBrowser_Params_Tool_VoiceIdentifier, 0, 0, 1, 2)

        self.Button_SyncParams_Tool_VoiceIdentifier = QPushButton(self.Widget_Right_Tool_VoiceIdentifier)
        self.Button_SyncParams_Tool_VoiceIdentifier.setObjectName(u"Button_SyncParams_Tool_VoiceIdentifier")
        self.Button_SyncParams_Tool_VoiceIdentifier.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_14.addWidget(self.Button_SyncParams_Tool_VoiceIdentifier, 1, 0, 1, 1)

        self.Button_CheckOutput_Tool_VoiceIdentifier = QPushButton(self.Widget_Right_Tool_VoiceIdentifier)
        self.Button_CheckOutput_Tool_VoiceIdentifier.setObjectName(u"Button_CheckOutput_Tool_VoiceIdentifier")
        self.Button_CheckOutput_Tool_VoiceIdentifier.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_14.addWidget(self.Button_CheckOutput_Tool_VoiceIdentifier, 1, 1, 1, 1)


        self.gridLayout_7.addWidget(self.Widget_Right_Tool_VoiceIdentifier, 0, 2, 1, 1)

        self.ProgressBar_Tool_VoiceIdentifier = QProgressBar(self.StackedWidget_Pages_Tool_VoiceIdentifier)
        self.ProgressBar_Tool_VoiceIdentifier.setObjectName(u"ProgressBar_Tool_VoiceIdentifier")
        self.ProgressBar_Tool_VoiceIdentifier.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Tool_VoiceIdentifier.setStyleSheet(u"QProgressBar {\n"
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
        self.ProgressBar_Tool_VoiceIdentifier.setValue(0)
        self.ProgressBar_Tool_VoiceIdentifier.setTextVisible(False)
        self.horizontalLayout_73 = QHBoxLayout(self.ProgressBar_Tool_VoiceIdentifier)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Tool_VoiceIdentifier = QStackedWidget(self.ProgressBar_Tool_VoiceIdentifier)
        self.StackedWidget_Tool_VoiceIdentifier.setObjectName(u"StackedWidget_Tool_VoiceIdentifier")
        self.StackedWidget_Tool_VoiceIdentifier.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_Tool_VoiceIdentifier.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_Tool_VoiceIdentifier_Execute = QWidget()
        self.Page_Tool_VoiceIdentifier_Execute.setObjectName(u"Page_Tool_VoiceIdentifier_Execute")
        self.verticalLayout_102 = QVBoxLayout(self.Page_Tool_VoiceIdentifier_Execute)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_VoiceIdentifier_Execute = QPushButton(self.Page_Tool_VoiceIdentifier_Execute)
        self.Button_Tool_VoiceIdentifier_Execute.setObjectName(u"Button_Tool_VoiceIdentifier_Execute")
        sizePolicy5.setHeightForWidth(self.Button_Tool_VoiceIdentifier_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceIdentifier_Execute.setSizePolicy(sizePolicy5)
        self.Button_Tool_VoiceIdentifier_Execute.setMinimumSize(QSize(0, 30))
        self.Button_Tool_VoiceIdentifier_Execute.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_102.addWidget(self.Button_Tool_VoiceIdentifier_Execute)

        self.StackedWidget_Tool_VoiceIdentifier.addWidget(self.Page_Tool_VoiceIdentifier_Execute)
        self.Page_Tool_VoiceIdentifier_Terminate = QWidget()
        self.Page_Tool_VoiceIdentifier_Terminate.setObjectName(u"Page_Tool_VoiceIdentifier_Terminate")
        self.verticalLayout_119 = QVBoxLayout(self.Page_Tool_VoiceIdentifier_Terminate)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_VoiceIdentifier_Terminate = QPushButton(self.Page_Tool_VoiceIdentifier_Terminate)
        self.Button_Tool_VoiceIdentifier_Terminate.setObjectName(u"Button_Tool_VoiceIdentifier_Terminate")
        sizePolicy5.setHeightForWidth(self.Button_Tool_VoiceIdentifier_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceIdentifier_Terminate.setSizePolicy(sizePolicy5)
        self.Button_Tool_VoiceIdentifier_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_Tool_VoiceIdentifier_Terminate.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_119.addWidget(self.Button_Tool_VoiceIdentifier_Terminate)

        self.StackedWidget_Tool_VoiceIdentifier.addWidget(self.Page_Tool_VoiceIdentifier_Terminate)

        self.horizontalLayout_73.addWidget(self.StackedWidget_Tool_VoiceIdentifier)


        self.gridLayout_7.addWidget(self.ProgressBar_Tool_VoiceIdentifier, 1, 0, 1, 3)

        self.StackedWidget_Pages_Tools.addWidget(self.StackedWidget_Pages_Tool_VoiceIdentifier)
        self.StackedWidget_Pages_Tool_VoiceTranscriber = QWidget()
        self.StackedWidget_Pages_Tool_VoiceTranscriber.setObjectName(u"StackedWidget_Pages_Tool_VoiceTranscriber")
        self.gridLayout_10 = QGridLayout(self.StackedWidget_Pages_Tool_VoiceTranscriber)
        self.gridLayout_10.setSpacing(12)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_Tool_VoiceTranscriber = QWidget(self.StackedWidget_Pages_Tool_VoiceTranscriber)
        self.Widget_Left_Tool_VoiceTranscriber.setObjectName(u"Widget_Left_Tool_VoiceTranscriber")
        self.Widget_Left_Tool_VoiceTranscriber.setMaximumSize(QSize(210, 16777215))
        self.Widget_Left_Tool_VoiceTranscriber.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.Widget_Left_Tool_VoiceTranscriber)
        self.verticalLayout_8.setSpacing(12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Tool_VoiceTranscriber = QTreeWidget(self.Widget_Left_Tool_VoiceTranscriber)
        __qtreewidgetitem2 = QTreeWidgetItem(self.TreeWidget_Catalogue_Tool_VoiceTranscriber)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.TreeWidget_Catalogue_Tool_VoiceTranscriber.setObjectName(u"TreeWidget_Catalogue_Tool_VoiceTranscriber")
        self.TreeWidget_Catalogue_Tool_VoiceTranscriber.setStyleSheet(u"QTreeWidget {\n"
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
"}*/")

        self.verticalLayout_8.addWidget(self.TreeWidget_Catalogue_Tool_VoiceTranscriber)


        self.gridLayout_10.addWidget(self.Widget_Left_Tool_VoiceTranscriber, 0, 0, 1, 1)

        self.ScrollArea_Middle_Tool_VoiceTranscriber = QScrollArea(self.StackedWidget_Pages_Tool_VoiceTranscriber)
        self.ScrollArea_Middle_Tool_VoiceTranscriber.setObjectName(u"ScrollArea_Middle_Tool_VoiceTranscriber")
        self.ScrollArea_Middle_Tool_VoiceTranscriber.setMinimumSize(QSize(630, 0))
        self.ScrollArea_Middle_Tool_VoiceTranscriber.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgb(36, 36, 36);\n"
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
"	height"
                        ": 0px;\n"
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
"	border-widt"
                        "h: 0px;\n"
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
        self.ScrollArea_Middle_Tool_VoiceTranscriber.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Tool_VoiceTranscriber.setWidgetResizable(True)
        self.ScrollArea_Right_WidgetContents_Tool_VoiceTranscriber = QWidget()
        self.ScrollArea_Right_WidgetContents_Tool_VoiceTranscriber.setObjectName(u"ScrollArea_Right_WidgetContents_Tool_VoiceTranscriber")
        self.ScrollArea_Right_WidgetContents_Tool_VoiceTranscriber.setGeometry(QRect(0, 0, 621, 1171))
        self.ScrollArea_Right_WidgetContents_Tool_VoiceTranscriber.setMinimumSize(QSize(0, 0))
        self.verticalLayout_19 = QVBoxLayout(self.ScrollArea_Right_WidgetContents_Tool_VoiceTranscriber)
        self.verticalLayout_19.setSpacing(12)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_Tool_VoiceTranscriber = QGroupBox(self.ScrollArea_Right_WidgetContents_Tool_VoiceTranscriber)
        self.GroupBox_EssentialParams_Tool_VoiceTranscriber.setObjectName(u"GroupBox_EssentialParams_Tool_VoiceTranscriber")
        self.GroupBox_EssentialParams_Tool_VoiceTranscriber.setMaximumSize(QSize(16777215, 16777215))
        self.GroupBox_EssentialParams_Tool_VoiceTranscriber.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_32 = QVBoxLayout(self.GroupBox_EssentialParams_Tool_VoiceTranscriber)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber = QCheckBox(self.GroupBox_EssentialParams_Tool_VoiceTranscriber)
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber.setObjectName(u"CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber")
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_32.addWidget(self.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber)

        self.Frame_BasicSettings_Tool_VoiceTranscriber = QFrame(self.GroupBox_EssentialParams_Tool_VoiceTranscriber)
        self.Frame_BasicSettings_Tool_VoiceTranscriber.setObjectName(u"Frame_BasicSettings_Tool_VoiceTranscriber")
        self.verticalLayout_129 = QVBoxLayout(self.Frame_BasicSettings_Tool_VoiceTranscriber)
        self.verticalLayout_129.setSpacing(0)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_VoiceTranscriber_WAV_Dir = QFrame(self.Frame_BasicSettings_Tool_VoiceTranscriber)
        self.Frame_Tool_VoiceTranscriber_WAV_Dir.setObjectName(u"Frame_Tool_VoiceTranscriber_WAV_Dir")
        self.Frame_Tool_VoiceTranscriber_WAV_Dir.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTranscriber_WAV_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_52 = QVBoxLayout(self.Frame_Tool_VoiceTranscriber_WAV_Dir)
        self.verticalLayout_52.setSpacing(12)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTranscriber_WAV_Dir = QLabel(self.Frame_Tool_VoiceTranscriber_WAV_Dir)
        self.Label_Tool_VoiceTranscriber_WAV_Dir.setObjectName(u"Label_Tool_VoiceTranscriber_WAV_Dir")
        self.Label_Tool_VoiceTranscriber_WAV_Dir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_52.addWidget(self.Label_Tool_VoiceTranscriber_WAV_Dir)

        self.ChildFrame_Tool_VoiceTranscriber_WAV_Dir = QFrame(self.Frame_Tool_VoiceTranscriber_WAV_Dir)
        self.ChildFrame_Tool_VoiceTranscriber_WAV_Dir.setObjectName(u"ChildFrame_Tool_VoiceTranscriber_WAV_Dir")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceTranscriber_WAV_Dir.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceTranscriber_WAV_Dir.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceTranscriber_WAV_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_14 = QHBoxLayout(self.ChildFrame_Tool_VoiceTranscriber_WAV_Dir)
        self.horizontalLayout_14.setSpacing(12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceTranscriber_WAV_Dir = QLineEdit(self.ChildFrame_Tool_VoiceTranscriber_WAV_Dir)
        self.LineEdit_Tool_VoiceTranscriber_WAV_Dir.setObjectName(u"LineEdit_Tool_VoiceTranscriber_WAV_Dir")
        self.LineEdit_Tool_VoiceTranscriber_WAV_Dir.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_14.addWidget(self.LineEdit_Tool_VoiceTranscriber_WAV_Dir)

        self.Button_Tool_VoiceTranscriber_WAV_Dir = QPushButton(self.ChildFrame_Tool_VoiceTranscriber_WAV_Dir)
        self.Button_Tool_VoiceTranscriber_WAV_Dir.setObjectName(u"Button_Tool_VoiceTranscriber_WAV_Dir")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceTranscriber_WAV_Dir.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTranscriber_WAV_Dir.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceTranscriber_WAV_Dir.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceTranscriber_WAV_Dir.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_14.addWidget(self.Button_Tool_VoiceTranscriber_WAV_Dir)


        self.verticalLayout_52.addWidget(self.ChildFrame_Tool_VoiceTranscriber_WAV_Dir)


        self.verticalLayout_129.addWidget(self.Frame_Tool_VoiceTranscriber_WAV_Dir)

        self.Frame_Tool_VoiceTranscriber_SRT_Dir = QFrame(self.Frame_BasicSettings_Tool_VoiceTranscriber)
        self.Frame_Tool_VoiceTranscriber_SRT_Dir.setObjectName(u"Frame_Tool_VoiceTranscriber_SRT_Dir")
        self.Frame_Tool_VoiceTranscriber_SRT_Dir.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTranscriber_SRT_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_58 = QVBoxLayout(self.Frame_Tool_VoiceTranscriber_SRT_Dir)
        self.verticalLayout_58.setSpacing(12)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTranscriber_SRT_Dir = QLabel(self.Frame_Tool_VoiceTranscriber_SRT_Dir)
        self.Label_Tool_VoiceTranscriber_SRT_Dir.setObjectName(u"Label_Tool_VoiceTranscriber_SRT_Dir")
        self.Label_Tool_VoiceTranscriber_SRT_Dir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_58.addWidget(self.Label_Tool_VoiceTranscriber_SRT_Dir)

        self.ChildFrame_Tool_VoiceTranscriber_SRT_Dir = QFrame(self.Frame_Tool_VoiceTranscriber_SRT_Dir)
        self.ChildFrame_Tool_VoiceTranscriber_SRT_Dir.setObjectName(u"ChildFrame_Tool_VoiceTranscriber_SRT_Dir")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceTranscriber_SRT_Dir.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceTranscriber_SRT_Dir.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceTranscriber_SRT_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.ChildFrame_Tool_VoiceTranscriber_SRT_Dir)
        self.horizontalLayout_16.setSpacing(12)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceTranscriber_SRT_Dir = QLineEdit(self.ChildFrame_Tool_VoiceTranscriber_SRT_Dir)
        self.LineEdit_Tool_VoiceTranscriber_SRT_Dir.setObjectName(u"LineEdit_Tool_VoiceTranscriber_SRT_Dir")
        self.LineEdit_Tool_VoiceTranscriber_SRT_Dir.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_16.addWidget(self.LineEdit_Tool_VoiceTranscriber_SRT_Dir)

        self.Button_Tool_VoiceTranscriber_SRT_Dir = QPushButton(self.ChildFrame_Tool_VoiceTranscriber_SRT_Dir)
        self.Button_Tool_VoiceTranscriber_SRT_Dir.setObjectName(u"Button_Tool_VoiceTranscriber_SRT_Dir")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceTranscriber_SRT_Dir.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTranscriber_SRT_Dir.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceTranscriber_SRT_Dir.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceTranscriber_SRT_Dir.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_16.addWidget(self.Button_Tool_VoiceTranscriber_SRT_Dir)


        self.verticalLayout_58.addWidget(self.ChildFrame_Tool_VoiceTranscriber_SRT_Dir)


        self.verticalLayout_129.addWidget(self.Frame_Tool_VoiceTranscriber_SRT_Dir)


        self.verticalLayout_32.addWidget(self.Frame_BasicSettings_Tool_VoiceTranscriber)

        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber = QCheckBox(self.GroupBox_EssentialParams_Tool_VoiceTranscriber)
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber.setObjectName(u"CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber")
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_32.addWidget(self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber)

        self.Frame_AdvanceSettings_Tool_VoiceTranscriber = QFrame(self.GroupBox_EssentialParams_Tool_VoiceTranscriber)
        self.Frame_AdvanceSettings_Tool_VoiceTranscriber.setObjectName(u"Frame_AdvanceSettings_Tool_VoiceTranscriber")
        self.verticalLayout_30 = QVBoxLayout(self.Frame_AdvanceSettings_Tool_VoiceTranscriber)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_VoiceTranscriber_Model_Dir = QFrame(self.Frame_AdvanceSettings_Tool_VoiceTranscriber)
        self.Frame_Tool_VoiceTranscriber_Model_Dir.setObjectName(u"Frame_Tool_VoiceTranscriber_Model_Dir")
        self.Frame_Tool_VoiceTranscriber_Model_Dir.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTranscriber_Model_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_53 = QVBoxLayout(self.Frame_Tool_VoiceTranscriber_Model_Dir)
        self.verticalLayout_53.setSpacing(12)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTranscriber_Model_Dir = QLabel(self.Frame_Tool_VoiceTranscriber_Model_Dir)
        self.Label_Tool_VoiceTranscriber_Model_Dir.setObjectName(u"Label_Tool_VoiceTranscriber_Model_Dir")
        self.Label_Tool_VoiceTranscriber_Model_Dir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_53.addWidget(self.Label_Tool_VoiceTranscriber_Model_Dir)

        self.ChildFrame_Tool_VoiceTranscriber_Model_Dir = QFrame(self.Frame_Tool_VoiceTranscriber_Model_Dir)
        self.ChildFrame_Tool_VoiceTranscriber_Model_Dir.setObjectName(u"ChildFrame_Tool_VoiceTranscriber_Model_Dir")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceTranscriber_Model_Dir.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceTranscriber_Model_Dir.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceTranscriber_Model_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.ChildFrame_Tool_VoiceTranscriber_Model_Dir)
        self.horizontalLayout_15.setSpacing(12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceTranscriber_Model_Dir = QLineEdit(self.ChildFrame_Tool_VoiceTranscriber_Model_Dir)
        self.LineEdit_Tool_VoiceTranscriber_Model_Dir.setObjectName(u"LineEdit_Tool_VoiceTranscriber_Model_Dir")
        self.LineEdit_Tool_VoiceTranscriber_Model_Dir.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_15.addWidget(self.LineEdit_Tool_VoiceTranscriber_Model_Dir)

        self.Button_Tool_VoiceTranscriber_Model_Dir = QPushButton(self.ChildFrame_Tool_VoiceTranscriber_Model_Dir)
        self.Button_Tool_VoiceTranscriber_Model_Dir.setObjectName(u"Button_Tool_VoiceTranscriber_Model_Dir")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceTranscriber_Model_Dir.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTranscriber_Model_Dir.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceTranscriber_Model_Dir.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceTranscriber_Model_Dir.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_15.addWidget(self.Button_Tool_VoiceTranscriber_Model_Dir)


        self.verticalLayout_53.addWidget(self.ChildFrame_Tool_VoiceTranscriber_Model_Dir)


        self.verticalLayout_30.addWidget(self.Frame_Tool_VoiceTranscriber_Model_Dir)

        self.Frame_Tool_VoiceTranscriber_Model_Name = QFrame(self.Frame_AdvanceSettings_Tool_VoiceTranscriber)
        self.Frame_Tool_VoiceTranscriber_Model_Name.setObjectName(u"Frame_Tool_VoiceTranscriber_Model_Name")
        self.Frame_Tool_VoiceTranscriber_Model_Name.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTranscriber_Model_Name.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_54 = QVBoxLayout(self.Frame_Tool_VoiceTranscriber_Model_Name)
        self.verticalLayout_54.setSpacing(12)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTranscriber_Model_Name = QLabel(self.Frame_Tool_VoiceTranscriber_Model_Name)
        self.Label_Tool_VoiceTranscriber_Model_Name.setObjectName(u"Label_Tool_VoiceTranscriber_Model_Name")
        self.Label_Tool_VoiceTranscriber_Model_Name.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_54.addWidget(self.Label_Tool_VoiceTranscriber_Model_Name)

        self.ComboBox_Tool_VoiceTranscriber_Model_Name = QComboBox(self.Frame_Tool_VoiceTranscriber_Model_Name)
        self.ComboBox_Tool_VoiceTranscriber_Model_Name.setObjectName(u"ComboBox_Tool_VoiceTranscriber_Model_Name")
        self.ComboBox_Tool_VoiceTranscriber_Model_Name.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_54.addWidget(self.ComboBox_Tool_VoiceTranscriber_Model_Name)


        self.verticalLayout_30.addWidget(self.Frame_Tool_VoiceTranscriber_Model_Name)

        self.Frame_Tool_VoiceTranscriber_Verbose = QFrame(self.Frame_AdvanceSettings_Tool_VoiceTranscriber)
        self.Frame_Tool_VoiceTranscriber_Verbose.setObjectName(u"Frame_Tool_VoiceTranscriber_Verbose")
        self.Frame_Tool_VoiceTranscriber_Verbose.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTranscriber_Verbose.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_55 = QVBoxLayout(self.Frame_Tool_VoiceTranscriber_Verbose)
        self.verticalLayout_55.setSpacing(12)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTranscriber_Verbose = QLabel(self.Frame_Tool_VoiceTranscriber_Verbose)
        self.Label_Tool_VoiceTranscriber_Verbose.setObjectName(u"Label_Tool_VoiceTranscriber_Verbose")
        self.Label_Tool_VoiceTranscriber_Verbose.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_55.addWidget(self.Label_Tool_VoiceTranscriber_Verbose)

        self.CheckBox_Tool_VoiceTranscriber_Verbose = QCheckBox(self.Frame_Tool_VoiceTranscriber_Verbose)
        self.CheckBox_Tool_VoiceTranscriber_Verbose.setObjectName(u"CheckBox_Tool_VoiceTranscriber_Verbose")
        self.CheckBox_Tool_VoiceTranscriber_Verbose.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_55.addWidget(self.CheckBox_Tool_VoiceTranscriber_Verbose)


        self.verticalLayout_30.addWidget(self.Frame_Tool_VoiceTranscriber_Verbose)

        self.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text = QFrame(self.Frame_AdvanceSettings_Tool_VoiceTranscriber)
        self.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text.setObjectName(u"Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text")
        self.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_56 = QVBoxLayout(self.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text)
        self.verticalLayout_56.setSpacing(12)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTranscriber_Condition_on_Previous_Text = QLabel(self.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text)
        self.Label_Tool_VoiceTranscriber_Condition_on_Previous_Text.setObjectName(u"Label_Tool_VoiceTranscriber_Condition_on_Previous_Text")
        self.Label_Tool_VoiceTranscriber_Condition_on_Previous_Text.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_56.addWidget(self.Label_Tool_VoiceTranscriber_Condition_on_Previous_Text)

        self.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text = QCheckBox(self.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text)
        self.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setObjectName(u"CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text")
        self.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_56.addWidget(self.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text)


        self.verticalLayout_30.addWidget(self.Frame_Tool_VoiceTranscriber_Condition_on_Previous_Text)

        self.Frame_Tool_VoiceTranscriber_fp16 = QFrame(self.Frame_AdvanceSettings_Tool_VoiceTranscriber)
        self.Frame_Tool_VoiceTranscriber_fp16.setObjectName(u"Frame_Tool_VoiceTranscriber_fp16")
        self.Frame_Tool_VoiceTranscriber_fp16.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTranscriber_fp16.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_57 = QVBoxLayout(self.Frame_Tool_VoiceTranscriber_fp16)
        self.verticalLayout_57.setSpacing(12)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTranscriber_fp16 = QLabel(self.Frame_Tool_VoiceTranscriber_fp16)
        self.Label_Tool_VoiceTranscriber_fp16.setObjectName(u"Label_Tool_VoiceTranscriber_fp16")
        self.Label_Tool_VoiceTranscriber_fp16.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_57.addWidget(self.Label_Tool_VoiceTranscriber_fp16)

        self.CheckBox_Tool_VoiceTranscriber_fp16 = QCheckBox(self.Frame_Tool_VoiceTranscriber_fp16)
        self.CheckBox_Tool_VoiceTranscriber_fp16.setObjectName(u"CheckBox_Tool_VoiceTranscriber_fp16")
        self.CheckBox_Tool_VoiceTranscriber_fp16.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_57.addWidget(self.CheckBox_Tool_VoiceTranscriber_fp16)


        self.verticalLayout_30.addWidget(self.Frame_Tool_VoiceTranscriber_fp16)


        self.verticalLayout_32.addWidget(self.Frame_AdvanceSettings_Tool_VoiceTranscriber)


        self.verticalLayout_19.addWidget(self.GroupBox_EssentialParams_Tool_VoiceTranscriber)

        self.GroupBox_OptionalParams_Tool_VoiceTranscriber = QGroupBox(self.ScrollArea_Right_WidgetContents_Tool_VoiceTranscriber)
        self.GroupBox_OptionalParams_Tool_VoiceTranscriber.setObjectName(u"GroupBox_OptionalParams_Tool_VoiceTranscriber")
        self.GroupBox_OptionalParams_Tool_VoiceTranscriber.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_31 = QVBoxLayout(self.GroupBox_OptionalParams_Tool_VoiceTranscriber)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber = QCheckBox(self.GroupBox_OptionalParams_Tool_VoiceTranscriber)
        self.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber.setObjectName(u"CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber")
        self.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_31.addWidget(self.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber)

        self.Frame_BasicOptionalSettings_Tool_VoiceTranscriber = QFrame(self.GroupBox_OptionalParams_Tool_VoiceTranscriber)
        self.Frame_BasicOptionalSettings_Tool_VoiceTranscriber.setObjectName(u"Frame_BasicOptionalSettings_Tool_VoiceTranscriber")
        self.verticalLayout_133 = QVBoxLayout(self.Frame_BasicOptionalSettings_Tool_VoiceTranscriber)
        self.verticalLayout_133.setSpacing(0)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_VoiceTranscriber_Language = QFrame(self.Frame_BasicOptionalSettings_Tool_VoiceTranscriber)
        self.Frame_Tool_VoiceTranscriber_Language.setObjectName(u"Frame_Tool_VoiceTranscriber_Language")
        self.Frame_Tool_VoiceTranscriber_Language.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTranscriber_Language.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_59 = QVBoxLayout(self.Frame_Tool_VoiceTranscriber_Language)
        self.verticalLayout_59.setSpacing(12)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTranscriber_Language = QLabel(self.Frame_Tool_VoiceTranscriber_Language)
        self.Label_Tool_VoiceTranscriber_Language.setObjectName(u"Label_Tool_VoiceTranscriber_Language")
        self.Label_Tool_VoiceTranscriber_Language.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_59.addWidget(self.Label_Tool_VoiceTranscriber_Language)

        self.ComboBox_Tool_VoiceTranscriber_Language = QComboBox(self.Frame_Tool_VoiceTranscriber_Language)
        self.ComboBox_Tool_VoiceTranscriber_Language.setObjectName(u"ComboBox_Tool_VoiceTranscriber_Language")
        self.ComboBox_Tool_VoiceTranscriber_Language.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_59.addWidget(self.ComboBox_Tool_VoiceTranscriber_Language)


        self.verticalLayout_133.addWidget(self.Frame_Tool_VoiceTranscriber_Language)


        self.verticalLayout_31.addWidget(self.Frame_BasicOptionalSettings_Tool_VoiceTranscriber)


        self.verticalLayout_19.addWidget(self.GroupBox_OptionalParams_Tool_VoiceTranscriber)

        self.ScrollArea_Middle_Tool_VoiceTranscriber.setWidget(self.ScrollArea_Right_WidgetContents_Tool_VoiceTranscriber)

        self.gridLayout_10.addWidget(self.ScrollArea_Middle_Tool_VoiceTranscriber, 0, 1, 1, 1)

        self.Widget_Right_Tool_VoiceTranscriber = QWidget(self.StackedWidget_Pages_Tool_VoiceTranscriber)
        self.Widget_Right_Tool_VoiceTranscriber.setObjectName(u"Widget_Right_Tool_VoiceTranscriber")
        self.Widget_Right_Tool_VoiceTranscriber.setMaximumSize(QSize(420, 16777215))
        self.Widget_Right_Tool_VoiceTranscriber.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout_15 = QGridLayout(self.Widget_Right_Tool_VoiceTranscriber)
        self.gridLayout_15.setSpacing(12)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Tool_VoiceTranscriber = QTextBrowser(self.Widget_Right_Tool_VoiceTranscriber)
        self.TextBrowser_Params_Tool_VoiceTranscriber.setObjectName(u"TextBrowser_Params_Tool_VoiceTranscriber")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Tool_VoiceTranscriber.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Tool_VoiceTranscriber.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Tool_VoiceTranscriber.setStyleSheet(u"QTextBrowser {\n"
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

        self.gridLayout_15.addWidget(self.TextBrowser_Params_Tool_VoiceTranscriber, 0, 0, 1, 2)

        self.Button_SyncParams_Tool_VoiceTranscriber = QPushButton(self.Widget_Right_Tool_VoiceTranscriber)
        self.Button_SyncParams_Tool_VoiceTranscriber.setObjectName(u"Button_SyncParams_Tool_VoiceTranscriber")
        self.Button_SyncParams_Tool_VoiceTranscriber.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_15.addWidget(self.Button_SyncParams_Tool_VoiceTranscriber, 1, 0, 1, 1)

        self.Button_CheckOutput_Tool_VoiceTranscriber = QPushButton(self.Widget_Right_Tool_VoiceTranscriber)
        self.Button_CheckOutput_Tool_VoiceTranscriber.setObjectName(u"Button_CheckOutput_Tool_VoiceTranscriber")
        self.Button_CheckOutput_Tool_VoiceTranscriber.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_15.addWidget(self.Button_CheckOutput_Tool_VoiceTranscriber, 1, 1, 1, 1)


        self.gridLayout_10.addWidget(self.Widget_Right_Tool_VoiceTranscriber, 0, 2, 1, 1)

        self.ProgressBar_Tool_VoiceTranscriber = QProgressBar(self.StackedWidget_Pages_Tool_VoiceTranscriber)
        self.ProgressBar_Tool_VoiceTranscriber.setObjectName(u"ProgressBar_Tool_VoiceTranscriber")
        self.ProgressBar_Tool_VoiceTranscriber.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Tool_VoiceTranscriber.setStyleSheet(u"QProgressBar {\n"
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
        self.ProgressBar_Tool_VoiceTranscriber.setValue(0)
        self.ProgressBar_Tool_VoiceTranscriber.setTextVisible(False)
        self.horizontalLayout_35 = QHBoxLayout(self.ProgressBar_Tool_VoiceTranscriber)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Tool_VoiceTranscriber = QStackedWidget(self.ProgressBar_Tool_VoiceTranscriber)
        self.StackedWidget_Tool_VoiceTranscriber.setObjectName(u"StackedWidget_Tool_VoiceTranscriber")
        self.StackedWidget_Tool_VoiceTranscriber.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_Tool_VoiceTranscriber.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_Tool_VoiceTranscriber_Execute = QWidget()
        self.Page_Tool_VoiceTranscriber_Execute.setObjectName(u"Page_Tool_VoiceTranscriber_Execute")
        self.verticalLayout_90 = QVBoxLayout(self.Page_Tool_VoiceTranscriber_Execute)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_VoiceTranscriber_Execute = QPushButton(self.Page_Tool_VoiceTranscriber_Execute)
        self.Button_Tool_VoiceTranscriber_Execute.setObjectName(u"Button_Tool_VoiceTranscriber_Execute")
        sizePolicy5.setHeightForWidth(self.Button_Tool_VoiceTranscriber_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTranscriber_Execute.setSizePolicy(sizePolicy5)
        self.Button_Tool_VoiceTranscriber_Execute.setMinimumSize(QSize(0, 30))
        self.Button_Tool_VoiceTranscriber_Execute.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_90.addWidget(self.Button_Tool_VoiceTranscriber_Execute)

        self.StackedWidget_Tool_VoiceTranscriber.addWidget(self.Page_Tool_VoiceTranscriber_Execute)
        self.Page_Tool_VoiceTranscriber_Terminate = QWidget()
        self.Page_Tool_VoiceTranscriber_Terminate.setObjectName(u"Page_Tool_VoiceTranscriber_Terminate")
        self.verticalLayout_91 = QVBoxLayout(self.Page_Tool_VoiceTranscriber_Terminate)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_VoiceTranscriber_Terminate = QPushButton(self.Page_Tool_VoiceTranscriber_Terminate)
        self.Button_Tool_VoiceTranscriber_Terminate.setObjectName(u"Button_Tool_VoiceTranscriber_Terminate")
        sizePolicy5.setHeightForWidth(self.Button_Tool_VoiceTranscriber_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTranscriber_Terminate.setSizePolicy(sizePolicy5)
        self.Button_Tool_VoiceTranscriber_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_Tool_VoiceTranscriber_Terminate.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_91.addWidget(self.Button_Tool_VoiceTranscriber_Terminate)

        self.StackedWidget_Tool_VoiceTranscriber.addWidget(self.Page_Tool_VoiceTranscriber_Terminate)

        self.horizontalLayout_35.addWidget(self.StackedWidget_Tool_VoiceTranscriber)


        self.gridLayout_10.addWidget(self.ProgressBar_Tool_VoiceTranscriber, 1, 0, 1, 3)

        self.StackedWidget_Pages_Tools.addWidget(self.StackedWidget_Pages_Tool_VoiceTranscriber)
        self.StackedWidget_Pages_Tool_DatasetCreator = QWidget()
        self.StackedWidget_Pages_Tool_DatasetCreator.setObjectName(u"StackedWidget_Pages_Tool_DatasetCreator")
        self.gridLayout_11 = QGridLayout(self.StackedWidget_Pages_Tool_DatasetCreator)
        self.gridLayout_11.setSpacing(12)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_Tool_DatasetCreator = QWidget(self.StackedWidget_Pages_Tool_DatasetCreator)
        self.Widget_Left_Tool_DatasetCreator.setObjectName(u"Widget_Left_Tool_DatasetCreator")
        self.Widget_Left_Tool_DatasetCreator.setMaximumSize(QSize(210, 16777215))
        self.Widget_Left_Tool_DatasetCreator.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.Widget_Left_Tool_DatasetCreator)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Tool_DatasetCreator = QTreeWidget(self.Widget_Left_Tool_DatasetCreator)
        __qtreewidgetitem3 = QTreeWidgetItem(self.TreeWidget_Catalogue_Tool_DatasetCreator)
        QTreeWidgetItem(__qtreewidgetitem3)
        self.TreeWidget_Catalogue_Tool_DatasetCreator.setObjectName(u"TreeWidget_Catalogue_Tool_DatasetCreator")
        self.TreeWidget_Catalogue_Tool_DatasetCreator.setStyleSheet(u"QTreeWidget {\n"
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
"}*/")

        self.verticalLayout_9.addWidget(self.TreeWidget_Catalogue_Tool_DatasetCreator)


        self.gridLayout_11.addWidget(self.Widget_Left_Tool_DatasetCreator, 0, 0, 1, 1)

        self.ScrollArea_Middle_Tool_DatasetCreator = QScrollArea(self.StackedWidget_Pages_Tool_DatasetCreator)
        self.ScrollArea_Middle_Tool_DatasetCreator.setObjectName(u"ScrollArea_Middle_Tool_DatasetCreator")
        self.ScrollArea_Middle_Tool_DatasetCreator.setMinimumSize(QSize(630, 0))
        self.ScrollArea_Middle_Tool_DatasetCreator.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgb(36, 36, 36);\n"
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
"	height"
                        ": 0px;\n"
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
"	border-widt"
                        "h: 0px;\n"
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
        self.ScrollArea_Middle_Tool_DatasetCreator.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Tool_DatasetCreator.setWidgetResizable(True)
        self.ScrollArea_Right_WidgetContents_Tool_DatasetCreator = QWidget()
        self.ScrollArea_Right_WidgetContents_Tool_DatasetCreator.setObjectName(u"ScrollArea_Right_WidgetContents_Tool_DatasetCreator")
        self.ScrollArea_Right_WidgetContents_Tool_DatasetCreator.setGeometry(QRect(0, 0, 621, 1221))
        self.ScrollArea_Right_WidgetContents_Tool_DatasetCreator.setMinimumSize(QSize(0, 0))
        self.verticalLayout_20 = QVBoxLayout(self.ScrollArea_Right_WidgetContents_Tool_DatasetCreator)
        self.verticalLayout_20.setSpacing(12)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_Tool_DatasetCreator = QGroupBox(self.ScrollArea_Right_WidgetContents_Tool_DatasetCreator)
        self.GroupBox_EssentialParams_Tool_DatasetCreator.setObjectName(u"GroupBox_EssentialParams_Tool_DatasetCreator")
        self.GroupBox_EssentialParams_Tool_DatasetCreator.setMaximumSize(QSize(16777215, 16777215))
        self.GroupBox_EssentialParams_Tool_DatasetCreator.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_111 = QVBoxLayout(self.GroupBox_EssentialParams_Tool_DatasetCreator)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator = QCheckBox(self.GroupBox_EssentialParams_Tool_DatasetCreator)
        self.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator.setObjectName(u"CheckBox_Toggle_BasicSettings_Tool_DatasetCreator")
        self.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_111.addWidget(self.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator)

        self.Frame_BasicSettings_Tool_DatasetCreator = QFrame(self.GroupBox_EssentialParams_Tool_DatasetCreator)
        self.Frame_BasicSettings_Tool_DatasetCreator.setObjectName(u"Frame_BasicSettings_Tool_DatasetCreator")
        self.verticalLayout_125 = QVBoxLayout(self.Frame_BasicSettings_Tool_DatasetCreator)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_DatasetCreator_WAV_Dir = QFrame(self.Frame_BasicSettings_Tool_DatasetCreator)
        self.Frame_Tool_DatasetCreator_WAV_Dir.setObjectName(u"Frame_Tool_DatasetCreator_WAV_Dir")
        self.Frame_Tool_DatasetCreator_WAV_Dir.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_DatasetCreator_WAV_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_60 = QVBoxLayout(self.Frame_Tool_DatasetCreator_WAV_Dir)
        self.verticalLayout_60.setSpacing(12)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_DatasetCreator_WAV_Dir = QLabel(self.Frame_Tool_DatasetCreator_WAV_Dir)
        self.Label_Tool_DatasetCreator_WAV_Dir.setObjectName(u"Label_Tool_DatasetCreator_WAV_Dir")
        self.Label_Tool_DatasetCreator_WAV_Dir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_60.addWidget(self.Label_Tool_DatasetCreator_WAV_Dir)

        self.ChildFrame_Tool_DatasetCreator_WAV_Dir = QFrame(self.Frame_Tool_DatasetCreator_WAV_Dir)
        self.ChildFrame_Tool_DatasetCreator_WAV_Dir.setObjectName(u"ChildFrame_Tool_DatasetCreator_WAV_Dir")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_DatasetCreator_WAV_Dir.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_DatasetCreator_WAV_Dir.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_DatasetCreator_WAV_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_17 = QHBoxLayout(self.ChildFrame_Tool_DatasetCreator_WAV_Dir)
        self.horizontalLayout_17.setSpacing(12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_DatasetCreator_WAV_Dir = QLineEdit(self.ChildFrame_Tool_DatasetCreator_WAV_Dir)
        self.LineEdit_Tool_DatasetCreator_WAV_Dir.setObjectName(u"LineEdit_Tool_DatasetCreator_WAV_Dir")
        self.LineEdit_Tool_DatasetCreator_WAV_Dir.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_17.addWidget(self.LineEdit_Tool_DatasetCreator_WAV_Dir)

        self.Button_Tool_DatasetCreator_WAV_Dir = QPushButton(self.ChildFrame_Tool_DatasetCreator_WAV_Dir)
        self.Button_Tool_DatasetCreator_WAV_Dir.setObjectName(u"Button_Tool_DatasetCreator_WAV_Dir")
        sizePolicy1.setHeightForWidth(self.Button_Tool_DatasetCreator_WAV_Dir.sizePolicy().hasHeightForWidth())
        self.Button_Tool_DatasetCreator_WAV_Dir.setSizePolicy(sizePolicy1)
        self.Button_Tool_DatasetCreator_WAV_Dir.setMaximumSize(QSize(24, 24))
        self.Button_Tool_DatasetCreator_WAV_Dir.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_17.addWidget(self.Button_Tool_DatasetCreator_WAV_Dir)


        self.verticalLayout_60.addWidget(self.ChildFrame_Tool_DatasetCreator_WAV_Dir)


        self.verticalLayout_125.addWidget(self.Frame_Tool_DatasetCreator_WAV_Dir)

        self.Frame_Tool_DatasetCreator_SRT_Dir = QFrame(self.Frame_BasicSettings_Tool_DatasetCreator)
        self.Frame_Tool_DatasetCreator_SRT_Dir.setObjectName(u"Frame_Tool_DatasetCreator_SRT_Dir")
        self.Frame_Tool_DatasetCreator_SRT_Dir.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_DatasetCreator_SRT_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_64 = QVBoxLayout(self.Frame_Tool_DatasetCreator_SRT_Dir)
        self.verticalLayout_64.setSpacing(12)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_DatasetCreator_SRT_Dir = QLabel(self.Frame_Tool_DatasetCreator_SRT_Dir)
        self.Label_Tool_DatasetCreator_SRT_Dir.setObjectName(u"Label_Tool_DatasetCreator_SRT_Dir")
        self.Label_Tool_DatasetCreator_SRT_Dir.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_64.addWidget(self.Label_Tool_DatasetCreator_SRT_Dir)

        self.ChildFrame_Tool_DatasetCreator_SRT_Dir = QFrame(self.Frame_Tool_DatasetCreator_SRT_Dir)
        self.ChildFrame_Tool_DatasetCreator_SRT_Dir.setObjectName(u"ChildFrame_Tool_DatasetCreator_SRT_Dir")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_DatasetCreator_SRT_Dir.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_DatasetCreator_SRT_Dir.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_DatasetCreator_SRT_Dir.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_19 = QHBoxLayout(self.ChildFrame_Tool_DatasetCreator_SRT_Dir)
        self.horizontalLayout_19.setSpacing(12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_DatasetCreator_SRT_Dir = QLineEdit(self.ChildFrame_Tool_DatasetCreator_SRT_Dir)
        self.LineEdit_Tool_DatasetCreator_SRT_Dir.setObjectName(u"LineEdit_Tool_DatasetCreator_SRT_Dir")
        self.LineEdit_Tool_DatasetCreator_SRT_Dir.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_19.addWidget(self.LineEdit_Tool_DatasetCreator_SRT_Dir)

        self.Button_Tool_DatasetCreator_SRT_Dir = QPushButton(self.ChildFrame_Tool_DatasetCreator_SRT_Dir)
        self.Button_Tool_DatasetCreator_SRT_Dir.setObjectName(u"Button_Tool_DatasetCreator_SRT_Dir")
        sizePolicy1.setHeightForWidth(self.Button_Tool_DatasetCreator_SRT_Dir.sizePolicy().hasHeightForWidth())
        self.Button_Tool_DatasetCreator_SRT_Dir.setSizePolicy(sizePolicy1)
        self.Button_Tool_DatasetCreator_SRT_Dir.setMaximumSize(QSize(24, 24))
        self.Button_Tool_DatasetCreator_SRT_Dir.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_19.addWidget(self.Button_Tool_DatasetCreator_SRT_Dir)


        self.verticalLayout_64.addWidget(self.ChildFrame_Tool_DatasetCreator_SRT_Dir)


        self.verticalLayout_125.addWidget(self.Frame_Tool_DatasetCreator_SRT_Dir)

        self.Frame_Tool_DatasetCreator_AutoEncoder = QFrame(self.Frame_BasicSettings_Tool_DatasetCreator)
        self.Frame_Tool_DatasetCreator_AutoEncoder.setObjectName(u"Frame_Tool_DatasetCreator_AutoEncoder")
        self.Frame_Tool_DatasetCreator_AutoEncoder.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_DatasetCreator_AutoEncoder.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_68 = QVBoxLayout(self.Frame_Tool_DatasetCreator_AutoEncoder)
        self.verticalLayout_68.setSpacing(12)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_DatasetCreator_AutoEncoder = QLabel(self.Frame_Tool_DatasetCreator_AutoEncoder)
        self.Label_Tool_DatasetCreator_AutoEncoder.setObjectName(u"Label_Tool_DatasetCreator_AutoEncoder")
        self.Label_Tool_DatasetCreator_AutoEncoder.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_68.addWidget(self.Label_Tool_DatasetCreator_AutoEncoder)

        self.ComboBox_Tool_DatasetCreator_AutoEncoder = QComboBox(self.Frame_Tool_DatasetCreator_AutoEncoder)
        self.ComboBox_Tool_DatasetCreator_AutoEncoder.setObjectName(u"ComboBox_Tool_DatasetCreator_AutoEncoder")
        self.ComboBox_Tool_DatasetCreator_AutoEncoder.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_68.addWidget(self.ComboBox_Tool_DatasetCreator_AutoEncoder)


        self.verticalLayout_125.addWidget(self.Frame_Tool_DatasetCreator_AutoEncoder)

        self.Frame_Tool_DatasetCreator_WAV_Dir_Split = QFrame(self.Frame_BasicSettings_Tool_DatasetCreator)
        self.Frame_Tool_DatasetCreator_WAV_Dir_Split.setObjectName(u"Frame_Tool_DatasetCreator_WAV_Dir_Split")
        self.Frame_Tool_DatasetCreator_WAV_Dir_Split.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_DatasetCreator_WAV_Dir_Split.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_63 = QVBoxLayout(self.Frame_Tool_DatasetCreator_WAV_Dir_Split)
        self.verticalLayout_63.setSpacing(12)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_DatasetCreator_WAV_Dir_Split = QLabel(self.Frame_Tool_DatasetCreator_WAV_Dir_Split)
        self.Label_Tool_DatasetCreator_WAV_Dir_Split.setObjectName(u"Label_Tool_DatasetCreator_WAV_Dir_Split")
        self.Label_Tool_DatasetCreator_WAV_Dir_Split.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_63.addWidget(self.Label_Tool_DatasetCreator_WAV_Dir_Split)

        self.ChildFrame_Tool_DatasetCreator_WAV_Dir_Split = QFrame(self.Frame_Tool_DatasetCreator_WAV_Dir_Split)
        self.ChildFrame_Tool_DatasetCreator_WAV_Dir_Split.setObjectName(u"ChildFrame_Tool_DatasetCreator_WAV_Dir_Split")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_DatasetCreator_WAV_Dir_Split.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_DatasetCreator_WAV_Dir_Split.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_DatasetCreator_WAV_Dir_Split.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.ChildFrame_Tool_DatasetCreator_WAV_Dir_Split)
        self.horizontalLayout_18.setSpacing(12)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_DatasetCreator_WAV_Dir_Split = QLineEdit(self.ChildFrame_Tool_DatasetCreator_WAV_Dir_Split)
        self.LineEdit_Tool_DatasetCreator_WAV_Dir_Split.setObjectName(u"LineEdit_Tool_DatasetCreator_WAV_Dir_Split")
        self.LineEdit_Tool_DatasetCreator_WAV_Dir_Split.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_18.addWidget(self.LineEdit_Tool_DatasetCreator_WAV_Dir_Split)

        self.Button_Tool_DatasetCreator_WAV_Dir_Split = QPushButton(self.ChildFrame_Tool_DatasetCreator_WAV_Dir_Split)
        self.Button_Tool_DatasetCreator_WAV_Dir_Split.setObjectName(u"Button_Tool_DatasetCreator_WAV_Dir_Split")
        sizePolicy1.setHeightForWidth(self.Button_Tool_DatasetCreator_WAV_Dir_Split.sizePolicy().hasHeightForWidth())
        self.Button_Tool_DatasetCreator_WAV_Dir_Split.setSizePolicy(sizePolicy1)
        self.Button_Tool_DatasetCreator_WAV_Dir_Split.setMaximumSize(QSize(24, 24))
        self.Button_Tool_DatasetCreator_WAV_Dir_Split.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_18.addWidget(self.Button_Tool_DatasetCreator_WAV_Dir_Split)


        self.verticalLayout_63.addWidget(self.ChildFrame_Tool_DatasetCreator_WAV_Dir_Split)


        self.verticalLayout_125.addWidget(self.Frame_Tool_DatasetCreator_WAV_Dir_Split)

        self.Frame_Tool_DatasetCreator_FileList_Path_Training = QFrame(self.Frame_BasicSettings_Tool_DatasetCreator)
        self.Frame_Tool_DatasetCreator_FileList_Path_Training.setObjectName(u"Frame_Tool_DatasetCreator_FileList_Path_Training")
        self.Frame_Tool_DatasetCreator_FileList_Path_Training.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_DatasetCreator_FileList_Path_Training.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_66 = QVBoxLayout(self.Frame_Tool_DatasetCreator_FileList_Path_Training)
        self.verticalLayout_66.setSpacing(12)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_DatasetCreator_FileList_Path_Training = QLabel(self.Frame_Tool_DatasetCreator_FileList_Path_Training)
        self.Label_Tool_DatasetCreator_FileList_Path_Training.setObjectName(u"Label_Tool_DatasetCreator_FileList_Path_Training")
        self.Label_Tool_DatasetCreator_FileList_Path_Training.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_66.addWidget(self.Label_Tool_DatasetCreator_FileList_Path_Training)

        self.ChildFrame_Tool_DatasetCreator_FileList_Path_Training = QFrame(self.Frame_Tool_DatasetCreator_FileList_Path_Training)
        self.ChildFrame_Tool_DatasetCreator_FileList_Path_Training.setObjectName(u"ChildFrame_Tool_DatasetCreator_FileList_Path_Training")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_DatasetCreator_FileList_Path_Training.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_DatasetCreator_FileList_Path_Training.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_DatasetCreator_FileList_Path_Training.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_20 = QHBoxLayout(self.ChildFrame_Tool_DatasetCreator_FileList_Path_Training)
        self.horizontalLayout_20.setSpacing(12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_DatasetCreator_FileList_Path_Training = QLineEdit(self.ChildFrame_Tool_DatasetCreator_FileList_Path_Training)
        self.LineEdit_Tool_DatasetCreator_FileList_Path_Training.setObjectName(u"LineEdit_Tool_DatasetCreator_FileList_Path_Training")
        self.LineEdit_Tool_DatasetCreator_FileList_Path_Training.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_20.addWidget(self.LineEdit_Tool_DatasetCreator_FileList_Path_Training)

        self.Button_Tool_DatasetCreator_FileList_Path_Training = QPushButton(self.ChildFrame_Tool_DatasetCreator_FileList_Path_Training)
        self.Button_Tool_DatasetCreator_FileList_Path_Training.setObjectName(u"Button_Tool_DatasetCreator_FileList_Path_Training")
        sizePolicy1.setHeightForWidth(self.Button_Tool_DatasetCreator_FileList_Path_Training.sizePolicy().hasHeightForWidth())
        self.Button_Tool_DatasetCreator_FileList_Path_Training.setSizePolicy(sizePolicy1)
        self.Button_Tool_DatasetCreator_FileList_Path_Training.setMaximumSize(QSize(24, 24))
        self.Button_Tool_DatasetCreator_FileList_Path_Training.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_20.addWidget(self.Button_Tool_DatasetCreator_FileList_Path_Training)


        self.verticalLayout_66.addWidget(self.ChildFrame_Tool_DatasetCreator_FileList_Path_Training)


        self.verticalLayout_125.addWidget(self.Frame_Tool_DatasetCreator_FileList_Path_Training)

        self.Frame_Tool_DatasetCreator_FileList_Path_Validation = QFrame(self.Frame_BasicSettings_Tool_DatasetCreator)
        self.Frame_Tool_DatasetCreator_FileList_Path_Validation.setObjectName(u"Frame_Tool_DatasetCreator_FileList_Path_Validation")
        self.Frame_Tool_DatasetCreator_FileList_Path_Validation.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_DatasetCreator_FileList_Path_Validation.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_65 = QVBoxLayout(self.Frame_Tool_DatasetCreator_FileList_Path_Validation)
        self.verticalLayout_65.setSpacing(12)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_DatasetCreator_FileList_Path_Validation = QLabel(self.Frame_Tool_DatasetCreator_FileList_Path_Validation)
        self.Label_Tool_DatasetCreator_FileList_Path_Validation.setObjectName(u"Label_Tool_DatasetCreator_FileList_Path_Validation")
        self.Label_Tool_DatasetCreator_FileList_Path_Validation.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_65.addWidget(self.Label_Tool_DatasetCreator_FileList_Path_Validation)

        self.ChildFrame_Tool_DatasetCreator_FileList_Path_Validation = QFrame(self.Frame_Tool_DatasetCreator_FileList_Path_Validation)
        self.ChildFrame_Tool_DatasetCreator_FileList_Path_Validation.setObjectName(u"ChildFrame_Tool_DatasetCreator_FileList_Path_Validation")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_DatasetCreator_FileList_Path_Validation.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_DatasetCreator_FileList_Path_Validation.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_DatasetCreator_FileList_Path_Validation.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_21 = QHBoxLayout(self.ChildFrame_Tool_DatasetCreator_FileList_Path_Validation)
        self.horizontalLayout_21.setSpacing(12)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_DatasetCreator_FileList_Path_Validation = QLineEdit(self.ChildFrame_Tool_DatasetCreator_FileList_Path_Validation)
        self.LineEdit_Tool_DatasetCreator_FileList_Path_Validation.setObjectName(u"LineEdit_Tool_DatasetCreator_FileList_Path_Validation")
        self.LineEdit_Tool_DatasetCreator_FileList_Path_Validation.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_21.addWidget(self.LineEdit_Tool_DatasetCreator_FileList_Path_Validation)

        self.Button_Tool_DatasetCreator_FileList_Path_Validation = QPushButton(self.ChildFrame_Tool_DatasetCreator_FileList_Path_Validation)
        self.Button_Tool_DatasetCreator_FileList_Path_Validation.setObjectName(u"Button_Tool_DatasetCreator_FileList_Path_Validation")
        sizePolicy1.setHeightForWidth(self.Button_Tool_DatasetCreator_FileList_Path_Validation.sizePolicy().hasHeightForWidth())
        self.Button_Tool_DatasetCreator_FileList_Path_Validation.setSizePolicy(sizePolicy1)
        self.Button_Tool_DatasetCreator_FileList_Path_Validation.setMaximumSize(QSize(24, 24))
        self.Button_Tool_DatasetCreator_FileList_Path_Validation.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_21.addWidget(self.Button_Tool_DatasetCreator_FileList_Path_Validation)


        self.verticalLayout_65.addWidget(self.ChildFrame_Tool_DatasetCreator_FileList_Path_Validation)


        self.verticalLayout_125.addWidget(self.Frame_Tool_DatasetCreator_FileList_Path_Validation)


        self.verticalLayout_111.addWidget(self.Frame_BasicSettings_Tool_DatasetCreator)

        self.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator = QCheckBox(self.GroupBox_EssentialParams_Tool_DatasetCreator)
        self.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator.setObjectName(u"CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator")
        self.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_111.addWidget(self.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator)

        self.Frame_AdvanceSettings_Tool_DatasetCreator = QFrame(self.GroupBox_EssentialParams_Tool_DatasetCreator)
        self.Frame_AdvanceSettings_Tool_DatasetCreator.setObjectName(u"Frame_AdvanceSettings_Tool_DatasetCreator")
        self.Frame_AdvanceSettings_Tool_DatasetCreator.setFrameShape(QFrame.StyledPanel)
        self.Frame_AdvanceSettings_Tool_DatasetCreator.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.Frame_AdvanceSettings_Tool_DatasetCreator)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_DatasetCreator_Sample_Rate = QFrame(self.Frame_AdvanceSettings_Tool_DatasetCreator)
        self.Frame_Tool_DatasetCreator_Sample_Rate.setObjectName(u"Frame_Tool_DatasetCreator_Sample_Rate")
        self.Frame_Tool_DatasetCreator_Sample_Rate.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_DatasetCreator_Sample_Rate.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_61 = QVBoxLayout(self.Frame_Tool_DatasetCreator_Sample_Rate)
        self.verticalLayout_61.setSpacing(12)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_DatasetCreator_Sample_Rate = QLabel(self.Frame_Tool_DatasetCreator_Sample_Rate)
        self.Label_Tool_DatasetCreator_Sample_Rate.setObjectName(u"Label_Tool_DatasetCreator_Sample_Rate")
        self.Label_Tool_DatasetCreator_Sample_Rate.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_61.addWidget(self.Label_Tool_DatasetCreator_Sample_Rate)

        self.SpinBox_Tool_DatasetCreator_Sample_Rate = QSpinBox(self.Frame_Tool_DatasetCreator_Sample_Rate)
        self.SpinBox_Tool_DatasetCreator_Sample_Rate.setObjectName(u"SpinBox_Tool_DatasetCreator_Sample_Rate")
        self.SpinBox_Tool_DatasetCreator_Sample_Rate.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Tool_DatasetCreator_Sample_Rate.setMinimum(-999999)
        self.SpinBox_Tool_DatasetCreator_Sample_Rate.setMaximum(999999)

        self.verticalLayout_61.addWidget(self.SpinBox_Tool_DatasetCreator_Sample_Rate)


        self.verticalLayout_67.addWidget(self.Frame_Tool_DatasetCreator_Sample_Rate)

        self.Frame_Tool_DatasetCreator_Subtype = QFrame(self.Frame_AdvanceSettings_Tool_DatasetCreator)
        self.Frame_Tool_DatasetCreator_Subtype.setObjectName(u"Frame_Tool_DatasetCreator_Subtype")
        self.Frame_Tool_DatasetCreator_Subtype.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_DatasetCreator_Subtype.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_62 = QVBoxLayout(self.Frame_Tool_DatasetCreator_Subtype)
        self.verticalLayout_62.setSpacing(12)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_DatasetCreator_Subtype = QLabel(self.Frame_Tool_DatasetCreator_Subtype)
        self.Label_Tool_DatasetCreator_Subtype.setObjectName(u"Label_Tool_DatasetCreator_Subtype")
        self.Label_Tool_DatasetCreator_Subtype.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_62.addWidget(self.Label_Tool_DatasetCreator_Subtype)

        self.ComboBox_Tool_DatasetCreator_Subtype = QComboBox(self.Frame_Tool_DatasetCreator_Subtype)
        self.ComboBox_Tool_DatasetCreator_Subtype.setObjectName(u"ComboBox_Tool_DatasetCreator_Subtype")
        self.ComboBox_Tool_DatasetCreator_Subtype.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_62.addWidget(self.ComboBox_Tool_DatasetCreator_Subtype)


        self.verticalLayout_67.addWidget(self.Frame_Tool_DatasetCreator_Subtype)

        self.Frame_Tool_DatasetCreator_TrainRatio = QFrame(self.Frame_AdvanceSettings_Tool_DatasetCreator)
        self.Frame_Tool_DatasetCreator_TrainRatio.setObjectName(u"Frame_Tool_DatasetCreator_TrainRatio")
        self.Frame_Tool_DatasetCreator_TrainRatio.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_DatasetCreator_TrainRatio.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_108 = QVBoxLayout(self.Frame_Tool_DatasetCreator_TrainRatio)
        self.verticalLayout_108.setSpacing(12)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_DatasetCreator_TrainRatio = QLabel(self.Frame_Tool_DatasetCreator_TrainRatio)
        self.Label_Tool_DatasetCreator_TrainRatio.setObjectName(u"Label_Tool_DatasetCreator_TrainRatio")
        self.Label_Tool_DatasetCreator_TrainRatio.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_108.addWidget(self.Label_Tool_DatasetCreator_TrainRatio)

        self.DoubleSpinBox_Tool_DatasetCreator_TrainRatio = QDoubleSpinBox(self.Frame_Tool_DatasetCreator_TrainRatio)
        self.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setObjectName(u"DoubleSpinBox_Tool_DatasetCreator_TrainRatio")
        self.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setEnabled(True)
        self.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setStyleSheet(u"QDoubleSpinBox {\n"
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
        self.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setMinimum(-999999.000000000000000)
        self.DoubleSpinBox_Tool_DatasetCreator_TrainRatio.setMaximum(999999.000000000000000)

        self.verticalLayout_108.addWidget(self.DoubleSpinBox_Tool_DatasetCreator_TrainRatio)


        self.verticalLayout_67.addWidget(self.Frame_Tool_DatasetCreator_TrainRatio)


        self.verticalLayout_111.addWidget(self.Frame_AdvanceSettings_Tool_DatasetCreator)


        self.verticalLayout_20.addWidget(self.GroupBox_EssentialParams_Tool_DatasetCreator)

        self.ScrollArea_Middle_Tool_DatasetCreator.setWidget(self.ScrollArea_Right_WidgetContents_Tool_DatasetCreator)

        self.gridLayout_11.addWidget(self.ScrollArea_Middle_Tool_DatasetCreator, 0, 1, 1, 1)

        self.Widget_Right_Tool_DatasetCreator = QWidget(self.StackedWidget_Pages_Tool_DatasetCreator)
        self.Widget_Right_Tool_DatasetCreator.setObjectName(u"Widget_Right_Tool_DatasetCreator")
        self.Widget_Right_Tool_DatasetCreator.setMaximumSize(QSize(420, 16777215))
        self.Widget_Right_Tool_DatasetCreator.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout_16 = QGridLayout(self.Widget_Right_Tool_DatasetCreator)
        self.gridLayout_16.setSpacing(12)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Tool_DatasetCreator = QTextBrowser(self.Widget_Right_Tool_DatasetCreator)
        self.TextBrowser_Params_Tool_DatasetCreator.setObjectName(u"TextBrowser_Params_Tool_DatasetCreator")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Tool_DatasetCreator.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Tool_DatasetCreator.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Tool_DatasetCreator.setStyleSheet(u"QTextBrowser {\n"
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

        self.gridLayout_16.addWidget(self.TextBrowser_Params_Tool_DatasetCreator, 0, 0, 1, 2)

        self.Button_SyncParams_Tool_DatasetCreator = QPushButton(self.Widget_Right_Tool_DatasetCreator)
        self.Button_SyncParams_Tool_DatasetCreator.setObjectName(u"Button_SyncParams_Tool_DatasetCreator")
        self.Button_SyncParams_Tool_DatasetCreator.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_16.addWidget(self.Button_SyncParams_Tool_DatasetCreator, 1, 0, 1, 1)

        self.Button_CheckOutput_Tool_DatasetCreator = QPushButton(self.Widget_Right_Tool_DatasetCreator)
        self.Button_CheckOutput_Tool_DatasetCreator.setObjectName(u"Button_CheckOutput_Tool_DatasetCreator")
        self.Button_CheckOutput_Tool_DatasetCreator.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_16.addWidget(self.Button_CheckOutput_Tool_DatasetCreator, 1, 1, 1, 1)


        self.gridLayout_11.addWidget(self.Widget_Right_Tool_DatasetCreator, 0, 2, 1, 1)

        self.ProgressBar_Tool_DatasetCreator = QProgressBar(self.StackedWidget_Pages_Tool_DatasetCreator)
        self.ProgressBar_Tool_DatasetCreator.setObjectName(u"ProgressBar_Tool_DatasetCreator")
        self.ProgressBar_Tool_DatasetCreator.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Tool_DatasetCreator.setStyleSheet(u"QProgressBar {\n"
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
        self.ProgressBar_Tool_DatasetCreator.setValue(0)
        self.ProgressBar_Tool_DatasetCreator.setTextVisible(False)
        self.horizontalLayout_37 = QHBoxLayout(self.ProgressBar_Tool_DatasetCreator)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Tool_DatasetCreator = QStackedWidget(self.ProgressBar_Tool_DatasetCreator)
        self.StackedWidget_Tool_DatasetCreator.setObjectName(u"StackedWidget_Tool_DatasetCreator")
        self.StackedWidget_Tool_DatasetCreator.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_Tool_DatasetCreator.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_Tool_DatasetCreator_Execute = QWidget()
        self.Page_Tool_DatasetCreator_Execute.setObjectName(u"Page_Tool_DatasetCreator_Execute")
        self.verticalLayout_92 = QVBoxLayout(self.Page_Tool_DatasetCreator_Execute)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_DatasetCreator_Execute = QPushButton(self.Page_Tool_DatasetCreator_Execute)
        self.Button_Tool_DatasetCreator_Execute.setObjectName(u"Button_Tool_DatasetCreator_Execute")
        sizePolicy5.setHeightForWidth(self.Button_Tool_DatasetCreator_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Tool_DatasetCreator_Execute.setSizePolicy(sizePolicy5)
        self.Button_Tool_DatasetCreator_Execute.setMinimumSize(QSize(0, 30))
        self.Button_Tool_DatasetCreator_Execute.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_92.addWidget(self.Button_Tool_DatasetCreator_Execute)

        self.StackedWidget_Tool_DatasetCreator.addWidget(self.Page_Tool_DatasetCreator_Execute)
        self.Page_Tool_DatasetCreator_Terminate = QWidget()
        self.Page_Tool_DatasetCreator_Terminate.setObjectName(u"Page_Tool_DatasetCreator_Terminate")
        self.verticalLayout_93 = QVBoxLayout(self.Page_Tool_DatasetCreator_Terminate)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_DatasetCreator_Terminate = QPushButton(self.Page_Tool_DatasetCreator_Terminate)
        self.Button_Tool_DatasetCreator_Terminate.setObjectName(u"Button_Tool_DatasetCreator_Terminate")
        sizePolicy5.setHeightForWidth(self.Button_Tool_DatasetCreator_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Tool_DatasetCreator_Terminate.setSizePolicy(sizePolicy5)
        self.Button_Tool_DatasetCreator_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_Tool_DatasetCreator_Terminate.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_93.addWidget(self.Button_Tool_DatasetCreator_Terminate)

        self.StackedWidget_Tool_DatasetCreator.addWidget(self.Page_Tool_DatasetCreator_Terminate)

        self.horizontalLayout_37.addWidget(self.StackedWidget_Tool_DatasetCreator)


        self.gridLayout_11.addWidget(self.ProgressBar_Tool_DatasetCreator, 1, 0, 1, 3)

        self.StackedWidget_Pages_Tools.addWidget(self.StackedWidget_Pages_Tool_DatasetCreator)
        self.StackedWidget_Pages_Tool_VoiceTrainer = QWidget()
        self.StackedWidget_Pages_Tool_VoiceTrainer.setObjectName(u"StackedWidget_Pages_Tool_VoiceTrainer")
        self.gridLayout_12 = QGridLayout(self.StackedWidget_Pages_Tool_VoiceTrainer)
        self.gridLayout_12.setSpacing(12)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_Tool_VoiceTrainer = QWidget(self.StackedWidget_Pages_Tool_VoiceTrainer)
        self.Widget_Left_Tool_VoiceTrainer.setObjectName(u"Widget_Left_Tool_VoiceTrainer")
        self.Widget_Left_Tool_VoiceTrainer.setMaximumSize(QSize(210, 16777215))
        self.Widget_Left_Tool_VoiceTrainer.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.Widget_Left_Tool_VoiceTrainer)
        self.verticalLayout_10.setSpacing(12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Tool_VoiceTrainer = QTreeWidget(self.Widget_Left_Tool_VoiceTrainer)
        __qtreewidgetitem4 = QTreeWidgetItem(self.TreeWidget_Catalogue_Tool_VoiceTrainer)
        QTreeWidgetItem(__qtreewidgetitem4)
        self.TreeWidget_Catalogue_Tool_VoiceTrainer.setObjectName(u"TreeWidget_Catalogue_Tool_VoiceTrainer")
        self.TreeWidget_Catalogue_Tool_VoiceTrainer.setStyleSheet(u"QTreeWidget {\n"
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
"}*/")

        self.verticalLayout_10.addWidget(self.TreeWidget_Catalogue_Tool_VoiceTrainer)


        self.gridLayout_12.addWidget(self.Widget_Left_Tool_VoiceTrainer, 0, 0, 1, 1)

        self.ScrollArea_Middle_Tool_VoiceTrainer = QScrollArea(self.StackedWidget_Pages_Tool_VoiceTrainer)
        self.ScrollArea_Middle_Tool_VoiceTrainer.setObjectName(u"ScrollArea_Middle_Tool_VoiceTrainer")
        self.ScrollArea_Middle_Tool_VoiceTrainer.setMinimumSize(QSize(630, 0))
        self.ScrollArea_Middle_Tool_VoiceTrainer.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgb(36, 36, 36);\n"
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
"	height"
                        ": 0px;\n"
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
"	border-widt"
                        "h: 0px;\n"
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
        self.ScrollArea_Middle_Tool_VoiceTrainer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Tool_VoiceTrainer.setWidgetResizable(True)
        self.ScrollArea_Right_WidgetContents_Tool_VoiceTrainer = QWidget()
        self.ScrollArea_Right_WidgetContents_Tool_VoiceTrainer.setObjectName(u"ScrollArea_Right_WidgetContents_Tool_VoiceTrainer")
        self.ScrollArea_Right_WidgetContents_Tool_VoiceTrainer.setGeometry(QRect(0, 0, 621, 2061))
        self.ScrollArea_Right_WidgetContents_Tool_VoiceTrainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_22 = QVBoxLayout(self.ScrollArea_Right_WidgetContents_Tool_VoiceTrainer)
        self.verticalLayout_22.setSpacing(12)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_Tool_VoiceTrainer = QGroupBox(self.ScrollArea_Right_WidgetContents_Tool_VoiceTrainer)
        self.GroupBox_EssentialParams_Tool_VoiceTrainer.setObjectName(u"GroupBox_EssentialParams_Tool_VoiceTrainer")
        self.GroupBox_EssentialParams_Tool_VoiceTrainer.setMinimumSize(QSize(0, 0))
        self.GroupBox_EssentialParams_Tool_VoiceTrainer.setMaximumSize(QSize(16777215, 16777215))
        self.GroupBox_EssentialParams_Tool_VoiceTrainer.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_114 = QVBoxLayout(self.GroupBox_EssentialParams_Tool_VoiceTrainer)
        self.verticalLayout_114.setSpacing(0)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer = QCheckBox(self.GroupBox_EssentialParams_Tool_VoiceTrainer)
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer.setObjectName(u"CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer")
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_114.addWidget(self.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer)

        self.Frame_BasicSettings_Tool_VoiceTrainer = QFrame(self.GroupBox_EssentialParams_Tool_VoiceTrainer)
        self.Frame_BasicSettings_Tool_VoiceTrainer.setObjectName(u"Frame_BasicSettings_Tool_VoiceTrainer")
        self.verticalLayout_130 = QVBoxLayout(self.Frame_BasicSettings_Tool_VoiceTrainer)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_VoiceTrainer_FileList_Path_Training = QFrame(self.Frame_BasicSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_FileList_Path_Training.setObjectName(u"Frame_Tool_VoiceTrainer_FileList_Path_Training")
        self.Frame_Tool_VoiceTrainer_FileList_Path_Training.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_FileList_Path_Training.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_69 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_FileList_Path_Training)
        self.verticalLayout_69.setSpacing(12)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_FileList_Path_Training = QLabel(self.Frame_Tool_VoiceTrainer_FileList_Path_Training)
        self.Label_Tool_VoiceTrainer_FileList_Path_Training.setObjectName(u"Label_Tool_VoiceTrainer_FileList_Path_Training")
        self.Label_Tool_VoiceTrainer_FileList_Path_Training.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_69.addWidget(self.Label_Tool_VoiceTrainer_FileList_Path_Training)

        self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Training = QFrame(self.Frame_Tool_VoiceTrainer_FileList_Path_Training)
        self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Training.setObjectName(u"ChildFrame_Tool_VoiceTrainer_FileList_Path_Training")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Training.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Training.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Training.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_22 = QHBoxLayout(self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Training)
        self.horizontalLayout_22.setSpacing(12)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceTrainer_FileList_Path_Training = QLineEdit(self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Training)
        self.LineEdit_Tool_VoiceTrainer_FileList_Path_Training.setObjectName(u"LineEdit_Tool_VoiceTrainer_FileList_Path_Training")
        self.LineEdit_Tool_VoiceTrainer_FileList_Path_Training.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_22.addWidget(self.LineEdit_Tool_VoiceTrainer_FileList_Path_Training)

        self.Button_Tool_VoiceTrainer_FileList_Path_Training = QPushButton(self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Training)
        self.Button_Tool_VoiceTrainer_FileList_Path_Training.setObjectName(u"Button_Tool_VoiceTrainer_FileList_Path_Training")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceTrainer_FileList_Path_Training.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTrainer_FileList_Path_Training.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceTrainer_FileList_Path_Training.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceTrainer_FileList_Path_Training.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_22.addWidget(self.Button_Tool_VoiceTrainer_FileList_Path_Training)


        self.verticalLayout_69.addWidget(self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Training)


        self.verticalLayout_130.addWidget(self.Frame_Tool_VoiceTrainer_FileList_Path_Training)

        self.Frame_Tool_VoiceTrainer_FileList_Path_Validation = QFrame(self.Frame_BasicSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_FileList_Path_Validation.setObjectName(u"Frame_Tool_VoiceTrainer_FileList_Path_Validation")
        self.Frame_Tool_VoiceTrainer_FileList_Path_Validation.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_FileList_Path_Validation.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_70 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_FileList_Path_Validation)
        self.verticalLayout_70.setSpacing(12)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_FileList_Path_Validation = QLabel(self.Frame_Tool_VoiceTrainer_FileList_Path_Validation)
        self.Label_Tool_VoiceTrainer_FileList_Path_Validation.setObjectName(u"Label_Tool_VoiceTrainer_FileList_Path_Validation")
        self.Label_Tool_VoiceTrainer_FileList_Path_Validation.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_70.addWidget(self.Label_Tool_VoiceTrainer_FileList_Path_Validation)

        self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Validation = QFrame(self.Frame_Tool_VoiceTrainer_FileList_Path_Validation)
        self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Validation.setObjectName(u"ChildFrame_Tool_VoiceTrainer_FileList_Path_Validation")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Validation.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Validation.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Validation.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_23 = QHBoxLayout(self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Validation)
        self.horizontalLayout_23.setSpacing(12)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation = QLineEdit(self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Validation)
        self.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation.setObjectName(u"LineEdit_Tool_VoiceTrainer_FileList_Path_Validation")
        self.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_23.addWidget(self.LineEdit_Tool_VoiceTrainer_FileList_Path_Validation)

        self.Button_Tool_VoiceTrainer_FileList_Path_Validation = QPushButton(self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Validation)
        self.Button_Tool_VoiceTrainer_FileList_Path_Validation.setObjectName(u"Button_Tool_VoiceTrainer_FileList_Path_Validation")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceTrainer_FileList_Path_Validation.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTrainer_FileList_Path_Validation.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceTrainer_FileList_Path_Validation.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceTrainer_FileList_Path_Validation.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_23.addWidget(self.Button_Tool_VoiceTrainer_FileList_Path_Validation)


        self.verticalLayout_70.addWidget(self.ChildFrame_Tool_VoiceTrainer_FileList_Path_Validation)


        self.verticalLayout_130.addWidget(self.Frame_Tool_VoiceTrainer_FileList_Path_Validation)

        self.Frame_Tool_VoiceTrainer_Language = QFrame(self.Frame_BasicSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Language.setObjectName(u"Frame_Tool_VoiceTrainer_Language")
        self.Frame_Tool_VoiceTrainer_Language.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Language.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_71 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Language)
        self.verticalLayout_71.setSpacing(12)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Language = QLabel(self.Frame_Tool_VoiceTrainer_Language)
        self.Label_Tool_VoiceTrainer_Language.setObjectName(u"Label_Tool_VoiceTrainer_Language")
        self.Label_Tool_VoiceTrainer_Language.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_71.addWidget(self.Label_Tool_VoiceTrainer_Language)

        self.ComboBox_Tool_VoiceTrainer_Language = QComboBox(self.Frame_Tool_VoiceTrainer_Language)
        self.ComboBox_Tool_VoiceTrainer_Language.setObjectName(u"ComboBox_Tool_VoiceTrainer_Language")
        self.ComboBox_Tool_VoiceTrainer_Language.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_71.addWidget(self.ComboBox_Tool_VoiceTrainer_Language)


        self.verticalLayout_130.addWidget(self.Frame_Tool_VoiceTrainer_Language)

        self.Frame_Tool_VoiceTrainer_Epochs = QFrame(self.Frame_BasicSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Epochs.setObjectName(u"Frame_Tool_VoiceTrainer_Epochs")
        self.Frame_Tool_VoiceTrainer_Epochs.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Epochs.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_73 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Epochs)
        self.verticalLayout_73.setSpacing(2)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Epochs = QLabel(self.Frame_Tool_VoiceTrainer_Epochs)
        self.Label_Tool_VoiceTrainer_Epochs.setObjectName(u"Label_Tool_VoiceTrainer_Epochs")
        self.Label_Tool_VoiceTrainer_Epochs.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_73.addWidget(self.Label_Tool_VoiceTrainer_Epochs)

        self.SpinBox_Tool_VoiceTrainer_Epochs = QSpinBox(self.Frame_Tool_VoiceTrainer_Epochs)
        self.SpinBox_Tool_VoiceTrainer_Epochs.setObjectName(u"SpinBox_Tool_VoiceTrainer_Epochs")
        self.SpinBox_Tool_VoiceTrainer_Epochs.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Tool_VoiceTrainer_Epochs.setMinimum(-999999)
        self.SpinBox_Tool_VoiceTrainer_Epochs.setMaximum(999999)

        self.verticalLayout_73.addWidget(self.SpinBox_Tool_VoiceTrainer_Epochs)


        self.verticalLayout_130.addWidget(self.Frame_Tool_VoiceTrainer_Epochs)

        self.Frame_Tool_VoiceTrainer_Batch_Size = QFrame(self.Frame_BasicSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Batch_Size.setObjectName(u"Frame_Tool_VoiceTrainer_Batch_Size")
        self.Frame_Tool_VoiceTrainer_Batch_Size.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Batch_Size.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_74 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Batch_Size)
        self.verticalLayout_74.setSpacing(12)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Batch_Size = QLabel(self.Frame_Tool_VoiceTrainer_Batch_Size)
        self.Label_Tool_VoiceTrainer_Batch_Size.setObjectName(u"Label_Tool_VoiceTrainer_Batch_Size")
        self.Label_Tool_VoiceTrainer_Batch_Size.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_74.addWidget(self.Label_Tool_VoiceTrainer_Batch_Size)

        self.SpinBox_Tool_VoiceTrainer_Batch_Size = QSpinBox(self.Frame_Tool_VoiceTrainer_Batch_Size)
        self.SpinBox_Tool_VoiceTrainer_Batch_Size.setObjectName(u"SpinBox_Tool_VoiceTrainer_Batch_Size")
        self.SpinBox_Tool_VoiceTrainer_Batch_Size.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Tool_VoiceTrainer_Batch_Size.setMinimum(-999999)
        self.SpinBox_Tool_VoiceTrainer_Batch_Size.setMaximum(999999)

        self.verticalLayout_74.addWidget(self.SpinBox_Tool_VoiceTrainer_Batch_Size)


        self.verticalLayout_130.addWidget(self.Frame_Tool_VoiceTrainer_Batch_Size)

        self.Frame_Tool_VoiceTrainer_Config_Dir_Save = QFrame(self.Frame_BasicSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Config_Dir_Save.setObjectName(u"Frame_Tool_VoiceTrainer_Config_Dir_Save")
        self.Frame_Tool_VoiceTrainer_Config_Dir_Save.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Config_Dir_Save.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_80 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Config_Dir_Save)
        self.verticalLayout_80.setSpacing(12)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Config_Dir_Save = QLabel(self.Frame_Tool_VoiceTrainer_Config_Dir_Save)
        self.Label_Tool_VoiceTrainer_Config_Dir_Save.setObjectName(u"Label_Tool_VoiceTrainer_Config_Dir_Save")
        self.Label_Tool_VoiceTrainer_Config_Dir_Save.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_80.addWidget(self.Label_Tool_VoiceTrainer_Config_Dir_Save)

        self.ChildFrame_Tool_VoiceTrainer_Config_Dir_Save = QFrame(self.Frame_Tool_VoiceTrainer_Config_Dir_Save)
        self.ChildFrame_Tool_VoiceTrainer_Config_Dir_Save.setObjectName(u"ChildFrame_Tool_VoiceTrainer_Config_Dir_Save")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceTrainer_Config_Dir_Save.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceTrainer_Config_Dir_Save.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceTrainer_Config_Dir_Save.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_24 = QHBoxLayout(self.ChildFrame_Tool_VoiceTrainer_Config_Dir_Save)
        self.horizontalLayout_24.setSpacing(12)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceTrainer_Config_Dir_Save = QLineEdit(self.ChildFrame_Tool_VoiceTrainer_Config_Dir_Save)
        self.LineEdit_Tool_VoiceTrainer_Config_Dir_Save.setObjectName(u"LineEdit_Tool_VoiceTrainer_Config_Dir_Save")
        self.LineEdit_Tool_VoiceTrainer_Config_Dir_Save.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_24.addWidget(self.LineEdit_Tool_VoiceTrainer_Config_Dir_Save)

        self.Button_Tool_VoiceTrainer_Config_Dir_Save = QPushButton(self.ChildFrame_Tool_VoiceTrainer_Config_Dir_Save)
        self.Button_Tool_VoiceTrainer_Config_Dir_Save.setObjectName(u"Button_Tool_VoiceTrainer_Config_Dir_Save")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceTrainer_Config_Dir_Save.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTrainer_Config_Dir_Save.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceTrainer_Config_Dir_Save.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceTrainer_Config_Dir_Save.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_24.addWidget(self.Button_Tool_VoiceTrainer_Config_Dir_Save)


        self.verticalLayout_80.addWidget(self.ChildFrame_Tool_VoiceTrainer_Config_Dir_Save)


        self.verticalLayout_130.addWidget(self.Frame_Tool_VoiceTrainer_Config_Dir_Save)

        self.Frame_Tool_VoiceTrainer_Model_Dir_Save = QFrame(self.Frame_BasicSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Model_Dir_Save.setObjectName(u"Frame_Tool_VoiceTrainer_Model_Dir_Save")
        self.Frame_Tool_VoiceTrainer_Model_Dir_Save.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Model_Dir_Save.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_82 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Model_Dir_Save)
        self.verticalLayout_82.setSpacing(12)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Model_Dir_Save = QLabel(self.Frame_Tool_VoiceTrainer_Model_Dir_Save)
        self.Label_Tool_VoiceTrainer_Model_Dir_Save.setObjectName(u"Label_Tool_VoiceTrainer_Model_Dir_Save")
        self.Label_Tool_VoiceTrainer_Model_Dir_Save.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_82.addWidget(self.Label_Tool_VoiceTrainer_Model_Dir_Save)

        self.ChildFrame_Tool_VoiceTrainer_Model_Dir_Save = QFrame(self.Frame_Tool_VoiceTrainer_Model_Dir_Save)
        self.ChildFrame_Tool_VoiceTrainer_Model_Dir_Save.setObjectName(u"ChildFrame_Tool_VoiceTrainer_Model_Dir_Save")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceTrainer_Model_Dir_Save.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceTrainer_Model_Dir_Save.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceTrainer_Model_Dir_Save.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_25 = QHBoxLayout(self.ChildFrame_Tool_VoiceTrainer_Model_Dir_Save)
        self.horizontalLayout_25.setSpacing(12)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceTrainer_Model_Dir_Save = QLineEdit(self.ChildFrame_Tool_VoiceTrainer_Model_Dir_Save)
        self.LineEdit_Tool_VoiceTrainer_Model_Dir_Save.setObjectName(u"LineEdit_Tool_VoiceTrainer_Model_Dir_Save")
        self.LineEdit_Tool_VoiceTrainer_Model_Dir_Save.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_25.addWidget(self.LineEdit_Tool_VoiceTrainer_Model_Dir_Save)

        self.Button_Tool_VoiceTrainer_Model_Dir_Save = QPushButton(self.ChildFrame_Tool_VoiceTrainer_Model_Dir_Save)
        self.Button_Tool_VoiceTrainer_Model_Dir_Save.setObjectName(u"Button_Tool_VoiceTrainer_Model_Dir_Save")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceTrainer_Model_Dir_Save.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTrainer_Model_Dir_Save.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceTrainer_Model_Dir_Save.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceTrainer_Model_Dir_Save.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_25.addWidget(self.Button_Tool_VoiceTrainer_Model_Dir_Save)


        self.verticalLayout_82.addWidget(self.ChildFrame_Tool_VoiceTrainer_Model_Dir_Save)


        self.verticalLayout_130.addWidget(self.Frame_Tool_VoiceTrainer_Model_Dir_Save)


        self.verticalLayout_114.addWidget(self.Frame_BasicSettings_Tool_VoiceTrainer)

        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer = QCheckBox(self.GroupBox_EssentialParams_Tool_VoiceTrainer)
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer.setObjectName(u"CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer")
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_114.addWidget(self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer)

        self.Frame_AdvanceSettings_Tool_VoiceTrainer = QFrame(self.GroupBox_EssentialParams_Tool_VoiceTrainer)
        self.Frame_AdvanceSettings_Tool_VoiceTrainer.setObjectName(u"Frame_AdvanceSettings_Tool_VoiceTrainer")
        self.Frame_AdvanceSettings_Tool_VoiceTrainer.setFrameShape(QFrame.StyledPanel)
        self.Frame_AdvanceSettings_Tool_VoiceTrainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.Frame_AdvanceSettings_Tool_VoiceTrainer)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_VoiceTrainer_Eval_Interval = QFrame(self.Frame_AdvanceSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Eval_Interval.setObjectName(u"Frame_Tool_VoiceTrainer_Eval_Interval")
        self.Frame_Tool_VoiceTrainer_Eval_Interval.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Eval_Interval.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_72 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Eval_Interval)
        self.verticalLayout_72.setSpacing(12)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Eval_Interval = QLabel(self.Frame_Tool_VoiceTrainer_Eval_Interval)
        self.Label_Tool_VoiceTrainer_Eval_Interval.setObjectName(u"Label_Tool_VoiceTrainer_Eval_Interval")
        self.Label_Tool_VoiceTrainer_Eval_Interval.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_72.addWidget(self.Label_Tool_VoiceTrainer_Eval_Interval)

        self.SpinBox_Tool_VoiceTrainer_Eval_Interval = QSpinBox(self.Frame_Tool_VoiceTrainer_Eval_Interval)
        self.SpinBox_Tool_VoiceTrainer_Eval_Interval.setObjectName(u"SpinBox_Tool_VoiceTrainer_Eval_Interval")
        self.SpinBox_Tool_VoiceTrainer_Eval_Interval.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Tool_VoiceTrainer_Eval_Interval.setMinimum(-999999)
        self.SpinBox_Tool_VoiceTrainer_Eval_Interval.setMaximum(999999)

        self.verticalLayout_72.addWidget(self.SpinBox_Tool_VoiceTrainer_Eval_Interval)


        self.verticalLayout_115.addWidget(self.Frame_Tool_VoiceTrainer_Eval_Interval)

        self.Frame_Tool_VoiceTrainer_Num_Workers = QFrame(self.Frame_AdvanceSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Num_Workers.setObjectName(u"Frame_Tool_VoiceTrainer_Num_Workers")
        self.Frame_Tool_VoiceTrainer_Num_Workers.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Num_Workers.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_75 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Num_Workers)
        self.verticalLayout_75.setSpacing(12)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Num_Workers = QLabel(self.Frame_Tool_VoiceTrainer_Num_Workers)
        self.Label_Tool_VoiceTrainer_Num_Workers.setObjectName(u"Label_Tool_VoiceTrainer_Num_Workers")
        self.Label_Tool_VoiceTrainer_Num_Workers.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_75.addWidget(self.Label_Tool_VoiceTrainer_Num_Workers)

        self.SpinBox_Tool_VoiceTrainer_Num_Workers = QSpinBox(self.Frame_Tool_VoiceTrainer_Num_Workers)
        self.SpinBox_Tool_VoiceTrainer_Num_Workers.setObjectName(u"SpinBox_Tool_VoiceTrainer_Num_Workers")
        self.SpinBox_Tool_VoiceTrainer_Num_Workers.setStyleSheet(u"QSpinBox {\n"
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
        self.SpinBox_Tool_VoiceTrainer_Num_Workers.setMinimum(-999999)
        self.SpinBox_Tool_VoiceTrainer_Num_Workers.setMaximum(999999)

        self.verticalLayout_75.addWidget(self.SpinBox_Tool_VoiceTrainer_Num_Workers)


        self.verticalLayout_115.addWidget(self.Frame_Tool_VoiceTrainer_Num_Workers)

        self.Frame_Tool_VoiceTrainer_FP16_Run = QFrame(self.Frame_AdvanceSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_FP16_Run.setObjectName(u"Frame_Tool_VoiceTrainer_FP16_Run")
        self.Frame_Tool_VoiceTrainer_FP16_Run.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_FP16_Run.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_76 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_FP16_Run)
        self.verticalLayout_76.setSpacing(12)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_FP16_Run = QLabel(self.Frame_Tool_VoiceTrainer_FP16_Run)
        self.Label_Tool_VoiceTrainer_FP16_Run.setObjectName(u"Label_Tool_VoiceTrainer_FP16_Run")
        self.Label_Tool_VoiceTrainer_FP16_Run.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_76.addWidget(self.Label_Tool_VoiceTrainer_FP16_Run)

        self.CheckBox_Tool_VoiceTrainer_FP16_Run = QCheckBox(self.Frame_Tool_VoiceTrainer_FP16_Run)
        self.CheckBox_Tool_VoiceTrainer_FP16_Run.setObjectName(u"CheckBox_Tool_VoiceTrainer_FP16_Run")
        self.CheckBox_Tool_VoiceTrainer_FP16_Run.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_76.addWidget(self.CheckBox_Tool_VoiceTrainer_FP16_Run)


        self.verticalLayout_115.addWidget(self.Frame_Tool_VoiceTrainer_FP16_Run)

        self.Frame_Tool_VoiceTrainer_Find_Unused_Parameters = QFrame(self.Frame_AdvanceSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Find_Unused_Parameters.setObjectName(u"Frame_Tool_VoiceTrainer_Find_Unused_Parameters")
        self.Frame_Tool_VoiceTrainer_Find_Unused_Parameters.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Find_Unused_Parameters.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_110 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Find_Unused_Parameters)
        self.verticalLayout_110.setSpacing(12)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Find_Unused_Parameters = QLabel(self.Frame_Tool_VoiceTrainer_Find_Unused_Parameters)
        self.Label_Tool_VoiceTrainer_Find_Unused_Parameters.setObjectName(u"Label_Tool_VoiceTrainer_Find_Unused_Parameters")
        self.Label_Tool_VoiceTrainer_Find_Unused_Parameters.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_110.addWidget(self.Label_Tool_VoiceTrainer_Find_Unused_Parameters)

        self.CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters = QCheckBox(self.Frame_Tool_VoiceTrainer_Find_Unused_Parameters)
        self.CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters.setObjectName(u"CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters")
        self.CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_110.addWidget(self.CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters)


        self.verticalLayout_115.addWidget(self.Frame_Tool_VoiceTrainer_Find_Unused_Parameters)


        self.verticalLayout_114.addWidget(self.Frame_AdvanceSettings_Tool_VoiceTrainer)


        self.verticalLayout_22.addWidget(self.GroupBox_EssentialParams_Tool_VoiceTrainer)

        self.GroupBox_OptionalParams_Tool_VoiceTrainer = QGroupBox(self.ScrollArea_Right_WidgetContents_Tool_VoiceTrainer)
        self.GroupBox_OptionalParams_Tool_VoiceTrainer.setObjectName(u"GroupBox_OptionalParams_Tool_VoiceTrainer")
        self.GroupBox_OptionalParams_Tool_VoiceTrainer.setMinimumSize(QSize(0, 0))
        self.GroupBox_OptionalParams_Tool_VoiceTrainer.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_34 = QVBoxLayout(self.GroupBox_OptionalParams_Tool_VoiceTrainer)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer = QCheckBox(self.GroupBox_OptionalParams_Tool_VoiceTrainer)
        self.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer.setObjectName(u"CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer")
        self.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_34.addWidget(self.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer)

        self.Frame_BasicOptionalSettings_Tool_VoiceTrainer = QFrame(self.GroupBox_OptionalParams_Tool_VoiceTrainer)
        self.Frame_BasicOptionalSettings_Tool_VoiceTrainer.setObjectName(u"Frame_BasicOptionalSettings_Tool_VoiceTrainer")
        self.verticalLayout_132 = QVBoxLayout(self.Frame_BasicOptionalSettings_Tool_VoiceTrainer)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G = QFrame(self.Frame_BasicOptionalSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G.setObjectName(u"Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G")
        self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_84 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G)
        self.verticalLayout_84.setSpacing(12)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Model_Path_Pretrained_G = QLabel(self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G)
        self.Label_Tool_VoiceTrainer_Model_Path_Pretrained_G.setObjectName(u"Label_Tool_VoiceTrainer_Model_Path_Pretrained_G")
        self.Label_Tool_VoiceTrainer_Model_Path_Pretrained_G.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_84.addWidget(self.Label_Tool_VoiceTrainer_Model_Path_Pretrained_G)

        self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_G = QFrame(self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G)
        self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_G.setObjectName(u"ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_G")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_G.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_G.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_G.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_27 = QHBoxLayout(self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_G)
        self.horizontalLayout_27.setSpacing(12)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G = QLineEdit(self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_G)
        self.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G.setObjectName(u"LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G")
        self.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_27.addWidget(self.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_G)

        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G = QPushButton(self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_G)
        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G.setObjectName(u"Button_Tool_VoiceTrainer_Model_Path_Pretrained_G")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_27.addWidget(self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G)


        self.verticalLayout_84.addWidget(self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_G)


        self.verticalLayout_132.addWidget(self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_G)

        self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D = QFrame(self.Frame_BasicOptionalSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D.setObjectName(u"Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D")
        self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_85 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D)
        self.verticalLayout_85.setSpacing(12)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Model_Path_Pretrained_D = QLabel(self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D)
        self.Label_Tool_VoiceTrainer_Model_Path_Pretrained_D.setObjectName(u"Label_Tool_VoiceTrainer_Model_Path_Pretrained_D")
        self.Label_Tool_VoiceTrainer_Model_Path_Pretrained_D.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_85.addWidget(self.Label_Tool_VoiceTrainer_Model_Path_Pretrained_D)

        self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_D = QFrame(self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D)
        self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_D.setObjectName(u"ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_D")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_D.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_D.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_D.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_28 = QHBoxLayout(self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_D)
        self.horizontalLayout_28.setSpacing(12)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D = QLineEdit(self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_D)
        self.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D.setObjectName(u"LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D")
        self.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_28.addWidget(self.LineEdit_Tool_VoiceTrainer_Model_Path_Pretrained_D)

        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D = QPushButton(self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_D)
        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D.setObjectName(u"Button_Tool_VoiceTrainer_Model_Path_Pretrained_D")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_28.addWidget(self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D)


        self.verticalLayout_85.addWidget(self.ChildFrame_Tool_VoiceTrainer_Model_Path_Pretrained_D)


        self.verticalLayout_132.addWidget(self.Frame_Tool_VoiceTrainer_Model_Path_Pretrained_D)


        self.verticalLayout_34.addWidget(self.Frame_BasicOptionalSettings_Tool_VoiceTrainer)

        self.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer = QCheckBox(self.GroupBox_OptionalParams_Tool_VoiceTrainer)
        self.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer.setObjectName(u"CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer")
        self.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_34.addWidget(self.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer)

        self.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer = QFrame(self.GroupBox_OptionalParams_Tool_VoiceTrainer)
        self.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer.setObjectName(u"Frame_AdvanceOptionalSettings_Tool_VoiceTrainer")
        self.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer.setFrameShape(QFrame.StyledPanel)
        self.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer)
        self.verticalLayout_116.setSpacing(0)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_VoiceTrainer_Config_Path_Load = QFrame(self.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Config_Path_Load.setObjectName(u"Frame_Tool_VoiceTrainer_Config_Path_Load")
        self.Frame_Tool_VoiceTrainer_Config_Path_Load.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Config_Path_Load.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_83 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Config_Path_Load)
        self.verticalLayout_83.setSpacing(12)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Config_Path_Load = QLabel(self.Frame_Tool_VoiceTrainer_Config_Path_Load)
        self.Label_Tool_VoiceTrainer_Config_Path_Load.setObjectName(u"Label_Tool_VoiceTrainer_Config_Path_Load")
        self.Label_Tool_VoiceTrainer_Config_Path_Load.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_83.addWidget(self.Label_Tool_VoiceTrainer_Config_Path_Load)

        self.ChildFrame_Tool_VoiceTrainer_Config_Path_Load = QFrame(self.Frame_Tool_VoiceTrainer_Config_Path_Load)
        self.ChildFrame_Tool_VoiceTrainer_Config_Path_Load.setObjectName(u"ChildFrame_Tool_VoiceTrainer_Config_Path_Load")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceTrainer_Config_Path_Load.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceTrainer_Config_Path_Load.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceTrainer_Config_Path_Load.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_26 = QHBoxLayout(self.ChildFrame_Tool_VoiceTrainer_Config_Path_Load)
        self.horizontalLayout_26.setSpacing(12)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceTrainer_Config_Path_Load = QLineEdit(self.ChildFrame_Tool_VoiceTrainer_Config_Path_Load)
        self.LineEdit_Tool_VoiceTrainer_Config_Path_Load.setObjectName(u"LineEdit_Tool_VoiceTrainer_Config_Path_Load")
        self.LineEdit_Tool_VoiceTrainer_Config_Path_Load.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_26.addWidget(self.LineEdit_Tool_VoiceTrainer_Config_Path_Load)

        self.Button_Tool_VoiceTrainer_Config_Path_Load = QPushButton(self.ChildFrame_Tool_VoiceTrainer_Config_Path_Load)
        self.Button_Tool_VoiceTrainer_Config_Path_Load.setObjectName(u"Button_Tool_VoiceTrainer_Config_Path_Load")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceTrainer_Config_Path_Load.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTrainer_Config_Path_Load.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceTrainer_Config_Path_Load.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceTrainer_Config_Path_Load.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_26.addWidget(self.Button_Tool_VoiceTrainer_Config_Path_Load)


        self.verticalLayout_83.addWidget(self.ChildFrame_Tool_VoiceTrainer_Config_Path_Load)


        self.verticalLayout_116.addWidget(self.Frame_Tool_VoiceTrainer_Config_Path_Load)

        self.Frame_Tool_VoiceTrainer_Speakers = QFrame(self.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer)
        self.Frame_Tool_VoiceTrainer_Speakers.setObjectName(u"Frame_Tool_VoiceTrainer_Speakers")
        self.Frame_Tool_VoiceTrainer_Speakers.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceTrainer_Speakers.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_79 = QVBoxLayout(self.Frame_Tool_VoiceTrainer_Speakers)
        self.verticalLayout_79.setSpacing(12)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceTrainer_Speakers = QLabel(self.Frame_Tool_VoiceTrainer_Speakers)
        self.Label_Tool_VoiceTrainer_Speakers.setObjectName(u"Label_Tool_VoiceTrainer_Speakers")
        self.Label_Tool_VoiceTrainer_Speakers.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_79.addWidget(self.Label_Tool_VoiceTrainer_Speakers)

        self.LineEdit_Tool_VoiceTrainer_Speakers = QLineEdit(self.Frame_Tool_VoiceTrainer_Speakers)
        self.LineEdit_Tool_VoiceTrainer_Speakers.setObjectName(u"LineEdit_Tool_VoiceTrainer_Speakers")
        self.LineEdit_Tool_VoiceTrainer_Speakers.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_79.addWidget(self.LineEdit_Tool_VoiceTrainer_Speakers)


        self.verticalLayout_116.addWidget(self.Frame_Tool_VoiceTrainer_Speakers)


        self.verticalLayout_34.addWidget(self.Frame_AdvanceOptionalSettings_Tool_VoiceTrainer)


        self.verticalLayout_22.addWidget(self.GroupBox_OptionalParams_Tool_VoiceTrainer)

        self.ScrollArea_Middle_Tool_VoiceTrainer.setWidget(self.ScrollArea_Right_WidgetContents_Tool_VoiceTrainer)

        self.gridLayout_12.addWidget(self.ScrollArea_Middle_Tool_VoiceTrainer, 0, 1, 1, 1)

        self.Widget_Right_Tool_VoiceTrainer = QWidget(self.StackedWidget_Pages_Tool_VoiceTrainer)
        self.Widget_Right_Tool_VoiceTrainer.setObjectName(u"Widget_Right_Tool_VoiceTrainer")
        self.Widget_Right_Tool_VoiceTrainer.setMaximumSize(QSize(420, 16777215))
        self.Widget_Right_Tool_VoiceTrainer.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout_17 = QGridLayout(self.Widget_Right_Tool_VoiceTrainer)
        self.gridLayout_17.setSpacing(12)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Tool_VoiceTrainer = QTextBrowser(self.Widget_Right_Tool_VoiceTrainer)
        self.TextBrowser_Params_Tool_VoiceTrainer.setObjectName(u"TextBrowser_Params_Tool_VoiceTrainer")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Tool_VoiceTrainer.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Tool_VoiceTrainer.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Tool_VoiceTrainer.setStyleSheet(u"QTextBrowser {\n"
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

        self.gridLayout_17.addWidget(self.TextBrowser_Params_Tool_VoiceTrainer, 0, 0, 1, 2)

        self.Button_SyncParams_Tool_VoiceTrainer = QPushButton(self.Widget_Right_Tool_VoiceTrainer)
        self.Button_SyncParams_Tool_VoiceTrainer.setObjectName(u"Button_SyncParams_Tool_VoiceTrainer")
        self.Button_SyncParams_Tool_VoiceTrainer.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_17.addWidget(self.Button_SyncParams_Tool_VoiceTrainer, 1, 0, 1, 1)

        self.Button_CheckOutput_Tool_VoiceTrainer = QPushButton(self.Widget_Right_Tool_VoiceTrainer)
        self.Button_CheckOutput_Tool_VoiceTrainer.setObjectName(u"Button_CheckOutput_Tool_VoiceTrainer")
        self.Button_CheckOutput_Tool_VoiceTrainer.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_17.addWidget(self.Button_CheckOutput_Tool_VoiceTrainer, 1, 1, 1, 1)


        self.gridLayout_12.addWidget(self.Widget_Right_Tool_VoiceTrainer, 0, 2, 1, 1)

        self.ProgressBar_Tool_VoiceTrainer = QProgressBar(self.StackedWidget_Pages_Tool_VoiceTrainer)
        self.ProgressBar_Tool_VoiceTrainer.setObjectName(u"ProgressBar_Tool_VoiceTrainer")
        self.ProgressBar_Tool_VoiceTrainer.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Tool_VoiceTrainer.setStyleSheet(u"QProgressBar {\n"
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
        self.ProgressBar_Tool_VoiceTrainer.setValue(0)
        self.ProgressBar_Tool_VoiceTrainer.setTextVisible(False)
        self.horizontalLayout_39 = QHBoxLayout(self.ProgressBar_Tool_VoiceTrainer)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Tool_VoiceTrainer = QStackedWidget(self.ProgressBar_Tool_VoiceTrainer)
        self.StackedWidget_Tool_VoiceTrainer.setObjectName(u"StackedWidget_Tool_VoiceTrainer")
        self.StackedWidget_Tool_VoiceTrainer.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_Tool_VoiceTrainer.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_Tool_VoiceTrainer_Execute = QWidget()
        self.Page_Tool_VoiceTrainer_Execute.setObjectName(u"Page_Tool_VoiceTrainer_Execute")
        self.verticalLayout_94 = QVBoxLayout(self.Page_Tool_VoiceTrainer_Execute)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_VoiceTrainer_Execute = QPushButton(self.Page_Tool_VoiceTrainer_Execute)
        self.Button_Tool_VoiceTrainer_Execute.setObjectName(u"Button_Tool_VoiceTrainer_Execute")
        sizePolicy5.setHeightForWidth(self.Button_Tool_VoiceTrainer_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTrainer_Execute.setSizePolicy(sizePolicy5)
        self.Button_Tool_VoiceTrainer_Execute.setMinimumSize(QSize(0, 30))
        self.Button_Tool_VoiceTrainer_Execute.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_94.addWidget(self.Button_Tool_VoiceTrainer_Execute)

        self.StackedWidget_Tool_VoiceTrainer.addWidget(self.Page_Tool_VoiceTrainer_Execute)
        self.Page_Tool_VoiceTrainer_Terminate = QWidget()
        self.Page_Tool_VoiceTrainer_Terminate.setObjectName(u"Page_Tool_VoiceTrainer_Terminate")
        self.verticalLayout_95 = QVBoxLayout(self.Page_Tool_VoiceTrainer_Terminate)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_VoiceTrainer_Terminate = QPushButton(self.Page_Tool_VoiceTrainer_Terminate)
        self.Button_Tool_VoiceTrainer_Terminate.setObjectName(u"Button_Tool_VoiceTrainer_Terminate")
        sizePolicy5.setHeightForWidth(self.Button_Tool_VoiceTrainer_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceTrainer_Terminate.setSizePolicy(sizePolicy5)
        self.Button_Tool_VoiceTrainer_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_Tool_VoiceTrainer_Terminate.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_95.addWidget(self.Button_Tool_VoiceTrainer_Terminate)

        self.StackedWidget_Tool_VoiceTrainer.addWidget(self.Page_Tool_VoiceTrainer_Terminate)

        self.horizontalLayout_39.addWidget(self.StackedWidget_Tool_VoiceTrainer)


        self.gridLayout_12.addWidget(self.ProgressBar_Tool_VoiceTrainer, 1, 0, 1, 3)

        self.StackedWidget_Pages_Tools.addWidget(self.StackedWidget_Pages_Tool_VoiceTrainer)
        self.StackedWidget_Pages_Tool_VoiceConverter = QWidget()
        self.StackedWidget_Pages_Tool_VoiceConverter.setObjectName(u"StackedWidget_Pages_Tool_VoiceConverter")
        self.gridLayout_13 = QGridLayout(self.StackedWidget_Pages_Tool_VoiceConverter)
        self.gridLayout_13.setSpacing(12)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Widget_Left_Tool_VoiceConverter = QWidget(self.StackedWidget_Pages_Tool_VoiceConverter)
        self.Widget_Left_Tool_VoiceConverter.setObjectName(u"Widget_Left_Tool_VoiceConverter")
        self.Widget_Left_Tool_VoiceConverter.setMaximumSize(QSize(210, 16777215))
        self.Widget_Left_Tool_VoiceConverter.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.Widget_Left_Tool_VoiceConverter)
        self.verticalLayout_11.setSpacing(12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(12, 12, 12, 12)
        self.TreeWidget_Catalogue_Tool_VoiceConverter = QTreeWidget(self.Widget_Left_Tool_VoiceConverter)
        __qtreewidgetitem5 = QTreeWidgetItem(self.TreeWidget_Catalogue_Tool_VoiceConverter)
        QTreeWidgetItem(__qtreewidgetitem5)
        self.TreeWidget_Catalogue_Tool_VoiceConverter.setObjectName(u"TreeWidget_Catalogue_Tool_VoiceConverter")
        self.TreeWidget_Catalogue_Tool_VoiceConverter.setStyleSheet(u"QTreeWidget {\n"
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
"}*/")

        self.verticalLayout_11.addWidget(self.TreeWidget_Catalogue_Tool_VoiceConverter)


        self.gridLayout_13.addWidget(self.Widget_Left_Tool_VoiceConverter, 0, 0, 1, 1)

        self.ScrollArea_Middle_Tool_VoiceConverter = QScrollArea(self.StackedWidget_Pages_Tool_VoiceConverter)
        self.ScrollArea_Middle_Tool_VoiceConverter.setObjectName(u"ScrollArea_Middle_Tool_VoiceConverter")
        self.ScrollArea_Middle_Tool_VoiceConverter.setMinimumSize(QSize(630, 0))
        self.ScrollArea_Middle_Tool_VoiceConverter.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgb(36, 36, 36);\n"
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
"	height"
                        ": 0px;\n"
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
"	border-widt"
                        "h: 0px;\n"
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
        self.ScrollArea_Middle_Tool_VoiceConverter.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollArea_Middle_Tool_VoiceConverter.setWidgetResizable(True)
        self.ScrollArea_Right_WidgetContents_Tool_VoiceConverter = QWidget()
        self.ScrollArea_Right_WidgetContents_Tool_VoiceConverter.setObjectName(u"ScrollArea_Right_WidgetContents_Tool_VoiceConverter")
        self.ScrollArea_Right_WidgetContents_Tool_VoiceConverter.setGeometry(QRect(0, 0, 621, 1320))
        self.ScrollArea_Right_WidgetContents_Tool_VoiceConverter.setMinimumSize(QSize(0, 0))
        self.verticalLayout_26 = QVBoxLayout(self.ScrollArea_Right_WidgetContents_Tool_VoiceConverter)
        self.verticalLayout_26.setSpacing(12)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(12, 12, 12, 12)
        self.GroupBox_EssentialParams_Tool_VoiceConverter = QGroupBox(self.ScrollArea_Right_WidgetContents_Tool_VoiceConverter)
        self.GroupBox_EssentialParams_Tool_VoiceConverter.setObjectName(u"GroupBox_EssentialParams_Tool_VoiceConverter")
        self.GroupBox_EssentialParams_Tool_VoiceConverter.setMinimumSize(QSize(0, 0))
        self.GroupBox_EssentialParams_Tool_VoiceConverter.setMaximumSize(QSize(16777215, 16777215))
        self.GroupBox_EssentialParams_Tool_VoiceConverter.setStyleSheet(u"QGroupBox {\n"
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
        self.verticalLayout_117 = QVBoxLayout(self.GroupBox_EssentialParams_Tool_VoiceConverter)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 12, 0, 12)
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter = QCheckBox(self.GroupBox_EssentialParams_Tool_VoiceConverter)
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter.setObjectName(u"CheckBox_Toggle_BasicSettings_Tool_VoiceConverter")
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_117.addWidget(self.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter)

        self.Frame_BasicSettings_Tool_VoiceConverter = QFrame(self.GroupBox_EssentialParams_Tool_VoiceConverter)
        self.Frame_BasicSettings_Tool_VoiceConverter.setObjectName(u"Frame_BasicSettings_Tool_VoiceConverter")
        self.verticalLayout_131 = QVBoxLayout(self.Frame_BasicSettings_Tool_VoiceConverter)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_VoiceConverter_Config_Path_Load = QFrame(self.Frame_BasicSettings_Tool_VoiceConverter)
        self.Frame_Tool_VoiceConverter_Config_Path_Load.setObjectName(u"Frame_Tool_VoiceConverter_Config_Path_Load")
        self.Frame_Tool_VoiceConverter_Config_Path_Load.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceConverter_Config_Path_Load.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_78 = QVBoxLayout(self.Frame_Tool_VoiceConverter_Config_Path_Load)
        self.verticalLayout_78.setSpacing(12)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceConverter_Config_Path_Load = QLabel(self.Frame_Tool_VoiceConverter_Config_Path_Load)
        self.Label_Tool_VoiceConverter_Config_Path_Load.setObjectName(u"Label_Tool_VoiceConverter_Config_Path_Load")
        self.Label_Tool_VoiceConverter_Config_Path_Load.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_78.addWidget(self.Label_Tool_VoiceConverter_Config_Path_Load)

        self.ChildFrame_Tool_VoiceConverter_Config_Path_Load = QFrame(self.Frame_Tool_VoiceConverter_Config_Path_Load)
        self.ChildFrame_Tool_VoiceConverter_Config_Path_Load.setObjectName(u"ChildFrame_Tool_VoiceConverter_Config_Path_Load")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceConverter_Config_Path_Load.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceConverter_Config_Path_Load.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceConverter_Config_Path_Load.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_41 = QHBoxLayout(self.ChildFrame_Tool_VoiceConverter_Config_Path_Load)
        self.horizontalLayout_41.setSpacing(12)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceConverter_Config_Path_Load = QLineEdit(self.ChildFrame_Tool_VoiceConverter_Config_Path_Load)
        self.LineEdit_Tool_VoiceConverter_Config_Path_Load.setObjectName(u"LineEdit_Tool_VoiceConverter_Config_Path_Load")
        self.LineEdit_Tool_VoiceConverter_Config_Path_Load.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_41.addWidget(self.LineEdit_Tool_VoiceConverter_Config_Path_Load)

        self.Button_Tool_VoiceConverter_Config_Path_Load = QPushButton(self.ChildFrame_Tool_VoiceConverter_Config_Path_Load)
        self.Button_Tool_VoiceConverter_Config_Path_Load.setObjectName(u"Button_Tool_VoiceConverter_Config_Path_Load")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceConverter_Config_Path_Load.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceConverter_Config_Path_Load.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceConverter_Config_Path_Load.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceConverter_Config_Path_Load.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_41.addWidget(self.Button_Tool_VoiceConverter_Config_Path_Load)


        self.verticalLayout_78.addWidget(self.ChildFrame_Tool_VoiceConverter_Config_Path_Load)


        self.verticalLayout_131.addWidget(self.Frame_Tool_VoiceConverter_Config_Path_Load)

        self.Frame_Tool_VoiceConverter_Model_Path_Load = QFrame(self.Frame_BasicSettings_Tool_VoiceConverter)
        self.Frame_Tool_VoiceConverter_Model_Path_Load.setObjectName(u"Frame_Tool_VoiceConverter_Model_Path_Load")
        self.Frame_Tool_VoiceConverter_Model_Path_Load.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceConverter_Model_Path_Load.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_96 = QVBoxLayout(self.Frame_Tool_VoiceConverter_Model_Path_Load)
        self.verticalLayout_96.setSpacing(12)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceConverter_Model_Path_Load = QLabel(self.Frame_Tool_VoiceConverter_Model_Path_Load)
        self.Label_Tool_VoiceConverter_Model_Path_Load.setObjectName(u"Label_Tool_VoiceConverter_Model_Path_Load")
        self.Label_Tool_VoiceConverter_Model_Path_Load.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_96.addWidget(self.Label_Tool_VoiceConverter_Model_Path_Load)

        self.ChildFrame_Tool_VoiceConverter_Model_Path_Load = QFrame(self.Frame_Tool_VoiceConverter_Model_Path_Load)
        self.ChildFrame_Tool_VoiceConverter_Model_Path_Load.setObjectName(u"ChildFrame_Tool_VoiceConverter_Model_Path_Load")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceConverter_Model_Path_Load.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceConverter_Model_Path_Load.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceConverter_Model_Path_Load.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_42 = QHBoxLayout(self.ChildFrame_Tool_VoiceConverter_Model_Path_Load)
        self.horizontalLayout_42.setSpacing(12)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceConverter_Model_Path_Load = QLineEdit(self.ChildFrame_Tool_VoiceConverter_Model_Path_Load)
        self.LineEdit_Tool_VoiceConverter_Model_Path_Load.setObjectName(u"LineEdit_Tool_VoiceConverter_Model_Path_Load")
        self.LineEdit_Tool_VoiceConverter_Model_Path_Load.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_42.addWidget(self.LineEdit_Tool_VoiceConverter_Model_Path_Load)

        self.Button_Tool_VoiceConverter_Model_Path_Load = QPushButton(self.ChildFrame_Tool_VoiceConverter_Model_Path_Load)
        self.Button_Tool_VoiceConverter_Model_Path_Load.setObjectName(u"Button_Tool_VoiceConverter_Model_Path_Load")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceConverter_Model_Path_Load.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceConverter_Model_Path_Load.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceConverter_Model_Path_Load.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceConverter_Model_Path_Load.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_42.addWidget(self.Button_Tool_VoiceConverter_Model_Path_Load)


        self.verticalLayout_96.addWidget(self.ChildFrame_Tool_VoiceConverter_Model_Path_Load)


        self.verticalLayout_131.addWidget(self.Frame_Tool_VoiceConverter_Model_Path_Load)

        self.Frame_Tool_VoiceConverter_Text = QFrame(self.Frame_BasicSettings_Tool_VoiceConverter)
        self.Frame_Tool_VoiceConverter_Text.setObjectName(u"Frame_Tool_VoiceConverter_Text")
        self.Frame_Tool_VoiceConverter_Text.setMinimumSize(QSize(0, 222))
        self.Frame_Tool_VoiceConverter_Text.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_98 = QVBoxLayout(self.Frame_Tool_VoiceConverter_Text)
        self.verticalLayout_98.setSpacing(12)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceConverter_Text = QLabel(self.Frame_Tool_VoiceConverter_Text)
        self.Label_Tool_VoiceConverter_Text.setObjectName(u"Label_Tool_VoiceConverter_Text")
        self.Label_Tool_VoiceConverter_Text.setMinimumSize(QSize(0, 60))
        self.Label_Tool_VoiceConverter_Text.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_98.addWidget(self.Label_Tool_VoiceConverter_Text)

        self.PlainTextEdit_Tool_VoiceConverter_Text = QPlainTextEdit(self.Frame_Tool_VoiceConverter_Text)
        self.PlainTextEdit_Tool_VoiceConverter_Text.setObjectName(u"PlainTextEdit_Tool_VoiceConverter_Text")
        self.PlainTextEdit_Tool_VoiceConverter_Text.setStyleSheet(u"QPlainTextEdit {\n"
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

        self.verticalLayout_98.addWidget(self.PlainTextEdit_Tool_VoiceConverter_Text)


        self.verticalLayout_131.addWidget(self.Frame_Tool_VoiceConverter_Text)

        self.Frame_Tool_VoiceConverter_Language = QFrame(self.Frame_BasicSettings_Tool_VoiceConverter)
        self.Frame_Tool_VoiceConverter_Language.setObjectName(u"Frame_Tool_VoiceConverter_Language")
        self.Frame_Tool_VoiceConverter_Language.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceConverter_Language.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_97 = QVBoxLayout(self.Frame_Tool_VoiceConverter_Language)
        self.verticalLayout_97.setSpacing(12)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceConverter_Language = QLabel(self.Frame_Tool_VoiceConverter_Language)
        self.Label_Tool_VoiceConverter_Language.setObjectName(u"Label_Tool_VoiceConverter_Language")
        self.Label_Tool_VoiceConverter_Language.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_97.addWidget(self.Label_Tool_VoiceConverter_Language)

        self.ComboBox_Tool_VoiceConverter_Language = QComboBox(self.Frame_Tool_VoiceConverter_Language)
        self.ComboBox_Tool_VoiceConverter_Language.setObjectName(u"ComboBox_Tool_VoiceConverter_Language")
        self.ComboBox_Tool_VoiceConverter_Language.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_97.addWidget(self.ComboBox_Tool_VoiceConverter_Language)


        self.verticalLayout_131.addWidget(self.Frame_Tool_VoiceConverter_Language)

        self.Frame_Tool_VoiceConverter_Speaker = QFrame(self.Frame_BasicSettings_Tool_VoiceConverter)
        self.Frame_Tool_VoiceConverter_Speaker.setObjectName(u"Frame_Tool_VoiceConverter_Speaker")
        self.Frame_Tool_VoiceConverter_Speaker.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceConverter_Speaker.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_104 = QVBoxLayout(self.Frame_Tool_VoiceConverter_Speaker)
        self.verticalLayout_104.setSpacing(12)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceConverter_Speaker = QLabel(self.Frame_Tool_VoiceConverter_Speaker)
        self.Label_Tool_VoiceConverter_Speaker.setObjectName(u"Label_Tool_VoiceConverter_Speaker")
        self.Label_Tool_VoiceConverter_Speaker.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_104.addWidget(self.Label_Tool_VoiceConverter_Speaker)

        self.ComboBox_Tool_VoiceConverter_Speaker = QComboBox(self.Frame_Tool_VoiceConverter_Speaker)
        self.ComboBox_Tool_VoiceConverter_Speaker.setObjectName(u"ComboBox_Tool_VoiceConverter_Speaker")
        self.ComboBox_Tool_VoiceConverter_Speaker.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_104.addWidget(self.ComboBox_Tool_VoiceConverter_Speaker)


        self.verticalLayout_131.addWidget(self.Frame_Tool_VoiceConverter_Speaker)

        self.Frame_Tool_VoiceConverter_Audio_Dir_Save = QFrame(self.Frame_BasicSettings_Tool_VoiceConverter)
        self.Frame_Tool_VoiceConverter_Audio_Dir_Save.setObjectName(u"Frame_Tool_VoiceConverter_Audio_Dir_Save")
        self.Frame_Tool_VoiceConverter_Audio_Dir_Save.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceConverter_Audio_Dir_Save.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_107 = QVBoxLayout(self.Frame_Tool_VoiceConverter_Audio_Dir_Save)
        self.verticalLayout_107.setSpacing(12)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceConverter_Audio_Dir_Save = QLabel(self.Frame_Tool_VoiceConverter_Audio_Dir_Save)
        self.Label_Tool_VoiceConverter_Audio_Dir_Save.setObjectName(u"Label_Tool_VoiceConverter_Audio_Dir_Save")
        self.Label_Tool_VoiceConverter_Audio_Dir_Save.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_107.addWidget(self.Label_Tool_VoiceConverter_Audio_Dir_Save)

        self.ChildFrame_Tool_VoiceConverter_Audio_Dir_Save = QFrame(self.Frame_Tool_VoiceConverter_Audio_Dir_Save)
        self.ChildFrame_Tool_VoiceConverter_Audio_Dir_Save.setObjectName(u"ChildFrame_Tool_VoiceConverter_Audio_Dir_Save")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceConverter_Audio_Dir_Save.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceConverter_Audio_Dir_Save.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceConverter_Audio_Dir_Save.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_46 = QHBoxLayout(self.ChildFrame_Tool_VoiceConverter_Audio_Dir_Save)
        self.horizontalLayout_46.setSpacing(12)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Tool_VoiceConverter_Audio_Dir_Save = QLineEdit(self.ChildFrame_Tool_VoiceConverter_Audio_Dir_Save)
        self.LineEdit_Tool_VoiceConverter_Audio_Dir_Save.setObjectName(u"LineEdit_Tool_VoiceConverter_Audio_Dir_Save")
        self.LineEdit_Tool_VoiceConverter_Audio_Dir_Save.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_46.addWidget(self.LineEdit_Tool_VoiceConverter_Audio_Dir_Save)

        self.Button_Tool_VoiceConverter_Audio_Dir_Save = QPushButton(self.ChildFrame_Tool_VoiceConverter_Audio_Dir_Save)
        self.Button_Tool_VoiceConverter_Audio_Dir_Save.setObjectName(u"Button_Tool_VoiceConverter_Audio_Dir_Save")
        sizePolicy1.setHeightForWidth(self.Button_Tool_VoiceConverter_Audio_Dir_Save.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceConverter_Audio_Dir_Save.setSizePolicy(sizePolicy1)
        self.Button_Tool_VoiceConverter_Audio_Dir_Save.setMaximumSize(QSize(24, 24))
        self.Button_Tool_VoiceConverter_Audio_Dir_Save.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_46.addWidget(self.Button_Tool_VoiceConverter_Audio_Dir_Save)


        self.verticalLayout_107.addWidget(self.ChildFrame_Tool_VoiceConverter_Audio_Dir_Save)


        self.verticalLayout_131.addWidget(self.Frame_Tool_VoiceConverter_Audio_Dir_Save)


        self.verticalLayout_117.addWidget(self.Frame_BasicSettings_Tool_VoiceConverter)

        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter = QCheckBox(self.GroupBox_EssentialParams_Tool_VoiceConverter)
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter.setObjectName(u"CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter")
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_117.addWidget(self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter)

        self.Frame_AdvanceSettings_Tool_VoiceConverter = QFrame(self.GroupBox_EssentialParams_Tool_VoiceConverter)
        self.Frame_AdvanceSettings_Tool_VoiceConverter.setObjectName(u"Frame_AdvanceSettings_Tool_VoiceConverter")
        self.Frame_AdvanceSettings_Tool_VoiceConverter.setFrameShape(QFrame.StyledPanel)
        self.Frame_AdvanceSettings_Tool_VoiceConverter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.Frame_AdvanceSettings_Tool_VoiceConverter)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.Frame_Tool_VoiceConverter_EmotionStrength = QFrame(self.Frame_AdvanceSettings_Tool_VoiceConverter)
        self.Frame_Tool_VoiceConverter_EmotionStrength.setObjectName(u"Frame_Tool_VoiceConverter_EmotionStrength")
        self.Frame_Tool_VoiceConverter_EmotionStrength.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceConverter_EmotionStrength.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_103 = QVBoxLayout(self.Frame_Tool_VoiceConverter_EmotionStrength)
        self.verticalLayout_103.setSpacing(12)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceConverter_EmotionStrength = QLabel(self.Frame_Tool_VoiceConverter_EmotionStrength)
        self.Label_Tool_VoiceConverter_EmotionStrength.setObjectName(u"Label_Tool_VoiceConverter_EmotionStrength")
        self.Label_Tool_VoiceConverter_EmotionStrength.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_103.addWidget(self.Label_Tool_VoiceConverter_EmotionStrength)

        self.ChildFrame_Tool_VoiceConverter_EmotionStrength = QFrame(self.Frame_Tool_VoiceConverter_EmotionStrength)
        self.ChildFrame_Tool_VoiceConverter_EmotionStrength.setObjectName(u"ChildFrame_Tool_VoiceConverter_EmotionStrength")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceConverter_EmotionStrength.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceConverter_EmotionStrength.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceConverter_EmotionStrength.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_43 = QHBoxLayout(self.ChildFrame_Tool_VoiceConverter_EmotionStrength)
        self.horizontalLayout_43.setSpacing(12)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSlider_Tool_VoiceConverter_EmotionStrength = QSlider(self.ChildFrame_Tool_VoiceConverter_EmotionStrength)
        self.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setObjectName(u"HorizontalSlider_Tool_VoiceConverter_EmotionStrength")
        self.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
        self.HorizontalSlider_Tool_VoiceConverter_EmotionStrength.setOrientation(Qt.Horizontal)

        self.horizontalLayout_43.addWidget(self.HorizontalSlider_Tool_VoiceConverter_EmotionStrength)

        self.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength = QDoubleSpinBox(self.ChildFrame_Tool_VoiceConverter_EmotionStrength)
        self.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength.setObjectName(u"DoubleSpinBox_Tool_VoiceConverter_EmotionStrength")
        self.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength.setStyleSheet(u"QDoubleSpinBox {\n"
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

        self.horizontalLayout_43.addWidget(self.DoubleSpinBox_Tool_VoiceConverter_EmotionStrength)


        self.verticalLayout_103.addWidget(self.ChildFrame_Tool_VoiceConverter_EmotionStrength)


        self.verticalLayout_118.addWidget(self.Frame_Tool_VoiceConverter_EmotionStrength)

        self.Frame_Tool_VoiceConverter_PhonemeDuration = QFrame(self.Frame_AdvanceSettings_Tool_VoiceConverter)
        self.Frame_Tool_VoiceConverter_PhonemeDuration.setObjectName(u"Frame_Tool_VoiceConverter_PhonemeDuration")
        self.Frame_Tool_VoiceConverter_PhonemeDuration.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceConverter_PhonemeDuration.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_105 = QVBoxLayout(self.Frame_Tool_VoiceConverter_PhonemeDuration)
        self.verticalLayout_105.setSpacing(12)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceConverter_PhonemeDuration = QLabel(self.Frame_Tool_VoiceConverter_PhonemeDuration)
        self.Label_Tool_VoiceConverter_PhonemeDuration.setObjectName(u"Label_Tool_VoiceConverter_PhonemeDuration")
        self.Label_Tool_VoiceConverter_PhonemeDuration.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_105.addWidget(self.Label_Tool_VoiceConverter_PhonemeDuration)

        self.ChildFrame_Tool_VoiceConverter_PhonemeDuration = QFrame(self.Frame_Tool_VoiceConverter_PhonemeDuration)
        self.ChildFrame_Tool_VoiceConverter_PhonemeDuration.setObjectName(u"ChildFrame_Tool_VoiceConverter_PhonemeDuration")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceConverter_PhonemeDuration.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceConverter_PhonemeDuration.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceConverter_PhonemeDuration.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_44 = QHBoxLayout(self.ChildFrame_Tool_VoiceConverter_PhonemeDuration)
        self.horizontalLayout_44.setSpacing(12)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration = QSlider(self.ChildFrame_Tool_VoiceConverter_PhonemeDuration)
        self.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setObjectName(u"HorizontalSlider_Tool_VoiceConverter_PhonemeDuration")
        self.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
        self.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration.setOrientation(Qt.Horizontal)

        self.horizontalLayout_44.addWidget(self.HorizontalSlider_Tool_VoiceConverter_PhonemeDuration)

        self.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration = QDoubleSpinBox(self.ChildFrame_Tool_VoiceConverter_PhonemeDuration)
        self.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration.setObjectName(u"DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration")
        self.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration.setStyleSheet(u"QDoubleSpinBox {\n"
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

        self.horizontalLayout_44.addWidget(self.DoubleSpinBox_Tool_VoiceConverter_PhonemeDuration)


        self.verticalLayout_105.addWidget(self.ChildFrame_Tool_VoiceConverter_PhonemeDuration)


        self.verticalLayout_118.addWidget(self.Frame_Tool_VoiceConverter_PhonemeDuration)

        self.Frame_Tool_VoiceConverter_SpeechRate = QFrame(self.Frame_AdvanceSettings_Tool_VoiceConverter)
        self.Frame_Tool_VoiceConverter_SpeechRate.setObjectName(u"Frame_Tool_VoiceConverter_SpeechRate")
        self.Frame_Tool_VoiceConverter_SpeechRate.setMinimumSize(QSize(0, 123))
        self.Frame_Tool_VoiceConverter_SpeechRate.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: rgb(33, 33, 33);\n"
"}")
        self.verticalLayout_106 = QVBoxLayout(self.Frame_Tool_VoiceConverter_SpeechRate)
        self.verticalLayout_106.setSpacing(12)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(21, 12, 21, 12)
        self.Label_Tool_VoiceConverter_SpeechRate = QLabel(self.Frame_Tool_VoiceConverter_SpeechRate)
        self.Label_Tool_VoiceConverter_SpeechRate.setObjectName(u"Label_Tool_VoiceConverter_SpeechRate")
        self.Label_Tool_VoiceConverter_SpeechRate.setStyleSheet(u"QLabel {\n"
"	/*text-align: center;*/\n"
"	/*color: rgb(255, 255, 255);*/\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"	border-style: solid;\n"
"}")

        self.verticalLayout_106.addWidget(self.Label_Tool_VoiceConverter_SpeechRate)

        self.ChildFrame_Tool_VoiceConverter_SpeechRate = QFrame(self.Frame_Tool_VoiceConverter_SpeechRate)
        self.ChildFrame_Tool_VoiceConverter_SpeechRate.setObjectName(u"ChildFrame_Tool_VoiceConverter_SpeechRate")
        sizePolicy4.setHeightForWidth(self.ChildFrame_Tool_VoiceConverter_SpeechRate.sizePolicy().hasHeightForWidth())
        self.ChildFrame_Tool_VoiceConverter_SpeechRate.setSizePolicy(sizePolicy4)
        self.ChildFrame_Tool_VoiceConverter_SpeechRate.setStyleSheet(u"QFrame {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_45 = QHBoxLayout(self.ChildFrame_Tool_VoiceConverter_SpeechRate)
        self.horizontalLayout_45.setSpacing(12)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.HorizontalSlider_Tool_VoiceConverter_SpeechRate = QSlider(self.ChildFrame_Tool_VoiceConverter_SpeechRate)
        self.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setObjectName(u"HorizontalSlider_Tool_VoiceConverter_SpeechRate")
        self.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
        self.HorizontalSlider_Tool_VoiceConverter_SpeechRate.setOrientation(Qt.Horizontal)

        self.horizontalLayout_45.addWidget(self.HorizontalSlider_Tool_VoiceConverter_SpeechRate)

        self.DoubleSpinBox_Tool_VoiceConverter_SpeechRate = QDoubleSpinBox(self.ChildFrame_Tool_VoiceConverter_SpeechRate)
        self.DoubleSpinBox_Tool_VoiceConverter_SpeechRate.setObjectName(u"DoubleSpinBox_Tool_VoiceConverter_SpeechRate")
        self.DoubleSpinBox_Tool_VoiceConverter_SpeechRate.setStyleSheet(u"QDoubleSpinBox {\n"
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

        self.horizontalLayout_45.addWidget(self.DoubleSpinBox_Tool_VoiceConverter_SpeechRate)


        self.verticalLayout_106.addWidget(self.ChildFrame_Tool_VoiceConverter_SpeechRate)


        self.verticalLayout_118.addWidget(self.Frame_Tool_VoiceConverter_SpeechRate)


        self.verticalLayout_117.addWidget(self.Frame_AdvanceSettings_Tool_VoiceConverter)


        self.verticalLayout_26.addWidget(self.GroupBox_EssentialParams_Tool_VoiceConverter)

        self.ScrollArea_Middle_Tool_VoiceConverter.setWidget(self.ScrollArea_Right_WidgetContents_Tool_VoiceConverter)

        self.gridLayout_13.addWidget(self.ScrollArea_Middle_Tool_VoiceConverter, 0, 1, 1, 1)

        self.Widget_Right_Tool_VoiceConverter = QWidget(self.StackedWidget_Pages_Tool_VoiceConverter)
        self.Widget_Right_Tool_VoiceConverter.setObjectName(u"Widget_Right_Tool_VoiceConverter")
        self.Widget_Right_Tool_VoiceConverter.setMaximumSize(QSize(420, 16777215))
        self.Widget_Right_Tool_VoiceConverter.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(36, 36, 36);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}\n"
"QWidget:hover {\n"
"}")
        self.gridLayout_18 = QGridLayout(self.Widget_Right_Tool_VoiceConverter)
        self.gridLayout_18.setSpacing(12)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(12, 12, 12, 12)
        self.TextBrowser_Params_Tool_VoiceConverter = QTextBrowser(self.Widget_Right_Tool_VoiceConverter)
        self.TextBrowser_Params_Tool_VoiceConverter.setObjectName(u"TextBrowser_Params_Tool_VoiceConverter")
        sizePolicy1.setHeightForWidth(self.TextBrowser_Params_Tool_VoiceConverter.sizePolicy().hasHeightForWidth())
        self.TextBrowser_Params_Tool_VoiceConverter.setSizePolicy(sizePolicy1)
        self.TextBrowser_Params_Tool_VoiceConverter.setStyleSheet(u"QTextBrowser {\n"
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

        self.gridLayout_18.addWidget(self.TextBrowser_Params_Tool_VoiceConverter, 0, 0, 1, 1)

        self.Button_CheckOutput_Tool_VoiceConverter = QPushButton(self.Widget_Right_Tool_VoiceConverter)
        self.Button_CheckOutput_Tool_VoiceConverter.setObjectName(u"Button_CheckOutput_Tool_VoiceConverter")
        self.Button_CheckOutput_Tool_VoiceConverter.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_18.addWidget(self.Button_CheckOutput_Tool_VoiceConverter, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.Widget_Right_Tool_VoiceConverter, 0, 2, 1, 1)

        self.ProgressBar_Tool_VoiceConverter = QProgressBar(self.StackedWidget_Pages_Tool_VoiceConverter)
        self.ProgressBar_Tool_VoiceConverter.setObjectName(u"ProgressBar_Tool_VoiceConverter")
        self.ProgressBar_Tool_VoiceConverter.setMinimumSize(QSize(0, 30))
        self.ProgressBar_Tool_VoiceConverter.setStyleSheet(u"QProgressBar {\n"
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
        self.ProgressBar_Tool_VoiceConverter.setValue(0)
        self.ProgressBar_Tool_VoiceConverter.setTextVisible(False)
        self.horizontalLayout_48 = QHBoxLayout(self.ProgressBar_Tool_VoiceConverter)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_Tool_VoiceConverter = QStackedWidget(self.ProgressBar_Tool_VoiceConverter)
        self.StackedWidget_Tool_VoiceConverter.setObjectName(u"StackedWidget_Tool_VoiceConverter")
        self.StackedWidget_Tool_VoiceConverter.setMaximumSize(QSize(16777215, 30))
        self.StackedWidget_Tool_VoiceConverter.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(90, 90, 90, 45);\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgba(120, 120, 120, 60);\n"
"}")
        self.Page_Tool_VoiceConverter_Execute = QWidget()
        self.Page_Tool_VoiceConverter_Execute.setObjectName(u"Page_Tool_VoiceConverter_Execute")
        self.verticalLayout_112 = QVBoxLayout(self.Page_Tool_VoiceConverter_Execute)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_VoiceConverter_Execute = QPushButton(self.Page_Tool_VoiceConverter_Execute)
        self.Button_Tool_VoiceConverter_Execute.setObjectName(u"Button_Tool_VoiceConverter_Execute")
        sizePolicy5.setHeightForWidth(self.Button_Tool_VoiceConverter_Execute.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceConverter_Execute.setSizePolicy(sizePolicy5)
        self.Button_Tool_VoiceConverter_Execute.setMinimumSize(QSize(0, 30))
        self.Button_Tool_VoiceConverter_Execute.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_112.addWidget(self.Button_Tool_VoiceConverter_Execute)

        self.StackedWidget_Tool_VoiceConverter.addWidget(self.Page_Tool_VoiceConverter_Execute)
        self.Page_Tool_VoiceConverter_Terminate = QWidget()
        self.Page_Tool_VoiceConverter_Terminate.setObjectName(u"Page_Tool_VoiceConverter_Terminate")
        self.verticalLayout_113 = QVBoxLayout(self.Page_Tool_VoiceConverter_Terminate)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.Button_Tool_VoiceConverter_Terminate = QPushButton(self.Page_Tool_VoiceConverter_Terminate)
        self.Button_Tool_VoiceConverter_Terminate.setObjectName(u"Button_Tool_VoiceConverter_Terminate")
        sizePolicy5.setHeightForWidth(self.Button_Tool_VoiceConverter_Terminate.sizePolicy().hasHeightForWidth())
        self.Button_Tool_VoiceConverter_Terminate.setSizePolicy(sizePolicy5)
        self.Button_Tool_VoiceConverter_Terminate.setMinimumSize(QSize(0, 30))
        self.Button_Tool_VoiceConverter_Terminate.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_113.addWidget(self.Button_Tool_VoiceConverter_Terminate)

        self.StackedWidget_Tool_VoiceConverter.addWidget(self.Page_Tool_VoiceConverter_Terminate)

        self.horizontalLayout_48.addWidget(self.StackedWidget_Tool_VoiceConverter)


        self.gridLayout_13.addWidget(self.ProgressBar_Tool_VoiceConverter, 1, 0, 1, 3)

        self.StackedWidget_Pages_Tools.addWidget(self.StackedWidget_Pages_Tool_VoiceConverter)

        self.verticalLayout_101.addWidget(self.StackedWidget_Pages_Tools)

        self.StackedWidget_Pages.addWidget(self.Page_Tools)
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
"	background-color: rgb(36, 36, 36);\n"
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
        sizePolicy3.setHeightForWidth(self.Frame_Settings_Title_Spacer.sizePolicy().hasHeightForWidth())
        self.Frame_Settings_Title_Spacer.setSizePolicy(sizePolicy3)
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
        self.verticalLayout_135 = QVBoxLayout(self.Frame_Settings_Middle)
        self.verticalLayout_135.setSpacing(0)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout_135.addWidget(self.Frame_Setting_Language)

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
        sizePolicy4.setHeightForWidth(self.CheckBox_Setting_AutoUpdate.sizePolicy().hasHeightForWidth())
        self.CheckBox_Setting_AutoUpdate.setSizePolicy(sizePolicy4)
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


        self.verticalLayout_135.addWidget(self.Frame_Setting_AutoUpdate)

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
        sizePolicy4.setHeightForWidth(self.CheckBox_Setting_Synchronizer.sizePolicy().hasHeightForWidth())
        self.CheckBox_Setting_Synchronizer.setSizePolicy(sizePolicy4)
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


        self.verticalLayout_135.addWidget(self.Frame_Setting_Synchronizer)


        self.verticalLayout_109.addWidget(self.Frame_Settings_Middle)

        self.VerticalSpacer_Settings = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_109.addItem(self.VerticalSpacer_Settings)

        self.StackedWidget_Pages.addWidget(self.Page_Settings)

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
        self.verticalLayout_23.setContentsMargins(12, 0, 12, 0)
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
        self.StatusBar.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(12, 12, 12, 123);\n"
"	border-width: 0px;\n"
"	border-style: solid;\n"
"}")
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
        self.StackedWidget_Pages_Tools.setCurrentIndex(0)
        self.StackedWidget_Tool_DatasetCreator.setCurrentIndex(1)
        self.StackedWidget_Tool_VoiceTrainer.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Label_Title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Home_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Download_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Tools_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Menu_Settings_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_Download_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Label_Download_FFmpeg.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_GCC.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_CMake.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_Python.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_PyReqs.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Download_Pytorch.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_Tools_Title_AudioProcessor.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_Tools_Title_VoiceIdentifier.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_Tools_Title_VoiceTranscriber.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_Tools_Title_DatasetCreator.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_Tools_Title_VoiceTrainer.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.ToolButton_Tools_Title_VoiceConverter.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        ___qtreewidgetitem = self.TreeWidget_Catalogue_Tool_AudioProcessor.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled = self.TreeWidget_Catalogue_Tool_AudioProcessor.isSortingEnabled()
        self.TreeWidget_Catalogue_Tool_AudioProcessor.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.TreeWidget_Catalogue_Tool_AudioProcessor.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Tool_AudioProcessor.setSortingEnabled(__sortingEnabled)

        self.GroupBox_EssentialParams_Tool_AudioProcessor.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_Tool_AudioProcessor.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_Tool_AudioProcessor_Media_Dir_Input.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_AudioProcessor_Media_Dir_Input.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_AudioProcessor_Media_Format_Output.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_AudioProcessor_Media_Dir_Output.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_AudioProcessor_Media_Dir_Output.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_Tool_AudioProcessor.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Tool_AudioProcessor_RMS_Threshold.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_AudioProcessor_Audio_Length_Min.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_AudioProcessor_Silent_Interval_Min.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_AudioProcessor_Hop_Size.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_AudioProcessor_Silence_Kept_Max.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtreewidgetitem3 = self.TreeWidget_Catalogue_Tool_VoiceIdentifier.headerItem()
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled1 = self.TreeWidget_Catalogue_Tool_VoiceIdentifier.isSortingEnabled()
        self.TreeWidget_Catalogue_Tool_VoiceIdentifier.setSortingEnabled(False)
        ___qtreewidgetitem4 = self.TreeWidget_Catalogue_Tool_VoiceIdentifier.topLevelItem(0)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Tool_VoiceIdentifier.setSortingEnabled(__sortingEnabled1)

        self.GroupBox_EssentialParams_Tool_VoiceIdentifier.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceIdentifier.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_Tool_VoiceIdentifier_Audio_Dir_Input.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceIdentifier_Audio_Dir_Input.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceIdentifier_Audio_Path_Std.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceIdentifier_Audio_Path_Std.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceIdentifier_Speaker.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceIdentifier_DecisionThreshold.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceIdentifier_Audio_Dir_Output.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceIdentifier_Audio_Dir_Output.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceIdentifier.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Tool_VoiceIdentifier_Model_Dir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceIdentifier_Model_Dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceIdentifier_Model_Type.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceIdentifier_Model_Name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceIdentifier_Feature_Method.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceIdentifier_Duration_of_Audio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtreewidgetitem6 = self.TreeWidget_Catalogue_Tool_VoiceTranscriber.headerItem()
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled2 = self.TreeWidget_Catalogue_Tool_VoiceTranscriber.isSortingEnabled()
        self.TreeWidget_Catalogue_Tool_VoiceTranscriber.setSortingEnabled(False)
        ___qtreewidgetitem7 = self.TreeWidget_Catalogue_Tool_VoiceTranscriber.topLevelItem(0)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Tool_VoiceTranscriber.setSortingEnabled(__sortingEnabled2)

        self.GroupBox_EssentialParams_Tool_VoiceTranscriber.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceTranscriber.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_Tool_VoiceTranscriber_WAV_Dir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceTranscriber_WAV_Dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceTranscriber_SRT_Dir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceTranscriber_SRT_Dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTranscriber.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Tool_VoiceTranscriber_Model_Dir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceTranscriber_Model_Dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceTranscriber_Model_Name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceTranscriber_Verbose.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Tool_VoiceTranscriber_Verbose.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Tool_VoiceTranscriber_Condition_on_Previous_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Tool_VoiceTranscriber_Condition_on_Previous_Text.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Tool_VoiceTranscriber_fp16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Tool_VoiceTranscriber_fp16.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_OptionalParams_Tool_VoiceTranscriber.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTranscriber.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_Tool_VoiceTranscriber_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtreewidgetitem9 = self.TreeWidget_Catalogue_Tool_DatasetCreator.headerItem()
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled3 = self.TreeWidget_Catalogue_Tool_DatasetCreator.isSortingEnabled()
        self.TreeWidget_Catalogue_Tool_DatasetCreator.setSortingEnabled(False)
        ___qtreewidgetitem10 = self.TreeWidget_Catalogue_Tool_DatasetCreator.topLevelItem(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Tool_DatasetCreator.setSortingEnabled(__sortingEnabled3)

        self.GroupBox_EssentialParams_Tool_DatasetCreator.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_Tool_DatasetCreator.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_Tool_DatasetCreator_WAV_Dir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_DatasetCreator_WAV_Dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_DatasetCreator_SRT_Dir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_DatasetCreator_SRT_Dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_DatasetCreator_AutoEncoder.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_DatasetCreator_WAV_Dir_Split.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_DatasetCreator_WAV_Dir_Split.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_DatasetCreator_FileList_Path_Training.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_DatasetCreator_FileList_Path_Training.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_DatasetCreator_FileList_Path_Validation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_DatasetCreator_FileList_Path_Validation.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_Tool_DatasetCreator.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Tool_DatasetCreator_Sample_Rate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_DatasetCreator_Subtype.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_DatasetCreator_TrainRatio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtreewidgetitem12 = self.TreeWidget_Catalogue_Tool_VoiceTrainer.headerItem()
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled4 = self.TreeWidget_Catalogue_Tool_VoiceTrainer.isSortingEnabled()
        self.TreeWidget_Catalogue_Tool_VoiceTrainer.setSortingEnabled(False)
        ___qtreewidgetitem13 = self.TreeWidget_Catalogue_Tool_VoiceTrainer.topLevelItem(0)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Tool_VoiceTrainer.setSortingEnabled(__sortingEnabled4)

        self.GroupBox_EssentialParams_Tool_VoiceTrainer.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceTrainer.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_Tool_VoiceTrainer_FileList_Path_Training.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceTrainer_FileList_Path_Training.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceTrainer_FileList_Path_Validation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceTrainer_FileList_Path_Validation.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceTrainer_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceTrainer_Epochs.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceTrainer_Batch_Size.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceTrainer_Config_Dir_Save.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceTrainer_Config_Dir_Save.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceTrainer_Model_Dir_Save.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceTrainer_Model_Dir_Save.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceTrainer.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Tool_VoiceTrainer_Eval_Interval.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceTrainer_Num_Workers.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceTrainer_FP16_Run.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Tool_VoiceTrainer_FP16_Run.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Tool_VoiceTrainer_Find_Unused_Parameters.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Tool_VoiceTrainer_Find_Unused_Parameters.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.GroupBox_OptionalParams_Tool_VoiceTrainer.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox2", None))
        self.CheckBox_Toggle_BasicOptionalSettings_Tool_VoiceTrainer.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_Tool_VoiceTrainer_Model_Path_Pretrained_G.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_G.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceTrainer_Model_Path_Pretrained_D.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceTrainer_Model_Path_Pretrained_D.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceOptionalSettings_Tool_VoiceTrainer.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Tool_VoiceTrainer_Config_Path_Load.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceTrainer_Config_Path_Load.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceTrainer_Speakers.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtreewidgetitem15 = self.TreeWidget_Catalogue_Tool_VoiceConverter.headerItem()
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"HeaderView", None));

        __sortingEnabled5 = self.TreeWidget_Catalogue_Tool_VoiceConverter.isSortingEnabled()
        self.TreeWidget_Catalogue_Tool_VoiceConverter.setSortingEnabled(False)
        ___qtreewidgetitem16 = self.TreeWidget_Catalogue_Tool_VoiceConverter.topLevelItem(0)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"RootItem", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"ChildItem", None));
        self.TreeWidget_Catalogue_Tool_VoiceConverter.setSortingEnabled(__sortingEnabled5)

        self.GroupBox_EssentialParams_Tool_VoiceConverter.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox1", None))
        self.CheckBox_Toggle_BasicSettings_Tool_VoiceConverter.setText(QCoreApplication.translate("MainWindow", u"CheckBox1", None))
        self.Label_Tool_VoiceConverter_Config_Path_Load.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceConverter_Config_Path_Load.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceConverter_Model_Path_Load.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceConverter_Model_Path_Load.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_Tool_VoiceConverter_Text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceConverter_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceConverter_Speaker.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceConverter_Audio_Dir_Save.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Button_Tool_VoiceConverter_Audio_Dir_Save.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CheckBox_Toggle_AdvanceSettings_Tool_VoiceConverter.setText(QCoreApplication.translate("MainWindow", u"CheckBox2", None))
        self.Label_Tool_VoiceConverter_EmotionStrength.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceConverter_PhonemeDuration.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Tool_VoiceConverter_SpeechRate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolButton_Settings_Title.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.Label_Setting_Language.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_AutoUpdate.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.CheckBox_Setting_Synchronizer.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.Label_ToolsStatus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Label_Usage_CPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Usage_GPU.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.Label_Version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))