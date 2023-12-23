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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import ui.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(960, 540))
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
"}\n"
"QLabel#topLabel{\n"
"	background-color:#22223a;\n"
"	color:#e6e6e6;\n"
"	font-size:12pt;\n"
"}\n"
"QLabel#settingLabel{\n"
"	color:#ededed;\n"
"}\n"
"QLabel#lineLabel{\n"
"	background-color:#ededed;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QFrame(self.styleSheet)
        self.background.setObjectName(u"background")
        self.horizontalLayout = QHBoxLayout(self.background)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(self.background)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setMinimumSize(QSize(60, 0))
        self.leftFrame.setMaximumSize(QSize(60, 16777215))
        self.leftFrame.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 15, 0, 0)
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
        self.buttonFrame.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#434458;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:#535468;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.buttonFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 15, 0, 0)
        self.reserveButton = QPushButton(self.buttonFrame)
        self.reserveButton.setObjectName(u"reserveButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.reserveButton.sizePolicy().hasHeightForWidth())
        self.reserveButton.setSizePolicy(sizePolicy3)
        self.reserveButton.setMinimumSize(QSize(60, 60))
        self.reserveButton.setMaximumSize(QSize(60, 60))
        self.reserveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.reserveButton.setStyleSheet(u"background-color:#434458;")
        icon = QIcon()
        icon.addFile(u":/resource/img/reserve.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reserveButton.setIcon(icon)
        self.reserveButton.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.reserveButton, 0, Qt.AlignHCenter)

        self.mineButton = QPushButton(self.buttonFrame)
        self.mineButton.setObjectName(u"mineButton")
        sizePolicy3.setHeightForWidth(self.mineButton.sizePolicy().hasHeightForWidth())
        self.mineButton.setSizePolicy(sizePolicy3)
        self.mineButton.setMinimumSize(QSize(60, 60))
        self.mineButton.setMaximumSize(QSize(60, 60))
        self.mineButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/resource/img/mine.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mineButton.setIcon(icon1)
        self.mineButton.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.mineButton, 0, Qt.AlignHCenter)

        self.hintButton = QPushButton(self.buttonFrame)
        self.hintButton.setObjectName(u"hintButton")
        sizePolicy3.setHeightForWidth(self.hintButton.sizePolicy().hasHeightForWidth())
        self.hintButton.setSizePolicy(sizePolicy3)
        self.hintButton.setMinimumSize(QSize(60, 60))
        self.hintButton.setMaximumSize(QSize(60, 60))
        self.hintButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/resource/img/hint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hintButton.setIcon(icon2)
        self.hintButton.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.hintButton, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.buttonFrame, 0, Qt.AlignRight)

        self.settingFrame = QFrame(self.leftFrame)
        self.settingFrame.setObjectName(u"settingFrame")
        self.verticalLayout_7 = QVBoxLayout(self.settingFrame)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.logoutButton = QPushButton(self.settingFrame)
        self.logoutButton.setObjectName(u"logoutButton")
        sizePolicy3.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy3)
        self.logoutButton.setMinimumSize(QSize(60, 40))
        self.logoutButton.setMaximumSize(QSize(60, 40))
        self.logoutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.logoutButton.setStyleSheet(u"background-color:transparent;")
        icon3 = QIcon()
        icon3.addFile(u":/resource/img/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutButton.setIcon(icon3)
        self.logoutButton.setIconSize(QSize(28, 28))

        self.verticalLayout_7.addWidget(self.logoutButton)

        self.settingButton = QPushButton(self.settingFrame)
        self.settingButton.setObjectName(u"settingButton")
        sizePolicy3.setHeightForWidth(self.settingButton.sizePolicy().hasHeightForWidth())
        self.settingButton.setSizePolicy(sizePolicy3)
        self.settingButton.setMinimumSize(QSize(60, 40))
        self.settingButton.setMaximumSize(QSize(60, 40))
        self.settingButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingButton.setStyleSheet(u"background-color:transparent;")
        icon4 = QIcon()
        icon4.addFile(u":/resource/img/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingButton.setIcon(icon4)
        self.settingButton.setIconSize(QSize(28, 28))
        self.settingButton.setAutoRepeat(False)

        self.verticalLayout_7.addWidget(self.settingButton)


        self.verticalLayout_2.addWidget(self.settingFrame, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftFrame)

        self.extraFrame = QFrame(self.background)
        self.extraFrame.setObjectName(u"extraFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.extraFrame.sizePolicy().hasHeightForWidth())
        self.extraFrame.setSizePolicy(sizePolicy4)
        self.extraFrame.setMinimumSize(QSize(0, 0))
        self.extraFrame.setMaximumSize(QSize(240, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.extraFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 20, 0, 0)
        self.settingLabel = QLabel(self.extraFrame)
        self.settingLabel.setObjectName(u"settingLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.settingLabel.sizePolicy().hasHeightForWidth())
        self.settingLabel.setSizePolicy(sizePolicy5)
        self.settingLabel.setStyleSheet(u"font-size:18pt;\n"
"font-weight:600;")
        self.settingLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.settingLabel)

        self.verticalSpacer = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.lineLabel = QLabel(self.extraFrame)
        self.lineLabel.setObjectName(u"lineLabel")
        self.lineLabel.setMinimumSize(QSize(0, 2))
        self.lineLabel.setMaximumSize(QSize(16777215, 2))
        self.lineLabel.setStyleSheet(u"margin:0 20px;")

        self.verticalLayout_3.addWidget(self.lineLabel)

        self.frame = QFrame(self.extraFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.extraFrame)

        self.contentFrame = QFrame(self.background)
        self.contentFrame.setObjectName(u"contentFrame")
        self.verticalLayout_4 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.topLabel = QLabel(self.contentFrame)
        self.topLabel.setObjectName(u"topLabel")
        sizePolicy4.setHeightForWidth(self.topLabel.sizePolicy().hasHeightForWidth())
        self.topLabel.setSizePolicy(sizePolicy4)
        self.topLabel.setMinimumSize(QSize(0, 40))
        self.topLabel.setMaximumSize(QSize(16777215, 40))
        self.topLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.topLabel)

        self.contentContainer = QFrame(self.contentFrame)
        self.contentContainer.setObjectName(u"contentContainer")
        self.contentContainer.setFrameShape(QFrame.StyledPanel)
        self.contentContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.contentContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.contentContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.reservePage = QWidget()
        self.reservePage.setObjectName(u"reservePage")
        self.label = QLabel(self.reservePage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 330, 54, 16))
        self.stackedWidget.addWidget(self.reservePage)
        self.minePage = QWidget()
        self.minePage.setObjectName(u"minePage")
        self.label_2 = QLabel(self.minePage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 310, 54, 16))
        self.stackedWidget.addWidget(self.minePage)
        self.hintPage = QWidget()
        self.hintPage.setObjectName(u"hintPage")
        self.label_3 = QLabel(self.hintPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(580, 320, 54, 16))
        self.stackedWidget.addWidget(self.hintPage)

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.contentContainer)


        self.horizontalLayout.addWidget(self.contentFrame)


        self.verticalLayout.addWidget(self.background)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u4e66\u9986", None))
        self.iconLabel.setText("")
        self.reserveButton.setText("")
        self.mineButton.setText("")
        self.hintButton.setText("")
        self.logoutButton.setText("")
        self.settingButton.setText("")
        self.settingLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.lineLabel.setText("")
        self.topLabel.setText(QCoreApplication.translate("MainWindow", u"\u4f60\u7684\u5b66\u53f7\uff1a\u672a\u77e5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Reserve", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mine", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hint", None))
    # retranslateUi

