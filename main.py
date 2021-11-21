from random import randint
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QApplication, QMainWindow
from design import Design


class MyWidget(QMainWindow, Design):
    def __init__(self):
        super().__init__(window=self)
        self.objects = list()
        self.button.clicked.connect(self.add)

    def add(self):
        self.objects.append(
            (randint(0, 350), randint(0, 250), randint(0, 100), (randint(0, 255), randint(0, 255), randint(0, 255))))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.objects:
            self.draw_figure(qp)
        qp.end()

    def draw_figure(self, qp):
        for obj in self.objects:
            qp.setBrush(QColor(*obj[3]))
            qp.drawEllipse(obj[0], obj[1], obj[2], obj[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
