在python开发的过程中，经常会遇到需要打印各种信息。海量的信息堆砌在控制台中，就会导致信息都混在一起，降低了重要信息的可读性。这时候，如果能给重要的信息加上字体颜色，那么就会更加方便用户阅读了。 
当然了，控制台的展示效果有限，并不能像前端一样炫酷，只能做一些简单的设置。不过站在可读性的角度来看，已经好很多了。

\书写格式:
     开头部分：\033[显示方式;前景色;背景色m + 结尾部分：\033[0m
     注意：开头部分的三个参数：显示方式，前景色，背景色是可选参数，可以只写其中的某一个；另外由于表示三个参数不同含义的数值都是唯一的没有重复的，所以三个参数的书写先后顺序没有固定要求，系统都能识别；
     但是，建议按照默认的格式规范书写。对于结尾部分，其实也可以省略，但是为了书写规范，建议\033[***开头，\033[0m结尾。

-------------------------------------------
字体色     |       背景色     |      颜色描述
-------------------------------------------
30        |        40       |       黑色
31        |        41       |       红色
32        |        42       |       绿色
33        |        43       |       黃色
34        |        44       |       蓝色
35        |        45       |       紫红色
36        |        46       |       青蓝色
37        |        47       |       白色
-------------------------------------------

-------------------------------
显示方式     |      效果
-------------------------------
0           |     终端默认设置
1           |     高亮显示
4           |     使用下划线
5           |     闪烁
7           |     反白显示
8           |     不可见
-------------------------------

\数值表示的参数含义:
显示方式: 0（默认值）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
前景色(字体): 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
背景色: 40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）

常见开头格式：
\033[0m             默认字体正常显示，不高亮
\033[32;0m          红色字体正常显示
\033[1;32;40m       显示方式: 高亮    字体前景色：绿色  背景色：黑色
\033[0;31;46m       显示方式: 正常    字体前景色：红色  背景色：青色
\033[1;31m          显示方式: 高亮    字体前景色：红色  背景色：无

\举例说明:
示例1：
print('\033[1;35;0m字体变色，但无背景色 \033[0m')  # 有高亮 或者 print('\033[1;35m字体有色，但无背景色 \033[0m')
print('\033[1;45m 字体不变色，有背景色 \033[0m')  # 有高亮
print('\033[1;35;46m 字体有色，且有背景色 \033[0m')  # 有高亮
print('\033[0;35;46m 字体有色，且有背景色 \033[0m')  # 无高亮

示例2：开头和结尾写格式，中间的就包含进去了。
print('\033[0;36m床前明月光，')
print('疑是地上霜。')
print('举头望明月，')
print('低头思故乡。\033[0m')

示例3：
print('\033[0m这是显示方式0')
print('\033[1m这是显示方式1')
print('\033[4m这是显示方式4')
print('\033[5m这是显示方式5')
print('\033[7m这是显示方式7')
print('\033[8m这是显示方式8')
print('\033[30m这是前景色0')
print('\033[31m这是前景色1')
print('\033[32m这是前景色2')
print('\033[33m这是前景色3')
print('\033[34m这是前景色4')
print('\033[35m这是前景色5')
print('\033[36m这是前景色6')
print('\033[37m这是前景色7')
print('\033[40m这是背景色0')
print('\033[41m这是背景色1')
print('\033[42m这是背景色2')
print('\033[43m这是背景色3')
print('\033[44m这是背景色4')
print('\033[45m这是背景色5')
print('\033[46m这是背景色6')
print('\033[47m这是背景色7')

示例4：
print('\033[1;31;40m是是是是是')     #下一目标输出背景为黑色，颜色红色高亮显示
print('*' * 50)
print('\033[7;31m错误次数超限，用户已被永久锁定，请联系管理员！\033[1;31;40m')  #字体颜色红色反白处理
print('*' * 50)
print('\033[0m')