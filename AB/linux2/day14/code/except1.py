def f1():
    print("开始盖房子打地基...")
    return -1  # -1 代表挖出文物
    print("地基完工")
    return 0

def f2():
    print("开始盖房子地面以上部分")
    return -2  # -2 代表要建高压线
    print("房子完工")

def f3():
    """第二承包商打人干活"""
    r = f1()
    if r < 0:
        return r
    else:
        r2 = f2()
        return r2

def build_house():
    r = f3()
    if r < 0:
        return r
    return 0


r = build_house()
if r == 0:
    print("房子盖好了")
elif r == -1:
    print("房子没盖成,因为文物问题")
elif r == -2:
    print("房子没盖成,因为高压线问题")



