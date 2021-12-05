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

Widget class has no more **append** method. This means it cannot be used as a Container.
Use the new class Container as a generic container instead.
This allows higher code consistency.


*2019 April 1*

Event listener registration can now be done by the **do** instruction instead of **connect** (that stays available for compatibility reasons).
i.e. 
```python
mybutton.onclick.do(myevent_listener)
```

*Older changes*

The current branch includes improvements about resource files handling. 
App constructor accepts **static_file_path** parameter. Its value have to be a dictionary, where elements represents named resources paths.

i.e.
```python
super(MyApp, self).__init__(*args, static_file_path = {'my_resources':'./files/resources/', 'my_other_res':'./other/'})
```
To address a specific resource, the user have to specify the resource folder key, prepending it to the filename in the format **'/key:'**
i.e.
```python
my_widget.attributes['background-image'] = "url('/my_resources:image.png')"
```
Subfolders are accepted, and so:
```python
my_widget.attributes['background-image'] = "url('/my_resources:subfolder/other_subfolder/image.png')"
```

The event TextInput.onenter is no longer supported.

The events TextInput.onkeydown and TextInput.onkeyup are now different, and require a different listener format. There is an additional parameter keycode.

The TextInput.onchange event now occurs also in case of Enter key pressed, if TextInput is single_line.

