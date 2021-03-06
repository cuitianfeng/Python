\一 引子
# 1 什么是数据？
　　x=10，10是我们要存储的数据

# 2 为何数据要分不同的类型
　　数据是用来表示状态的，不同的状态就应该用不同的类型的数据去表示

# 3 数据类型
　　数字（整形，长整形，浮点型，复数）
   浮点数
　　字符串
　　字节串：在介绍字符编码时介绍字节bytes类型
　　列表
　　字典
　　元组
　　集合
   布尔类型
   日期

# 4 按照以下几个点展开数据类型的学习
#======================================基本使用======================================
1、用途
2、定义方式
3、常用操作+内置的方法
#======================================该类型总结====================================
存一个值or存多个值
有序or无序
可变or不可变是指（1、可变：值变，id不变。可变的数据类型不可hash 
               2、不可变：值变，id就变。不可变的数据类型可hash）


\二 数字(整型与浮点型)
# int,不可变. 
# 作用：年龄，级别，等级，身份证号
x=10 # x=int(10)
print(id(x),type(x),x)

>>> x=1234567890
>>> y=1234567890
>>> id(x)
140206023973008
>>> id(y)
140206023972960

# 数据比较小的时候id也会相同，使用的是同一块内存空间。
>>> m=123
>>> n=123
>>> id(m)
140206023947248
>>> id(n)
140206023947248

# float,不可变. 
# 作用：工资，身高，体重
salary=3.1 # salary=float(3.1)
print(id(salary),type(salary),salary)

#长整形（了解）
    在python2中（python3中没有长整形的概念）：　　　　　　
    >>> num=2L
    >>> type(num)
    <type 'long'>

#复数（了解）　　
    >>> x=1-2j
    >>> x.real
    1.0
    >>> x.imag
    -2.0　
