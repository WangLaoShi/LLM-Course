# LLM-Course

[大模型系列课程仓库](https://github.com/WangLaoShi/LLM-Course)

## 使用本项目的 2 种方式

1. 如果无法很顺利的打开 [GitHub](https://www.github.com) 网站，可以使用老师提供的离线包来操作
2. 如果你竟然可以上的去 [GitHub](https://www.github.com) 网站，推荐使用检出项目的方式，这样可以保持项目一直可以跟老师的项目进行同步（当然这涉及到一些 `git` 的基础操作了，是另外的知识）。

### 打开本地项目的方法（方式 1）

### 从 GitHub 检出项目的方法(方式 2）

1. 打开项目，找到项目的检出地址

   ![LawsonShot20240724PM8S224iIB@2x](https://oss.images.shujudaka.com/uPic/LawsonShot20240724PM8S224iIB@2x.png)
2. 打开 PyCharm 或者你喜欢的 IDE，检出项目

   ![LawsonShot20240724PMk9cCo4Nd@2x](https://oss.images.shujudaka.com/uPic/LawsonShot20240724PMk9cCo4Nd@2x.png)

## 配置环境

在使用的 IDE 例如 PyCharm 中配置你的 Python 环境（在这里强烈建议新建一个）

![LawsonShot20240724PMEHsHCyqo@2x](https://oss.images.shujudaka.com/uPic/LawsonShot20240724PMEHsHCyqo@2x.png)

![LawsonShot20240724PMiPMCX7M0@2x](https://oss.images.shujudaka.com/uPic/LawsonShot20240724PMiPMCX7M0@2x.png)

![XkbcF6](https://oss.images.shujudaka.com/uPic/XkbcF6.png)

## 激活环境

到现在，我们已经创建好了虚拟环境，接下来我们需要激活这个环境，你可以按照下面的方式激活你的环境，参考[这里](https://docs.python.org/3/library/venv.html#how-venvs-work)

### Windows

```shell
venv\Scripts\activate
```

### Mac

```shell
source venv/bin/activate
```

> 请注意，venv 是你创建的虚拟环境的名字，如果你的虚拟环境名字不是 venv，请替换成你的虚拟环境名字
> 
> ![LawsonShot20240724PMAjyMW8Xa@2x](https://oss.images.shujudaka.com/uPic/LawsonShot20240724PMAjyMW8Xa@2x.png)


### 测试环境是否激活成功

```shell
python -V
```

## 安装依赖

### ChatGPT OpenAI
    
```shell
pip install openai
```  

### 文心一言

```shell
pip install requests
```


## 环境申请

### ChatGPT的API申请

1. 首先你要有一个ChatGPT的账号，怎么有呢？自己注册或者买一个 😄。

2. 第二来到下面这个页面创建你的key,打开[网址](https://platform.openai.com/api-keys)

3. ![LawsonShot20240724PMAjyMW8Xa@2x](https://oss.images.shujudaka.com/uPic/LawsonShot20240724PMAjyMW8Xa@2x.png)
4. 创建新的key，然后复制你的key，保存好，这个key是你调用ChatGPT的API的凭证
5. 可以参考 `ChatGPT.py` 文件中的代码，将你的key填入到代码中，可以运行代码测试一下是否成功
   * 5.1 可以在命令行中 `python ChatGPT.py` 运行代码
   * 5.2 也可以在 PyCharm 中运行代码，这样可以更好的调试代码 

### 文心一言的API申请

#### 步骤一. 创建千帆应用

1. 登录百度智能云千帆控制台。

请您注册并登录[百度智能云千帆控制台](https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application) 。

**注意**为保障服务稳定运行，账户最好不处于欠费状态。

2. 创建千帆应用

进入[控制台创建应用](https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application/create) 。如果已有应用，此步骤可跳过。

3. 创建应用后，获取AppID、API Key、Secret Key。

![aUbEs7](https://oss.images.shujudaka.com/uPic/aUbEs7.png)

![LawsonShot20240724PMzlAJ6o7D@2x](https://oss.images.shujudaka.com/uPic/LawsonShot20240724PMzlAJ6o7D@2x.png)

![LawsonShot20240724PMqw5ZseYh@2x](https://oss.images.shujudaka.com/uPic/LawsonShot20240724PMqw5ZseYh@2x.png)

4. 调用API接口

调用千帆提供的相关接口，如ERNIE-Bot等，详见[API列表](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu)。

![LawsonShot20240724PMhE2j2M0t@2x](https://oss.images.shujudaka.com/uPic/LawsonShot20240724PMhE2j2M0t@2x.png)

![LawsonShot20240724PMejdGDezt@2x](https://oss.images.shujudaka.com/uPic/LawsonShot20240724PMejdGDezt@2x.png)

![LawsonShot20240724PMtk40Z47e@2x](https://oss.images.shujudaka.com/uPic/LawsonShot20240724PMtk40Z47e@2x.png)

5. 可以参考 `WenXin.py` 文件中的代码，将你的key填入到代码中，可以运行代码测试一下是否成功(我这里用的是 HTTP 请求，你也可以使用 SDK)
   * 5.1 可以在命令行中 `python WenXin.py` 运行代码
   * 5.2 也可以在 PyCharm 中运行代码，这样可以更好的调试代码 