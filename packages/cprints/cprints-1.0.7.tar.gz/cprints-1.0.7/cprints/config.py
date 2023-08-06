# coding: utf-8

class Color:

    # 字体颜色
    black   = {"code": (30, 40), "en": "black",   "zh": "黑色"}
    red     = {"code": (31, 41), "en": "red",     "zh": "红色"}
    green   = {"code": (32, 42), "en": "green",   "zh": "绿色"}
    yellow  = {"code": (33, 43), "en": "yellow",  "zh": "黄色"}
    blue    = {"code": (34, 44), "en": "blue",    "zh": "蓝色"}
    magenta = {"code": (35, 45), "en": "magenta", "zh": "洋红"}
    cyan    = {"code": (36, 46), "en": "cyan",    "zh": "青色"}
    white   = {"code": (37, 47), "en": "white",   "zh": "白色"}


class Style:

    # 字体样式
    highlight  = {"code": (1,), "en": "highlight",  "zh": "高亮"}
    underline  = {"code": (4,), "en": "underline",  "zh": "下划线"}
    flash      = {"code": (5,), "en": "flash",      "zh": "闪烁"}
    reverse    = {"code": (7,), "en": "reverse",    "zh": "反显"}
    no_visible = {"code": (8,), "en": "no_visible", "zh": "不可见"}
    default    = {"code": ("", ""), "en": "default", "zh": "默认"}

class ColorPrintData(Color, Style):

    def __init__(self):
        self._all = []
        for name in self.__dir__():
            if not name.startswith("_") \
                and isinstance(getattr(self, name), dict):
                self._all.append(getattr(self, name))

    def set_color_or_style(self, data):
        # type(data) -> int
        if isinstance(data, int):
            data = self.__set_type_int(data)
        # type(data) -> str
        elif isinstance(data, str):
            data = self.__set_type_str(data)
        # type(data) -> list, tuple
        elif isinstance(data, (list, tuple)):
            data = self.__set_type_iter(data)
        # type(data) -> dict
        elif isinstance(data, dict):
            data = self.__set_type_dict(data)
        # other
        else:
            data = self.default
        return data

    def __set_type_int(self, data):
        for item in self._all:
            if item["code"] is not None and data in item["code"]:
                data = item
                break
        else:
            data = self.default
        return data

    def __set_type_str(self, data):
        if data.isdigit():
            return self.__set_type_int(int(data))
        data = data.lower()
        for item in self._all:
            if data == item["en"] or data == item["zh"]:
                data = item
                break
        else:
            data = self.default
        return data

    def __set_type_iter(self, data):
        return tuple(self.set_color_or_style(item) for item in data)

    def __set_type_dict(self, data):
        for item in self._all:
            if data == item:
                break
        else:
            data = self.default
        return data
