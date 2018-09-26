

import mypack  # 导入 mypack包

# 想调用 menu.py 模块里的show_menu函数
import mypack.menu  # 导入　mypack包里的menu模块
mypack.menu.show_menu()  # 调用menu里的函数

# 导入子包 games 里的contra模块
import mypack.games.contra

mypack.games.contra.play()  # 调用contra模块的play
