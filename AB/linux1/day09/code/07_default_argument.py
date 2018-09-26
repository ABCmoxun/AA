# 07_default_argument.py


def info(name, age=1, address="不详"):
    print("我叫", name, '我今年:', age,
          '岁, 家庭住址:', address)


info("张飞", 30, "中原")
info("Tarena", 10)
info("赵云")

