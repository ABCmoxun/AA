# 练习：
#   1. 有字符串列表如下:
#       L = ["tarena", 'xiaozhang', 'hello']
#     用推导式生成如下字典:
#       d = {"tarena":6, 'xiaozhang':9, 'hello':5}
#     注: 字典的值为键的长度

L = ["tarena", 'xiaozhang', 'hello']
d = {x: len(x) for x in L}
print(d)

