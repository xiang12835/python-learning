#  PythonLearn

### 学习资料

1. Python教程(廖雪峰的官方网站)
2. 《A Byte of Python》
3. 《Effective Python》
4. 《Target Offer》


# Python 开发工程师 - 职位

### 工作职责：
1. 优酷 APP 服务端业务需求开发，性能优化
2. 参与系统架构设计、接口规范制定、技术文档编写
3. 负责基于 python web 快速开发、相关优化以及产品部署
4. 搭建系统开发环境，完成系统框架和核心代码的实现，负责解决开发过程中的技术问题
5. 负责 Python 技术的相关产品规划、需求、设计、开发、测试等研发工作

### 任职要求：
1. 精通 python 语言开发，熟悉 django、tornado、flask 开发框架
2. 熟悉常用数据结构和算法，熟练设计模式
3. 熟练使用 HTML、CSS、JavaScript 等前端知识，熟悉 BootStrap、jQuery、Node.js、Vue.js 框架
4. 熟悉 MySQL、Redis、MongoDB 等常用数据库，具有数据库开发和设计能力
5. 熟悉缓存技术，如 Memcache、Vanish
6. 熟悉 Linux 操作系统及 shell 编程，熟悉 git 等源代码管理工具
7. 熟悉 TCP/IP、HTTP 等通信协议，具有 socket 网络编程和大规模并发服务器开发经验
8. 了解异步框架、集群与负载均衡，消息中间件，容灾备份等技术
9. 有全栈开发经验或大型在线服务开发经验优先
10. 掌握操作系统、软件工程、设计模式、数据结构、数据库系统、网络安全等软件知识结构
11. 熟悉 LVS 等开源负载均衡系统


# 后端开发 - 总结

## Python 

### mac 上安装 python 开发环境

- 安装 brew
```shell
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

- 安装 python
```shell
$ brew install python2 python3
```

- 安装 virtualenv & virtualenvwrapper
```shell
$ sudo pip install virtualenv
$ sudo pip install virtualenvwrapper
```

- 配置文件
```shell
$ touch .bash_login
$ vi .bash_login
source /usr/local/bin/virtualenvwrapper.sh
# 作用就是：wrapper在每次打开shell的时候自动运行
```

- 常用命令
```shell
$ mkvirtualenv env3.5 -p /usr/local/bin/python3
$ mkvirtualenv env2.7
$ lsvirtualenv
$ rmvirtualenv env2.7
$ workon env3.5
$ deactivate
```

### mac 安装 pylibmc

#### pylibmc 是什么

> pylibmc 为 memcached 的 python 客户端，底层为 c 实现的 libmemcached ，效率比较高。安装 libmemcached 需要本机安装了 memcached

#### 安装步骤

- 安装libevent
```shell
$ sudo brew install libevent
```

- 安装memcached
```shell
$ sudo brew install memcached
```

- 安装libmemcached
```shell
$ sudo brew install libmemcached
```

- 安装pylibmc

```shell
$ sudo pip install pylibmc
```

### ubuntu 安装 pylibmc 模块

```shell
$ sudo apt-get install libmemcached-dev zlib1g-dev
$ sudo pip install pylibmc
```

### ubuntu 安装 MySQLdb 模块

```shell
pip install mysql-python
```

### HTTPServer

> 如果想让身边的同事临时访问你电脑中的文件目录，通常的做法是搭一个共享目录出来供大家访问，不过你要是安装了Python，那么一切都变得简单很多了，只需要打开命令行窗口，切换到指定目录，执行：

``` shell
$ python -m SimpleHTTPServer  # python2
$ python -m http.server  # python3
```

> 这是 Python 内置的一个简单 http server，方便自己、他人用浏览器来访问你的文件目录

### 静态方法／类方法／实例方法

### 全局变量／类变量／实例变量

### 装饰器／@property

### 切片 slice



## Django

### filter | exclude

``` Python
if has_buy == "1":
    datas = datas.filter(phone__in=customer_phone_list)
elif has_buy == "0":
    datas = datas.exclude(phone__in=customer_phone_list)
```

### Q

- Q()对象的前面使用字符“~”来代表意义“非”

``` Python
datas = OrderInfo.objects.filter(status="2", amount__gt=0).filter(~Q(express_code=""))
```

- 使用 “&”或者“|”还有括号来对条件进行分组从而组合成更加复杂的查询逻辑
``` Python
users = BskUser.objects.filter(Q(user_name__contains=search_key)|Q(nickname__contains=search_key))
```

### 注意点
> 不能拖库

### queryset

``` shell
$ python manage.py shell

>>> questions = QuestionInfo.objects.using("bskgk_slave").filter(status='1').values('custom_id').annotate(count=Count('custom_id')).filter(count__gte=5).order_by('-comment_time')
>>> questions.query.__str__()
```

上面这句话的SQL语句是：
``` sql
select customId, count(customId) as count
from bskgk.custom_review_info
where status="1"
group by customId
having count >= 5
order by commentTime desc;
```

### 进入 python 命令行模式

``` shell
python manage.py shell
```

### 进入 数据库 命令行模式

``` shell
python manage.py dbshell
```


### django ORM 中大于等于、小于等于
``` python
__gt  # 大于
__gte  # 大于等于
__lt  # 小于
__lte  # 小于等于
```

### 取出 django 注册的用户

``` python
admin_user = request.user
```

### default_if_none
``` python
@register.filter(is_safe=False)
def default_if_none(value, arg):
    """If value is None, use given default."""
    if value is None:
        return arg
    return value
```
使用：
{{video.live_url|default_if_none:""}} - 如果值有可能为none 加上这个 templatetags 就可以把None装换成空字符串了


### 项目目录结构分析
 - app
 - api
 - background
 - base

### db router

### 查找指定数据库“bsk_db”的对象

``` python
lessons = LessonInfo.objects.using('bsk_db').filter(status=1).order_by('lesson_name', "-id")
```

### 创建admin帐号

```shell
$ python manage.py createsuperuser --username=yu.xiang --email=yu.xiang@alibaba-inc.com
```

### 创建数据库

```shell
$ python manage.py sqlindexes content  # 显示出所有的索引
$ python manage.py sql content  # 若不是默认数据库，显示出所有的表格
$ python manage.py syncdb  # 若是默认数据库
```

### south
- 第一次使用

```shell
python manage.py syncdb # 用来创建south_migrationhistory表，用来记录数据表更改(Migration)的历史纪录
python manage.py migrate
python manage.py schemamigration youappname --initial # youappname目录下面创建一个migrations的子目录 0001_initial.py
python manage.py migrate youappname #将更改反应到数据库（如果出现表已存在的错误，后面加 --fake）
```

- 以后每次对models更改后，可以运行以下两条命令同步到数据库

```shell
python manage.py schemamigration youappname --auto #检测对models的更改
python manage.py migrate youappname #将更改反应到数据库（如果出现表已存在的错误，后面加 --fake）
```

### Django CharField 中的 max_length 是指字符的个数或字节数


### 模板中的变量／标签／过滤器
- https://my.oschina.net/u/240562/blog/50393

### ForeignKey.db_constraint
> 数据库是否设置外键关系，对于外键关系，添加一条数据时，对应外键没有相应字段将会出错，但是设置为false，数据库不存在外键关系，不会检察外键约束，默认true

### django auto_now与auto_now_add的区别

- auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间
- auto_now_add为添加时的时间，更新对象时不会有变动


## Tornado

### 并行与并发

### 同步与异步

### 阻塞与非阻塞

### 总结

> 每个接口<=100ms * 10个并发 * 40个进程




## RESTfull API

### 资源路径命名规则

- URI – 统一资源标识符，用来唯一的标识一个资源
- URL – 统一资源定位器，用来定位某个特定的资源，如一个网址

> RESTful API 的设计以资源为核心，每一个 URI 代表一种资源。因此，URI 不能包含动词，只能是名词。注意的是，形容词也是可以使用的，但是尽量少用。一般来说，不论资源是单个还是多个，API 的名词要以复数进行命名。此外，命名名词的时候，要使用小写、数字及下划线来区分多个单词。这样的设计是为了与 json 对象及属性的命名方案保持一致。

> 一般地，/项目/模块/v1/视图名称

例如：
- /api/user_info/v5/product_count GET 获取产品的数量
- /api/user_info/v5/product_list GET 获取产品列表
- /api/user_info/v5/product_detail?id=100 GET 获取id为100的产品详情
- /api/user_info/v5/product_post?item_id=100 POST 创建产品信息
- /api/user_info/v5/product_put?item_id=100 PUT 更新产品的全部信息
- /api/user_info/v5/product_patch?item_id=100 PATCH 更新产品的部分信息
- /api/user_info/v5/product_delete?id=100 DELETE 删除id为100的产品信息



### 请求参数

在设计服务端的 RESTful API 的时候，我们还需要对请求参数进行限制说明。例如一个支持批量查询的接口，我们要考虑最大支持查询的数量。
【GET】     /v1/users/batch?user_ids=1001,1002      // 批量查询用户信息
参数说明
- user_ids: 用户ID串，最多允许 20 个。此外，在设计新增或修改接口时，我们还需要在文档中明确告诉调用者哪些参数是必填项，哪些是选填项，以及它们的边界值的限制。

【POST】    /v1/users                              // 创建用户信息

请求内容

``` json 
{
    "username": "lgz",                 # 必填, 用户名称, max 10
    "realname": "your_name",           # 必填, 用户名称, max 10
    "password": "123456",              # 必填, 用户密码, max 32
    "email": "lianggzone@163.com",     # 选填, 电子邮箱, max 32
    "weixin": "LiangGzone",            # 选填，微信账号, max 32
    "sex": 1                           # 必填, 用户性别[1-男 2-女 99-未知]
}

```

### 分页信息 （pageNum;pageSize）

- 若是 SQL

```python
limit = pageSize
offset = (pageNum - 1) * pageSize

```
    
- 若是 列表[]

```python
start = (pageNum - 1) * pageSize
end = start + pageSize
```

### 使用小驼峰命名法

> 使用小驼峰命名法作为属性标识符。

```json
{ "yearOfBirth": 1982 }
```

### 请求方式

> 可以通过 GET、 POST、 PUT、 PATCH、 DELETE 等方式对服务端的资源进行操作。其中，

- GET 用于查询资源，
- POST 用于创建资源，
- PUT 用于更新服务端的资源的全部信息，
- PATCH 用于更新服务端的资源的部分信息，
- DELETE 用于删除服务端的资源。


### 状态码

 状态码  | 描述
------- | ---------
 200    | 请求成功
 201    | 创建成功
 400    | 错误的请求
 401    | 未验证
 403    | 被拒绝
 404    | 无法找到
 409    | 资源冲突
 500    | 服务器内部错误
