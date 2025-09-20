import json
import os
from typing import Optional, Tuple


class ConfigManager:
    def __init__(self, config_path: str = None):
        cfg_exist: bool = os.path.exists(config_path)
        if cfg_exist == False:
            raise Exception("Конфигурационный файл не найден!")
        else:
            self.config_path = config_path

    def get_size(self) -> Optional[Tuple[int, int]]:
        """
        Возвращает (width, height) из конфига.
        Если ошибка — возвращает None.
        """
        with open(self.config_path, "r", encoding="utf-8") as cfg:
            app_size = json.load(cfg)["app"]
            return int(app_size.get("width")), int(app_size.get("height"))
