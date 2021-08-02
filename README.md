[![Build Status](https://travis-ci.com/dddomodossola/remi.svg?branch=master)](https://travis-ci.com/dddomodossola/remi)

<p align="center">
    <img src="https://raw.githubusercontent.com/dddomodossola/remi/master/remi/res/logo.png" width="430">
</p>

<h2 align="center" style="font-weight:bolder">
    GUI library for your Python applications
</h2>

<p align="center" style="white-space:pre">
Remi is a GUI library for Python applications that gets rendered in web browsers. 
This allows you to access your interface locally and remotely.
</p>

Do you need support?
<p align="center">
<a href="https://www.reddit.com/r/RemiGUI" style="font-size:25px">Reddit - (subreddit RemiGUI)</a>
</p>


There is also a **drag n drop GUI Editor**. Look at the [Editor](https://github.com/dddomodossola/remi/tree/master/editor) subfolder to download your copy.

<a href="https://vimeo.com/517626422" style="font-size:25px">A demostrative video from the great REVVEN labs</a>

<p align="center">


开始
===
获取一个稳定的版本:
```
pip install remi
```

获取一个有更多更新的实验版本 [下载](https://github.com/dddomodossola/remi/archive/master.zip) 或者直接从项目git

```
python setup.py install
```
或者直接使用pip安装

```
pip install git+https://github.com/dddomodossola/remi.git
```

然后测试实验脚本 (从github下载 https://github.com/dddomodossola/remi/blob/master/examples/widgets_overview_app.py):
```
python widgets_overview_app.py
```


Remi
===
Remi是一个独立的Python GUI库. 只有不到100 Kbytes的源代码, 完美符合您的胃口.

<p align="center">
    <img src="https://raw.githubusercontent.com/dddomodossola/remi/development/remi/res/screenshot.png" title="Widgets overview">
</p>

Remi 允许开发者使用创建一个独立的GUI平台. 整个GUI呈现在你的浏览器中. **无需HTML** , Remi自动翻译你的python代码至HTML. 当你启动你的项目时, 它会开启一个网络服务器来运行.

最基础的项目如下:

```py
import remi.gui as gui
from remi import start, App

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=120, height=100)
        self.lbl = gui.Label('Hello world!')
        self.bt = gui.Button('Press me!')

        # 为鼠标点击按钮创造一个监听事件
        self.bt.onclick.do(self.on_button_pressed)

        # 添加一个部件, 第一个参数是必须的
        container.append(self.lbl)
        container.append(self.bt)

        # 返回到根部件
        return container

    # 监听事件
    def on_button_pressed(self, widget):
        self.lbl.set_text('Button pressed!')
        self.bt.set_text('Hi!')

#开启服务器
start(MyApp)
```

为了能够看到效果并交互, 打开你最新的浏览器并打开"http://127.0.0.1:8081".
你可以改变URL地址参数来开始函数调用. 这在下面将会被提及.

在Android, Linux, Windows上测试过.
在Raspberry Pi 同样可以运行. 他允许你和你的Raspberry Pi在移动设备上远程交互.


FAQ
===
- **为什么我们需要这样的GUI库?**
Kivy, PyQT, and PyGObject在主机上都需要额外的代码,那意味着安装或编译大量的依赖. Remi只需要一个浏览器来展现你的GUI.

- **我需要精通HTML吗?**
不,这不需要, 你只需要在python中撰写代码.

- **它开源吗?**
当然! Remi基于Apache License. 更多细节请看``LICENSE`` 文件.

- **我需要某种网络服务器吗?**
不, 它已经包含在其中了.


Brief tutorial
===
Import Remi library and some other useful stuff.

```py
import remi.gui as gui
from remi import start, App
```

Subclass the `App` class and declare a `main` function that will be the entry point of the application. Inside the main function you have to <code>return</code> the root widget.

```py
class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        lbl = gui.Label("Hello world!", width=100, height=30)

        # return of the root widget
        return lbl
```

Outside the main class, start the application by calling the function `start` and passing the name of the class you declared previously as the parameter:

```py
# starts the webserver
start(MyApp)
```

Run the script. If it's all OK the GUI will be opened automatically in your browser, otherwise, you have to type in the address bar "http://127.0.0.1:8081".

You can customize optional parameters in the `start` call like:

```py
start(MyApp, address='127.0.0.1', port=8081, multiple_instance=False, enable_file_cache=True, update_interval=0.1, start_browser=True)
```

Parameters:
- address: network interface IP
- port: listen port
- multiple_instance: boolean, if True multiple clients that connect to your script has different App instances (identified by unique cookie session identifier)
- enable_file_cache: boolean, if True enable resource caching
- update_interval: GUI update interval in seconds. If zero, the update happens at each change. If zero, the App.idle method is not called.
- start_browser: boolean that defines if the browser should be opened automatically at startup
- standalone: boolean, indicates where to run the application as a standard Desktop application with its own window. If False, the interface is shown in a browser webpage.

Additional Parameters:
- username: for a basic HTTP authentication
- password: for a basic HTTP authentication
- certfile: SSL certificate filename
- keyfile: SSL key file
- ssl_version: authentication version (i.e. ssl.PROTOCOL_TLSv1_2). If None disables SSL encryption

All widgets constructors accept two standards**kwargs that are:
- width: can be expressed as int (and is interpreted as a pixel) or as str (and you can specify the measuring unit like '10%')
- height: can be expressed as int (and is interpreted as a pixel) or as str (and you can specify the measuring unit like '10%')


Events and callbacks
===
Widgets expose a set of events that happen during user interaction.
Such events are a convenient way to define the application behavior.
Each widget has its own callbacks, depending on the type of user interaction it allows.
The specific callbacks for the widgets will be illustrated later.

In order to register a function as an event listener you have to call a function like eventname.do (i.e. onclick.do) passing as parameters the callback that will manage the event.
Follows an example:

```py
import remi.gui as gui
from remi import start, App

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=120, height=100)
        self.lbl = gui.Label('Hello world!')
        self.bt = gui.Button('Press me!')

        # setting the listener for the onclick event of the button
        self.bt.onclick.do(self.on_button_pressed)

        # appending a widget to another, the first argument is a string key
        container.append(self.lbl)
        container.append(self.bt)

        # returning the root widget
        return container

    # listener function
    def on_button_pressed(self, widget):
        self.lbl.set_text('Button pressed!')
        self.bt.set_text('Hi!')

# starts the web server
start(MyApp)
```

In the shown example *self.bt.onclick.do(self.on_button_pressed)* registers the self's *on_button_pressed* function as a listener for the event *onclick* exposed by the Button widget.
Simple, easy.

Listener's callbacks will receive the emitter's instance firstly, then all other parameters provided by the specific event.


Besides the standard event registration (as aforementioned), it is possible to pass user parameters to listener functions. This can be achieves appending parameters to the *do* function call.

```py
import remi.gui as gui
from remi import start, App

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=120, height=100)
        self.lbl = gui.Label('Hello world!')
        self.bt = gui.Button('Hello name!')
        self.bt2 = gui.Button('Hello name surname!')

        # setting the listener for the onclick event of the buttons
        self.bt.onclick.do(self.on_button_pressed, "Name")
        self.bt2.onclick.do(self.on_button_pressed, "Name", "Surname")

        # appending a widget to another
        container.append(self.lbl)
        container.append(self.bt)
        container.append(self.bt2)

        # returning the root widget
        return container

    # listener function
    def on_button_pressed(self, widget, name='', surname=''):
        self.lbl.set_text('Button pressed!')
        widget.set_text('Hello ' + name + ' ' + surname)

# starts the web server
start(MyApp)
```

This allows great flexibility, getting different behaviors with the same event listener definition.


HTML Attribute accessibility
===
Sometimes it is required to access Widget's HTML representation in order to manipulate HTML attributes.
The library allows accessing this information easily.

A simple example: It is the case where you would like to add a hover text to a widget. This can be achieved by the *title* attribute of an HTML tag.
In order to do this:

```py
    widget_instance.attributes['title'] = 'Your title content'
```

A special case of HTML attribute is the *style*.
The style attributes can be altered in this way:

```py
    widget_instance.style['color'] = 'red'
```

The assignment of a new attribute automatically creates it.

For a reference list of HTML attributes, you can refer to https://www.w3schools.com/tags/ref_attributes.asp

For a reference list of style attributes, you can refer to https://www.w3schools.com/cssref/default.asp

Take care about internally used attributes. These are:
- **class**: It is used to store the Widget class name for styling purpose
- **id**: It is used to store the instance id of the widget for callback management


Remote access
===
If you are using your REMI app remotely, with a DNS and behind a firewall, you can specify special parameters in the `start` call:
- **port**: HTTP server port. Don't forget to NAT this port on your router;

```py
start(MyApp, address='0.0.0.0', port=8081)
```


Standalone Execution
===
I suggest using the browser as a standard interface window.

However, you can avoid using the browser.
This can be simply obtained joining REMI and [PyWebView](https://github.com/r0x0r/pywebview).
Here is an example about this [standalone_app.py](https://github.com/dddomodossola/remi/blob/development/examples/standalone_app.py).

**Be aware that PyWebView uses qt, gtk and so on to create the window. An outdated version of these libraries can cause UI problems. If you experience UI issues, update these libraries, or better avoid standalone execution.**


Authentication
===
In order to limit remote access to your interface, you can define a username and password. It consists of a simple authentication process.
Just define the parameters **username** and **password** in the start call:
```py
start(MyApp, username='myusername', password='mypassword')
```


Styling
===
In order to define a new style for your app, you have to do the following.
Create a *res* folder and pass it to your App class constructor:
```python
class MyApp(App):
    def __init__(self, *args):
        res_path = os.path.join(os.path.dirname(__file__), 'res')
        super(MyApp, self).__init__(*args, static_file_path={'res':res_path})
```

Copy the standard style.css file from the remi folder and paste it inside your *res* folder. Edit it in order to customize.
This way the standard *style.css* file gets overridden by the one you created.


Compatibility
===
Remi is made to be compatible from Python2.7 to Python3.X. Please notify compatibility issues.


安全
===
Remi应作为标准桌面GUI框架
图书馆自身不带有安全策略，因此建议不要将其数据库公开与不安全的公用网络中。

从外部加载数据时，留意在直接显示内容之前保护应用程序免受潜在的javascript注入。



贡献者
===
感谢您与我们合作，让Remi变得更好！

开源的真正力量来源于贡献者。 请自由地参与这个项目， 并且考虑将你自己加入 [contributors list](doc/contributors.md).
我知道GitHub已经为我们提供了贡献者名单， 但我觉得我应该提到这些提供帮助的贡献者。

<a href="https://github.com/dddomodossola/remi/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=dddomodossola/remi" >
</a>


使用Remi的项目
===
[PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI): Launched in 2018 Actively developed and supported. Supports tkinter, Qt, WxPython, Remi (in browser). Create custom layout GUI's simply. Python 2.7 & 3 Support. 100+ Demo programs & Cookbook for rapid start. Extensive documentation.

[App Template For REMI](https://github.com/cheak1974/remi-app-template): A really well written template for multiview applications.

[Web based dynamic reconfigure for ROS robots](https://github.com/awesomebytes/web_dyn_reconf)

[razmq](https://github.com/MrYsLab/razmq)

[Espresso-ARM](http://hallee.github.io/espresso-arm/)

[PiPresents](https://github.com/KenT2/pipresents-gapless)

[The Python Banyan Framework](https://github.com/MrYsLab/python_banyan)

[LightShowPi show manager](https://github.com/Chrispizzi75/ShowManager)

[rElectrum](https://github.com/emanuelelaface/rElectrum): A powerful promising Electrum wallet manager for safe transactions.

Other Implementations
===
Listed here are other implementations of this library:
- [**cremi**](https://github.com/cyberpro4/cremi): (WIP) developed for your C++ projects by [Claudio Cannatà](https://github.com/cyberpro4).
