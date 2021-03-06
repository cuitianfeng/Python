\函数知识体系
1 什么是函数？
2 为什么要用函数？
3 函数的分类：内置函数与自定义函数
4 如何自定义函数
  语法
  定义有参数函数，及有参函数的应用场景
  定义无参数函数，及无参函数的应用场景
  定义空函数，及空函数的应用场景

5 调用函数
    如何调用函数
    函数的返回值
    函数参数的应用：形参和实参，位置参数，关键字参数，默认参数，*args，**kwargs

6 高阶函数（函数对象）
7 函数嵌套
8 作用域与名称空间
9 装饰器
10 迭代器与生成器及协程函数
11 三元运算，列表解析、生成器表达式
12 函数的递归调用
13 内置函数
14 面向过程编程与函数式编程

\1、为何要用函数之不用函数的问题
# 1、代码的组织结构不清晰，可读性差
# 2、遇到重复的功能只能重复编写实现代码，代码冗余(重复代码多)。
# 3、功能需要扩展时，需要找出所有实现该功能的地方修改之，无法统一管理且维护难度极大（当修改时需要修改多处代码）。

\2、函数是什么
# 针对上述第二点中的问题，想象生活中的例子，修理工需要实现准备好工具箱里面放好锤子，扳手，钳子等工具，然后遇到锤钉子的场景，拿来锤子用就可以，而无需临时再制造一把锤子。
# 修理工 ===> 程序员
# 具备某一功能的工具 ===> 函数
# 要想使用工具，需要事先准备好，然后拿来就用且可以重复使用.即要想用函数，需要先定义，再使用
# 具备某一功能的工具即函数，函数的使用的必须遵循：先定义，后调用。（例如修理工和工具箱）


\3、函数分类
1、内置函数：python解释器自带的函数，python解释器启动就会定义好这些函数
为了方便我们的开发，针对一些简单的功能，python解释器已经为我们定义好了的函数即内置函数。对于内置函数，我们可以拿来就用而无需事先定义，如len(),sum(),max()
ps：我们将会在最后详细介绍常用的内置函数。
# len()
# max()
# min()
# sum()
# print()
# list()
# dist()
# set()
# int()

2、自定义函数：
很明显内置函数所能提供的功能是有限的，这就需要我们自己根据需求，事先定制好我们自己的函数来实现某种功能，以后，在遇到应用场景时，调用自定义的函数即可。例如
语法:
def 函数名(参数1,参数2,...): # 参数是可选的,def 就是definde的意思
    """注释"""
    函数体
    return 返回值


# 定义阶段，函数需要先定义后使用
def tell_tag():
    print('===========')

def tell_msg(msg):
    print(msg)


# 调用阶段
tell_tag()
tell_tag()
tell_msg('hello world')  # 为此函数传参给msg
tell_tag()
tell_tag()
# func() # 没定义的函数调用会报错。

'''
===========
===========
hello world
===========
===========

'''
