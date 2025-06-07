from typing import Optional
from QEasyWidgets.Windows import MainWindowBase, ChildWindowBase

from ui import *

##############################################################################################################################

class Window_MainWindow(MainWindowBase):
    ui = Ui_MainWindow()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 1280, min_height = 720)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)

        self.setCentralWidget(self.ui.CentralWidget)

        self.langChanged.connect(lambda: self.ui.retranslateUi(self))

##############################################################################################################################

class Window_ChildWindow_VPR(ChildWindowBase):
    ui = Ui_ChildWindow_VPR()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 960, min_height = 540)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)


class Window_ChildWindow_ASR(ChildWindowBase):
    ui = Ui_ChildWindow_ASR()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 960, min_height = 540)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)


class Window_ChildWindow_DAT(ChildWindowBase):
    ui = Ui_ChildWindow_DAT()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 960, min_height = 540)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)


class Window_ChildWindow_TTS(ChildWindowBase):
    ui = Ui_ChildWindow_TTS()

    def __init__(self, parent = None):
        super().__init__(parent, min_width = 450, min_height = 300)

        self.ui.setupUi(self)

        self.setTitleBar(self.ui.TitleBar)

##############################################################################################################################