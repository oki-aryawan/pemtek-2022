# Ketik 5 baris perintah untuk meng-import beberapa modul yang dibutuhkan
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui

# Pendefinisian Class
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
    # Memanggil file Design GUI yang sudah dibuat
        loadUi("LoadPicture.ui", self)
    # Mendefinisikan Perilaku obyek Push Button yang bernama "buka" 
    # jika di Click maka akan menjalankan sub/fungsi 'buka_gambar'
        self.buka.clicked.connect(self.buka_gambar)
        self.keluar.clicked.connect(self.menu_keluar)

    # Membuat/Mendefinisikan fungsi yang bernama 'buka_gambar' 
    def buka_gambar(self):
        
    # Menampilkan dialog untuk membuka file, gambar yang dipilih disimpan di variabel 'namaf'
        namaf=QFileDialog.getOpenFileName(self,'Pilih file gambar','c:')
    # Menampilkan file gambar 'namaf' yang dipilih pada QLabel yang bernama 'photo'
        self.photo.setPixmap(QtGui.QPixmap(namaf[0]))
        
    def menu_keluar(self):
        sys.exit(app.exec_())
        
app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1920)
widget.setFixedHeight(1000)
widget.show()
sys.exit(app.exec_())
        