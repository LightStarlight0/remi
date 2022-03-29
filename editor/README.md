
# *用来编辑Remi图形界面的WYSIWYG编辑器*

介绍
===
什么是Remi？
**适用于您的应用程序的python图形界面库独立平台**

[![加入聊天 https://gitter.im/dddomodossola/remi](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/dddomodossola/remi?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

RemI是一个易于使用的python图形界面库。它在浏览器中显示并且可以远程访问。这会删除特定平台的依赖性并让您轻松地在 Python 中开发跨平台应用程序！
[更多信息 https://github.com/dddomodossola/remi](https://github.com/dddomodossola/remi)

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/preview.png "Editor window")

**editor_app** 允许您在易于使用的环境中以图形方式设计 gui 界面。
你可以在屏幕左侧的小组件集合添加你需要添加到界面中的小组件。
选择小部件，您必须填写分配小组件所需的一些字段。 除了构造函数参数之外，还需要一些附加信息：
- **变量名**：用于生成应用程序代码的标识符；
- **重载基类** 标示： 定义了变量是否必须是一个新类的实例，该类将重载基类。

在屏幕的右侧，可以看到小组件的参数。它由一组html和css属性组成。
可以通过点击来选定小组件。 选择小部件后，可以通过属性面板对其进行自定义。

小工具可以被添加到另一个中。目前有三种类型的容器可用。
- **Widget**: 一个通用的容器，允许绝对定位。
- **HBox, VBox**: 两种布局都会自动生成内部小组件。

通过使用Widget容器，你可以手动调整大小和拖动Widget。

HBox和VBox容器 **不支持**手动拖动和调整小组件的大小。但小组件可以通过右边的属性面板调整大小。

一旦你的界面准备好了，你可以保存你的应用程序。它将被**直接导出到python代码中**。
你的应用程序**可以重新载入编辑**。


让我们来逐步举例！😊
===
现在，让我们来写第一个*Hello world*应用

首先我们必须从左侧toolbox中选择Widget部件。这会成为我们的主窗口。在显示的对话框中我们要为变量去一个名称。我们可以叫它mainContainer。

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/new_container.png "New Widget container")


接下来，只要将小部件(widget)加入到到eidtor中，我们就可以拖动并调整其大小。

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/drag_resize_container.png "Drag and resize container")

现在，从左边toolbox中选择一个Lable widget用来存储我们的*Hello world*信息。让我们再次为这个部件取名字。

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/new_label.png "Add new label")


现在，我们可以点击选中这个标签(lable)来拖动和调整它的大小

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/drag_resize_label.png "Drag and resize label")

我们显然会需要用到一个Button。让我们点击选择一种container来将按钮(button)添加到mainContainer中。之后，在左侧toolbox中选择the Button widget。确认并输入变量名称。

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/new_button.png "Add new button")


点击按钮部件来拖动并更改大小

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/drag_resize_button.png "Drag and resize button")

恭喜你！所有需要的部件已经添加好了。😉 <br>现在，我们必须将*onclick*事件从按钮连接到一个监听器(listener)上。在我们的例子中，监听器将是主应用程序。

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/connect_button.png "Connect button onclick event to App")


全部完成之后，通过上面的菜单保存项目。

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/save_menu.png "Save menu")


选择目标文件夹，输入这个app的名称并确认。

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/save_dialog.png "Save dialog")

我们现在可以编辑代码*Hello World*的啦 

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/edit_hello_message.png "Edit the code to say Hello World")

运行这个程序……<br>你好，世界！！

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/hello.png "Run the App")


Project configuration
===
