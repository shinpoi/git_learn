How to use markdown
=======================
`Learn from：`http://www.tuicool.com/m/articles/zIJrEjn </br>
`#2：`http://www.zhihu.com/question/20409634

tlie-middle
-----------------------------

#tile lv1
##tile lv2
###tile lv3
####tile lv4
#####tile lv5
######tile lv6

**加粗两个星号**</br>
*斜体一个星号*</br>
~~删除线~~

这是一段普通的文本，据说不能用回车换行？--回车
换行了吗？ --回车变成了小空格</br>
用br标签换行试试…… --br</br>
换行了吗？</br>
原来如此原来如此～  
麻烦？好吧……其实加俩空格再回车就行了orz

文字`高亮`

    代码模式,空格不会被无视啦！    <-多个空格
    Onnnanoko girlfriend = new Onnnanoko(kawaii)
    girlfriend.print()
    >>そんなも、いねぇよ
    可以前加两个tab，也可以用``括起来
    于是这样就`自动换行`了？（p.s.双tab==高亮模式）
    注意：代码模式内一切文本格式都会无效，比如*斜体*，[链接](www.12345.123)
  

    
文字超链接：[welcome to aoi-lucario.org](http://aoi-lucario.org "闲得发慌神志不清时搭起来的的半成品都算不上的不可名状之物")

* *后加个空格==原点符，否则只是普通的星号
* 再试一行
  * tab+*==二级（空心）圆点
    * 同理还有三级圆点（明明是方的）
    
引用？
>一级
</br>引用内必须使用br换行，换行并前加>没用
>>二级
>>>三级
>>>>四级

插入图片：</br>
`![](URL "注释")  //!必须有 []里的内容在图片未加载时会显示出来`

![比如这张图就无法加载，因为URL不存在](./null) </br>
![啊，图裂了](https://avatars0.githubusercontent.com/u/17242436?v=3&s=300 "俺の嫁（オイ"  )

`markdown可以混用html，那么img标签也是可行的`

<img height="200" width="200" src="https://avatars0.githubusercontent.com/u/17242436"></img>

    超链接图可以通过两行来实现：
    [![标识]](链接URL)
    [标识]:图片URL "注释"
    上下两行标示必须一样

e.g.：
[![shigure]](https://github.com/shinpoi)
[shigure]:https://avatars0.githubusercontent.com/u/17242436?v=3&s=96 "点我看看"

代码高亮：</br>
`在代码的上下行用```标记，并注明语言`

```cpp
cout<<"Hello,world"<<end;   //cpp
```

```python
print("Hellow,world")   //python
```

```html
<p style="color:blue">Hello,world</p>   //html
```
