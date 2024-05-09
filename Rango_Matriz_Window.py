
from PyQt5.QtWidgets import QMainWindow
class RangoMatrizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rango Matriz")
        self.setFixedSize(640, 480)


        self.initUI()
