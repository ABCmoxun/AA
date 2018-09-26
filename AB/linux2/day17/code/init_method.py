# init_method.py


# 此示例示意初始化方法的定义方法和调用过程

class Car:
    """小汽车类"""
    def __init__(self, c, b, m):
        self.color = c  # 颜色
        self.brand = b  # 品牌
        self.model = m  # 型号
        self.wheel = 4
        print("__init__方法被调用")

    def run(self, speed):
        print(self.color, '的', self.brand,
              self.model, '正在以', speed,
              '公里/小时的速度行驶')

    def change_color(self, c):
        self.color = c

a4 = Car('红色', '奥迪', 'A4')
a4.run(199)
a4.change_color("白色")
a4.run(280)


x5 = Car('蓝色', '宝马', 'x5')
x5.run(188)

