from PyQt5.QtWidgets import QMainWindow
class MatrizOperacionesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operaciones Matriz")
        self.setFixedSize(640, 480)


        self.initUI()
