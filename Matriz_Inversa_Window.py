from PyQt5.QtWidgets import QMainWindow
class MatrizInversaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matriz Inversa")
        self.setFixedSize(640, 480)


        self.initUI()

