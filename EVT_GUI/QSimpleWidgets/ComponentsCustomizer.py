from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from .QFunctions import *
from .Sources import *

##############################################################################################################################
"""
class ButtonBase(QAbstractButton):
    '''
    '''
    def __init__(self,
        text: Optional[str] = None,
        parent: Optional[QWidget] = None
    ):
        super().__init__(parent)

        self.setFont('Microsoft YaHei')
        self.setText(text) if text is not None else None

        ComponentsSignals.Signal_SetTheme.connect(self.InitDefaultStyleSheet)
        self.InitDefaultStyleSheet('Auto')

    def InitDefaultStyleSheet(self, Theme: str) -> None:
        super().setStyleSheet(Function_GetStyleSheet('Button', Theme))

    def ClearDefaultStyleSheet(self) -> None:
        ComponentsSignals.Signal_SetTheme.disconnect(self.InitDefaultStyleSheet)


class Button_UnderLined(ButtonBase):
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

        ComponentsSignals.Signal_SetTheme.connect(self.InitDefaultStyleSheet)
        self.InitDefaultStyleSheet('Auto')

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

    def InitDefaultStyleSheet(self, Theme: str) -> None:
        super().setStyleSheet(Function_GetStyleSheet('Table', Theme))

    def ClearDefaultStyleSheet(self) -> None:
        ComponentsSignals.Signal_SetTheme.disconnect(self.InitDefaultStyleSheet)

##############################################################################################################################

class LineEditBase(QFrame):
    '''
    '''
    textChanged = Signal(str)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.LineEdit = QLineEdit()
        self.LineEdit.textChanged.connect(self.LineEdit.setStatusTip)
        self.LineEdit.textChanged.connect(self.textChanged.emit)

        self.Button = QPushButton()

        HBoxLayout = QHBoxLayout(self)
        HBoxLayout.setSpacing(0)
        HBoxLayout.setContentsMargins(0, 0, 0, 0)
        HBoxLayout.addWidget(self.LineEdit)
        HBoxLayout.addWidget(self.Button, alignment = Qt.AlignRight)

        ComponentsSignals.Signal_SetTheme.connect(self.InitDefaultStyleSheet)
        self.InitDefaultStyleSheet('Auto')

    def clear(self) -> None:
        self.LineEdit.clear()

    def text(self) -> str:
        return self.LineEdit.text()

    def setText(self, arg__1: str) -> None:
        return self.LineEdit.setText(arg__1)

    def placeholderText(self) -> str:
        return self.LineEdit.placeholderText()

    def setPlaceholderText(self, arg__1: str) -> None:
        self.LineEdit.setPlaceholderText(arg__1)

    def SetFileDialog(self, Mode: str, FileType: Optional[str] = None, Directory: Optional[str] = None, ButtonTooltip: str = "Browse"):
        self.Button.clicked.connect(
            lambda: self.LineEdit.setText(
                Function_GetFileDialog(
                    Mode = Mode,
                    FileType = FileType,
                    Directory = os.path.expanduser('~/Documents' if platform.system() == "Windows" else '~/') if Directory is None else Directory
                )
            )
        )
        self.Button.setToolTip(ButtonTooltip)

    def RemoveFileDialogButton(self):
        self.Button.deleteLater()
        self.Button.hide()

    def InitDefaultStyleSheet(self, Theme: str) -> None:
        super().setStyleSheet(Function_GetStyleSheet('Edit', Theme))

    def ClearDefaultStyleSheet(self) -> None:
        ComponentsSignals.Signal_SetTheme.disconnect(self.InitDefaultStyleSheet)

##############################################################################################################################

class MediaPlayerBase(QWidget):
    '''
    '''
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.StackedWidget = QStackedWidget()
        self.StackedWidget.setMaximumSize(36, 36)
        self.StackedWidget.setContentsMargins(0, 0, 0, 0)
        self.PlayButton = QPushButton()
        self.PlayButton.setStyleSheet(self.styleSheet() + "QPushButton {border-image: url(:/Button_Icon/Sources/Play.png);}")
        self.PauseButton = QPushButton()
        self.PauseButton.setStyleSheet(self.styleSheet() + "QPushButton {border-image: url(:/Button_Icon/Sources/Pause.png);}")
        self.PauseButton.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.PlayButton))
        self.PlayButton.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.PauseButton))
        self.StackedWidget.addWidget(self.PlayButton)
        self.StackedWidget.addWidget(self.PauseButton)
        self.StackedWidget.setCurrentWidget(self.PlayButton)

        self.Slider = QSlider()
        self.Slider.setOrientation(Qt.Horizontal)

        HBoxLayout = QHBoxLayout(self)
        HBoxLayout.setSpacing(12)
        HBoxLayout.setContentsMargins(21, 12, 21, 12)
        HBoxLayout.addWidget(self.StackedWidget, stretch = 1)
        HBoxLayout.addWidget(self.Slider, stretch = 5)

        AudioOutput = QAudioOutput(self)
        self.MediaPlayer = QMediaPlayer()
        self.MediaPlayer.setAudioOutput(AudioOutput)
        #self.MediaPlayer.mediaStatusChanged.connect(lambda Status: self.MediaPlayer.stop() if Status == QMediaPlayer.EndOfMedia else None)

        ComponentsSignals.Signal_SetTheme.connect(self.InitDefaultStyleSheet)
        self.InitDefaultStyleSheet('Auto')

    def SetMediaPlayer(self, MediaPath: str):
        self.MediaPlayer.setSource(QUrl.fromLocalFile(MediaPath))

        self.PlayButton.clicked.connect(self.MediaPlayer.play)
        self.PauseButton.clicked.connect(self.MediaPlayer.pause)
        self.MediaPlayer.mediaStatusChanged.connect(lambda status: self.StackedWidget.setCurrentWidget(self.PlayButton) if status == QMediaPlayer.EndOfMedia else None)

        self.Slider.setRange(0, 100)
        self.Slider.sliderMoved.connect(lambda: self.MediaPlayer.setPosition(int(self.Slider.value() / 100 * self.MediaPlayer.duration())))
        self.MediaPlayer.positionChanged.connect(lambda Position: self.Slider.setValue(int(Position / self.MediaPlayer.duration() * 100)))

    def ReleaseMediaPlayer(self):
        self.MediaPlayer.stop()
        self.MediaPlayer.setSource('')
        #self.MediaPlayer.deleteLater()

    def InitDefaultStyleSheet(self, Theme: str) -> None:
        super().setStyleSheet(Function_GetStyleSheet('Player', Theme))

    def ClearDefaultStyleSheet(self) -> None:
        ComponentsSignals.Signal_SetTheme.disconnect(self.InitDefaultStyleSheet)

##############################################################################################################################