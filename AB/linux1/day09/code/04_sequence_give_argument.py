# sequence_give_argument.py


# 此示例示意序列传参

def fx(a, b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


s1 = [11, 22, 33]
# 用索引传参
# fx(s1[0], s1[1], s1[2])
# 序列传参
fx(*s1)  # * 代表要将s1 拆解后再依次传入
fx(*"ABC")
fx(*(101, 202, 303))

# fx(*"ABCD")  # 有错,序列中有四个元素,但形参是3个