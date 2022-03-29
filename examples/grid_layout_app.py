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

"""这个展示了GridBox方式的布局.
    grid布局允许以一种灵活的方式定义布局
    使用GridBox.define_grid，传递一个二维可迭代对象作为参数。
    被定义在grid中的每个元素, 是一个关键部分对于GridBox.append函数
    在这个例子中, 模型是一些字符串, 每个字符都被用来当作key.
    一个key可以在定义的模型中出现多次, 使组件覆盖更大的空间.
    每个在布局中的纵列和横行的大小都可以通过GridBox.style被定义,
     style参数是类似这样的 
     {'grid-template-columns':'10% 90%', 'grid-template-rows':'10% 90%'}.
"""

import remi.gui as gui
from remi import start, App
import os


class MyApp(App):
    def main(self):
        #创建一个grid格式的容器
        main_container = gui.GridBox(width='100%', height='100%', style={'margin':'0px auto'})
        
        label = gui.Label('This is a label')
        label.style['background-color'] = 'lightgreen'
        
        button = gui.Button('Change layout', height='100%')
        button.onclick.do(self.redefine_grid, main_container)
        
        text = gui.TextInput()

        
        main_container.set_from_asciiart("""
            |label |button                      |
            |label |text                        |
            |label |text                        |
            |label |text                        |
            |label |text                        |
            """, 10, 10)

        main_container.append({'label':label, 'button':button, 'text':text})

        # returning the root widget
        return main_container
    
    def redefine_grid(self, emitter, container):
        #redefining grid layout
        container.define_grid([ ['text','label','button'],['text','.','.']])
        container.style.update({'grid-template-columns':'33% 33% 33%', 'grid-template-rows':'50% 50%'})
        container.set_column_gap("0%")
        container.set_row_gap("0%")
        emitter.set_text("Done")


if __name__ == "__main__":
    start(MyApp, debug=True)
