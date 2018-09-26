# recursion.py


# 此程序用来示意递归函数的调用 
# 以下程序会无限递归，永不终止
def story():
    print("从前有座山，山上有座庙,庙里有个老和尚讲故事: ")
    story()
    print("故事请讲完了")

story()
