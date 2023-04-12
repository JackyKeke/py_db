# 创建  类似 create table %s  (
#         bk_id varchar(30) primary key,
#         title varchar(30),
#         district varchar(20))
__sql_create_table = f"""create table  %s  %s  engine=innoDB default charset=utf8mb4 """


# 普通建表语句
def create_table_sql(table_name, column):
    return f"""{__sql_create_table}""" % (table_name, column)


# 我觉得适合任何应该插入更新的语句
def sql_insert_info(table_name, columns, li):
    sql = f"""insert into %s ("""
    for i in range(len(columns)):
        sql += f"{columns[i]}"
        if i < (len(columns) - 1):
            sql += ", "

    sql += """ ) values %s ON DUPLICATE KEY UPDATE  """

    for i in range(len(columns)):
        sql += f"""{columns[i]}=VALUES({columns[i]})"""
        if i < (len(columns) - 1):
            sql += ", "

    return sql % (table_name, li)


def sql_general_search_info(table_name, columns, sections=None):
    # sql = f"""select distinct info {columns} from {table_name} where {sections}"""

    sql = f"""select distinct """
    for i in range(len(columns)):
        sql += f"{columns[i]}"
        if i < (len(columns) - 1):
            sql += ", "

    sql += """  from %s """
    if sections is not None:
        sql += " where %s  "
        return sql % (table_name, sections)

    return sql % (table_name)


def sql_search_by_group(table_name, columns, group_name):
    sql = f"""select distinct """
    for i in range(len(columns)):
        sql += f"{columns[i]}"
        if i < (len(columns) - 1):
            sql += ", "

    sql += """  from %s  group by %s"""
    return sql % (table_name, group_name)
