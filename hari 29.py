import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget

class BookManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Book Manager')
        
        # Layout utama
        self.layout = QVBoxLayout()
        
        # Label judul
        self.titleLabel = QLabel('Title:')
        self.layout.addWidget(self.titleLabel)
        
        # Input field judul
        self.titleEdit = QLineEdit()
        self.layout.addWidget(self.titleEdit)
        
        # Label penulis
        self.authorLabel = QLabel('Author:')
        self.layout.addWidget(self.authorLabel)
        
        # Input field penulis
        self.authorEdit = QLineEdit()
        self.layout.addWidget(self.authorEdit)
        
        # Tombol tambah buku
        self.addButton = QPushButton('Add Book')
        self.addButton.clicked.connect(self.addBook)
        self.layout.addWidget(self.addButton)
        
        # Daftar buku
        self.bookList = QListWidget()
        self.layout.addWidget(self.bookList)
        
        # Tombol hapus buku
        self.deleteButton = QPushButton('Delete Book')
        self.deleteButton.clicked.connect(self.deleteBook)
        self.layout.addWidget(self.deleteButton)
        
        # Set layout utama ke window
        self.setLayout(self.layout)
        
        # Inisialisasi daftar buku
        self.books = []

    def addBook(self):
        title = self.titleEdit.text()
        author = self.authorEdit.text()
        if title and author:
            self.books.append((title, author))
            self.bookList.addItem(f'{title} - {author}')
            self.titleEdit.clear()
            self.authorEdit.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter both title and author.')

    def deleteBook(self):
        selected_book = self.bookList.currentRow()
        if selected_book >= 0:
            del self.books[selected_book]
            self.bookList.takeItem(selected_book)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    manager = BookManager()
    manager.show()
    sys.exit(app.exec_())
