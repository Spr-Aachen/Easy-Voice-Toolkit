import win32gui
import win32con
from ctypes import Structure, c_int, POINTER, WinDLL, byref
from ctypes.wintypes import UINT, HWND, RECT, MSG, LPRECT
from PySide6.QtCore import Qt, QPoint, QEvent
from PySide6.QtGui import QGuiApplication, QCursor, QMouseEvent, QResizeEvent
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

        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Bar', Theme))
        ) if self.isVisible() else None
        ComponentsSignals.Signal_SetTheme.emit('Auto')

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
    edge_size = 3 # 窗体边缘尺寸（出现缩放标记的范围）

    def __init__(self,
        min_width = 630, # 窗体的最小宽度
        min_height = 420, # 窗体的最小高度
    ):
        self.resize(min_width, min_height)

        self.TitleBar = TitleBarBase(self)

    def _check_ifdraggable(self, pos) -> bool:
        return 0 < pos.x() < self.width()# and 0 < pos.y() < self.TitleBar.height()

    def _move_window(self, pos) -> None:
        self.windowHandle().startSystemMove()
        QApplication.instance().postEvent(
            receiver = self.windowHandle(),
            event = QMouseEvent(
                type = QEvent.MouseButtonRelease,
                localPos = QPoint(-1, -1),
                button = Qt.LeftButton,
                buttons = Qt.NoButton,
                modifiers = Qt.NoModifier
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

    def resizeEvent(self, event: QResizeEvent):
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def nativeEvent(self, eventType, message):
        Message = MSG.from_address(int(message))
        if Message.message == win32con.WM_NCCALCSIZE:
            if Message.wParam != 0:
                Rect = NCCALCSIZE_PARAMS.from_address(Message.lParam).rgrc[0]
                '''
                def GetMissingBorderPixels(hWnd: int):
                    for Window in QGuiApplication.allWindows():
                        if Window.winId() == hWnd:
                            MissingBorderSize = [win32con.SM_CXSIZEFRAME, win32con.SM_CYSIZEFRAME]
                            for Index, MissingBorderLength in enumerate(MissingBorderSize):
                                MissingBorderPixels = win32api.GetSystemMetrics(MissingBorderLength) + win32api.GetSystemMetrics(win32con.SM_CXPADDEDBORDER)
                                if MissingBorderPixels > 0:
                                    MissingBorderSize[Index] = MissingBorderPixels
                                else:
                                    def IsCompositionEnabled():
                                        Result = windll.dwmapi.DwmIsCompositionEnabled(byref(c_int(0)))
                                        return bool(Result.value)
                                    MissingBorderSize[Index] = round((6 if IsCompositionEnabled() else 3) * Window.devicePixelRatio())
                            return MissingBorderSize
                MissingHBorderPixels, MissingVBorderPixels = GetMissingBorderPixels(Message.hWnd)
                '''
                MissingHBorderPixels = MissingVBorderPixels = round(6 * self.devicePixelRatio())
                Rect.left -= MissingHBorderPixels
                Rect.top -= MissingVBorderPixels
                Rect.right += MissingHBorderPixels
                Rect.bottom += MissingVBorderPixels
            else:
                Rect = LPRECT.from_address(Message.lParam)
        if Message.message == win32con.WM_NCHITTEST:
            left   = QCursor.pos().x() - self.x() < self.edge_size
            top    = QCursor.pos().y() - self.y() < self.edge_size
            right  = QCursor.pos().x() - self.x() > self.width() - self.edge_size
            bottom = QCursor.pos().y() - self.y() > self.height() - self.edge_size
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
        win32gui.SetWindowLong(hWnd, Index, Value | win32con.WS_THICKFRAME & ~win32con.WS_CAPTION)
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
        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Window', Theme))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')

    def setCentralWidget(self, CentralWidget: Optional[QWidget]) -> None:
        try:
            super().takeCentralWidget(self.CentralWidget)
            self.CentralWidget.deleteLater()
            self.CentralWidget.hide()
            ComponentsSignals.Signal_SetTheme.disconnect(
                lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Window', Theme))
            )
        except:
            pass
        if CentralWidget is not None:
            self.CentralWidget = CentralWidget
            super().setCentralWidget(self.CentralWidget)
            self.CentralWidget.setParent(self) if self.CentralWidget.parent() is None else None
            self.CentralWidget.raise_() if self.CentralWidget.isHidden() else None


class DialogBase(WindowBase, QDialog):
    '''
    '''
    def __init__(self,
        parent: Optional[QWidget] = None,
        f: Qt.WindowType = Qt.Dialog,
        min_width: int = 630,
        min_height: int = 420
    ):
        QDialog.__init__(self, parent, f)
        WindowBase.__init__(self, min_width, min_height)

        self.setFrameless(SetStrechable = False)

        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Dialog', Theme))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')

        self.TitleBar.MinimizeButton.hide()
        self.TitleBar.MinimizeButton.deleteLater()
        self.TitleBar.MaximizeButton.hide()
        self.TitleBar.MaximizeButton.deleteLater()

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        return

##############################################################################################################################