# ebicycle.py

# 4. 练习：
#   写一个Bicycle(自行车)类,有run(骑行)方法，调用时显示骑行里程km
#   class Bycycle:
#       def run(self, km):
#           print("自行车骑行了", km, "公里")
#  再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性，同时属有两个方法：
#    1. fill_charge(vol)  用来充电，vol 为电量(度)
#    2. run(km) 方法用于骑行,每骑行10km消耗电量1度,当电量消耗尽时调用Bicycle的run方法骑行
#    并显示骑行结果
#   主程序：
#     b = EBicycle(5)  # 创建一个电动自行车,默认电量5度
#     b.run(10)   # 骑行10km
#     b.run(100)  # 骑行100km
#     b.fill_charge(6)  # 充电6度
#     b.run(70)   # 又骑行70km


class Bicycle:

    def run(self, km):
        print("自行车骑行了", km, "公里")


class EBicycle(Bicycle):

    def __init__(self, vol):
        self.volume = vol

    def fill_charge(self, vol):
        self.volume += vol

    def run(self, km):
        e_km = min(km, self.volume * 10)
        self.volume -= e_km / 10  # 电量消耗
        if e_km > 0:
            print("电动自行车骑行了", e_km, "公里")
        if km > e_km:  # 判断没电后行驶的过程
            super().run(km - e_km)

#     2. run(km) 方法用于骑行, 每骑行10km消耗电量1度, 当电量消耗尽时调用Bicycle的run方法骑行
#     并显示骑行结果
# 主程序：
b = EBicycle(5)  # 创建一个电动自行车,默认电量5度
b.run(10)   # 骑行10km
b.run(100)   # 骑行100km
b.fill_charge(6)  # 充电6度
b.run(70)   # 又骑行70km
