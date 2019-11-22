# 类属性和实例属性
```python
class Tencent():
    i = 10 # 此处i为类属性
    def __init__(self,name):
        self.name = name # 此处name为实例属性
    def function(self):
        print(self.name)
```
- 可以将类属性（比如i）理解我类的静态属性，可以通过*Tencent.i* 或者 *实例名.i* 访问，但是类名不能直接访问实例属性。
- 在使用实例更改类属性时，会创建一个实例属性的副本，就是说实例改不了类属性值，只能创建属于实例的相应副本并对其修改。
> ```python
> print(id(a.i))
> print(id(Tencent.i))
> a.i += 1
> print(a.i,end="  "),print(id(a.i)) #输出修改后a.i的内存地址
> print(Tencent.i,end="  "),print(id(Tencent.i))  #输出修改后Tencent.i的内存地址
> ```
输出结果：
> 140712785339504
> 140712785339504
> 11 140712785339536
> 10 140712785339504