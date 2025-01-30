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
    Download = Signal(tuple)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.setIndexHeaderVisible(False)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.Clipboard = QApplication.instance().clipboard()

    def setHorizontalHeaderLabels(self, headers: list):
        self.HorizontalHeaderLabels = headers
        self.ColumnCount = len(headers)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def addRow(self, param: tuple):
        ModelName, ModelType, ModelSize, ModelDate, DownloadParam = param

        RowHeight = 36
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        Label_ModelName = LabelBase()
        QFunc.setText(Label_ModelName, ModelName)
        ColumnLayout_ModelName = QHBoxLayout()
        SetColumnLayout(ColumnLayout_ModelName)
        ColumnLayout_ModelName.addWidget(Label_ModelName)

        Label_ModelType = LabelBase()
        QFunc.setText(Label_ModelType, ModelType)
        ColumnLayout_ModelType = QHBoxLayout()
        SetColumnLayout(ColumnLayout_ModelType)
        ColumnLayout_ModelType.addWidget(Label_ModelType)

        Label_ModelSize = LabelBase()
        QFunc.setText(Label_ModelSize, ModelSize)
        ColumnLayout_ModelSize = QHBoxLayout()
        SetColumnLayout(ColumnLayout_ModelSize)
        ColumnLayout_ModelSize.addWidget(Label_ModelSize)

        Label_ModelDate = LabelBase()
        QFunc.setText(Label_ModelDate, ModelDate)
        ColumnLayout_ModelDate = QHBoxLayout()
        SetColumnLayout(ColumnLayout_ModelDate)
        ColumnLayout_ModelDate.addWidget(Label_ModelDate)

        stackedWidget = QStackedWidget()
        stackedWidget.setContentsMargins(0, 0, 0, 0)
        OpenButton = ButtonBase()
        OpenButton.setBorderless(True)
        OpenButton.setTransparent(True)
        OpenButton.setIcon(IconBase.OpenedFolder)
        OpenButton.clicked.connect(lambda: QFunc.openURL(DownloadParam if isinstance(DownloadParam, str) else DownloadParam[1]))
        DownloadButton = ButtonBase()
        DownloadButton.setBorderless(True)
        DownloadButton.setTransparent(True)
        DownloadButton.setIcon(IconBase.Download)
        DownloadButton.clicked.connect(lambda: self.Download.emit(DownloadParam) if isinstance(DownloadParam, tuple) else None)
        DownloadButton.clicked.connect(lambda: stackedWidget.setCurrentWidget(OpenButton))
        stackedWidget.addWidget(OpenButton)
        stackedWidget.addWidget(DownloadButton)
        stackedWidget.setCurrentWidget(OpenButton) if isinstance(DownloadParam, str) else stackedWidget.setCurrentWidget(DownloadButton)
        CopyButton = ButtonBase()
        CopyButton.setBorderless(True)
        CopyButton.setTransparent(True)
        CopyButton.setIcon(IconBase.Clipboard)
        CopyButton.clicked.connect(lambda: self.Clipboard.setText(DownloadParam[0]) if isinstance(DownloadParam, tuple) else None)
        CopyButton.clicked.connect(lambda: MessageBoxBase.pop(windowTitle = "Tip", text = "已复制链接到剪切板"))
        QFunc.setRetainSizeWhenHidden(CopyButton)
        CopyButton.hide() if stackedWidget.currentWidget() == OpenButton else None
        stackedWidget.currentChanged.connect(lambda: CopyButton.hide() if stackedWidget.currentWidget() == OpenButton else None)
        ColumnLayout_Management = QHBoxLayout()
        SetColumnLayout(ColumnLayout_Management)
        ColumnLayout_Management.addWidget(stackedWidget)
        ColumnLayout_Management.addWidget(CopyButton)

        super().addRow(
            [ColumnLayout_ModelName, ColumnLayout_ModelType, ColumnLayout_ModelSize, ColumnLayout_ModelDate, ColumnLayout_Management],
            [QHeaderView.Stretch, QHeaderView.Interactive, QHeaderView.Interactive, QHeaderView.Stretch, QHeaderView.Fixed],
            [None, None, None, None, 2 * RowHeight],
            RowHeight
        )

    def setValue(self, params: list = [['name', 'type', 'size', 'date', 'url'], ]):
        self.clearRows()
        super().setColumnCount(self.columnCount())
        super().setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        for param in params:
            QApplication.instance().processEvents()
            self.addRow(param)


class Table_EditAudioSpeaker(TableBase):
    '''
    '''
    ValueChanged = Signal(dict)

    fileType = None

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.setIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.model().dataChanged.connect(
            lambda: self.ValueChanged.emit(self.getValue())
        )

    def setHorizontalHeaderLabels(self, headers: list):
        self.HorizontalHeaderLabels = headers
        self.ColumnCount = len(headers)

    def setStyleSheet(self, styleSheet: str):
        super().setStyleSheet(styleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def addRow(self, param: Optional[tuple] = None):
        RowHeight = 30
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        LineEdit0 = LineEditBase()
        LineEdit0.setBorderless(True)
        LineEdit0.setTransparent(True)
        QFunc.setText(LineEdit0, param[0] if param else '', setPlaceholderText = True)
        LineEdit0.textChanged.connect(
            lambda: self.ValueChanged.emit(self.getValue())
        )
        Column0Layout = QHBoxLayout()
        SetColumnLayout(Column0Layout)
        Column0Layout.addWidget(LineEdit0)

        LineEdit1 = LineEditBase()
        LineEdit1.setBorderless(True)
        LineEdit1.setTransparent(True)
        LineEdit1.setFileDialog(FileDialogMode.SelectFile, self.fileType)
        QFunc.setText(LineEdit1, param[1] if param else '', setPlaceholderText = True)
        LineEdit1.textChanged.connect(
            lambda: self.ValueChanged.emit(self.getValue())
        )
        Column1Layout = QHBoxLayout()
        SetColumnLayout(Column1Layout)
        Column1Layout.addWidget(LineEdit1)

        AddButton = ButtonBase()
        AddButton.setBorderless(True)
        AddButton.setTransparent(True)
        AddButton.setText("+")
        AddButton.clicked.connect(lambda: self.selectOuterRow(AddButton), Qt.QueuedConnection)
        AddButton.clicked.connect(self.addRow, Qt.QueuedConnection)
        DelButton = ButtonBase()
        DelButton.setBorderless(True)
        DelButton.setTransparent(True)
        DelButton.setText("-")
        DelButton.clicked.connect(lambda: self.selectOuterRow(DelButton), Qt.QueuedConnection)
        DelButton.clicked.connect(self.delRow, Qt.QueuedConnection)
        Column2Layout = QHBoxLayout()
        SetColumnLayout(Column2Layout)
        Column2Layout.addWidget(AddButton)
        Column2Layout.addWidget(DelButton)

        super().addRow(
            [Column0Layout, Column1Layout, Column2Layout],
            [QHeaderView.ResizeToContents, QHeaderView.Stretch, QHeaderView.Fixed],
            [None, None, 2 * RowHeight],
            RowHeight
        )

    def setValue(self, params: dict = {'%Speaker%': '%Path%'}):
        self.clearRows()
        super().setColumnCount(self.columnCount())
        super().setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        for Key, Value in (params if isinstance(params, dict) else (eval(params) if not (params is None or len(params) == 0) else {'': ''})).items():
            QApplication.instance().processEvents()
            param = (Key, Value)
            #Index = next((i for i, key in enumerate(ParamDict) if key == Key), None)
            self.addRow(param)

    def setFileDialog(self, fileType: Optional[str] = None):
        '''
        for RowCount in range(self.rowCount()):
            self.cellWidget(RowCount, 1).findChild(LineEditBase).setFileDialog(FileDialogMode.SelectFile, fileType)
        '''
        self.fileType = fileType

    def getValue(self):
        ValueDict = {}
        for RowCount in range(self.rowCount()):
            try:
                Key = QFunc.getText(self.cellWidget(RowCount, 0).findChild(QLineEdit))
                Value = QFunc.getText(self.cellWidget(RowCount, 1).findChild(QLineEdit))
                ValueDict[Key] = Value
            except:
                pass
        return ValueDict


class Table_VPRResult(TableBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.setIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def setHorizontalHeaderLabels(self, headers: list):
        self.HorizontalHeaderLabels = headers
        self.ColumnCount = len(headers)

    def setStyleSheet(self, styleSheet: str):
        super().setStyleSheet(styleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def addRow(self, param: tuple, comboItems: list):
        RowHeight = 30
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        Label0 = LabelBase()
        QFunc.setText(Label0, param[0])
        Column0Layout = QHBoxLayout()
        SetColumnLayout(Column0Layout)
        Column0Layout.addWidget(Label0)

        ComboBox = ComboBoxBase()
        ComboBox.setBorderless(True)
        ComboBox.setTransparent(True)
        ComboBox.addItems(comboItems)
        ComboBox.setCurrentText(param[1])
        Column1Layout = QHBoxLayout()
        SetColumnLayout(Column1Layout)
        Column1Layout.addWidget(ComboBox)

        Label2 = LabelBase()
        QFunc.setText(Label2, param[2])
        Column2Layout = QHBoxLayout()
        SetColumnLayout(Column2Layout)
        Column2Layout.addWidget(Label2)

        PlayerWidget = MediaPlayerBase()
        PlayerWidget.setBorderless(True)
        PlayerWidget.setTransparent(True)
        PlayerWidget.setMediaPlayer(param[0])
        PlayerWidget.layout().setContentsMargins(6, 6, 6, 6)
        PlayerWidget.Slider.hide()
        Column3Layout = QHBoxLayout()
        SetColumnLayout(Column3Layout)
        Column3Layout.addWidget(PlayerWidget)

        DelButton = ButtonBase()
        DelButton.setBorderless(True)
        DelButton.setTransparent(True)
        DelButton.setText("删除")
        DelButton.clicked.connect(
            lambda: MessageBoxBase.pop(None,
                QMessageBox.Question, "Ask",
                "确认删除该行？",
                QMessageBox.Yes|QMessageBox.No,
                {
                    QMessageBox.Yes: lambda: (
                        self.selectOuterRow(DelButton),
                        self.delRow()
                    )
                }
            )
        )
        Column4Layout = QHBoxLayout()
        SetColumnLayout(Column4Layout)
        Column4Layout.addWidget(DelButton)

        super().addRow(
            [Column0Layout, Column1Layout, Column2Layout, Column3Layout, Column4Layout],
            [QHeaderView.Stretch, QHeaderView.Stretch, QHeaderView.Stretch, QHeaderView.Fixed, QHeaderView.Fixed],
            [None, None, None, RowHeight, 1.5 * RowHeight],
            RowHeight
        )

    def setValue(self, params: list = [['%Path%', '%Namex%', '%Sim%'], ], comboItems: Optional[list] = ['%Name1%', ]):
        self.clearRows()
        super().setColumnCount(self.columnCount())
        super().setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        if comboItems is None:
            comboItems = []
            for param in params:
                comboItem = param[1]
                comboItems.append(comboItem) if comboItem not in comboItems else None
        for param in params:
            QApplication.instance().processEvents()
            self.addRow(param, comboItems + [''])

    def getValue(self):
        ValueDict = {}
        for RowCount in range(self.rowCount()):
            try:
                Key = QFunc.getText(self.cellWidget(RowCount, 0).findChild(LabelBase))
                Value = self.cellWidget(RowCount, 1).findChild(ComboBoxBase).currentText()
                ValueDict[Key] = Value
            except:
                pass
        return ValueDict


class Table_ASRResult(TableBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.setIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def setHorizontalHeaderLabels(self, headers: list):
        self.HorizontalHeaderLabels = headers
        self.ColumnCount = len(headers)

    def setStyleSheet(self, styleSheet: str):
        super().setStyleSheet(styleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def addRow(self, param: tuple):
        RowHeight = 30
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        Label0 = LabelBase()
        QFunc.setText(Label0, param[0])
        Column0Layout = QHBoxLayout()
        SetColumnLayout(Column0Layout)
        Column0Layout.addWidget(Label0)

        LineEdit = LineEditBase()
        LineEdit.setBorderless(True)
        LineEdit.setTransparent(True)
        QFunc.setText(LineEdit, param[1], setPlaceholderText = True)
        Column1Layout = QHBoxLayout()
        SetColumnLayout(Column1Layout)
        Column1Layout.addWidget(LineEdit)

        PlayerWidget = MediaPlayerBase()
        PlayerWidget.setBorderless(True)
        PlayerWidget.setTransparent(True)
        PlayerWidget.setMediaPlayer(param[0])
        PlayerWidget.layout().setContentsMargins(6, 6, 6, 6)
        PlayerWidget.Slider.hide()
        Column2Layout = QHBoxLayout()
        SetColumnLayout(Column2Layout)
        Column2Layout.addWidget(PlayerWidget)

        super().addRow(
            [Column0Layout, Column1Layout, Column2Layout],
            [QHeaderView.Stretch, QHeaderView.Stretch, QHeaderView.Fixed],
            [None, None, RowHeight],
            RowHeight
        )

    def setValue(self, params: dict = {'%Path%': '%Transcription%'}):
        self.clearRows()
        super().setColumnCount(self.columnCount())
        super().setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        for Key, Value in (params if isinstance(params, dict) else eval(params)).items():
            QApplication.instance().processEvents()
            param = (Key, Value)
            self.addRow(param)

    def getValue(self):
        ValueDict = {}
        for RowCount in range(self.rowCount()):
            try:
                Key = QFunc.getText(self.cellWidget(RowCount, 0).findChild(LabelBase))
                Value = QFunc.getText(self.cellWidget(RowCount, 1).findChild(QLineEdit))
                ValueDict[Key] = Value
            except:
                pass
        return ValueDict


class Table_DATResult(TableBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.setIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def setHorizontalHeaderLabels(self, headers: list):
        self.HorizontalHeaderLabels = headers
        self.ColumnCount = len(headers)

    def setStyleSheet(self, styleSheet: str):
        super().setStyleSheet(styleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def addRow(self, param: tuple):
        RowHeight = 30
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        LineEdit = LineEditBase()
        LineEdit.setBorderless(True)
        LineEdit.setTransparent(True)
        QFunc.setText(LineEdit, param[1], setPlaceholderText = True)
        Column0Layout = QHBoxLayout()
        SetColumnLayout(Column0Layout)
        Column0Layout.addWidget(LineEdit)

        PlayerWidget = MediaPlayerBase()
        PlayerWidget.setBorderless(True)
        PlayerWidget.setTransparent(True)
        PlayerWidget.setMediaPlayer(param[0])
        PlayerWidget.layout().setContentsMargins(6, 6, 6, 6)
        PlayerWidget.Slider.hide()
        Column1Layout = QHBoxLayout()
        SetColumnLayout(Column1Layout)
        Column1Layout.addWidget(PlayerWidget)

        super().addRow(
            [Column0Layout, Column1Layout],
            [QHeaderView.Stretch, QHeaderView.Fixed],
            [None, RowHeight],
            RowHeight
        )

    def setValue(self, params: dict = {'%Path%': '%Data%'}):
        self.clearRows()
        super().setColumnCount(self.columnCount())
        super().setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        for Key, Value in (params if isinstance(params, dict) else eval(params)).items():
            QApplication.instance().processEvents()
            param = (Key, Value)
            self.addRow(param)

    def getValue(self):
        ValueList = []
        for RowCount in range(self.rowCount()):
            try:
                Value = QFunc.getText(self.cellWidget(RowCount, 0).findChild(QLineEdit))
                ValueList.append(Value)
            except:
                pass
        return ValueList

##############################################################################################################################