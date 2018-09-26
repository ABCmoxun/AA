# 11_dict_keyword_argument.py


# 此示例示意双星号字典形参的用法:
def func(**kwargs):
    print("关键字传参的个数是:", len(kwargs))
    print("kwargs=", kwargs)


func(name='tarena', age=15)
func(a=1, b="BBBB", c=[2, 3, 4], d=True)


