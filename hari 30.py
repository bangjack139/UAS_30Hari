import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
class RandomQuoteGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Random Quote Generator')
        
        # Layout utama
        self.layout = QVBoxLayout()
        
        # Label untuk menampilkan kutipan
        self.quoteLabel = QLabel()
        self.quoteLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.quoteLabel)
        
        # Tombol untuk menghasilkan kutipan baru
        self.generateButton = QPushButton('Generate Quote')
        self.generateButton.clicked.connect(self.generateQuote)
        self.layout.addWidget(self.generateButton)
        
        # Set layout utama ke window
        self.setLayout(self.layout)

        # Daftar kutipan
        self.quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Innovation distinguishes between a leader and a follower. - Steve Jobs",
            "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
            "Stay hungry, stay foolish. - Steve Jobs",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
            "Life is like riding a bicycle. To keep your balance, you must keep moving. - Albert Einstein",
            "The only impossible journey is the one you never begin. - Tony Robbins",
            "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
            "It does not matter how slowly you go as long as you do not stop. - Confucius"
        ]

    def generateQuote(self):
        quote = random.choice(self.quotes)
        self.quoteLabel.setText(quote)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = RandomQuoteGenerator()
    generator.show()
    sys.exit(app.exec_())

