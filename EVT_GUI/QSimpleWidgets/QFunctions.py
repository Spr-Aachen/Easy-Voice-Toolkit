import os
import sys
sys.path.append('..')
import darkdetect
from typing import Union, Optional
from PySide6.QtCore import Qt, QObject, QFile, QRect, QRectF, Signal, Slot, QPropertyAnimation, QEasingCurve, QUrl
from PySide6.QtGui import QColor, QIcon, QPainter, QDesktopServices
from PySide6.QtWidgets import *

from .Utils import *

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

def Function_SetAnimation(
    Animation: QPropertyAnimation,
    StartValue,
    EndValue,
    Duration: int
):
    Animation.setStartValue(StartValue)
    Animation.setEndValue(EndValue)
    Animation.setDuration(Duration)
    Animation.setEasingCurve(QEasingCurve.InOutQuart)
    return Animation


def Function_OpenURL(
    URL: str, #URL: str | list
):
    '''
    Function to open web/local URL
    '''
    def OpenURL(URL):
        QURL = QUrl(URL)
        if QURL.isValid():
            QURL_Localized = QURL.toLocalFile()
            QDesktopServices.openUrl(QURL_Localized) if QURL_Localized != "" else QDesktopServices.openUrl(QURL)
        else:
            print(f"Invalid URL: {URL} !")

    if isinstance(URL, str):
        OpenURL(URL)
    else:
        URLList = IterChecker(URL)
        for Index, URL in enumerate(URLList):
            #URL = Function_ParamsChecker(URLList)[Index] if isinstance(URL, QObject) else URL
            OpenURL(URL)


def Function_GetFileDialog(
    Mode: str,
    FileType: Optional[str] = '任意类型 (*.*)',
    Directory: Optional[str] = None
):
    if Mode == 'SelectDir':
        DisplayText = QFileDialog.getExistingDirectory(
            caption = "选择文件夹",
            dir = Directory if Directory is not None else os.getcwd()
        )
    if Mode == 'SelectFile':
        DisplayText, _ = QFileDialog.getOpenFileName(
            caption = "选择文件",
            dir = Directory if Directory is not None else os.getcwd(),
            filter = FileType
        ) if FileType is not None else print('FileType is empty')
    if Mode == 'SaveFile':
        DisplayText, _ = QFileDialog.getSaveFileName(
            caption = "保存文件",
            dir = Directory if Directory is not None else os.getcwd(),
            filter = FileType
        ) if FileType is not None else print('FileType is empty')
    return DisplayText

##############################################################################################################################