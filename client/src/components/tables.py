from typing import Optional
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import *
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets import IconBase
from QEasyWidgets.Common import FileDialogMode
from QEasyWidgets.Components import *
from QEasyWidgets.Windows import MessageBoxBase

from assets import *

##############################################################################################################################

class Table_ViewModels(TableBase):
    '''
    '''
    download = Signal(tuple)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.setIndexHeaderVisible(False)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setHorizontalHeaderLabels([self.tr("名字"), self.tr("类型"), self.tr("大小"), self.tr("日期"), self.tr("操作")])

        self.clipboard = QApplication.instance().clipboard()

    def addRow(self, param: tuple):
        modelName, modelType, modelSize, modelDate, downloadParam = param

        rowHeight = 36
        def _setColumnLayout(columnLayout):
            columnLayout.setContentsMargins(0, 0, 0, 0)
            columnLayout.setSpacing(0)

        label_modelName = LabelBase()
        QFunc.setText(label_modelName, modelName)
        columnLayout_modelName = QHBoxLayout()
        _setColumnLayout(columnLayout_modelName)
        columnLayout_modelName.addWidget(label_modelName)

        label_modelType = LabelBase()
        QFunc.setText(label_modelType, modelType)
        columnLayout_modelType = QHBoxLayout()
        _setColumnLayout(columnLayout_modelType)
        columnLayout_modelType.addWidget(label_modelType)

        label_modelSize = LabelBase()
        QFunc.setText(label_modelSize, modelSize)
        columnLayout_modelSize = QHBoxLayout()
        _setColumnLayout(columnLayout_modelSize)
        columnLayout_modelSize.addWidget(label_modelSize)

        label_modelDate = LabelBase()
        QFunc.setText(label_modelDate, modelDate)
        columnLayout_modelDate = QHBoxLayout()
        _setColumnLayout(columnLayout_modelDate)
        columnLayout_modelDate.addWidget(label_modelDate)

        stackedWidget = QStackedWidget()
        stackedWidget.setContentsMargins(0, 0, 0, 0)
        openButton = ButtonBase()
        openButton.setBorderless(True)
        openButton.setTransparent(True)
        openButton.setIcon(IconBase.OpenedFolder)
        openButton.clicked.connect(lambda: QFunc.openURL(downloadParam if isinstance(downloadParam, str) else downloadParam[1]))
        downloadButton = ButtonBase()
        downloadButton.setBorderless(True)
        downloadButton.setTransparent(True)
        downloadButton.setIcon(IconBase.Download)
        downloadButton.clicked.connect(lambda: self.download.emit(downloadParam) if isinstance(downloadParam, tuple) else None)
        downloadButton.clicked.connect(lambda: stackedWidget.setCurrentWidget(openButton))
        stackedWidget.addWidget(openButton)
        stackedWidget.addWidget(downloadButton)
        stackedWidget.setCurrentWidget(openButton) if isinstance(downloadParam, str) else stackedWidget.setCurrentWidget(downloadButton)
        copyButton = ButtonBase()
        copyButton.setBorderless(True)
        copyButton.setTransparent(True)
        copyButton.setIcon(IconBase.Clipboard)
        copyButton.clicked.connect(lambda: self.clipboard.setText(downloadParam[0]) if isinstance(downloadParam, tuple) else None)
        copyButton.clicked.connect(lambda: MessageBoxBase.pop(windowTitle = "Tip", text = "已复制链接到剪切板"))
        QFunc.setRetainSizeWhenHidden(copyButton)
        copyButton.hide() if stackedWidget.currentWidget() == openButton else None
        stackedWidget.currentChanged.connect(lambda: copyButton.hide() if stackedWidget.currentWidget() == openButton else None)
        columnLayout_management = QHBoxLayout()
        _setColumnLayout(columnLayout_management)
        columnLayout_management.addWidget(stackedWidget)
        columnLayout_management.addWidget(copyButton)

        super().addRow(
            [columnLayout_modelName, columnLayout_modelType, columnLayout_modelSize, columnLayout_modelDate, columnLayout_management],
            [QHeaderView.Stretch, QHeaderView.Interactive, QHeaderView.Interactive, QHeaderView.Stretch, QHeaderView.Fixed],
            [None, None, None, None, 2 * rowHeight],
            rowHeight
        )

    def setValue(self, params: list = [['name', 'type', 'size', 'date', 'url'], ]):
        self.clearRows()
        super().setColumnCount(self.columnCount())
        for param in params:
            QApplication.instance().processEvents()
            self.addRow(param)


class Table_EditAudioSpeaker(TableBase):
    '''
    '''
    valueChanged = Signal(dict)

    fileType = None

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.setIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.model().dataChanged.connect(
            lambda: self.valueChanged.emit(self.getValue())
        )

    def setStyleSheet(self, styleSheet: str):
        super().setStyleSheet(styleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def addRow(self, param: Optional[tuple] = None):
        rowHeight = 30
        def _setColumnLayout(columnLayout):
            columnLayout.setContentsMargins(0, 0, 0, 0)
            columnLayout.setSpacing(0)

        lineEdit0 = LineEditBase()
        lineEdit0.setBorderless(True)
        lineEdit0.setTransparent(True)
        lineEdit0.textChanged.connect(
            lambda: self.valueChanged.emit(self.getValue())
        )
        QFunc.setText(lineEdit0, param[0] if param else '', setPlaceholderText = True)
        column0Layout = QHBoxLayout()
        _setColumnLayout(column0Layout)
        column0Layout.addWidget(lineEdit0)

        lineEdit1 = LineEditBase()
        lineEdit1.setBorderless(True)
        lineEdit1.setTransparent(True)
        lineEdit1.setFileDialog(FileDialogMode.SelectFile, self.fileType)
        lineEdit1.textChanged.connect(
            lambda: self.valueChanged.emit(self.getValue())
        )
        QFunc.setText(lineEdit1, param[1] if param else '', setPlaceholderText = True)
        column1Layout = QHBoxLayout()
        _setColumnLayout(column1Layout)
        column1Layout.addWidget(lineEdit1)

        addButton = ButtonBase()
        addButton.setBorderless(True)
        addButton.setTransparent(True)
        addButton.setText("+")
        addButton.clicked.connect(lambda: self.selectOuterRow(addButton), Qt.QueuedConnection)
        addButton.clicked.connect(self.addRow, Qt.QueuedConnection)
        delButton = ButtonBase()
        delButton.setBorderless(True)
        delButton.setTransparent(True)
        delButton.setText("-")
        delButton.clicked.connect(lambda: self.selectOuterRow(delButton), Qt.QueuedConnection)
        delButton.clicked.connect(self.delRow, Qt.QueuedConnection)
        column2Layout = QHBoxLayout()
        _setColumnLayout(column2Layout)
        column2Layout.addWidget(addButton)
        column2Layout.addWidget(delButton)

        super().addRow(
            [column0Layout, column1Layout, column2Layout],
            [QHeaderView.ResizeToContents, QHeaderView.Stretch, QHeaderView.Fixed],
            [None, None, 2 * rowHeight],
            rowHeight
        )

    def setValue(self, params: dict = {'%Speaker%': '%Path%'}):
        self.clearRows()
        super().setColumnCount(self.columnCount())
        for key, value in (params if isinstance(params, dict) else (eval(params) if not (params is None or len(params) == 0) else {'': ''})).items():
            QApplication.instance().processEvents()
            param = (key, value)
            #Index = next((i for i, key in enumerate(ParamDict) if key == key), None)
            self.addRow(param)

    def setFileDialog(self, fileType: Optional[str] = None):
        '''
        for rowCount in range(self.rowCount()):
            self.cellWidget(rowCount, 1).findChild(LineEditBase).setFileDialog(FileDialogMode.SelectFile, fileType)
        '''
        self.fileType = fileType

    def getValue(self):
        valueDict = {}
        for rowCount in range(self.rowCount()):
            try:
                key = QFunc.getText(self.cellWidget(rowCount, 0).findChild(QLineEdit))
                value = QFunc.getText(self.cellWidget(rowCount, 1).findChild(QLineEdit))
                valueDict[key] = value
            except:
                pass
        return valueDict


class Table_VPRResult(TableBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.setIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.setHorizontalHeaderLabels([self.tr("音频路径"), self.tr("人物姓名"), self.tr("相似度"), self.tr("播放"), self.tr("操作")])

    def setStyleSheet(self, styleSheet: str):
        super().setStyleSheet(styleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def addRow(self, param: tuple, comboItems: list):
        rowHeight = 30
        def _setColumnLayout(columnLayout):
            columnLayout.setContentsMargins(0, 0, 0, 0)
            columnLayout.setSpacing(0)

        label0 = LabelBase()
        QFunc.setText(label0, param[0])
        column0Layout = QHBoxLayout()
        _setColumnLayout(column0Layout)
        column0Layout.addWidget(label0)

        comboBox = ComboBoxBase()
        comboBox.setBorderless(True)
        comboBox.setTransparent(True)
        comboBox.addItems(comboItems)
        comboBox.setCurrentText(param[1])
        column1Layout = QHBoxLayout()
        _setColumnLayout(column1Layout)
        column1Layout.addWidget(comboBox)

        label2 = LabelBase()
        QFunc.setText(label2, param[2])
        column2Layout = QHBoxLayout()
        _setColumnLayout(column2Layout)
        column2Layout.addWidget(label2)

        playerWidget = MediaPlayerBase()
        playerWidget.setBorderless(True)
        playerWidget.setTransparent(True)
        playerWidget.setMediaPlayer(param[0])
        playerWidget.layout().setContentsMargins(6, 6, 6, 6)
        playerWidget.Slider.hide()
        column3Layout = QHBoxLayout()
        _setColumnLayout(column3Layout)
        column3Layout.addWidget(playerWidget)

        delButton = ButtonBase()
        delButton.setBorderless(True)
        delButton.setTransparent(True)
        delButton.setText("删除")
        delButton.clicked.connect(
            lambda: MessageBoxBase.pop(None,
                QMessageBox.Question, "Ask",
                "确认删除该行？", None,
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        self.selectOuterRow(delButton),
                        self.delRow()
                    )
                }
            )
        )
        column4Layout = QHBoxLayout()
        _setColumnLayout(column4Layout)
        column4Layout.addWidget(delButton)

        super().addRow(
            [column0Layout, column1Layout, column2Layout, column3Layout, column4Layout],
            [QHeaderView.Stretch, QHeaderView.Stretch, QHeaderView.Stretch, QHeaderView.Fixed, QHeaderView.Fixed],
            [None, None, None, rowHeight, 1.5 * rowHeight],
            rowHeight
        )

    def setValue(self, params: list = [['%Path%', '%Namex%', '%Sim%'], ], comboItems: Optional[list] = ['%Name1%', ]):
        self.clearRows()
        super().setColumnCount(self.columnCount())
        if comboItems is None:
            comboItems = []
            for param in params:
                comboItem = param[1]
                comboItems.append(comboItem) if comboItem not in comboItems else None
        for param in params:
            QApplication.instance().processEvents()
            self.addRow(param, comboItems + [''])

    def getValue(self):
        valueDict = {}
        for rowCount in range(self.rowCount()):
            try:
                key = QFunc.getText(self.cellWidget(rowCount, 0).findChild(LabelBase))
                value = self.cellWidget(rowCount, 1).findChild(ComboBoxBase).currentText()
                valueDict[key] = value
            except:
                pass
        return valueDict


class Table_ASRResult(TableBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.setIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.setHorizontalHeaderLabels([self.tr("音频路径"), self.tr("音频内容"), self.tr("播放")])

    def setStyleSheet(self, styleSheet: str):
        super().setStyleSheet(styleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def addRow(self, param: tuple):
        rowHeight = 30
        def _setColumnLayout(columnLayout):
            columnLayout.setContentsMargins(0, 0, 0, 0)
            columnLayout.setSpacing(0)

        label0 = LabelBase()
        QFunc.setText(label0, param[0])
        column0Layout = QHBoxLayout()
        _setColumnLayout(column0Layout)
        column0Layout.addWidget(label0)

        lineEdit = LineEditBase()
        lineEdit.setBorderless(True)
        lineEdit.setTransparent(True)
        QFunc.setText(lineEdit, param[1], setPlaceholderText = True)
        column1Layout = QHBoxLayout()
        _setColumnLayout(column1Layout)
        column1Layout.addWidget(lineEdit)

        playerWidget = MediaPlayerBase()
        playerWidget.setBorderless(True)
        playerWidget.setTransparent(True)
        playerWidget.setMediaPlayer(param[0])
        playerWidget.layout().setContentsMargins(6, 6, 6, 6)
        playerWidget.Slider.hide()
        column2Layout = QHBoxLayout()
        _setColumnLayout(column2Layout)
        column2Layout.addWidget(playerWidget)

        super().addRow(
            [column0Layout, column1Layout, column2Layout],
            [QHeaderView.Stretch, QHeaderView.Stretch, QHeaderView.Fixed],
            [None, None, rowHeight],
            rowHeight
        )

    def setValue(self, params: dict = {'%Path%': '%Transcription%'}):
        self.clearRows()
        super().setColumnCount(self.columnCount())
        for key, value in (params if isinstance(params, dict) else eval(params)).items():
            QApplication.instance().processEvents()
            param = (key, value)
            self.addRow(param)

    def getValue(self):
        valueDict = {}
        for rowCount in range(self.rowCount()):
            try:
                key = QFunc.getText(self.cellWidget(rowCount, 0).findChild(LabelBase))
                value = QFunc.getText(self.cellWidget(rowCount, 1).findChild(QLineEdit))
                valueDict[key] = value
            except:
                pass
        return valueDict


class Table_DATResult(TableBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.setIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.setHorizontalHeaderLabels([self.tr("数据文本"), self.tr("播放")])

    def setStyleSheet(self, styleSheet: str):
        super().setStyleSheet(styleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def addRow(self, param: tuple):
        rowHeight = 30
        def _setColumnLayout(columnLayout):
            columnLayout.setContentsMargins(0, 0, 0, 0)
            columnLayout.setSpacing(0)

        lineEdit = LineEditBase()
        lineEdit.setBorderless(True)
        lineEdit.setTransparent(True)
        QFunc.setText(lineEdit, param[1], setPlaceholderText = True)
        column0Layout = QHBoxLayout()
        _setColumnLayout(column0Layout)
        column0Layout.addWidget(lineEdit)

        playerWidget = MediaPlayerBase()
        playerWidget.setBorderless(True)
        playerWidget.setTransparent(True)
        playerWidget.setMediaPlayer(param[0])
        playerWidget.layout().setContentsMargins(6, 6, 6, 6)
        playerWidget.Slider.hide()
        column1Layout = QHBoxLayout()
        _setColumnLayout(column1Layout)
        column1Layout.addWidget(playerWidget)

        super().addRow(
            [column0Layout, column1Layout],
            [QHeaderView.Stretch, QHeaderView.Fixed],
            [None, rowHeight],
            rowHeight
        )

    def setValue(self, params: dict = {'%Path%': '%Data%'}):
        self.clearRows()
        super().setColumnCount(self.columnCount())
        for key, value in (params if isinstance(params, dict) else eval(params)).items():
            QApplication.instance().processEvents()
            param = (key, value)
            self.addRow(param)

    def getValue(self):
        valueList = []
        for rowCount in range(self.rowCount()):
            try:
                value = QFunc.getText(self.cellWidget(rowCount, 0).findChild(QLineEdit))
                valueList.append(value)
            except:
                pass
        return valueList

##############################################################################################################################