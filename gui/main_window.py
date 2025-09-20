from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from utils.config_manager import ConfigManager


class VPetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = ConfigManager("./config/vpet.json")
        self.initUI()

    def initUI(self):
        size = self.config.get_size()
        if size is None:
            width, height = 200, 300  # * дефолтные значения
        else:
            width, height = size

        self.setWindowTitle("VPet - Linux")
        self.setFixedSize(QSize(width, height))
        self.main_text = QLabel("тут аниме животное")
        self.setCentralWidget(self.main_text)

    def mousePressEvent(self, event):
        """Переопределяем обработчик нажатия мыши для основного окна"""
        if event.button() == Qt.MouseButton.RightButton:
            self.on_right_click(event)
        elif event.button() == Qt.MouseButton.LeftButton:
            self.on_left_click(event)
        super().mousePressEvent(event)

    def on_right_click(self, event):
        """
        Открываем панель инструментов
        """
        print("ПКМ")

    def on_left_click(self, event):
        """Обработка ЛКМ"""
        print("ЛКМ")
