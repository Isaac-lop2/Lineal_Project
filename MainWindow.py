import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from Rango_Matriz_Window import RangoMatrizWindow
from Operacion_Vectores import  OperacionVectores
from Matriz_Operaciones_Window import MatrizOperacionesWindow
from Matriz_Inversa_Window import MatrizInversaWindow
from Markov_Window import MarkovWindow
from Determinante_Matriz_Window import DeterminanteMatrizWindow
from Cifrado_Window import CifradoWindow
class MainWindow(QMainWindow):
    def __init__(self, app):

        super().__init__()
        self.Rango_Matriz_Window = None
        self.Operacion_Vectores = None
        self.Matriz_Operaciones_Window = None
        self.Matriz_Inversa_Window = None
        self.Markov_Window = None
        self.Determinante_Matriz_Windoww = None
        self.Cifrado_Window = None
        self.app = app

        self.setFixedSize(640, 480)
        self.setWindowTitle("")

        # Creamos un widget central para la ventana principal
        widget_central = QWidget()
        widget_central.setStyleSheet("background-color: #E0EBFF")

        # Creamos un layout horizontal que contendrá a los dos verticales
        layout_horizontal_main = QHBoxLayout()
        layout_vertical_left = QVBoxLayout()
        layout_vertical_right = QVBoxLayout()
        # Creamos los botones correspondientes para cada estructura y ajustamos su tamaño.
        boton_1 = QPushButton("Operacion Matrices")
        boton_1.setFixedSize(130, 40)
        boton_1.setStyleSheet("background-color: #bcbcbc")
        boton_2 = QPushButton("Matriz Inversa")
        boton_2.setFixedSize(130, 40)
        boton_2.setStyleSheet("background-color: #bcbcbc")
        boton_3 = QPushButton("Rango Matriz")
        boton_3.setFixedSize(130, 40)
        boton_3.setStyleSheet("background-color: #bcbcbc")
        boton_4 = QPushButton("Determinante Matriz")
        boton_4.setFixedSize(130, 40)
        boton_4.setStyleSheet("background-color: #bcbcbc")
        boton_5 = QPushButton("Cifrado")
        boton_5.setFixedSize(130, 40)
        boton_5.setStyleSheet("background-color: #bcbcbc")
        boton_6 = QPushButton("Markov")
        boton_6.setFixedSize(130, 40)
        boton_6.setStyleSheet("background-color: #bcbcbc")
        boton_7 = QPushButton("Operacion Vectores")
        boton_7.setFixedSize(130, 40)
        boton_7.setStyleSheet("background-color: #bcbcbc")
        boton_8 = QPushButton("Cerrar")
        boton_8.setFixedSize(80, 30)
        boton_8.setStyleSheet("background-color: #bcbcbb")


        # Creamos un layout horizontal auxiliar para centrar los botones.
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        layout_horizontal3 = QHBoxLayout()
        layout_horizontal4 = QHBoxLayout()
        layout_horizontal5 = QHBoxLayout()
        layout_horizontal6 = QHBoxLayout()
        layout_horizontal7 = QHBoxLayout()
        layout_horizontal8 = QHBoxLayout()

        # Añadimos los botones al layout horizontal.
        layout_horizontal1.addWidget(boton_1)
        layout_horizontal2.addWidget(boton_2)
        layout_horizontal3.addWidget(boton_3)
        layout_horizontal4.addWidget(boton_4)
        layout_horizontal5.addWidget(boton_5)
        layout_horizontal6.addWidget(boton_6)
        layout_horizontal7.addWidget(boton_7)
        layout_horizontal8.addWidget(boton_8)


        # **Centramos los botones horizontalmente.**
        layout_horizontal1.setAlignment(Qt.AlignHCenter)
        layout_horizontal2.setAlignment(Qt.AlignHCenter)
        layout_horizontal3.setAlignment(Qt.AlignHCenter)
        layout_horizontal4.setAlignment(Qt.AlignHCenter)
        layout_horizontal5.setAlignment(Qt.AlignHCenter)
        layout_horizontal6.setAlignment(Qt.AlignHCenter)
        layout_horizontal7.setAlignment(Qt.AlignHCenter)
        layout_horizontal8.setAlignment(Qt.AlignHCenter)


        # Añadimos los layouts horizontales a los layouts verticales.
        layout_vertical_left.addLayout(layout_horizontal1)
        layout_vertical_left.addLayout(layout_horizontal2)
        layout_vertical_left.addLayout(layout_horizontal3)
        layout_vertical_left.addLayout(layout_horizontal4)


        layout_vertical_right.addLayout(layout_horizontal5)
        layout_vertical_right.addLayout(layout_horizontal6)
        layout_vertical_right.addLayout(layout_horizontal7)
        layout_vertical_right.addLayout(layout_horizontal8)


        # Establecemos el layout horizontal como el layout del widget central

        layout_horizontal_main.addLayout(layout_vertical_left)
        layout_horizontal_main.addLayout(layout_vertical_right)
        widget_central.setLayout(layout_horizontal_main)

        # Establecemos el widget central como el widget principal de la ventana
        self.setCentralWidget(widget_central)

        # Conectamos los botones a las funciones para abrir las otras ventanas
        boton_1.clicked.connect(self.show_Rango_Matriz_Window)
        boton_2.clicked.connect(self.show_Operacion_Vectores)
        boton_3.clicked.connect(self.show_Matriz_Operaciones_Window)
        boton_4.clicked.connect(self.show_Matriz_Inversa_Window)
        boton_5.clicked.connect(self.show_Markov_Window)
        boton_6.clicked.connect(self.show_Determinante_Matriz_Window)
        boton_7.clicked.connect(self.show_Cifrado_Window)


    # Funciones para mostrar cada ventana
    def show_Rango_Matriz_Window(self):
        self.Rango_Matriz_Window = RangoMatrizWindow(self.app)
        self.Rango_Matriz_Window.show()
        while True:
            self.app.processEvents()

    def show_Operacion_Vectores(self):
        self.Operacion_Vectores = OperacionVectores(self.app)
        self.Operacion_Vectores.show()
        while True:
            self.app.processEvents()

    def show_Matriz_Operaciones_Window(self):
        self.Matriz_Operaciones_Window = MatrizOperacionesWindow(self.app)
        self.Matriz_Operaciones_Window.show()
        while True:
            self.app.processEvents()

    def show_Matriz_Inversa_Window(self):
        self.Matriz_Inversa_Window = MatrizInversaWindow()
        self.Matriz_Inversa_Window.show()
        while True:
            self.app.processEvents()

    def show_Markov_Window(self):
        self.Markov_Window = MarkovWindow(self.app)
        self.Markov_Window.show()
        while True:
            self.app.processEvents()

    def show_Determinante_Matriz_Window(self):
        self.Determinante_Matriz_Window = DeterminanteMatrizWindow()
        self.Determinante_Matriz_Window.show()
        while True:
            self.app.processEvents()

    def show_Cifrado_Window(self):
        self.Cifrado_Window = CifradoWindow()
        self.Cifrado_Window.show()
        while True:
            self.app.processEvents()


    def close_program(self):
        sys.exit(self.app.exec())

