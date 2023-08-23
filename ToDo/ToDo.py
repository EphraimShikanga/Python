from ui import Ui_MainWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.MainWindow.show()
    sys.exit(app.exec_())
