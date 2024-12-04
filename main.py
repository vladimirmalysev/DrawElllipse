import sys
from random import randint

from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Супрематизм')

        self.pushButton = QPushButton(self)
        self.pushButton.move(50, 50)
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        self.qp = QPainter(self)
        self.qp.begin(self)
        side = randint(20, 100)
        self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))

        self.qp.drawEllipse(QPointF(200, 200), side, side)

        self.qp.end()

    def run(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
