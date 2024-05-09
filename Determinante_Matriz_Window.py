from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QMessageBox

class DeterminanteMatrizWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Determinante Matriz")
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

        # Etiqueta y caja de entrada para el número de filas
        row_layout = QHBoxLayout()
        row_label = QLabel("Número de filas:")
        self.row_spinbox = QSpinBox()
        self.row_spinbox.setMinimum(1)
        row_layout.addWidget(row_label)
        row_layout.addWidget(self.row_spinbox)
        layout.addLayout(row_layout)

        # Etiqueta y caja de entrada para el número de columnas
        col_layout = QHBoxLayout()
        col_label = QLabel("Número de columnas:")
        self.col_spinbox = QSpinBox()
        self.col_spinbox.setMinimum(1)
        col_layout.addWidget(col_label)
        col_layout.addWidget(self.col_spinbox)
        layout.addLayout(col_layout)

        # Botón para generar la matriz y calcular el determinante
        self.generate_button = QPushButton("Generar Matriz y Calcular Determinante")
        self.generate_button.clicked.connect(self.generate_matrix_and_determinant)
        layout.addWidget(self.generate_button)

        # Etiqueta para mostrar el determinante
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

    def generate_matrix_and_determinant(self):
        rows = self.row_spinbox.value()
        cols = self.col_spinbox.value()

        # Verificar si es una matriz cuadrada
        if rows != cols:
            QMessageBox.warning(self, "Error", "La matriz debe ser cuadrada (número de filas igual al número de columnas)")
            return

        # Crear matriz a partir de las entradas del usuario
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                text, ok = QInputDialog.getText(self, f"Entrada ({i+1},{j+1})", f"Ingrese el elemento ({i+1},{j+1}):")
                if ok:
                    try:
                        value = float(text)
                        row.append(value)
                    except ValueError:
                        QMessageBox.warning(self, "Error", "Por favor, ingrese un número válido.")
                        return
            matrix.append(row)

        # Calcular el determinante de la matriz
        determinant = self.calculate_determinant(matrix)
        self.result_label.setText(f"Determinante de la matriz:\n{determinant}")

    def calculate_determinant(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        elif n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            det = 0
            for j in range(n):
                minor = [row[:j] + row[j+1:] for row in matrix[1:]]
                det += ((-1) ** j) * matrix[0][j] * self.calculate_determinant(minor)
            return det

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QInputDialog

    app = QApplication(sys.argv)
    window = DeterminanteMatrizWindow(app)
    window.show()
    sys.exit(app.exec_())
