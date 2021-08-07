from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from messagebox import Ui_MainWindow
import sys

class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.exit_button.clicked.connect(self.show_dialog)

    def show_dialog(self):
        result = QMessageBox.question(self, 'Close','Are you sure?',
                                      QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore,
                                      QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print('Yes Clicked')
            QtWidgets.qApp.quit()
        else:
            print('no clicked')




def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

create_app()