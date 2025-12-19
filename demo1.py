from urllib import request,parse
# resp = request.urlopen('http://wwww.baidu.com')

# print(resp.read(5))
# print(resp.readline())
# print(resp.readlines(20))
# print(resp.getcode())


# request.urlretrieve('http://www.baidu.com','baidu.html') 


url = 'https://www.baidu.com/s'
params = {"wd":"刘德华"}

qs = parse.urlencode(params)

print("qs is ",qs)

result = parse.parse_qs(qs)

print("parse qs is ",result)

resp = request.urlopen(url+'?'+qs)

print(resp.read())