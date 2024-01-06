from .QSimpleWidgets.Utils import *
from .QSimpleWidgets.QFunctions import *
from .QSimpleWidgets.Sources import *
from .QSimpleWidgets.ComponentsCustomizer import *

##############################################################################################################################

def Function_ShowMessageBox(
    MessageType: object = QMessageBox.Information,
    WindowTitle: str = ...,
    Text: str = ...,
    Buttons: object = QMessageBox.Ok,
    EventButtons: list = [],
    EventLists: list[list] = [[], ],
    ParamLists: list[list[tuple]] = [[()], ]
):
    '''
    Function to pop up a msgbox
    '''
    MsgBox = QMessageBox()

    MsgBox.setIcon(MessageType)
    MsgBox.setWindowTitle(WindowTitle)
    MsgBox.setText(Text)
    MsgBox.setStandardButtons(Buttons)

    Result = MsgBox.exec()

    if Result in EventButtons:
        EventList = EventLists[EventButtons.index(Result)]
        ParamList = ParamLists[EventButtons.index(Result)]
        RunEvent(EventList, ParamList)


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

class Table_ViewModels(TableBase):
    '''
    '''
    Download = Signal(tuple)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(4)
        self.SetIndexHeaderVisible(False)

        self.Clipboard = QApplication.clipboard()

    def setStyleSheet(self, StyleSheet: str):
        super().setStyleSheet(StyleSheet + "QTableView{border-radius:0px;}")

    def AddRow(self, Param: tuple):
        RowHeight = 36
        LabelStyle = '''
        QLabel {
            background-color: transparent;
            padding: 6px;
            border-width: 1px;
            border-style: solid;
            border-color: rgba(201, 210, 222, 123);
        }
        '''
        ButtonStyle = '''
        QPushButton {
            background-color: transparent;
            padding: 6px;
            border-width: 1px;
            border-style: solid;
            border-color: rgba(201, 210, 222, 123);
        }
        '''
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        Label0 = QLabel()
        Label0.setStyleSheet(LabelStyle)
        Function_SetText(Label0, Param[0])
        Column0Layout = QHBoxLayout()
        SetColumnLayout(Column0Layout)
        Column0Layout.addWidget(Label0)

        Label1 = QLabel()
        Label1.setStyleSheet(LabelStyle)
        Function_SetText(Label1, Param[1])
        Column1Layout = QHBoxLayout()
        SetColumnLayout(Column1Layout)
        Column1Layout.addWidget(Label1)

        Label2 = QLabel()
        Label2.setStyleSheet(LabelStyle)
        Function_SetText(Label2, Param[2])
        Column2Layout = QHBoxLayout()
        SetColumnLayout(Column2Layout)
        Column2Layout.addWidget(Label2)

        StackedWidget = QStackedWidget()
        StackedWidget.setContentsMargins(0, 0, 0, 0)
        OpenButton = QPushButton()
        OpenButton.setStyleSheet(ButtonStyle + "QPushButton {image: url(:/Button_Icon/Sources/OpenedFolder.png);}")
        OpenButton.clicked.connect(lambda: Function_OpenURL(Param[3] if isinstance(Param[3], str) else Param[3][1]))
        DownloadButton = QPushButton()
        DownloadButton.setStyleSheet(ButtonStyle + "QPushButton {image: url(:/Button_Icon/Sources/Download.png);}")
        DownloadButton.clicked.connect(lambda: self.Download.emit(Param[3]) if isinstance(Param[3], tuple) else None)
        DownloadButton.clicked.connect(lambda: StackedWidget.setCurrentWidget(OpenButton))
        StackedWidget.addWidget(OpenButton)
        StackedWidget.addWidget(DownloadButton)
        StackedWidget.setCurrentWidget(OpenButton) if isinstance(Param[3], str) else StackedWidget.setCurrentWidget(DownloadButton)
        CopyButton = QPushButton()
        CopyButton.setStyleSheet(ButtonStyle + "QPushButton {image: url(:/Button_Icon/Sources/Clipboard.png);}")
        CopyButton.clicked.connect(lambda: self.Clipboard.setText(Param[3][0]) if isinstance(Param[3], tuple) else None)
        CopyButton.clicked.connect(lambda: Function_ShowMessageBox(WindowTitle = "Tip", Text = "已复制链接到剪切板"))
        Function_SetRetainSizeWhenHidden(CopyButton)
        CopyButton.hide() if StackedWidget.currentWidget() == OpenButton else None
        StackedWidget.currentChanged.connect(lambda: CopyButton.hide() if StackedWidget.currentWidget() == OpenButton else None)
        Column3Layout = QHBoxLayout()
        SetColumnLayout(Column3Layout)
        Column3Layout.addWidget(StackedWidget)
        Column3Layout.addWidget(CopyButton)

        super().AddRow(
            [Column0Layout, Column1Layout, Column2Layout, Column3Layout],
            [QHeaderView.Stretch, QHeaderView.Stretch, QHeaderView.Stretch, QHeaderView.Fixed],
            [None, None, None, 2 * RowHeight],
            RowHeight
        )

    def SetValue(self, Params: list = [['', '', '', 'url'], ]):
        self.ClearRows()
        for Index, Param in enumerate(Params):
            if Index == 1 + self.columnCount():
                return print("Maximum params reached")
            self.AddRow(Param)


class Table_EditAudioSpeaker(TableBase):
    '''
    '''
    ValueChanged = Signal(dict)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRowCount(0)
        self.setColumnCount(3)
        self.SetIndexHeaderVisible(True)

        self.model().dataChanged.connect(
            lambda: self.ValueChanged.emit(self.GetValue())
        )

    def AddRow(self, Param: Optional[tuple] = None, FileType: Optional[str] = None):
        RowHeight = 24
        LineEditStyle = '''
        QLineEdit {
            background-color: transparent;
            padding: 6px;
            border-width: 1px;
            border-style: solid;
            border-color: rgba(201, 210, 222, 123);
        }
        '''
        ButtonStyle = '''
        QPushButton {
            background-color: transparent;
            padding: 6px;
            border-width: 1px;
            border-style: solid;
            border-color: rgba(201, 210, 222, 123);
        }
        '''
        def SetColumnLayout(ColumnLayout):
            ColumnLayout.setContentsMargins(0, 0, 0, 0)
            ColumnLayout.setSpacing(0)

        LineEdit0 = QLineEdit()
        LineEdit0.setStyleSheet(LineEditStyle)
        Function_SetText(LineEdit0, Param[0] if Param else '', SetPlaceholderText = True)
        LineEdit0.textChanged.connect(
            lambda: self.ValueChanged.emit(self.GetValue())
        )
        Column0Layout = QHBoxLayout()
        SetColumnLayout(Column0Layout)
        Column0Layout.addWidget(LineEdit0)

        LineEdit1 = QLineEdit()
        LineEdit1.setStyleSheet(LineEditStyle)
        Function_SetText(LineEdit1, Param[1] if Param else '', SetPlaceholderText = True)
        LineEdit1.textChanged.connect(
            lambda: self.ValueChanged.emit(self.GetValue())
        )
        Button = QPushButton()
        Button.setStyleSheet(ButtonStyle)
        Button.setText("...")
        Function_SetFileDialog(Button, LineEdit1, "SelectFile", FileType)
        Column1Layout = QHBoxLayout()
        SetColumnLayout(Column1Layout)
        Column1Layout.addWidget(LineEdit1)
        Column1Layout.addWidget(Button)

        AddButton = QPushButton()
        AddButton.setStyleSheet(ButtonStyle)
        AddButton.setText("+")
        AddButton.clicked.connect(lambda: self.SelectOuterRow(AddButton), Qt.QueuedConnection)
        AddButton.clicked.connect(self.AddRow, Qt.QueuedConnection)
        DelButton = QPushButton()
        DelButton.setStyleSheet(ButtonStyle)
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

    def SetValue(self, Params: dict = {'': ''}, FileType: Optional[str] = None):
        self.ClearRows()
        ParamDict = ToIterable(Params)
        for Key, Value in ParamDict.items():
            Param = (Key, Value)
            Index = next((i for i, key in enumerate(ParamDict) if key == Key), None)
            if Index == 1 + self.columnCount() - 1:
                return print("Maximum params reached")
            self.AddRow(Param, FileType)

    def GetValue(self):
        ValueDict = {}
        for RowCount in range(self.rowCount()):
            try:
                Key = Function_GetText(self.cellWidget(RowCount, 0).findChild(QLineEdit))
                Value = Function_GetText(self.cellWidget(RowCount, 1).findChild(QLineEdit))
                ValueDict[Key] = Value
            except:
                pass
        return ValueDict

##############################################################################################################################