# 3.用while 循环生成如下字符串:
#    1. 生成'ABCDEFG...... XYZ' 并打印
#    2. 生成'AaBbCcDdEeFf.....XxYyZz' 并打印
#    提示:
#      用chr和ord函数

# 1. 生成'ABCDEFG...... XYZ' 并打印
az = ""  # 用于累加字符
i = ord('A') # 65 # 0x41
end = ord('Z')  # ord('A') + 26 -1
while i <= end:
    az += chr(i)
    i += 1
else:
    print(az)

# 2. 生成'AaBbCcDdEeFf.....XxYyZz' 并打印
az = ''
i = ord('A')
while i <= end:
    az += chr(i)  # 加了一个大写字母
    # az += chr(i + (ord('a')-ord('A')))    # 
    az += chr(i + 0x20)    #  大写变小写码值+32,加一个小写字母
    i += 1
else:
    print(az)

