import pymysql
from dbutils.pooled_db import PooledDB
from db.db_constant import db_constant


def tableExists(cursor, name):
    stmt = "show tables like '" + name + "'"
    cursor.execute(stmt)
    return cursor.fetchone()


def dbExists(cursor, name):
    stmt = "show databases like '" + name + "'"
    cursor.execute(stmt)
    return cursor.fetchone()


py_db_pool = PooledDB(creator=pymysql,
                maxconnections=db_constant.get_maxconnections(),  # 连接池允许的最大连接数，0和None表示不限制连接数
                mincached=db_constant.get_mincached(),  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
                maxcached=db_constant.get_maxcached(),  # 链接池中最多闲置的链接，0和None不限制
                maxusage=db_constant.get_maxusage(),  # 一个链接最多被重复使用的次数，None表示无限制
                blocking=db_constant.get_blocking(),  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
                host=db_constant.get_host(),  # 此处必须是是127.0.0.1
                port=db_constant.get_port(),
                user=db_constant.get_user(),
                passwd=db_constant.get_passwd(),
                db=f'{db_constant.get_db_name()}'
                )
