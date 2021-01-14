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

