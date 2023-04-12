db_name = "bk_house"


# table_name = ""

# community_sale_table_name=f"second_%s_community_%s_%s_%s"
#
# district_sale_table_name=f"second_%s_district_%s_%s_%s"


class db_constant(object):
    __db_name = ""
    __prefix = ""
    __maxconnections = 5
    __mincached = 1
    __maxcached = 5
    __maxusage = 5
    __blocking = True
    __host = "127.0.0.1"
    __port = 9527
    __user = "root"
    __passwd = 'root'

    @staticmethod
    def set_db_name(db_name):
        db_constant.__db_name = db_name

    @staticmethod
    def get_db_name():
        return db_constant.__db_name

    @staticmethod
    def set_prefix(prefix):
        db_constant.__prefix = prefix

    @staticmethod
    def get_prefix():
        return db_constant.__prefix

    @staticmethod
    def set_maxconnections(maxconnections):
        db_constant.__maxconnections = maxconnections

    @staticmethod
    def get_maxconnections():
        return db_constant.__maxconnections

    @staticmethod
    def set_mincached(mincached):
        db_constant.__mincached = mincached

    @staticmethod
    def get_mincached():
        return db_constant.__mincached

    @staticmethod
    def set_maxcached(maxcached):
        db_constant.__maxcached = maxcached

    @staticmethod
    def get_maxcached():
        return db_constant.__maxcached

    @staticmethod
    def set_maxusage(maxusage):
        db_constant.__maxusage = maxusage

    @staticmethod
    def get_maxusage():
        return db_constant.__maxusage

    @staticmethod
    def set_blocking(blocking):
        db_constant.__blocking = blocking

    @staticmethod
    def get_blocking():
        return db_constant.__blocking

    @staticmethod
    def set_host(host):
        db_constant.__host = host

    @staticmethod
    def get_host():
        return db_constant.__host

    @staticmethod
    def set_port(port):
        db_constant.__port = port

    @staticmethod
    def get_port():
        return db_constant.__port

    @staticmethod
    def set_user(user):
        db_constant.__user = user

    @staticmethod
    def get_user():
        return db_constant.__user

    @staticmethod
    def set_passwd(passwd):
        db_constant.__passwd = passwd

    @staticmethod
    def get_passwd():
        return db_constant.__passwd
