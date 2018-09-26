# years.py


# 练习：
#   1. 假设1年只有365天，输入年数，打印这些年有多少个周

s = input("请输入年数:")
years = int(s)

weeks = years * 365 // 7
days = years * 365 % 7
print("共有", weeks, '个周，余', days, "天")
