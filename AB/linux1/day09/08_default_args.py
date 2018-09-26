# 08_default_args.py


# 此示例来示意fn函数中lst绑定的缺省参数的列表的生命周期
def fn(a, lst=[]):  # <<--- 重要
    lst.append(a)
    print(lst)


# L = [1, 2, 3, 4]
# fn(5, L)  # [ 1,2,3,4,5]
# fn(6, L)  # [1,2,3,4,5,6]

fn(1.1)  # [1.1]
fn(2.2)  # [1.1, 2.2]
