import enum
from dataclasses import dataclass
from PySide6.QtCore import Qt, QObject
from PySide6.QtGui import QFont, QPainter, QPaintEvent, QResizeEvent, QMouseEvent
from PySide6.QtWidgets import *

from .QFunctions import *

##############################################################################################################################

class TitleBarBase(QFrame):
    '''
    '''
    def __init__(self,
        parent: Optional[QWidget] = None
    ):
        super().__init__(parent)

        self.setStyleSheet(Function_GetStyleSheet('Bar'))
        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Bar', Theme))
        )

        self.setMouseTracking(True)


class CustomizeTitleBar:
    '''
    自定义标题栏
    '''
    def __init__(self,
        Window: Optional[QWidget] = None,
        ExistedTitleBar: Optional[QWidget] = None
    ):
        if ExistedTitleBar is None:
            self.IsTitleBarExisted = False
            self.TitleBar = TitleBarBase()
        else:
            self.IsTitleBarExisted = True
            self.TitleBar = ExistedTitleBar
            if isinstance(self.TitleBar, TitleBarBase) == False:
                self.TitleBar.setStyleSheet(Function_GetStyleSheet('Bar'))
                ComponentsSignals.Signal_SetTheme.connect(
                    lambda Theme:  self.TitleBar.setStyleSheet(Function_GetStyleSheet('Bar', Theme))
                )

        self.DEFAULT_TITILE_BAR_HEIGHT = 30 # 默认标题栏高度
        self.YAxis = self.DEFAULT_TITILE_BAR_HEIGHT / 5
        self.Width = self.DEFAULT_TITILE_BAR_HEIGHT / 2
        self.Height = self.DEFAULT_TITILE_BAR_HEIGHT / 2

        self.Window = Window if isinstance(Window, QWidget) else self.TitleBar.topLevelWidget()
        self.MouseDoubleClickEvent_Parent = self.Window.mouseDoubleClickEvent # 存储父类的双击事件
        self.ResizeEvent_Parent = self.Window.resizeEvent # 存储父类的窗口大小改变事件

        self.CloseButton = self.setCloseButton()
        self.MaximizeButton = self.setMaximizeButton()
        self.MinimizeButton = self.setMinimizeButton()

        #self.SetUp()
    
    def setTitle(self, Text: str):
        TitleLabel = QLabel(Text, self.Window)
        TitleLabel.setGeometry(0 + 33, self.YAxis, self.Width, self.Height)
        TitleLabel.setStyleSheet(
            "QLabel"
            "{"
                "background-color: transparent;"
                "color: rgba(210, 210, 210, 210);"
                "padding: 3.3px;"
                "border-width: 0px;"
                #"border-top-left-radius: 3px;"
                #"border-top-right-radius: 3px;"
                "border-style: solid;"
                #"border-color: rgb(111, 111, 111);"
            "}"
        )
        #TitleLabel.setFont(QFont("Microsoft YaHei", 11.1, QFont.Normal))
        TitleLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    def setCloseEvent(self):
        self.Window.close()

    def setMaximizeEvent(self):
        self.Window.showNormal() if self.Window.isMaximized() else self.Window.showMaximized()

    def setMinimizeEvent(self):
        self.Window.showMinimized()

    def setCloseButton(self):
        CloseButton = QPushButton("", self.Window)
        CloseButton.setGeometry(self.Window.width() - 33, self.YAxis, self.Width, self.Height)
        CloseButton.setStyleSheet(
            "QPushButton"
            "{"
                "background: rgba(210, 123, 123, 0.6);"
                "border-radius: 6.6px;"
            "}"
            "QPushButton:hover"
            "{"
                "background: rgba(210, 123, 123, 0.9);"
            "}"

            "QToolTip"
            "{"
                "color: rgba(255, 255, 255, 210);"
                "background-color: transparent;"
                "border-width: 0px;"
                "border-style: solid;"
            "}"
        )
        CloseButton.setCursor(Qt.PointingHandCursor)
        CloseButton.clicked.connect(self.setCloseEvent)
        CloseButton.setToolTipDuration(-1)
        CloseButton.setToolTip("Close 关闭")
        return CloseButton

    def setMaximizeButton(self):
        MaximizeButton = QPushButton("", self.Window)
        MaximizeButton.setGeometry(self.Window.width() - 66, self.YAxis, self.Width, self.Height)
        MaximizeButton.setStyleSheet(
            "QPushButton"
            "{"
                "background: rgba(210, 210, 123, 0.6);"
                "border-radius: 6.6px;"
            "}"
            "QPushButton:hover"
            "{"
                "background: rgba(210, 210, 123, 0.9);"
            "}"

            "QToolTip"
            "{"
                "color: rgba(255, 255, 255, 210);"
                "background-color: transparent;"
                "border-width: 0px;"
                "border-style: solid;"
            "}"
        )
        MaximizeButton.setCursor(Qt.PointingHandCursor)
        MaximizeButton.clicked.connect(self.setMaximizeEvent)
        MaximizeButton.setToolTipDuration(-1)
        MaximizeButton.setToolTip("Restore 还原") if self.Window.isMaximized() else MaximizeButton.setToolTip("Maximize 最大化")
        return MaximizeButton

    def setMinimizeButton(self):
        MinimizeButton = QPushButton("", self.Window)
        MinimizeButton.setGeometry(self.Window.width() - 99, self.YAxis, self.Width, self.Height)
        MinimizeButton.setStyleSheet(
            "QPushButton"
            "{"
                "background: rgba(123, 210, 123, 0.6);"
                "border-radius: 6.6px;"
            "}"
            "QPushButton:hover"
            "{"
                "background: rgba(123, 210, 123, 0.9);"
            "}"

            "QToolTip"
            "{"
                "color: rgba(255, 255, 255, 210);"
                "background-color: transparent;"
                "border-width: 0px;"
                "border-style: solid;"
            "}"
        )
        MinimizeButton.setCursor(Qt.PointingHandCursor)
        MinimizeButton.clicked.connect(self.setMinimizeEvent)
        MinimizeButton.setToolTipDuration(-1)
        MinimizeButton.setToolTip("Minimize 最小化")
        return MinimizeButton

    def mouseDoubleClickEvent(self, a0: QMouseEvent) -> None:
        '''
        鼠标双击事件
        '''
        # 如果双击的是鼠标左键且在标题栏范围内，则放大缩小窗口
        if a0.button() == Qt.MouseButton.LeftButton and a0.position().y() < self.TitleBar.height():
            self.setMaximizeEvent()
        return self.MouseDoubleClickEvent_Parent(a0)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        '''
        窗口缩放事件
        '''
        self.TitleBar.resize(self.Window.width(), self.DEFAULT_TITILE_BAR_HEIGHT)
        # 最大化最小化的时候，需要去改变按钮组位置
        self.CloseButton.move(self.Window.width() - 33, self.YAxis)
        self.MaximizeButton.move(self.Window.width() - 66, self.YAxis)
        self.MinimizeButton.move(self.Window.width() - 99, self.YAxis)
        return self.ResizeEvent_Parent(a0)

    def SetUp(self):
        if self.IsTitleBarExisted == False:
            self.setTitle("Title - by Spr_Aachen")
            self.TitleBar.setGeometry(0, 0, self.Window.width(), self.DEFAULT_TITILE_BAR_HEIGHT) # 将自定义的标题栏置于最顶部
            self.Window.setContentsMargins(0, self.DEFAULT_TITILE_BAR_HEIGHT, 0, 0) # 设置ui文件里main_layout上边距，以免遮挡标题栏
        self.Window.mouseDoubleClickEvent = self.mouseDoubleClickEvent # 将本类的双击事件赋值给将父类的双击事件
        self.Window.resizeEvent = self.resizeEvent # 将本类的窗口大小改变事件赋值给将父类的窗口大小改变事件

##############################################################################################################################

class Edge(enum.Flag):
    '''
    边缘类型枚举
    '''
    NoEdge: Qt.Edge = 0  # 不在边缘地带

    TopEdge: Qt.Edge = 1  # 顶部边缘
    LeftEdge: Qt.Edge = 2  # 左部边缘
    RightEdge: Qt.Edge = 3.  # 右部边缘
    BottomEdge: Qt.Edge = 4  # 底部边缘

    LeftTopEdge: Qt.Edge = 5  # 左顶部边缘
    RightTopEdge: Qt.Edge = 6  # 右顶部边缘
    LeftBottomEdge: Qt.Edge = 7  # 左底部边缘
    RightBottomEdge: Qt.Edge = 8  # 右底部边缘


@dataclass
class EdgePress:
    '''
    边缘按下区域类型
    '''
    leftEdgePress: bool = False
    rightEdgePress: bool = False
    topEdgePress: bool = False
    bottomEdgePress: bool = False
    leftTopEdgePress: bool = False
    rightBottomEdgePress: bool = False
    leftBottomEdgePress: bool = False
    rightTopEdgePress: bool = False
    moveEdgePress: bool = False
    movePosition = None # 点击时的窗口初始位置


class MainWindowBase(QMainWindow):
    '''
    '''
    def __init__(self,
        parent: Optional[QWidget] = None,
        SetTitleBar: bool = True
    ):
        super().__init__(parent)

        self.setStyleSheet(Function_GetStyleSheet('Window'))
        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Window', Theme))
        )

        self.setWindowFlags(
            Qt.Window
            | Qt.FramelessWindowHint
            | Qt.WindowSystemMenuHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowMaximizeButtonHint
        ) # 设置无边框

        self.CustomizeTitleBar = CustomizeTitleBar(self)
        self.CustomizeTitleBar.SetUp() if SetTitleBar else None

        self.setMouseTracking(True)

        self.edge_press = EdgePress() # 拖放标记

        self.edge_size = 3 # 窗体边缘尺寸（出现缩放标记的范围）

        self.min_width = 1280 # 窗体的最小宽度
        self.min_height = 720 # 窗体的最小高度

        self.move_event_height = 30 # 顶部可移动窗口高度

    def paintEvent(self, event: QPaintEvent) -> None:
        '''
        设置边框
        '''
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing) # 设置抗锯齿，不然边框会有明显锯齿
        painter.setBrush(Qt.white) # 设置窗体颜色
        #painter.drawRoundedRect(self.rect(), 3, 3) #画边框圆角
        super().paintEvent(event)

    def _get_edge_press(self):
        '''
         边缘按下区域类型
        '''
        if self.edge_press.leftEdgePress:
            return Edge.LeftEdge
        elif self.edge_press.rightEdgePress:
            return Edge.RightEdge
        elif self.edge_press.topEdgePress:
            return Edge.TopEdge
        elif self.edge_press.bottomEdgePress:
            return Edge.BottomEdge
        elif self.edge_press.leftTopEdgePress:
            return Edge.LeftTopEdge
        elif self.edge_press.rightBottomEdgePress:
            return Edge.RightBottomEdge
        elif self.edge_press.leftBottomEdgePress:
            return Edge.LeftBottomEdge
        elif self.edge_press.rightTopEdgePress:
            return Edge.RightTopEdge
        else:
            return Edge.NoEdge

    def _resize_window(self, pos):
        '''
        缩放窗口
        '''
        edges = self._get_edge_press() # 判断按下时的区域是哪一块
        geo = self.frameGeometry() # 获取窗口的初始大小
        x, y, width, height = geo.x(), geo.y(), geo.width(), geo.height() # 获取窗口的初始位置
        if edges is Edge.LeftEdge:
            width -= pos.x()
            if width <= self.min_width:
                return
            else:
                x += pos.x()
        elif edges is Edge.RightEdge:
            width = pos.x()
            if width <= self.min_width:
                return
        elif edges is Edge.TopEdge:
            height -= pos.y()
            if height <= self.min_height:
                return
            else:
                y += pos.y()
        elif edges is Edge.BottomEdge:
            height = pos.y()
            if height <= self.min_height:
                return
        elif edges is Edge.LeftTopEdge:
            width -= pos.x()
            if width <= self.min_width:
                width = geo.width()
            else:
                x += pos.x()
            height -= pos.y()
            if height <= self.min_height:
                height = geo.height()
            else:
                y += pos.y()
        elif edges is Edge.LeftBottomEdge:
            width -= pos.x()
            if width <= self.min_width:
                width = geo.width()
            else:
                x += pos.x()
            height = pos.y()
            if height <= self.min_height:
                height = geo.height()
        elif edges is Edge.RightTopEdge:
            width = pos.x()
            if width <= self.min_width:
                width = geo.width()
            height -= pos.y()
            if height <= self.min_height:
                height = geo.height()
            else:
                y += pos.y()
        elif edges is Edge.RightBottomEdge:
            width = pos.x()
            if width <= self.min_width:
                width = geo.width()
            height = pos.y()
            if height <= self.min_height:
                height = geo.height()
        self.setGeometry(x, y, width, height)

    def mouseMoveEvent(self, event):
        '''
        根据鼠标按钮是否按下来检查鼠标位置与更新窗口光标
        '''
        if event.buttons() == Qt.MouseButton.NoButton:
            pos = event.globalPosition().toPoint() - self.pos()
            edges = self._get_edges(pos)
            if edges == Edge.LeftEdge or edges == Edge.RightEdge:
                self.setCursor(Qt.SizeHorCursor)
            elif edges == Edge.TopEdge or edges == Edge.BottomEdge:
                self.setCursor(Qt.SizeVerCursor)
            elif edges == Edge.LeftTopEdge or edges == Edge.RightBottomEdge:
                self.setCursor(Qt.CursorShape.SizeFDiagCursor)
            elif edges == Edge.LeftBottomEdge or edges == Edge.RightTopEdge:
                self.setCursor(Qt.CursorShape.SizeBDiagCursor)
            else:
                self.setCursor(Qt.CursorShape.ArrowCursor)
    
        elif event.buttons() == Qt.MouseButton.LeftButton:
            if self.edge_press.moveEdgePress:
                self.move(event.globalPosition().toPoint() - self.edge_press.movePosition) # 移动窗口
            elif self._get_edge_press() is not Edge.NoEdge:
                self._resize_window(event.globalPosition().toPoint() - self.pos()) # 缩放窗口

    def mouseReleaseEvent(self, event) -> None:
        self.edge_press.leftEdgePress = False
        self.edge_press.rightEdgePress = False
        self.edge_press.topEdgePress = False
        self.edge_press.bottomEdgePress = False
        self.edge_press.leftTopEdgePress = False
        self.edge_press.rightBottomEdgePress = False
        self.edge_press.leftBottomEdgePress = False
        self.edge_press.rightTopEdgePress = False
        self.edge_press.moveEdgePress = False
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def _get_edges(self, pos):
        '''
        获取边缘类型
        '''
        edges = Edge.NoEdge
 
        in_left_edge: bool = pos.x() <= self.edge_size # 左
        in_right_edge: bool = pos.x() >= (self.width() - self.edge_size) # 右
        in_top_edge: bool = pos.y() <= self.edge_size # 上
        in_bottom_edge: bool = pos.y() >= (self.height() - self.edge_size) # 下

        size = len([i for i in [in_left_edge, in_right_edge, in_top_edge, in_bottom_edge] if i])

        if size == 0:
            return edges
        if size == 1:
            if in_left_edge:
                return Edge.LeftEdge
            if in_right_edge:
                return Edge.RightEdge
            if in_top_edge:
                return Edge.TopEdge
            if in_bottom_edge:
                return Edge.BottomEdge
        if size == 2:
            if in_left_edge and in_top_edge:
                return Edge.LeftTopEdge
            if in_left_edge and in_bottom_edge:
                return Edge.LeftBottomEdge
            if in_right_edge and in_top_edge:
                return Edge.RightTopEdge
            if in_right_edge and in_bottom_edge:
                return Edge.RightBottomEdge

    def _get_move_edges(self, pos):
        '''
        获取移动窗口事件标记
        '''
        in_move_edge: bool = pos.y() <= self.move_event_height # 是否在可移动区域内
        not_in_edges: bool = self._get_edges(pos) == Edge.NoEdge # 是否在非缩放区域内
        return in_move_edge and not_in_edges

    def mousePressEvent(self, event) -> None:
        pos = event.globalPosition().toPoint() - self.pos()
        edges = self._get_edges(pos)
        if edges == Edge.LeftEdge:
            self.edge_press.leftEdgePress = True
        elif edges == Edge.RightEdge:
            self.edge_press.rightEdgePress = True
        elif edges == Edge.TopEdge:
            self.edge_press.topEdgePress = True
        elif edges == Edge.BottomEdge:
            self.edge_press.bottomEdgePress = True
        elif edges == Edge.LeftTopEdge:
            self.edge_press.leftTopEdgePress = True
        elif edges == Edge.RightBottomEdge:
            self.edge_press.rightBottomEdgePress = True
        elif edges == Edge.LeftBottomEdge:
            self.edge_press.leftBottomEdgePress = True
        elif edges == Edge.RightTopEdge:
            self.edge_press.rightTopEdgePress = True
        else: # 移动事件
            if self._get_move_edges(pos):
                self.edge_press.moveEdgePress = True
                self.edge_press.movePosition = event.globalPosition().toPoint() - self.pos()
                self.setCursor(Qt.CursorShape.OpenHandCursor)

    def resizeEvent(self, event):
        '''
        处理窗口大小更改事件
        '''
        self.setCursor(Qt.CursorShape.ArrowCursor)

##############################################################################################################################