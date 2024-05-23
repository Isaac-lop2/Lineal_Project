from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QApplication, QMessageBox, QTextEdit


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

        # Botón para generar las tablas de vectores
        self.generate_button = QPushButton("Generar Vectores (Tamaño 2)")
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

        # Área de texto para mostrar el procedimiento
        self.process_text = QTextEdit()
        self.process_text.setReadOnly(True)
        layout.addWidget(self.process_text)

        # Etiqueta para mostrar resultados
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        # Generar vectores de tamaño 2 por defecto
        self.generate_vectors()

    def generate_vectors(self):
        size = 2

        # Configurar las tablas de vectores
        self.vector1_table.setRowCount(1)
        self.vector1_table.setColumnCount(size)
        self.vector2_table.setRowCount(1)
        self.vector2_table.setColumnCount(size)

        # Inicializar la matriz con entradas vacías
        for i in range(size):
            self.vector1_table.setItem(0, i, QTableWidgetItem(""))
            self.vector2_table.setItem(0, i, QTableWidgetItem(""))

    def sum_vectors(self):
        try:
            size = self.vector1_table.columnCount()
            vector1 = [float(self.vector1_table.item(0, i).text()) for i in range(size)]
            vector2 = [float(self.vector2_table.item(0, i).text()) for i in range(size)]

            result = [vector1[i] + vector2[i] for i in range(size)]

            # Mostrar el procedimiento paso a paso
            self.process_text.clear()
            self.process_text.append(f"Vector 1: {vector1}")
            self.process_text.append(f"Vector 2: {vector2}")
            self.process_text.append("Procedimiento de suma:")
            for i in range(size):
                self.process_text.append(f"Componente {i + 1}: {vector1[i]} + {vector2[i]} = {result[i]}")

            self.result_label.setText("Suma de vectores: " + str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese componentes válidas para ambos vectores.")

    def dot_product_vectors(self):
        try:
            size = self.vector1_table.columnCount()
            vector1 = [float(self.vector1_table.item(0, i).text()) for i in range(size)]
            vector2 = [float(self.vector2_table.item(0, i).text()) for i in range(size)]

            result = sum(vector1[i] * vector2[i] for i in range(size))

            # Mostrar el procedimiento paso a paso
            self.process_text.clear()
            self.process_text.append(f"Vector 1: {vector1}")
            self.process_text.append(f"Vector 2: {vector2}")
            self.process_text.append("Procedimiento de producto punto:")
            for i in range(size):
                self.process_text.append(f"Componente {i + 1}: {vector1[i]} * {vector2[i]} = {vector1[i] * vector2[i]}")
            self.process_text.append(f"Suma total: {result}")

            self.result_label.setText("Producto punto: " + str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese componentes válidas para ambos vectores.")

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QApplication, QMessageBox, QTextEdit


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

        # Botón para generar las tablas de vectores
        self.generate_button = QPushButton("Generar Vectores (Tamaño 2)")
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

        # Área de texto para mostrar el procedimiento
        self.process_text = QTextEdit()
        self.process_text.setReadOnly(True)
        layout.addWidget(self.process_text)

        # Etiqueta para mostrar resultados
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        # Generar vectores de tamaño 2 por defecto
        self.generate_vectors()

    def generate_vectors(self):
        size = 2

        # Configurar las tablas de vectores
        self.vector1_table.setRowCount(1)
        self.vector1_table.setColumnCount(size)
        self.vector2_table.setRowCount(1)
        self.vector2_table.setColumnCount(size)

        # Inicializar la matriz con entradas vacías
        for i in range(size):
            self.vector1_table.setItem(0, i, QTableWidgetItem(""))
            self.vector2_table.setItem(0, i, QTableWidgetItem(""))

    def sum_vectors(self):
        try:
            size = self.vector1_table.columnCount()
            vector1 = [float(self.vector1_table.item(0, i).text()) for i in range(size)]
            vector2 = [float(self.vector2_table.item(0, i).text()) for i in range(size)]

            result = [vector1[i] + vector2[i] for i in range(size)]

            # Mostrar el procedimiento paso a paso
            self.process_text.clear()
            self.process_text.append(f"Vector 1: {vector1}")
            self.process_text.append(f"Vector 2: {vector2}")
            self.process_text.append("Procedimiento de suma:")
            for i in range(size):
                self.process_text.append(f"Componente {i + 1}: {vector1[i]} + {vector2[i]} = {result[i]}")

            self.result_label.setText("Suma de vectores: " + str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese componentes válidas para ambos vectores.")

    def dot_product_vectors(self):
        try:
            size = self.vector1_table.columnCount()
            vector1 = [float(self.vector1_table.item(0, i).text()) for i in range(size)]
            vector2 = [float(self.vector2_table.item(0, i).text()) for i in range(size)]

            result = sum(vector1[i] * vector2[i] for i in range(size))

            # Mostrar el procedimiento paso a paso
            self.process_text.clear()
            self.process_text.append(f"Vector 1: {vector1}")
            self.process_text.append(f"Vector 2: {vector2}")
            self.process_text.append("Procedimiento de producto punto:")
            for i in range(size):
                self.process_text.append(f"Componente {i + 1}: {vector1[i]} * {vector2[i]} = {vector1[i] * vector2[i]}")
            self.process_text.append(f"Suma total: {result}")

            self.result_label.setText("Producto punto: " + str(result))
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese componentes válidas para ambos vectores.")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = OperacionVectores(app)
    window.show()
    sys.exit(app.exec_())
