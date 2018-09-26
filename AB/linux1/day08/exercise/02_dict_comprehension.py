# 2. 有两个列表：
#   no = [1001, 1002, 1003, 1004]
#   names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#   用no中的编码为作为键，以names中的字符串作为值，生成相应的字典
#   提示 : range(4)来生成索引

no = [1001, 1002, 1003, 1004]
names = ['Tom', 'Jerry', 'Spike', 'Tyke']

d = {no[i]: names[i] for i in range(len(no))}

print(d)
