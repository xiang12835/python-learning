# coding=utf-8

# 发送 GET 请求
import requests


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'cookie': 'some_cookie'
}
response = requests.request("GET", url, headers=headers)

# 发送 POST 请求



import requests


payload={}
files=[]
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'cookie': 'some_cookie'
}
response = requests.request("POST", url, headers=headers, data=payload, files=files)
