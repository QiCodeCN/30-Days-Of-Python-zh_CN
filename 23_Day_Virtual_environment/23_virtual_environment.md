
[<< Day 22](../22_Day_Web_scraping/22_web_scraping.md) | [Day 24 >>](../24_Day_Statistics/24_statistics.md)

- [📘 Day 23](#-day-23)
  - [虚拟环境](#虚拟环境设置)
  - [💻 第23天练习](#-第23天练习)

# 📘 Day 23

## 虚拟环境设置

从项目开始，最好有一个虚拟环境。虚拟环境可以帮助我们创建一个隔离或分离的环境。这将帮助我们避免项目间依赖关系的冲突。如果你在你的终端上执行pip freeze 你会看到你的计算机上所有已安装的包。如果我们使用virtualenv，我们将只访问特定于该项目的包。

安装 virtualenv 包环境语法命令

```sh
pip install virtualenv
Collecting virtualenv
...
Successfully installed distlib-0.3.6 filelock-3.9.0 virtualenv-20.19.0
```

让我们实际操作下，首先在 30-Days-Of-Python-zh_CN 文件夹中创建 flask_project 文件夹。

安装 virtualenv 包后，进入你的项目文件夹，通过以下命令创建一个虚拟env:

在 Mac/Linux 上:
```sh
..30-Days-Of-Python-zh_CN\flask_project\$ virtualenv venv

```

在 Windows 上:
```sh
..30-Days-Of-Python-zh_CN\flask_project> python -m venv venv
```

笔者比较新项目中虚拟环境命名为 venv，但其实这个名字可以随意命名。让我们检查一下是否创建成功了，用命令 ls (或windows命令提示符的dir)查看。
I prefer to call the new project venv, but feel free to name it differently. Let us check if the the venv was created by using ls (or dir for windows command prompt) command.

```sh
..\30-Days-Of-Python-zh_CN\flask_project> dir
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2023/2/26     15:26                venv
```

继续，让我们通过在项目文件夹中写入以下命令来激活虚拟环境。

在 Mac/Linux 上:
```sh
..\30-Days-Of-Python-zh_CN\flask_project$ source venv/bin/activate
```

在 Windows 中激活虚拟环境可能依赖 Windows Power shell 和 git bash。

在 Windows Power Shell 上:
```sh
..\30-Days-Of-Python-zh_CN\flask_project> venv\Scripts\activate
```

在 Windows Git bash:
```sh
..\30-Days-Of-Python-zh_CN\flask_project> venv\Scripts\. activate
```

在激活虚拟环境之后，您的项目目录将使用venv独立环境。请参阅下面的示例。

```sh
(venv) PS D:\QiCode\30-Days-Of-Python-zh_CN\flask_project>
```

现在，让我们通过 `pip freeze` 检查这个项目中可用的包。结果是，你不会看到任何包裹，很干净。

我们利用这个权限的虚拟环境项目创建一个小的flask项目，因此我们先安装下 flask 依赖包。

```sh
(venv) ..30-Days-Of-Python-zh_CN\flask_project> pip install Flask
```

现在, 让我们再次查看下安装的列表:

```sh
(venv) ..\30-Days-Of-Python-zh_CN\flask_project> pip freeze
click==8.1.3
colorama==0.4.6
Flask==2.2.3
importlib-metadata==6.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
Werkzeug==2.2.3
zipp==3.15.0
```

When you finish you should dactivate active project using _deactivate_.
当你不在使用此项目时，你可以使用 _deactivate_ 停用项目虚拟环境。

```sh
(venv) ..\30-Days-Of-Python-zh_CN\flask_project> deactivate
```

以上就是一个项目如何创建和使用虚拟环境的知识点。其实除了 `virtualenv` 还有个不错的虚拟环境管理 `anaconda` 非常值得体验。
总之在正式编程的项目中，非常建议使用虚拟环境，这样在项目共享，多项目开发，打包使用中就会减少很多依赖和冲突的问题。

## 💻 第23天练习

1. 基于上面给出的示例，用虚拟环境创建一个项目目录。
2. 查找一些关于 anaconda 知识，用它尝试做一个虚拟环境项目。

🎉 CONGRATULATIONS ! 🎉

[<< Day 22](../22_Day_Web_scraping/22_web_scraping.md) | [Day 24 >>](../24_Day_Statistics/24_statistics.md)
