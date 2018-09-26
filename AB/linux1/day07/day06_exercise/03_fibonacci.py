# 3. 计算 20 个百斐波那契数( fabonacci 数)
#   存于列表中，最后打印这20个数
#   1, 1, 2, 3, 5, 8, 13, ...
#     (从第三个数起，后一个数是前两个数之和)

# 方法1
L = []
a = 1
b = 1
L.append(a)
L.append(b)
# c 变量 代表下一个值  c = a + b
while len(L) < 20:
    c = a + b  # 计算下一个值
    L.append(c)
    a = b  # 让a绑定的对象向后移动一个
    b = c  # 让b绑定的对象向后移动一个
print(L)


# 方法2
L = []
a = 1
b = 1
L.append(a)
L.append(b)
# c 变量 代表下一个值  c = a + b
while len(L) < 20:
    L.append(a + b)
    a, b = b, a + b
print(L)

# 方法3
L = [1, 1]
while len(L) < 20:
    L.append(L[-1] + L[-2])

print(L)

