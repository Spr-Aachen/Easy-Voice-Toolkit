import enum
from dataclasses import dataclass
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPainter, QPaintEvent
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel


class CustomTitleBar:
    '''
    自定义标题栏
    '''
    def __init__(self, window: QtWidgets, window_title: str = ""):
        self.window = window

        self.DEFAULT_TITILE_BAR_HEIGHT = 27 # 默认标题栏高度

        self.mouseDoubleClickEvent_parent = self.window.mouseDoubleClickEvent # 存储父类的双击事件
        self.window.mouseDoubleClickEvent = self.mouseDoubleClickEvent # 将本类的双击事件赋值给将父类的双击事件

        self.resizeEvent_parent = self.window.resizeEvent # 存储父类的窗口大小改变事件
        self.window.resizeEvent = self.resizeEvent # 将本类的窗口大小改变事件赋值给将父类的窗口大小改变事件

        self.window.setContentsMargins(0, self.DEFAULT_TITILE_BAR_HEIGHT, 0, 0) # 设置ui文件里main_layout上边距，以免遮挡标题栏

        self.window.setWindowFlags(
            Qt.Window
            | Qt.FramelessWindowHint
            | Qt.WindowSystemMenuHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowMaximizeButtonHint
        ) # 设置无边框

        #self.window.setAttribute(Qt.WA_TranslucentBackground) # 设置透明背景

        # 添加自定义的标题栏到最顶部
        self.title = QLabel(window_title, self.window)
        self.title.setGeometry(0, 0, self.window.width(), self.DEFAULT_TITILE_BAR_HEIGHT)
        self.title.setStyleSheet(
            "QLabel"
            "{"
                "background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(63, 63, 63, 210), stop:1 rgba(51, 51, 51, 210));"
                "color: rgba(210, 210, 210, 210);"
                "padding: 3.3px;"
                "border-width: 0px;"
                #"border-top-left-radius: 3px;"
                #"border-top-right-radius: 3px;"
                "border-style: solid;"
                #"border-color: rgb(111, 111, 111);"
            "}"
        )
        self.title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.title.setFont(QFont("Microsoft YaHei", 11.1, QFont.Normal))
        self.title.setMouseTracking(True)

        # 添加关闭按钮
        self.close_btn = QPushButton("", self.window)
        self.close_btn.setGeometry(self.window.width() - 33, 6, 15, 15)
        self.close_btn.setStyleSheet(
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
        self.close_btn.setCursor(Qt.PointingHandCursor)
        self.close_btn.setToolTipDuration(-1)
        self.close_btn.setToolTip("Close 关闭")
        self.close_btn.clicked.connect(self.window.close) # 绑定窗口关闭事件

        # 添加最大化按钮
        self.max_btn = QPushButton("", self.window)
        self.max_btn.setGeometry(self.window.width() - 66, 6, 15, 15)
        self.max_btn.setStyleSheet(
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
        self.max_btn.setCursor(Qt.PointingHandCursor)
        self.max_btn.setToolTipDuration(-1)
        self.max_btn.setToolTip("Maximize 最大化")
        self.max_btn.clicked.connect(self.setMaxEvent) # 绑定窗口最大化事件（自定义函数）

        # 添加最小化按钮
        self.min_btn = QPushButton("", self.window)
        self.min_btn.setGeometry(self.window.width() - 99, 6, 15, 15)
        self.min_btn.setStyleSheet(
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
        self.min_btn.setCursor(Qt.PointingHandCursor)
        self.min_btn.setToolTipDuration(-1)
        self.min_btn.setToolTip("Minimize 最小化")
        self.min_btn.clicked.connect(self.window.showMinimized) # 绑定窗口最小化事件

    def setMaxEvent(self):
        '''
        窗口最大化事件和恢复事件
        '''
        if self.window.isMaximized():
            self.window.showNormal()
            self.max_btn.setToolTip("Restore 还原")
        else:
            self.window.showMaximized()
            self.max_btn.setToolTip("Maximize 最大化")

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        '''
        鼠标双击事件
        '''
        # 如果双击的是鼠标左键且在标题栏范围内，则放大缩小窗口
        if a0.button() == Qt.MouseButton.LeftButton and a0.position().y() < self.title.height():
            self.setMaxEvent()
        return self.mouseDoubleClickEvent_parent(a0)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        '''
        窗口缩放事件
        '''
        # 最大化最小化的时候，需要去改变按钮组位置
        self.close_btn.move(self.window.width() - 33, 6)
        self.max_btn.move(self.window.width() - 66, 6)
        self.min_btn.move(self.window.width() - 99, 6)
        self.title.resize(self.window.width(), self.DEFAULT_TITILE_BAR_HEIGHT)
        return self.resizeEvent_parent(a0)


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


class Window_Customizing(QMainWindow):
    def __init__(self,
        parent = None,
        window_title = "Title"
    ):
        super().__init__(parent)

        CustomTitleBar(self, window_title = window_title)

        self.setMouseTracking(True)

        self.resize(100, 100)

        self.setWindowFlags(
            Qt.Window
            | Qt.FramelessWindowHint
            | Qt.WindowSystemMenuHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowMaximizeButtonHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.edge_press = EdgePress() # 拖放标记

        self.edge_size = 6 # 窗体边缘尺寸（出现缩放标记的范围）

        self.min_width = 60 # 窗体的最小宽度
        self.min_height = 24 # 窗体的最小高度

        self.move_event_height = 27 # 顶部可移动窗口高度

    def paintEvent(self, event: QPaintEvent) -> None:
        '''
        设置边框
        '''
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing) # 设置抗锯齿，不然边框会有明显锯齿
        painter.setBrush(Qt.white) # 设置窗体颜色
        #painter.drawRoundedRect(self.rect(), 3, 3) #画边框圆角
        super().paintEvent(event)

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

    def _get_move_edges(self, pos):
        '''
        获取移动窗口事件标记
        '''
        in_move_edge: bool = pos.y() <= self.move_event_height # 是否在可移动区域内
        not_in_edges: bool = self._get_edges(pos) == Edge.NoEdge # 是否在非缩放区域内
        return in_move_edge and not_in_edges

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

    def resizeEvent(self, event):
        '''
        处理窗口大小更改事件
        '''
        self.setCursor(Qt.CursorShape.ArrowCursor)