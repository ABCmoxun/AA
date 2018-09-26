# 练习:
#   1. 输入一段字符串，打印所有输入过的字符串，
#     但重复的只打印一次，(不要求打印的顺序与输入顺序一致)
#     输入: abcdabcaba
#     打印:
#       a b c d

s = input("请输入: ")
# 方法1 用集合实现
# char_set = set(s)  # 去掉重复的
# for c in char_set:
#     print(c, end=' ')
# else:
#     print()

# 方法2 用列表实现
L = []
for c in s:
    if c not in L:
        L.append(c)

print(L)
