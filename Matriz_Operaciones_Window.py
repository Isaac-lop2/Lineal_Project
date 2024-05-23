from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QHBoxLayout, \
    QTableWidget, QMessageBox
from PyQt5.QtCore import Qt


class MatrizOperacionesWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.setWindowTitle("Operaciones Matriz")
        self.setFixedSize(640, 480)
        self.setStyleSheet('background-color: #07F7F3')
        self.app = app
        self.initUI()

    def initUI(self):
        widget = QWidget()
        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignVCenter)
        layoutH = QVBoxLayout()
        text = QLabel('Que opreracion desea hacer:')
        text.setAlignment(Qt.AlignCenter)
        layout_main.addWidget(text)
        button_plus = QPushButton('Suma')
        button_plus.setStyleSheet('background-color: pink')
        button_plus.clicked.connect(self.operation_plus)
        layoutH.addWidget(button_plus)
        button_minus = QPushButton('Resta')
        button_minus.clicked.connect(self.operation_manius)
        button_minus.setStyleSheet('background-color: pink')
        layoutH.addWidget(button_minus)
        button_multiplication = QPushButton('multiplicacion')
        button_multiplication.setStyleSheet('background-color: pink')
        button_multiplication.clicked.connect(self.operation_multiply)
        layoutH.addWidget(button_multiplication)
        button_close = QPushButton('Volver')
        button_close.setStyleSheet('background-color: pink')
        button_close.clicked.connect(self.close)
        layoutH.addWidget(button_close)
        layout_main.addLayout(layoutH)
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)
        widget.show()

# Operaciones de suma de matricez
    def operation_plus(self):
        self.window_plus = QMainWindow()
        self.window_plus.setWindowTitle('Suma de matrices')
        self.window_plus.setFixedSize(900, 600)
        self.window_plus.setStyleSheet('background-color: skyblue')
        widget = QWidget()
        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignVCenter)
        self.layout_rigth = QVBoxLayout()
        self.layout_left = QVBoxLayout()
        layout_H = QHBoxLayout()
        text = QLabel('Solo se pueden matrices cuadradas')
        text.setAlignment(Qt.AlignHCenter)
        layout_main.addWidget(text)
        line1_text = QLabel('Ingrese el numero de filas y columnas')
        line1_text.setAlignment(Qt.AlignCenter)
        line2_text = QLabel('Ingrese el numero de filas y columnas')
        line2_text.setAlignment(Qt.AlignHCenter)
        self.layout_left.addWidget(line1_text)
        self.layout_rigth.addWidget(line2_text)
        self.line1 = QLineEdit()
        self.line1.setAlignment(Qt.AlignCenter)
        self.line1.setStyleSheet('background-color: pink')
        self.line2 = QLineEdit()
        self.line2.setAlignment(Qt.AlignCenter)
        self.line2.setStyleSheet('background-color: pink')
        text1 = QPushButton('Definir la primera matriz')
        text1.clicked.connect(self.matrix_A_funcion_sum)
        text1.setStyleSheet('background-color: pink')
        self.layout_left.addWidget(self.line1)
        self.layout_left.addWidget(text1)
        text2 = QPushButton('Definier la segunda matriz')
        text2.clicked.connect(self.matrix_B_funcion_sum)
        text2.setStyleSheet('background-color: pink')
        self.layout_rigth.addWidget(self.line2)
        self.layout_rigth.addWidget(text2)
        confirm = QPushButton('Confirmar')
        confirm.setStyleSheet('background-color: pink')
        confirm.clicked.connect(self.confirm_sum)
        layout_H.addLayout(self.layout_left)
        layout_H.addLayout(self.layout_rigth)
        layout_main.addLayout(layout_H)
        layout_main.addWidget(confirm)
        widget.setLayout(layout_main)
        self.window_plus.setCentralWidget(widget)
        self.window_plus.show()

        while True:
            self.app.processEvents()

    def matrix_A_funcion_sum(self):
        self.tablaA = QTableWidget()
        self.tablaA.setColumnCount(int(self.line1.text()))
        self.tablaA.setRowCount(int(self.line1.text()))
        self.tablaA.setStyleSheet('background-color: white')
        self.setFixedSize(500, 300)


        layout = QVBoxLayout()
        layout.addWidget(self.tablaA)
        self.layout_left.addLayout(layout)

    def save_a_sum(self):
        self.vault = None
        self.matrix_a = []
        for fila in range(self.tablaA.rowCount()):
            fila_datos = []
            for columna in range(int(self.line1.text())):
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
            QMessageBox.warning(self.window_plus, 'Error de valor', 'Algun valor no es correcto')


    def matrix_B_funcion_sum(self):
        self.tablaB = QTableWidget()
        self.tablaB.setColumnCount(int(self.line2.text()))
        self.tablaB.setRowCount(int(self.line2.text()))
        self.tablaB.setStyleSheet('background-color: white')

        self.setFixedSize(500, 300)



        layout = QVBoxLayout()
        layout.addWidget(self.tablaB)
        self.layout_rigth.addLayout(layout)

    def save_b_sum(self):
        self.vault = None
        self.matrix_b = []
        for fila in range(self.tablaB.rowCount()):
            fila_datos = []
            for columna in range(int(self.line2.text())):
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
            QMessageBox.warning(self.window_plus, 'Error de valor', 'Algun valor no es correcto')

    def confirm_sum(self):
        self.save_a_sum()
        self.save_b_sum()
        if self.vault is None:
            pass

        else:
            self.operation_matrix_sum()

    def operation_matrix_sum(self):
        if int(len(self.matrix_a)) != int(len(self.matrix_b)) or int(len(self.matrix_a[0])) != int(len(self.matrix_b[0])):
            QMessageBox.warning(self.window_plus, 'Error', 'Las matrices no coinciden')

        else:
            result_row = []
            operation_row = []
            for i in range(len(self.matrix_a)):
                result_column = []
                operation_column = []
                for j in range(len(self.matrix_b[0])):
                    operation = f'{int(self.matrix_a[i][j])} + {int(self.matrix_b[i][j])}'
                    result = float(self.matrix_a[i][j]) + float(self.matrix_b[i][j])
                    operation_column.append(operation)
                    result_column.append(result)

                result_row.append(result_column)
                operation_row.append(operation_column)

            self.window_result_plus = QMainWindow()
            self.window_result_plus.setWindowTitle('Resultado')
            self.window_result_plus.setFixedSize(500, 250)
            self.window_result_plus.setStyleSheet('background-color: skyblue')
            widget = QWidget()
            layout_main = QVBoxLayout()
            layout_main.setAlignment(Qt.AlignCenter)
            layout_operation = QVBoxLayout()
            layout_operation.setAlignment(Qt.AlignCenter)
            text = QLabel('Resultado')
            layout_main.addWidget(text)
            layout_result = QVBoxLayout()
            layout_result.setAlignment(Qt.AlignCenter)
            for i in result_row:
                text = QLabel(f'{i}')
                text.setStyleSheet('background-color: pink')
                text.setAlignment(Qt.AlignCenter)
                layout_result.addWidget(text)
            layout_main.addLayout(layout_result)
            taxt2 = QLabel('Procedimiento')
            layout_main.addWidget(taxt2)
            for i in operation_row:
                text = QLabel(f'{i}')
                text.setStyleSheet('background-color: pink')
                layout_operation.addWidget(text)
            layout_main.addLayout(layout_operation)
            confirmar = QPushButton('Cerrar')
            confirmar.setStyleSheet('background-color: pink')
            confirmar.clicked.connect(self.close_all_sum)
            layout_main.addWidget(confirmar)
            widget.setLayout(layout_main)
            self.window_result_plus.setCentralWidget(widget)
            self.window_result_plus.show()

            while True:
                self.app.processEvents()
    def close_all_sum(self):
        self.window_result_plus.close()
        self.window_plus.close()

#opreracion de resta de matrices

    def operation_manius(self):
        self.window_manius = QMainWindow()
        self.window_manius.setWindowTitle('Resta de matrices')
        self.window_manius.setFixedSize(900, 600)
        self.window_manius.setStyleSheet('background-color: skyblue')
        widget = QWidget()
        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignVCenter)
        self.layout_rigth = QVBoxLayout()
        self.layout_left = QVBoxLayout()
        layout_H = QHBoxLayout()
        text = QLabel('Solo se pueden matrices cuadradas')
        text.setAlignment(Qt.AlignHCenter)
        layout_main.addWidget(text)
        line1_text = QLabel('Ingrese el numero de filas y columnas')
        line1_text.setAlignment(Qt.AlignCenter)
        line2_text = QLabel('Ingrese el numero de filas y columnas')
        line2_text.setAlignment(Qt.AlignHCenter)
        self.layout_left.addWidget(line1_text)
        self.layout_rigth.addWidget(line2_text)
        self.line1 = QLineEdit()
        self.line1.setAlignment(Qt.AlignCenter)
        self.line1.setStyleSheet('background-color: pink')
        self.line2 = QLineEdit()
        self.line2.setAlignment(Qt.AlignCenter)
        self.line2.setStyleSheet('background-color: pink')
        text1 = QPushButton('Definir la primera matriz')
        text1.clicked.connect(self.matrix_A_funcion_rest)
        text1.setStyleSheet('background-color: pink')
        self.layout_left.addWidget(self.line1)
        self.layout_left.addWidget(text1)
        text2 = QPushButton('Definier la segunda matriz')
        text2.clicked.connect(self.matrix_B_funcion_rest)
        text2.setStyleSheet('background-color: pink')
        self.layout_rigth.addWidget(self.line2)
        self.layout_rigth.addWidget(text2)
        confirm = QPushButton('Confirmar')
        confirm.setStyleSheet('background-color: pink')
        confirm.clicked.connect(self.confirm_rest)
        layout_H.addLayout(self.layout_left)
        layout_H.addLayout(self.layout_rigth)
        layout_main.addLayout(layout_H)
        layout_main.addWidget(confirm)
        widget.setLayout(layout_main)
        self.window_manius.setCentralWidget(widget)
        self.window_manius.show()

        while True:
            self.app.processEvents()

    def matrix_A_funcion_rest(self):
        self.tablaA = QTableWidget()
        self.tablaA.setColumnCount(int(self.line1.text()))
        self.tablaA.setRowCount(int(self.line1.text()))
        self.tablaA.setStyleSheet('background-color: white')
        self.setFixedSize(500, 300)


        layout = QVBoxLayout()
        layout.addWidget(self.tablaA)
        self.layout_left.addLayout(layout)

    def save_a_rest(self):
        self.vault = None
        self.matrix_a = []
        for fila in range(self.tablaA.rowCount()):
            fila_datos = []
            for columna in range(int(self.line1.text())):
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
            QMessageBox.warning(self.window_manius, 'Error de valor', 'Algun valor no es correcto')


    def matrix_B_funcion_rest(self):
        self.tablaB = QTableWidget()
        self.tablaB.setColumnCount(int(self.line2.text()))
        self.tablaB.setRowCount(int(self.line2.text()))
        self.tablaB.setStyleSheet('background-color: white')

        self.setFixedSize(500, 300)

        layout = QVBoxLayout()
        layout.addWidget(self.tablaB)
        self.layout_rigth.addLayout(layout)

    def save_b_rest(self):
        self.vault = None
        self.matrix_b = []
        for fila in range(self.tablaB.rowCount()):
            fila_datos = []
            for columna in range(int(self.line2.text())):
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
            QMessageBox.warning(self.window_manius, 'Error de valor', 'Algun valor no es correcto')

    def confirm_rest(self):
        self.save_a_rest()
        self.save_b_rest()
        if self.vault is None:
            pass

        else:
            self.operation_matrix_rest()


    def operation_matrix_rest(self):
        if int(len(self.matrix_a)) != int(len(self.matrix_b)) or int(len(self.matrix_a[0])) != int(len(self.matrix_b[0])):
            QMessageBox.warning(self.window_manius, 'Error', 'Las matrices no coinciden')

        else:
            result_row = []
            operation_row = []
            for i in range(len(self.matrix_a)):
                result_column = []
                operation_column = []
                for j in range(len(self.matrix_b[0])):
                    operation = f'{int(self.matrix_a[i][j])} - {int(self.matrix_b[i][j])}'
                    result = float(self.matrix_a[i][j]) - float(self.matrix_b[i][j])
                    operation_column.append(operation)
                    result_column.append(result)

                result_row.append(result_column)
                operation_row.append(operation_column)

            self.window_result_manius = QMainWindow()
            self.window_result_manius.setWindowTitle('Resultado')
            self.window_result_manius.setFixedSize(500, 250)
            self.window_result_manius.setStyleSheet('background-color: skyblue')
            widget = QWidget()
            layout_main = QVBoxLayout()
            layout_main.setAlignment(Qt.AlignCenter)
            layout_operation = QVBoxLayout()
            layout_operation.setAlignment(Qt.AlignCenter)
            text = QLabel('Resultado')
            layout_main.addWidget(text)
            layout_result = QVBoxLayout()
            layout_result.setAlignment(Qt.AlignCenter)
            for i in result_row:
                text = QLabel(f'{i}')
                text.setStyleSheet('background-color: pink')
                text.setAlignment(Qt.AlignCenter)
                layout_result.addWidget(text)
            layout_main.addLayout(layout_result)
            taxt2 = QLabel('Procedimiento')
            layout_main.addWidget(taxt2)
            for i in operation_row:
                text = QLabel(f'{i}')
                text.setStyleSheet('background-color: pink')
                layout_operation.addWidget(text)
            layout_main.addLayout(layout_operation)
            confirmar = QPushButton('Cerrar')
            confirmar.setStyleSheet('background-color: pink')
            confirmar.clicked.connect(self.close_all_rest)
            layout_main.addWidget(confirmar)
            widget.setLayout(layout_main)
            self.window_result_manius.setCentralWidget(widget)
            self.window_result_manius.show()

            while True:
                self.app.processEvents()
    def close_all_rest(self):
        self.window_result_manius.close()
        self.window_manius.close()

# operacion de multiplicacion de matrices

    def operation_multiply(self):
        self.window_multiply = QMainWindow()
        self.window_multiply.setWindowTitle('Resta de matrices')
        self.window_multiply.setFixedSize(900, 600)
        self.window_multiply.setStyleSheet('background-color: skyblue')
        widget = QWidget()
        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignVCenter)
        self.layout_rigth = QVBoxLayout()
        self.layout_left = QVBoxLayout()
        layout_H = QHBoxLayout()
        line1_text_row = QLabel('Ingrese el numero de filas')
        line1_text_row.setAlignment(Qt.AlignCenter)
        line1_text_column = QLabel('Ingrese el numero de columnas')
        line1_text_column.setAlignment(Qt.AlignCenter)
        line2_text_row = QLabel('Ingrese el numero de filas')
        line2_text_row.setAlignment(Qt.AlignHCenter)
        line2_text_column = QLabel('Ingrese el numero de columnas')
        line2_text_column.setAlignment(Qt.AlignCenter)
        self.layout_left.addWidget(line1_text_row)
        self.layout_rigth.addWidget(line2_text_row)
        self.line1_row = QLineEdit()
        self.line1_row.setAlignment(Qt.AlignCenter)
        self.line1_row.setStyleSheet('background-color: pink')
        self.line1_column = QLineEdit()
        self.line1_column.setAlignment(Qt.AlignCenter)
        self.line1_column.setStyleSheet('background-color: pink')
        self.line2_row = QLineEdit()
        self.line2_row.setAlignment(Qt.AlignCenter)
        self.line2_row.setStyleSheet('background-color: pink')
        self.line2_column = QLineEdit()
        self.line2_column.setAlignment(Qt.AlignCenter)
        self.line2_column.setStyleSheet('background-color: pink')
        text1 = QPushButton('Definir la primera matriz')
        text1.clicked.connect(self.matrix_A_funcion_mult)
        text1.setStyleSheet('background-color: pink')
        self.layout_left.addWidget(self.line1_row)
        self.layout_left.addWidget(line1_text_column)
        self.layout_left.addWidget(self.line1_column)
        self.layout_left.addWidget(text1)
        text2 = QPushButton('Definier la segunda matriz')
        text2.clicked.connect(self.matrix_B_funcion_mult)
        text2.setStyleSheet('background-color: pink')
        self.layout_rigth.addWidget(self.line2_row)
        self.layout_rigth.addWidget(line2_text_column)
        self.layout_rigth.addWidget(self.line2_column)
        self.layout_rigth.addWidget(text2)
        confirm = QPushButton('Confirmar')
        confirm.setStyleSheet('background-color: pink')
        confirm.clicked.connect(self.confirm_multi)
        layout_H.addLayout(self.layout_left)
        layout_H.addLayout(self.layout_rigth)
        layout_main.addLayout(layout_H)
        layout_main.addWidget(confirm)
        widget.setLayout(layout_main)
        self.window_multiply.setCentralWidget(widget)
        self.window_multiply.show()

        while True:
            self.app.processEvents()

    def matrix_A_funcion_mult(self):
        self.tablaA = QTableWidget()
        self.tablaA.setColumnCount(int(self.line1_column.text()))
        self.tablaA.setRowCount(int(self.line1_row.text()))
        self.tablaA.setStyleSheet('background-color: white')
        self.setFixedSize(500, 300)

        layout = QVBoxLayout()
        layout.addWidget(self.tablaA)
        self.layout_left.addLayout(layout)

    def save_a_mult(self):
        self.vault = None
        self.matrix_a = []
        for fila in range(self.tablaA.rowCount()):
            fila_datos = []
            for columna in range(int(self.line1_column.text())):
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
            QMessageBox.warning(self.window_multiply, 'Error de valor', 'Algun valor no es correcto')

    def matrix_B_funcion_mult(self):
        self.tablaB = QTableWidget()
        self.tablaB.setColumnCount(int(self.line2_column.text()))
        self.tablaB.setRowCount(int(self.line2_row.text()))
        self.tablaB.setStyleSheet('background-color: white')

        self.setFixedSize(500, 300)


        layout = QVBoxLayout()
        layout.addWidget(self.tablaB)
        self.layout_rigth.addLayout(layout)

    def save_b_mult(self):
        self.vault = None
        self.matrix_b = []
        for fila in range(self.tablaB.rowCount()):
            fila_datos = []
            for columna in range(int(self.line2_column.text())):
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
            QMessageBox.warning(self.window_multiply, 'Error de valor', 'Algun valor no es correcto')

    def confirm_multi(self):
        self.save_a_mult()
        self.save_b_mult()
        if self.vault is None:
            pass

        else:
            self.operation_matrix_mult()

    def operation_matrix_mult(self):
        if len(self.matrix_a[0]) != len(self.matrix_b):
            QMessageBox.warning(self.window_multiply, 'Error de matriz', 'No coinciden las matrices para la multiplicacion')

        else:
            result = []
            operation = []
            for i in range(len(self.matrix_a)):
                result.append([])
                operation.append([])
                for j in range(len(self.matrix_b[0])):
                    result[i].append(0)
                    operation[i].append('')

            for i in range(len(self.matrix_a)):
                for j in range(len(self.matrix_b[0])):
                    for k in range(len(self.matrix_a[0])):
                        if k == len(self.matrix_a[0]) - 1:
                            text = ''
                        else:
                            text = ' + '
                        operation[i][j] += f'{self.matrix_a[i][k]} * {self.matrix_b[k][j]}' + text
                        result[i][j] += float(self.matrix_a[i][k]) * float(self.matrix_b[k][j])

            self.window_result_mult = QMainWindow()
            self.window_result_mult.setWindowTitle('Resultado')
            self.window_result_mult.setFixedSize(500, 300)
            self.window_result_mult.setStyleSheet('background-color: skyblue')
            widget = QWidget()
            layout_main = QVBoxLayout()
            layout_main.setAlignment(Qt.AlignCenter)
            layout_operation = QVBoxLayout()
            layout_operation.setAlignment(Qt.AlignCenter)
            text = QLabel('Resultado')
            layout_main.addWidget(text)
            layout_result = QVBoxLayout()
            layout_result.setAlignment(Qt.AlignCenter)
            for i in result:
                text = QLabel(f'{i}')
                text.setStyleSheet('background-color: pink')
                text.setAlignment(Qt.AlignCenter)
                layout_result.addWidget(text)
            layout_main.addLayout(layout_result)
            taxt2 = QLabel('Procedimiento')
            layout_main.addWidget(taxt2)
            for i in operation:
                text = QLabel(f'{i}')
                text.setStyleSheet('background-color: pink')
                layout_operation.addWidget(text)
            layout_main.addLayout(layout_operation)
            confirmar = QPushButton('Cerrar')
            confirmar.setStyleSheet('background-color: pink')
            confirmar.clicked.connect(self.close_all_mult)
            layout_main.addWidget(confirmar)
            widget.setLayout(layout_main)
            self.window_result_mult.setCentralWidget(widget)
            self.window_result_mult.show()

            while True:
                self.app.processEvents()
    def close_all_mult(self):
        self.window_result_mult.close()
        self.window_multiply.close()
