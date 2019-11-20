# 文本的词向量的构造
## 正则分割
```python
import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."  
print re.sub(r'\s+', '-', text)  
```