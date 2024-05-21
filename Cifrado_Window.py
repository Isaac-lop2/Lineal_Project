from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QApplication, QMessageBox, QTextEdit
)
from PyQt5.QtGui import QFont
import sys

class CifradoWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Cifrado por Matrices")
        self.setFixedSize(640, 480)
        self.app = app

        self.initUI()

    def initUI(self):
        # Widget central
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #E0EBFF")
        self.setCentralWidget(central_widget)

        # Diseño vertical para los widgets
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Campo de entrada para el mensaje
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Ingrese el mensaje a cifrar")
        layout.addWidget(self.message_input)

        # Botón para generar la tabla de la matriz clave
        self.generate_matrix_button = QPushButton("Generar Matriz Clave")
        self.generate_matrix_button.clicked.connect(self.generate_matrix)
        layout.addWidget(self.generate_matrix_button)

        # Crear QTableWidget para la matriz clave
        self.matrix_table = QTableWidget()
        layout.addWidget(self.matrix_table)

        # Botones para cifrar y descifrar
        self.encrypt_button = QPushButton("Cifrar Mensaje")
        self.encrypt_button.clicked.connect(self.encrypt_message)
        layout.addWidget(self.encrypt_button)

        # Campo de texto para mostrar los números cifrados
        self.encrypted_numbers = QTextEdit()
        self.encrypted_numbers.setPlaceholderText("Números cifrados")
        layout.addWidget(self.encrypted_numbers)

        # Campo de entrada para los números cifrados
        self.encrypted_input = QLineEdit()
        self.encrypted_input.setPlaceholderText("Ingrese los números cifrados para descifrar")
        layout.addWidget(self.encrypted_input)

        self.decrypt_button = QPushButton("Descifrar Mensaje")
        self.decrypt_button.clicked.connect(self.decrypt_message)
        layout.addWidget(self.decrypt_button)

        # Etiqueta para mostrar el mensaje cifrado/descifrado
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 14))
        layout.addWidget(self.result_label)

    def generate_matrix(self):
        size = len(self.message_input.text())
        self.matrix_table.setRowCount(size)
        self.matrix_table.setColumnCount(size)

        for i in range(size):
            for j in range(size):
                self.matrix_table.setItem(i, j, QTableWidgetItem("1" if i == j else "0"))

    def get_matrix(self):
        size = self.matrix_table.rowCount()
        matrix = []

        try:
            for i in range(size):
                row = []
                for j in range(size):
                    item = self.matrix_table.item(i, j)
                    if item and item.text():
                        row.append(float(item.text()))
                    else:
                        row.append(0.0)
                matrix.append(row)
            return matrix
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese valores numéricos válidos en la matriz.")
            return None

    def encrypt_message(self):
        message = self.message_input.text()
        if not message:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un mensaje para cifrar.")
            return

        matrix = self.get_matrix()
        if matrix is None:
            return

        size = len(matrix)
        vector = [ord(char) for char in message]

        # Padding if necessary
        while len(vector) < size:
            vector.append(0)

        encrypted_vector = self.matrix_vector_mult(matrix, vector)
        encrypted_message = ''.join(chr(int(round(num))) for num in encrypted_vector)

        self.result_label.setText(f"Mensaje Cifrado: {encrypted_message}")
        self.encrypted_numbers.setText(' '.join(map(str, encrypted_vector)))

    def decrypt_message(self):
        encrypted_numbers_text = self.encrypted_input.text()
        if not encrypted_numbers_text:
            QMessageBox.warning(self, "Error", "Por favor, ingrese los números cifrados para descifrar.")
            return

        try:
            encrypted_vector = list(map(int, encrypted_numbers_text.split()))
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese una lista válida de números cifrados.")
            return

        matrix = self.get_matrix()
        if matrix is None:
            return

        try:
            inverse_matrix = self.invert_matrix(matrix)
            decrypted_vector = self.matrix_vector_mult(inverse_matrix, encrypted_vector)
            decrypted_message = ''.join(chr(int(round(num))) for num in decrypted_vector).rstrip('\x00')

            self.result_label.setText(f"Mensaje Descifrado: {decrypted_message}")
        except ValueError:
            QMessageBox.warning(self, "Error", "La matriz no es invertible. No se puede descifrar el mensaje.")

    def matrix_vector_mult(self, matrix, vector):
        result = []
        for row in matrix:
            result.append(sum(row[i] * vector[i] for i in range(len(vector))))
        return result

    def invert_matrix(self, matrix):
        size = len(matrix)
        identity = [[float(i == j) for i in range(size)] for j in range(size)]

        for i in range(size):
            # Search for maximum in this column
            max_el = abs(matrix[i][i])
            max_row = i
            for k in range(i + 1, size):
                if abs(matrix[k][i]) > max_el:
                    max_el = abs(matrix[k][i])
                    max_row = k

            # Swap maximum row with current row (column by column)
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            identity[i], identity[max_row] = identity[max_row], identity[i]

            # Make all rows below this one 0 in current column
            for k in range(i + 1, size):
                c = -matrix[k][i] / matrix[i][i]
                for j in range(i, size):
                    if i == j:
                        matrix[k][j] = 0
                    else:
                        matrix[k][j] += c * matrix[i][j]
                for j in range(size):
                    identity[k][j] += c * identity[i][j]

        # Solve equation matrix * inverse_matrix = identity
        for i in range(size - 1, -1, -1):
            for k in range(size):
                identity[i][k] /= matrix[i][i]
            for k in range(i):
                c = -matrix[k][i] / matrix[i][i]
                for j in range(size):
                    identity[k][j] += c * identity[i][j]

        return identity

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CifradoWindow(app)
    window.show()
    sys.exit(app.exec_())

