import os
import darkdetect
from typing import Union, Optional
from ctypes import c_int, byref, windll
from PySide6.QtCore import Qt, QObject, QFile, QRect, QRectF, QSize, Signal, Slot, QPropertyAnimation, QParallelAnimationGroup, QEasingCurve, QUrl
from PySide6.QtGui import QGuiApplication, QColor, QRgba64, QIcon, QPainter, QDesktopServices
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


def Function_SetWidgetPosAnimation(
    Widget: QWidget,
    Duration: int = 99
):
    OriginalGeometry = Widget.geometry()
    AlteredGeometry = QRect(OriginalGeometry.left(), OriginalGeometry.top() + OriginalGeometry.height() / Duration, OriginalGeometry.width(), OriginalGeometry.height())

    WidgetAnimation = QPropertyAnimation(Widget, b"geometry", Widget)

    return Function_SetAnimation(WidgetAnimation, OriginalGeometry, AlteredGeometry, Duration)


def Function_SetWidgetSizeAnimation(
    Frame: QWidget,
    TargetWidth: Optional[int] = None,
    TargetHeight: Optional[int] = None,
    Duration: int = 210
):
    '''
    Function to animate widget size
    '''
    CurrentWidth = Frame.geometry().width() if Frame.size() == QSize(100, 30) else Frame.width()
    CurrentHeight = Frame.geometry().height() if Frame.size() == QSize(100, 30) else Frame.height()

    FrameAnimationMinWidth = QPropertyAnimation(Frame, b"minimumWidth", Frame)
    FrameAnimationMaxWidth = QPropertyAnimation(Frame, b"maximumWidth", Frame)
    FrameAnimationMinHeight = QPropertyAnimation(Frame, b"minimumHeight", Frame)
    FrameAnimationMaxHeight = QPropertyAnimation(Frame, b"maximumHeight", Frame)

    AnimationGroup = QParallelAnimationGroup(Frame)

    AnimationGroup.addAnimation(Function_SetAnimation(FrameAnimationMinWidth, CurrentWidth, TargetWidth, Duration)) if TargetWidth is not None else None
    AnimationGroup.addAnimation(Function_SetAnimation(FrameAnimationMaxWidth, CurrentWidth, TargetWidth, Duration)) if TargetWidth is not None else None
    AnimationGroup.addAnimation(Function_SetAnimation(FrameAnimationMinHeight, CurrentHeight, TargetHeight, Duration)) if TargetHeight is not None else None
    AnimationGroup.addAnimation(Function_SetAnimation(FrameAnimationMaxHeight, CurrentHeight, TargetHeight, Duration)) if TargetHeight is not None else None

    return AnimationGroup


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


def Function_GetFileDialog(
    Mode: str,
    FileType: Optional[str] = None,
    Directory: Optional[str] = None
):
    os.makedirs(Directory, exist_ok = True) if Directory is not None and Path(Directory).exists() == False else None
    if Mode == 'SelectFolder':
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


def GetMissingBorderPixels(hWnd: int):
    MissingBorderSize = []

    for QWindow in QGuiApplication.allWindows():
        if QWindow.winId() == hWnd:
            Window = QWindow
            break

    SIZEFRAME = {
        win32con.SM_CXSIZEFRAME: True,
        win32con.SM_CYSIZEFRAME: False
    }
    for BorderLengthIndex, dpiScaling in SIZEFRAME.items():
        MissingBorderPixels = GetSystemMetrics(hWnd, BorderLengthIndex, dpiScaling) + GetSystemMetrics(hWnd, 92, dpiScaling) #MissingBorderPixels = win32api.GetSystemMetrics(MissingBorderLength) + win32api.GetSystemMetrics(win32con.SM_CXPADDEDBORDER)
        if not MissingBorderPixels > 0:
            def IsCompositionEnabled():
                Result = windll.dwmapi.DwmIsCompositionEnabled(byref(c_int(0)))
                return bool(Result.value)
            MissingBorderPixels = round((6 if IsCompositionEnabled() else 3) * Window.devicePixelRatio())
        MissingBorderSize.append(MissingBorderPixels)

    return MissingBorderSize


def Function_OpenURL(
    URL: Union[str, list],
    CreateIfNotExist: bool = False
):
    '''
    Function to open web/local URL
    '''
    def OpenURL(URL):
        QURL = QUrl().fromLocalFile(NormPath(URL))
        if QURL.isValid():
            os.makedirs(NormPath(URL), exist_ok = True) if CreateIfNotExist else None
            IsSucceeded = QDesktopServices.openUrl(QURL)
            RunCMD([f'start {URL}']) if not IsSucceeded else None
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