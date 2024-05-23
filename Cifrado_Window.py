from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem,
    QApplication, QMessageBox, QTextEdit
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
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #E0EBFF")
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Ingrese el mensaje a cifrar")
        layout.addWidget(self.message_input)

        self.generate_matrix_button = QPushButton("Generar Matriz Clave")
        self.generate_matrix_button.clicked.connect(self.generate_matrix)
        layout.addWidget(self.generate_matrix_button)

        self.matrix_table = QTableWidget()
        layout.addWidget(self.matrix_table)

        self.encrypt_button = QPushButton("Cifrar Mensaje")
        self.encrypt_button.clicked.connect(self.encrypt_message)
        layout.addWidget(self.encrypt_button)

        self.encrypted_numbers = QTextEdit()
        self.encrypted_numbers.setPlaceholderText("Números cifrados")
        layout.addWidget(self.encrypted_numbers)

        self.encrypted_input = QLineEdit()
        self.encrypted_input.setPlaceholderText("Ingrese los números cifrados para descifrar")
        layout.addWidget(self.encrypted_input)

        self.decrypt_button = QPushButton("Descifrar Mensaje")
        self.decrypt_button.clicked.connect(self.decrypt_message)
        layout.addWidget(self.decrypt_button)

        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 14))
        layout.addWidget(self.result_label)

        self.process_text = QTextEdit()
        self.process_text.setReadOnly(True)
        layout.addWidget(self.process_text)

    def generate_matrix(self):
        size = 3  # For simplicity, using a fixed size of 3x3
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
        message = self.message_input.text().upper().replace(' ', '')
        if not message:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un mensaje para cifrar.")
            return

        matrix = self.get_matrix()
        if matrix is None:
            return

        vector = [ord(char) - 64 for char in message]

        while len(vector) % 3 != 0:
            vector.append(0)

        self.process_text.clear()
        self.process_text.append("Mensaje original: " + message)
        self.process_text.append("Vector numérico del mensaje: " + str(vector))

        blocks = [vector[i:i + 3] for i in range(0, len(vector), 3)]
        encrypted_vector = []

        for block in blocks:
            encrypted_block = self.matrix_vector_mult(matrix, block)
            encrypted_vector.extend(encrypted_block)

        encrypted_message = ' '.join(map(str, encrypted_vector))
        self.process_text.append("Matriz clave:\n" + '\n'.join(map(str, matrix)))
        self.process_text.append("Vector cifrado: " + encrypted_message)

        self.result_label.setText(f"Mensaje Cifrado: {encrypted_message}")
        self.encrypted_numbers.setText(encrypted_message)

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
            self.process_text.clear()
            self.process_text.append("Números cifrados: " + str(encrypted_vector))

            inverse_matrix = self.invert_matrix(matrix)
            self.process_text.append("Matriz clave invertida:\n" + '\n'.join(map(str, inverse_matrix)))

            blocks = [encrypted_vector[i:i + 3] for i in range(0, len(encrypted_vector), 3)]
            decrypted_vector = []

            for block in blocks:
                decrypted_block = self.matrix_vector_mult(inverse_matrix, block)
                decrypted_vector.extend(decrypted_block)

            decrypted_message = ''.join(chr(int(round(num)) + 64) for num in decrypted_vector).rstrip('@')
            self.process_text.append("Vector descifrado: " + str(decrypted_vector))
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
            max_el = abs(matrix[i][i])
            max_row = i
            for k in range(i + 1, size):
                if abs(matrix[k][i]) > max_el:
                    max_el = abs(matrix[k][i])
                    max_row = k

            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            identity[i], identity[max_row] = identity[max_row], identity[i]

            for k in range(i + 1, size):
                c = -matrix[k][i] / matrix[i][i]
                for j in range(i, size):
                    if i == j:
                        matrix[k][j] = 0
                    else:
                        matrix[k][j] += c * matrix[i][j]
                for j in range(size):
                    identity[k][j] += c * identity[i][j]

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
