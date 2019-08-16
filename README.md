# music-downloader

从 liumingye.cn 下载音乐，自动整合入封面等信息入音乐

### Usage

1. 从 [liumingye.cn](http://lab.liumingye.cn/api/) 获得带 token 的音乐信息请求，形如

   ```plain
   http://lab.liumingye.cn/api/ajax/search/text/5ZGo5p2w5Lym/page/1/type/qq/token/466b25f5faf650fae5e90ffbc3feadc8
   ```

2. 存入 `todo.txt` 中，两条 link 间用换行 `\n` 分隔

3. 安装 python3 环境 + pip3，运行一下命令安装第三方库
   
   ```python
   pip3 install -r requirements.txt
   ```

4. 运行 `spider.py`，脚本会自动下载音乐。

### Custom

脚本默认使用 `cp` 命令进行复制，`wget` 工具进行下载。如果这两个工具在你的电脑上不存在或你想更换其他方式，可以自行实现 `function.py` 里的 `copy_file(source_file, target_file)` 函数和 `download.py` 里的 `download(url, path)` 函数。

### Warning

仅供学习交流，请适度使用，切勿用作非法用途或恶意消耗流量资源。