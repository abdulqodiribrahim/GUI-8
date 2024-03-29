import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow

class MainWindow_EXEC():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)

        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.update_calendar()
        self.update_progressbar()

        MainWindow.show()
        sys.exit(app.exec_())

    def update_calendar(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)

    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    def update_progressbar(self):
        radio3 = self.ui.Select.text()
        self.ui.Select.setText('Set Progressbar')
        radio3_upd = self.ui.Select.text()
        print (radio3,radio3_upd)

        self.ui.Select.clicked.connect(self.set_progressbar)

    def set_progressbar(self):
        progress_value = self.ui.progressBar.value()
        print('progressBar: ', progress_value)
        new_value = self.ui.lcdNumber.value()
        self.ui.progressBar.setValue(new_value)
        print('progressBar: ', self.ui.progressBar.value())

if __name__ == "__main__":
    MainWindow_EXEC()