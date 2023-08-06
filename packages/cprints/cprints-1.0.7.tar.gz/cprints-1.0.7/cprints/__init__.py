from .main  import ColorPrint
from .config import Color, Style


__all__ = ["ColorPrint", "Color", "Style"]

# 实例
cp = ColorPrint()

# 彩色打印
cprint        = cp.cprint
print_black   = cp.print_black
print_red     = cp.print_red
print_green   = cp.print_green
print_yellow  = cp.print_yellow
print_blue    = cp.print_blue
print_magenta = cp.print_magenta
print_cyan    = cp.print_cyan
print_white   = cp.print_white

# 着色文本
color         = cp.colored
color_black   = cp.colored_black
color_red     = cp.colored_red
color_green   = cp.colored_green
color_yellow  = cp.colored_yellow
color_blue    = cp.colored_blue
color_magenta = cp.colored_magenta
color_cyan    = cp.colored_cyan
color_white   = cp.colored_white

# 进度条
progress_bar    = cp.progress_bar
