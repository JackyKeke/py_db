# 创建  类似 create table %s  (
#         bk_id varchar(30) primary key,
#         title varchar(30),
#         district varchar(20))
__sql_create_table = f"""create table  %s  %s  engine=innoDB default charset=utf8mb4 """


# column = f"""(
#             {Community.m_community_id} varchar(30) primary key,
#             {Community.m_community_name} varchar(30),
#             {Community.m_district} varchar(20),
#             {Community.m_community_one_m2_price} int,
#             {Community.m_community_listing_number} int,
#             {Community.m_record_time} varchar(15),
#             {Community.m_recent_deal_record} varchar(600),
#             {Community.m_followers_number} int,
#             {Community.m_recent_90_days_deal} int,
#             {Community.m_recent_30_days_watch} int
#         )"""
#         con_sql = f"""{sql_create_table}""" % (table_name, column)
# 普通建表语句
def create_table_sql(table_name, column):
    return f"""{__sql_create_table}""" % (table_name, column)


#     li = " "
#     for i in range(len(communityList)):
#         community = communityList[i]
#         li += f""" (
#            '{community.community_id}', '{community.community_name}', '{community.district}',
#            {community.community_one_m2_price}, {community.community_listing_number}, '{community.record_time}',
#            '{community.recent_deal_record}', {community.followers_number}, {community.recent_90_days_deal}, {community.recent_30_days_watch}
#            ) """
#         if i < len(communityList) - 1:
#             li += ""","""
#     columns = [Community.m_community_id, Community.m_community_name, Community.m_district,
#                Community.m_community_one_m2_price, Community.m_community_listing_number, Community.m_record_time,
#                Community.m_recent_deal_record, Community.m_followers_number, Community.m_recent_90_days_deal,
#                Community.m_recent_30_days_watch]
#     sql_insert = sql_insert_info(table_name, columns, li)
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


#     columns = ["big", "one_m2_price", "construct_time", "followers", "district"]
#     sql = sql_general_search_info(table_name, columns, "1=1 and construct_time>1970  limit 1000")
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


# table_name = "second_test_gz_2023_3_2"
#     columns = ["community_name", "COUNT(*)"]
#     sql = sql_search_by_group(table_name, columns, columns[0])
def sql_search_by_group(table_name, columns, group_name):
    sql = f"""select distinct """
    for i in range(len(columns)):
        sql += f"{columns[i]}"
        if i < (len(columns) - 1):
            sql += ", "

    sql += """  from %s  group by %s"""
    return sql % (table_name, group_name)
