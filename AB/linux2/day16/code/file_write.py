# file_write.py


try:
    f = open("mydata.txt", 'w')  # 以只写的方法打开文件
    print("打开文件成功")
    f.write("我是第一行数据\n")
    f.write("我是第二行数据\n")
    f.writelines(['我是第三行\n', '我是第四行\n', 'five'])

    f.close()
except IOError:
    print("打开文件失败")

