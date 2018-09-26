# student.py


# 此模块用来描述学生对象
class Student:
    def __init__(self, n, a, s):
        self.__name = n
        self.__age = a
        self.__score = s

    def get_infos(self):
        return (self.__name, self.__age, self.__score)

    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score

    def write_to_file(self, f):
        f.write(self.__name)
        f.write(',')
        f.write(str(self.__age))
        f.write(',')
        f.write(str(self.__score))
        f.write('\n')