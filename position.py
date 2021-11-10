import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QSettings, QPoint, QSize


class myApp(QWidget):
    def __init__(self):
        super(myApp, self).__init__()

        self.settings = QSettings('My company', 'myApp')
        print(QSettings.fileName(self.settings))
        # Initial window size/pos last saved. Use default values for first time
        self.resize(self.settings.value("size", QSize(270, 225)))
        self.move(self.settings.value("pos", QPoint(50, 50)))

    def closeEvent(self, e):
        # Write window size and position to config file
        self.settings.setValue("size", self.size())
        self.settings.setValue("pos", self.pos())

        e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    frame = myApp()
    frame.show()
    app.exec_()
