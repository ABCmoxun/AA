def f1():
    print("开始盖房子打地基...")
    raise ValueError("挖出文物")
    print("地基完工")

def f2():
    print("开始盖房子地面以上部分")
    raise ZeroDivisionError("要建高压线")
    print("房子完工")

def f3():
    """第二承包商打人干活"""
    f1()
    f2()

def build_house():
    f3()


try:
    build_house()
except ValueError as err:
    print("房子没盖成,因为", err)
except ZeroDivisionError as err:
    print("房子没盖成,因为", err)
else:
    print("房子盖好了")



