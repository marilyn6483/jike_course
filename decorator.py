# -*- coding: utf-8 -*-
import time
from functools import wraps

'''
def logging(func):
    def wrapper(**kwargs):
        print "{} called".format(func.__name__)
        func(**kwargs)
        print "{} finished".format(func.__name__)
    return wrapper
    
@logging
def process(**kwargs):
    print(kwargs)
    
args = {"k1": "hello", "k2": "world"}
process(**args)



#静态方法，类方法

class A(object):
    var = 1
    
    def func(self):
        print self.var
        print "T am a func in class A"
        
    @staticmethod #静态方法
    def static_method():
        print A.var
        print "I am a static_method"
        
    @classmethod #类方法
    def class_method(cls):
        print cls.var
        cls().func()
        print cls
        print "I am a class method"
   
a = A()
a.func()
a.static_method()
a.class_method()      

# @staticmethod将类成员方法声明为静态方法，不需要传入self参数，可以通过类直接调用，也可以通过实例调用
# @classmethod将类成员方法声明为类方法，传入cls参数，通过类直接调用，cls是指当前具体类
A.var
A.static_method()
A.class_method() 
A.func() #不能通过类直接调用，需要通过实例调用


     
#带有参数的装饰器
#使用两层包装函数 一个传function，一个传function的参数

def time_me(info="cost"):
    def wrapper1(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print "{} {} total time is {}".format(func.__name__, info, end-start)
        return wrapper
    return wrapper1
    
@time_me("consume")
def test1(*args, **kwargs):
    print args
    time.sleep(1)
    
test1(1, 2, 3, 4)
test1({"k1": "123", "k2": "456"})



#装饰器不带参数
def time_cost(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        #print func.__name__
        result = func(*args, **kwargs)
        end = time.time()
        print "{} consumes total {} seconds".format(func.__name__, end-start)
        return result
    wrapper.__name__ = func.__name__ #重命名
    return wrapper

@time_cost
def test1(x, y):
    print test1.__name__
    print "func test1 called"
    time.sleep(1)
    return x + y
print test1(1, 10)

'''

#使用functools.wraps
def dec_fun(func):
    #@wraps(func)
    def wrapper(*args, **kwargs):
        print "in wrapper"
        return func(*args, **kwargs)
    return wrapper
    
@dec_fun
def test(*args, **kwargs):
    "test func"
    print "in test"
    print test.__name__
    print test.__doc__
    return args
    
print test(1, 2, 3, 4)

#重绑定的过程----
'''
    def test以后，test = dec_fun(test) = wrapper
    test(1, 2, 3, 4) = wrapper(1, 2, 3, 4)
    此时test函数已经被重新绑定为wrapp函数，所以在test函数里面打印test.__name__,得到的是wrapp，test.__doc__得到的是None
'''



        
        
        
        
        
        
        
        
        
        