import sys
from PySide6.QtCore import Slot,Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap, QImage, QIcon
from Ui_login import Ui_LoginWindow
from Ui_main import Ui_MainWindow
from modules.ui_style import UIStyle
from modules.util_function import LoginThread, UtilFunction, CodeThread

  
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 初始化
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 初始化
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        
        # 去除边框
        # self.setWindowFlags(Qt.FramelessWindowHint)
        
        # 添加阴影
        UIStyle.add_shadow(self.ui.Container)
        
        # 绑定事件
        self.ui.loginButton.clicked.connect(self.login)
        
        def on_code_abel_clicked(event):
            if event.button() == Qt.LeftButton:
                self.codeThread.start()
        
        self.ui.codeLabel.setOpenExternalLinks(True)
        self.ui.codeLabel.mousePressEvent = lambda event: on_code_abel_clicked(event)
        
        # 获取验证码
        self.codeThread = CodeThread()
        self.codeThread.signal.connect(self.handleCode)
        self.codeThread.start()
    
    # 登录
    @Slot()
    def login(self):
        flag = UtilFunction.verify(self.ui.number.text(), self.ui.password.text(), self.ui.code.text())
        if not flag:
            QMessageBox.warning(self, "提示", "格式不正确！")
            return
        self.loginThread = LoginThread(self.cookie, self.ui.number.text(), self.ui.password.text(), self.ui.code.text())
        self.loginThread.signal.connect(self.handleLogin)
        self.loginThread.start()
    
    # 处理验证码
    @Slot(str, bytes)
    def handleCode(self, cookie, img):
        if cookie == '':
            QMessageBox.warning(self, "提示", "网络错误！")
            self.codeThread.start()
            return
        self.cookie = cookie
        self.ui.codeLabel.setPixmap(QPixmap.fromImage(QImage.fromData(img)))
    
    # 处理登录
    @Slot(int,str,str,str)
    def handleLogin(self, type, account, upass, ticketCode):
        if type != 1:
            if type == 2:
                QMessageBox.warning(self, "提示", "验证码错误！")
            elif type == 3:
                QMessageBox.warning(self, "提示", "用户名或密码错误！")
            self.codeThread.start()
            self.ui.number.setText("")
            self.ui.password.setText("")
            self.ui.code.setText("")
            return
        print("account:",account)
        print("upass",upass)
        print("ticketCode",ticketCode)
        print("登陆成功")
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("icon.ico"))
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())