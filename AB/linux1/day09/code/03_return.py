# 03_return.py

# 此示例示意return语句的用法

def hello():
    print("hello aaa")
    print("hello bbb")
    return [2, 3, 5, 7]  # 用于返回到调用的地方
    print("hello ccc")


v = hello()
print('v绑定', v)
