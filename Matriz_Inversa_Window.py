from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QMessageBox

class MatrizInversaWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Matriz Inversa")
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

        # Botón para generar la matriz y calcular la inversa
        self.generate_button = QPushButton("Generar Matriz e Invertir")
        self.generate_button.clicked.connect(self.generate_matrix_and_inverse)
        layout.addWidget(self.generate_button)

        # Etiqueta para mostrar la matriz inversa
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

    def generate_matrix_and_inverse(self):
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

        # Calcular la inversa de la matriz
        inverse = self.calculate_inverse(matrix)

        if inverse is not None:
            self.result_label.setText("Matriz Inversa:\n" + str(inverse))
        else:
            QMessageBox.warning(self, "Error", "La matriz no es invertible.")

    def calculate_inverse(self, matrix):
        # Calcula la matriz identidad del mismo tamaño que la matriz original
        n = len(matrix)
        identity = [[0] * n for _ in range(n)]
        for i in range(n):
            identity[i][i] = 1

        # Aplica el algoritmo de eliminación gaussiana
        for i in range(n):
            # Busca el máximo valor en la columna debajo de la fila actual
            max_row = i
            for k in range(i + 1, n):
                if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                    max_row = k

            # Intercambia la fila actual con la fila del máximo valor encontrado
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            identity[i], identity[max_row] = identity[max_row], identity[i]

            # Normaliza la fila actual
            divisor = matrix[i][i]
            if divisor == 0:
                return None  # La matriz no es invertible
            for j in range(i, n):
                matrix[i][j] /= divisor
                identity[i][j] /= divisor

            # Elimina los otros elementos de la columna actual
            for k in range(n):
                if k != i:
                    factor = matrix[k][i]
                    for j in range(i, n):
                        matrix[k][j] -= factor * matrix[i][j]
                        identity[k][j] -= factor * identity[i][j]

        return identity

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QInputDialog

    app = QApplication(sys.argv)
    window = MatrizInversaWindow(app)
    window.show()
    sys.exit(app.exec_())
