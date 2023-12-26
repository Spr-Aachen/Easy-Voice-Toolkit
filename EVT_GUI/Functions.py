import re
from typing import Union, Optional
from PySide6.QtCore import Qt, QObject, Signal, Slot, QSize, QParallelAnimationGroup
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
    if isinstance(InsertUI, (QPushButton, QToolButton)):
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
            TargetRect = TargetWidget.geometry()
        else:
            try:
                TargetRect = ScrollArea.widget().layout().itemAt(Trigger.property("Index")).geometry()
            except:
                raise Exception("Please set property 'Index' for Trigger widget!")

        ScrollArea.verticalScrollBar().setValue(TargetRect.top())

    if isinstance(Trigger, QTreeWidgetItem):
        def TreeWidgetEvent(Item, Column):
            ScrollToWidget() if Item == Trigger else None
        Trigger.treeWidget().itemClicked.connect(TreeWidgetEvent)

    if isinstance(Trigger, (QPushButton, QToolButton)):
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

    for Index, RootItemText in enumerate(RootItemTexts):
        RootItem = QTreeWidgetItem(TreeWidget)
        RootItem.setText(0 if AddVertically else Index, RootItemText)
        RootItemTextFont = QFont()
        RootItemTextFont.setPixelSize(15)
        RootItem.setFont(0 if AddVertically else Index, RootItemTextFont)
        for ChildItemText in ChildItemTexts[Index]:
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
    CheckedEventList: list = [],
    CheckedArgsList: list = [()],
    UncheckedText: Optional[str] = None,
    UncheckedEventList: list = [],
    UncheckedArgsList: list = [()],
    TakeEffect: bool = False
):
    '''
    Function to configure checkbox
    '''
    if CheckedText is not None:
        CheckedEventList.append(CheckBox.setText)
        CheckedArgsList.append((CheckedText, ))
    if UncheckedText is not None:
        UncheckedEventList.append(CheckBox.setText)
        UncheckedArgsList.append((UncheckedText, ))

    CheckBox.toggled.connect(
        lambda IsChecked: RunEvent(CheckedEventList, CheckedArgsList) if IsChecked else RunEvent(UncheckedEventList, UncheckedArgsList)
    )

    RunEvent(CheckedEventList, CheckedArgsList) if TakeEffect and CheckBox.isChecked() else None
    RunEvent(UncheckedEventList, UncheckedArgsList) if TakeEffect and not CheckBox.isChecked() else None


def Function_SetURL(
    Button: QToolButton,
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
    Button: QToolButton,
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
    EventButtons: list = [], #EventRoles: list = [],
    EventLists: list[list] = [[], ],
    ParamLists: list[list[tuple]] = [[()], ]
):
    '''
    Function to pop up a msgbox
    '''
    MsgBox = QMessageBox() #MsgBox = MessageBoxBase()

    MsgBox.setIcon(MessageType)
    MsgBox.setWindowTitle(WindowTitle)
    MsgBox.setText(Text)
    MsgBox.setStandardButtons(Buttons)

    '''
    @Slot(QToolButton)
    def ConnectEvent(Button: QAbstractButton):
        if Button.role() in EventRoles:
            EventList = EventLists[EventRoles.index(Button.role())]
            ParamList = ParamLists[EventRoles.index(Button.role())]
            RunEvent(EventList, ParamList)
        else:
            pass
    MsgBox.buttonClicked.connect(ConnectEvent)
    '''
    Result = MsgBox.exec()

    if Result in EventButtons:
        EventList = EventLists[EventButtons.index(Result)]
        ParamList = ParamLists[EventButtons.index(Result)]
        RunEvent(EventList, ParamList)


def Function_ParamsHandler(
    UI: QObject,
    Param: Optional[str],
    Mode: str = "Get",
):
    '''
    Function to get/set the param of UI
    '''
    if Mode == "Get":
        if isinstance(UI, (QLineEdit, QPlainTextEdit)):
            return Function_GetText(UI)
        if isinstance(UI, QComboBox):
            return UI.currentText()
        if isinstance(UI, (QSlider, QSpinBox, QDoubleSpinBox)):
            return UI.value()
        if isinstance(UI, (QCheckBox, QRadioButton)):
            return UI.isChecked()

        if isinstance(UI, TableWidget_ButtonMixed):
            return UI.GetValue()

    if Mode == "Set":
        if isinstance(UI, QLineEdit):
            UI.setText(Param)
        if isinstance(UI, QPlainTextEdit):
            UI.setPlainText(Param)
        if isinstance(UI, QComboBox):
            UI.setCurrentText(Param)
        if isinstance(UI, (QSlider, QSpinBox, QDoubleSpinBox)):
            UI.setValue(Param)
        if isinstance(UI, (QCheckBox, QRadioButton)):
            UI.setChecked(Param)

        if isinstance(UI, TableWidget_ButtonMixed):
            UI.SetValue(Param)


def Function_ParamsSynchronizer(
    Trigger: Union[QObject, list],
    ParamsFrom: list = [],
    Times: Optional[float] = None,
    ParamsTo: list = [],
    Connection: str = "Connect"
):
    '''
    Function to synchronize params
    '''
    @Slot()
    def ParamsSynchronizer():
        for Index, UI_Get in enumerate(ParamsFrom):
            UI_Set = ParamsTo[Index]
            Param_Get = Function_ParamsHandler(UI_Get, "Get")
            Param_Get = Param_Get * Times if isinstance(Param_Get, (int, float, complex)) else Param_Get
            Function_ParamsHandler(UI_Set, Param_Get, "Set")
    
    TriggerList = ToIterable(Trigger)

    for Trigger in TriggerList:
        if isinstance(Trigger, (QPushButton, QToolButton)):
            Trigger.clicked.connect(ParamsSynchronizer) if Connection == "Connect" else Trigger.clicked.disconnect(ParamsSynchronizer)
        if isinstance(Trigger, (QSlider, QSpinBox, QDoubleSpinBox)):
            Trigger.valueChanged.connect(ParamsSynchronizer) if Connection == "Connect" else Trigger.valueChanged.disconnect(ParamsSynchronizer)
        if isinstance(Trigger, QLineEdit):
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
                if UI in EmptyAllowed:
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
            if "None" in Param or "None" in Param.values() or "" in Param or "" in Param.values():
                if UI in EmptyAllowed:
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
    Parent: QWidget,
    StackedWidget: QStackedWidget,
    TargetIndex: int = 0,
    Duration: int = 99
):
    '''
    Function to animate stackedwidget
    '''
    OriginalWidget = StackedWidget.currentWidget()
    OriginalGeometry = OriginalWidget.geometry()
    AlteredGeometry = QRect(OriginalGeometry.left(), OriginalGeometry.top() + OriginalGeometry.height() / 66, OriginalGeometry.width(), OriginalGeometry.height())

    WidgetAnimation = QPropertyAnimation(OriginalWidget, b"geometry", Parent)

    WidgetAnimation = Function_SetAnimation(WidgetAnimation, OriginalGeometry, AlteredGeometry, Duration)
    WidgetAnimation.finished.connect(
        lambda: StackedWidget.setCurrentIndex(TargetIndex),
        type = Qt.QueuedConnection
    )
    WidgetAnimation.finished.connect(
        lambda: OriginalWidget.setGeometry(OriginalGeometry),
        type = Qt.QueuedConnection
    )
    WidgetAnimation.start() if StackedWidget.currentIndex() != TargetIndex else None


def Function_AnimateWidgetSize(
    Parent: QWidget,
    Frame: QWidget,
    TargetWidth: Optional[int] = None,
    TargetHeight: Optional[int] = None,
    Duration: int = 210
):
    '''
    Function to animate widget size
    '''
    CurrentWidth = Frame.geometry().width() if Frame.size() == QSize(100, 30) else Frame.width()
    CurrentHeight = Frame.geometry().height() if Frame.size() == QSize(100, 30) else Frame.height()

    FrameAnimationMinWidth = QPropertyAnimation(Frame, b"minimumWidth", Parent)
    FrameAnimationMaxWidth = QPropertyAnimation(Frame, b"maximumWidth", Parent)
    FrameAnimationMinHeight = QPropertyAnimation(Frame, b"minimumHeight", Parent)
    FrameAnimationMaxHeight = QPropertyAnimation(Frame, b"maximumHeight", Parent)

    AnimationGroup = QParallelAnimationGroup(Parent)

    AnimationGroup.addAnimation(Function_SetAnimation(FrameAnimationMinWidth, CurrentWidth, TargetWidth, Duration)) if TargetWidth is not None else None
    AnimationGroup.addAnimation(Function_SetAnimation(FrameAnimationMaxWidth, CurrentWidth, TargetWidth, Duration)) if TargetWidth is not None else None
    AnimationGroup.addAnimation(Function_SetAnimation(FrameAnimationMinHeight, CurrentHeight, TargetHeight, Duration)) if TargetHeight is not None else None
    AnimationGroup.addAnimation(Function_SetAnimation(FrameAnimationMaxHeight, CurrentHeight, TargetHeight, Duration)) if TargetHeight is not None else None
    AnimationGroup.start()


def Function_AnimateFrame(
    Parent: QWidget,
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
        Function_AnimateWidgetSize(Parent, Frame, MaxWidth, None, Duration) if MaxWidth not in (None, Frame.width()) else None
        Function_AnimateWidgetSize(Parent, Frame, None, MaxHeight, Duration) if MaxHeight not in (None, Frame.height()) else None

    def ReduceFrame():
        Function_AnimateWidgetSize(Parent, Frame, MinWidth, None, Duration) if MinWidth not in (None, Frame.width()) else None
        Function_AnimateWidgetSize(Parent, Frame, None, MinHeight, Duration) if MinHeight not in (None, Frame.height()) else None

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