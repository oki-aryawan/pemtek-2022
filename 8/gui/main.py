import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("suhu.ui", self)

        self.hitung.clicked.connect(self.konversi)
        self.cel.textChanged.connect(self.kosong)
        self.Selesai.clicked.connect(self.keluar)

    def konversi(self):
        a = 10



app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
# Setingan Width dan Height untuk Fullscreen
# widget.setFixedWidth(1920)
# widget.setFixedHeight(1000)
widget.setFixedWidth(527)
widget.setFixedHeight(446)
widget.show()
sys.exit(app.exec_())