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

""" HelloWorld例程
"""

import remi.gui as gui
from remi import start, App


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        #添加一个宽为300高为200的网页窗口
        wid = gui.VBox(width=300, height=200)

        #创建一个文本框,style是{"white-space":"pre"}，高为50%，宽为80%
        self.lbl = gui.Label('Hello\n test', width='80%', height='50%', style={"white-space":"pre"})

        #一个简单交互的按钮
        bt = gui.Button('Press me!', width=200, height=30)

        #建立这个按钮的点击事件
        bt.onclick.do(self.on_button_pressed)
        
        #添加按钮到容器
        wid.append(self.lbl)
        wid.append(bt)

        # 返回根部件
        return wid

    # 按钮的点击事件
    def on_button_pressed(self, emitter):
        self.lbl.set_text('Hello World!')
        

if __name__ == "__main__":
    # 开启服务器，在IP0.0.0.0,端口为随机
    start(MyApp, debug=True, address='0.0.0.0', port=0)
