# 1. 
#   输入一个Unicode的开始值 用变量begin绑定
#   输入一个.........结束值 用变量stop绑定
#      打印开始值至结束值之间的所有对应的文字,生成字符串并打印
#   请输入开始值: 20013
#   请输入结束值: 20050
#      打印:
#       中丮丯...........乑乒

begin = int(input("请输入开始值: "))
stop = int(input("请输入结束值: "))
s = ''
for code in range(begin, stop):
    s += chr(code)

print(s)