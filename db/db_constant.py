db_name = "bk_house"
# table_name = ""

# community_sale_table_name=f"second_%s_community_%s_%s_%s"
#
# district_sale_table_name=f"second_%s_district_%s_%s_%s"


class db_constant(object):
    __db_name = ""
    __prefix=""
    __maxconnections=5
    __mincached=1
    __maxcached=5
    __maxusage=5
    __blocking=True
    __host="127.0.0.1"
    __port=9527
    __user="root"
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


