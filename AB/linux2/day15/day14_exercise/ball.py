# 1. 一个球从100米高度落下，每次落地后反弹高度为原高度的一半，再落下，
#   1) 写程序算出皮球从第10次落地后反弹高度是多少？
#   2) 球共经过多少米路径?


def ball_last_height(height, times):
    for _ in range(times):
        # 此处的语句会执行 times 次
        height /= 2

    return height


def ball_distance(height, times):
    meter = 0  # 用来累加路程的和
    for _ in range(times):
        meter += height  # 累加下落过程的路程
        height /= 2  # 算出反弹高度
        meter += height  # 累加反弹过程的路程
    return meter


height = ball_last_height(100, 10)
print("最终的高度是: ", height)

meter = ball_distance(100, 10)
print("球经历的路程是: ", meter)