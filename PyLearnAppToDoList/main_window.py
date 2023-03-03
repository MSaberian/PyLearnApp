# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(368, 422)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.verticalLayout.addLayout(self.gl_tasks)

        self.btn_newtask = QPushButton(self.centralwidget)
        self.btn_newtask.setObjectName(u"btn_newtask")
        font = QFont()
        font.setPointSize(15)
        self.btn_newtask.setFont(font)

        self.verticalLayout.addWidget(self.btn_newtask)

        self.tb_new_task_title = QLineEdit(self.centralwidget)
        self.tb_new_task_title.setObjectName(u"tb_new_task_title")
        self.tb_new_task_title.setFont(font)

        self.verticalLayout.addWidget(self.tb_new_task_title)

        self.tb_new_task_description = QTextEdit(self.centralwidget)
        self.tb_new_task_description.setObjectName(u"tb_new_task_description")
        self.tb_new_task_description.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.tb_new_task_description)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 368, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_newtask.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

