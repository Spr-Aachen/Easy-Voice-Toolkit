import re
from typing import Union, Optional
from PySide6.QtCore import Qt, QObject, Signal, Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *

from .QSimpleWidgets.Utils import *
from .QSimpleWidgets.QFunctions import *
from .Components import *

##############################################################################################################################

def Function_FindParentUI(
    ChildUI: QWidget,
    ParentType: object
):
    '''
    Function to find parent UI
    '''
    ChildUI_Parent = ChildUI.parent()

    while not isinstance(ChildUI_Parent, ParentType):
        try:
            ChildUI_Parent = ChildUI_Parent.parent()
        except:
            raise Exception(f"{ChildUI}'s parent UI not found! Please check if the layout is correct.")

    return ChildUI_Parent


def Function_InsertUI(
    ParentUI: QWidget,
    InsertType: object,
    InsertPosition: str = "End",
    UIParam: Optional[str] = None,
    UIToolTip: Optional[str] = None,
):
    '''
    Function to insert UI
    '''
    InsertUI = InsertType(UIParam)
    if isinstance(InsertUI, QAbstractButton):
        InsertUI.setMinimumHeight(24)
        InsertUI.setStyleSheet(
            f"{InsertType.__name__}"
            "{"
                "text-align: center;"
                "font-size: 12px;"
                "color: rgb(255, 255, 255);"
                "background-color: rgb(90, 90, 90);"
                "padding: 0px;"
                "border-width: 0px;"
                "border-radius: 6px;"
                "border-style: solid;"
            "}"
            f"{InsertType.__name__}:hover"
            "{"
                "background-color: rgb(120, 120, 120);"
            "}"

            "QToolTip"
            "{"
                "color: rgba(255, 255, 255, 210);"
                "background-color: transparent;"
                "border-width: 0px;"
                "border-style: solid;"
            "}"
        )
    else:
        pass

    Layout = ParentUI.layout() if ParentUI.layout() != None else QGridLayout(ParentUI)
    if InsertPosition == "Start":
        RowCount = 0
    if InsertPosition == "End":
        RowCount = ParentUI.document().lineCount() if isinstance(ParentUI, (QPlainTextEdit, QTextEdit, QTextBrowser)) else round(ParentUI.height()/15)
    for Row in range(0, RowCount):
        SpacingUI = QWidget(ParentUI)
        SpacingUI.setStyleSheet(
            "QWidget"
            "{"
                "background-color: transparent;"
                "padding: 0px;"
                "border-width: 0px;"
            "}"
        )
        Layout.addWidget(SpacingUI, Row, 0)
    Layout.addWidget(InsertUI, RowCount, 0)
    
    InsertUI.setToolTipDuration(-1)
    InsertUI.setToolTip(UIToolTip)

    return InsertUI


def Function_ScrollToWidget(
    Trigger: QWidget,
    TargetWidget: Optional[QWidget],
    ScrollArea: QScrollArea,
    #Alignment: str = 'Top'
):
    '''
    '''
    def ScrollToWidget():
        if TargetWidget is not None:
            TargetRect = TargetWidget.mapToGlobal(QPoint(0, 0))
        else:
            try:
                TargetRect = ScrollArea.widget().layout().itemAt(Trigger.property("Index")).mapToGlobal(QPoint(0, 0))
            except:
                raise Exception("Please set property 'Index' for Trigger widget!")
        TargetYPos = TargetRect.y() - ScrollArea.widget().mapToGlobal(QPoint(0, 0)).y()

        ScrollArea.verticalScrollBar().setValue(TargetYPos)

    if isinstance(Trigger, QTreeWidgetItem):
        def TreeWidgetEvent(Item, Column):
            ScrollToWidget() if Item == Trigger else None
        Trigger.treeWidget().itemClicked.connect(TreeWidgetEvent)

    if isinstance(Trigger, QAbstractButton):
        Trigger.clicked.connect(ScrollToWidget)


def Function_SetTreeWidget(
    TreeWidget: QTreeWidget,
    RootItemTexts: list = [],
    ChildItemTexts: list = [()],
    AddVertically: bool = False,
    HideHeader: bool = True,
    ExpandItems: bool = True
):
    '''
    '''
    TreeWidget.clear()

    RootItems = []

    for Index, RootItemText in enumerate(ToIterable(RootItemTexts)):
        RootItem = QTreeWidgetItem(TreeWidget)
        RootItem.setText(0 if AddVertically else Index, RootItemText)
        RootItemTextFont = QFont()
        RootItemTextFont.setPixelSize(15)
        RootItem.setFont(0 if AddVertically else Index, RootItemTextFont)
        for ChildItemText in ToIterable(ChildItemTexts[Index]):
            ChildItem = QTreeWidgetItem(RootItem)
            ChildItem.setText(0 if AddVertically else Index, ChildItemText)
            ChildItemTextFont = QFont()
            ChildItemTextFont.setPixelSize(12)
            ChildItem.setFont(0 if AddVertically else Index, ChildItemTextFont)

        RootItems.append(RootItem)

    TreeWidget.setColumnCount(1) if AddVertically else None
    TreeWidget.addTopLevelItems(RootItems)

    TreeWidget.setHeaderHidden(HideHeader)

    TreeWidget.expandAll() if ExpandItems else None

'''
def Function_SetTreeView(
    TreeView: QTreeView,
    HeaderTexts: list = [],
    RootItemTexts: list = [()],
    ChildItemTexts: list = [(())],
    AddVertically: bool = False
):

    for Index, HeaderText in enumerate(HeaderTexts):
        TreeView.setHeaderLabels(HeaderTexts)
        TreeView.header().setOrientation(Qt.Vertical)
'''

def Function_ConfigureCheckBox(
    CheckBox: QCheckBox,
    CheckedText: Optional[str] = None,
    CheckedEvents: list = [],
    UncheckedText: Optional[str] = None,
    UncheckedEvents: list = [],
    TakeEffect: bool = False
):
    '''
    Function to configure checkbox
    '''
    if CheckedText is not None:
        CheckedEvents.append(lambda: CheckBox.setText(CheckedText))
    if UncheckedText is not None:
        UncheckedEvents.append(lambda: CheckBox.setText(UncheckedText))

    CheckBox.toggled.connect(
        lambda IsChecked: RunEvents(CheckedEvents if IsChecked else UncheckedEvents)
    )

    RunEvents(CheckedEvents) if TakeEffect and CheckBox.isChecked() else None
    RunEvents(UncheckedEvents) if TakeEffect and not CheckBox.isChecked() else None


def Function_SetURL(
    Button: QAbstractButton,
    URL: Union[str, QWidget, list],
    ButtonTooltip: str = "Open"
):
    '''
    Function to open URL (through button)
    '''
    Button.clicked.connect(
        lambda: Function_OpenURL([(Function_ParamsHandler(URL, None) if isinstance(URL, QWidget) else URL) for URL in ToIterable(URL)])
    )
    Button.setToolTipDuration(-1)
    Button.setToolTip(ButtonTooltip)


def Function_SetFileDialog(
    Button: QAbstractButton,
    LineEdit: QLineEdit,
    Mode: str,
    FileType: Optional[str] = None,
    Directory: Optional[str] = None,
    #DisplayText: str = "None",
    ButtonTooltip: str = "Browse"
):
    '''
    Function to select/save file path (through button)
    '''
    #LineEdit.setText(DisplayText)

    @Slot()
    def SetFileDialog():
        DisplayText = Function_GetFileDialog(
            Mode = Mode,
            FileType = FileType,
            Directory = os.path.expanduser('~/Documents' if platform.system() == "Windows" else '~/') if Directory is None else Directory
        )
        LineEdit.setText(DisplayText)
        LineEdit.setStatusTip(DisplayText)

    Button.clicked.connect(SetFileDialog)
    Button.setToolTipDuration(-1)
    Button.setToolTip(ButtonTooltip)


def Function_ShowMessageBox(
    MessageType: object = QMessageBox.Information,
    WindowTitle: str = ...,
    Text: str = ...,
    Buttons: object = QMessageBox.Ok,
    ButtonEvents: dict = {}
):
    '''
    Function to pop up a msgbox
    '''
    MsgBox = QMessageBox() #MsgBox = MessageBoxBase()

    MsgBox.setIcon(MessageType)
    MsgBox.setWindowTitle(WindowTitle)
    MsgBox.setText(Text)
    MsgBox.setStandardButtons(Buttons)

    Result = MsgBox.exec()

    ButtonEvents[Result]() if Result in list(ButtonEvents.keys()) else None


def Function_ParamsHandler(
    UI: QObject,
    Param: Optional[str],
    Mode: str = "Get",
):
    '''
    Function to get/set the param of UI
    '''
    if Mode == "Get":
        if isinstance(UI, (QLineEdit, LineEditBase, QPlainTextEdit)):
            return Function_GetText(UI)
        if isinstance(UI, QComboBox):
            return UI.currentText()
        if isinstance(UI, (QSlider, QAbstractSpinBox)):
            return UI.value()
        if isinstance(UI, (QCheckBox, QRadioButton)):
            return UI.isChecked()

        if isinstance(UI, Table_EditAudioSpeaker):
            return UI.GetValue()

    if Mode == "Set":
        if isinstance(UI, (QLineEdit, LineEditBase)):
            UI.setText(Param)
        if isinstance(UI, QPlainTextEdit):
            UI.setPlainText(Param)
        if isinstance(UI, QComboBox):
            UI.setCurrentText(Param)
        if isinstance(UI, (QSlider, QAbstractSpinBox)):
            UI.setValue(Param)
        if isinstance(UI, (QCheckBox, QRadioButton)):
            UI.setChecked(Param)

        if isinstance(UI, Table_EditAudioSpeaker):
            UI.SetValue(Param)


def Function_ParamsSynchronizer(
    Trigger: Union[QObject, list],
    FromTo: dict = {},
    Times: Optional[float] = None,
    Connection: str = "Connect"
):
    '''
    Function to synchronize params (ParamsFrom.value * Times = ParamsTo.value)
    '''
    @Slot()
    def ParamsSynchronizer():
        for UI_Get, UI_Set in FromTo.items():
            Param_Get = Function_ParamsHandler(UI_Get, "Get")
            Param_Get = Param_Get * Times if isinstance(Param_Get, (int, float, complex)) else Param_Get
            Function_ParamsHandler(UI_Set, Param_Get, "Set")
    
    TriggerList = ToIterable(Trigger)

    for Trigger in TriggerList:
        if isinstance(Trigger, QAbstractButton):
            Trigger.clicked.connect(ParamsSynchronizer) if Connection == "Connect" else Trigger.clicked.disconnect(ParamsSynchronizer)
        if isinstance(Trigger, QAbstractSlider):
            Trigger.sliderMoved.connect(ParamsSynchronizer) if Connection == "Connect" else Trigger.sliderMoved.disconnect(ParamsSynchronizer)
        if isinstance(Trigger, QAbstractSpinBox):
            Trigger.valueChanged.connect(ParamsSynchronizer) if Connection == "Connect" else Trigger.valueChanged.disconnect(ParamsSynchronizer)
        if isinstance(Trigger, (QLineEdit, LineEditBase)):
            Trigger.textChanged.connect(ParamsSynchronizer) if Connection == "Connect" else Trigger.textChanged.disconnect(ParamsSynchronizer)


def Function_ParamsChecker(
    ParamsFrom: list = [],
    EmptyAllowed: list = []
):
    '''
    Function to return handled params
    '''
    Params = []

    for UI in ParamsFrom:
        Param = Function_ParamsHandler(UI, "Get")
        if isinstance(Param, str):
            if Param.strip() == "None" or Param.strip() == "":
                if UI in ToIterable(EmptyAllowed):
                    Param = None
                else:
                    Function_ShowMessageBox(
                        MessageType = QMessageBox.Warning,
                        WindowTitle = "Warning",
                        Text = "Empty param detected!\n检测到参数空缺！"
                    )
                    return "Abort"
            else:
                if "，" in Param or "," in Param:
                    Param = re.split(
                        pattern = '[，,]',
                        string = Param,
                        maxsplit = 0
                    )
        if isinstance(Param, dict):
            if "None" in list(Param.keys()&Param.values()) or "" in list(Param.keys()&Param.values()):
                if UI in ToIterable(EmptyAllowed):
                    Param = None
                else:
                    Function_ShowMessageBox(
                        MessageType = QMessageBox.Warning,
                        WindowTitle = "Warning",
                        Text = "Empty param detected!\n检测到参数空缺！"
                    )
                    return "Abort"
            else:
                pass
        else:
            pass
        Params.append(Param)
    
    Args = tuple(Params)#if Params != [] else None

    return Args


def Function_AnimateStackedWidget(
    StackedWidget: QStackedWidget,
    TargetIndex: int = 0,
    Duration: int = 99
):
    '''
    Function to animate stackedwidget
    '''
    OriginalWidget = StackedWidget.currentWidget()
    OriginalGeometry = OriginalWidget.geometry()

    WidgetAnimation = Function_SetWidgetPosAnimation(OriginalWidget, Duration)
    WidgetAnimation.finished.connect(
        lambda: StackedWidget.setCurrentIndex(TargetIndex),
        type = Qt.QueuedConnection
    )
    WidgetAnimation.finished.connect(
        lambda: OriginalWidget.setGeometry(OriginalGeometry),
        type = Qt.QueuedConnection
    )
    WidgetAnimation.start() if StackedWidget.currentIndex() != TargetIndex else None


def Function_AnimateFrame(
    Frame: QWidget,
    MinWidth: Optional[int] = None,
    MaxWidth: Optional[int] = None,
    MinHeight: Optional[int] = None,
    MaxHeight: Optional[int] = None,
    Duration: int = 210,
    Mode: str = "Toggle"
):
    '''
    Function to animate frame
    '''
    def ExtendFrame():
        Function_SetWidgetSizeAnimation(Frame, MaxWidth, None, Duration).start() if MaxWidth not in (None, Frame.width()) else None
        Function_SetWidgetSizeAnimation(Frame, None, MaxHeight, Duration).start() if MaxHeight not in (None, Frame.height()) else None

    def ReduceFrame():
        Function_SetWidgetSizeAnimation(Frame, MinWidth, None, Duration).start() if MinWidth not in (None, Frame.width()) else None
        Function_SetWidgetSizeAnimation(Frame, None, MinHeight, Duration).start() if MinHeight not in (None, Frame.height()) else None

    if Mode == "Extend":
        ExtendFrame()
    if Mode == "Reduce":
        ReduceFrame()
    if Mode == "Toggle":
        ExtendFrame() if Frame.width() == MinWidth or Frame.height() == MinHeight else ReduceFrame()


def Function_AnimateProgressBar(
    ProgressBar: QProgressBar,
    MinValue: int = 0,
    MaxValue: int = 100,
    DisplayValue: bool = False,
    IsTaskAlive: bool = False
):
    '''
    Function to animate progressbar
    '''
    ProgressBar.setTextVisible(DisplayValue)
    ProgressBar.setRange(MinValue, MaxValue)
    ProgressBar.setValue(MinValue)

    if IsTaskAlive == True:
        ProgressBar.setRange(0, 0)
        #QApplication.processEvents()
    else:
        ProgressBar.setRange(MinValue, MaxValue)
        ProgressBar.setValue(MaxValue)

##############################################################################################################################