import os
import sys
sys.path.append('..')
import darkdetect
from typing import Union, Optional
from PySide6.QtCore import Qt, QObject, QFile, QRect, QRectF, Signal, Slot
from PySide6.QtGui import QColor, QIcon, QPainter
from PySide6.QtWidgets import *

##############################################################################################################################

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