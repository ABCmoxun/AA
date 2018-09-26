# 2. 分三次输入当前的小时，分钟，秒数，在终端打印此时间距离 0:0:0 过了多少秒?

s = input("请输入小时:")
hours = int(s)

s = input("请输入分钟:")
minutes = int(s)

s = input("请输入秒:")
second = int(s)

print("总秒数:", hours * 3600
      + minutes * 60 +
      second)
