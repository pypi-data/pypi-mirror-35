运行环境
===
## 安装python
1、首先，从Python的官方[python.org](https://www.python.org/)网站下载[3.6.5](https://www.python.org/downloads/release/python-365/)版本       
2、运行下载的MSI安装包，在选择安装组件的一步时，勾上所有的组件,特别要注意选上pip和Add python.exe to Path，然后一路点“Next”即可完成安装      
3、默认会安装到C:\PythonXX目录下，然后打开cmd窗口，敲入`python`后出现`>>>`提示符就表示安装成功      
    
    如果出现`‘python’不是内部或外部命令，也不是可运行的程序或批处理文件。`
    很有可能因为Windows会根据一个Path的环境变量设定的路径去查找python.exe，如果没找到，就会报错。可能是安装时漏掉了勾选Add python.exe to Path，
    那就要手动把python.exe所在的路径C:\PythonXX添加到Path中。
    如果不知道怎么修改环境变量，建议把Python安装程序重新运行一遍，勾上Add python.exe to Path。
    
###### 查看python文档： [Python文档下载地址](https://www.python.org/doc/)

## 安装项目环境
1、cd 到项目路径，打开gitbash，执行`pip install dafeiauto`
2、执行`dafeiauto init 项目名称`

## 运行项目环境
2、打开项目，cd到项目目录，在ide内执行`pip install -r requirements.txt`
【个别安装包有可能会安装失败，调用的时候需要手动安装】
3、成功后，运行__main__.py

## 如需要添加新的安装包
1、本机执行'pip install xxxx'
2、然后cd 项目路径 有requirements.txt的路径，执行`pip freeze > requirements.txt`生成包管理文件
