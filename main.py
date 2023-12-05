from PySide6.QtWidgets import QApplication, QMainWindow
from Ui_login import Ui_Form

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])

    window = LoginWindow()
    window.show()

    app.exec()