#file:mysite3/__init__.py

import pymysql
#让django用mysql进行操作
pymysql.install_as_MySQLdb()