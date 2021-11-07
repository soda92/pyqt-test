import ctypes
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from pathlib import Path
CURR = Path(__file__).resolve().parent
print(CURR)
import os
print(os.listdir(CURR))
app = QApplication(sys.argv)

w = QWidget()
w.resize(400, 300)
w.setWindowTitle('Simple')
w.setWindowIcon(QIcon(str(Path.joinpath(CURR,'icon.png'))))
qtRectangle = w.frameGeometry()
centerPoint = QDesktopWidget().availableGeometry().center()
qtRectangle.moveCenter(centerPoint)
w.move(qtRectangle.topLeft())


myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

w.show()

sys.exit(app.exec_())
