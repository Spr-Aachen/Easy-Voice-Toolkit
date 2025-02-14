from typing import Type, Optional
from PyEasyUtils import setRichText
from PySide6.QtCore import Qt, QRect, QSize
from PySide6.QtCore import QCoreApplication as QCA
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import *
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets.Common import FileDialogMode
from QEasyWidgets.Components import *
from QEasyWidgets import QTasks

from components import Frame_RangeSetting
#from assets import *
from functions import *

##############################################################################################################################

class SubPage(QWidget):
    """
    """
    def __init__(self, parent = None, paramsManager: ParamsManager = ...):
        super().__init__(parent)

        self.widgets = {}
        self.paramWidgets = {}

        self.paramsManager = paramsManager

        leftWidget = QWidget(self)
        leftWidget.setMinimumSize(QSize(150, 0))
        leftWidget_layout = QVBoxLayout(leftWidget)
        leftWidget_layout.setSpacing(12)
        leftWidget_layout.setContentsMargins(12, 12, 12, 12)
        self.catalogueWidget = TreeWidgetBase()
        self.catalogueWidget.clear()
        self.catalogueWidget.setHeaderHidden(True)
        leftWidget_layout.addWidget(self.catalogueWidget)

        middleWidget = ScrollAreaBase(self)
        middleWidget.setMinimumSize(QSize(600, 0))
        middleWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        middleWidget.setWidgetResizable(True)
        self.middleWidget_contentWidget = QWidget()
        middleWidget_contentWidget_layout = QVBoxLayout(self.middleWidget_contentWidget)
        middleWidget_contentWidget_layout.setSpacing(12)
        middleWidget_contentWidget_layout.setContentsMargins(12, 12, 12, 12)
        middleWidget.setWidget(self.middleWidget_contentWidget)

        rightWidget = QWidget(self)
        self.rightWidget_layout = QGridLayout(rightWidget)
        self.rightWidget_layout.setSpacing(12)
        self.rightWidget_layout.setContentsMargins(12, 12, 12, 12)
        rightWidget.setStyleSheet("""
            QWidget:hover {
                background-color: rgba(36, 36, 36, 3);
            }
        """)
        textBrowser_params = TextBrowserBase()
        monitorFile_config = QTasks.MonitorFile(self.paramsManager.configPath)
        monitorFile_config.start()
        monitorFile_config.Signal_fileContent.connect(
            lambda fileContent: textBrowser_params.setText(
                fileContent
            )
        )
        self.rightWidget_layout.addWidget(textBrowser_params, 0, 0, 1, 3)
        button_resetSettings = HollowButton()
        button_resetSettings.setText(QCA.translate('MainWindow', "全部重置"))
        button_resetSettings.clicked.connect(
            lambda: self.paramsManager.resetSettings()
        )
        self.rightWidget_layout.addWidget(button_resetSettings, 1, 0, 1, 1)
        button_importSettings = HollowButton()
        button_importSettings.setText(QCA.translate('MainWindow', "导入配置"))
        button_importSettings.clicked.connect(
            lambda: self.paramsManager.importSettings(
                QFunc.getFileDialog(
                    mode = FileDialogMode.SelectFile,
                    fileType = "ini类型 (*.ini)"
                )
            )
        )
        self.rightWidget_layout.addWidget(button_importSettings, 1, 1, 1, 1)
        button_exportSettings = HollowButton()
        button_exportSettings.setText(QCA.translate('MainWindow', "导出配置"))
        button_exportSettings.clicked.connect(
            lambda: self.paramsManager.exportSettings(
                QFunc.getFileDialog(
                    mode = FileDialogMode.SaveFile,
                    fileType = "ini类型 (*.ini)"
                )
            )
        )
        self.rightWidget_layout.addWidget(button_exportSettings, 1, 2, 1, 1)

        self.progressBar = ProgressBarBase(self)
        self.progressBar.setMinimumSize(QSize(0, 30))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        progressBar_stackedWidget = QStackedWidget()
        progressBar_stackedWidget.setStyleSheet("""
            QWidget {
                background-color: rgba(123, 123, 123, 24);
            }
            QWidget:hover {
                background-color: rgba(123, 123, 123, 48);
            }
        """)
        progressBar_stackedWidget_page_execute = QWidget()
        progressBar_stackedWidget_execute_layout = QVBoxLayout(progressBar_stackedWidget_page_execute)
        progressBar_stackedWidget_execute_layout.setSpacing(0)
        progressBar_stackedWidget_execute_layout.setContentsMargins(0, 0, 0, 0)
        self.executeButton = HollowButton()
        progressBar_stackedWidget_execute_layout.addWidget(self.executeButton)
        progressBar_stackedWidget.addWidget(progressBar_stackedWidget_page_execute)
        progressBar_stackedWidget_page_terminate = QWidget()
        progressBar_stackedWidget_terminate_layout = QVBoxLayout(progressBar_stackedWidget_page_terminate)
        progressBar_stackedWidget_terminate_layout.setSpacing(0)
        progressBar_stackedWidget_terminate_layout.setContentsMargins(0, 0, 0, 0)
        self.terminateButton = HollowButton()
        progressBar_stackedWidget_terminate_layout.addWidget(self.terminateButton)
        progressBar_stackedWidget.addWidget(progressBar_stackedWidget_page_terminate)
        progressBar_layout = QHBoxLayout(self.progressBar)
        progressBar_layout.setContentsMargins(0, 0, 0, 0)
        progressBar_layout.setSpacing(0)
        progressBar_layout.addWidget(progressBar_stackedWidget)

        layout = QGridLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(leftWidget, 0, 0, 1, 1)
        layout.setColumnStretch(0, 3)
        layout.addWidget(middleWidget, 0, 1, 1, 1)
        layout.setColumnStretch(1, 10)
        layout.addWidget(rightWidget, 0, 2, 1, 1)
        layout.setColumnStretch(2, 7)
        layout.addWidget(self.progressBar, 1, 0, 1, 3)

    def findChildWidget(self, *args, type: Optional[Type[QWidget]] = None):
        if len(args) > 3:
            args, type = args[:-1], args[-1]
        childWidget = self.widgets.get(args, None)
        if type is not None and not isinstance(childWidget, type):
            childWidget = QFunc.findChild(childWidget, type)
        return childWidget

    def _setLabelText(self, label, text):
        QFunc.setText(
            widget = label,
            text = setRichText(
                text = QCA.translate('MainWindow', text),
            )
        )

    def _setButtonMenu(self, menuButton: MenuButton, widget):
        menuButton.setMenu(
            actionEvents = {
                "重置": lambda: self.paramsManager.resetParam(widget),
                "复制": lambda: QApplication.clipboard().setText(str(Function_GetParam(widget))),
            }
        )

    def _connectToTreeWidget(self, widget, rootItemText: str, childItemText: str):
        Function_AddToTreeWidget(
            widget = widget,
            treeWidget = self.catalogueWidget,
            rootItemText = QCA.translate('MainWindow', rootItemText),
            childItemText = QCA.translate('MainWindow', childItemText.splitlines()[0]),
        )

    def _addToContainer(self, label: LabelBase, inputWidget: QWidget, menuButton: MenuButton, rootItemText: str, toolBoxText: Optional[str] = None, text: str = ...):
        menuButton.setFixedSize(QSize(27, 27))
        inputWidget.setMaximumHeight(27) if isinstance(inputWidget, (QLineEdit, QComboBox, QCheckBox, QSpinBox, QDoubleSpinBox, QSlider)) else None
        # Add to childFrame
        childFrame = QFrame()
        childFrame.setMinimumHeight(105 if not isinstance(inputWidget, (QTextBrowser, QTextEdit, QTableView)) else 210)
        childFrame.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border: none;
            }
            QFrame:hover {
                background-color: rgba(36, 36, 36, 12);
            }
        """)
        childFrame_layout = QGridLayout(childFrame)
        childFrame_layout.setSpacing(12)
        childFrame_layout.setContentsMargins(21, 12, 21, 12)
        childFrame_layout.addWidget(label, 0, 0, 1, 1)
        childFrame_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 1, 1, 1)
        childFrame_layout.addWidget(menuButton, 0, 2, 1, 1)
        childFrame_layout.addWidget(inputWidget, 1, 0, 1, 3)
        self.widgets[(rootItemText, toolBoxText, text.splitlines()[0])] = childFrame # record the childFrame
        # Add to toolBox
        if toolBoxText is None:
            toolBox = childFrame
        else:
            toolBoxText = toolBoxText.splitlines()[0]
            toolBox = self.findChildWidget(rootItemText, toolBoxText)
            if isinstance(toolBox, ToolBoxBase):
                toolBox.widget(0).addWidget(childFrame)
            else:
                toolBox = ToolBoxBase()
                toolPageItem = QWidget()
                toolPageItem_layout = QGridLayout(toolPageItem)
                toolPageItem_layout.setSpacing(0)
                toolPageItem_layout.setContentsMargins(0, 0, 0, 0)
                toolPageItem_layout.addWidget(childFrame)
                toolBox.addItem(toolPageItem, toolBoxText)
                self.widgets[(rootItemText, toolBoxText)] = toolBox # record the toolBox
            toolBox.widget(0).collapse()
        # Add to groupBox
        rootItemText = rootItemText.splitlines()[0]
        groupBox = self.findChildWidget(rootItemText)
        if isinstance(groupBox, GroupBoxBase):
            groupBox.layout().addWidget(toolBox)
        else:
            groupBox = GroupBoxBase()
            groupBox_layout = QGridLayout(groupBox)
            groupBox_layout.setSpacing(0)
            groupBox_layout.setContentsMargins(0, 12, 0, 12)
            groupBox_layout.addWidget(toolBox)
            groupBox.setTitle(rootItemText)
            self.middleWidget_contentWidget.layout().addWidget(groupBox)
            self.widgets[(rootItemText,)] = groupBox # record the groupbox

    def addLineEditFrame(self,
        rootItemText: str = ..., toolBoxText: Optional[str] = None, text: str = ..., toolTip: Optional[str] = None,
        fileDialogMode: Optional[FileDialogMode] = None, fileType: Optional[str] = None, directory: Optional[str] = None,
        section: str = ..., option: str = ..., defaultValue: str = ..., placeholderText: str = "",
        emptyAllowed: bool = False
    ):
        label = LabelBase()
        lineEdit = LineEditBase(self)
        lineEdit.setObjectName(text.splitlines()[0])
        button = MenuButton()
        self._setLabelText(label, text)
        lineEdit.setToolTip(toolTip) if toolTip is not None else None
        lineEdit.setFileDialog(fileDialogMode, fileType, directory) if fileDialogMode is not None else None
        self.paramsManager.setParam(lineEdit, section, option, defaultValue,
            setPlaceholderText = True,
            placeholderText = placeholderText
        )
        self._setButtonMenu(button, lineEdit)
        self._addToContainer(label, lineEdit, button, rootItemText, toolBoxText, text)
        self._connectToTreeWidget(label, rootItemText, text)
        self.paramWidgets[lineEdit] = emptyAllowed

    def addTextEditFrame(self,
        rootItemText: str = ..., toolBoxText: Optional[str] = None, text: str = ..., toolTip: Optional[str] = None,
        section: str = ..., option: str = ..., defaultValue: str = ..., placeholderText: str = "",
        emptyAllowed: bool = False
    ):
        label = LabelBase()
        textEdit = TextEditBase(self)
        textEdit.setObjectName(text.splitlines()[0])
        button = MenuButton()
        self._setLabelText(label, text)
        textEdit.setToolTip(toolTip) if toolTip is not None else None
        self.paramsManager.setParam(textEdit, section, option, defaultValue,
            setPlaceholderText = True,
            placeholderText = placeholderText
        )
        self._setButtonMenu(button, textEdit)
        self._addToContainer(label, textEdit, button, rootItemText, toolBoxText, text)
        self._connectToTreeWidget(label, rootItemText, text)
        self.paramWidgets[textEdit] = emptyAllowed

    def addCheckBoxFrame(self,
        rootItemText: str = ..., toolBoxText: Optional[str] = None, text: str = ..., toolTip: Optional[str] = None,
        section: str = ..., option: str = ..., defaultValue: str = ...,
        emptyAllowed: bool = False
    ):
        label = LabelBase()
        checkBox = CheckBoxBase(self)
        checkBox.setObjectName(text.splitlines()[0])
        Function_ConfigureCheckBox(checkBox, checkedText = "已启动", uncheckedText = "未启动")
        button = MenuButton()
        self._setLabelText(label, text)
        checkBox.setToolTip(toolTip) if toolTip is not None else None
        self.paramsManager.setParam(checkBox, section, option, defaultValue)
        self._setButtonMenu(button, checkBox)
        self._addToContainer(label, checkBox, button, rootItemText, toolBoxText, text)
        self._connectToTreeWidget(label, rootItemText, text)
        self.paramWidgets[checkBox] = emptyAllowed

    def addComboBoxFrame(self,
        rootItemText: str = ..., toolBoxText: Optional[str] = None, text: str = ..., toolTip: Optional[str] = None,
        items: list = ..., currentIndex: Optional[int] = None,
        section: str = ..., option: str = ..., defaultValue: str = ...,
        emptyAllowed: bool = False
    ):
        label = LabelBase()
        comboBox = ComboBoxBase(self)
        comboBox.setObjectName(text.splitlines()[0])
        button = MenuButton()
        self._setLabelText(label, text)
        comboBox.setToolTip(toolTip) if toolTip is not None else None
        comboBox.addItems(items)
        self.paramsManager.setParam(comboBox, section, option, defaultValue)
        comboBox.setCurrentIndex(currentIndex) if currentIndex is not None else None
        self._setButtonMenu(button, comboBox)
        self._addToContainer(label, comboBox, button, rootItemText, toolBoxText, text)
        self._connectToTreeWidget(label, rootItemText, text)
        self.paramWidgets[comboBox] = emptyAllowed

    def addSpinBoxFrame(self,
        rootItemText: str = ..., toolBoxText: Optional[str] = None, text: str = ..., toolTip: Optional[str] = None,
        minimum: int = ..., maximum: int = ..., step: Optional[int] = ...,
        section: str = ..., option: str = ..., defaultValue: str = ...,
        emptyAllowed: bool = False
    ):
        label = LabelBase()
        spinBox = SpinBoxBase(self)
        spinBox.setObjectName(text.splitlines()[0])
        button = MenuButton()
        self._setLabelText(label, text)
        spinBox.setToolTip(toolTip) if toolTip is not None else None
        spinBox.setRange(minimum, maximum)
        spinBox.setSingleStep(step) if step is not None else None
        self.paramsManager.setParam(spinBox, section, option, defaultValue)
        self._setButtonMenu(button, spinBox)
        self._addToContainer(label, spinBox, button, rootItemText, toolBoxText, text)
        self._connectToTreeWidget(label, rootItemText, text)
        self.paramWidgets[spinBox] = emptyAllowed

    def addDoubleSpinBoxFrame(self,
        rootItemText: str = ..., toolBoxText: Optional[str] = None, text: str = ..., toolTip: Optional[str] = None,
        minimum: float = ..., maximum: float = ..., step: Optional[float] = None,
        section: str = ..., option: str = ..., defaultValue: str = ...,
        emptyAllowed: bool = False
    ):
        label = LabelBase()
        doubleSpinBox = DoubleSpinBoxBase(self)
        doubleSpinBox.setObjectName(text.splitlines()[0])
        button = MenuButton()
        self._setLabelText(label, text)
        doubleSpinBox.setToolTip(toolTip) if toolTip is not None else None
        doubleSpinBox.setRange(minimum, maximum)
        doubleSpinBox.setSingleStep(step) if step is not None else None
        self.paramsManager.setParam(doubleSpinBox, section, option, defaultValue)
        self._setButtonMenu(button, doubleSpinBox)
        self._addToContainer(label, doubleSpinBox, button, rootItemText, toolBoxText, text)
        self._connectToTreeWidget(label, rootItemText, text)
        self.paramWidgets[doubleSpinBox] = emptyAllowed

    def addRangeSettingFrame(self,
        rootItemText: str = ..., toolBoxText: Optional[str] = None, text: str = ..., toolTip: Optional[str] = None,
        minimum: float = ..., maximum: float = ..., step: Optional[float] = None,
        section: str = ..., option: str = ..., defaultValue: str = ...,
        emptyAllowed: bool = False
    ):
        label = LabelBase()
        rangeSetting = Frame_RangeSetting(self)
        rangeSetting.setObjectName(text.splitlines()[0])
        button = MenuButton()
        self._setLabelText(label, text)
        rangeSetting.setToolTip(toolTip) if toolTip is not None else None
        rangeSetting.setRange(minimum, maximum)
        rangeSetting.setSingleStep(step) if step is not None else None
        self.paramsManager.setParam(rangeSetting, section, option, defaultValue)
        self._setButtonMenu(button, rangeSetting)
        self._addToContainer(label, rangeSetting, button, rootItemText, toolBoxText, text)
        self._connectToTreeWidget(label, rootItemText, text)
        self.paramWidgets[rangeSetting] = emptyAllowed

    def addEditAudioSpeakerTableFrame(self,
        rootItemText: str = ..., toolBoxText: Optional[str] = None, text: str = ...,
        headerLabels: list = ...,
        fileType: Optional[str] = None,
        section: str = ..., option: str = ..., defaultValue: str = ...,
    ):
        label = LabelBase()
        table = Table_EditAudioSpeaker()
        button = MenuButton()
        self._setLabelText(label, text)
        table.setHorizontalHeaderLabels(headerLabels)
        table.setFileDialog(fileType)
        self.paramsManager.setParam(table, section, option, defaultValue)
        #self._setButtonMenu(button, table)
        self._addToContainer(label, table, button, rootItemText, toolBoxText, text)
        self._connectToTreeWidget(label, rootItemText, text)

    def addSideBtn(self,
        text: str = ...,
        events: list = [],
    ):
        sideButton = HollowButton()
        sideButton.setText(text)
        sideButton.clicked.connect(lambda: EasyUtils.runEvents(events))
        self.rightWidget_layout.addWidget(sideButton, self.rightWidget_layout.rowCount(), 0, 1, 3)
        self.widgets[(text.splitlines()[0],)] = sideButton

    def addChkOutputSideBtn(self,
        outputRootEdit: QLineEdit
    ):
        chkOutputButton = HollowButton()
        chkOutputButton.setText(QCA.translate('MainWindow', "打开输出目录"))
        self.rightWidget_layout.addWidget(chkOutputButton, self.rightWidget_layout.rowCount(), 0, 1, 3)
        Function_SetURL(
            button = chkOutputButton,
            url = outputRootEdit,
            buttonTooltip = "Click to open",
            createIfNotExist = True
        )

    def setExecutor(self,
        consoleWidget: QWidget,
        method: object,
        paramTargets: list,
        successEvents: list
    ):
        self.executeButton.setText(QCA.translate('MainWindow', "执行"))
        self.terminateButton.setText(QCA.translate('MainWindow', "终止"))
        def _findParamWidget(paramTarget):
            if isinstance(paramTarget, QFrame):
                for type in (QLineEdit, QComboBox, QCheckBox, QSpinBox, QDoubleSpinBox, QSlider, QTextBrowser, QTextEdit, QTableView):
                    target = QFunc.findChild(paramTarget, type)
                    if target is not None:
                        return target
            return paramTarget
        Function_SetMethodExecutor(self,
            executeButton = self.executeButton,
            terminateButton = self.terminateButton,
            progressBar = self.progressBar,
            consoleWidget = consoleWidget,
            method = method,
            paramTargets = [_findParamWidget(paramTarget) for paramTarget in paramTargets], #paramTargets = list(self.paramWidgets.keys()),
            emptyAllowed = [paramWidget for paramWidget in self.paramWidgets.keys() if self.paramWidgets[paramWidget] == True],
            successEvents = successEvents
        )


class ToolPage(QWidget):
    """
    """
    def __init__(self, parent = None):
        super().__init__(parent)

        navigationArea = QWidget()
        navigationArea.setMinimumHeight(60)
        navigationArea.setStyleSheet("""
            QWidget {
                border-width: 0px 0px 3px 0px;
                border-style: solid;
                border-bottom-color: rgba(123, 123, 123, 123);
            }
        """)
        self.navigationAreaLayout = QHBoxLayout(navigationArea)
        self.navigationAreaLayout.setSpacing(0)
        self.navigationAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.navigationAreaLayout.addItem(self.horizontalSpacer)
        self.helpButton = QPushButton()
        self.helpButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.helpButton.setStyleSheet("""
            QPushButton {
                image-position: center;
                image: url(:/Button_Icon/images/icons/Question.png);
                padding: 18px;
                background-color: transparent;
                border-width: 0px;
                border-style: solid;
            }
            QPushButton:hover {
                background-color: rgba(201, 210, 222, 33);
            }
        """)
        self.navigationAreaLayout.addWidget(self.helpButton)

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(21)
        layout.setContentsMargins(21, 12, 21, 12)
        layout.addWidget(navigationArea)
        layout.addWidget(self.stackedWidget)

    def addSubPage(self,
        title, subPage
    ):
        self.stackedWidget.addWidget(subPage)
        navigationButton = NavigationButton()
        navigationButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        navigationButton.setText(title)
        navigationButton.setHorizontal(True)
        navigationButton.setAutoExclusive(True)
        navigationButton.clicked.connect(
            lambda: Function_AnimateStackedWidget(
                stackedWidget = self.stackedWidget,
                target = subPage
            )
        )
        self.navigationAreaLayout.insertWidget(self.navigationAreaLayout.indexOf(self.horizontalSpacer), navigationButton)
        navigationButton.setChecked(True) if self.stackedWidget.indexOf(subPage) == 0 else None

    def setHelpBtnEvent(self,
        event
    ):
        self.helpButton.clicked.connect(event)

##############################################################################################################################