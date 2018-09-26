# 练习：
#   1. 输入三行文字，让这三行文字依次以20个字符的宽度右对齐输出.
#   如:
#     请输入第1行: hello world
#     请输入第2行: abcd
#     请输入第3行: a
#   打印结果:
#            hello world
#                   abcd
#                      a
#   做完上面的题再思考：
#     能否以最长字符串的长度进行右对齐显示,左侧填充空格

line1 = input("请输入第1行: ")
line2 = input("请输入第2行: ")
line3 = input("请输入第3行: ")

print("%20s" % line1)
print("%20s" % line2)
print("%20s" % line3)

ml = max(len(line1), len(line2), len(line3))
# 方法1：
# print("最长的字符串是:", ml)
# print(' ' * (ml - len(line1)) + line1)
# print(' ' * (ml - len(line2)) + line2)
# print(' ' * (ml - len(line3)) + line3)

# 方法2
# fmt = "%" + str(ml) + 's'  # '%11d'
fmt = "%%%ds" % ml
print("格式化字符串是:", fmt)
print(fmt % line1)
print(fmt % line2)
print(fmt % line3)




