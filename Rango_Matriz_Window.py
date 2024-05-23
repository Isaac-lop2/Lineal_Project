from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, \
    QTableWidget, QMessageBox
from PyQt5.QtCore import Qt
import numpy as np
class RangoMatrizWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Rango Matriz")
        self.setFixedSize(640, 480)
        self.app = app

        self.initUI()

    def initUI(self):
        self.window_range = QMainWindow()
        self.window_range.setWindowTitle('Rango de una matriz')
        self.window_range.setFixedSize(800, 400)
        self.window_range.setStyleSheet('background-color: skyblue')
        widget = QWidget()
        self.layout_main = QVBoxLayout()
        self.layout_main.setAlignment(Qt.AlignVCenter)
        self.layout = QVBoxLayout()
        text = QLabel('ingrese la cantidad de filas')
        self.layout_main.addWidget(text)
        self.row = QLineEdit()
        self.row.setStyleSheet('background-color: pink')
        self.layout_main.addWidget(self.row)
        text2 = QLabel('ingrese la cantidad de columnas')
        self.layout_main.addWidget(text2)
        self.columns = QLineEdit()
        self.columns.setStyleSheet('background-color: pink')
        self.layout_main.addWidget(self.columns)
        button = QPushButton('Generar la matriz')
        button.clicked.connect(self.create_matrix)
        button.setStyleSheet('background-color: pink')
        self.layout_main.addWidget(button)
        self.layout_main.addLayout(self.layout)
        widget.setLayout(self.layout_main)
        self.window_range.setCentralWidget(widget)
        self.window_range.show()

        while True:
            self.app.processEvents()

    def create_matrix(self):
        line1_text = QLabel('Ingrese los datos')
        line1_text.setAlignment(Qt.AlignCenter)
        self.tablaA = QTableWidget()
        self.tablaA.setColumnCount(int(self.columns.text()))
        self.tablaA.setRowCount(int(self.row.text()))
        self.tablaA.setStyleSheet('background-color: white')
        self.tablaA.setFixedSize(400, 150)
        button = QPushButton('Confirmar')
        button.setStyleSheet('background-color: pink')
        button.clicked.connect(self.operation_matrix_range)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.addWidget(line1_text)
        layout.addWidget(self.tablaA)
        layout.addWidget(button)
        self.layout.addLayout(layout)


    def save_a(self):
        try:
            self.matrix_a = []
            for fila in range(self.tablaA.rowCount()):
                fila_datos = []
                for columna in range(self.tablaA.columnCount()):
                    item = self.tablaA.item(fila, columna)
                    if item is not None:
                        texto = item.text()
                        fila_datos.append(texto)
                    else:
                        fila_datos.append('')
                self.matrix_a.append(fila_datos)

            QMessageBox.information(self.window_range, 'Datos Ingresados',
                                    'Los valores se han ingresado correctamente')

        except Exception as e:
            QMessageBox.critical(self.window_range, 'Error', f'Ocurrió un error al guardar los datos: {e}')

    def rango_eliminacion_gaussiana(self, matriz):
        matriz = np.array(matriz, dtype=float)

        filas, columnas = matriz.shape

        for i in range(min(filas, columnas)):
            max_fila = i + np.argmax(abs(matriz[i:, i]))
            if matriz[max_fila, i] == 0:
                continue

            matriz[[i, max_fila]] = matriz[[max_fila, i]]

            matriz[i] = matriz[i] / matriz[i, i]

            for j in range(i + 1, filas):
                matriz[j] = matriz[j] - matriz[i] * matriz[j, i]

        rango = 0
        for fila in matriz:
            if not np.allclose(fila, 0):
                rango += 1

        return rango

    def operation_matrix_range(self):
        self.save_a()
        self.window_result = QMainWindow()
        self.window_result.setWindowTitle('Resultado')
        self.window_result.setStyleSheet('background-color: skyblue')
        widget = QWidget()
        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignCenter)
        layout_operation = QVBoxLayout()
        layout_operation.setAlignment(Qt.AlignCenter)
        text = QLabel('Resultado')
        layout_main.addWidget(text)
        layout_result = QVBoxLayout()
        layout_result.setAlignment(Qt.AlignCenter)
        result = self.rango_eliminacion_gaussiana(self.matrix_a)
        label = QLabel(f'{result}')
        label.setAlignment(Qt.AlignCenter)
        layout_main.addWidget(label)
        layout_main.addLayout(layout_result)
        taxt2 = QLabel('Procedimiento')
        layout_main.addWidget(taxt2)
        layout_main.addLayout(layout_operation)
        confirmar = QPushButton('Cerrar')
        confirmar.setStyleSheet('background-color: pink')
        confirmar.clicked.connect(self.close_all_mult)
        layout_main.addWidget(confirmar)
        widget.setLayout(layout_main)
        self.window_result.setCentralWidget(widget)
        self.window_result.show()

        while True:
            self.app.processEvents()

    def close_all_mult(self):
        self.window_result.close()
        self.window_range.close()