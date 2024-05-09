from PyQt5.QtWidgets import QMainWindow
class CifradoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cifrado")
        self.setFixedSize(640, 480)


        self.initUI()
