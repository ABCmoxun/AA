import time 

def fun1():
    time.sleep(6)
    print("做完第一件事")

def fun2():
    time.sleep(4)
    print("做完第二件事")

if __name__ == "__main__":
    fun1()
    fun2()