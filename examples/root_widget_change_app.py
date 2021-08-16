"""
根据 Apache 许可，版本 2.0（“许可”）获得许可；
除非遵守许可，否则您不得使用此文件。
您可以在以下网址获取许可证副本
http://www.apache.org/licenses/LICENSE-2.0
除非适用法律要求或书面同意，否则软件
根据许可证分发的分发是按“原样”的基础分发的，
不作任何形式的明示或暗示的保证或条件。
请参阅许可证以了解管理权限的特定语言和许可证下的限制。
"""

""" 
这个案例展示了如何更改App的根部件。这使得我们能模仿页面更改行为。
它是由 App.set_root_widget(mywidget) 方法完成的。

"""

import remi.gui as gui
from remi import start, App
import os


class MyApp(App):
    def __init__(self, *args):
        res_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res')
        # static_file_path 可以是一个允许定义的字符串数组
        # 多个资源路径放置资源
        super(MyApp, self).__init__(*args, static_file_path=res_path)

    def main(self):
        # 创建两个要交替显示的“页面”小部件
        lbl = gui.Label("Page 2. Press the button to change the page.", style={'font-size': '20px'})
        bt2 = gui.Button("change page")
        page2 = gui.HBox(children=[lbl, bt2], style={'margin': '0px auto', 'background-color': 'lightgray'})

        lbl = gui.Label("Page 1. Press the button to change the page.", style={'font-size': '20px'})
        bt1 = gui.Button("change page")
        page1 = gui.VBox(children=[lbl, bt1],
                         style={'width': '300px', 'height': '200px', 'margin': '0px auto', 'background-color': 'white'})

        bt1.onclick.do(self.set_different_root_widget, page2)
        bt2.onclick.do(self.set_different_root_widget, page1)

        # 返回根部件
        return page1

    def set_different_root_widget(self, emitter, page_to_be_shown):
        self.set_root_widget(page_to_be_shown)


if __name__ == "__main__":
    # 启动网络服务器
    start(MyApp, address='0.0.0.0', port=0, start_browser=True, username=None, password=None)
