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
"""网页弹出提示的例程
"""

import remi.gui as gui
from remi import start, App


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        wid = gui.VBox(width=300, height=200, margin='0px auto')
        self.lbl = gui.Label('Press the button', width='80%', height='50%')
        self.lbl.style['margin'] = 'auto'
        self.bt = gui.Button('Press me!', width=200, height=30)
        self.bt.style['margin'] = 'auto 50px'

        self.bt.onclick.do(self.on_button_pressed)

        wid.append(self.lbl)
        wid.append(self.bt)

        return wid

    # listener function
    def on_button_pressed(self, widget):
        self.lbl.set_text('A notification message should appear.')#修改标签内容
        self.bt.set_text('Hi!')#修改按钮文本内容
        self.notification_message("Message title", "Hello world!", "")#弹出提示


if __name__ == "__main__":
    #可选的:start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1,
    start(MyApp, debug=True, address='0.0.0.0', port=0, )
