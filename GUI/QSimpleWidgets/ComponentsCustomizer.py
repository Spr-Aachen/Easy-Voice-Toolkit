from PySide6.QtCore import Qt, QObject
from PySide6.QtGui import QColor, QIcon, QPainter
from PySide6.QtWidgets import *

from .QFunctions import *

##############################################################################################################################

class LineEditBase(QLineEdit):
    '''
    '''
    def __init__(self,
        arg__1: str,
        parent: Optional[QWidget] = None
    ):
        super().__init__(arg__1, parent)

        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Edit', Theme))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')


class LineEdit_NoBorder(LineEditBase):
    '''
    Check its stylesheet in qss file
    '''

##############################################################################################################################

class ToolButtonBase(QToolButton):
    '''
    '''
    def __init__(self,
        text: str,
        parent: Optional[QWidget] = None
    ):
        super().__init__(parent)

        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Button', Theme))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')

        self.setFont('Microsoft YaHei')
        self.setText(text)
    """
        self.setIconSize(QSize(16, 16))
        self.setIcon(QIcon())

        self.isPressed = False
        self.isHover = False

    def setProperty(self, name: str, value) -> bool:
        if name != 'icon':
            return super().setProperty(name, value)

        self.setIcon(value)
        return True

    def setIcon(self, icon: Union[QIcon, str]):
        self.setProperty('hasIcon', icon is not None)
        self.setStyle(QApplication.style())
        self._icon = icon or QIcon()
        self.update()

    def paintEvent(self, e):
        super().paintEvent(e)
        if self._icon is None:
            return

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing |
                               QPainter.SmoothPixmapTransform)

        if not self.isEnabled():
            painter.setOpacity(0.43)
        elif self.isPressed:
            painter.setOpacity(0.63)

        w, h = self.iconSize().width(), self.iconSize().height()
        y = (self.height() - h) / 2
        x = (self.width() - w) / 2
        Function_DrawIcon(self._icon, painter, QRectF(x, y, w, h))

    def mousePressEvent(self, e):
        self.isPressed = True
        super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        self.isPressed = False
        super().mouseReleaseEvent(e)

    def enterEvent(self, e):
        self.isHover = True
        self.update()

    def leaveEvent(self, e):
        self.isHover = False
        self.update()
    """

class ToolButton_UnderLined(ToolButtonBase):
    '''
    Check its stylesheet in qss file
    '''

##############################################################################################################################

class TableWidgetBase(QTableWidget):
    '''
    '''
    def __init__(self,
        parent: Optional[QWidget] = None
    ):
        super().__init__(parent)

        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Table', Theme))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')

        self.setSelectionMode(QAbstractItemView.NoSelection)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred) #self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.RowHeight = self.horizontalHeader().height()

        self.SetIndexHeader()
        self.IsIndexShown = False
        self.SetIndexHeaderVisible(True)

    def SetIndexHeader(self):
        self.verticalHeader().setVisible(False)
        #self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setVisible(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.insertColumn(0)
        self.setHorizontalHeaderItem(0, QTableWidgetItem('Index'))
        #self.setColumnWidth(0, self.RowHeight * 1.5)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents) #self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        def SetIndex():
            for Index in range(self.rowCount()):
                self.setItem(Index, 0, QTableWidgetItem(f"{Index + 1}"))
        self.model().rowsInserted.connect(SetIndex)
        self.model().rowsRemoved.connect(SetIndex)

    def SetIndexHeaderVisible(self, ShowIndexHeader: bool = True):
        if ShowIndexHeader and not self.IsIndexShown:
            self.showColumn(0)
            self.IsIndexShown = True

        if not ShowIndexHeader and self.IsIndexShown:
            self.hideColumn(0)
            self.IsIndexShown = False

##############################################################################################################################

class DialogBase(QDialog):
    '''
    '''
    def __init__(self,
        parent: Optional[QWidget] = None,
        #f: WindowType = ...
    ):
        super().__init__(parent)

        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Dialog', Theme))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')

"""
class MessageBoxBase(DialogBase):
    '''
    '''
    def __init__(self,
        parent: Optional[QWidget] = None
    ):  
        super().__init__(parent)

        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Custom Dialog")
        self.resize(400, 200)

        layout = QVBoxLayout(self)

        message_label = QLabel("This is a custom dialog.", self)
        layout.addWidget(message_label)

        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancel", self)
        cancel_button.clicked.connect(self.reject)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)
"""
class MessageBoxBase(QMessageBox):
    '''
    '''
    def __init__(self,
        parent: Optional[QWidget] = None
    ):
        super().__init__(parent)

        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Dialog', Theme))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')

##############################################################################################################################