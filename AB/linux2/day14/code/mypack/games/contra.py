

# 此为相对导入,当前所在位置为mypack.games.contra
from ..menu import show_menu
# 以下导入是错的, 已超出包的范围
# from ...mypack.menu import show_menu

def play():
    print("正在玩魂斗罗")

def gameover():
    print("游戏结束!!!")
    # 调有menu模块内的show_menu
    show_menu()

print("魂斗罗模块被加载!")