import win32gui
import win32con
from ctypes import Structure, c_int, POINTER, WinDLL, byref
from ctypes.wintypes import UINT, HWND, RECT, MSG, LPRECT
from PySide6.QtCore import Qt, QPoint, QEvent, QEventLoop
from PySide6.QtGui import QPixmap, QIcon, QFont, QCursor, QMouseEvent, QShowEvent, QCloseEvent, QMoveEvent, QResizeEvent
from PySide6.QtWidgets import *

from .QFunctions import *
from .Sources import *

##############################################################################################################################

class TitleBarBase(QWidget):
    '''
    '''
    DEFAULT_TITILE_BAR_HEIGHT = 30 # 默认标题栏高度

    def __init__(self,
        parent: QWidget = ...,
    ):
        super().__init__(parent)

        self.Window = parent if isinstance(parent, (QMainWindow, QDialog)) else parent.window()
        self.Window.installEventFilter(self)

        self.setFixedHeight(self.DEFAULT_TITILE_BAR_HEIGHT)
        self.setGeometry(0, 0, self.Window.width(), self.height())

        self.MinimizeButton = self.setMinimizeButton(parent = self)
        self.MinimizeButton.clicked.connect(self.setMinimizeEvent)
        self.MaximizeButton = self.setMaximizeButton(parent = self)
        self.MaximizeButton.clicked.connect(self.setMaximizeEvent)
        self.CloseButton = self.setCloseButton(parent = self)
        self.CloseButton.clicked.connect(self.setCloseEvent)

        self.HBoxLayout = QHBoxLayout(self)
        self.HBoxLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.HBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.HBoxLayout.setSpacing(0)
        self.HBoxLayout.addStretch(1)
        self.HBoxLayout.addWidget(self.MinimizeButton, stretch = 0, alignment = Qt.AlignRight)
        self.HBoxLayout.addWidget(self.MaximizeButton, stretch = 0, alignment = Qt.AlignRight)
        self.HBoxLayout.addWidget(self.CloseButton, stretch = 0, alignment = Qt.AlignRight)

        ComponentsSignals.Signal_SetTheme.connect(self.InitDefaultStyleSheet) if self.isVisible() else None
        self.InitDefaultStyleSheet('Auto')

    '''
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if 0 < event.position().y() < self.height() and event.buttons() == Qt.MouseButton.LeftButton:
            self.setMaximizeEvent()
    '''

    def resizeEvent(self, event: QResizeEvent):
        self.resize(self.Window.width(), self.DEFAULT_TITILE_BAR_HEIGHT)

    def setCloseEvent(self):
        self.Window.close()

    def setMaximizeEvent(self):
        self.Window.showNormal() if self.Window.isMaximized() else self.Window.showMaximized()

    def setMinimizeEvent(self):
        self.Window.showMinimized()

    def setCloseButton(self, parent):
        CloseButton = QPushButton("", parent)
        CloseButton.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        CloseButton.setStyleSheet(
            "QPushButton {"
            "   image: url(:/Button_Icon/Sources/X.png);"
            "   background-color: transparent;"
            "   padding: 6.6px;"
            "   border-width: 0px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(210, 123, 123, 210);"
            "}"
        )
        CloseButton.setCursor(Qt.PointingHandCursor)
        return CloseButton

    def setMaximizeButton(self, parent):
        MaximizeButton = QPushButton("", parent)
        MaximizeButton.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        MaximizeButton.setStyleSheet(
            "QPushButton {"
            "   image: url(:/Button_Icon/Sources/FullScreen.png);"
            "   background-color: transparent;"
            "   padding: 6.6px;"
            "   border-width: 0px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(123, 123, 123, 123);"
            "}"
        )
        MaximizeButton.setCursor(Qt.PointingHandCursor)
        return MaximizeButton

    def setMinimizeButton(self, parent):
        MinimizeButton = QPushButton("", parent)
        MinimizeButton.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        MinimizeButton.setStyleSheet(
            "QPushButton {"
            "   image: url(:/Button_Icon/Sources/Dash.png);"
            "   background-color: transparent;"
            "   padding: 6.6px;"
            "   border-width: 0px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(123, 123, 123, 123);"
            "}"
        )
        MinimizeButton.setCursor(Qt.PointingHandCursor)
        return MinimizeButton

    def setTitle(self, Text: str, parent):
        TitleLabel = QLabel(Text, parent)
        TitleLabel.setGeometry(0 + 33, 0 + self.height() / 5, self.width() / 2, self.height())
        TitleLabel.setStyleSheet(
            "QLabel {"
            "   color: rgba(210, 210, 210, 210);"
            "   background-color: transparent;"
            "   padding: 3.3px;"
            "   border-width: 0px;"
            "   border-style: solid;"
            "}"
        )
        #TitleLabel.setFont(QFont("Microsoft YaHei", 11.1, QFont.Normal))
        TitleLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    def InitDefaultStyleSheet(self, Theme: str) -> None:
        super().setStyleSheet(Function_GetStyleSheet('Bar', Theme))

    def ClearDefaultStyleSheet(self) -> None:
        ComponentsSignals.Signal_SetTheme.disconnect(self.InitDefaultStyleSheet)

##############################################################################################################################

class MARGINS(Structure):
    '''
    typedef struct _MARGINS {
        int cxLeftWidth;
        int cxRightWidth;
        int cyTopHeight;
        int cyBottomHeight;
    } MARGINS, *PMARGINS;
    '''
    _fields_ = [
        ("cxLeftWidth",    c_int),
        ("cxRightWidth",   c_int),
        ("cyTopHeight",    c_int),
        ("cyBottomHeight", c_int),
    ]


PMARGINS = POINTER(MARGINS)


class WINDOWPOS(Structure):
    '''
    typedef struct tagWINDOWPOS {
        HWND hwnd;
        HWND hwndInsertAfter;
        int  x;
        int  y;
        int  cx;
        int  cy;
        UINT flags;
    } WINDOWPOS, *LPWINDOWPOS, *PWINDOWPOS;
    '''
    _fields_ = [
        ('hwnd',            HWND),
        ('hwndInsertAfter', HWND),
        ('x',               c_int),
        ('y',               c_int),
        ('cx',              c_int),
        ('cy',              c_int),
        ('flags',           UINT)
    ]


PWINDOWPOS = POINTER(WINDOWPOS)


class NCCALCSIZE_PARAMS(Structure):
    '''
    typedef struct tagNCCALCSIZE_PARAMS {
        RECT       rgrc[3];
        PWINDOWPOS lppos;
    } NCCALCSIZE_PARAMS, *LPNCCALCSIZE_PARAMS;
    '''
    _fields_ = [
        ('rgrc',  RECT*3),
        ('lppos', PWINDOWPOS)
    ]


class WindowBase:
    '''
    '''
    showed = Signal()
    closed = Signal()

    rectChanged = Signal(QRect)

    edge_size = 3 # 窗体边缘尺寸（出现缩放标记的范围）

    def __init__(self,
        min_width = 630, # 窗体的最小宽度
        min_height = 420, # 窗体的最小高度
    ):
        self.resize(min_width, min_height)

        self.TitleBar = TitleBarBase(self)

        self.Mask = QLabel(self)
        self.rectChanged.connect(self.Mask.setGeometry)
        self.Mask.setStyleSheet('background-color: rgba(0, 0, 0, 111);')
        self.Mask.setAlignment(Qt.AlignCenter)
        self.Mask.setFont(QFont('Microsoft YaHei', int(min_height / 10), QFont.Bold))
        self.Mask.hide()

    def _check_ifdraggable(self, pos) -> bool:
        return 0 < pos.x() < self.width() and 0 < pos.y() < self.TitleBar.height()

    def _move_window(self, pos) -> None:
        self.windowHandle().startSystemMove()
        QApplication.instance().postEvent(
            self.windowHandle(),
            QMouseEvent(
                QEvent.MouseButtonRelease,
                QPoint(-1, -1),
                Qt.LeftButton,
                Qt.NoButton,
                Qt.NoModifier
            )
        )

    def _resize_window(self, pos, edges) -> None:
        self.windowHandle().startSystemResize(edges) if edges is not None else None

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self._check_ifdraggable(event.position()) == True and event.buttons() == Qt.MouseButton.LeftButton:
            self.setCursor(Qt.CursorShape.OpenHandCursor)
            self._move_window(event.position())

    def mousePressEvent(self, event: QMouseEvent) -> None:
        '''
        if self._check_ifdraggable(event.position()) == True and event.buttons() == Qt.MouseButton.LeftButton:
            self.setCursor(Qt.CursorShape.OpenHandCursor)
            self._move_window(event.position())
        '''

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if self._check_ifdraggable(event.position()) == True:
            self.setCursor(Qt.CursorShape.ArrowCursor)
            self._resize_window(event.position(), None)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if self._check_ifdraggable(event.position()) == True and event.buttons() == Qt.MouseButton.LeftButton:
            self.showNormal() if self.isMaximized() else self.showMaximized() #self.setWindowState(Qt.WindowState.WindowMaximized)

    def showEvent(self, event: QShowEvent) -> None:
        self.showed.emit()
        event.accept()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.closed.emit()
        event.accept()

    def moveEvent(self, event: QMoveEvent) -> None:
        self.rectChanged.emit(self.rect())

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.rectChanged.emit(self.rect())
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def nativeEvent(self, eventType, message):
        Message = MSG.from_address(int(message))
        if Message.message == win32con.WM_NCCALCSIZE:
            if Message.wParam != 0:
                Rect = NCCALCSIZE_PARAMS.from_address(Message.lParam).rgrc[0]
                MissingHBorderPixels, MissingVBorderPixels = GetMissingBorderPixels(Message.hWnd) if IsWindowMaximized(Message.hWnd) and not IsWindowFullScreen(Message.hWnd) else (0, 0)
                Rect.left += MissingHBorderPixels
                Rect.top += MissingVBorderPixels
                Rect.right -= MissingHBorderPixels
                Rect.bottom -= MissingVBorderPixels
                return True, win32con.WVR_REDRAW
            else:
                Rect = LPRECT.from_address(Message.lParam)
                return True, 0
        if Message.message == win32con.WM_NCHITTEST:
            border_width = self.edge_size if not IsWindowMaximized(Message.hWnd) and not IsWindowFullScreen(Message.hWnd) else 0
            left   = QCursor.pos().x() - self.x() < border_width
            top    = QCursor.pos().y() - self.y() < border_width
            right  = QCursor.pos().x() - self.x() > self.frameGeometry().width() - border_width
            bottom = QCursor.pos().y() - self.y() > self.frameGeometry().height() - border_width
            if True not in (left, top, right, bottom):
                pass
            elif left and top:
                return True, win32con.HTTOPLEFT
            elif left and bottom:
                return True, win32con.HTBOTTOMLEFT
            elif right and top:
                return True, win32con.HTTOPRIGHT
            elif right and bottom:
                return True, win32con.HTBOTTOMRIGHT
            elif left:
                return True, win32con.HTLEFT
            elif top:
                return True, win32con.HTTOP
            elif right:
                return True, win32con.HTRIGHT
            elif bottom:
                return True, win32con.HTBOTTOM
        return QWidget.nativeEvent(self, eventType, message)

    def setFrameless(self, SetStrechable: bool = True, SetDropShadowEffect: bool = True) -> None:
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        hWnd = self.winId()
        Index = win32con.GWL_STYLE
        Value = win32gui.GetWindowLong(hWnd, Index)
        win32gui.SetWindowLong(hWnd, Index, Value | win32con.WS_THICKFRAME | win32con.WS_CAPTION)
        if not SetStrechable:
            self.edge_size = 0
        if SetDropShadowEffect:
            ExtendFrameIntoClientArea = WinDLL("dwmapi").DwmExtendFrameIntoClientArea
            ExtendFrameIntoClientArea.argtypes = [c_int, PMARGINS]
            ExtendFrameIntoClientArea(hWnd, byref(MARGINS(-1, -1, -1, -1)))

    def setTitleBar(self, TitleBar: Optional[QWidget]) -> None:
        try:
            self.TitleBar.deleteLater()
            self.TitleBar.hide()
            ComponentsSignals.Signal_SetTheme.disconnect(
                lambda Theme: self.TitleBar.setStyleSheet(Function_GetStyleSheet('Bar', Theme))
            )
        except:
            pass
        if TitleBar is not None:
            self.TitleBar = TitleBar
            self.TitleBar.setParent(self) if self.TitleBar.parent() is None else None
            self.TitleBar.raise_() if self.TitleBar.isHidden() else None

    def ShowMask(self, SetVisible: bool, MaskContent: Optional[str] = None) -> None:
        if SetVisible:
            self.Mask.raise_() if self.Mask.isHidden() else None
            self.Mask.setText(MaskContent) if MaskContent is not None else self.Mask.clear()
            self.Mask.show()
        else:
            self.Mask.clear()
            self.Mask.hide()


class MainWindowBase(WindowBase, QMainWindow):
    '''
    '''
    def __init__(self,
        parent: Optional[QWidget] = None,
        flags: Qt.WindowType = Qt.Window | Qt.WindowSystemMenuHint | Qt.WindowMinMaxButtonsHint,
        min_width: int = 1280,
        min_height: int = 720
    ):
        QMainWindow.__init__(self, parent, flags)
        WindowBase.__init__(self, min_width, min_height)

        self.setFrameless()

        self.CentralLayout = QGridLayout()
        self.CentralWidget = QWidget(self)
        self.CentralWidget.setObjectName('CentralWidget')
        self.CentralWidget.setLayout(self.CentralLayout)
        self.setCentralWidget(self.CentralWidget)
        ComponentsSignals.Signal_SetTheme.connect(self.InitDefaultStyleSheet)
        self.InitDefaultStyleSheet('Auto')

    def setCentralWidget(self, CentralWidget: Optional[QWidget]) -> None:
        try:
            super().takeCentralWidget(self.CentralWidget)
            self.CentralWidget.deleteLater()
            self.CentralWidget.hide()
            self.ClearDefaultStyleSheet()
        except:
            pass
        if CentralWidget is not None:
            self.CentralWidget = CentralWidget
            super().setCentralWidget(self.CentralWidget)
            self.CentralWidget.setParent(self) if self.CentralWidget.parent() is None else None
            self.CentralWidget.raise_() if self.CentralWidget.isHidden() else None

    def InitDefaultStyleSheet(self, Theme: str) -> None:
        super().setStyleSheet(Function_GetStyleSheet('Window', Theme).replace('#CentralWidget', f'#{self.CentralWidget.objectName()}'))

    def ClearDefaultStyleSheet(self) -> None:
        ComponentsSignals.Signal_SetTheme.disconnect(self.InitDefaultStyleSheet)


class ChildWindowBase(WindowBase, QWidget):
    '''
    '''
    def __init__(self,
        parent: Optional[QWidget] = None,
        f: Qt.WindowType = Qt.Widget,
        min_width: int = 630,
        min_height: int = 420
    ):
        QWidget.__init__(self, None, f) #QWidget.__init__(self, parent, f)
        WindowBase.__init__(self, min_width, min_height)

        self.setFrameless()

        self.setWindowModality(Qt.ApplicationModal)

        self.EventLoop = QEventLoop(self)

        self.showed.connect(lambda: parent.ShowMask(True)) if isinstance(parent, WindowBase) else None
        self.closed.connect(lambda: parent.ShowMask(False)) if isinstance(parent, WindowBase) else None

    def exec(self) -> int:
        self.show()
        Result = self.EventLoop.exec()
        self.closed.emit()
        return Result

    def closeEvent(self, event: QCloseEvent) -> None:
        Result = self.EventLoop.exit()
        super().closeEvent(event)


class DialogBase(WindowBase, QDialog):
    '''
    '''
    def __init__(self,
        parent: Optional[QWidget] = None,
        f: Qt.WindowType = Qt.Dialog,
        min_width: int = 630,
        min_height: int = 420
    ):
        QDialog.__init__(self, None, f) #QDialog.__init__(self, parent, f)
        WindowBase.__init__(self, min_width, min_height)

        self.setFrameless(SetStrechable = False)

        ComponentsSignals.Signal_SetTheme.connect(self.InitDefaultStyleSheet)
        self.InitDefaultStyleSheet('Auto')

        self.TitleBar.MinimizeButton.hide()
        self.TitleBar.MinimizeButton.deleteLater()
        self.TitleBar.MaximizeButton.hide()
        self.TitleBar.MaximizeButton.deleteLater()

        self.showed.connect(lambda: parent.ShowMask(True)) if isinstance(parent, WindowBase) else None
        self.closed.connect(lambda: parent.ShowMask(False)) if isinstance(parent, WindowBase) else None

    def exec(self) -> int:
        Result = super().exec()
        self.closed.emit()
        return Result

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        return

    def InitDefaultStyleSheet(self, Theme: str) -> None:
        super().setStyleSheet(Function_GetStyleSheet('Dialog', Theme))

    def ClearDefaultStyleSheet(self) -> None:
        ComponentsSignals.Signal_SetTheme.disconnect(self.InitDefaultStyleSheet)

##############################################################################################################################

class MessageBoxBase(DialogBase):
    '''
    '''
    ClickedButton = None

    StandardButtonDict = {
        QMessageBox.NoButton:        QDialogButtonBox.NoButton,
        QMessageBox.Ok:              QDialogButtonBox.Ok,
        QMessageBox.Cancel:          QDialogButtonBox.Cancel,
        QMessageBox.Yes:             QDialogButtonBox.Yes,
        QMessageBox.No:              QDialogButtonBox.No,
        QMessageBox.Retry:           QDialogButtonBox.Retry,
        QMessageBox.Ignore:          QDialogButtonBox.Ignore,
        QMessageBox.Open:            QDialogButtonBox.Open,
        QMessageBox.Close:           QDialogButtonBox.Close,
        QMessageBox.Save:            QDialogButtonBox.Save,
        QMessageBox.Discard:         QDialogButtonBox.Discard,
        QMessageBox.Apply:           QDialogButtonBox.Apply,
        QMessageBox.RestoreDefaults: QDialogButtonBox.RestoreDefaults,
        QMessageBox.Ok | QMessageBox.Cancel:             QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
        QMessageBox.Yes | QMessageBox.No:                QDialogButtonBox.Yes | QDialogButtonBox.No,
        QMessageBox.Retry | QMessageBox.Ignore:          QDialogButtonBox.Retry | QDialogButtonBox.Ignore,
        QMessageBox.Open | QMessageBox.Close:            QDialogButtonBox.Open | QDialogButtonBox.Close,
        QMessageBox.Save | QMessageBox.Discard:          QDialogButtonBox.Save | QDialogButtonBox.Discard,
        QMessageBox.Apply | QMessageBox.RestoreDefaults: QDialogButtonBox.Apply | QDialogButtonBox.RestoreDefaults
    }

    StandardIconDict = {
        QMessageBox.Question:    QStyle.SP_MessageBoxQuestion,
        QMessageBox.Information: QStyle.SP_MessageBoxInformation,
        QMessageBox.Warning:     QStyle.SP_MessageBoxWarning,
        QMessageBox.Critical:    QStyle.SP_MessageBoxCritical
    }

    def __init__(self,
        parent: Optional[QWidget] = None,
        min_width = 360,
        min_height = 210
    ):  
        super().__init__(parent, Qt.Dialog, min_width, min_height)

        self.PicLabel = QLabel()
        self.TextLabel = QLabel()
        PicTextLayout = QHBoxLayout()
        PicTextLayout.setContentsMargins(0, 0, 0, 0)
        PicTextLayout.setSpacing(0)
        PicTextLayout.addWidget(self.PicLabel, stretch = 0)
        PicTextLayout.addWidget(self.TextLabel, stretch = 1)

        self.ButtonBox = QDialogButtonBox()
        self.ButtonBox.clicked.connect(self.updateClickedButton)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)
        self.ButtonBox.setOrientation(Qt.Horizontal)
        self.ButtonBox.setStyleSheet("padding: 6px 18px 6px 18px;")

        self.Layout = QVBoxLayout(self)
        self.Layout.setContentsMargins(21, 12, 21, 12)
        self.Layout.setSpacing(12)
        self.Layout.addLayout(PicTextLayout)
        self.Layout.addWidget(self.ButtonBox)

    def updateClickedButton(self, button: QAbstractButton):
        self.ClickedButton = FindKey(self.StandardButtonDict, self.ButtonBox.standardButton(button))

    def exec(self) -> int:
        Result = super().exec()
        return self.ClickedButton# if self.ClickedButton is not None else Result

    def setStandardButtons(self, buttons: QMessageBox.StandardButton) -> None:
        buttons = self.StandardButtonDict.get(buttons, buttons)
        if isinstance(buttons, QMessageBox.StandardButton):
            pass
        self.ButtonBox.setStandardButtons(buttons)

    def setWindowIcon(self, icon: Union[QIcon, QPixmap, QStyle.StandardPixmap]) -> None:
        icon = self.StandardIconDict.get(icon, icon)
        if isinstance(icon, QStyle.StandardPixmap):
            icon = QApplication.style().standardIcon(icon)
        if isinstance(icon, (QIcon, QPixmap)):
            pass
        super().setWindowIcon(icon)

    def setIcon(self, icon: Union[QIcon, QPixmap, QStyle.StandardPixmap]) -> None:
        icon = self.StandardIconDict.get(icon, icon)
        Length = int(min(self.width(), self.height()) / 6)
        if isinstance(icon, QStyle.StandardPixmap):
            standardIcon = QApplication.style().standardIcon(icon)
            icon = standardIcon.pixmap(standardIcon.actualSize(QSize(Length, Length)))
        if isinstance(icon, QIcon):
            icon = icon.pixmap(icon.actualSize(QSize(Length, Length)))
        if isinstance(icon, QPixmap):
            pass
        self.PicLabel.setPixmap(icon)

    def setText(self, text: str, textsize: float = 11.1, textweight: int = 420):
        Function_SetText(
            Widget = self.TextLabel,
            Text = SetRichText(
                Title = text,
                TitleSize = textsize,
                TitleWeight = textweight,
                TitleAlign = 'center'
            )
        )

##############################################################################################################################