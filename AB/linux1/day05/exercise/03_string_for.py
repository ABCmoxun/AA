# 3.用while 循环生成如下字符串:
#    1. 生成'ABCDEFG...... XYZ' 并打印
#    2. 生成'AaBbCcDdEeFf.....XxYyZz' 并打印
#    提示:
#      用chr和ord函数

# 1. 生成'ABCDEFG...... XYZ' 并打印
az = ""  # 用于累加字符
for i in range(ord('A'), ord('Z') + 1):
    az += chr(i)
else:
    print(az)

# 2. 生成'AaBbCcDdEeFf.....XxYyZz' 并打印
az = ''
for i in range(ord('A'), ord('A') + 26):
    az += chr(i) + chr(i + 0x20)
else:
    print(az)

