from typing import Type, Optional
from PyEasyUtils import setRichText
from PySide6.QtCore import Qt, QRect, QSize, SignalInstance
from PySide6.QtWidgets import *
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets.Common import FileDialogMode
from QEasyWidgets.Components import *

from .common import ComponentFlag, SubPage, Page
#from assets import *
from functions import *

##############################################################################################################################

class SubSettingsPage(SubPage):
    """
    """
    def __init__(self, parent = None, paramsManager: ParamsManager = ...):
        super().__init__(parent)

        self.paramsManager = paramsManager

        layout = self.cleanLayout()
        layout.addWidget(self.contentWidget, 0, 0)

    def _setLabelText(self, label, text, size = 12):
        QFunc.setText(
            widget = label,
            text = setRichText(
                size = size,
                text = text,
            )
        )

    def _setButtonMenu(self, menuButton: MenuButton, widget):
        menuButton.setMenu(
            actionEvents = {
                self.tr("重置"): lambda: self.paramsManager.resetParam(widget),
                self.tr("复制"): lambda: QApplication.clipboard().setText(str(Function_GetParam(widget))),
            }
        )

    def _addToChildFrame(self, label: LabelBase, inputWidget: QWidget, menuButton: MenuButton):
        label.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed))
        inputWidget.setMinimumSize(QSize(123, 30))
        menuButton.setFixedSize(QSize(27, 27))
        # 
        childFrame = QFrame()
        childFrame.setMinimumSize(QSize(0, 90))
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
        childFrame_layout.addWidget(label, 0, 0)
        childFrame_layout.addWidget(inputWidget, 0, 1, Qt.AlignRight) if not isinstance(inputWidget, QTableView) else childFrame_layout.addWidget(inputWidget, 1, 0)
        childFrame_layout.addWidget(menuButton, 0, 2, Qt.AlignCenter)
        return childFrame

    def addLineEditFrame(self,
        rootItemText: Optional[str] = None, toolBoxText: Optional[str] = None, text: str = ..., toolTip: Optional[str] = None,
        fileDialogMode: Optional[FileDialogMode] = None, fileType: Optional[str] = None, directory: Optional[str] = None,
        section: str = ..., option: str = ..., defaultValue: str = ..., placeholderText: str = "", paramsManager: Optional[ParamsManager] = None,
    ):
        label = LabelBase(self)
        lineEdit = LineEditBase(self)
        button = MenuButton()
        self._setLabelText(label, text)
        lineEdit.setToolTip(toolTip) if toolTip is not None else None
        lineEdit.setFileDialog(fileDialogMode, fileType, directory) if fileDialogMode is not None else None
        (paramsManager or self.paramsManager).setParam(lineEdit, section, option, defaultValue, setPlaceholderText = True, placeholderText = placeholderText)
        self._setButtonMenu(button, lineEdit)
        containerDict = self._addToContainer(rootItemText, toolBoxText, label, lineEdit, button)
        return {
            ComponentFlag.LineEdit: lineEdit,
            **containerDict
        }

    def addCheckBoxFrame(self,
        rootItemText: Optional[str] = None, toolBoxText: Optional[str] = None, text: str = ..., toolTip: Optional[str] = None,
        section: str = ..., option: str = ..., defaultValue: str = ..., paramsManager: Optional[ParamsManager] = None,
    ):
        label = LabelBase()
        checkBox = CheckBoxBase(self)
        button = MenuButton()
        self._setLabelText(label, text)
        Function_ConfigureCheckBox(checkBox, checkedText = self.tr("已启动"), uncheckedText = self.tr("未启动"))
        checkBox.setToolTip(toolTip) if toolTip is not None else None
        (paramsManager or self.paramsManager).setParam(checkBox, section, option, defaultValue)
        self._setButtonMenu(button, checkBox)
        containerDict = self._addToContainer(rootItemText, toolBoxText, label, checkBox, button)
        return {
            ComponentFlag.CheckBox: checkBox,
            **containerDict
        }

    def addComboBoxFrame(self,
        rootItemText: Optional[str] = None, toolBoxText: Optional[str] = None, text: str = ..., toolTip: Optional[str] = None,
        items: list = ..., currentIndex: Optional[int] = None,
        signal: Optional[SignalInstance] = None, textDict: Optional[dict] = None,
        section: str = ..., option: str = ..., defaultValue: str = ..., paramsManager: Optional[ParamsManager] = None,
    ):
        label = LabelBase(self)
        comboBox = ComboBoxBase(self)
        button = MenuButton()
        self._setLabelText(label, text)
        comboBox.setToolTip(toolTip) if toolTip is not None else None
        comboBox.addItems(items)
        if signal and textDict:
            signal.connect(
                lambda val: comboBox.setCurrentText(
                    EasyUtils.findKey(textDict, val)
                ) if EasyUtils.findKey(textDict, val) != comboBox.currentText() else None
            )
            comboBox.currentIndexChanged.connect(
                lambda: (
                    (paramsManager or self.paramsManager).config.editConfig(
                        section, option, textDict.get(comboBox.currentText())
                    ),
                    signal.emit(
                        textDict.get(comboBox.currentText())
                    )
                )
            )
        else:
            (paramsManager or self.paramsManager).setParam(comboBox, section, option, defaultValue)
        comboBox.setCurrentIndex(currentIndex) if currentIndex is not None else None
        self._setButtonMenu(button, comboBox)
        containerDict = self._addToContainer(rootItemText, toolBoxText, label, comboBox, button)
        return {
            ComponentFlag.ComboBox: comboBox,
            **containerDict
        }


class SettingsPage(Page):
    """
    """
    def __init__(self, parent = None):
        super().__init__(parent)

##############################################################################################################################