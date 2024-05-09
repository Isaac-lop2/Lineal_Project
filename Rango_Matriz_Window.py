from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
class RangoMatrizWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.setWindowTitle("Rango Matriz")
        self.setFixedSize(640, 480)
        self.app = app

        self.initUI()

    def initUI(self):
        # Widget central
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #E0EBFF")

        self.setCentralWidget(central_widget)
        # Diseño vertical para los widgets
        layout = QVBoxLayout()

