import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt,QTimer, QTime

class CountdownTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Countdown Timer')
        
        # Layout utama
        self.layout = QVBoxLayout()
        
        # Label untuk menampilkan waktu
        self.timeLabel = QLabel('00:00:00')
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.timeLabel)
        
        # Input field untuk waktu awal
        self.timeEdit = QLineEdit()
        self.timeEdit.setPlaceholderText('Enter time in format HH:MM:SS')
        self.layout.addWidget(self.timeEdit)
        
        # Layout untuk tombol
        self.hbox = QHBoxLayout()
        
        # Tombol mulai timer
        self.startButton = QPushButton('Start')
        self.startButton.clicked.connect(self.startTimer)
        self.hbox.addWidget(self.startButton)
        
        # Tombol hentikan timer
        self.stopButton = QPushButton('Stop')
        self.stopButton.clicked.connect(self.stopTimer)
        self.stopButton.setEnabled(False)
        self.hbox.addWidget(self.stopButton)
        
        # Tambahkan layout horizontal ke layout utama
        self.layout.addLayout(self.hbox)
        
        # Set layout utama ke window
        self.setLayout(self.layout)
        
        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.startTime = QTime(0, 0, 0)

    def startTimer(self):
        time_str = self.timeEdit.text()
        if not time_str:
            QMessageBox.warning(self, 'Warning', 'Please enter a valid time.')
            return
        
        time_components = time_str.split(':')
        if len(time_components) != 3:
            QMessageBox.warning(self, 'Warning', 'Invalid time format. Please enter time in HH:MM:SS format.')
            return
        
        try:
            hours = int(time_components[0])
            minutes = int(time_components[1])
            seconds = int(time_components[2])
            if hours < 0 or minutes < 0 or seconds < 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, 'Warning', 'Invalid time values. Please enter non-negative integers.')
            return
        
        self.startTime = QTime(hours, minutes, seconds)
        self.timer.start(1000)
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)

    def stopTimer(self):
        self.timer.stop()
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)

    def updateTime(self):
        self.startTime = self.startTime.addSecs(-1)
        if self.startTime.hour() == 0 and self.startTime.minute() == 0 and self.startTime.second() == 0:
            self.timer.stop()
            QMessageBox.information(self, 'Countdown Finished', 'Time is up!')
            self.startButton.setEnabled(True)
            self.stopButton.setEnabled(False)
        self.timeLabel.setText(self.startTime.toString('hh:mm:ss'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = CountdownTimer()
    timer.show()
    sys.exit(app.exec_())
