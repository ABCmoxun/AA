# 3. 写一个函数minmax, 可以给出任意个数字实参,返回这些实参的最小数和最大数,
#   要求两个数字形成元组后返回(最小数在前,最大数在后)
#   调用此函数,能得到实参的最小值和最大值
#   def minmax(...):
#       ....

#   xiao, da = minmax(5,7,9,3,1)
#   print("最小数是:", xiao)
#   print("最大数是:", da)


def minmax(*args):
    return (min(args), max(args))

xiao, da = minmax(5, 7, 9, 3, 1)
print("最小数是:", xiao)
print("最大数是:", da)
