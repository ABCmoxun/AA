# instance_method.py


# 本示例示意实例方法的定义方式和调用方法
class Dog:
    """这是一个类，用于描述一个小动物的行为"""
    def eat(self, food):
        """小狗能够有吃东西的行为"""
        print("小狗吃了", food)

    def sleep(self, hour):
        print("小狗睡了", hour, "小时")


dog1 = Dog()  # 创建一个实例对象
dog1.eat("骨头")  # 让狗吃东西
dog1.sleep(1)  # 让狗睡觉

dog2 = Dog()  # 再创建一个实例对象
dog2.eat("包子")
dog2.sleep(2)

dog3 = Dog()
Dog.eat(dog3, "狗粮")
Dog.sleep(dog3, 3)
