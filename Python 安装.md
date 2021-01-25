# Python 安装

1. ###### https://www.python.org/

2. ![image-20210110161108354](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210110161108354.png)

3. python验证是否安装成功

   cmd（Windows + r）后 跳到安装目录下D:\Program Files\python

    执行python.exe

   显示python版本，则安装成功。

4. python配置

   我的电脑-> 属性->高级系统设置->环境变量->Path里追加pyhon的安装路径D:\Program Files\python

   然后cmd，执行python

   显示python版本，则配置成功。

5. 第一个脚本

   ![image-20210110163957995](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210110163957995.png)

   d盘下新建一个txt文件里，写个print('hello world')，python执行结果如上图。

   但是Python的文件后缀以py结尾。

6. 关于编码

   python3以前的版本，默认编码是asc编码，打印中文会乱码。python3默认utf8.

   改变编码：文件头部加

   > #-\*-  coding:utf-8 -\*-

    asc：只识别英文，8位表示一个字符。共2的8次方

    unicode(万国码)：32位表示一个字符。共2的32次方

    utf8：unicode的压缩。以尽量少的方式表示字符。

7. ---打印 print()

   字符串用单引号或者双引号包裹。

   多行字符串:用三引号包裹的字符串支持换行。注意：在多行字符串前面加r,里面的\n就变成字符串了。

   > print(r'''hello,\n
   > world''')
   >
   > 结果：
   >
   > hello,\n
   > world

   

   ---input()  输入 ，输出是Output

   

   ---

   ###### 数据类型

   1. 整型 浮点数

      整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。

      整数的除法：

      ​	在Python中，有两种除法，一种除法是`/`：计算结果是浮点数，即使是两个整数恰好整除。

      ​    还有一种除法是`//`，称为地板除，两个整数的除法仍然是整数。

      余数：

      ```python
      >>>10/3
      3.3333333333333335
      >>>10//3
      3.0
      >>>10%3
      1
      ```

   2. 布尔

      只有`True`、`False`两种值。布尔值可以用`and`、`or`和`not`运算

   3. 空值

      空值是Python里一个特殊的值，用`None`表示。None不是0。

   4. list

      list是一种有序的集合，可以随时添加和删除其中的元素。

      ```python
      #list赋值
      >>> classmates = ['Michael', 'Bob', 'Tracy']
      #显示list
      >>> classmates
      ['Michael', 'Bob', 'Tracy']
      #显示元素个数
      >>> len(classmates)
      3
      #用索引获取list值
      >>> classmates[0]
      'Michael'
      #倒着取值
      >>> classmates[-1]
      'Tracy'
      >>> classmates[-2]
      'Bob'
      #在最后面追加元素
      >>> classmates.append('lily')
      >>> classmates
      ['Michael', 'Bob', 'Tracy', 'lily']
      #在指定位置添加
      >>> classmates.insert(2,'Jack')
      >>> classmates
      ['Michael', 'Bob', 'Jack', 'Tracy', 'lily']
      #删除最后一个
      >>> classmates.pop();
      'lily'
      >>> classmates
      ['Michael', 'Bob', 'Jack', 'Tracy']
      #删除指定位置
      >>> classmates.pop(1)
      'Bob'
      #通过索引赋值，可以更改list的元素
      >>> classmates[0]='baby'
      >>> classmates
      ['baby', 'Jack', 'Tracy']
      ```

      

   5. tuple

      另一种有序列表叫元组。tuple和list非常类似，但是tuple一旦初始化就<span style="color:red">不能修改</span>。

      ```python
      >>>classmates = ('Michael', 'Bob', 'Tracy')
      ```

      因为tuple不可变，所以代码更安全。

      ```python
      #定义空tuple
      >>> t=()
      >>> t
      ()
      #多个元素的tuple
      >>> t1 = (1,3)
      >>> t1
      (1, 3)
      #定义1个元素的tuple，元素后面必须加逗号，不然这里1就代表单纯的一个数字了。
      >>> t2 = (1)
      >>> t2
      1
      >>> t2 = (1,)
      >>> t2
      (1,)
      ```

      

      来看一个“可变的”tuple：

      ```python
      >>> t = ('a', 'b', ['A', 'B'])
      >>> t[2][0] = 'X'
      >>> t[2][1] = 'Y'
      >>> t
      ('a', 'b', ['X', 'Y'])
      ```

      为什么可以变？是因为tuple里面指向了一个list。

      

      

      

8. 注释#，

   每一行都是一个语句，当语句以冒号`:`结尾时，缩进的语句视为代码块。

   > ```python
   > # print absolute value of an integer:
   > a = 100
   > if a >= 0:
   >     print(a)
   > else:
   >     print(-a)
   > ```

9. 条件判断

   if else esif  关键词后面加冒号：。

   注意缩进，python里是根据缩进来包裹代码块的。

   

10. 循环 

    for x in ...

    函数range()可以生成一个整数序列。

    while只要条件满足，就不断循环，条件不满足时退出循环。

    ```python
    L = ['Bart', 'Lisa', 'Adam']
    for name in L:
        print("hello",name)
    #while
    i=0
    while i<len(L):
        print("hello",L[i])
        i=i+1
    
        
    ```

    

11. 字典dict，相当于Java里的Map

     ```python
    >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    #key是不能重复的
    >>> d['Bob']
    75
    #对应的key值更改后，之前的值会被覆盖
    >>> d['Bob']=80
    >>> d['Bob']
    80
    #判断key是否存在
    #存在则返回True
    >>> 'Bob' in d
    True
    #存在返回值
    >>> d.get('Bob')
    80
    >>> d.get('Bob',0)
    80
    #不存在返回False
    >>> 'lily' in d
    False
    #不存在返回None,在窗口里打印不出来，看不到
    >>> d.get('lily')
    #也可以指定key不存在，返回的结果，即第二个参数
    >>> d.get('lily',-2)
    -2
     ```

    

12. set

    一组key的集合，但不存储value。无重复key，也是无序的。

    ```python
    >>> s = set([1,2,3])
    >>> s
    {1, 2, 3}
    #会去掉重复的
    #添加了3，但是set里不会多一个3
    >>> s.add(3)
    >>> s
    {1, 2, 3}
    >>> s.add(4)
    >>> s
    {1, 2, 3, 4}
    #删除key
    >>> s.remove(1)
    >>> s
    {2, 3, 4}
    ```

    

13. 函数

    ###### 内置函数：

    https://docs.python.org/3/library/functions.html

    ###### 自定义函数：

    定义一个函数要使用`def`语句，依次写出函数名、括号、括号中的参数和冒号`:`，然后，在缩进块中编写函数体，函数的返回值用`return`语句返回。

    如果你已经把`my_abs()`的函数定义保存为`abstest.py`文件了，那么，可以在该文件的当前目录下启动Python解释器，Python交互环境中用`from abstest import my_abs`来导入`my_abs()`函数，注意`abstest`是文件名（不含`.py`扩展名）：

    ```python
    >>> from abstest import my_abs                         
    >>> my_abs(-9)                                          
    9                                                        
    ```

    ###### 空函数

    如果想定义一个什么事也不做的空函数，可以用`pass`语句：

    ```python
    def nofuc:
        pass
    ```

    在if判断里，如果什么都不写，就写`pass`，如果缺少了pass,代码运行就会有语法错误。

    pass还可以作为占位符，以后想到写什么后，再补充。

    ###### 返回多个参数

    ```python
    >>> def my_func(x,y):
    ...     x1=x+2
    ...     y1=y+3
    ...     return x1,y1
    ...
    #返回多个参数可以用多个变量来接收
    >>> m,n = my_func(2,3)
    >>> print(m,n)
    4 6
    #也可以用一个变量接收，接收的变量其实是个tuple
    >>> t=my_func(2,3)
    >>> t
    (4, 6)
    ```

    ###### 函数的参数

    参数如果是list或tuple的话，变量前加*，就变成了可变参数，是一个tuple。

    默认参数：跟PHP一样使用。

    ###### 关键字参数

    可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时<span style="color:red">自动组装为一个tuple</span>。关键字参数可以不用传。

    ```python
    # 关键字参数变量前**
    >>> def person(name, age, **kw):
    ...  print('name:', name, 'age:', age, 'other:', kw)
    ...
    >>> person('Bob', 35, city='Beijing')
    name: Bob age: 35 other: {'city': 'Beijing'}
    ```

    ###### 命名关键字参数

    函数的调用者可以传入任意不受限制的关键字参数。要限制关键字参数的名字，就可以用命名关键字参数。

    命名关键字参数必须传入<span style="color:red">*参数名*</span>。关键字参数也可以传默认参数。

    ```python
    #和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    #关键字参数也可以传默认参数
    #定义了后，关键字参数只能传city和job
    def person(name, age, *, city, job):
        print(name, age, city, job)
    >>> person('Bob', 35,city=12,job='teacher')
    Bob 35 12 teacher
    #如果传入非city和job的sex参数，就会报错
    >>> person('Bob', 35,sex=12,job='teacher')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: person() got an unexpected keyword argument 'sex'
    #如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
    def person(name, age, *args, city, job):
        print(name, age, args,city, job)
    ```

    ###### 参数组合

    在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

14. 练习

    ```python
    #一般参数
    def product(t):
        if len(t)==1:
            return t[0]
        elif len(t)>1:
            x = 1
            for n in t:
                x=x*n
            return x
        else:
            return 0
            
    print(product([]))
    0
    print(product([5]))
    5
    print(product([5,6,7]))
    210
    #可变参数*t,
    def product(*t):
        if len(t)==1:
            return t[0]
        elif len(t)>1:
            x = 1
            for n in t:
                x=x*n
            return x
        else:
            return 0
    #可变参数就是传入的参数个数是可变的        
    print(product(1,2,3,4))
    24
    ```

    

15. 

    

    