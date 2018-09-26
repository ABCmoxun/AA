# 2. 输入一个整数（代表树干的高度)
#     打印如下一棵圣诞树
#   输入:2
#     *
#    ***
#     *
#     *
#   输入:3
#     *
#    ***
#   *****
#     *
#     *
#     *

n = int(input("请输入: "))

# 打印树冠
# 方法1
for i in range(1, n + 1):
    starts = '*' * (2 * i - 1)  # 星号个数
    blanks = ' ' * (n - i)  # 计算空格个数
    print(blanks + starts)

# 方法2
# for i in range(1, n + 1):
#     starts = '*' * (2 * i - 1)
#     print(starts.center(2 * n - 1))

for _ in range(n):
    print(' ' * (n - 1) + '*')
