# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'information.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Information(object):
    def setupUi(self, Information):
        if not Information.objectName():
            Information.setObjectName(u"Information")
        Information.resize(300, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Information.sizePolicy().hasHeightForWidth())
        Information.setSizePolicy(sizePolicy)
        Information.setMinimumSize(QSize(300, 150))
        Information.setMaximumSize(QSize(300, 150))
        Information.setStyleSheet(u"background-color:#0f102c;")
        self.verticalLayout = QVBoxLayout(Information)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.label = QLabel(Information)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white;font-size:16px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(Information)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setStyleSheet(u"QPushButton{\n"
"	background-color:#434458;\n"
"	color:white;\n"
"	font-size:14px;\n"
"	font-weight:600;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#333448;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(70, 30))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Information)

        QMetaObject.connectSlotsByName(Information)
    # setupUi

    def retranslateUi(self, Information):
        Information.setWindowTitle(QCoreApplication.translate("Information", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Information", u"\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef\uff01", None))
        self.pushButton.setText(QCoreApplication.translate("Information", u"\u786e\u8ba4", None))
    # retranslateUi

