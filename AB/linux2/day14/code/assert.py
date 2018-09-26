# assert.py


def get_age():
    a = input("请输入年龄：")
    a = int(a)
    assert a < 140, "年龄不可能大于140!!!"
    assert a >= 0, "年龄不可能出现负数!!!"
    return a


try:
    age = get_age()
except AssertionError as err:
    print("发生了断言错误！错误对象是:", err)
    age = 0  # 　做相应的处理
print("您输入的年龄是: ", age)
