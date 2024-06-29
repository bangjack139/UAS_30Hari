import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox, QMessageBox

class UnitConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Unit Converter')
        
        # Layout utama
        self.layout = QVBoxLayout()
        
        # Input field untuk nilai yang akan dikonversi
        self.inputValue = QLineEdit()
        self.inputValue.setPlaceholderText('Enter value')
        self.layout.addWidget(self.inputValue)
        
        # Dropdown untuk memilih satuan asal
        self.fromUnit = QComboBox()
        self.fromUnit.addItems(['Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Inch', 'Foot'])
        self.layout.addWidget(self.fromUnit)
        
        # Dropdown untuk memilih satuan tujuan
        self.toUnit = QComboBox()
        self.toUnit.addItems(['Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Inch', 'Foot'])
        self.layout.addWidget(self.toUnit)
        
        # Tombol untuk melakukan konversi
        self.convertButton = QPushButton('Convert')
        self.convertButton.clicked.connect(self.convert)
        self.layout.addWidget(self.convertButton)
        
        # Label untuk menampilkan hasil konversi
        self.resultLabel = QLabel('Result: ')
        self.layout.addWidget(self.resultLabel)
        
        # Set layout utama ke window
        self.setLayout(self.layout)
    
    def convert(self):
        value = self.inputValue.text()
        if not value:
            QMessageBox.warning(self, 'Warning', 'Please enter a value to convert.')
            return
        
        try:
            value = float(value)
        except ValueError:
            QMessageBox.warning(self, 'Warning', 'Invalid value. Please enter a numeric value.')
            return
        
        from_unit = self.fromUnit.currentText()
        to_unit = self.toUnit.currentText()
        
        # Satuan konversi dasar dalam meter
        units_in_meters = {
            'Meter': 1,
            'Kilometer': 1000,
            'Centimeter': 0.01,
            'Millimeter': 0.001,
            'Inch': 0.0254,
            'Foot': 0.3048
        }
        
        # Konversi dari satuan asal ke meter
        value_in_meters = value * units_in_meters[from_unit]
        
        # Konversi dari meter ke satuan tujuan
        result = value_in_meters / units_in_meters[to_unit]
        
        self.resultLabel.setText(f'Result: {result} {to_unit}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = UnitConverter()
    converter.show()
    sys.exit(app.exec_())
