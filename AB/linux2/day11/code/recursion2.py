

# 此程序用来示意递归函数的调用 
# 此递归用参数来控制最大次数为3
def story(times):  # times代表讲故事的次数
    print("第", times, "遍:")
    print("从前有座山，山上有座庙,庙里有个老和尚讲故事: ")
    if times >= 3:
        return  # 不要再讲故事了
    story(times + 1)  # 将当前次数加1,再讲一遍
    print("故事请讲完了")


story(1)
