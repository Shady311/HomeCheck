# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeCheck_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(600, 210)
        MainWindow.setBaseSize(QSize(10, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setWeight(QFont.Black)
        font.setItalic(False)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle(u"HomeCheck")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(229, 229, 229);\n"
"font: 900 12pt \"Segoe UI\";\n"
"border-radius: 5px;")
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(20, 0, 561, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(18)
        font1.setWeight(QFont.Black)
        font1.setItalic(False)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 900 18pt \"Segoe UI\";")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_disk = QLabel(self.centralwidget)
        self.label_disk.setObjectName(u"label_disk")
        self.label_disk.setGeometry(QRect(20, 50, 81, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_disk.setFont(font2)
        self.label_disk.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_disk.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_disk.setTextFormat(Qt.TextFormat.AutoText)
        self.label_disk.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.listView_curdir = QListWidget(self.centralwidget)
        self.listView_curdir.setObjectName(u"listView_curdir")
        self.listView_curdir.setEnabled(False)
        self.listView_curdir.setGeometry(QRect(20, 100, 461, 31))
        self.listView_curdir.setStyleSheet(u"background-color: rgb(74, 101, 114);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Segoe UI\";\n"
"border: none;")
        self.listView_curdir.setWordWrap(True)
        self.label_year = QLabel(self.centralwidget)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setGeometry(QRect(170, 50, 41, 31))
        self.label_year.setFont(font2)
        self.label_year.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_year.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_year.setTextFormat(Qt.TextFormat.AutoText)
        self.label_year.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_month = QLabel(self.centralwidget)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setGeometry(QRect(350, 50, 61, 31))
        self.label_month.setFont(font2)
        self.label_month.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_month.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_month.setTextFormat(Qt.TextFormat.AutoText)
        self.label_month.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.listView_log = QListWidget(self.centralwidget)
        self.listView_log.setObjectName(u"listView_log")
        self.listView_log.setEnabled(False)
        self.listView_log.setGeometry(QRect(70, 140, 411, 51))
        self.listView_log.setStyleSheet(u"background-color: rgb(74, 101, 114);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Segoe UI\";\n"
"border: none;")
        self.listView_log.setWordWrap(True)
        self.label_log = QLabel(self.centralwidget)
        self.label_log.setObjectName(u"label_log")
        self.label_log.setGeometry(QRect(20, 140, 41, 51))
        self.label_log.setFont(font2)
        self.label_log.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_log.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_log.setTextFormat(Qt.TextFormat.AutoText)
        self.label_log.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButton_Create = QPushButton(self.centralwidget)
        self.pushButton_Create.setObjectName(u"pushButton_Create")
        self.pushButton_Create.setGeometry(QRect(490, 50, 91, 141))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(16)
        font3.setWeight(QFont.Black)
        font3.setItalic(False)
        self.pushButton_Create.setFont(font3)
        self.pushButton_Create.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(249, 170, 51);\n"
"color: rgb(40, 47, 57);\n"
"font: 900 16pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(35, 47, 52);\n"
"color: rgb(255, 255, 255);\n"
"font: 900 18pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}")
        self.pushButton_Create.setAutoDefault(False)
        self.pushButton_Create.setFlat(False)
        self.dateEdit_year = QDateEdit(self.centralwidget)
        self.dateEdit_year.setObjectName(u"dateEdit_year")
        self.dateEdit_year.setEnabled(True)
        self.dateEdit_year.setGeometry(QRect(220, 50, 121, 31))
        self.dateEdit_year.setSizeIncrement(QSize(5, 0))
        self.dateEdit_year.setCursor(QCursor(Qt.ArrowCursor))
        self.dateEdit_year.setAcceptDrops(False)
        self.dateEdit_year.setToolTipDuration(-1)
        self.dateEdit_year.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.dateEdit_year.setStyleSheet(u"background-color: rgb(249, 170, 51);\n"
"color: rgb(40, 47, 57);\n"
"font: 900 12pt \"Segoe UI\";\n"
"border-radius: 9px; ")
        self.dateEdit_year.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)
        self.dateEdit_year.setWrapping(False)
        self.dateEdit_year.setReadOnly(False)
        self.dateEdit_year.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.dateEdit_year.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.dateEdit_year.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.comboBox_disk = QComboBox(self.centralwidget)
        self.comboBox_disk.addItem("")
        self.comboBox_disk.addItem("")
        self.comboBox_disk.addItem("")
        self.comboBox_disk.addItem("")
        self.comboBox_disk.addItem("")
        self.comboBox_disk.setObjectName(u"comboBox_disk")
        self.comboBox_disk.setGeometry(QRect(110, 50, 51, 31))
        self.comboBox_disk.setStyleSheet(u"background-color: rgb(249, 170, 51);\n"
"color: rgb(40, 47, 57);\n"
"font: 900 12pt \"Segoe UI\";\n"
"border-radius: 9px; ")
        self.dateEdit_month = QDateEdit(self.centralwidget)
        self.dateEdit_month.setObjectName(u"dateEdit_month")
        self.dateEdit_month.setGeometry(QRect(410, 50, 71, 31))
        self.dateEdit_month.setSizeIncrement(QSize(5, 0))
        self.dateEdit_month.setAcceptDrops(False)
        self.dateEdit_month.setToolTipDuration(-1)
        self.dateEdit_month.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.dateEdit_month.setStyleSheet(u"background-color: rgb(249, 170, 51);\n"
"color: rgb(40, 47, 57);\n"
"font: 900 12pt \"Segoe UI\";\n"
"border-radius: 9px; ")
        self.dateEdit_month.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)
        self.dateEdit_month.setWrapping(False)
        self.dateEdit_month.setReadOnly(False)
        self.dateEdit_month.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.dateEdit_month.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.dateEdit_month.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_Create.setDefault(False)
        self.comboBox_disk.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"HomeCheck", None))
        self.label_disk.setText(QCoreApplication.translate("MainWindow", u"Change: disk", None))
        self.label_year.setText(QCoreApplication.translate("MainWindow", u"year:", None))
        self.label_month.setText(QCoreApplication.translate("MainWindow", u"month:", None))
        self.label_log.setText(QCoreApplication.translate("MainWindow", u"Log:", None))
        self.pushButton_Create.setText(QCoreApplication.translate("MainWindow", u"Create!", None))
        self.dateEdit_year.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy", None))
        self.comboBox_disk.setItemText(0, QCoreApplication.translate("MainWindow", u"C", None))
        self.comboBox_disk.setItemText(1, QCoreApplication.translate("MainWindow", u"D", None))
        self.comboBox_disk.setItemText(2, QCoreApplication.translate("MainWindow", u"E", None))
        self.comboBox_disk.setItemText(3, QCoreApplication.translate("MainWindow", u"F", None))
        self.comboBox_disk.setItemText(4, QCoreApplication.translate("MainWindow", u"G", None))

        self.comboBox_disk.setCurrentText(QCoreApplication.translate("MainWindow", u"E", None))
        self.dateEdit_month.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM", None))
        pass
    # retranslateUi

