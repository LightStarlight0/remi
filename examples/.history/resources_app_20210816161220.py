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

import remi.gui as gui
from remi import start, App
import os

class MyApp(App):
    def __init__(self, *args):
        res_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res')
        #将这里的资源文件夹声明为一个字典，参数为*static_file_path*
        super(MyApp, self).__init__(*args, static_file_path={'my_res_folder':res_path})

    def main(self):
        #您可以从资源文件声明中加载图像，如/key:filename
        #您必须使用参数 *static_file_path* 字典在 App.__init__ 函数中声明资源文件夹
        resource_image = gui.Image("/my_res_folder:mine.png", width="30", height="30")

        #您可以使用函数 *load_resource* 通过其路径和文件名直接加载图像
        local_image = gui.Image(gui.load_resource("./res/mine.png"), width="30", height="30")

        standard_widget = gui.Widget(width="30", height="30", style={'background-repeat':'no-repeat'})

        standard_widget2 = gui.Widget(width="30", height="30", style={'background-repeat':'no-repeat'})

        #像 *background-image* 这样的样式图像属性需要用 url('') 包裹文件名
        #  你可以使用函数 *to_uri* 
        standard_widget.style['background-image'] = gui.to_uri("/my_res_folder:mine.png")
        standard_widget2.style['background-image'] = gui.to_uri(gui.load_resource("./res/mine.png"))

        print(gui.to_uri("/my_res_folder:mine.png"))
        print(gui.to_uri(gui.load_resource("./res/mine.png")))
        main_container = gui.VBox(children=[resource_image, local_image, standard_widget, standard_widget2], width=200, height=300, style={'margin':'0px auto'})
        
        # 返回根部件
        return main_container


if __name__ == "__main__":
    # 启动网络服务器
    start(MyApp, address='0.0.0.0', port=0, start_browser=True, username=None, password=None)
