import os
import darkdetect
from typing import Union, Optional
from PySide6.QtCore import Qt, QObject, QFile, Signal, QUrl, QRect, QRectF, QSize
from PySide6.QtGui import QColor, QIcon, QPainter
from PySide6.QtWidgets import *

from .QFunctions import Function_SetFileDialog
from .Utils import IterChecker


class CustomSignals_ComponentsCustomizer(QObject):
    '''
    Set up signals for components
    '''
    # Set theme
    Signal_SetTheme = Signal(str)


ComponentsSignals = CustomSignals_ComponentsCustomizer()

##############################################################################################################################

def Function_GetStyleSheet(
    Widget: str,
    Theme: Optional[str] = None
):
    '''
    Get style sheet

    Parameters
    ----------

    Widget: str
        Name of widget (base)

    Theme: str | None
        Type of theme
    '''
    if Theme not in ('Dark', 'Light'):
        Theme = darkdetect.theme()

    File = QFile(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'QSS/{Theme}/{Widget}.qss'))
    File.open(QFile.ReadOnly | QFile.Text)
    QSS = str(File.readAll(), encoding = 'utf-8')
    File.close()
    return QSS


def Function_DrawIcon(
    Icon: Union[str, QIcon],
    Painter: QPainter,
    Rect: Union[QRect, QRectF]
):
    '''
    Draw icon

    Parameters
    ----------

    Icon: str | QIcon
        the icon to be drawn

    Painter: QPainter
        painter

    Rect: QRect | QRectF
        the rect to render icon
    '''
    icon = QIcon(Icon)
    icon.paint(Painter, QRectF(Rect).toRect(), Qt.AlignCenter, state = QIcon.Off)

##############################################################################################################################

class ToolButtonBase(QToolButton):
    '''
    '''
    def __init__(self, text: str, parent: QWidget = None):
        super().__init__(parent)

        self.setStyleSheet(Function_GetStyleSheet('Button'))
        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Button', Theme))
        )

        self.setFont('Microsoft YaHei')
        self.setText(text)
    '''
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
    '''


class ToolButton_UnderLined(ToolButtonBase):
    '''
    Check its stylesheet in qss file
    '''

##############################################################################################################################

class TableWidgetBase(QTableWidget):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setStyleSheet(Function_GetStyleSheet('Table'))
        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Table', Theme))
        )

        self.SetIndexHeader()
        self.IsIndexShown = False
        self.SetIndexHeaderVisible(True)

        self.setSelectionMode(QAbstractItemView.NoSelection)

    def SetIndexHeader(self):
        self.verticalHeader().setVisible(False)
        self.insertColumn(0)
        self.setHorizontalHeaderItem(0, QTableWidgetItem('Index'))
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


class TableWidget_ButtonMixed(TableWidgetBase):
    '''
    '''
    ValueChanged = Signal(dict)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.ColumnCount = 3
        self.setColumnCount(self.ColumnCount + 1)
        self.setRowCount(0)

        self.cellChanged.connect( #self.itemChanged.connect(
            lambda: self.ValueChanged.emit(self.GetValue())
        )

    def DelRow(self):
        self.removeRow(self.currentRow()) if self.rowCount() > 1 else None

    def AddRow(self, Param: Optional[tuple] = None):
        CurrentColumnCount = self.columnCount()
        CurrentRowCount = self.rowCount()

        self.insertRow(CurrentRowCount)
        for ColumnCount in range(1, 1 + self.ColumnCount):
            self.setCellWidget(CurrentRowCount, ColumnCount, QWidget())

            if ColumnCount == 1 + 0:
                LineEdit = QLineEdit(Param[ColumnCount] if Param else 'None')
                Column0Layout = QGridLayout()
                Column0Layout.setContentsMargins(0, 0, 0, 0)
                Column0Layout.addWidget(LineEdit)
                self.cellWidget(CurrentRowCount, ColumnCount).setLayout(Column0Layout)

            if ColumnCount == 1 + 1:
                LineEdit = QLineEdit(Param[ColumnCount] if Param else 'None')
                Button = ToolButtonBase("...")
                Function_SetFileDialog(Button, LineEdit, "SelectFile")
                Column1Layout = QHBoxLayout()
                Column1Layout.setContentsMargins(0, 0, 0, 0)
                Column1Layout.addWidget(LineEdit)
                Column1Layout.addWidget(Button)
                self.cellWidget(CurrentRowCount, ColumnCount).setLayout(Column1Layout)

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
                Column2Layout.setContentsMargins(0, 0, 0, 0)
                Column2Layout.addWidget(AddButton)
                Column2Layout.addWidget(DelButton)
                self.cellWidget(CurrentRowCount, ColumnCount).setLayout(Column2Layout)

    def SetValue(self, Params: dict = {'': ''}):
        ParamDict = Params #ParamDict = IterChecker(Params)
        for Key, Value in ParamDict.items():
            Param = tuple(('',) + (Key, Value)) #if self.IsIndexShown else Param
            Index = next((i for i, key in enumerate(ParamDict) if key == Key), None)
            if Index == 1 + self.ColumnCount:
                return print("Maximum params reached")
            self.AddRow(Param)

    def GetValue(self):
        ValueDict = {}
        for Row in range(self.rowCount()):
            Key = self.cellWidget(Row, 0).findChild(QLineEdit).text() #Key = TableWidget.item(Row, 0)
            Value = self.cellWidget(Row, 1).findChild(QLineEdit).text()
            ValueDict[Key] = Value
        return ValueDict

    def SetHorizontalHeaders(self, Headers: list = ['', '', '']):
        HeaderList = IterChecker(Headers)
        HeaderList.insert(0, '') #if self.IsIndexShown else None
        for Index, Header in enumerate(HeaderList):
            if Index == 1 + self.ColumnCount:
                return print("Maximum headers reached")
            self.setHorizontalHeaderItem(1 + Index, QTableWidgetItem(Header))

##############################################################################################################################
'''
if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()

    TableWidget = TableWidget_ButtonMixed()
    TableWidget.SetValue()
    TableWidget.SetHorizontalHeaders()
    layout = QVBoxLayout()
    layout.addWidget(TableWidget)

    widget = QWidget()
    widget.setLayout(layout)
    window.setCentralWidget(widget)

    window.show()
    app.exec()
'''