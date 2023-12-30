from typing import Optional
from PySide6.QtCore import Qt, QObject

from .QSimpleWidgets.WindowCustomizer import *
from .UI import Ui_MainWindow

##############################################################################################################################

class Window_Customizing(MainWindowBase):
    ui = Ui_MainWindow()

    def __init__(self, parent):
        super().__init__(parent, min_width = 1280, min_height = 720)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)

        self.setCentralWidget(self.ui.CentralWidget)
        ComponentsSignals.Signal_SetTheme.connect(
            lambda Theme: self.setStyleSheet(Function_GetStyleSheet('Window', Theme).replace('#CentralWidget', f'#{self.CentralWidget.objectName()}'))
        )
        ComponentsSignals.Signal_SetTheme.emit('Auto')

##############################################################################################################################