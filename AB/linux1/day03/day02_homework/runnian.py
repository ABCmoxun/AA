# 3. 给出一个年份，判断是否为闰年并打印
#   闰年规则：
#   　　每四年一闰，每百年不闰，四百年又闰
#   2016年　闰年
#   2100年 非闰年
#   2400年 闰年

year = int(input("请输入年份:"))
#方法1
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(year, "是闰年")
# else:
#     print(year, "不是闰年")

# 方法2
if year % 400 == 0:
    print(year, "是闰年")
elif year % 100 == 0:
    print(year, '不是闰年')
elif year % 4 == 0:
    print(year, "是闰年")
else:
    print(year, '不是闰年')
    