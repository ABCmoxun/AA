# enumerate.py


# 此示例示意enumerate的用法
names = ['中国移动', '中国电信', '中国联通']
# for t in enumerate(names, 1):

for k, n in enumerate(names, 1):
    print("序号:", k, '----->', n)

it = iter(enumerate(names, 1))
while True:
    try:
        k, n = next(it)
        print("序号:", k, '----->', n)
    except StopIteration:
        break
