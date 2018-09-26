# 1. 写一个函数,mysum,可以传入任意个实参的数字,返回所有实参的和

# def mysum(....):
#     ....

#   print(mysum(1,2,3,4)) # 10
#   print(mysum(5,6,7,8,9)) # 35

def mysum(*args):
    return sum(args)

print(mysum(1,2,3,4)) # 10
print(mysum(5,6,7,8,9)) # 35