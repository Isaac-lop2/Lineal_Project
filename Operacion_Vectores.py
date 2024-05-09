from PyQt5.QtWidgets import QMainWindow
class OperacionVectores(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operacion Vectores")
        self.setFixedSize(640, 480)


        self.initUI()

