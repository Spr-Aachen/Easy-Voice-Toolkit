from PySide6.QtCore import Qt, QObject
from PySide6.QtGui import QColor, QIcon, QPainter, QPaintEvent
from PySide6.QtWidgets import *

from .QFunctions import *
from .Sources import *
from .WindowCustomizer import DialogBase

##############################################################################################################################

class WidgetBase(QWidget):
    '''
    '''
    def __init__(self,
        parent: Optional[QWidget] = None,
        f: Qt.WindowType = Qt.Widget
    ):
        super().__init__(parent, f)

        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Widget', Theme))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(Qt.transparent)
        painter.setPen(Qt.gray)

##############################################################################################################################

class LineEditBase(QLineEdit):
    '''
    '''
    def __init__(self,
        text: Optional[str] = None,
        parent: Optional[QWidget] = None
    ):
        super().__init__(parent)

        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Edit', Theme))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')

        self.setFont('Microsoft YaHei')
        self.setText(text) if text is not None else None


class LineEdit_NoBorder(LineEditBase):
    '''
    Check its stylesheet in qss file
    '''

##############################################################################################################################

class ToolButtonBase(QToolButton):
    '''
    '''
    def __init__(self,
        text: Optional[str] = None,
        parent: Optional[QWidget] = None
    ):
        super().__init__(parent)

        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Button', Theme))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')

        self.setFont('Microsoft YaHei')
        self.setText(text) if text is not None else None
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

class MessageBoxBase(DialogBase):
    '''
    '''
    ButtonDict = {
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

    def __init__(self,
        parent: Optional[QWidget] = None,
        min_width = 630,
        min_height = 420
    ):  
        super().__init__(parent, Qt.Dialog, min_width, min_height)

        self.setWindowModality(Qt.ApplicationModal)
        self.setModal(True)

        self.Label = QLabel(str(), parent = self)

        self.ButtonBox = QDialogButtonBox(parent = self)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)
        self.ButtonBox.setOrientation(Qt.Horizontal)

        self.Layout = QVBoxLayout()
        self.Layout.setAlignment(Qt.AlignCenter)
        self.Layout.setContentsMargins(21, 12, 21, 12)
        self.Layout.setSpacing(21)
        self.Layout.addWidget(self.Label)
        self.Layout.addWidget(self.ButtonBox)
        self.setLayout(self.Layout)

        self.setIcon(QMessageBox.Information)
        self.setText('Text')
        self.setStandardButtons(QMessageBox.NoButton)

    def setIcon(self, arg__1):
        if arg__1 == QMessageBox.Question:
            self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxQuestion))
        if arg__1 == QMessageBox.Information:
            self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxInformation))
        if arg__1 == QMessageBox.Warning:
            self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxWarning))
        if arg__1 == QMessageBox.Critical:
            self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxCritical))

    def setText(self, text: str):
        Function_SetText(
            Widget = self.Label,
            Text = SetRichText(
                Title = text,
                TitleAlign = 'center'
            )
        )

    def setStandardButtons(self, buttons: QMessageBox.StandardButton):
        self.ButtonBox.setStandardButtons(self.ButtonDict.get(buttons))
        '''
        for PushButton in self.ButtonBox.buttons():
            StandardButton = FindKey(self.ButtonDict, self.ButtonBox.standardButton(PushButton))
            PushButton.clicked.connect(lambda: ComponentsSignals.Signal_ClickedButton.emit(StandardButton)) if PushButton is not None else None
        '''

    def exec(self) -> int:
        Result = super().exec()
        StandardButton = FindKey(self.ButtonDict, Result)
        return StandardButton if StandardButton is not None else Result

    def InsertItem(self, Item: QObject, Position: str = 'Center'):
        if isinstance(Item, QWidget):
            if Position is 'Top':
                self.Layout.insertWidget(0, Item)
            if Position is 'Center':
                self.Layout.insertWidget(1, Item)
            if Position is 'Bottom':
                self.Layout.insertWidget(2, Item)
        if isinstance(Item, QLayout):
            if Position is 'Top':
                self.Layout.insertLayout(0, Item)
            if Position is 'Center':
                self.Layout.insertLayout(1, Item)
            if Position is 'Bottom':
                self.Layout.insertLayout(2, Item)

##############################################################################################################################