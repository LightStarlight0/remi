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
"""
这个例子展示了通过引用PIL的库实现对于图片的展示，支持打开保存图片
"""
import time
import io
import traceback
import PIL.Image

import remi.gui as gui
from remi import start, App
import remi


class PILImageViewverWidget(gui.Image):                                         #定义一个查看图片的组件
    def __init__(self, filename=None, **kwargs):                                #初始化组件,**kwargs可以看出是传入的size
        self.app_instance = None
        super(PILImageViewverWidget, self).__init__("/res:logo.png", **kwargs)
        self.frame_index = 0
        self._buf = None
        if filename:
            self.load(filename)

    def load(self, file_path_name):                                             #加载图片的函数,传入file_path_name即图片地址
        pil_image = PIL.Image.open(file_path_name)
        self._buf = io.BytesIO()
        pil_image.save(self._buf, format='png')

        self.refresh()

    def search_app_instance(self, node):                                       #搜索应用程序实例
        if issubclass(node.__class__, remi.server.App):
            return node
        if not hasattr(node, "get_parent"):
            return None
        return self.search_app_instance(node.get_parent()) 

    def refresh(self, *args):                                                  #刷新页面
        if self.app_instance==None:
            self.app_instance = self.search_app_instance(self)
            if self.app_instance==None:
                return
        self.frame_index = self.frame_index + 1
        self.app_instance.execute_javascript("""
            url = '/%(id)s/get_image_data?index=%(frame_index)s';
            
            xhr = null;
            xhr = new XMLHttpRequest();
            xhr.open('GET', url, true);
            xhr.responseType = 'blob'
            xhr.onload = function(e){
                urlCreator = window.URL || window.webkitURL;
                urlCreator.revokeObjectURL(document.getElementById('%(id)s').src);
                imageUrl = urlCreator.createObjectURL(this.response);
                document.getElementById('%(id)s').src = imageUrl;
            }
            xhr.send();
            """ % {'id': id(self), 'frame_index':self.frame_index})

    def get_image_data(self, index=0):
        try:
            self._buf.seek(0)
            headers = {'Content-type': 'image/png'}
            return [self._buf.read(), headers]
        except:
            print(traceback.format_exc())
        return None, None


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self, name='world'):
        #这些参数是宽度 - 高度 - 布局方向
        self.mainContainer = gui.Container(width=640, height=270, margin='0px auto')
        self.mainContainer.style['text-align'] = 'center'                           #居中显示            
        self.image_widget = PILImageViewverWidget(width=200, height=200)

        self.menu = gui.Menu(width=620, height=30)                                  #菜单组件
        m1 = gui.MenuItem('File', width=100, height=30)
        m11 = gui.MenuItem('Save', width=100, height=30)
        m12 = gui.MenuItem('Open', width=100, height=30)
        m12.onclick.do(self.menu_open_clicked)
        m111 = gui.MenuItem('Save', width=100, height=30)
        m111.onclick.do(self.menu_save_clicked)
        m112 = gui.MenuItem('Save as', width=100, height=30)
        m112.onclick.do(self.menu_saveas_clicked)

        self.menu.append(m1)                                                        #加入菜单组件
        m1.append(m11)
        m1.append(m12)
        m11.append(m111)
        m11.append(m112)

        self.mainContainer.append(self.menu)
        self.mainContainer.append(self.image_widget)

        # returning the root widget
        return self.mainContainer

    def menu_open_clicked(self, widget):
        self.fileselectionDialog = gui.FileSelectionDialog('File Selection Dialog', 'Select an image file', False, '.')#选择文件
        self.fileselectionDialog.confirm_value.do(                                   #选择成功
            self.on_image_file_selected)
        self.fileselectionDialog.cancel_dialog.do(                                   #取消
            self.on_dialog_cancel)
        self.fileselectionDialog.show(self)

    def menu_save_clicked(self, widget):
        pass
        
    def menu_saveas_clicked(self, widget):
        pass
        
    def on_image_file_selected(self, widget, file_list):
        if len(file_list) < 1:
            return
        self.image_widget.load(file_list[0])
        self.set_root_widget(self.mainContainer)
    
    def on_dialog_cancel(self, widget):
        self.set_root_widget(self.mainContainer)


if __name__ == "__main__":
    start(MyApp, address='0.0.0.0', port=0, start_browser=True)
