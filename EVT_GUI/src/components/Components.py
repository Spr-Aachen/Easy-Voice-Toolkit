from typing import Optional
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import *
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets import IconBase
from QEasyWidgets.Components import *
from QEasyWidgets.Windows import MessageBoxBase

from assets.Sources import *

##############################################################################################################################

class Table_ViewModels(TableBase):
    '''
    '''
    Download = Signal(tuple)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.SetIndexHeaderVisible(False)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.Clipboard = QApplication.clipboard()

    def setHorizontalHeaderLabels(self, Headers: list):
        self.HorizontalHeaderLabels = Headers
        self.ColumnCount = len(Headers)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def AddRow(self, Param: tuple):
        ModelName, ModelType, ModelSize, ModelDate, DownloadParam = Param

        RowHeight = 36
        LabelStyle = '''
        QLabel {
            background-color: transparent;
            border: none;
        }
        '''
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        Label_ModelName = QLabel()
        Label_ModelName.setStyleSheet(LabelStyle)
        QFunc.Function_SetText(Label_ModelName, ModelName)
        ColumnLayout_ModelName = QHBoxLayout()
        SetColumnLayout(ColumnLayout_ModelName)
        ColumnLayout_ModelName.addWidget(Label_ModelName)

        Label_ModelType = QLabel()
        Label_ModelType.setStyleSheet(LabelStyle)
        QFunc.Function_SetText(Label_ModelType, ModelType)
        ColumnLayout_ModelType = QHBoxLayout()
        SetColumnLayout(ColumnLayout_ModelType)
        ColumnLayout_ModelType.addWidget(Label_ModelType)

        Label_ModelSize = QLabel()
        Label_ModelSize.setStyleSheet(LabelStyle)
        QFunc.Function_SetText(Label_ModelSize, ModelSize)
        ColumnLayout_ModelSize = QHBoxLayout()
        SetColumnLayout(ColumnLayout_ModelSize)
        ColumnLayout_ModelSize.addWidget(Label_ModelSize)

        Label_ModelDate = QLabel()
        Label_ModelDate.setStyleSheet(LabelStyle)
        QFunc.Function_SetText(Label_ModelDate, ModelDate)
        ColumnLayout_ModelDate = QHBoxLayout()
        SetColumnLayout(ColumnLayout_ModelDate)
        ColumnLayout_ModelDate.addWidget(Label_ModelDate)

        StackedWidget = QStackedWidget()
        StackedWidget.setContentsMargins(0, 0, 0, 0)
        OpenButton = ButtonBase()
        OpenButton.setBorderless(True)
        OpenButton.setTransparent(True)
        OpenButton.setIcon(IconBase.OpenedFolder)
        OpenButton.clicked.connect(lambda: QFunc.Function_OpenURL(DownloadParam if isinstance(DownloadParam, str) else DownloadParam[1]))
        DownloadButton = ButtonBase()
        DownloadButton.setBorderless(True)
        DownloadButton.setTransparent(True)
        DownloadButton.setIcon(IconBase.Download)
        DownloadButton.clicked.connect(lambda: self.Download.emit(DownloadParam) if isinstance(DownloadParam, tuple) else None)
        DownloadButton.clicked.connect(lambda: StackedWidget.setCurrentWidget(OpenButton))
        StackedWidget.addWidget(OpenButton)
        StackedWidget.addWidget(DownloadButton)
        StackedWidget.setCurrentWidget(OpenButton) if isinstance(DownloadParam, str) else StackedWidget.setCurrentWidget(DownloadButton)
        CopyButton = ButtonBase()
        CopyButton.setBorderless(True)
        CopyButton.setTransparent(True)
        CopyButton.setIcon(IconBase.Clipboard)
        CopyButton.clicked.connect(lambda: self.Clipboard.setText(DownloadParam[0]) if isinstance(DownloadParam, tuple) else None)
        CopyButton.clicked.connect(lambda: MessageBoxBase.pop(WindowTitle = "Tip", Text = "已复制链接到剪切板"))
        QFunc.Function_SetRetainSizeWhenHidden(CopyButton)
        CopyButton.hide() if StackedWidget.currentWidget() == OpenButton else None
        StackedWidget.currentChanged.connect(lambda: CopyButton.hide() if StackedWidget.currentWidget() == OpenButton else None)
        ColumnLayout_Management = QHBoxLayout()
        SetColumnLayout(ColumnLayout_Management)
        ColumnLayout_Management.addWidget(StackedWidget)
        ColumnLayout_Management.addWidget(CopyButton)

        super().AddRow(
            [ColumnLayout_ModelName, ColumnLayout_ModelType, ColumnLayout_ModelSize, ColumnLayout_ModelDate, ColumnLayout_Management],
            [QHeaderView.Stretch, QHeaderView.Interactive, QHeaderView.Interactive, QHeaderView.Stretch, QHeaderView.Fixed],
            [None, None, None, None, 2 * RowHeight],
            RowHeight
        )

    def SetValue(self, Params: list = [['name', 'type', 'size', 'date', 'url'], ]):
        self.ClearRows()
        super().setColumnCount(self.columnCount())
        super().setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        for Param in Params:
            QApplication.processEvents()
            self.AddRow(Param)


class Table_EditAudioSpeaker(TableBase):
    '''
    '''
    ValueChanged = Signal(dict)

    FileType = None

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.SetIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.model().dataChanged.connect(
            lambda: self.ValueChanged.emit(self.GetValue())
        )

    def setHorizontalHeaderLabels(self, Headers: list):
        self.HorizontalHeaderLabels = Headers
        self.ColumnCount = len(Headers)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def setStyleSheet(self, StyleSheet: str):
        super().setStyleSheet(StyleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def AddRow(self, Param: Optional[tuple] = None):
        RowHeight = 30
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        LineEdit0 = LineEditBase()
        LineEdit0.setBorderless(True)
        LineEdit0.setTransparent(True)
        QFunc.Function_SetText(LineEdit0, Param[0] if Param else '', SetPlaceholderText = True)
        LineEdit0.textChanged.connect(
            lambda: self.ValueChanged.emit(self.GetValue())
        )
        Column0Layout = QHBoxLayout()
        SetColumnLayout(Column0Layout)
        Column0Layout.addWidget(LineEdit0)

        LineEdit1 = LineEditBase()
        LineEdit1.setBorderless(True)
        LineEdit1.setTransparent(True)
        LineEdit1.SetFileDialog("SelectFile", self.FileType)
        QFunc.Function_SetText(LineEdit1, Param[1] if Param else '', SetPlaceholderText = True)
        LineEdit1.textChanged.connect(
            lambda: self.ValueChanged.emit(self.GetValue())
        )
        Column1Layout = QHBoxLayout()
        SetColumnLayout(Column1Layout)
        Column1Layout.addWidget(LineEdit1)

        AddButton = ButtonBase()
        AddButton.setBorderless(True)
        AddButton.setTransparent(True)
        AddButton.setText("+")
        AddButton.clicked.connect(lambda: self.SelectOuterRow(AddButton), Qt.QueuedConnection)
        AddButton.clicked.connect(self.AddRow, Qt.QueuedConnection)
        DelButton = ButtonBase()
        DelButton.setBorderless(True)
        DelButton.setTransparent(True)
        DelButton.setText("-")
        DelButton.clicked.connect(lambda: self.SelectOuterRow(DelButton), Qt.QueuedConnection)
        DelButton.clicked.connect(self.DelRow, Qt.QueuedConnection)
        Column2Layout = QHBoxLayout()
        SetColumnLayout(Column2Layout)
        Column2Layout.addWidget(AddButton)
        Column2Layout.addWidget(DelButton)

        super().AddRow(
            [Column0Layout, Column1Layout, Column2Layout],
            [QHeaderView.ResizeToContents, QHeaderView.Stretch, QHeaderView.Fixed],
            [None, None, 2 * RowHeight],
            RowHeight
        )

    def SetValue(self, Params: dict = {'%Speaker%': '%Path%'}):
        self.ClearRows()
        super().setColumnCount(self.columnCount())
        super().setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        ParamDict = QFunc.ToIterable(Params if Params is None or len(Params) != 0 else {'': ''})
        for Key, Value in ParamDict.items():
            QApplication.processEvents()
            Param = (Key, Value)
            #Index = next((i for i, key in enumerate(ParamDict) if key == Key), None)
            self.AddRow(Param)

    def SetFileDialog(self, FileType: Optional[str] = None):
        '''
        for RowCount in range(self.rowCount()):
            self.cellWidget(RowCount, 1).findChild(LineEditBase).SetFileDialog("SelectFile", FileType)
        '''
        self.FileType = FileType

    def GetValue(self):
        ValueDict = {}
        for RowCount in range(self.rowCount()):
            try:
                Key = QFunc.Function_GetText(self.cellWidget(RowCount, 0).findChild(QLineEdit))
                Value = QFunc.Function_GetText(self.cellWidget(RowCount, 1).findChild(QLineEdit))
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
        self.SetIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def setHorizontalHeaderLabels(self, Headers: list):
        self.HorizontalHeaderLabels = Headers
        self.ColumnCount = len(Headers)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def setStyleSheet(self, StyleSheet: str):
        super().setStyleSheet(StyleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def AddRow(self, Param: tuple, ComboItems: list):
        RowHeight = 30
        LabelStyle = '''
        QLabel {
            background-color: transparent;
            border: none;
        }
        '''
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        Label0 = QLabel()
        Label0.setStyleSheet(LabelStyle)
        QFunc.Function_SetText(Label0, Param[0])
        Column0Layout = QHBoxLayout()
        SetColumnLayout(Column0Layout)
        Column0Layout.addWidget(Label0)

        ComboBox = ComboBoxBase()
        ComboBox.setBorderless(True)
        ComboBox.setTransparent(True)
        ComboBox.addItems(ComboItems)
        ComboBox.setCurrentText(Param[1])
        Column1Layout = QHBoxLayout()
        SetColumnLayout(Column1Layout)
        Column1Layout.addWidget(ComboBox)

        Label2 = QLabel()
        Label2.setStyleSheet(LabelStyle)
        QFunc.Function_SetText(Label2, Param[2])
        Column2Layout = QHBoxLayout()
        SetColumnLayout(Column2Layout)
        Column2Layout.addWidget(Label2)

        PlayerWidget = MediaPlayerBase()
        PlayerWidget.setBorderless(True)
        PlayerWidget.setTransparent(True)
        PlayerWidget.SetMediaPlayer(Param[0])
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
                        self.SelectOuterRow(DelButton),
                        self.DelRow()
                    )
                }
            )
        )
        Column4Layout = QHBoxLayout()
        SetColumnLayout(Column4Layout)
        Column4Layout.addWidget(DelButton)

        super().AddRow(
            [Column0Layout, Column1Layout, Column2Layout, Column3Layout, Column4Layout],
            [QHeaderView.Stretch, QHeaderView.Stretch, QHeaderView.Stretch, QHeaderView.Fixed, QHeaderView.Fixed],
            [None, None, None, RowHeight, 1.5 * RowHeight],
            RowHeight
        )

    def SetValue(self, Params: list = [['%Path%', '%Namex%', '%Sim%'], ], ComboItems: Optional[list] = ['%Name1%', ]):
        self.ClearRows()
        super().setColumnCount(self.columnCount())
        super().setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        if ComboItems is None:
            ComboItems = []
            for Param in Params:
                ComboItem = Param[1]
                ComboItems.append(ComboItem) if ComboItem not in ComboItems else None
        for Param in Params:
            QApplication.processEvents()
            self.AddRow(Param, ComboItems + [''])

    def GetValue(self):
        ValueDict = {}
        for RowCount in range(self.rowCount()):
            try:
                Key = QFunc.Function_GetText(self.cellWidget(RowCount, 0).findChild(QLabel))
                Value = self.cellWidget(RowCount, 1).findChild(ComboBoxBase).currentText()
                ValueDict[Key] = Value
            except:
                pass
        return ValueDict


class Table_STTResult(TableBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(0)
        self.SetIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def setHorizontalHeaderLabels(self, Headers: list):
        self.HorizontalHeaderLabels = Headers
        self.ColumnCount = len(Headers)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def setStyleSheet(self, StyleSheet: str):
        super().setStyleSheet(StyleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def AddRow(self, Param: tuple):
        RowHeight = 30
        LabelStyle = '''
        QLabel {
            background-color: transparent;
            border: none;
        }
        '''
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        Label0 = QLabel()
        Label0.setStyleSheet(LabelStyle)
        QFunc.Function_SetText(Label0, Param[0])
        Column0Layout = QHBoxLayout()
        SetColumnLayout(Column0Layout)
        Column0Layout.addWidget(Label0)

        LineEdit = LineEditBase()
        LineEdit.setBorderless(True)
        LineEdit.setTransparent(True)
        QFunc.Function_SetText(LineEdit, Param[1], SetPlaceholderText = True)
        Column1Layout = QHBoxLayout()
        SetColumnLayout(Column1Layout)
        Column1Layout.addWidget(LineEdit)

        PlayerWidget = MediaPlayerBase()
        PlayerWidget.setBorderless(True)
        PlayerWidget.setTransparent(True)
        PlayerWidget.SetMediaPlayer(Param[0])
        PlayerWidget.layout().setContentsMargins(6, 6, 6, 6)
        PlayerWidget.Slider.hide()
        Column2Layout = QHBoxLayout()
        SetColumnLayout(Column2Layout)
        Column2Layout.addWidget(PlayerWidget)

        super().AddRow(
            [Column0Layout, Column1Layout, Column2Layout],
            [QHeaderView.Stretch, QHeaderView.Stretch, QHeaderView.Fixed],
            [None, None, RowHeight],
            RowHeight
        )

    def SetValue(self, Params: dict = {'%Path%': '%Transcription%'}):
        self.ClearRows()
        super().setColumnCount(self.columnCount())
        super().setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        ParamDict = QFunc.ToIterable(Params)
        for Key, Value in ParamDict.items():
            QApplication.processEvents()
            Param = (Key, Value)
            self.AddRow(Param)

    def GetValue(self):
        ValueDict = {}
        for RowCount in range(self.rowCount()):
            try:
                Key = QFunc.Function_GetText(self.cellWidget(RowCount, 0).findChild(QLabel))
                Value = QFunc.Function_GetText(self.cellWidget(RowCount, 1).findChild(QLineEdit))
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
        self.SetIndexHeaderVisible(True)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def setHorizontalHeaderLabels(self, Headers: list):
        self.HorizontalHeaderLabels = Headers
        self.ColumnCount = len(Headers)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def setStyleSheet(self, StyleSheet: str):
        super().setStyleSheet(StyleSheet + '''
            QHeaderView::section, QTableView::item {padding: 0px;}
        '''
        )

    def AddRow(self, Param: tuple):
        RowHeight = 30
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        LineEdit = LineEditBase()
        LineEdit.setBorderless(True)
        LineEdit.setTransparent(True)
        QFunc.Function_SetText(LineEdit, Param[1], SetPlaceholderText = True)
        Column0Layout = QHBoxLayout()
        SetColumnLayout(Column0Layout)
        Column0Layout.addWidget(LineEdit)

        PlayerWidget = MediaPlayerBase()
        PlayerWidget.setBorderless(True)
        PlayerWidget.setTransparent(True)
        PlayerWidget.SetMediaPlayer(Param[0])
        PlayerWidget.layout().setContentsMargins(6, 6, 6, 6)
        PlayerWidget.Slider.hide()
        Column1Layout = QHBoxLayout()
        SetColumnLayout(Column1Layout)
        Column1Layout.addWidget(PlayerWidget)

        super().AddRow(
            [Column0Layout, Column1Layout],
            [QHeaderView.Stretch, QHeaderView.Fixed],
            [None, RowHeight],
            RowHeight
        )

    def SetValue(self, Params: dict = {'%Path%': '%Data%'}):
        self.ClearRows()
        super().setColumnCount(self.columnCount())
        super().setHorizontalHeaderLabels(self.HorizontalHeaderLabels)
        ParamDict = QFunc.ToIterable(Params)
        for Key, Value in ParamDict.items():
            QApplication.processEvents()
            Param = (Key, Value)
            self.AddRow(Param)

    def GetValue(self):
        ValueList = []
        for RowCount in range(self.rowCount()):
            try:
                Value = QFunc.Function_GetText(self.cellWidget(RowCount, 0).findChild(QLineEdit))
                ValueList.append(Value)
            except:
                pass
        return ValueList

##############################################################################################################################