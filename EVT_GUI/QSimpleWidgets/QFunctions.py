import os
import darkdetect
from typing import Union, Optional
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
    Title: Optional[str] = None,
    TitleAlign: str = "left",
    TitleSize: float = 9.9,
    TitleWeight: float = 840.,
    TitleColor: str = "#ffffff",
    TitleSpacing: float = 0.6,
    TitleLineHeight: float = 21.,
    Body: Optional[str] = None,
    BodyAlign: str = "left",
    BodySize: float = 9.9,
    BodyWeight: float = 420.,
    BodySpacing: float = 0.6,
    BodyLineHeight: float = 21.,
    BodyColor: str = "#ffffff",
):
    '''
    Function to set text for widget
    '''
    def ToHtml(Content, Align, Size, Weight, Color, LetterSpacing, LineHeight):
        Style = f"'text-align:{Align}; font-size:{Size}pt; font-weight:{Weight}; color:{Color}; letter-spacing: {LetterSpacing}px; line-height:{LineHeight}px'"
        Content = re.sub(
            pattern = "[\n]",
            repl = "<br>",
            string = Content
        ) if Content is not None else None
        return f"<p style={Style}>{Content}</p>" if Content is not None else ''

    Text = (
        "<html>"
            "<head>"
                f"<title>{ToHtml(Title, TitleAlign, TitleSize, TitleWeight, TitleColor, TitleSpacing, TitleLineHeight)}</title>" # Not Working
            "</head>"
            "<body>"
                f"{ToHtml(Title, TitleAlign, TitleSize, TitleWeight, TitleColor, TitleSpacing, TitleLineHeight)}"
                f"{ToHtml(Body, BodyAlign, BodySize, BodyWeight, BodyColor, BodySpacing, BodyLineHeight)}"
            "</body>"
        "</html>"
    )

    if isinstance(Widget, QLabel):
        Widget.setText(Text)
    if isinstance(Widget, (QTextEdit, QPlainTextEdit, QTextBrowser)):
        Widget.setHtml(Text)


def Function_GetText(
    Widget: QWidget
):
    if hasattr(Widget, 'text'):
        Text = Widget.text()
        Text = Widget.placeholderText() if hasattr(Widget, 'placeholderText') and Text.strip() in ('', str(None)) else Text
    if hasattr(Widget, 'toPlainText'):
        Text = Widget.toPlainText()
        Text = Widget.placeholderText() if hasattr(Widget, 'placeholderText') and Text.strip() in ('', str(None)) else Text
    return Text


def Function_OpenURL(
    URL: Union[str, list],
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