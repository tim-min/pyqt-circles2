from PyQt5.QtWidgets import QPushButton


class Design:
    def __init__(self, window):
        window.setObjectName("Circles2")
        window.resize(400, 300)
        self.button = QPushButton("Circle!", self)
        self.button.move(150, 260)
        self.button.resize(100, 25)
