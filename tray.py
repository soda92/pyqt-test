import ctypes
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtCore import QSettings
from pathlib import Path

CURR = Path(__file__).resolve().parent


class myApp(QWidget):
    def __init__(self):
        super(myApp, self).__init__()
        self.resize(400, 300)
        self.settings = QSettings('My company', 'myApp')
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(self.settings.value("pos", qtRectangle.topLeft()))
        self.setWindowTitle('示例程序')
        self.setWindowIcon(QIcon(str(Path.joinpath(CURR, 'icon.png'))))

    def closeEvent(self, e):
        # Write window size and position to config file
        self.settings.setValue("size", self.size())
        self.settings.setValue("pos", self.pos())

        e.accept()


if __name__ == '__main__':
    myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)
    frame = myApp()
    frame.show()
    sys.exit(app.exec_())
