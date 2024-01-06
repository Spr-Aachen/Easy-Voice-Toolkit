from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from .QFunctions import *
from .Sources import *

##############################################################################################################################
"""
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


class ToolButton_UnderLined(ToolButtonBase):
    '''
    Check its stylesheet in qss file
    '''

##############################################################################################################################
"""
class TableBase(QTableView):
    '''
    '''
    sorted = Signal()

    def __init__(self,
        parent: Optional[QWidget] = None
    ):
        super().__init__(parent)

        self.StandardItemModel = QStandardItemModel(self)
        super().setModel(self.StandardItemModel)

        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Table', Theme))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')

        super().setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        super().verticalHeader().setStretchLastSection(False)
        super().verticalHeader().setResizeContentsPrecision(0)
        super().verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        super().horizontalHeader().setStretchLastSection(False)
        super().horizontalHeader().setResizeContentsPrecision(0)
        super().horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        super().setSelectionMode(QAbstractItemView.NoSelection)
        super().setEditTriggers(QAbstractItemView.NoEditTriggers)

        super().verticalHeader().setVisible(False)
        super().horizontalHeader().setVisible(True)
        self.model().insertColumn(0)
        self.model().setHorizontalHeaderItem(0, QStandardItem('Index'))
        super().horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.model().rowsInserted.connect(self.SetIndex)
        self.model().rowsRemoved.connect(self.SetIndex)
        self.sorted.connect(self.SetIndex)

        self.IsIndexShown = False
        self.SetIndexHeaderVisible(True)

    def model(self) -> QStandardItemModel:
        return self.StandardItemModel

    def currentRow(self) -> int:
        return super().currentIndex().row()

    def insertRow(self, row: int) -> None:
        self.model().insertRow(row)

    def removeRow(self, row: int) -> None:
        self.model().removeRow(row)

    def rowCount(self) -> int:
        return self.model().rowCount()

    def setRowCount(self, rows: int) -> None:
        self.model().setRowCount(rows)

    def currentColumn(self) -> int:
        return super().currentIndex().column() + 1

    def insertColumn(self, column: int) -> None:
        self.model().insertColumn(column + 1)

    def removeColumn(self, column: int) -> None:
        self.model().removeColumn(column + 1)

    def columnCount(self) -> int:
        return self.model().columnCount() - 1

    def setColumnCount(self, columns: int) -> None:
        self.model().setColumnCount(columns + 1)

    def setColumnWidth(self, column: int, width: int) -> None:
        super().setColumnWidth(column + 1, width)

    def selectColumn(self, column: int) -> None:
        super().selectColumn(column + 1)

    def insertColumn(self, column: int) -> None:
        self.model().insertColumn(column + 1)

    def sortByColumn(self, column: int, order: Qt.SortOrder) -> None:
        #super().setSortingEnabled(True) if not super().isSortingEnabled() else None
        super().sortByColumn(column + 1, order)
        self.sorted.emit()

    def cellWidget(self, row: int, column: int) -> QWidget:
        return super().indexWidget(self.model().index(row, column + 1))

    def setCellWidget(self, row: int, column: int, widget: QWidget) -> None:
        super().setIndexWidget(self.model().index(row, column + 1), widget)

    def setHorizontalHeaderItem(self, column: int, item: QStandardItem) -> None:
        self.model().setHorizontalHeaderItem(column + 1, item)

    def SetIndex(self) -> None:
        for Index in range(self.model().rowCount()):
            self.model().setItem(Index, 0, QStandardItem(f"{Index + 1}"))

    def SetIndexHeaderVisible(self, ShowIndexHeader: bool = True) -> None:
        if ShowIndexHeader and not self.IsIndexShown:
            super().showColumn(0)
            self.IsIndexShown = True
        if not ShowIndexHeader and self.IsIndexShown:
            super().hideColumn(0)
            self.IsIndexShown = False

    def SetHorizontalHeaders(self, Headers: list[str]) -> None:
        for Index, Header in enumerate(Headers):
            if Index == 1 + self.columnCount():
                return print("Maximum headers reached")
            self.setHorizontalHeaderItem(Index, QStandardItem(Header))

    def SetSectionVerticalResizeMode(self, row: int, mode: QHeaderView.ResizeMode) -> None:
        super().verticalHeader().setSectionResizeMode(row, mode)

    def SetSectionHorizontalResizeMode(self, column: int, mode: QHeaderView.ResizeMode) -> None:
        super().horizontalHeader().setSectionResizeMode(column + 1, mode)

    def SelectOuterRow(self, InnerWidget: QWidget) -> None:
        CellWidget = InnerWidget.parent()
        ModelIndex = self.indexAt(CellWidget.pos())
        self.selectRow(ModelIndex.row()) #if index.isValid() else None

    def AddRow(self, Layouts: list[QLayout], ResizeModes: list[Optional[QHeaderView.ResizeMode]], ColumnWidth: list[Optional[int]], Height: Optional[int]) -> None:
        TargetRow = self.currentRow() + 1
        ColumnCount = self.columnCount()
        self.insertRow(TargetRow)
        for ColumnCount in range(ColumnCount):
            self.setCellWidget(TargetRow, ColumnCount, QWidget())
            self.cellWidget(TargetRow, ColumnCount).setLayout(Layouts[ColumnCount])
            self.SetSectionHorizontalResizeMode(ColumnCount, ResizeModes[ColumnCount]) if ResizeModes[ColumnCount] is not None else None
            self.setColumnWidth(ColumnCount, ColumnWidth[ColumnCount]) if ColumnWidth[ColumnCount] is not None else None
        self.setRowHeight(TargetRow, Height) if Height is not None else None

    def DelRow(self) -> None:
        self.removeRow(self.currentRow()) if self.rowCount() > 1 else None

    def ClearRows(self):
        while self.rowCount() > 0:
            self.removeRow(0)

##############################################################################################################################