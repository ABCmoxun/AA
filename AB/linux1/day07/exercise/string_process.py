# 练习：
#   任意输入一个字符串,将此字符串中的空格全部去掉，生成返转后的字符串:
#   如:
#     输入: abc def g<回车>
#   打印输出: gfedcba
#     (提示:可以用反向切片或reversed进行反转)

s = input("请输入: ")
# 方法1 替换
# s2 = s.replace(' ', '')
# s2 = s2[::-1]
# print(s2)

# 方法2
# L  = []
# for x in reversed(s):  # 反向迭代
#     if x != ' ':  # 把不是空格的加入到列表中
#         L.append(x)
# s2 = ''.join(L)
# print(s2)

# 以下方法是错的
# L = list(s)
# for index in range(len(L)):  # 'abc def g'
#     if L[index] == ' ':
#         del L[index]  # 此种方法索引越界

# 方法3:
# L = s.split()  # ['abc', 'def', 'g']
# s2 = ''.join(L)  # 'abcdefg'
# s2 = s2[::-1]  # 'gfedcba'
# print(s2)


# 方法4
s2 = ''.join([x for x in reversed(s) if x != ' '])
print(s2)
