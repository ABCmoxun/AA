# instance_method.py


# 本示例示意实例方法的定义方式和调用方法
class Dog:
    """这是一个类，用于描述一个小动物的行为"""
    def eat(self, food):
        """小狗能够有吃东西的行为"""
        print("小狗吃了", food)
        # 为self绑定的对象添加food属性来记着狗吃的是什么
        self.food = food

    def food_info(self):
        """能否在此方法内得到小狗上次吃的食物是什么"""
        print("上次吃的是:", self.food)


dog1 = Dog()  # 创建一个实例对象
dog1.eat("骨头")  # 让狗吃东西
# dog1.food = "骨头"

dog2 = Dog()  # 再创建一个实例对象
dog2.eat("包子")

dog1.food_info()  # 得到上次dog1吃的是什么？
dog2.food_info()
