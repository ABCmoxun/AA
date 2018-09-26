# 06_dict_keyword_argument.py


# 此示例示意关键字传参
def fx(a, b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


d = {'c': 33, 'b': 22, 'a': 11}

fx(**d)  # 拆解字典后再进行关键字传参
# fx(c=33, b=22, a=11)




