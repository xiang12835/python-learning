# coding=utf-8

import md5

src = 'winlesson'
m1 = md5.new()
m1.update(src)
print m1.hexdigest()



import hashlib

m2 = hashlib.md5()
m2.update(src)
print m2.hexdigest()


"""
一个签名问题

- 问题：
116.115.163.120 "2017-11-09T14:11:03+08:00" GET "/content/operation/list/by_category" "device=phone&platform=android&app_type=2&_s_=4d8efe586ab1386b4c449f4f656e9efb&category_id=&from=2&user_id=201710272223096210192734&ver=3.6.0&_t_=1510207862" "-" 403 168 0.000 "okhttp/${project.version}"


- 签名方式:
token_string = req_method + ":" + path + ":" + sorted(query) + ":" + timestamp + ":" + secret
其中：sorted(query) 是按照key的自然顺序排列,然后以key=value的形式累加
例如: GET /test?b=2&a=1
token_string = GET + ":" + /test + ":" + a=1b=2 + ":" + 1457665234 + ":" + secret_xxxxxx
signature = ngx.md5(token_string)
secret秘钥需要服务端提供，另外客户端需要确保secret安全。

- 解决：

import md5

token_string = "GET" + ":" + "/content/operation/list/by_category" + ":" + "app_type=2category_id=device=phonefrom=2platform=androiduser_id=201710272223096210192734ver=3.6.0" + ":" + "1510207862" + ":" + "821l1i1x3fv8vs3dxlj1v2x91jqfs3om"
m1 = md5.new()
m1.update(token_string)
print m1.hexdigest()

"""