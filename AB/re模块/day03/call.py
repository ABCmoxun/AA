class CallTest(object):
    def __call__(self,a,b):
        print("This is call test")
        print('a = ',a,'b = ',b)

test = CallTest()

test(1,2)