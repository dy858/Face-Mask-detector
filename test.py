import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # 화면의 (x : 150, y: 50) 위치에서 (width : 1000, height : 500) 크기의 윈도우가 생성됩니다.
        self.setGeometry(150, 50, 1000, 500)
        # Window의 Title을 지정합니다.
        self.UI()

    def UI(self):
        # 이미지를 삽일 할 때에도 QLabel을 이용합니다.
        self.image = QLabel(self)
        # QLabel의 속성에 보면 setPixmap이 있는데 이 값을 통하여 이미지를 지정합니다.
        self.image.setPixmap(QPixmap("image.png"))
        self.image.move(50, 50)

        remove_button = QPushButton("remove", self)
        remove_button.move(380, 450)
        remove_button.clicked.connect(self.Remove)

        show_button = QPushButton("show", self)
        show_button.move(500, 450)
        show_button.clicked.connect(self.Show)

        self.checkbox = QCheckBox("체크박스", self)
        self.checkbox.move(100,450)




        # Window를 띄웁니다.
        self.show()

    def Remove(self):
        self.image.close()

    def Show(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()