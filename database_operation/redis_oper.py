# coding=utf-8


import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
r.get('foo')

print r.get('foo')

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

keys = r.keys()
print type(keys)
print keys


r = redis.Redis(host='localhost', port=6379, db=0)

print r.keys()
# print r.llen(r)

r.delete("foo")
print r.keys()



import redis


pool = redis.ConnectionPool(host='10.66.175.85', password='crs-kdbd9qqa:!@#123qwe', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

keys = r.keys()
print type(keys)
print keys


# r.delete("del1")
