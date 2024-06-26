import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        
        # Layout utama
        self.layout = QVBoxLayout()
        
        # Label untuk menampilkan waktu
        self.timeLabel = QLabel()
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.timeLabel.setStyleSheet("font-size: 48px;")
        self.layout.addWidget(self.timeLabel)
        
        # Set layout utama ke window
        self.setLayout(self.layout)
        
        # Timer untuk memperbarui waktu setiap detik
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)  # 1000 ms = 1 detik
        
        # Tampilkan waktu saat ini
        self.showTime()

    def showTime(self):
        currentTime = QTime.currentTime()
        timeString = currentTime.toString('hh:mm:ss')
        self.timeLabel.setText(timeString)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
