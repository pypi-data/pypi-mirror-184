import math
from .config import ColorPrintData

PREFIX = "\033["
SUFFIX = "\033[0m"

class ColorPrint(ColorPrintData):

    def color(self, text, /, *args, fg=None, bg=None, style=None, suffix=True):
        """
        :params text   : 着色文本
        :params args   : print可变位置参数
        :params fg     : 前景色(black, red, green, yellow, blue, magenta, cyan, white)
        :params bg     : 背景色(black, red, green, yellow, blue, magenta, cyan, white)
        :params style  : 文本样式(default, highlight, underline, flash, reverse)
        :params suffix : 恢复默认打印方式

        explain:

        from cprints import cp
        text = cp.color("Hello World", fg=cp.red, bg=cp.black, style=cp.underline)
        print(text)
        """
        fg = self.set_color_or_style(fg)
        bg = self.set_color_or_style(bg)
        style  = self.set_color_or_style(style)
        # 字体颜色
        if isinstance(fg, tuple):
            fg = fg[0]
        fg = str(fg["code"][0])
        # 背景颜色
        if isinstance(bg, tuple):
            bg = bg[0]
        bg = str(bg["code"][1])
        # 字体样式
        if not isinstance(style, tuple):
            style = (style, )
        style = ";".join(set([str(item["code"][0]) for item in style]))
        # 拼接
        data  = ";".join([item for item in (style, fg, bg) if item])
        if not data:
            data = str(0)
        suffix = SUFFIX if bool(suffix) else ""
        args   = " ".join([str(i) for i in args])
        if args:
            args = " " + args
        return f"{PREFIX}{data}m{text}{args}{suffix}"

    colored = color


    def cprint(self, text, /, *args, fg=None, bg=None, style=None, suffix=True, **kwargs):
        """
        :params text   : 着色文本
        :params args   : print可变位置参数
        :params fg     : 前景色(black, red, green, yellow, blue, magenta, cyan, white)
        :params bg     : 背景色(black, red, green, yellow, blue, magenta, cyan, white)
        :params style  : 文本样式(default, highlight, underline, flash, reverse)
        :params suffix : 恢复默认打印方式
        :params kwargs : print内置函数可变关键字参数

        explain:

        from cprints import cp
        cp.cprint("Hello World", fg=cp.red, bg=cp.black, style=cp.underline)
        """
        text = self.color(text, *args, fg=fg, bg=bg, style=style, suffix=suffix)
        print(text, **kwargs)


    def progress_bar(self, now: int, total: int, lenght=36, bar=b"\xe2\x94\x81", pad=""):
        """
        :params now    : 当前进度值
        :params total  : 总进度值
        :params lenght : 进度条长度
        :params bar    : 进度条 进度填充
        :params pad    : 进度条 其余填充

        explain:

        from cprints import cp
        maximum = 100
        for i in range(1, maximum+1):
            cp.progress_bar(now=i, total=maximum)
        """
        now = total if now >= total else now
        bar = bar.decode() if isinstance(bar, bytes) else str(bar)
        # 百分比
        percent = now / total
        # 进度条总长度
        total_bar  = len(self.color(lenght * bar))
        foreground = self.red if now < total else self.green
        # 进度条
        progress_bar = self.color(
            math.floor(percent * lenght) * bar, fg=foreground)
        # 需要打印的百分比
        percent = self.color(f"{percent:.2%}", fg=self.magenta)
        _num    = self.color(f"{now}/{total}", fg=self.yellow)
        end     = "\n" if now >= total else ""
        print(f"\r{percent: >16} {progress_bar:{pad}<{total_bar}} {_num} ", end=end, flush=True)


    def color_black(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.color(text, *args, fg=self.black, bg=bg, style=style, suffix=suffix)

    colored_black = color_black

    def color_red(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.color(text, *args, fg=self.red, bg=bg, style=style, suffix=suffix)

    colored_red = color_red

    def color_green(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.color(text, *args, fg=self.green, bg=bg, style=style, suffix=suffix)

    colored_green = color_green

    def color_yellow(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.color(text, *args, fg=self.yellow, bg=bg, style=style, suffix=suffix)

    colored_yellow = color_yellow

    def color_blue(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.color(text, *args, fg=self.blue, bg=bg, style=style, suffix=suffix)

    colored_blue = color_blue

    def color_magenta(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.color(text, *args, fg=self.magenta, bg=bg, style=style, suffix=suffix)

    colored_magenta = color_magenta

    def color_cyan(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.color(text, *args, fg=self.cyan, bg=bg, style=style, suffix=suffix)

    colored_cyan = color_cyan

    def color_white(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.color(text, *args, fg=self.white, bg=bg, style=style, suffix=suffix)

    colored_white = color_white

    def print_black(self, text ,/, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.black, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_red(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.red, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_green(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.green, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_yellow(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.yellow, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_blue(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.blue, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_magenta(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.magenta, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_cyan(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.cyan, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_white(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.white, bg=bg, style=style, suffix=suffix, **kwargs)
