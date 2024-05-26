# U校园听力爬虫

考虑到爬虫的普适性，以及部分音频转文字api需要购买和库难以导入。就没有将音频识别为文字的功能集成在代码中。

### 功能介绍

![image-20240526143413624](image-20240526143413624.png)

我们可以看到平时做听力会很麻烦的，因为音频毕竟不是英文，无法粘贴给AI让其回答。

所以此小爬虫的功能是将u校园的听力的音频下载为mp3

后期用[音频转文本 - 100%免费和在线 (converter.app)](https://converter.app/cn/audio-text/)

这种类似的mp3转文本的网站进行转化

### 操作流程

首先提前打开浏览器开发者界面（F12键盘）并点进去网络界面

![image-20240526143952301](image-20240526143952301.png)

接着保持此界面，接着进入你想要爬取的课后测试

![image-20240526143850986](image-20240526143850986.png)

等待全部完成会出现很多网络请求

![image-20240526144209287](image-20240526144209287.png)

已经用brup抓包工具分析过了，只需要Ctrl+F 搜索 https://uexercise.unipus.cn/itest/s/clsanswer/load

![image-20240526144354335](image-20240526144354335.png)

即可找到指定的url我们点进去，这里我们采集两个数据

一个是Cookie

![image-20240526144509516](image-20240526144509516.png)

另一个是User-Agent

![image-20240526144601916](image-20240526144601916.png)

接着将复制到的数据粘贴到我们代码的指定位置

![image-20240526144721930](image-20240526144721930.png)

后续也需要自己定义合适的地址存放产生的mp3文件

![image-20240526144807097](image-20240526144807097.png)

然后就可以正常运行了！

### 运行效果

![image-20240526144900622](image-20240526144900622.png)

**注：1~n依据音频播放小喇叭的顺序**