class A: #框架
    def prepare(self):
        print('AAA的prepare')

    def init(self):
        print('AAA的print方法')

    #钩子方法（Hook/Handler）
    def get(self):
        pass

    def finish(self):
        print('AAA的finish方法')

    def do(self):
        #完整的业务逻辑
        self.prepare()
        self.init()
        self.get()
        self.finish()

class B(A):
    def get(self):
        print('BBB的具体业务逻辑！')

class MyTest:
    def __init__(self,x):
        x.do()

MyTest(B())