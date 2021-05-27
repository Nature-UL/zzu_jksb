# 郑州大学健康上报
![img](https://img.shields.io/github/license/21wang12/zzu_jksb)
## 为什么造轮子？
网上找了一些自动打卡的程序，一种是采用模拟点击的方式进行打卡，另一种虽然也是模拟`http`请求，但是引入了一堆打卡不相关的函数库，使用起来一点也不优雅。本项目旨在提供优雅的打卡方式，引入了最少的函数库，程序配置简单，运行速度快。

## 环境
+ `python3`
+ `requests`
## 用法：
需要确保电脑安装`python`以及`python`的`requests`模块：
1. 如果你已安装`python`，请看第二步。[点击此处](https://www.baidu.com/link?url=78fS9ExFcc-uQCdfKhT-l7XpsRKIysDEDZag9AaOcqmJw-JKa0fOdfaQWjl7DH_UoQsTHpkPvAjuRhKlUqj59w3gIuRFN26iBmgFt7aoGz7&wd=&eqid=fca2268e0003b78f0000000360afad5e)查看安装`python`的教程
2. 请打开命令行使用如下命令安装`requests`模块
```bash
pip install requests
```
3. 安装好之后，将`jksb.py`下载下来
4. 用记事本打开并修改`jksb.py`的第五行第六行，修改为自己的**账户名**和**密码**，修改完之后保存。
5. 打开命令行，运行下列命令即可打卡。如果你的文件未放在`D`盘下，请自动更改为文件所在路径。
```bash
python D:\jksb.py
``` 

## Q&A
+ 如何打开命令行？
  + 利用键盘的组合按键`win+r`，在弹出的窗口输入`cmd`并按下回车即可打开命令行

+ 如何查看自己是否安装了`python`?
  + 打开命令行，输入下面语句，如果返回了python的版本，说明已经安装
  ```bash
  python --version
  ```

+ 如何每日执行此程序？
  + 需要你有一台Linux服务器。服务器按照此教程：[Linux设置定时任务](https://segmentfault.com/a/1190000023186565#:~:text=%E5%9C%A8Linux%20%E4%B8%AD%EF%BC%8C%E5%8F%AF%E4%BB%A5%E4%BD%BF%E7%94%A8,%E5%86%99%E5%85%A5%E4%B8%80%E4%B8%AAcrontab%20%E6%96%87%E4%BB%B6%E3%80%82)进行配置
  + 如果没有linux服务器，在windows上定时任务可以参考[windows定时执行python](https://www.jianshu.com/p/43676346b0be)
