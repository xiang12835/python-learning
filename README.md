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
