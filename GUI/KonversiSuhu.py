import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("KonversiSuhu.ui", self)

        self.Hitung.clicked.connect(self.konversi)
        self.Cel.textChanged.connect(self.kosong)
        self.Selesai.clicked.connect(self.keluar)

    def konversi(self):
        C = self.Cel.text()
        R = float(C)*0.8
        K = float(C)+273
        F = float(C)*(9/5) +32
        
        self.Rea.setText(str(R))
        self.Fah.setText(str(F))
        self.Kal.setText(str(K))
        
    def kosong(self):
        self.Rea.setText('')
        self.Fah.setText('')
        self.Kal.setText('')
    
    def keluar(self):
        sys.exit(app.exec_())
        
app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
# Setingan Width dan Height untuk Fullscreen
# widget.setFixedWidth(1920)
# widget.setFixedHeight(1000)
widget.setFixedWidth(527)
widget.setFixedHeight(446)
widget.show()
sys.exit(app.exec_())
        