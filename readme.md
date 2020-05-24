## 情话一言 Telegram bot
这是为[情话箱](https://t.me/qinghua_box)频道开发的一言机器，基于本地数据库

### 开始使用
开始之前我已默认你已经有一台Linux服务器，并且已经安装了所有依赖包，这里以Ubuntu为例
```
sudo apt update
sudo apt dist-upgrade -y
sudo apt install python3 python3-pip nodejs npm redis php php-xml php-redis -y
pip3 install telethon numpy norm sklearn
npm i -g pm2 yarn
```

 * 打开telegram，登录账号，完成验证，目光聚集在左上角的搜索框  
 * 搜索创建机器人`@botfahter`，有个官方认证的符号，不要搞错了  
 * 进入botfather界面，点击底部的`/start`，开始创建机器人  
 * 输入`/start`后，会出现使用菜单的说明，创建一个新的机器人，点击蓝色字体/newbot  
 * 然后设置机器人的名称，这个名称可以被公开搜索到，所以名字不能重复  
 * 接着创建机器人的username，这个机器人的username必须以bot结尾，这个需要注意一下  
 * 最后，创建成功后，会有这个机器人的聊天窗口，以及想要调用这个机器人的API接口token，复制这个token  
 * 登录你的服务器，执行`git clone https://github.com/qinghua-osc/yiyan.git ;cd yiyan; mv env.example .env`  
 * 接下来执行`vim .env`编辑配置文件，将其中的xxxx替换为你刚刚复制的token  
 * 修改完毕保存后执行`npm install`待依赖安装完成后执行`pm2 start`  
  
到这里你的服务已经完成了，可以在telegram与机器人对话，发送 `/getqh` 就可以获取一条历史

### 各文件说明
| 文件名 | 说明 |
| ---- | ---- |
| db.txt | 情话箱历史推送数据库，文本格式，由`getmsg.py`自动更新 |
| get.sh | 用于随机获取一句情话箱历史推送，并且调用`getmsg.py`自动更新`db.txt` |
| index.js | 机器人主体代码，调用`get.sh`获取情话 |
| getmsg.py | 用于情话箱的爬虫，依赖`telethon`，若需要自动更新，则打开文件，参考[官方Wiki](https://docs.telethon.dev/)进行修改 |
| index.php | 用于随机获取一条情话箱历史推送的API，依赖`redis`实现限流策略 |
| test.sh | 用于检测句子与历史推送的一致性，由`qinghua-bot`项目调用|

### 遵循协议
<a href="http://www.wtfpl.net/"><img src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png" width="80" height="15" alt="WTFPL"></a>