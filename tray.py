import ctypes
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

app = QApplication(sys.argv)

w = QWidget()
w.resize(400, 300)
w.setWindowTitle('Simple')
w.setWindowIcon(QIcon('face.png'))
qtRectangle = w.frameGeometry()
centerPoint = QDesktopWidget().availableGeometry().center()
qtRectangle.moveCenter(centerPoint)
w.move(qtRectangle.topLeft())


myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

w.show()

sys.exit(app.exec_())
