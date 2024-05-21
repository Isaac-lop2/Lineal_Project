from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QApplication, QMessageBox


class OperacionVectores(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Operaciones con Vectores")
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

        # Etiquetas y cajas de entrada para el tamaño del vector
        vector_size_layout = QHBoxLayout()
        vector_size_label = QLabel("Tamaño del vector:")
        self.vector_size_input = QLineEdit()
        vector_size_layout.addWidget(vector_size_label)
        vector_size_layout.addWidget(self.vector_size_input)
        layout.addLayout(vector_size_layout)

        # Botón para generar las tablas de vectores
        self.generate_button = QPushButton("Generar Vectores")
        self.generate_button.clicked.connect(self.generate_vectors)
        layout.addWidget(self.generate_button)

        # Crear QTableWidget para los vectores
        self.vector1_table = QTableWidget()
        self.vector2_table = QTableWidget()
        layout.addWidget(QLabel("Vector 1"))
        layout.addWidget(self.vector1_table)
        layout.addWidget(QLabel("Vector 2"))
        layout.addWidget(self.vector2_table)

        # Botones para realizar operaciones
        self.sum_button = QPushButton("Sumar Vectores")
        self.sum_button.clicked.connect(self.sum_vectors)
        layout.addWidget(self.sum_button)

        self.dot_product_button = QPushButton("Producto Punto")
        self.dot_product_button.clicked.connect(self.dot_product_vectors)
        layout.addWidget(self.dot_product_button)

        # Etiqueta para mostrar resultados
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

    def generate_vectors(self):
        try:
            size = int(self.vector_size_input.text())
            if size <= 0:
                raise ValueError("El tamaño del vector debe ser mayor que cero.")

            # Configurar las tablas de vectores
            self.vector1_table.setRowCount(1)
            self.vector1_table.setColumnCount(size)
            self.vector2_table.setRowCount(1)
            self.vector2_table.setColumnCount(size)
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un tamaño válido para los vectores.")

    def sum_vectors(self):
        try:
            size = self.vector1_table.columnCount()
            vector1 = [float(self.vector1_table.item(0, i).text()) for i in range(size)]
            vector2 = [float(self.vector2_table.item(0, i).text()) for i in range(size)]

            result = [vector1[i] + vector2[i] for i in range(size)]
            self.result_label.setText("Suma de vectores: " + str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese componentes válidas para ambos vectores.")

    def dot_product_vectors(self):
        try:
            size = self.vector1_table.columnCount()
            vector1 = [float(self.vector1_table.item(0, i).text()) for i in range(size)]
            vector2 = [float(self.vector2_table.item(0, i).text()) for i in range(size)]

            result = sum(vector1[i] * vector2[i] for i in range(size))
            self.result_label.setText("Producto punto: " + str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese componentes válidas para ambos vectores.")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = OperacionVectores(app)
    window.show()
    sys.exit(app.exec_())
