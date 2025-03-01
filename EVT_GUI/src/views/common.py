from typing import Type, Optional
from PySide6.QtCore import Qt, QRect, QSize
from PySide6.QtWidgets import *
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets.Components import *

#from assets import *
from functions import *

##############################################################################################################################

class SubPage(QWidget):
    """
    """
    def __init__(self, parent = None):
        super().__init__(parent)

        self.widgets = {}

        self.container = QWidget()
        container_layout = QVBoxLayout(self.container)
        container_layout.setSpacing(12)
        container_layout.setContentsMargins(12, 12, 12, 12)
        self.contentWidget = ScrollAreaBase(self)
        self.contentWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.contentWidget.setWidgetResizable(True)
        self.contentWidget.setWidget(self.container)

        layout = QGridLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.contentWidget, 0, 0)

    def findChildWidget(self, *args, type: Optional[Type[QWidget]] = None):
        if len(args) > 3:
            args, type = args[:-1], args[-1]
        childWidget = self.widgets.get(args, None)
        if type is not None and not isinstance(childWidget, type):
            childWidget = QFunc.findChild(childWidget, type)
        return childWidget

    def cleanLayout(self) -> QGridLayout:
        layout = self.layout()
        layout.removeWidget(self.contentWidget)
        return layout

    def _addToChildFrame(self, inputWidget: QWidget):
        childFrame = QFrame()
        childFrame_layout = QGridLayout(childFrame)
        childFrame_layout.setSpacing(12)
        childFrame_layout.setContentsMargins(21, 12, 21, 12)
        childFrame_layout.addWidget(inputWidget)
        return childFrame

    def _addToContainer(self, rootItemText: Optional[str] = None, toolBoxText: Optional[str] = None, text: str = ..., *args):
        # Add to childFrame
        childFrame = self._addToChildFrame(*args)
        self.widgets[(rootItemText, toolBoxText, text.splitlines()[0])] = childFrame # record the childFrame
        # Add to toolBox
        if toolBoxText is None:
            toolBox = childFrame
        else:
            toolBoxText = toolBoxText.splitlines()[0]
            toolBox = self.findChildWidget(rootItemText, toolBoxText)
            if isinstance(toolBox, ToolBoxBase):
                toolBox.widget(0).addWidget(childFrame)
            else:
                toolBox = ToolBoxBase()
                toolPageItem = QWidget()
                toolPageItem_layout = QGridLayout(toolPageItem)
                toolPageItem_layout.setSpacing(0)
                toolPageItem_layout.setContentsMargins(0, 0, 0, 0)
                toolPageItem_layout.addWidget(childFrame)
                toolBox.addItem(toolPageItem, toolBoxText)
                self.widgets[(rootItemText, toolBoxText)] = toolBox # record the toolBox
            toolBox.widget(0).collapse()
        # Add to groupBox
        if rootItemText is None:
            groupBox = toolBox
        else:
            rootItemText = rootItemText.splitlines()[0]
            groupBox = self.findChildWidget(rootItemText)
            if isinstance(groupBox, GroupBoxBase):
                groupBox.layout().addWidget(toolBox)
            else:
                groupBox = GroupBoxBase()
                groupBox_layout = QGridLayout(groupBox)
                groupBox_layout.setSpacing(0)
                groupBox_layout.setContentsMargins(0, 12, 0, 12)
                groupBox_layout.addWidget(toolBox)
                groupBox.setTitle(rootItemText)
                self.widgets[(rootItemText,)] = groupBox # record the groupbox
        self.container.layout().addWidget(groupBox)

##############################################################################################################################

class Page(QWidget):
    """
    """
    def __init__(self, parent = None):
        super().__init__(parent)

        self.navigationArea = QWidget()
        self.navigationArea.setMinimumHeight(60)
        self.navigationArea.setStyleSheet("""
            QWidget {
                border-width: 0px 0px 3px 0px;
                border-style: solid;
                border-bottom-color: rgba(123, 123, 123, 123);
            }
        """)
        self.navigationAreaLayout = QHBoxLayout(self.navigationArea)
        self.navigationAreaLayout.setSpacing(0)
        self.navigationAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.navigationAreaLayout.addItem(self.horizontalSpacer)

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(21)
        layout.setContentsMargins(21, 12, 21, 12)
        layout.addWidget(self.navigationArea)
        layout.addWidget(self.stackedWidget)

    def addSubPage(self,
        title: str, subPage: SubPage, showNavigator: bool = True
    ):
        self.stackedWidget.addWidget(subPage)
        if showNavigator:
            navigationButton = NavigationButton()
            navigationButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            navigationButton.setText(title)
            navigationButton.setHorizontal(True)
            navigationButton.setAutoExclusive(True)
            navigationButton.clicked.connect(
                lambda: Function_AnimateStackedWidget(
                    stackedWidget = self.stackedWidget,
                    target = subPage
                )
            )
            self.navigationAreaLayout.insertWidget(self.navigationAreaLayout.indexOf(self.horizontalSpacer), navigationButton)
            navigationButton.setChecked(True) if self.stackedWidget.indexOf(subPage) == 0 else None
        else:
            self.navigationArea.hide()

##############################################################################################################################