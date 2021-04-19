import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(900, 500)


        self.pixmap = QPixmap('image.png')
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)  # 이미지 세팅
        self.label.setContentsMargins(10, 10, 10, 10)



        remove_button = QPushButton("remove", self)
        remove_button.move(380, 450)
        remove_button.clicked.connect(self.Remove)

        show_button = QPushButton("show", self)
        show_button.move(500, 450)
        show_button.clicked.connect(self.Show)

        self.checkbox = QCheckBox("체크박스", self)
        self.checkbox.move(100, 450)

        self.show()

    def Remove(self):
        self.image.close()

    def Show(self):
        self.image.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
