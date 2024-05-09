from PyQt5.QtWidgets import QMainWindow
class MarkovWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markov")
        self.setFixedSize(640, 480)


        self.initUI()