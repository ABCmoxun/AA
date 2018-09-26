# continue_for.py

# 打印5以内的整数, 跳过2,不打印2
for i in range(5):
    if i == 2:  # 如果i等于2, 重新开始一次新的循环
        continue
    print(i)
