import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox, QInputDialog

class ContactManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contact Manager')
        
        # Layout utama
        self.layout = QVBoxLayout()
        
        # Widget daftar kontak
        self.contactList = QListWidget()
        self.layout.addWidget(self.contactList)
        
        # Layout untuk input dan tombol
        self.hbox = QHBoxLayout()
        
        # Input field untuk menambah kontak
        self.nameInput = QLineEdit()
        self.nameInput.setPlaceholderText('Name')
        self.hbox.addWidget(self.nameInput)
        
        self.phoneInput = QLineEdit()
        self.phoneInput.setPlaceholderText('Phone')
        self.hbox.addWidget(self.phoneInput)
        
        # Tombol tambah kontak
        self.addButton = QPushButton('Add Contact')
        self.addButton.clicked.connect(self.addContact)
        self.hbox.addWidget(self.addButton)
        
        # Tombol edit kontak
        self.editButton = QPushButton('Edit Contact')
        self.editButton.clicked.connect(self.editContact)
        self.hbox.addWidget(self.editButton)
        
        # Tombol hapus kontak
        self.deleteButton = QPushButton('Delete Contact')
        self.deleteButton.clicked.connect(self.deleteContact)
        self.hbox.addWidget(self.deleteButton)
        
        # Tambahkan layout horizontal ke layout utama
        self.layout.addLayout(self.hbox)
        
        # Set layout utama ke window
        self.setLayout(self.layout)
        
        # Inisialisasi kontak
        self.contacts = {}
        self.currentContact = None

    def addContact(self):
        name = self.nameInput.text()
        phone = self.phoneInput.text()
        if name and phone:
            if name in self.contacts:
                QMessageBox.warning(self, 'Warning', 'Contact already exists.')
            else:
                self.contacts[name] = phone
                self.contactList.addItem(f'{name}: {phone}')
                self.nameInput.clear()
                self.phoneInput.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Name and phone cannot be empty.')

    def editContact(self):
        selectedContact = self.contactList.currentItem()
        if selectedContact:
            name, phone = selectedContact.text().split(': ')
            newName, okName = QInputDialog.getText(self, 'Edit Contact', 'Edit name:', QLineEdit.Normal, name)
            newPhone, okPhone = QInputDialog.getText(self, 'Edit Contact', 'Edit phone:', QLineEdit.Normal, phone)
            if okName and newName and okPhone and newPhone:
                del self.contacts[name]
                self.contacts[newName] = newPhone
                selectedContact.setText(f'{newName}: {newPhone}')
        else:
            QMessageBox.warning(self, 'Warning', 'No contact selected.')

    def deleteContact(self):
        selectedContact = self.contactList.currentItem()
        if selectedContact:
            reply = QMessageBox.question(self, 'Delete Contact', 'Are you sure you want to delete this contact?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                name, _ = selectedContact.text().split(': ')
                del self.contacts[name]
                self.contactList.takeItem(self.contactList.row(selectedContact))
        else:
            QMessageBox.warning(self, 'Warning', 'No contact selected.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactManager()
    window.show()
    sys.exit(app.exec_())
