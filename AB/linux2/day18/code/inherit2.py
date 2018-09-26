# inherit.py


# 此示例示意单继承的语法及使用方法
class Human:  # 人
    def say(self, what):  # 说话的行为
        print("说: ", what)

    def walk(self, distance):  # 走路的行为
        print("走了", distance, "公里")


class Student(Human):
    def study(self, subject):
        print("正在学习", subject)


class Teacher(Student):
    def teach(self, that):
        print("老师正在教：", that)

t1 = Teacher()
t1.say("今天下班早点回家!")
t1.walk(1)
t1.teach("面向对象")

t1.study("转魔方")