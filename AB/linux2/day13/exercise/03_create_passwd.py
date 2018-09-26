# create_passwd.py


import random as r

def get_random_passwd(n):
    """生成n位的随机密码"""
    source = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_'
    s = ''
    for _ in range(n):
        s += r.choice(source)
    return s

print("现在生成6位的随机密码是:",
      get_random_passwd(6))
