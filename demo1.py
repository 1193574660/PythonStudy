from urllib import request
resp = request.urlopen('http://wwww.baidu.com')

print(resp.read(5))
print(resp.readline())
print(resp.readlines(3))
print(resp.getcode())