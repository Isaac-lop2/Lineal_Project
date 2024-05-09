from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt5.QtCore import Qt


class MatrizOperacionesWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.setWindowTitle("Operaciones Matriz")
        self.setFixedSize(640, 480)
        self.app = app

        self.initUI()

    def initUI(self):
        widget = QWidget()
        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignVCenter)
        layoutH = QVBoxLayout()
        text = QLabel('Que opreracion desea hacer:')
        text.setAlignment(Qt.AlignVCenter)
        layout_main.addWidget(text)
        button_plus = QPushButton('Suma')
        button_plus.setStyleSheet('background-color: pink')
        button_plus.clicked.connect(self.operation_plus)
        layoutH.addWidget(button_plus)
        button_minus = QPushButton('menos')
        button_minus.setStyleSheet('background-color: pink')
        layoutH.addWidget(button_minus)
        button_multiplication = QPushButton('multiplicacion')
        button_multiplication.setStyleSheet('background-color: pink')
        layoutH.addWidget(button_multiplication)
        button_product = QPushButton('Producto punto')
        button_product.setStyleSheet('background-color: pink')
        layoutH.addWidget(button_product)
        button_close = QPushButton('Volver')
        button_close.setStyleSheet('background-color: pink')
        button_close.clicked.connect(self.close())
        layoutH.addWidget(button_close)
        layout_main.addLayout(layoutH)
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)
        widget.show()

    def operation_plus(self):
        self.window_plus = QMainWindow()
        self.vault_window.setVisible(False)
        self.vault_window = self.window_plus
        self.window_plus.setWindowTitle('Operaciones de matrices')
        self.window_plus.setFixedSize(800, 400)
        self.window_plus.setStyleSheet('background-color: skyblue')
        widget = QWidget()
        layout_main = QVBoxLayout()
        layout_main.setAlignment(Qt.AlignVCenter)
        text = QLabel('Solo se pueden matrices cuadradas')
        text.setAlignment(Qt.AlignVCenter)
        layout_main.addWidget(text)
        row_and_columns = QLineEdit()
        layout_main.addWidget(row_and_columns)
        widget.setLayout(layout_main)
        self.window_plus.setCentralWidget(widget)
        self.window_plus.show()


        while True:
            self.app.processEvents()