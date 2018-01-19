#  PythonLearn

### 学习资料

1. [Python教程(廖雪峰的官方网站)](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
2. [A Byte of Python](https://python.swaroopch.com/)
3. [《编写高质量代码：改善Python程序的91个建议》](https://zhuanlan.zhihu.com/p/26761842)
4. [《Effective Python》](https://guoruibiao.gitbooks.io/effective-python/content/)
5. [《Target Offer》](http://blog.csdn.net/u012505432/article/details/52071537)


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


## html/css/js

### 格式化时间
```html

<div class="form-group">
    <label class="control-label col-sm-2" for="validate_time">截止时间</label>
    <div class="col-sm-8 input-prepend input-group">
        <span class="add-on input-group-addon"><i class="glyphicon glyphicon-calendar fa fa-calendar"></i></span>
        <input type="text" style="width: 200px" name="deadline_time" id="deadline_time" class="form_datetime"
               value="{% if item.id %}{{item.deadline_time|date:"Y-m-d H:i:s"}}{% endif %}"/>
    </div>
</div>

```
    
```js
$('.form_datetime').datetimepicker({
    format: 'yyyy-mm-dd hh:ii:ss',
    language:  'zh-CN',
    weekStart: 1,
    todayBtn:  1,
    autoclose: 1,
    todayHighlight: 1
});

```

### 页面上限制字数个数

[示例] maxlength=16 只允许显示16字

```html
<div class="form-group">
  <label for="voucher_scope_str">适用范围描述</label>
  <input type="text" class="form-control" maxlength=16 id="voucher_scope_desc" name="voucher_scope_desc"
         value="{% if voucher %}{{ voucher.scope_desc }}{% endif %}">
</div>

```
### &nbsp

[问题]&nbsp是什么意思？？

[解答]&nbsp;是空格，因为html对连续的空格只作为一个空格处理，所以要用&nbsp;显示空格


### window.location.href

```js
$(".device_type_selector").change(function(){
    window.location.href = "{% url 'search_hot_word_words' %}" + "?device_type=" + $(this).val()
})
```

### 返回按钮 - onclick="history.back()"

```html
<a class="btn btn-default" onclick="history.back()" href="#"><i class="icon-circle-arrow-left"></i>返回</a>

```


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

一般地，/项目/模块/v1/视图名称

例如：
- /api/user_info/v5/item_count GET 获取产品的数量
- /api/user_info/v5/item_list GET 获取产品列表
- /api/user_info/v5/item_detail?id=100 GET 获取id为100的产品详情
- /api/user_info/v5/item_post?item_id=100 POST 创建产品信息
- /api/user_info/v5/item_put?item_id=100 PUT 更新产品的全部信息
- /api/user_info/v5/item_patch?item_id=100 PATCH 更新产品的部分信息
- /api/user_info/v5/item_delete?id=100 DELETE 删除id为100的产品信息



### 请求参数

在设计服务端的 RESTful API 的时候，我们还需要对请求参数进行限制说明。例如一个支持批量查询的接口，我们要考虑最大支持查询的数量。
【GET】     /v1/users/batch?user_ids=1001,1002      // 批量查询用户信息
参数说明
- user_ids: 用户ID串，最多允许 20 个。此外，在设计新增或修改接口时，我们还需要在文档中明确告诉调用者哪些参数是必填项，哪些是选填项，以及它们的边界值的限制。

【POST】    /v1/users                              // 创建用户信息

请求内容

``` python 
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
 
 
### JSON数据返回格式
```python
{
    "msg": "请求成功",
    "status": "success",    # "success"|"failed"
    "code": 200,
    "result": {
        "balance": 8001,  # 余额（数据结构：Float）
        "voucher_count": 1,  # 卡券数量
        "order_count": 178  # 订单数量
    }
}


{
    "status": "failed",
    "code": 400,
    "desc": "list index out of range,list index out of range"
}
```


## MySQL


### limit
```sql
SELECT * FROM table  LIMIT [offset,] rows | rows OFFSET offset
```
在我们使用查询语句的时候，经常要返回前几条或者中间某几行数据，这个时候怎么办呢？不用担心，mysql已经为我们提供了上面这样一个功能。

LIMIT 子句可以被用于强制 SELECT 语句返回指定的记录数。LIMIT 接受一个或两个数字参数。参数必须是一个整数常量。如果给定两个参数，第一个参数指定第一个返回记录行的偏移量，第二个参数指定返回记录行的最大数目。初始记录行的偏移量是 0(而不是 1)： 为了与 PostgreSQL 兼容，MySQL 也支持句法： LIMIT # OFFSET #。

```sql
-- 检索记录行6-15
mysql> SELECT * FROM table LIMIT 5,10;  

-- 为了检索从某一个偏移量到记录集的结束所有的记录行，可以指定第二个参数为 -1：
-- 检索记录行 96-last.
mysql> SELECT * FROM table LIMIT 95,-1; 

-- 如果只给定一个参数，它表示返回最大的记录行数目：
-- 检索前 5 个记录行 
mysql> SELECT * FROM table LIMIT 5;     
-- 换句话说，LIMIT n 等价于 LIMIT 0,n。

```

示例：
```sql
-- pageNum = 1, pageSize = 5
SELECT * FROM bskgk.`course_user_info` WHERE `course_user_info`.`userId` = '201702071511512892383865'  ORDER BY `course_user_info`.`purchaseTime` DESC LIMIT 5;
-- pageNum = 2, pageSize = 5
SELECT * FROM bskgk.`course_user_info` WHERE `course_user_info`.`userId` = '201702071511512892383865'  ORDER BY `course_user_info`.`purchaseTime` DESC LIMIT 5 OFFSET 5;
-- pageNum = 3, pageSize = 5
SELECT * FROM bskgk.`course_user_info` WHERE `course_user_info`.`userId` = '201702071511512892383865'  ORDER BY `course_user_info`.`purchaseTime` DESC LIMIT 5 OFFSET 10;
-- pageNum = 4, pageSize = 5
SELECT * FROM bskgk.`course_user_info` WHERE `course_user_info`.`userId` = '201702071511512892383865'  ORDER BY `course_user_info`.`purchaseTime` DESC LIMIT 5 OFFSET 15;

```


总结：

已知 pageNum = 1, pageSize = 5

1) 若是列表
```python
start = (pageNum - 1) * pageSize
end = start + pageSize

```

2）若是SQL
```python
limit = pageSize
offset = (pageNum - 1) * pageSize

```


### explain

```sql
explain select tb1.orderId
from bskgk.order_info as tb1 
inner join bskgk.order_info_detail as tb2 on tb1.orderId=tb2.orderId 
where tb1.PayJe>0 and tb1.status=2 and tb2.productId=201801051723328662664953
ORDER BY tb1.createTime DESC;

```

修改：

```sql
explain select tb1.orderId
from bskgk.order_info as tb1 
inner join bskgk.order_info_detail as tb2 on tb1.orderId=tb2.orderId 
where tb1.PayJe>0 and tb1.status=2 and tb2.productId="201801051723328662664953"
ORDER BY tb1.createTime DESC;

```


### 数据库优化

表A，表B，A.b_id = B.id

1> o(1+n)

```python
a_list = A.objects.all()
b_list = []
for a in a_list:
  b = B.objects.filter(id=a.b_id)
  b_list.append(b)

```

缺点：时间复杂都高

2> o(1)
```sql
select * from A 
inner join B on B.item_id=A.item_id

```

缺点：空间复杂都高，占用大量内存，内存不够用时用磁盘

3> o(1+1)

```python
a_list = A.objects.all()
b_ids = []
for a in a_list:
  b_ids.append(a.b_id)
b_list = B.objects.filter(id__in=b_ids)

```


### 数据库原理

二叉排序树 - B树 - B+树



### 不同的 SQL JOIN

除了我们在上面的例子中使用的 INNER JOIN（内连接），我们还可以使用其他几种连接。

下面列出了您可以使用的 JOIN 类型，以及它们之间的差异。

- INNER JOIN: 如果表中有至少一个匹配，则返回行
- LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行
- RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行
- FULL JOIN: 只要其中一个表中存在匹配，就返回行


### 数据库的增删查
```sql
CREATE SCHEMA `cms_platform_test` DEFAULT CHARACTER SET utf8 ;
DROP DATABASE `cms_platform`;
show databases;
```

### 删除外键

```sql
show create table cms_platform.content_iphonebigdatavideo;
alter table content_iphonebigdatavideo drop foreign key box_id_refs_id_913ba4c50663220;

```


### SQL语句增加列、修改列、删除列

- 增加列：

```sql
alter table tableName add columnName varchar(30)

```

- 修改列类型：
```sql
alter table tableName alter column columnName varchar(100)

```

- 修改列的名称：
```sql
EXEC sp_rename 'tableName.column1', 'column2'  (把表名为tableName的column1列名修改为column2)

```

- 删除列：
```sql
alter table tableName drop column columnName1[, drop column columnName2]

```
 


### mysql中数据迁移
法一：
```bash
mysqldump -u root -h hostname -p --databases cms_platform > cms_platform.sql
mysql -u root -p
```

输入密码进入 MySQL 命令行
```bash
source /path/to/cms_platform.sql;
```

法二：
数据库导入：
```bash
mysqldump -uroot -pxxxx -h xxxx db_name > db_name_dump.SQL
mysql -uxxxx -pxxxx -h xxxx -e "CREATE DATABASE new_db_name"
mysql -uxxxx -pxxxx -h xxxx new_db_name < db_name_dump.SQL
```

法三：
```bash
use db_name
show create table tab_name  # 确认character
mysqldump --default-character-set=utf8  db_name > db_name.dump
gzip dumpname
```



### 在online线上如何生成sql语句
［法一］
```bash
git log # 记录版本号
git reset --hard [commit] # 提交之前的commit_id号
python manage.py schemamigration youappname --auto
python manage.py migrate youappname

git reset --hard [commit] # 提交之后的commit_id号
python manage.py schemamigration youappname --auto
python manage.py migrate youappname

```

［法二］
```bash
python manage.py schemamigration content --auto
python manage.py migrate content --db-dry-run --verbosity=2

```


### 添加非本地的SQL，手动添加
```bash
$ ssh 10.100.27.174
$ mysql -uwireless-admin -h10.100.56.81 -p1LytSCuf5tFZ
```

```sql
mysql> show databases;
mysql> use cms_platform;
mysql> ALTER TABLE `content_synclog` ADD COLUMN `subtitles` varchar(255) NOT NULL;
```


### mysql 定义存储过程

```sql
DELIMITER $$

DROP PROCEDURE IF EXISTS `get_top_n_androidboxvideo` $$
CREATE PROCEDURE `get_top_n_androidboxvideo` ()
BEGIN

          SET @row=0;
          SET @box_id='';
          SELECT a.*,b.rownum FROM foreign_cms_2.content_androidboxvideo a
          LEFT JOIN (
          SELECT id,box_id,position, CASE WHEN @box_id = box_id THEN @row:=@row+1 ELSE @row:=1 END rownum, @box_id:=box_id MID
          FROM foreign_cms_2.content_androidboxvideo
          ORDER BY box_id,position DESC
          ) b ON b.box_id=a.box_id AND b.id=a.id  WHERE b.rownum<11;

END $$

DELIMITER ;

call get_top_n_androidboxvideo();

```



### mysql优化
- mysql - where执行顺序

where执行顺序是从左往右执行的，在数据量小的时候不用考虑，但数据量多的时候要考虑条件的先后顺序，此时应遵守一个原则：排除越多的条件放在第一个

sql语句：
```sql
select 考生姓名, max(总成绩) as max总成绩
from tb_Grade
where 考生姓名 is not null
group by 考生姓名
having max(总成绩) > 600
order by max总成绩

```

在上面的示例中 SQL 语句的执行顺序如下:

1. 首先执行 FROM 子句, 从 tb_Grade 表组装数据源的数据
2. 执行 WHERE 子句, 筛选 tb_Grade 表中所有数据不为 NULL 的数据
3. 执行 GROUP BY 子句, 把 tb_Grade 表按 "学生姓名" 列进行分组(注：这一步的时候它会只用select中的别名，这是唯一一个使用select别名的地方，他返回的是一个游标，而不是一个表，所以在where中不可以使用select中的别名，而having却可以使用)
4. 计算 max() 聚集函数, 按 "总成绩" 求出总成绩中最大的一些数值
5. 执行 HAVING 子句, 筛选课程的总成绩大于 600 分的.
6. 执行 ORDER BY 子句, 把最后的结果按 "Max 成绩" 进行排序.



- 加索引，使用联合索引

- 死锁问题

因为sql中in查询中有太多id的话，连续执行容易造成死锁，所以将大sql化成多个小sql

```python

step = 8
ids = id_list
id_group = [ids[x:x + step] for x in range(0, len(ids), step)]
for id_items in id_group:
    try:
        IphoneSubChannel.objects.filter(id__in=id_items).update(state=int(value))
        response = {'status': 'success', 'channel_ids': channel_ids.split(",")}
    except:
        response = {'status': 'error', 'msg': u"视频不存在!"}

```
    
- 减少循环中sql的查询次数

> a) 1+n -> 1+1 问题: 通过建立 where in []

问题<1+n>:
    
```python
user_vouchers = UserVoucher.objects.filter(user_id=user_id).order_by("-create_time")  # 第一次
vouchers = []
for each in user_vouchers:
    voucher = VoucherEntity.objects.get(id=each.voucher_id)  # n次
    vouchers.append(voucher)

```
        
        
解决<1+1>:
```python
user_vouchers = UserVoucher.objects.filter(user_id=user_id).order_by("-create_time")  # 第一次
voucher_id_list = []
for each in user_vouchers:
    voucher_id_list.append(each.voucher_id)
vouchers = VoucherEntity.objects.filter(id__in=voucher_id_list).order_by("-create_time")  # 第二次

```

> b n+1 -> 1+1 问题: 通过建立外键


- 少用 count(*) 效率问题，因为当数据多时，页面会加载慢


- 少用many_to_many，因为会有三张表做笛卡尔积，然后再查询，效率极低
   正确的做法是：用两个Foreigin_Key做关联


- 检查是否重复
```python
phone = qd.get("phone", '')
customer = Customer.objects.filter(phone=phone).first()
if customer:
    if _id and customer.id == int(_id):
        exists = False
    else:
        exists = True
else:
    exists = False

if exists:
    msg = "有重复的手机号码"

    context = {
        "msg": msg,
        "item": item,
        "user_id": request.user.id,
        "menu_id": "100",
    }

    return render(request, 'customer/customer_new.html', context)

```
        
- 一个示例

优化前
```python
def get(self):
    page = self.arg_int('page', 1)
    page_count = self.arg_int('page_count', 20)
    result = {}

    topics = Topic.objects.filter(status=Topic.STATUS_NORMAL)[(page-1)*page_count:((page-1)*page_count+page_count)]  # 1次，假设有10个话题
    details_of_topics = []
    for t in topics:
        comments = TopicComment.objects.filter(topic_id=t.id, status=TopicComment.STATUS_NORMAL).order_by("-admire_count")[:3] # 10个话题*1次，每次假设有10个评论
        details_of_comments = []
        for c in comments:
            reply_count = TopicComment.objects.filter(reply_comment_id=c.id).count() # 10个话题*10个评论*1次
            details_of_comments.append({
                "id": c.id,
                "user_detail": c.to_user.to_json(),  # 10个话题*10个评论*1次
                "content": c.content,
                "topic_id": c.topic_id,
                "reply_comment_id": c.reply_comment_id,
                "admire_count": c.admire_count,
                "reply_count": reply_count,
                "created_at": c.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            })

        details_of_topics.append({
            "id": t.id,
            "title": t.title,
            "icon": t.topic,
            "topic_image": t.image,
            "background_image": t.bg_image,
            "participant_count": t.participant_count,
            "activity_title": t.activity_title,
            "activity_desc": t.activity_desc,
            "activity_content": t.activity_content,
            "comment_list": details_of_comments,
        })

    result["topics"] = details_of_topics
    result["status"] = "success"
    result["code"] = 200
    result["msg"] = ""

    return self.write(result)

```
    
总共 1+10+100+100=211次


# 优化后

```python

def get(self):
    page = self.arg_int('page', 1)
    page_count = self.arg_int('page_count', 20)
    result = {}

    topics = Topic.objects.filter(status=Topic.STATUS_NORMAL).order_by("-created_at")[(page-1)*page_count:((page-1)*page_count+page_count)]  # 查询1次，假设有10个话题
    topic_list = []
    user_ids = []
    for t in topics:
        comments = TopicComment.objects.filter(topic_id=t.id, status=TopicComment.STATUS_NORMAL).order_by("-admire_count")[:3]  # 10个话题*1次，每次假设有10个评论

        comment_list = []
        for c in comments:
            comment_list.append(c.to_json())
            user_ids.append(c.user_id)

        data = t.to_json()
        data["comment_list"] = comment_list
        topic_list.append(data)

    users = BskUser.objects.filter(user_id__in=user_ids)  # 1次
    users_dict = queryset_to_dict(users, "user_id")

    for t in topic_list:
        for comment in t.get("comment_list", []):
            user = users_dict.get(comment["user_id"])
            if user:
                comment["user_detail"] = user.to_json()

    result["topics"] = topic_list
    result["status"] = "success"
    result["code"] = 200
    result["msg"] = ""

    return self.write(result)


```

    
总共 1+10+1=12 次



### mysql 时间戳与日期格式的相互转换


- UNIX时间戳转换为日期用函数： FROM_UNIXTIME()
```sql
select FROM_UNIXTIME(1156219870);  
```
输出：2006-08-22 12:11:10


- 日期转换为UNIX时间戳用函数： UNIX_TIMESTAMP()


```sql
Select UNIX_TIMESTAMP('2006-11-04 12:23:00'); 
```
输出：1162614180  


### mysql 格式化日期

```sql
select now();
```

输出：'2018-01-15 20:39:37'
```sql
select DATE_FORMAT(now(),'%Y-%m-%d');
```

输出：'2018-01-15'



### like

```sql 
SELECT * FROM Persons
WHERE City LIKE 'N%'

```

"%" 可用于定义通配符（模式中缺少的字母）




## 缓存
### 缓存系统工作原理：

> 对于给定的网址，尝试从缓存中找到网址，如果页面在缓存中，直接返回缓存的页面，如果缓存中没有，一系列操作（比如查数据库）后，保存生成的页面内容到缓存系统以供下一次使用，然后返回生成的页面内容。

示例：当使用了cache后，访问情况变成了如下：

> 访问一个网址时, 尝试从 cache 中找有没有缓存内容，如果网页在缓存中显示缓存内容，否则生成访问的页面，保存在缓存中以便下次使用，显示缓存的页面。

```shell
given a URL, try finding that page in the cache

if the page is in the cache:
  return the cached page
else:
  generate the page
  save the generated page in the cache (for next time)
  return the generated page

```

### 算法：
- 简单的路由算法：

余数hash

出现的问题：使用余数Hash的路由算法，在扩容的时候会造成大量的数据无法正确命中（其实不仅仅是无法命中，那些大量的无法命中的数据还在原缓存中在被移除前占据着内存）

解决：

一致性性hash算法 － 构造一个长度为232的整数环（这个环被称为一致性Hash环）

出现的问题：由于随机数服从正态分布，其中的M出现的数据比较集中

解决：

katama算法 － 统计学中，使用160个M

### 缓存分类：

- 内存缓存

Memcached的缓存策略是LRU（最近最少使用）加上到期失效策略

Memcached 是目前 Django 可用的最快的缓存

示例：

Django settings 中 cache 默认为

```json
{
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
```

- 数据库缓存

示例：

```json
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table_name',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 2000
        }
    }
}
```


- 文件缓存

示例：

```json
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}
```

- 其他

action cache

fragment cache

page cache


## memcached
### 清本地memcached缓存

```shell

$ telnet localhost 11211
$ flush_all  #清空所有键值，但不会删除items，此时MemCache依旧占用内存

```
  

### 清测试线memcached缓存

```shell
  telnet 10.105.28.41 11233
  flush_all
```

### 缓存示例
假设给app的首页接口是A， 给你们的接口是B

A的缓存是：1m + 2m ＋ 1h（内容变更后更新）

B的缓存是： 1h

A中1h的部分在内容变更后更新，所以缓存3m；B中1h的部分之前由于使用不同组的缓存服务器是没办法清除的，但是用10.100.188.99测试B的话是和A中1h的缓存是同源的。

所以用10.100.188.99访问的话的接口数据基本就是最新的了，相差3分钟

```python
from api.view.base import BaseHandler, CachedPlusHandler
＃ 若某个类继承BaseHandler，则无缓存
＃ 若某个类继承CachedPlusHandler，则有缓存

from api.lib.cached_data import cached_all_boxes, cached_all_video_list_modules, cached_all_jumps, cached_box_videos, cached_all_tags, cached_box_poster_videos, cached_all_banners, cached_all_boxes_by_platform_id
＃ 当某个内容需要经常使用的时候，需要使用缓存，以减少SQL语句，提高效率

```


## redis
### redis常见操作

```shell
$ redis-server &
$ redis-cli

127.0.0.1:6379> select 12
OK
127.0.0.1:6379[12]> keys *
1) "async.channel.job"
127.0.0.1:6379[12]> llen async.channel.job
(integer) 143
127.0.0.1:6379[12]> del async.channel.job
(integer) 1
127.0.0.1:6379[12]> llen async.channel.job
(integer) 0
```



### 链接redis服务器

```shell
cd ~/mobile-cms-background/target/mobile-cms-background/app/
/home/tops/bin/python manage.py shell
import redis
r =redis.Redis(host='11.173.167.16',port=6379,db=12)
r.keys()
r.llen('cache.do_cms_url_clean')

```


## varnish

使用varnish去除掉URL中的时间戳和一些PID，作为key值

/Users/yourname/work/python/m-cms-new/api/conf/varnish/varnish3.vcl

