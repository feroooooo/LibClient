# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import ui.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1232, 720)
        MainWindow.setMinimumSize(QSize(960, 540))
        MainWindow.setMaximumSize(QSize(1280, 720))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"QWidget#styleSheet{\n"
"	color: rgb(221, 221, 221);\n"
"	background-color:#434458;\n"
"}\n"
"QFrame#leftFrame{\n"
"	background-color:#0f102c;\n"
"}\n"
"QFrame#extraFrame{\n"
"	background-color:#22223a;\n"
"}\n"
"QFrame#contentFrame{\n"
"	background-color:#434458;\n"
"}\n"
"QFrame#iconFrame{\n"
"	background-color:#434458;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QFrame(self.styleSheet)
        self.background.setObjectName(u"background")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.background)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(self.background)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setMinimumSize(QSize(60, 0))
        self.leftFrame.setMaximumSize(QSize(60, 16777215))
        self.leftFrame.setStyleSheet(u"")
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.leftFrame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.iconFrame = QFrame(self.leftFrame)
        self.iconFrame.setObjectName(u"iconFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconFrame.sizePolicy().hasHeightForWidth())
        self.iconFrame.setSizePolicy(sizePolicy)
        self.iconFrame.setMinimumSize(QSize(50, 50))
        self.iconFrame.setMaximumSize(QSize(50, 50))
        self.iconFrame.setStyleSheet(u"border-radius:25px;")
        self.iconFrame.setFrameShape(QFrame.StyledPanel)
        self.iconFrame.setFrameShadow(QFrame.Raised)
        self.iconFrame.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.iconFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.iconLabel = QLabel(self.iconFrame)
        self.iconLabel.setObjectName(u"iconLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy1)
        self.iconLabel.setMaximumSize(QSize(40, 40))
        self.iconLabel.setStyleSheet(u"")
        self.iconLabel.setTextFormat(Qt.PlainText)
        self.iconLabel.setPixmap(QPixmap(u":/resource/img/icon.png"))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.iconLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.iconFrame, 0, Qt.AlignHCenter)

        self.buttonFrame = QFrame(self.leftFrame)
        self.buttonFrame.setObjectName(u"buttonFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.buttonFrame.sizePolicy().hasHeightForWidth())
        self.buttonFrame.setSizePolicy(sizePolicy2)
        self.buttonFrame.setMinimumSize(QSize(60, 0))
        self.buttonFrame.setStyleSheet(u"padding:0;")
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.buttonFrame)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 25, 0, 0)
        self.reserveButton = QPushButton(self.buttonFrame)
        self.reserveButton.setObjectName(u"reserveButton")
        sizePolicy2.setHeightForWidth(self.reserveButton.sizePolicy().hasHeightForWidth())
        self.reserveButton.setSizePolicy(sizePolicy2)
        self.reserveButton.setMinimumSize(QSize(50, 55))
        self.reserveButton.setMaximumSize(QSize(50, 55))
        self.reserveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.reserveButton.setStyleSheet(u"background-color:#434458;")
        icon = QIcon()
        icon.addFile(u":/resource/img/reserve.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reserveButton.setIcon(icon)
        self.reserveButton.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.reserveButton, 0, Qt.AlignHCenter)

        self.mineButton = QPushButton(self.buttonFrame)
        self.mineButton.setObjectName(u"mineButton")
        sizePolicy2.setHeightForWidth(self.mineButton.sizePolicy().hasHeightForWidth())
        self.mineButton.setSizePolicy(sizePolicy2)
        self.mineButton.setMinimumSize(QSize(50, 55))
        self.mineButton.setMaximumSize(QSize(50, 55))
        self.mineButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.mineButton.setStyleSheet(u"background-color:#434458;")
        icon1 = QIcon()
        icon1.addFile(u":/resource/img/mine.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mineButton.setIcon(icon1)
        self.mineButton.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.mineButton, 0, Qt.AlignHCenter)

        self.hintButton = QPushButton(self.buttonFrame)
        self.hintButton.setObjectName(u"hintButton")
        sizePolicy2.setHeightForWidth(self.hintButton.sizePolicy().hasHeightForWidth())
        self.hintButton.setSizePolicy(sizePolicy2)
        self.hintButton.setMinimumSize(QSize(50, 55))
        self.hintButton.setMaximumSize(QSize(50, 55))
        self.hintButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.hintButton.setStyleSheet(u"background-color:transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/resource/img/hint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hintButton.setIcon(icon2)
        self.hintButton.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.hintButton, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.buttonFrame, 0, Qt.AlignRight)

        self.settingFrame = QFrame(self.leftFrame)
        self.settingFrame.setObjectName(u"settingFrame")
        self.settingFrame.setStyleSheet(u"")
        self.settingFrame.setFrameShape(QFrame.StyledPanel)
        self.settingFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.settingFrame)


        self.horizontalLayout.addWidget(self.leftFrame)

        self.extraFrame = QFrame(self.background)
        self.extraFrame.setObjectName(u"extraFrame")
        self.extraFrame.setMinimumSize(QSize(0, 0))
        self.extraFrame.setMaximumSize(QSize(240, 16777215))
        self.extraFrame.setFrameShape(QFrame.StyledPanel)
        self.extraFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.extraFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.extraFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(240, 0))
        self.label_3.setMaximumSize(QSize(240, 16777215))
        self.label_3.setStyleSheet(u"b")

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.extraFrame)

        self.contentFrame = QFrame(self.background)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setFrameShape(QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.contentFrame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)


        self.horizontalLayout.addWidget(self.contentFrame)


        self.verticalLayout.addWidget(self.background)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u4e66\u9986", None))
        self.iconLabel.setText("")
        self.reserveButton.setText("")
        self.mineButton.setText("")
        self.hintButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"frame2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"frame3", None))
    # retranslateUi

