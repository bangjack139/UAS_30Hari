import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox, QInputDialog

class ToDoListManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('To-Do List Manager')
        
        # Layout utama
        self.layout = QVBoxLayout()
        
        # Widget daftar tugas
        self.taskList = QListWidget()
        self.layout.addWidget(self.taskList)
        
        # Layout untuk input dan tombol
        self.hbox = QHBoxLayout()
        
        # Input field untuk menambah tugas
        self.taskInput = QLineEdit()
        self.hbox.addWidget(self.taskInput)
        
        # Tombol tambah tugas
        self.addButton = QPushButton('Add Task')
        self.addButton.clicked.connect(self.addTask)
        self.hbox.addWidget(self.addButton)
        
        # Tombol edit tugas
        self.editButton = QPushButton('Edit Task')
        self.editButton.clicked.connect(self.editTask)
        self.hbox.addWidget(self.editButton)
        
        # Tombol hapus tugas
        self.deleteButton = QPushButton('Delete Task')
        self.deleteButton.clicked.connect(self.deleteTask)
        self.hbox.addWidget(self.deleteButton)
        
        # Tambahkan layout horizontal ke layout utama
        self.layout.addLayout(self.hbox)
        
        # Set layout utama ke window
        self.setLayout(self.layout)

    def addTask(self):
        task = self.taskInput.text()
        if task:
            self.taskList.addItem(task)
            self.taskInput.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Task cannot be empty.')

    def editTask(self):
        selectedTask = self.taskList.currentItem()
        if selectedTask:
            newTask, ok = QInputDialog.getText(self, 'Edit Task', 'Edit task:', QLineEdit.Normal, selectedTask.text())
            if ok and newTask:
                selectedTask.setText(newTask)
        else:
            QMessageBox.warning(self, 'Warning', 'No task selected.')

    def deleteTask(self):
        selectedTask = self.taskList.currentItem()
        if selectedTask:
            self.taskList.takeItem(self.taskList.row(selectedTask))
        else:
            QMessageBox.warning(self, 'Warning', 'No task selected.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToDoListManager()
    window.show()
    sys.exit(app.exec_())
