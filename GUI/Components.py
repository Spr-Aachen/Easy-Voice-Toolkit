#from .Functions import *
from .QSimpleWidgets.Utils import *
from .QSimpleWidgets.ComponentsCustomizer import *

##############################################################################################################################

def Function_SetFileDialog(
    Button: QPushButton,
    LineEdit: QLineEdit,
    Mode: str,
    FileType: Optional[str] = None,
    #DisplayText: str = "None",
    ButtonTooltip: str = "Browse"
):
    '''
    Function to select/save file path (through button)
    '''
    #LineEdit.setText(DisplayText)

    @Slot()
    def SetFileDialog():
        if Mode == "SelectDir":
            DisplayText = QFileDialog.getExistingDirectory(
                caption = "选择文件夹",
                dir = os.getcwd()
            )
        if Mode == "SelectFile":
            DisplayText, _ = QFileDialog.getOpenFileName(
                caption = "选择文件",
                dir = os.getcwd(),
                filter = FileType
            )
        if Mode == "SaveFile":
            DisplayText, _ = QFileDialog.getSaveFileName(
                caption = "保存文件",
                dir = os.getcwd(),
                filter = FileType
            )

        LineEdit.setText(DisplayText)
        LineEdit.setStatusTip(DisplayText)
    
    Button.clicked.connect(SetFileDialog)
    Button.setToolTipDuration(-1)
    Button.setToolTip(ButtonTooltip)

##############################################################################################################################

class TableWidget_ButtonMixed(TableWidgetBase):
    '''
    '''
    ValueChanged = Signal(dict)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.ColumnCount = 3
        self.setColumnCount(self.ColumnCount + 1)
        self.setRowCount(0)

        self.model().dataChanged.connect( #self.itemChanged.connect(
            lambda: self.ValueChanged.emit(self.GetValue())
        )

    def DelRow(self):
        self.removeRow(self.currentRow()) if self.rowCount() > 1 else None

    def AddRow(self, Param: Optional[tuple] = None):
        CurrentColumnCount = self.columnCount()
        CurrentRowCount = self.rowCount()

        self.insertRow(CurrentRowCount)
        for ColumnCount in range(1, 1 + self.ColumnCount):
            self.setCellWidget(CurrentRowCount, ColumnCount, QWidget())

            if ColumnCount == 1 + 0:
                LineEdit0 = QLineEdit(Param[ColumnCount] if Param else 'None')
                LineEdit0.textChanged.connect(
                    lambda: self.ValueChanged.emit(self.GetValue())
                )
                Column0Layout = QGridLayout()
                Column0Layout.setContentsMargins(3, 3, 3, 3)
                #Column0Layout.setSpacing(3)
                Column0Layout.addWidget(LineEdit0)
                self.cellWidget(CurrentRowCount, ColumnCount).setLayout(Column0Layout)
                self.horizontalHeader().setSectionResizeMode(ColumnCount, QHeaderView.ResizeToContents)

            if ColumnCount == 1 + 1:
                LineEdit1 = QLineEdit(Param[ColumnCount] if Param else 'None')
                LineEdit1.textChanged.connect(
                    lambda: self.ValueChanged.emit(self.GetValue())
                )
                Button = ToolButtonBase("...")
                Function_SetFileDialog(Button, LineEdit1, "SelectFile")
                Column1Layout = QHBoxLayout()
                Column1Layout.setContentsMargins(3, 3, 3, 3)
                Column1Layout.setSpacing(3)
                Column1Layout.addWidget(LineEdit1)
                Column1Layout.addWidget(Button)
                self.cellWidget(CurrentRowCount, ColumnCount).setLayout(Column1Layout)
                self.horizontalHeader().setSectionResizeMode(ColumnCount, QHeaderView.Stretch)

            if ColumnCount == 1 + 2:
                def SelectButtonRow(Button):
                    CellWidget = Button.parent()
                    ModelIndex = self.indexAt(CellWidget.pos())
                    self.selectRow(ModelIndex.row()) #if index.isValid() else None
                AddButton = ToolButtonBase("+")
                AddButton.clicked.connect(lambda: SelectButtonRow(AddButton), Qt.QueuedConnection)
                AddButton.clicked.connect(self.AddRow, Qt.QueuedConnection)
                DelButton = ToolButtonBase("-")
                DelButton.clicked.connect(lambda: SelectButtonRow(DelButton), Qt.QueuedConnection)
                DelButton.clicked.connect(self.DelRow, Qt.QueuedConnection)
                Column2Layout = QHBoxLayout()
                Column2Layout.setContentsMargins(3, 3, 3, 3)
                Column2Layout.setSpacing(3)
                Column2Layout.addWidget(AddButton)
                Column2Layout.addWidget(DelButton)
                self.cellWidget(CurrentRowCount, ColumnCount).setLayout(Column2Layout)
                self.horizontalHeader().setSectionResizeMode(ColumnCount, QHeaderView.ResizeToContents)

    def SetValue(self, Params: dict = {'': ''}):
        ParamDict = Params #ParamDict = IterChecker(Params)
        for Key, Value in ParamDict.items():
            Param = tuple(('',) + (Key, Value)) #if self.IsIndexShown else Param
            Index = next((i for i, key in enumerate(ParamDict) if key == Key), None)
            if Index == 1 + self.ColumnCount:
                return print("Maximum params reached")
            self.AddRow(Param)

    def GetValue(self):
        ValueDict = {}
        for RowCount in range(self.rowCount()):
            try:
                Key = self.cellWidget(RowCount, 1 + 0).findChild(QLineEdit).text()
                Value = self.cellWidget(RowCount, 1 + 1).findChild(QLineEdit).text()
                ValueDict[Key] = Value
            except:
                pass
        return ValueDict

    def SetHorizontalHeaders(self, Headers: list = ['', '', '']):
        HeaderList = IterChecker(Headers)
        HeaderList.insert(0, '') #if self.IsIndexShown else None
        for Index, Header in enumerate(HeaderList):
            if Index == 1 + self.ColumnCount:
                return print("Maximum headers reached")
            self.setHorizontalHeaderItem(1 + Index, QTableWidgetItem(Header))

##############################################################################################################################