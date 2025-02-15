# Notebooks with remi

## Install

在一个虚拟环境中

`pip install jupyterlab, jupyter-server-proxy`

jupyter-server-proxy 是我们在 jupyter lab 中使用的代理

Pythonnet 需要Visual Studio Build Tools 2019，并需要在Windows上安装github

`pip install git+https://github.com/pythonnet/pythonnet.git`

`pip install pywebview`

## Notebooks

* JlabRemiHelloWorld.ipynb => the "HelloWorld" application
* JlabRemiWidgets_Overview.ipynb => the remi widget overview app
* JlabRemiEditor.ipynb => the remi 'IDE'

## Using...

### 创建一个代理类

* 8085 应该是本地的REMI端口

```python
remiport = 8085
# overload _net_interface_ip, _overload and _process_all
class MyApp(Editor):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args,)
            
    def _net_interface_ip(self):
        # used for the ws(s) address
        ip = super()._net_interface_ip()
        return ip + f"/proxy/{remiport}"
    
    def _overload(self, data, **kwargs):
        # every content sent back to a client needs /res: to be overloaded and replaced by /proxy/8085/res: (holds for editor_resources and the like)
        if "filename" in kwargs:
            filename = kwargs['filename']
        else:
            return data
        paths = self.all_paths()
        for pattern in paths.keys():
            if ( filename.endswith(".css") or filename.endswith(".html") or filename.endswith(".js") or filename.endswith("internal") ):
                if type(data) == str:
                    data = re.sub(f"/{pattern}:", f"/proxy/{remiport}/{pattern}:", data)
                else:
                    data = re.sub(f"/{pattern}:", f"/proxy/{remiport}/{pattern}:", data.decode()).encode()
        return data
 
```

* 像往常一样START

```python
myRemi = Thread(target=start, 
                         args=(MyApp,),
                         kwargs={'address':'127.0.0.1', 
                                 'port':{remiport}, 
                                 'multiple_instance':True,
                                 'enable_file_cache':True, 
                                 'update_interval':0.5, 
                                 'start_browser':False})
```
如果没有显示过载, remi 表现正常

## 免责声明

只有 jupyter-server-proxy 测试了, 但是其他proxy应该也可以使用
