from typing import Optional
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import *
from QEasyWidgets.Components import *

from assets import *

##############################################################################################################################

class Frame_RangeSetting(QFrame):
    '''
    '''
    valueChanged = Signal(float)

    def __init__(self, parent = None):
        super().__init__(parent)

        self.Slider = SliderBase(Qt.Horizontal, self)
        self.Slider.valueChanged.connect(
            lambda value: (
                self.setValue(value),
                self.valueChanged.emit(value)
            )
        )

        self.Label = LabelBase(self)
        self.Label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.setSpacing(12)
        self.hBoxLayout.addWidget(self.Label)
        self.hBoxLayout.addWidget(self.Slider)

    def setOrientation(self, arg__1):
        self.Slider.setOrientation(arg__1)

    def setRange(self, min, max):
        self.Slider.setRange(min, max)

    def setSingleStep(self, arg__1):
        self.Slider.setSingleStep(arg__1)

    def setValue(self, value):
        self.Slider.setValue(value)
        self.Label.setNum(value)

    def value(self):
        return self.Slider.value()

##############################################################################################################################