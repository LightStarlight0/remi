"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

""" 这个例子展现了一下几种部件的使用方法:
    Widget.append(widget, key) : 添加部件到一个容器
    Widget.remove_child(widget) : 从某个容器中移除某个部件
    Widget.empty() : 移除容器中的所有部件
"""

import remi.gui as gui
from remi import start, App
import os


class MyApp(App):
    def main(self):
        main_container = gui.VBox()
        lbl = gui.Label("Press the buttons to add or remove labels")
        #创建按钮
        bt_add = gui.Button("add a label", style={'margin': '3px'})
        #按钮事件
        bt_add.onclick.do(self.on_add_a_label_pressed)
        
        bt_remove = gui.Button("remove a label", style={'margin': '3px', 'background-color': 'orange'})
        bt_remove.onclick.do(self.on_remove_a_label_pressed)
        
        bt_empty = gui.Button("empty", style={'margin': '3px', 'background-color': 'red'})
        bt_empty.onclick.do(self.on_empty_pressed)
        
        self.lbls_container = gui.HBox()
        main_container.append([lbl, bt_add, bt_remove, bt_empty, self.lbls_container])

        # 返回根部件
        return main_container

    def on_add_a_label_pressed(self, emitter):
        # 创建一个标签，并让其拥有一个特殊id
        key = str(len(self.lbls_container.children))
        lbl = gui.Label("label id: " + key, style={'border': '1px solid gray', 'margin': '3px'})
        self.lbls_container.append(lbl, key)

    def on_remove_a_label_pressed(self, emitter):
        # 如果没有这个部件，那就退出函数
        if len(self.lbls_container.children) < 1:
            return
        key = str(len(self.lbls_container.children) - 1)
        self.lbls_container.remove_child(self.lbls_container.children[key])

    def on_empty_pressed(self, emitter):
        self.lbls_container.empty()


if __name__ == "__main__":
    start(MyApp)
