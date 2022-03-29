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

""" 这个例子展现了运用App.close()关闭服务器
    如果有多个连接的客户端, 服务器会关闭所有连接.
"""

import remi.gui as gui
from remi import start, App


class MyApp(App):
    def main(self, name='world'):
        # margin 0px auto 允许让app显示在屏幕中央
        wid = gui.VBox(width=300, height=200, margin='0px auto')

        bt = gui.Button('Close App', width=200, height=30)
        bt.style['margin'] = 'auto 50px'
        bt.style['background-color'] = 'red'

        bt.onclick.do(self.on_button_pressed)

        wid.append(bt)
        return wid

    #监听事件
    def on_button_pressed(self, _):
        self.close()  # 关闭服务器

    def on_close(self):
        #加载App.on_close允许在关闭前进行一些操作
        print("I'm going to be closed.")
        super(MyApp, self).on_close()#关闭


if __name__ == "__main__":
    start(MyApp)
