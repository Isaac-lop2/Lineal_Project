from PyQt5.QtWidgets import QMainWindow
class DeterminanteMatrizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Determinante Matriz")
        self.setFixedSize(640, 480)


        self.initUI()