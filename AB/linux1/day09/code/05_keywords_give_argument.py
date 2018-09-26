# keywords_give_argument.py


# 此示例示意关键字传参
def fx(a, b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


fx(b=22, c=33, a=11)  # 11->a, 22->b, 33->c


fx(b=22, c=33, b=55)  # 错的
