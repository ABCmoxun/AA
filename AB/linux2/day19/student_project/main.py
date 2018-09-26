# main.py
# 用于输入操作:
from menu import show_menu

import student_info as si  # 整体导入当前模块

def main():
    while True:
        # 显示菜单
        show_menu()
        # 让用户做出选择
        s = input("请选择: ")
        # 根据用户做出的选择处理相应的事情
        if s == 'q':
            return
        if s == '1':
            si.add_student()
        elif s == '2':
            # output_studnet(docs)
            si.list_all_student()
        elif s == '5':
            si.list_order_by_score_desc()  # 降序打印
        elif s == '6':
            si.list_order_by_score_asc()  # 升序
        elif s == '7':
            si.list_order_by_age_desc()
        elif s == '8':
            si.list_order_by_age_asc()
        elif s == '9':
            si.save_to_file()
        elif s == '10':
            si.read_from_file()

        # elif .....:
        #     以下同学们自己完成


main()
