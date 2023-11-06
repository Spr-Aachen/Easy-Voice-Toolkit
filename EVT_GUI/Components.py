from .QSimpleWidgets.Utils import *
from .QSimpleWidgets.QFunctions import *
from .QSimpleWidgets.ComponentsCustomizer import *

##############################################################################################################################

def Function_SetFileDialog(
    Button: QPushButton,
    LineEdit: QLineEdit,
    Mode: str,
    FileType: Optional[str] = None,
    ButtonTooltip: str = "Browse"
):
    '''
    Function to select/save file path (through button)
    '''
    @Slot()
    def SetFileDialog():
        DisplayText = Function_GetFileDialog(Mode, FileType)
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

    def AddRow(self, Param: Optional[tuple] = None, FileType: Optional[str] = None):
        CurrentColumnCount = self.columnCount()
        CurrentRowCount = self.rowCount()

        self.insertRow(CurrentRowCount)
        for ColumnCount in range(1, 1 + self.ColumnCount):
            self.setCellWidget(CurrentRowCount, ColumnCount, QWidget())

            if ColumnCount == 1 + 0:
                LineEdit0 = LineEdit_NoBorder(Param[ColumnCount] if Param else 'None')
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
                LineEdit1 = LineEdit_NoBorder(Param[ColumnCount] if Param else 'None')
                LineEdit1.textChanged.connect(
                    lambda: self.ValueChanged.emit(self.GetValue())
                )
                Button = ToolButtonBase("...")
                Function_SetFileDialog(Button, LineEdit1, "SelectFile", FileType)
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

    def SetValue(self, Params: dict = {'': ''}, FileType: Optional[str] = None):
        ParamDict = Params #ParamDict = IterChecker(Params)
        for Key, Value in ParamDict.items():
            Param = tuple(('',) + (Key, Value))
            Index = next((i for i, key in enumerate(ParamDict) if key == Key), None)
            if Index == 1 + self.ColumnCount:
                return print("Maximum params reached")
            self.AddRow(Param, FileType)

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
        HeaderList.insert(0, '')
        for Index, Header in enumerate(HeaderList, 1):
            if Index == 1 + self.ColumnCount:
                return print("Maximum headers reached")
            self.setHorizontalHeaderItem(Index, QTableWidgetItem(HeaderList[Index]))

##############################################################################################################################

class MessageBox_Stacked(MessageBoxBase):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setMinimumSize(900, 480)

        self.StackedWidget = QStackedWidget()

        self.ButtonP = QPushButton()
        self.ButtonP.clicked.connect(lambda: self.StackedWidget.setCurrentIndex(self.StackedWidget.currentIndex() - 1))
        self.ButtonP.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        Function_SetRetainSizeWhenHidden(self.ButtonP)
        self.ButtonP.setStyleSheet(
            "QPushButton {"
            "   background-color: transparent;"
            "   border-image: url(:/Button_Icon/Sources/LeftArrow.png);"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(210, 222, 234, 12);"
            "}"
        )
        self.ButtonP.setToolTip("Prev Page")

        self.ButtonN = QPushButton()
        self.ButtonN.clicked.connect(lambda: self.StackedWidget.setCurrentIndex(self.StackedWidget.currentIndex() + 1))
        self.ButtonN.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        Function_SetRetainSizeWhenHidden(self.ButtonN)
        self.ButtonN.setStyleSheet(
            "QPushButton {"
            "   background-color: transparent;"
            "   border-image: url(:/Button_Icon/Sources/RightArrow.png);"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(210, 222, 234, 12);"
            "}"
        )
        self.ButtonN.setToolTip("Next Page")

        Layout = QHBoxLayout()
        Layout.setAlignment(Qt.AlignCenter)
        Layout.setContentsMargins(0, 0, 0, 0)
        Layout.setSpacing(12)
        Layout.addWidget(self.ButtonP)
        Layout.addWidget(self.StackedWidget)
        Layout.addWidget(self.ButtonN)
        self.InsertItem(Layout)

        self.SetContent(None, 'None')

    def SetContent(self, Images: list, Texts: list):
        Function_SetNoContents(self.StackedWidget)

        for Index, Image in enumerate(IterChecker(Images)):
            TextBrowser = QTextBrowser()
            TextBrowser.setStyleSheet(
                "QTextBrowser {"
                f"    background-image: url({NormPath(Image, 'Posix')});"
                "    background-size: cover;"
                "    background-repeat: no-repeat;"
                "    background-position: center 0px;"
                "    padding: 0px;"
                "    border-width: 0px;"
                "    border-radius: 6px;"
                "    border-style: solid;"
                "}"
            ) if Image is not None else None

            Label = QLabel()
            Function_SetText(Label, IterChecker(Texts)[Index], 'center', 9.9, 630)

            SubLayout = QVBoxLayout()
            SubLayout.setAlignment(Qt.AlignCenter)
            SubLayout.setContentsMargins(0, 0, 0, 0)
            SubLayout.setSpacing(12)
            SubLayout.addWidget(TextBrowser)
            SubLayout.addWidget(Label)

            Widget = QWidget()
            Widget.setLayout(SubLayout)
            self.StackedWidget.addWidget(Widget)
    
        self.StackedWidget.currentChanged.connect(lambda: self.ButtonP.setVisible(False) if self.StackedWidget.currentIndex() == 0 else self.ButtonP.setVisible(True))
        self.ButtonP.setVisible(False)
        self.StackedWidget.currentChanged.connect(lambda: self.ButtonN.setVisible(False) if self.StackedWidget.currentIndex() == self.StackedWidget.count() - 1 else self.ButtonN.setVisible(True))
        self.ButtonN.setVisible(True)

        self.StackedWidget.currentChanged.connect(lambda: self.setText(f'{self.StackedWidget.currentIndex() + 1} / {self.StackedWidget.count()}'))
        self.setText(f'1 / {self.StackedWidget.count()}')

##############################################################################################################################