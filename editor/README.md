
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
你可以在屏幕左侧的小部件集合添加你需要添加到界面中的小组件。
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


A step by step example
===
Now, let's create our first *Hello World* application.

First of all we have to select from the left side toolbox the Widget component. It will be our main window.
In the shown dialog we have to write a name for the variable. We will call it *mainContainer*.

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/new_container.png "New Widget container")


Then, once the widget is added to the editor, you can drag and resize it.

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/drag_resize_container.png "Drag and resize container")


Now, from the left side toolbox we select a Label widget that will contain our *Hello World* message.
Again, we have to type the variable name for this widget.

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/new_label.png "Add new label")


Then, we can select the label by clicking on it in order to drag and resize.

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/drag_resize_label.png "Drag and resize label")


We need for sure a Button. Since we have to add it to the mainContainer, we have to select the container by clicking on it.
After that, click on the Button widget in the left side toolbox. 
Type the variable name and confirm.

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/new_button.png "Add new button")


Select the Button widget by clicking on it and drag and resize.

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/drag_resize_button.png "Drag and resize button")


Now, all the required widgets are added. We have to connect the *onclick* event from the button to a listener, in our case the listener will be the main App.

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/connect_button.png "Connect button onclick event to App")


All it's done, save the project by the upper menu bar.

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/save_menu.png "Save menu")


Select the destination folder. Type the app filename and confirm.

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/save_dialog.png "Save dialog")


We can now edit the code to say the *Hello World* message.

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/edit_hello_message.png "Edit the code to say Hello World")


Run the application and... Say Hello!

![Alt text](https://raw.githubusercontent.com/dddomodossola/remi/master/editor/res/tutorial_images/hello.png "Run the App")


Project configuration
===
