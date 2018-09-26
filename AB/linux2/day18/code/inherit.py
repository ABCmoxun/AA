# inherit.py


# 此示例示意单继承的语法及使用方法
class Human:  # 人
    def say(self, what):  # 说话的行为
        print("说: ", what)

    def walk(self, distance):  # 走路的行为
        print("走了", distance, "公里")


h1 = Human()
h1.say("今天天气不错!")
h1.walk(5)


print("-------------------")
class Student(Human):
    # def say(self, what):  # 说话的行为
    #     print("说: ", what)

    # def walk(self, distance):  # 走路的行为
    #     print("走了", distance, "公里")

    def study(self, subject):
        print("正在学习", subject)


s1 = Student()
s1.say("今天晚饭吃什么？")
s1.walk(3)
s1.study("python")

print('------------------------')

class Teacher(Human):
    def teach(self, that):
        print("老师正在教：", that)

t1 = Teacher()
t1.say("今天下班早点回家!")
t1.walk(1)
t1.teach("面向对象")

# t1.study("魔方")