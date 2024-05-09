import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout



class MainWindow(QMainWindow):
    def __init__(self, app):

        super().__init__()
        self.stack_window = None
        self.queue_window = None
        self.single_list_window = None
        self.circular_list_window = None
        self.double_list_window = None
        self.double_circular_list_window = None
        self.binary_tree_window = None
        self.search_tree_window = None
        self.app = app

        self.setFixedSize(640, 480)
        self.setWindowTitle("")
        self.setWindowIcon(QIcon("icono.png"))

        # Creamos un widget central para la ventana principal
        widget_central = QWidget()
        widget_central.setStyleSheet("background-color: #E0EBFF")

        # Creamos un layout horizontal que contendrá a los dos verticales
        layout_horizontal_main = QHBoxLayout()
        layout_vertical_left = QVBoxLayout()
        layout_vertical_right = QVBoxLayout()
        # Creamos los botones correspondientes para cada estructura y ajustamos su tamaño.
        boton_1 = QPushButton("Pila")
        boton_1.setFixedSize(130, 40)
        boton_1.setStyleSheet("background-color: #bcbcbc")
        boton_2 = QPushButton("Cola")
        boton_2.setFixedSize(130, 40)
        boton_2.setStyleSheet("background-color: #bcbcbc")
        boton_3 = QPushButton("Lista simple")
        boton_3.setFixedSize(130, 40)
        boton_3.setStyleSheet("background-color: #bcbcbc")
        boton_4 = QPushButton("Lista circular")
        boton_4.setFixedSize(130, 40)
        boton_4.setStyleSheet("background-color: #bcbcbc")
        boton_5 = QPushButton("Lista doble")
        boton_5.setFixedSize(130, 40)
        boton_5.setStyleSheet("background-color: #bcbcbc")
        boton_6 = QPushButton("Lista circular doble")
        boton_6.setFixedSize(130, 40)
        boton_6.setStyleSheet("background-color: #bcbcbc")
        boton_7 = QPushButton("Árbol binario")
        boton_7.setFixedSize(130, 40)
        boton_7.setStyleSheet("background-color: #bcbcbc")
        boton_8 = QPushButton("Árbol de búsqueda")
        boton_8.setFixedSize(130, 40)
        boton_8.setStyleSheet("background-color: #bcbcbc")

        boton_9 = QPushButton("Cerrar")
        boton_9.setFixedSize(80, 30)
        boton_9.setStyleSheet("background-color: #bcbcbb")

        boton_10 = QPushButton("Guardar")
        boton_10.setFixedSize(80, 30)
        boton_10.setStyleSheet("background-color: #bcbcbb")

        # Creamos un layout horizontal auxiliar para centrar los botones.
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        layout_horizontal3 = QHBoxLayout()
        layout_horizontal4 = QHBoxLayout()
        layout_horizontal5 = QHBoxLayout()
        layout_horizontal6 = QHBoxLayout()
        layout_horizontal7 = QHBoxLayout()
        layout_horizontal8 = QHBoxLayout()
        layout_horizontal9 = QHBoxLayout()
        layout_horizontal10 = QHBoxLayout()

        # Añadimos los botones al layout horizontal.
        layout_horizontal1.addWidget(boton_1)
        layout_horizontal2.addWidget(boton_2)
        layout_horizontal3.addWidget(boton_3)
        layout_horizontal4.addWidget(boton_4)
        layout_horizontal5.addWidget(boton_5)
        layout_horizontal6.addWidget(boton_6)
        layout_horizontal7.addWidget(boton_7)
        layout_horizontal8.addWidget(boton_8)
        layout_horizontal9.addWidget(boton_9)
        layout_horizontal10.addWidget(boton_10)

        # **Centramos los botones horizontalmente.**
        layout_horizontal1.setAlignment(Qt.AlignHCenter)
        layout_horizontal2.setAlignment(Qt.AlignHCenter)
        layout_horizontal3.setAlignment(Qt.AlignHCenter)
        layout_horizontal4.setAlignment(Qt.AlignHCenter)
        layout_horizontal5.setAlignment(Qt.AlignHCenter)
        layout_horizontal6.setAlignment(Qt.AlignHCenter)
        layout_horizontal7.setAlignment(Qt.AlignHCenter)
        layout_horizontal8.setAlignment(Qt.AlignHCenter)
        layout_horizontal9.setAlignment(Qt.AlignRight)
        layout_horizontal10.setAlignment(Qt.AlignLeft)

        # Añadimos los layouts horizontales a los layouts verticales.
        layout_vertical_left.addLayout(layout_horizontal1)
        layout_vertical_left.addLayout(layout_horizontal2)
        layout_vertical_left.addLayout(layout_horizontal3)
        layout_vertical_left.addLayout(layout_horizontal4)
        layout_vertical_left.addLayout(layout_horizontal9)

        layout_vertical_right.addLayout(layout_horizontal5)
        layout_vertical_right.addLayout(layout_horizontal6)
        layout_vertical_right.addLayout(layout_horizontal7)
        layout_vertical_right.addLayout(layout_horizontal8)
        layout_vertical_right.addLayout(layout_horizontal10)

        # Establecemos el layout horizontal como el layout del widget central

        layout_horizontal_main.addLayout(layout_vertical_left)
        layout_horizontal_main.addLayout(layout_vertical_right)
        widget_central.setLayout(layout_horizontal_main)

        # Establecemos el widget central como el widget principal de la ventana
        self.setCentralWidget(widget_central)

        # Conectamos los botones a las funciones para abrir las otras ventanas
        boton_1.clicked.connect(self.show_stack_window)
        boton_2.clicked.connect(self.show_queue_window)
        boton_3.clicked.connect(self.show_single_list_window)
        boton_4.clicked.connect(self.show_circular_list_window)
        boton_5.clicked.connect(self.show_double_list_window)
        boton_6.clicked.connect(self.show_double_circular_list_window)
        boton_7.clicked.connect(self.show_binary_tree_window)
        boton_8.clicked.connect(self.show_search_tree_window)
        boton_9.clicked.connect(self.close_program)
        boton_10.clicked.connect(self.save_data)

    # Funciones para mostrar cada ventana
    def show_stack_window(self):
        self.stack_window = StackWindow()
        self.stack_window.show()
        while True:
            self.app.processEvents()

    def show_queue_window(self):
        self.queue_window = QueueWindow(self.app)
        self.queue_window.show()
        while True:
            self.app.processEvents()

    def show_single_list_window(self):
        self.single_list_window = SingleListWindow(self.app)
        self.single_list_window.show()
        while True:
            self.app.processEvents()

    def show_circular_list_window(self):
        self.circular_list_window = CircularListWindow()
        self.circular_list_window.show()
        while True:
            self.app.processEvents()

    def show_double_list_window(self):
        self.double_list_window = DoubleListWindow(self.app)
        self.double_list_window.show()
        while True:
            self.app.processEvents()

    def show_double_circular_list_window(self):
        self.double_circular_list_window = CircularDoubleListWindow()
        self.double_circular_list_window.show()
        while True:
            self.app.processEvents()

    def show_binary_tree_window(self):
        self.binary_tree_window = BinaryTreeWindow()
        self.binary_tree_window.show()
        while True:
            self.app.processEvents()

    def show_search_tree_window(self):
        self.search_tree_window = SearchTreeWindow()
        self.search_tree_window.show()
        while True:
            self.app.processEvents()

    def close_program(self):
        sys.exit(self.app.exec())

    def save_data(self):
        pass