import sys

from PyQt5.QtWidgets import *
from OpenGL.GL import *
from mywindow import *

def main():
    app = QApplication(sys.argv)
    gui = MyWindow()

    gui.resize(800, 600)
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()