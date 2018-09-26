import re 

s = '''hello world
Hello kitty
nihao China
'''

pattern = '''(?P<dog>hello) #dog 组
\s+ #空字符
(world) #第二组用来匹配world
'''
l = re.findall(pattern,s,re.X | re.I)
print(l)


# l = re.findall('.+',s,re.S)
# print(l)


# l = re.findall('^nihao',s,re.M)
# print(l)

# l = re.findall('H\w+',s,re.I)
# print(l)



