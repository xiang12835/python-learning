# coding=utf-8

import urllib
import urllib2

url = 'http://www.pythontab.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

values = {'name': 'Michael Foord',
          'location': 'pythontab',
          'language': 'Python'}
headers = {'User-Agent': user_agent}  # 添加headers到你的HTTP请求，模拟成Internet Explorer
data = urllib.urlencode(values)  # 有时候你希望发送一些数据到URL(通常URL与CGI[通用网关接口]脚本，或其他WEB应用程序挂接)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
