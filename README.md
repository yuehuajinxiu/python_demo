













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