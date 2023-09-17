from typing import Optional
from PySide6.QtCore import Qt, QObject

from .QSimpleWidgets.WindowCustomizer import *
from .UI import Ui_MainWindow

##############################################################################################################################

class Window_Customizing(MainWindowBase):
    ui = Ui_MainWindow()

    def __init__(self,
        edge_size: int = 3,
        min_width: int = 1280,
        min_height: int = 720,
        move_event_height: int = 30
    ):
        super().__init__(None, False)

        self.ui.setupUi(self)

        self.CustomizeTitleBar = CustomizeTitleBar(self, self.ui.TitleBar)
        self.CustomizeTitleBar.SetUp()

        self.edge_size = edge_size # 窗体边缘尺寸（出现缩放标记的范围）

        self.min_width = min_width # 窗体的最小宽度
        self.min_height = min_height # 窗体的最小高度

        self.move_event_height = move_event_height # 顶部可移动窗口高度

##############################################################################################################################