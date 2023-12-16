# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import ui.resource_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(1280, 720)
        LoginWindow.setMinimumSize(QSize(960, 540))
        self.StyleFrame = QWidget(LoginWindow)
        self.StyleFrame.setObjectName(u"StyleFrame")
        self.StyleFrame.setStyleSheet(u"QWidget#StyleFrame{\n"
"	background-color:#0f102c;\n"
"}\n"
"QFrame#Container {\n"
"	background-color:#22223a;\n"
"}\n"
"QLineEdit{\n"
"	background-color:#434458;\n"
"	color:white;\n"
"}\n"
"QPushButton{\n"
"	background-color:white;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#d1d1d1;\n"
"}\n"
"QLabel#codeLabel{\n"
"	background-color:#434458;\n"
"}\n"
"QFrame#titleFrame{\n"
"	background-color:#434458;;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.StyleFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contentLayout = QHBoxLayout()
        self.contentLayout.setObjectName(u"contentLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.contentLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.title = QLabel(self.StyleFrame)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"QLabel#title{\n"
"	background-color:transparent;\n"
"	color:white;\n"
"	font-size:40px;\n"
"	font-weight:900;\n"
"	margin-bottom:20px;\n"
"}")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)

        self.Container = QFrame(self.StyleFrame)
        self.Container.setObjectName(u"Container")
        self.Container.setMinimumSize(QSize(500, 300))
        self.Container.setStyleSheet(u"QFrame{\n"
"	border-radius:20px;\n"
"	padding:0 30px;\n"
"}\n"
"QLineEdit{\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"	font-size: 18px;\n"
"	border:0;\n"
"}\n"
"QLabel{\n"
"	padding:4px;\n"
"	border-radius:3px;\n"
"}\n"
"QPushButton{\n"
"	border-radius:20px;\n"
"	font-size:18px;\n"
"	font-weight:600;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.Container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.number = QLineEdit(self.Container)
        self.number.setObjectName(u"number")
        self.number.setMinimumSize(QSize(0, 50))
        self.number.setMaxLength(13)

        self.horizontalLayout.addWidget(self.number)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.password = QLineEdit(self.Container)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 50))
        self.password.setMaxLength(6)

        self.horizontalLayout_4.addWidget(self.password)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.code = QLineEdit(self.Container)
        self.code.setObjectName(u"code")
        self.code.setMinimumSize(QSize(0, 50))
        self.code.setMaxLength(4)

        self.horizontalLayout_5.addWidget(self.code)

        self.codeLabel = QLabel(self.Container)
        self.codeLabel.setObjectName(u"codeLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codeLabel.sizePolicy().hasHeightForWidth())
        self.codeLabel.setSizePolicy(sizePolicy)
        self.codeLabel.setMinimumSize(QSize(0, 0))
        self.codeLabel.setMaximumSize(QSize(200, 50))
        self.codeLabel.setTextFormat(Qt.PlainText)
        self.codeLabel.setPixmap(QPixmap(u":/resource/img/code.jpg"))
        self.codeLabel.setScaledContents(False)
        self.codeLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.codeLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.loginButton = QPushButton(self.Container)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(140, 45))
        self.loginButton.setMaximumSize(QSize(140, 16777215))
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.loginButton, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.Container)

        self.spacer = QLabel(self.StyleFrame)
        self.spacer.setObjectName(u"spacer")
        self.spacer.setStyleSheet(u"QLabel#spacer{\n"
"	background-color:transparent;\n"
"font-size:50px;\n"
"}")

        self.verticalLayout_2.addWidget(self.spacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.contentLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.contentLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.contentLayout)

        LoginWindow.setCentralWidget(self.StyleFrame)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"\u56fe\u4e66\u9986", None))
        self.title.setText(QCoreApplication.translate("LoginWindow", u"CAU Library Client", None))
        self.number.setText("")
        self.number.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u5b66\u53f7", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u5bc6\u7801\uff08\u8eab\u4efd\u8bc1\u540e6\u4f4d\uff0cX\u66ff\u6362\u4e3a0\uff09", None))
        self.code.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u9a8c\u8bc1\u7801", None))
        self.codeLabel.setText("")
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"\u767b    \u5f55", None))
        self.spacer.setText("")
    # retranslateUi

