import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui


class MainWindow(QtWidgets):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("calc-suhu.ui", self)

        self.hitung.clicked.connect(self.konversi)
        self.cel.textChanged.connect(self.kosong)
        self.Selesai.clicked.connect(self.keluar)

    def konversi(self):
        C = self.cel.text()
        R = float(C) * 0.8
        K = float(C) + 273
        F = float(C) * (9 / 5) + 32

        self.rea.setText(str(R))
        self.fah.setText(str(F))
        self.kal.setText(str(K))

    def kosong(self):
        self.rea.setText('')
        self.fah.setText('')
        self.kal.setText('')

    def keluar(self):
        sys.exit(app.exec_())


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
