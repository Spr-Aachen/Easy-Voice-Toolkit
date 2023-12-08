import os
import darkdetect
from typing import Union, Optional
#from urllib.parse import quote
from PySide6.QtCore import Qt, QObject, QFile, QRect, QRectF, Signal, Slot, QPropertyAnimation, QEasingCurve, QUrl
from PySide6.QtGui import QColor, QRgba64, QIcon, QPainter, QDesktopServices
from PySide6.QtWidgets import *

from .Utils import *

##############################################################################################################################

class CustomSignals_ComponentsCustomizer(QObject):
    '''
    Set up signals for components
    '''
    # Set theme
    Signal_SetTheme = Signal(str)
    '''
    # Get clicked button
    Signal_ClickedButton = Signal(QMessageBox.StandardButton)
    '''

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

def Function_SetRetainSizeWhenHidden(
    Widget: QWidget,
    RetainSize: bool = True
):
    sizePolicy = Widget.sizePolicy()
    sizePolicy.setRetainSizeWhenHidden(RetainSize)
    Widget.setSizePolicy(sizePolicy)


def Function_SetDropShadowEffect(
    Widget: QWidget,
    Radius: float = 3.,
    Color: Union[QColor, QRgba64] = Qt.gray
):
    DropShadowEffect = QGraphicsDropShadowEffect()
    DropShadowEffect.setOffset(0, 0)
    DropShadowEffect.setBlurRadius(Radius)
    DropShadowEffect.setColor(Color)
    Widget.setGraphicsEffect(DropShadowEffect)


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


def Function_SetNoContents(
    Widget: QWidget
):
    if isinstance(Widget, QStackedWidget):
        while Widget.count():
            Widget.removeWidget(Widget.widget(0))


def Function_SetText(
    Widget: QWidget,
    Text: str,
    SetHtml: bool = True,
    SetPlaceholderText: bool = False,
    PlaceholderText: Optional[str] = None
):
    if hasattr(Widget, 'setText'):
        Widget.setText(Text)
    if hasattr(Widget, 'setPlainText'):
        Widget.setPlainText(Text)
    if hasattr(Widget, 'setHtml') and SetHtml:
        Widget.setHtml(Text)
    if hasattr(Widget, 'setPlaceholderText') and SetPlaceholderText:
        Widget.setPlaceholderText(str(PlaceholderText) if Text.strip() in ('', str(None)) else Text)


def Function_GetText(
    Widget: QWidget,
    GetHtml: bool = False,
    GetPlaceholderText: bool = False
):
    if hasattr(Widget, 'text'):
        Text = Widget.text()
    if hasattr(Widget, 'toPlainText'):
        Text = Widget.toPlainText()
    if hasattr(Widget, 'toHtml') and GetHtml:
        Text = Widget.toHtml()
    if hasattr(Widget, 'placeholderText') and GetPlaceholderText:
        Text = Widget.placeholderText() if Text.strip() in ('', str(None)) else Text
    return Text


def Function_OpenURL(
    URL: Union[str, list],
):
    '''
    Function to open web/local URL
    '''
    def OpenURL(URL):
        #URL = quote(URL, encoding = 'ansi')
        QURL = QUrl(URL)
        if QURL.isValid():
            IsSucceeded = QDesktopServices.openUrl(QURL)
            RunCMD([f'start "{URL}"']) if not IsSucceeded else None
        else:
            print(f"Invalid URL: {URL} !")

    if isinstance(URL, str):
        OpenURL(URL)
    else:
        URLList = ToIterable(URL)
        for Index, URL in enumerate(URLList):
            #URL = Function_ParamsChecker(URLList)[Index] if isinstance(URL, QObject) else URL
            OpenURL(URL)

##############################################################################################################################

def Function_GetFileDialog(
    Mode: str,
    FileType: Optional[str] = None,
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
            filter = FileType if FileType is not None else '任意类型 (*.*)'
        )
    if Mode == 'SaveFile':
        DisplayText, _ = QFileDialog.getSaveFileName(
            caption = "保存文件",
            dir = Directory if Directory is not None else os.getcwd(),
            filter = FileType if FileType is not None else '任意类型 (*.*)'
        )
    return DisplayText

##############################################################################################################################