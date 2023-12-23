import sys
from PySide6.QtCore import Slot,Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QDialog
from PySide6.QtGui import QPixmap, QImage, QIcon, QIntValidator, QDoubleValidator
from ui.Ui_login import Ui_LoginWindow
from ui.Ui_main import Ui_MainWindow
from ui.Ui_information import Ui_Information
from ui.Ui_confirm import Ui_Confirm
from modules.ui_style import UIStyle
from modules.util_function import CookieThread, LoginThread, UtilFunction, CodeThread


# 消息界面
class InformationDialog(QDialog):
    def __init__(self, title, info):
        super().__init__()
        # 初始化
        self.ui = Ui_Information()
        self.ui.setupUi(self)
        self.setWindowTitle(title)
        self.ui.label.setText(info)
        self.ui.pushButton.clicked.connect(self.accept)
        

# 确认界面
class ConfirmDialog(QDialog):
    def __init__(self, title, info):
        super().__init__()
        # 初始化
        self.ui = Ui_Confirm()
        self.ui.setupUi(self)
        self.setWindowTitle(title)
        self.ui.label.setText(info)
        self.ui.pushButton.clicked.connect(self.accept)
        self.ui.cancelButton.clicked.connect(self.reject)


# 主界面
class MainWindow(QMainWindow):
    buttonList = []
    settingOpen = False
    
    def __init__(self, loginWindow, account, upass, ticketCode, stuId):
        super().__init__()
        # 初始化
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loginWindow = loginWindow
        self.account = account
        self.upass = upass
        self.ticketCode = ticketCode
        
        # 设置默认界面
        self.ui.stackedWidget.setCurrentWidget(self.ui.reservePage)
        
        # 显示学号
        self.ui.topLabel.setText("你的学号：" + str(stuId))
        
        # 获取Cookie
        self.cookieThread = CookieThread(self.account, self.upass, self.ticketCode)
        self.cookieThread.signal.connect(self.handleCookie)
        self.cookieThread.start()
        
        # 关闭设置界面
        self.ui.extraFrame.setMaximumSize(0, 16777215)
        
        # 页面选择按钮
        self.buttonList.append(self.ui.reserveButton)
        self.buttonList.append(self.ui.mineButton)
        self.buttonList.append(self.ui.hintButton)
        for button in self.buttonList:
            button.clicked.connect(self.change_menu)
            
        # 退出按钮
        self.ui.logoutButton.clicked.connect(self.exit)
        # 设置按钮
        self.ui.settingButton.clicked.connect(self.switch_setting)
    
    
    # 用户变更
    def change_user(self, account, upass, ticketCode, stuId):
        self.account = account
        self.upass = upass
        self.ticketCode = ticketCode
        
        # 显示学号
        self.ui.topLabel.setText("你的学号：" + str(stuId))
        
        self.cookieThread.start()
        
    
    # 页面选择
    @Slot()
    def change_menu(self):
        btn = self.sender()
        btnName = btn.objectName()
        
        if btnName == "reserveButton":
            self.ui.mineButton.setStyleSheet("")
            self.ui.hintButton.setStyleSheet("")
            self.ui.reserveButton.setStyleSheet("background-color:#434458;")
            self.ui.stackedWidget.setCurrentWidget(self.ui.reservePage)
        elif btnName == "mineButton":
            self.ui.reserveButton.setStyleSheet("")
            self.ui.hintButton.setStyleSheet("")
            self.ui.mineButton.setStyleSheet("background-color:#434458;")
            self.ui.stackedWidget.setCurrentWidget(self.ui.minePage)
        elif btnName == "hintButton":
            self.ui.reserveButton.setStyleSheet("")
            self.ui.mineButton.setStyleSheet("")
            self.ui.hintButton.setStyleSheet("background-color:#434458;")
            self.ui.stackedWidget.setCurrentWidget(self.ui.hintPage)
    
    # 退出登录
    @Slot()
    def exit(self):
        replay = ConfirmDialog("操作确认","是否确认退出登录？").exec()
        if replay == QDialog.Accepted:
            self.loginWindow.show()
            self.loginWindow.refresh()
            self.close()
        
        # replay = QMessageBox.question(self, "退出登录", "是否确认退出登录？")
        # if replay == QMessageBox.StandardButton.Ok:
        #     self.loginWindow.show()
        #     self.loginWindow.refresh()
        #     self.close()
        
    
    # 切换设置界面
    @Slot()
    def switch_setting(self):
        if self.settingOpen:
            self.animation = QPropertyAnimation(self.ui.extraFrame, b"maximumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(240)
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
        else:
            self.animation = QPropertyAnimation(self.ui.extraFrame, b"maximumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(0)
            self.animation.setEndValue(240)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
        self.settingOpen = not self.settingOpen
    
    @Slot(str)
    def handleCookie(self, cookie):
        self.cookie = cookie
        print(cookie)


# 登陆界面
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
        
        # 密码模式设置
        self.ui.password.setEchoMode(QLineEdit.EchoMode.Password)
        
        # 仅允许输入数字
        self.ui.number.setValidator(QDoubleValidator())
        self.ui.password.setValidator(QIntValidator())
        self.ui.code.setValidator(QIntValidator())
        
        # 绑定事件
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.number.returnPressed.connect(self.login)
        self.ui.password.returnPressed.connect(self.login)
        self.ui.code.returnPressed.connect(self.login)
        
        def on_code_label_clicked(event):
            if event.button() == Qt.LeftButton:
                self.codeThread.start()
        
        # 重新获取验证码
        self.ui.codeLabel.setOpenExternalLinks(True)
        self.ui.codeLabel.mousePressEvent = lambda event: on_code_label_clicked(event)
        
        # 获取验证码
        self.codeThread = CodeThread()
        self.codeThread.signal.connect(self.handleCode)
        self.codeThread.start()
        
    # 刷新界面
    def refresh(self):
        self.codeThread.start()
        self.ui.number.setText("")
        self.ui.password.setText("")
        self.ui.code.setText("")
    
    # 登录
    @Slot()
    def login(self):
        flag = UtilFunction.verify(self.ui.number.text(), self.ui.password.text(), self.ui.code.text())
        if not flag:
            InformationDialog("提示","格式不正确！").exec()
            # QMessageBox.warning(self, "提示", "格式不正确！")
            return
        self.stuId = self.ui.number.text()
        self.loginThread = LoginThread(self.cookie, self.stuId, self.ui.password.text(), self.ui.code.text())
        self.loginThread.signal.connect(self.handleLogin)
        self.loginThread.start()
    
    # 处理验证码
    @Slot(str, bytes)
    def handleCode(self, cookie, img):
        if cookie == '':
            InformationDialog("提示","网络错误！").exec()
            # QMessageBox.warning(self, "提示", "网络错误！")
            self.codeThread.start()
            return
        self.cookie = cookie
        self.ui.codeLabel.setPixmap(QPixmap.fromImage(QImage.fromData(img)))
    
    # 处理登录
    @Slot(int,str,str,str)
    def handleLogin(self, type, account, upass, ticketCode):
        if type != 1:
            if type == 2:
                InformationDialog("提示","验证码错误！").exec()
                # QMessageBox.warning(self, "提示", "验证码错误！")
            elif type == 3:
                InformationDialog("提示","用户名或密码错误！").exec()
                # QMessageBox.warning(self, "提示", "用户名或密码错误！")
            self.refresh()
            return
        print("account:",account)
        print("upass",upass)
        print("ticketCode",ticketCode)
        print("登陆成功")
        if hasattr(self, "main_window"):
            self.main_window.change_user(account, upass, ticketCode, self.stuId)
        else:
            self.main_window = MainWindow(self, account, upass, ticketCode, self.stuId)
        self.main_window.show()
        self.close()


if __name__ == "__main__":
    sys.argv += ['-platform', 'windows:darkmode=2']
    app = QApplication(sys.argv)
    # app = QApplication([])
    app.setWindowIcon(QIcon("icon.ico"))
    window = LoginWindow()
    # window = MainWindow(window, "4521D610DC9460D22004EC76E32BF7E1", "6BED22231B81701E9F89F37B269CC290", "840c6e1e71b34f0e8140944e451b133f", "2020308250121")
    window.show()
    sys.exit(app.exec())