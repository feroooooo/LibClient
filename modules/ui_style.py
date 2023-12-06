from PySide6.QtWidgets import QGraphicsDropShadowEffect

class UIStyle():
    def add_shadow(self):
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(40)
        self.shadow.setColor("#080808")
        self.shadow.setOffset(0, 4)
        self.setGraphicsEffect(self.shadow)