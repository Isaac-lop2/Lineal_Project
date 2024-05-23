from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpinBox, QMessageBox, QTableWidget, QTableWidgetItem, QApplication, QTextEdit

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

        # Botón para generar la matriz
        self.generate_button = QPushButton("Generar Matriz")
        self.generate_button.clicked.connect(self.generate_matrix)
        layout.addWidget(self.generate_button)

        # Crear un QTableWidget para la matriz
        self.matrix_table = QTableWidget()
        layout.addWidget(self.matrix_table)

        # Botón para calcular la inversa
        self.calculate_button = QPushButton("Calcular Inversa")
        self.calculate_button.clicked.connect(self.calculate_inverse)
        layout.addWidget(self.calculate_button)

        # Etiqueta para mostrar la matriz inversa
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        # Área de texto para mostrar el proceso de cálculo
        self.process_text = QTextEdit()
        self.process_text.setReadOnly(True)
        layout.addWidget(self.process_text)

    def generate_matrix(self):
        rows = self.row_spinbox.value()
        cols = self.col_spinbox.value()

        # Verificar si es una matriz cuadrada
        if rows != cols:
            QMessageBox.warning(self, "Error", "La matriz debe ser cuadrada (número de filas igual al número de columnas)")
            return

        # Configurar el QTableWidget para la matriz
        self.matrix_table.setRowCount(rows)
        self.matrix_table.setColumnCount(cols)
        self.matrix_table.clear()

    def calculate_inverse(self):
        rows = self.row_spinbox.value()
        cols = self.col_spinbox.value()

        # Crear matriz a partir de las entradas del usuario
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                item = self.matrix_table.item(i, j)
                if item and item.text():
                    try:
                        value = float(item.text())
                        row.append(value)
                    except ValueError:
                        QMessageBox.warning(self, "Error", "Por favor, ingrese un número válido en todas las celdas.")
                        return
                else:
                    QMessageBox.warning(self, "Error", "Por favor, ingrese un número válido en todas las celdas.")
                    return
            matrix.append(row)

        # Calcular la inversa de la matriz y mostrar el proceso
        self.process_text.clear()
        inverse = self.calculate_inverse_recursive(matrix)

        if inverse is not None:
            inverse_str = "\n".join(["\t".join(map(str, row)) for row in inverse])
            self.result_label.setText(f"Matriz Inversa:\n{inverse_str}")
        else:
            QMessageBox.warning(self, "Error", "La matriz no es invertible.")

    def calculate_inverse_recursive(self, matrix):
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

            self.process_text.append(f"Intercambiar filas {i + 1} y {max_row + 1}")
            self.process_text.append(f"Matriz:\n{self.matrix_to_string(matrix)}")
            self.process_text.append(f"Identidad:\n{self.matrix_to_string(identity)}")

            # Normaliza la fila actual
            divisor = matrix[i][i]
            if divisor == 0:
                return None  # La matriz no es invertible
            for j in range(n):
                matrix[i][j] /= divisor
                identity[i][j] /= divisor

            self.process_text.append(f"Normalizar fila {i + 1} dividiendo por {divisor}")
            self.process_text.append(f"Matriz:\n{self.matrix_to_string(matrix)}")
            self.process_text.append(f"Identidad:\n{self.matrix_to_string(identity)}")

            # Elimina los otros elementos de la columna actual
            for k in range(n):
                if k != i:
                    factor = matrix[k][i]
                    for j in range(n):
                        matrix[k][j] -= factor * matrix[i][j]
                        identity[k][j] -= factor * identity[i][j]

                    self.process_text.append(f"Eliminar elemento en posición ({k + 1}, {i + 1}) multiplicando fila {i + 1} por {factor} y restando")
                    self.process_text.append(f"Matriz:\n{self.matrix_to_string(matrix)}")
                    self.process_text.append(f"Identidad:\n{self.matrix_to_string(identity)}")

        return identity

    def matrix_to_string(self, matrix):
        return "\n".join(["\t".join(map(str, row)) for row in matrix])


