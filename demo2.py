from urllib import parse


url = 'http://www.baidu.com/s?wd=python&username=abc#1'

result = parse.urlparse(url)

result = parse.urlsplit(url)

print(result) 