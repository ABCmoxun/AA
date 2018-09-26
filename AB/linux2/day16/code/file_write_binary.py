# file_write_binary.py

# 此程序示意以二进制方式打开文件后进行写操作

f = open('mydata.bin', 'wb')  # <<< 'wb' 二进制写模式
print("文件打开成功")

f.write(b'hello\xe4\xb8\xad')  # 写入五个字节
s = '我是汉字'
r = f.write(s.encode('utf-8'))  # 返回写入字节的数量
print("写入", s, '共写入', r, "个字节")

f.close()
