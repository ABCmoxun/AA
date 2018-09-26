# 01_lambda.py

# 1. 写一个lambda表达式, 判断这个数的2次方+1 能否被5整数，如果能整除返回True, 否则返回False

#    fx = lambda n: .......
#    print(fx(4))  # False
#    print(fx(3))  # True

fx = lambda n: (n ** 2 + 1) % 5 == 0

print(fx(4))  # False
print(fx(3))  # True
