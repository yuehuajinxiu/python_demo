

https://www.lanqiao.cn/questions/102676/

### python高级特性



##### 切片

Python提供了切片（Slice）操作符。

```python
#比如list截取
>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取从索引0，到索引3的值，但是不包括索引3
>>> L[0:3]
['Michael', 'Sarah', 'Tracy']
#取索引2，3，不包括4
>>> L[2:4]
['Tracy', 'Bob']
>>> L[2:6]
['Tracy', 'Bob', 'Jack']
#只写[:]就可以原样复制一个list
>>> L[:]
['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#倒数第一个元素的索引是-1
#从-1开始截取
>>> L[-1]
'Jack'
>>> L[-1:]
['Jack']
#从倒数第三个元素
>>> L[-3:]
['Tracy', 'Bob', 'Jack']
```

这里是以list为例，其实tuple也是一样的。<span style="color:red">字符串</span>也可以看成是一种list。

##### 迭代for

```python
#dict迭代的是key
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...     print(key)
...
a
b
c
#如果想迭代value，d.values()
>>> for v in d.values():
...     print(v)
...
1
2
3
#key,value一起，d.items()
>>> for k,v in d.items():
...     print(k,v)
...
a 1
b 2
c 3
```

如何判断一个对象是可迭代对象呢？

```python
>>> from collections.abc import Iterable
>>> isinstance('abc', Iterable)
True
```

如果要对list实现类似Java那样的下标循环怎么办？Python内置的`enumerate`函数可以把一个list变成<span style="color:red">索引-元素对</span>，这样就可以在`for`循环中同时迭代索引和元素本身：

```python
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i)
...
0
1
2
>>> for i in enumerate(['A', 'B', 'C']):
...     print(i)
...
(0, 'A')
(1, 'B')
(2, 'C')
```



##### 列表生成式

列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

```python
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

要生成`[1x1, 2x2, 3x3, ..., 10x10]`怎么做？

```python
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

for循环后面还可以加上if判断,

但是<span style="color:red">注意：</span>

使用列表生成式的时候,不能在最后的`if`加上`else`

如果if 写在前面，必须加上else 如[x if x % 2 == 0 else -x for x in range(1, 11)]

```python
>>> [x * x for x in range(1, 11) if x%2==1]
[1, 9, 25, 49, 81]
```

还可以使用两层循环，可以生成全排列：

```python
>>> [m+n for m in 'abc' for n in 'xyz']
['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']
```

##### 生成器

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。

如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

只要把一个列表生成式的`[]`改成`()`，就创建了一个generator：

```python
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x0000026F3AAACF20>
>>>
>>> for n in g:
...     print(n)
...
0
1
4
9
16
25
36
49
64
81
```



在每次调用`next()`的时候执行，遇到`yield`语句返回，再次执行时从上次返回的`yield`语句处继续执行。

##### 迭代器

可以被`next()`函数调用并不断返回下一个值的对象称为迭代器：`Iterator`。

生成器都是`Iterator`对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`。

把`list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用`iter()`函数：

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

### 函数式编程

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

##### 变量可以指向函数

```python
>>> abs(-10)
10
>>> f=abs
>>> f(-10)
10
```

##### 传入函数

既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为<span style="color:red">高阶函数</span>。

```python
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))
11
```

Python内建的高阶函数：

##### map()

`map()`函数接收两个参数，一个是函数，一个是`Iterable`，`map`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`返回。Iterator是一个惰性序列，所以要强迫`map()`完成计算结果，需要用`list()`函数获得所有结果并返回list。

```python
>>> def f(x):
...     return x*x
...
>>> r = map(f,[1,3,5,6])
>>> r
<map object at 0x000001A8DAB5EFD0>
>>> list(r)
[1, 9, 25, 36]
```



##### reduce()

`reduce`把一个函数作用在一个序列`[x1, x2, x3, ...]`上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算，其效果就是：

```
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

```python
>>> from functools import reduce
>>> def fn(x, y):
...     return x*10+y
...
>>> reduce(fn,[1,3,4,6])
1346
```



##### filter()

`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。

```python
>>> def not_empty(s):
...     return s and s.strip()
...
>>> f = filter( not_empty,['a','','b',' ',None])
>>> list(f)
['a', 'b']
```

****埃拉算法练习****

```python

```



##### sorted()

```python
#对list排序
>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
#还可以接收一个key函数来实现自定义的排序
#这里是按照绝对值大小排序
>>> sorted([36, 5, -12, 9, -21],key=abs)
[5, 9, -12, -21, 36]
#排序的结果，再倒序
>>> sorted([36, 5, -12, 9, -21],key=abs,reverse=True)
[36, -21, -12, 9, 5]
#再看个例子，把字符串转成小写后再排序即（不区分大小写排序）
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
['about', 'bob', 'Credit', 'Zoo']
```

练习

```python
>>> L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
>>> def by_score(t):
...     return t[1]
...
>>> def by_name(t):
...     return t[0]
...
#按成绩从高到低排序
>>> L2 = sorted(L,key=by_score,reverse=True)
>>> print(L2)
[('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]
#按姓名排序
>>> L3 =  sorted(L,key=by_name)
>>> L3
[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
```

##### 返回函数

函数不只可以作为参数，还可以作为另一个函数的返回值。

```python
#定义一个求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
>>>f = lazy_sum(1, 3, 5, 7, 9)
#当调用f()时，才是真正的计算求和
>>> f()
25

```

内部函数`sum`可以引用外部函数`lazy_sum`的参数和局部变量，当`lazy_sum`返回函数`sum`时，相关参数和变量都保存在返回的函数中，这种称为“<span style="color:red">闭包</span>（Closure）”的程序结构拥有极大的威力。

##### 装饰器decorator

```python
>>> def now():
...     print('2021-1-18')
...
#__name__属性，可以拿到函数的名字
>>> now.__name__
'now'

```

在函数调用前后自动打印日志，但又不希望修改`now()`函数的定义，这种在代码运行期间动态增加功能的方式，称之为<span style='color:red'>“装饰器”（Decorator）</span>。

本质上，decorator就是一个返回函数的高阶函数。

```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
#我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2015-3-25')
    
#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
>>> now()
call now():
2015-3-25
```

##### 偏函数

Python的`functools`模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。

当函数的参数个数太多，需要简化时，使用`functools.partial`可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

```python
#字符串转整数函数
#默认是10进制
>>> int('123')
123
>>> int('123',8)
83
>>> int('123',16)
291
#如果想转二级制，就要每次调用
>>> int('100',2)
4
#闲麻烦得话，就定义一个转二进制字符串的int2()方法
#这时不需要自己定义，python提供了偏函数，
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000')
8
```

#### 模块

大大提高了代码的可维护性。

python里一个py文件就是一个模块。

按目录来组织模块的方法，称为包（Package）。

```ascii
#例如mycompany目录，每一个包目录下面必须有一个__init__.py的文件，不然就被当成普通目录，而不是包了。
#__init__.py可以是空文件，也可以有Python代码
mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py
```

Python模块的标准文件模板：

​	第一行，在Linux/Mac下运行

​	第二行，编码设定

​	第四行，文档注释

​	第六行，标记作者

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'
```

使用模块：python自带的sys模块 

```python
 import sys
```

##### 作用域

正常的函数和变量名是公开的（public），可以被直接引用，比如：`abc`，`x123`，`PI`等；

类似`__xxx__`这样的变量是特殊变量，可以被直接引用，比如`__author__，__name__`

类似`_xxx`和`__xxx`这样的函数或变量就是<span style="color:red">非公开</span>的（private），不应该被直接引用，不是说不能被引用。python里没有像Java里可以把变量或者函数设置为private属性，就用这样__开头的变量代替。

##### 第三方模块

在Python中，安装第三方模块，是通过包管理工具<span style="color:red">pip</span>完成的。

用pip一个个安装有点麻烦，而且还要考虑兼容性，推荐Anaconda，这是一个基于Python的数据处理和科学计算平台。可以从<a href="https://www.anaconda.com/products/individual">Anaconda官网</a>下载GUI安装包，安装包有500~600M，所以需要耐心等待下载。下载后直接安装，Anaconda会把系统Path中的python指向自己自带的Python，并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录。

python的IDE : Anaconda ,<a href="https://www.jetbrains.com/pycharm/">Pycharm</a>

#### 面向对象编程

##### 类和实例

```python
#class 关键字，Student类名 (object)表示该类是从哪个类继承下来的
class Student(object):
    def __init__(self, name, score):
        #属性名称前加`__`，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__name = name
        self.__score = score
```

`__init__`相当于构造函数

```python
from Student import *
str = Student(‘Lily’,15)
print(str)
<Student.Student object at 0x0000021DA25F86D0>
```



##### 获取对象信息

type()获取对象类型

isinstance()判断class的类型

dir()获得一个对象的所有属性和方法

##### 实例属性和类属性

python是动态语言，类实例创建后，可以绑定任意的属性和方法。

```python
#比如这个类，里面什么都没有定义
class Student(object):
    pass
#给实例绑定一个属性
s = Student()
s.name = 'Lucy'
print(s.name)
Lucy
#给实例绑定一个方法
def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(12)
print(s.age)
12
#注意：给一个实例绑定的方法，对另一个实例是不起作用的：
#可以给class绑定方法，这样所有的实例都可以用

Student.set_age = set_age
s.set_age(20)
s2 = Student()
s2.set_age(22)
print(s.age)
print(s2.age)
20
22

```

但是可以通过一个特殊的`__slots__`变量限制添加实例的属性。

```python
#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student(object):
    #name,age以外的属性不能添加，否则报错
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = "Lucy"
print(s.name)
s.score=23
print(s.score)
Lucy
Traceback (most recent call last):
  File "C:/Users/dell/PycharmProjects/pythonProject/main.py", line 20, in <module>
    s.score=23
AttributeError: 'Student' object has no attribute 'score'    
```

##### `@property`

python内置装饰器

```python
class Student(object):
#相当于一个get方法
    @property
    def score(self):
        return self._score
    #property又创建了score.setter装饰器，这个相当于set方法
    @score.setter装饰器，这个相当于set方法
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
#利用装饰器，相当于写了get set方法，对属性做了检验        
s.score = 9999
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
```

##### 多重继承

python允许多重继承

```python
class Dog(Mammal, Runnable):
    pass
```

##### 定制类

https://docs.python.org/3/reference/datamodel.html#special-method-names

`__str__`

```python
#原本类是这样的
class Student(object):

    def __init__(self,name):
        self.name = name
s = Student("meimei")
print(s)
<Student.Student object at 0x000001D31A8386D0>
#在类里定义了__str__()方法后，打印类实例后
class Student(object):

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
s = Student("meimei")
print(s)
Student object (name: meimei)
```

`__iter__()`

一个类想被用于`for ... in`循环，类似list或tuple那样，就必须实现一个`__iter__()`方法，该方法返回一个迭代对象。

`__getitem__`

`__getattr__` 调用类的方法或属性时，如果不存在，就会报错。利用这个方法，做判断。

`__call__`可以直接对实例进行调用。

##### 枚举类

为枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。

```python
from enum import Enum

Months = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Months.__members__.items():
    print(name, '=>', member, ',', member.value)
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
Apr => Month.Apr , 4
May => Month.May , 5
Jun => Month.Jun , 6
Jul => Month.Jul , 7
Aug => Month.Aug , 8
Sep => Month.Sep , 9
Oct => Month.Oct , 10
Nov => Month.Nov , 11
Dec => Month.Dec , 12
```

`value`属性则是自动赋给成员的`int`常量，默认从`1`开始计数。

可以从`Enum`派生出自定义类：

```python
from enum import Enum,unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Wed)
print(Weekday['Wed'])

print(Weekday.Wed.value)
print(Weekday(3))
print(Weekday(7))
Weekday.Wed
Weekday.Wed
3
Weekday.Wed
```

#### IO编程

文件读写

文件读写权限：

| r    | 只读模式                           |
| ---- | ---------------------------------- |
| w    | 写入文件，如果文件不存在会自动创建 |
| rb   | 以二进制文件打开文件只读。         |
| wb   | 以二进制文件打开文件可写。         |
| a    | 在文件末尾追加。                   |



```python
f = open("test.txt","w")  #在当前目录创建一个文件
f.write("hello world")
f.close()
```

```python
#读取文件
f = open("test.txt","r")
content = f.read(5)
print(content)
#read方法，指针移动
content = f.read(3)
print(content)
f.close()
#打印结果
hello
 wo
```

```python
#若文件里有多行内容
#hello world
#hello 123
#如何读取文件所有的内容
f = open("test.txt","r")
content = f.readlines()
print(content)
f.close()
#结果  文件读取时，按每一行读取，放到字典里
['hello world\n', 'hello 123']
#还有f.readline()每次只读一行
```



```python
import os

os.rename
os下有很多对文件的处理方法，自学去
```

#### 异常处理

```python
try:
    pass
except Exception as e:
    print('except:', e)
finally:
    
```

#### 爬虫

参考资料：https://www.bilibili.com/video/BV12E411A7ZQ?p=20

```python
#-*- coding = utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import xlwt
import re



def getData(url):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
    req = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    return data



if __name__ == "__main__" :
    url = "https://movie.douban.com/top250"
    data = getData(url)
    print(data)
```

