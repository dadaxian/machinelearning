# list（列表）

> Python内置的一种数据类型是列表：list。是一种有序的集合，可以随时添加和删除其中的元素
> 使用中括号 []
> 用索引来访问list中每一个位置的元素，记得索引是从0开始的：当索引超出了范围时，Python会报一个> IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，list[-1]直接获取最后一个元素。
> 1. 可以往list中追加元素到末尾list.append(要添加的元素) 
> 2. 也可以把元素插入到指定的位置，比如索引号为1的位置：list.insert(1,要添加的数据)
> 3. 要删除list末尾的元素，用pop()方法：list.pop(),不填东西默认删除最后一个。要删除指定位置元素，用pop(i)方法，其中i是索引位置，例：list.pop(1)删除索引为1的数据信息。
> 4. 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：list[1] = '替换元素'
> 5. list元素也可以是另一个list，比如：list[1,2,3,[1,2,3],4]
> > append() 追加数据
> > insert() 插入数据
> > pop()    移出数据
> > clear()  删除列表所有元素
> > copy()   拷贝列表
> > count()  获取某元素出现的次数
> > extend   扩展列表,把
> > index()  获取某个元素的索引
> > remove() 移除列表中某个元素
> > reverse()反向排序
> > sort()   排序(升序. 降序)


# tuple(元组)

> 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，它也没有append()，insert()这> 样的方法，其他获取元素的方法和list是一样的，可以正常地使用tupe[0]， tupe[-1]，但不能赋值成另外的元素。
> 使用小括号 ()
> > count() 统计元组中某个元素出现的次数
> > result = tuple1.count(2)
> > print(result)
> > index() 获取某个元素在元组中的第一个位置索引，若有返回索引值，若没有抛出异常错误
> > result = tuple1.index(1)


# set(集合)

> 集合中可以存储任意类型的数据，集合中不会出现重复的数据
> python 集合的添加有两种常用方法，分别是add和update。  set1.add(要添加的数据)
> set1.update（）
> 删除 setl.remove(要删除的数据) . . . 从集合中移出一个元素setl.pop()
> > 1. 列表转换为集合
> > ```python
> > list1 = [1,2,1,2,2,1,3,2,14,2]
> > t = set(list1)
> > ```
> > 2. 集合转换为列表
> > ```python
> > list2 = list(t)
> > print(list2)
> > ```
> > 3. 列表转换为元组
> > ```python
> > tuple1 = tuple(list1)
> > print(tuple1)
> > ```
> > 4. 元组转换为列表
> > ```python
> > list3 = list(tuple1)
> > print(list3) 
> > ``` 
> >  

# dict(字典)
> 字典是另一种可变容器模型，且可存储任意类型对象。
> 使用大括号 {}
> 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：
> ```python
> d = {key1 : value1, key2 : value2 }
> ```
> 字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
> 两个重要的点需要记住：
> > - 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
> > - 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行。
> 
> > 1. dict.clear()
> > 删除字典内所有元素
> > 2. dict.copy()
> > 返回一个字典的浅复制
> > 3. dict.fromkeys(seq[, val])
> > 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
> > 4. dict.get(key, default=None)
> > dic["a"]=dic.get("a",0)+1 这里赋值不能像C++里面那样，C++里如果原来没有这个键，就默认这个键对应的值为0，但这样在Python里会报错
> > 返回指定键的值，如果值不在字典中返回default值（根据key取出值，若key不存在，返回默认值）
> > 5. dict.has_key(key)
> > 如果键在字典dict里返回true，否则返回false
> > 6. dict.items()
> > 以列表返回可遍历的(键, 值) 元组数组    即获取字典中所有的key,value，返回[(key,value)
> > 7. dict.keys()
> > 以列表返回一个字典所有的键（获取字典所有的key）
> > 8. dict.setdefault(key, default=None)
> > 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
> > 9. dict.update(dict2)
> > 把字典dict2的键/值对更新到dict里
> > 10. dict.values()
> > 以列表返回字典中的所有值 （获取字典所有的value）
> > 11. pop(key[,default])
> > 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
> > 根据key移出值
> > 12. popitem()
> > 随机返回并删除字典中的一对键和值。 移出字典中某个key和值，返回(key,value)