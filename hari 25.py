import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Viewer')
        
        # Layout utama
        self.layout = QVBoxLayout()
        
        # Label untuk menampilkan gambar
        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.imageLabel)
        
        # Tombol untuk membuka gambar
        self.openButton = QPushButton('Open Image')
        self.openButton.clicked.connect(self.openImage)
        self.layout.addWidget(self.openButton)
        
        # Set layout utama ke window
        self.setLayout(self.layout)

    def openImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.jpg *.jpeg *.bmp *.gif)', options=options)
        if fileName:
            pixmap = QPixmap(fileName)
            if pixmap.isNull():
                QMessageBox.warning(self, 'Warning', 'Cannot load image.')
            else:
                self.imageLabel.setPixmap(pixmap.scaled(self.imageLabel.size(), Qt.KeepAspectRatio))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())
