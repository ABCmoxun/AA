# 2. 输入一段字符串，打印出这个字符串中出现过的字符及出现过的次数：
#   如:
#     输入:abcdabcaba
#   打印如下:
#     a: 4次
#     b: 3次
#     d: 1次
#     c: 2次
#     注: 不要求打印顺序    

s = input("请输入: ")
# 方法1
# char_set = set(s)
# for c in char_set:
#     print(c, ":", s.count(c), "次")

# 方法2
# 先创建一个空字典，字典的键为字符，字典的值为: 重复次数
# 'abcdabcaba'
d = {}
for c in s:
    # 先判断字典d里有没有 c对应的字符。
    if c in d:
        # 如果已经存在于字典中，将次数做加1操作
        d[c] += 1
    else:
        # 否则 把c绑定的字符作为键加到字典中，此键对应的值为1
        d[c] = 1

print(d)
for k in d:  # 打印结果
    print(k, ":", d[k], "次")

