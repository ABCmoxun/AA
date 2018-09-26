
""" 这是一个用来测试用的包，此处是标题

此包有两个函数：
以下略...
"""

__all__ = ['games', 'menu']

def fx():
    print("我是mypack内的fx()函数")


name1 = "我是mypack内的name1变量"

import math  # 导入其它的包

print("mypack包被加载！", math.factorial(5))


