# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 501, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 10, 481, 331))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 221, 131))
        self.groupBox.setObjectName("groupBox")
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(10, 30, 151, 76))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Default = QtWidgets.QRadioButton(self.widget1)
        self.Default.setObjectName("Default")
        self.verticalLayout_2.addWidget(self.Default)
        self.Reset = QtWidgets.QRadioButton(self.widget1)
        self.Reset.setObjectName("Reset")
        self.verticalLayout_2.addWidget(self.Reset)
        self.Select = QtWidgets.QRadioButton(self.widget1)
        self.Select.setObjectName("Select")
        self.verticalLayout_2.addWidget(self.Select)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 20, 211, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget2.setGeometry(QtCore.QRect(10, 30, 191, 91))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dial = QtWidgets.QDial(self.widget2)
        self.dial.setObjectName("dial")
        self.horizontalLayout.addWidget(self.dial)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(20, 290, 441, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.widget3 = QtWidgets.QWidget(self.tab_2)
        self.widget3.setGeometry(QtCore.QRect(20, 170, 228, 101))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fontComboBox = QtWidgets.QFontComboBox(self.widget3)
        self.fontComboBox.setObjectName("fontComboBox")
        self.verticalLayout_3.addWidget(self.fontComboBox)
        self.label = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.Reset.clicked.connect(self.progressBar.reset)
        self.dial.valueChanged['int'].connect(self.lcdNumber.display)
        self.fontComboBox.activated['QString'].connect(self.label.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.groupBox.setTitle(_translate("MainWindow", "Chose Option"))
        self.Default.setText(_translate("MainWindow", "Default"))
        self.Reset.setText(_translate("MainWindow", "Reset ProgressBar"))
        self.Select.setText(_translate("MainWindow", "Select PrograssBar"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Move Dial Top Dial"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
