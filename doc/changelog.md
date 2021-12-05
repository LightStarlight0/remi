Changelog
===
*2019 December 26*

从现在起，remi采用类属性来设置css样式和html属性，使适用的属性显式。
举个栗子, 现在更改 widget background 你可以这样做:

```python
    mywidget.css_background_color = 'green'
```

当然老的方法也是兼容的 

```python
    mywidget.style['background-color'] = 'green'
```

*2019 November 21*

Widget 类再也没有 **append** 方法了。这意味着它不能够做为 Container 被使用。
请使用新类 Container 做为通用 container 😊
这使得代码拥有更高一致性。


*2019 April 1*

事件监听注册现在可以由**do**指令完成而不是 **connect** (出于兼容性原因，它依旧可用).
i.e. 
```python
mybutton.onclick.do(myevent_listener)
```

*Older changes*

当前分支包括资源文件处理的改进
App 构造器支持  **static_file_path** 参数. 它的 value 必须是一个字典 , 其中的元素代表已命名的资源的路径。

i.e.
```python
super(MyApp, self).__init__(*args, static_file_path = {'my_resources':'./files/resources/', 'my_other_res':'./other/'})
```
为了处理特定的资源， 用户必须指定资源文件夹 key, 在文件名前加上 **'/key:'**
i.e.
```python
my_widget.attributes['background-image'] = "url('/my_resources:image.png')"
```
子文件夹被接受，所以:
```python
my_widget.attributes['background-image'] = "url('/my_resources:subfolder/other_subfolder/image.png')"
```

时间 TextInput.onenter 不再被支持。

事件 TextInput.onkeydown 和 TextInput.onkeyup 现在不同了，并且需要不同的侦听器格式。还有一个额外的 keycode。

如果输入文本只有一行(single_line)，事件 TextInput.onchange 在 Enter 键按下后也会发生

