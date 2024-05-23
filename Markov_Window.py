from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QHBoxLayout, \
    QTableWidget, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt

class MarkovWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.setWindowTitle("Markov")
        self.setFixedSize(640, 480)
        self.app = app

        self.initUI()

    def initUI(self):
        self.window_markov = QMainWindow()
        self.window_markov.setWindowTitle('multiplicacion de matrices')
        self.window_markov.setFixedSize(800, 400)
        self.window_markov.setStyleSheet('background-color: skyblue')
        widget = QWidget()
        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignAbsolute)
        self.layout_rigth = QVBoxLayout()
        self.layout_left = QVBoxLayout()
        layout_H = QHBoxLayout()
        text = QLabel('ingrese la cantidad de ciclos')
        layout_main.addWidget(text)
        self.cicle = QLineEdit()
        self.cicle.setStyleSheet('background-color: pink')
        layout_main.addWidget(self.cicle)

        line1_text = QLabel('Ingrese los datos')
        self.tablaA = QTableWidget()
        self.tablaA.setColumnCount(3)
        self.tablaA.setRowCount(3)
        self.tablaA.setStyleSheet('background-color: white')
        self.tablaA.setFixedSize(400, 150)
        layout = QVBoxLayout()
        layout.addWidget(line1_text)
        layout.addWidget(self.tablaA)
        self.layout_left.addLayout(layout)

        line2_text = QLabel('Ingrese las probabilidades')
        self.tablaB = QTableWidget()
        self.tablaB.setColumnCount(1)
        self.tablaB.setRowCount(3)
        self.tablaB.setStyleSheet('background-color: white')
        self.tablaB.setFixedSize(150, 150)

        layout = QVBoxLayout()
        layout.addWidget(line2_text)
        layout.addWidget(self.tablaB)
        self.layout_rigth.addLayout(layout)

        confirm = QPushButton('Confirmar')
        confirm.setStyleSheet('background-color: pink')
        confirm.clicked.connect(self.confirm)
        layout_H.addLayout(self.layout_left)
        layout_H.addLayout(self.layout_rigth)
        layout_main.addLayout(layout_H)
        layout_main.addWidget(confirm)
        widget.setLayout(layout_main)
        self.window_markov.setCentralWidget(widget)
        self.window_markov.show()

        while True:
            self.app.processEvents()

    def save_a(self):
        self.vault = None
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

        Error = 0
        for i in self.matrix_a:
            for j in i:
                try:
                    if int(j):
                        pass

                except ValueError:
                    Error += 1

        if Error == 0:
            self.vault = 1

        else:
            QMessageBox.warning(self.window_markov, 'Error de valor', 'Algun valor no es correcto')

    def save_b(self):
        self.vault = None
        self.matrix_b = []
        for fila in range(self.tablaB.rowCount()):
            fila_datos = []
            for columna in range(int(self.tablaB.columnCount())):
                item = self.tablaB.item(fila, columna)
                if item is not None:
                    texto = item.text()
                    fila_datos.append(texto)
                else:
                    fila_datos.append('')
            self.matrix_b.append(fila_datos)
        Error = 0
        for i in self.matrix_b:
            for j in i:
                try:
                    if int(j):
                        pass

                except ValueError:
                    Error += 1

        if Error == 0:
            self.vault = 1

        else:
            QMessageBox.warning(self.window_markov, 'Error de valor', 'Algun valor no es correcto')

    def confirm(self):
        self.save_a()
        self.save_b()
        if self.vault is None:
            pass

        else:
            self.operation_matrix_markov()

    def matriz_transpuesta(self):
        filas_original = int(len(self.matrix_a))
        columnas_original = int(len(self.matrix_a[0]))

        self.transpuesta = []
        for i in range(len(self.matrix_a)):
            self.transpuesta.append([])
            for j in range(len(self.matrix_a[0])):
                self.transpuesta[i].append(0)

        for i in range(filas_original):
            for j in range(columnas_original):
                self.transpuesta[j][i] = self.matrix_a[i][j]

    def operation_matrix_markov(self):
        self.matriz_transpuesta()
        if len(self.transpuesta[0]) != len(self.matrix_b):
            QMessageBox.warning(self.window_multiply, 'Error de matriz', 'No coinciden las matrices para la multiplicacion')

        else:
            operation = []
            ciclos = self.matrix_b
            for _ in range(int(self.cicle.text())):
                result = []
                product = []
                for i in range(len(self.transpuesta)):
                    result.append([])
                    product.append([])
                    for j in range(len(self.matrix_b[0])):
                        result[i].append(0)
                        product[i].append('')

                for i in range(len(self.transpuesta)):
                    for j in range(len(ciclos[0])):
                        for k in range(len(self.transpuesta[0])):
                            if k == len(self.transpuesta) - 1:
                                text = ''
                            else:
                                text = ' + '
                            product[i][j] += f'{self.matrix_a[i][k]} * {self.matrix_b[k][j]}' + text
                            result[i][j] += float(self.transpuesta[i][k]) * float(ciclos[k][j])

                ciclos = result
                operation.append(product)


            self.window_result = QMainWindow()
            self.window_result.setWindowTitle('Resultado')
            self.window_result.setStyleSheet('background-color: skyblue')
            widget = QWidget()
            layout_main = QVBoxLayout()
            layout_main.setAlignment(Qt.AlignCenter)
            layout_operation = QGridLayout()
            layout_operation.setAlignment(Qt.AlignCenter)
            text = QLabel('Resultado')
            layout_main.addWidget(text)
            layout_result = QVBoxLayout()
            layout_result.setAlignment(Qt.AlignCenter)
            for i in ciclos:
                text = QLabel(f'{i}')
                text.setStyleSheet('background-color: pink')
                text.setAlignment(Qt.AlignCenter)
                layout_result.addWidget(text)
            layout_main.addLayout(layout_result)
            taxt2 = QLabel('Procedimiento')
            layout_main.addWidget(taxt2)
            contador = 1
            for i in operation:
                text = QLabel(f'Ciclo {contador}: \n {i}')
                text.setStyleSheet('background-color: pink')
                layout_operation.addWidget(text)
                contador += 1
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
        self.window_markov.close()
