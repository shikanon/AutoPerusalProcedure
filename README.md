# AutoPerusalProcedure
--------------

英文作文自动批阅程序，主要包括拼写检测、语法检测、语句一致性检测与主题检测等几个部分。

## 程序架构

程序主要包括了五个模块，拼写检测模块、语法检测模块、统计信息模块、机器训练模块和Web页面模块。

**1、拼写检查模块**

拼写检查模块用[PyEnchant](http://pythonhosted.org/pyenchant/)对单词进行检查。

**2、语法检查模块**

语法检查模块采用[pylinkgrammar](https://pypi.python.org/pypi/pylinkgrammar)库，主要通过语法链对语义进行分析。

```>>> from pylinkgrammar.linkgrammar import Parser
>>> p = Parser()
>>> linkages = p.parse_sent("This is a simple sentence.")
>>> len(linkages)
2
>>> print linkages[0].diagram

        +-------------------Xp------------------+
        |              +--------Ost-------+     |
        |              |  +-------Ds------+     |
        +---Wd---+-Ss*b+  |     +----A----+     |
        |        |     |  |     |         |     |
    LEFT-WALL this.p is.v a simple.a sentence.n .
```


**3、统计信息模块**

这里的统计信息主要包括单词个数，句子平均长度，句子长度方差等。

**4、机器训练模块**

通过拼写检查构建拼写得分，语法检查计算各句语法得分，。

**5、Web页面模块**

grammar-link
https://www.abisource.com/projects/link-grammar/
