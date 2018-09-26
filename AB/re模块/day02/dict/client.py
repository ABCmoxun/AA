from socket import * 
import sys 
import getpass

def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return 
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    s = socket()
    s.connect((HOST,PORT))

    while True:
        print('''
            ===========Welcome=========
            --1:注册   2:登录   3:退出--
            ===========================
            ''')
        try:
            cmd = int(input("输入选项>>"))
        except Exception:
            print('命令错误')
            continue
        if cmd not in [1,2,3]:
            print('请出入正确选项')
            sys.stdin.flush() #清除标准输入的缓存
            continue 
        elif cmd == 1:
            if do_register(s) == 0:
                print('注册成功！')
            else:
                print("注册失败！")
        elif cmd == 2:
            name = do_login(s)
            if name != 1:
                print('登录成功')
                login(s,name)
            else:
                print('登录失败') 
        elif cmd == 3:
            s.send(b'E')
            sys.exit('谢谢使用') 

def do_register(s):
    while True:
        name = input("User:")
        passwd = getpass.getpass()
        passwd1 = getpass.getpass('Confirm:')
        if (' ' in name) or (' ' in passwd):
            print('用户名密码不许有空格')
            continue
        if passwd != passwd1:
            print("密码不一致")
            continue
        msg = 'R {} {}'.format(name,passwd)
        s.send(msg.encode())
        data = s.recv(128).decode()

        if data == 'OK':
            return 0
        elif data == 'EXISTS':
            print("用户名存在")
            return 1
        else:
            return 1

def do_login(s):
    name = input("用户名:")
    passwd = getpass.getpass('密 码:')
    msg = 'L {} {}'.format(name,passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        return name
    else:
        print("用户名或密码不正确")
        return 1

def login(s,name):
    while True:
        print('''
        ==========查询界面===========
        --1.查词   2.历史记录  3.退出--
        ============================
        ''')
        try:
            cmd = int(input("输入选项>>"))
        except Exception:
            print('命令错误')
            continue
        if cmd not in [1,2,3]:
            print('请出入正确选项')
            sys.stdin.flush() #清除标准输入的缓存
            continue 
        elif cmd == 1:
            do_query(s,name)
        elif cmd == 2:
            do_history(s,name)
        elif cmd == 3:
            return
def do_query(s,name):
    while True:
        word = input('单词:')
        if word == '##':
            break
        msg = 'Q {} {}'.format(name,word)
        s.send(msg.encode())
        data = s.recv(128).decode()
        if data == 'OK':
            data = s.recv(2048).decode()
            print(data)
        else:
            print("没有找到该单词")

def do_history(s,name):
    msg = 'H {}'.format(name)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print("没有历史记录")

if __name__ == "__main__":
    main()