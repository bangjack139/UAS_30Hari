import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTextEdit, QListWidget, QMessageBox, QFileDialog

class SimpleNoteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Note App')
        
        # Layout utama
        self.layout = QVBoxLayout()
        
        # Widget daftar catatan
        self.noteList = QListWidget()
        self.noteList.clicked.connect(self.loadNote)
        self.layout.addWidget(self.noteList)
        
        # Widget teks untuk menulis catatan
        self.noteEditor = QTextEdit()
        self.layout.addWidget(self.noteEditor)
        
        # Layout untuk tombol
        self.hbox = QHBoxLayout()
        
        # Tombol tambah catatan
        self.newButton = QPushButton('New Note')
        self.newButton.clicked.connect(self.newNote)
        self.hbox.addWidget(self.newButton)
        
        # Tombol simpan catatan
        self.saveButton = QPushButton('Save Note')
        self.saveButton.clicked.connect(self.saveNote)
        self.hbox.addWidget(self.saveButton)
        
        # Tombol hapus catatan
        self.deleteButton = QPushButton('Delete Note')
        self.deleteButton.clicked.connect(self.deleteNote)
        self.hbox.addWidget(self.deleteButton)
        
        # Tambahkan layout horizontal ke layout utama
        self.layout.addLayout(self.hbox)
        
        # Set layout utama ke window
        self.setLayout(self.layout)
        
        # Inisialisasi catatan
        self.notes = {}
        self.currentNote = None

    def newNote(self):
        noteName, _ = QFileDialog.getSaveFileName(self, 'New Note', '', 'Text Files (*.txt)')
        if noteName:
            if os.path.exists(noteName):
                QMessageBox.warning(self, 'Warning', 'Note name already exists.')
            else:
                self.notes[noteName] = ''
                self.noteList.addItem(noteName)
                self.currentNote = noteName
                self.noteEditor.clear()

    def saveNote(self):
        if self.currentNote is not None:
            self.notes[self.currentNote] = self.noteEditor.toPlainText()
            with open(self.currentNote, 'w') as file:
                file.write(self.notes[self.currentNote])
            QMessageBox.information(self, 'Saved', 'Note saved successfully.')

    def loadNote(self):
        selectedNote = self.noteList.currentItem()
        if selectedNote:
            self.currentNote = selectedNote.text()
            with open(self.currentNote, 'r') as file:
                self.notes[self.currentNote] = file.read()
            self.noteEditor.setPlainText(self.notes[self.currentNote])

    def deleteNote(self):
        selectedNote = self.noteList.currentItem()
        if selectedNote:
            reply = QMessageBox.question(self, 'Delete Note', 'Are you sure you want to delete this note?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                noteName = selectedNote.text()
                del self.notes[noteName]
                self.noteList.takeItem(self.noteList.row(selectedNote))
                self.noteEditor.clear()
                self.currentNote = None
                if os.path.exists(noteName):
                    os.remove(noteName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleNoteApp()
    window.show()
    sys.exit(app.exec_())
