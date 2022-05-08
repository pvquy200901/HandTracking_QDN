import  sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Loading import Ui_Loading
from DesignerHandTracking import Ui_Dialog
from  User import Ui_MainWindow

couter = 0

class MainWindow(QDialog):
    def  __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnUManual.clicked.connect(self.fUserManual)
    def fUserManual(self):
        self.UserManual = QtWidgets.QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.UserManual)
        self.UserManual.show()
class Loading(QDialog):
    def  __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Loading()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        self.ui.DropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progressBar)

        self.timer.start(25)


        self.show()
    def progressBar(self):
        global  couter

        self.ui.progressBar.setValue(couter)

        if couter > 100:
            self.timer.stop()

            self.main = MainWindow()
            self.main.show()

            self.close()
        couter += 1


if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = Loading()
    sys.exit(app.exec_())