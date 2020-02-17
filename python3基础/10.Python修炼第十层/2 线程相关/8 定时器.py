# 定时器，指定n秒后执行某操作。

from threading import Timer


def hello(id):
    print("hello, world",id)


t = Timer(5, hello,args=(30,)) #Timer方法，5是时间、args是参数
t.start()  # after 1 seconds, "hello, world" will be printed


# # 验证码定时器
# from threading import Timer
# import random,time

# class Code:
#     def __init__(self):
#         self.make_cache()

#     def make_cache(self,interval=5):
#         self.cache=self.make_code()
#         print(self.cache)
#         self.t=Timer(interval,self.make_cache)
#         self.t.start()

#     def make_code(self,n=4):
#         res=''
#         for i in range(n):
#             s1=str(random.randint(0,9))
#             s2=chr(random.randint(65,90))
#             res+=random.choice([s1,s2])
#         return res

#     def check(self):
#         while True:
#             inp=input('>>: ').strip()
#             if inp.upper() ==  self.cache:
#                 print('验证成功',end='\n')
#                 self.t.cancel()
#                 break


# if __name__ == '__main__':
#     obj=Code()
#     obj.check()