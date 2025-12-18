# PythonStudy
for studying python

---
# *Day1*

## 什么是爬虫
爬虫——网络爬虫，即模仿人去请求页面、访问网站等操作，并获取数据的一个网络技术。

## 爬虫分类

### 通用爬虫
什么网站都爬，例如 百度、谷歌等

### 聚焦爬虫
只爬取和需求相关的信息，例如 股票资讯等

## 需要准备的工具
1. Python
2. Pycharm
3. 虚拟环境


## 什么是HTTP协议、HTTPS协议

### HTTP协议
超文本传输协议，服务器端口 80.

### HTTPS协议
在HTTP协议基础上增加了SSL层，服务器端口 443


## URL（Uniform Resource Locator）

### URL 组成
`scheme://host:port/path/?query-string-xxx#anchor`

- **scheme :** 代表访问协议，http https ftp
- **host :** 主机名，域名，比如www.baidu.com。
- **port :** 端口号，浏览器默认是80
- **path :** 查找路径，比如 www.jianshu.com/trending/now
- **query-string :** 查询字符串，https://www.baidu.com/s?wd=sm 的 s?wd=sm 就是查询字符串
- **anchor :** 锚点，后台一般不用管，前端用来做页面定位的
---


# *Day2*

## Normal request manner
- **get :** 从服务器上拿数据
- **post :** 向服务器发送数据

具体使用**post** 还是**get**，从网站上去看

## 请求头常见参数

* User-Agent : 浏览器名称。未定制则认为是```Python```
* Refer : 表明当前的请求是从哪个URL过来的
* Cookie : 第一次请求网站时，会返回一个Cookie。用来识别用户。

## 常见响应状态码
https://m.runoob.com/http/http-status-codes.html

## Chrome 抓包工具

---

# *Day3*

## urllib 库

### urlopen函数
所有网络请求都被集中到```urllib.request```模块中。

```
from urllib import request
resp = request.urlopen('http://wwww.baidu.com')
print(resp.read())
```

返回值 : 
* read : 读取字符个数
* readline ： 读取一行
* readlines ： 读取目标行数
* getcode ： 获取状态码

### urlretrieve函数
可以将网页上的文件下载到本地
```
from urllib import request
request.urlretrieve('http://www.baidu.com','FileName')   
```