import pymysql
from pymysql.constants import CLIENT
from typing import List, Tuple, AnyStr, Dict, Union, Any
import pandas as pd
import re

from lazycode.setting import TEMP_DIR, CODE_DATA_DIR
from lazycode.core.LzFileDir import LzFileDirImp
from lazycode.core.LzDataTypeMap import LzDataTypeMap
from lazycode.core.LzDateTime import LzDateTimeImp


# # 数据于列名称对其，不错行
# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)
# # 显示所有列
# pd.set_option('display.max_columns', None)
# # 限制最多显示10行数据, 设置None表示全部显示
# pd.set_option('display.max_rows', 10)

class TableFieldMetaInfo(object):
    field_name: str = None
    field_type: str = None
    field_comment: str = None
    # 是否可以为空
    whether_null: bool = True
    # 默认值
    default_value: object = None
    # 有效数字位数/字符串长度,小数部分位数
    field_type_length: Tuple[int, int] = None
    # 是否为主键
    primary: bool = False
    # 是否唯一
    unique: bool = False
    # 字段所在的位置顺序
    position: int = 0
    # 是否自增
    increment: bool = False
    # 是否为外键
    foreign_key: bool = False
    # 外键关联的 (表名, 列名)
    foreign_key_references: Tuple[AnyStr, AnyStr] = None

    def __init__(self, field_name, field_type,
                 field_comment=None,
                 whether_null=True,
                 default_value=None,
                 field_type_length=None,
                 primary=False,
                 unique=False,
                 position=0,
                 increment=False,
                 foreign_key=False,
                 foreign_key_references=None,
                 ) -> None:
        self.field_name = field_name
        self.field_type = field_type
        self.field_comment = field_comment
        self.whether_null = whether_null
        self.default_value = default_value
        self.field_type_length = field_type_length
        self.primary = primary
        self.unique = unique
        self.position = position
        self.increment = increment
        self.foreign_key = foreign_key
        self.foreign_key_references = foreign_key_references


class TableMetaInfo(object):
    table_name: str = None
    table_comment: str = None
    db_name: str = None
    table_field_list: List[TableFieldMetaInfo] = None

    def __init__(self, table_name, table_comment=None, db_name=None, table_field_list=None) -> None:
        self.table_name = table_name
        self.table_field_list = table_field_list
        self.table_comment = table_comment
        self.db_name = db_name

    def set_table_field_list(self, table_field_list: List[TableFieldMetaInfo]):
        self.table_field_list = table_field_list


class LzMySQL(object):
    __connect: pymysql.Connection = None
    __cursor: pymysql.cursors.Cursor = None
    dbname: str = None

    def __init__(self, user: str, password: str, db: str,
                 host: str = 'localhost', port: int = 3306, charset: str = 'utf8'):
        self.dbname = db
        self.init(host=host, user=user, password=password, db=db, port=port, charset=charset)

    def init(self, user: str, password: str, db: str,
             host: str = 'localhost', port: int = 3306, charset: str = 'utf8'):
        self.__connect = pymysql.Connection(host=host, user=user, password=password, db=db,
                                            port=port, charset=charset,
                                            # pymysql在0.8及以后的版本, 添加这个参数才能一次性执行多条sql
                                            client_flag=CLIENT.MULTI_STATEMENTS
                                            )
        self.__cursor = self.__connect.cursor()

    def close(self):
        self.__cursor.close()
        self.__connect.close()

    def execute(self, sql: str, args: List = None) -> int:
        res = self.__cursor.execute(sql, args)
        self.__connect.commit()
        return res

    def executemany(self, sql: str, args: List[List] = None) -> int:
        res = self.__cursor.executemany(sql, args)
        self.__connect.commit()
        return res

    def execute_transaction(self, sql: str, args: List = None) -> int:
        res = None
        try:
            res = self.__cursor.execute(sql, args)
            self.__connect.commit()
        except Exception as e:
            print(f'{sql} 语句执行失败, 事务回滚')
            self.__connect.rollback()
        return res

    def executemany_transaction(self, sql: str, args: List[List] = None) -> int:
        res = None
        try:
            res = self.__cursor.executemany(sql, args)
            self.__connect.commit()
        except Exception as e:
            print(e)
            print(f'{sql} 语句执行失败, 事务回滚')
            self.__connect.rollback()

        return res

    def query(self, sql: str, args: List = None) -> List:
        """
        查询数据
        :param sql:
        :param args:
        :return:  [ {col_name1 : data, col_name2 : data, ... }, ... ]
        """
        line_num = self.__cursor.execute(sql, args)

        res_data = []
        if line_num > 0:
            self.__connect.commit()
            data_line = self.__cursor.fetchall()

            # 获取列字段元数据信息
            col_infos = self.__cursor.description
            col_names = [col[0] for col in col_infos]
            res_data = [dict(zip(col_names, line)) for line in data_line]
        return res_data

    def query_to_df(self, sql: str, args: List = None) -> pd.DataFrame:
        data = self.query(sql, args)
        df = pd.DataFrame(data)
        return df

    def table_meta_data(self, like_table_reg='%'):
        sql = f'''
        SELECT
            a.TABLE_SCHEMA as dbname, -- 0 数据库名
            a.TABLE_NAME as tbname,     -- 1 表名
            b.TABLE_COMMENT tbcomment,  -- 2 表注释

            a.COLUMN_NAME as colname,       -- 3 列名
            a.COLUMN_COMMENT as colcomment, -- 4 列注释
            a.DATA_TYPE as col_datatype,    -- 5 数据类型 'varchar'
            a.COLUMN_TYPE as coltype,       -- 6 列数据类型(全) 'varchar(255)'
            a.IS_NULLABLE as isnull,        -- 7 是否可以为空 'YES' , 'NO'
            a.ORDINAL_POSITION as  col_position,    -- 8 列所在位置 1
            c.CONSTRAINT_NAME as cs_type,   -- 9 列约束类型 None, PRIMARY, ... 
            c.COLUMN_NAME as cs_col_name,   -- 10 约束列名
            c.REFERENCED_TABLE_SCHEMA as cs_dbname,      -- 11 外键主表数据库名
            c.REFERENCED_TABLE_NAME as cs_tbname,        -- 12 外键主表表名
            c.REFERENCED_COLUMN_NAME as cs_tb_col_name 	 -- 13 外键主表关联列名
        FROM
            (
            SELECT * FROM information_schema.COLUMNS WHERE TABLE_SCHEMA= "{self.dbname}" -- 数据库名
            ) AS a
        LEFT JOIN information_schema.TABLES AS b
            ON a.TABLE_NAME=b.TABLE_NAME AND a.TABLE_SCHEMA=b.TABLE_SCHEMA
        LEFT JOIN information_schema.KEY_COLUMN_USAGE as c
            ON c.CONSTRAINT_SCHEMA = a.TABLE_SCHEMA 
                AND c.TABLE_NAME = a.TABLE_NAME 
                AND c.COLUMN_NAME = a.COLUMN_NAME
        WHERE a.TABLE_NAME like "{like_table_reg}" -- 需要选择的表格, 默认全部表格
        order by a.TABLE_NAME, a.ORDINAL_POSITION 
        ;
        '''

        return self.query(sql)

    # 美化 字符串
    @staticmethod
    def beautiful_string(string, prefix_space: str = ''):
        # 行前空白
        space = ' ' * 500
        lines = string.split('\n')
        for line in lines:
            if len(line.strip()) > 0:
                temp_space = re.search(r'^(\s*)\S', line).group(1)
                if len(temp_space) < len(space):
                    space = temp_space

        # 去除指定行前空白
        for i, line in enumerate(lines):
            if len(line.strip()) > 0:
                line = re.sub(r'^' + space, prefix_space, line)
            lines[i] = line
        return '\n'.join(lines)

    @staticmethod
    def create_sql_database(db_name: str, drop=False):

        drop_database = f"drop database if exists {db_name};"
        create_database = f"create database if not exists {db_name} default charset utf8mb4;"

        sql = create_database
        if drop:
            sql = drop_database + '\n' + create_database

        return sql

    @staticmethod
    def create_sql_table(table_info: TableMetaInfo, drop=False):
        """
        生成建表语句
        """

        table_field_list = table_info.table_field_list
        table_field_list.sort(key=lambda ele: ele.position)

        field_str_list1 = []
        field_str_list2 = []
        for field in table_field_list:
            field_type = field.field_type
            whether_null = '' if field.whether_null else 'not null'
            default_value = '' if field.default_value is None else f'default {field.default_value}'
            increment = '' if field.increment is False else 'auto_increment'
            field_comment = '' if field.field_comment is None else f'comment "{field.field_comment}"'

            # 主键
            if field.primary:
                field_str_list2.append(f'primary key(`{field.field_name}`)')
                whether_null = 'not null'
            # 唯一
            if field.unique:
                field_str_list2.append(f'unique(`{field.field_name}`)')
            # 外键
            if field.foreign_key:
                foreign_table = field.foreign_key_references[0]
                foreign_field = field.foreign_key_references[1]
                field_str_list2.append(f'foreign key(`{field.field_name}`) references {foreign_table}({foreign_field})')

            field_str = f'`{field.field_name}` {field_type} {whether_null} {default_value} {increment} {field_comment}'
            field_str_list1.append(field_str)

        f_str = ',\n            '.join(field_str_list1 + field_str_list2)

        db_name = '' if table_info.db_name is None else f'{table_info.db_name}.'

        table_comment = '' if table_info.table_comment is None else f'comment "{table_info.table_comment}"'

        drop_table = ''
        if drop:
            drop_table = f'drop table if exists {db_name}{table_info.table_name};'

        create_table_sql = f"""
        {drop_table}
        create table if not exists {db_name}{table_info.table_name}(
            {f_str}
        )engine=innodb default charset=utf8mb4 {table_comment};
        """

        create_table_sql = LzMySQL.beautiful_string(create_table_sql)
        return create_table_sql

    @staticmethod
    def table_update(from_db: 'LzMySQL', s_table_name: str,
                     target_db: 'LzMySQL', t_table_name: str):
        """
        数据表迁移
        """

        now_datetime_str = LzDateTimeImp.convert_now().to_string('%Y%m%d%H%M')
        bak_table_name = f'bak_{now_datetime_str}_{t_table_name}'
        # 备份数据表
        target_db.execute(f'''
        create table {bak_table_name}
            like {t_table_name};
    
        insert into {bak_table_name}
            select * from {t_table_name};
        ''')

        # 清空数据表
        target_db.execute(f'truncate table {t_table_name}; ')

        count = target_db.query(f'select count(1) as c  from {s_table_name}')[0]['c']
        print(f'{s_table_name} 总共 {count} 条数据, 迁移到 {t_table_name}')

        sep = 100000
        for i in range(0, count, sep):
            data_list = from_db.query(f'select * from {s_table_name} limit {i}, {sep}')
            print(f'迁移 {s_table_name} 第 {i}-{i + sep} 数据中')
            if not data_list:
                continue

            fileds = data_list[0].keys()
            fs1 = ','.join([f'`{ele}`' for ele in fileds])
            fs2 = ','.join(['%s' for ele in fileds])
            sql = f'insert into {t_table_name}({fs1}) values({fs2})'
            datas = [[line_dic[key] for key in fileds] for line_dic in data_list]
            target_db.executemany(sql, datas)

        print(f'{s_table_name} 表数据迁移完成')

    @staticmethod
    def table_update_rollback(target_db: 'LzMySQL', bak_table_name: str):
        """
        将备份的数据表进行复原
        """
        t_table_name = re.compile(r'^bak_\d+_(.*)$').search(bak_table_name).group(1)
        LzMySQL.table_update(target_db, bak_table_name, target_db, t_table_name)
        return True


class JavaBeanInfo(object):
    table_name: str = None
    col_name: str = None
    col_comment: str = None
    col_type: str = None

    def __init__(self, table_name: str, col_name: str, col_type: str = 'varchar', col_comment: str = '') -> None:
        self.table_name = table_name
        self.col_name = col_name
        self.col_comment = col_comment
        self.col_type = col_type


class LzMySQLJava(LzMySQL):
    base_dir: str = None
    out_dir: str = None
    kwargs_dict: dict = {}

    def table_bean(self, table_name: str, package_path: str, base_dir=None, underscore_to_camel_case=False):
        """
        读取MySQL表元数据转化为 java bean
        """
        if base_dir is None:
            MYSQL_TABLE_BEAN_DIR = LzFileDirImp.static_join(TEMP_DIR, 'table_bean')
        else:
            MYSQL_TABLE_BEAN_DIR = base_dir
        LzFileDirImp.static_make_dirs(MYSQL_TABLE_BEAN_DIR)

        self.kwargs_dict['MYSQL_TABLE_MODEL_DIR'] = MYSQL_TABLE_BEAN_DIR
        self.kwargs_dict['table_model_package'] = package_path

        table_meta_info = self.table_meta_data(table_name)
        table_comment = table_meta_info[0]['tbcomment']

        field_str_list = []
        for col_info in table_meta_info:
            colname = col_info['colname']
            colcomment = col_info['colcomment']
            col_type = col_info['col_datatype']
            cs_type = col_info['cs_type']

            col_datatype = LzDataTypeMap.mysql_to_Java(col_type)

            if underscore_to_camel_case is True:
                temp_list = colname.split('_')
                var_field_name = ''.join([temp_list[0]] + [ele.title() for ele in temp_list[1:]])

            else:
                var_field_name = colname

            if cs_type == 'PRIMARY':
                other_str = f'@TableId(value="{colname}", type = IdType.INPUT)'
            else:
                other_str = f'@TableField("{colname}")'

            if col_type == 'datetime':
                other_str += '\n@JsonFormat(pattern = "yyyy-MM-dd")'
            field_str = f"""
            @ApiModelProperty(value = "{colcomment}")
            {other_str}
            private {col_datatype} {var_field_name};
            """
            field_str_list.append(field_str)
        code_field_str = ''.join(field_str_list)
        code_field_str = self.beautiful_string(code_field_str, '	')

        table_name_title = table_name.title()
        self.kwargs_dict = {**self.kwargs_dict, **dict(
            table_comment=table_comment,
            table_name=table_name,
            table_name_title=table_name_title,
            field_str=code_field_str,
        )}

        JavaTableBeanTemplate = LzFileDirImp(
            LzFileDirImp.static_join(CODE_DATA_DIR, 'JavaTableBeanTemplate')).read_context()
        JavaTableBeanTemplate = JavaTableBeanTemplate.format(**self.kwargs_dict)

        # 数据表 bean
        LzFileDirImp(LzFileDirImp.static_join(self.kwargs_dict['MYSQL_TABLE_MODEL_DIR'],
                                              f'{table_name_title}.java')).write_content(
            JavaTableBeanTemplate)

        print(f'文件已生成在 {MYSQL_TABLE_BEAN_DIR}')
        return MYSQL_TABLE_BEAN_DIR

    def table_bean_mapper(self, table_name: str, package_path: str, base_dir=None):
        if base_dir is None:
            MYSQL_TABLE_BEAN_DIR = LzFileDirImp.static_join(TEMP_DIR, 'table_bean')
        else:
            MYSQL_TABLE_BEAN_DIR = base_dir
        LzFileDirImp.static_make_dirs(MYSQL_TABLE_BEAN_DIR)

        MAPPER_DIR = LzFileDirImp.static_join(MYSQL_TABLE_BEAN_DIR, 'mapper')
        LzFileDirImp.static_make_dirs(MAPPER_DIR)

        MAPPER_XML_DIR = LzFileDirImp.static_join(MAPPER_DIR, 'xml')
        LzFileDirImp.static_make_dirs(MAPPER_XML_DIR)

        self.kwargs_dict['MYSQL_TABLE_MAPPER_DIR'] = MAPPER_DIR
        self.kwargs_dict['MYSQL_TABLE_MAPPER_XML_DIR'] = MAPPER_XML_DIR

        self.kwargs_dict['table_mapper_package'] = f'{package_path}.mapper'

        table_meta_info = self.table_meta_data(table_name)
        table_comment = table_meta_info[0]['tbcomment']
        table_name_title = table_name.title()
        self.kwargs_dict = {**self.kwargs_dict, **dict(
            table_comment=table_comment,
            table_name=table_name,
            table_name_title=table_name_title,
        )}
        JavaTableMapperTemplate = LzFileDirImp(
            LzFileDirImp.static_join(CODE_DATA_DIR, 'JavaTableMapperTemplate')).read_context()
        JavaTableMapperTemplate = JavaTableMapperTemplate.format(**self.kwargs_dict)

        JavaTableMapperXmlTemplate = LzFileDirImp(
            LzFileDirImp.static_join(CODE_DATA_DIR, 'JavaTableMapperXmlTemplate')).read_context()
        JavaTableMapperXmlTemplate = JavaTableMapperXmlTemplate.format(**self.kwargs_dict)

        mapper_path = LzFileDirImp.static_join(MAPPER_DIR, f'{table_name_title}Mapper.java')
        mapper_xml_path = LzFileDirImp.static_join(MAPPER_XML_DIR, f'{table_name_title}Mapper.xml')

        LzFileDirImp(mapper_path).write_content(JavaTableMapperTemplate)
        LzFileDirImp(mapper_xml_path).write_content(JavaTableMapperXmlTemplate)
        print(f'文件已生成在 {MYSQL_TABLE_BEAN_DIR}')
        return MYSQL_TABLE_BEAN_DIR

    def table_bean_service(self, table_name: str, package_path: str, base_dir=None):
        if base_dir is None:
            MYSQL_TABLE_BEAN_DIR = LzFileDirImp.static_join(TEMP_DIR, 'table_bean')
        else:
            MYSQL_TABLE_BEAN_DIR = base_dir
        LzFileDirImp.static_make_dirs(MYSQL_TABLE_BEAN_DIR)

        SERVICE_DIR = LzFileDirImp.static_join(MYSQL_TABLE_BEAN_DIR, 'service')
        LzFileDirImp.static_make_dirs(SERVICE_DIR)

        SERVICE_IMPL_DIR = LzFileDirImp.static_join(SERVICE_DIR, 'impl')
        LzFileDirImp.static_make_dirs(SERVICE_IMPL_DIR)

        self.kwargs_dict['MYSQL_TABLE_SERVICE_DIR'] = SERVICE_DIR
        self.kwargs_dict['MYSQL_TABLE_SERVICE_IMPL_DIR'] = SERVICE_IMPL_DIR

        self.kwargs_dict['table_service_package'] = f'{package_path}.service'
        self.kwargs_dict['table_serviceimp_package'] = f'{package_path}.service.impl'

        table_meta_info = self.table_meta_data(table_name)
        table_comment = table_meta_info[0]['tbcomment']
        table_name_title = table_name.title()
        self.kwargs_dict = {**self.kwargs_dict, **dict(
            table_comment=table_comment,
            table_name=table_name,
            table_name_title=table_name_title,
        )}

        JavaTableServiceTemplate = LzFileDirImp(
            LzFileDirImp.static_join(CODE_DATA_DIR, 'JavaTableServiceTemplate')).read_context()
        JavaTableServiceTemplate = JavaTableServiceTemplate.format(**self.kwargs_dict)
        service_path = LzFileDirImp.static_join(SERVICE_DIR, f'{table_name_title}Service.java')
        LzFileDirImp(service_path).write_content(JavaTableServiceTemplate)

        JavaTableServiceImplTemplate = LzFileDirImp(
            LzFileDirImp.static_join(CODE_DATA_DIR, 'JavaTableServiceImplTemplate')).read_context()
        JavaTableServiceImplTemplate = JavaTableServiceImplTemplate.format(**self.kwargs_dict)
        service_impl_path = LzFileDirImp.static_join(SERVICE_IMPL_DIR, f'{table_name_title}ServiceImpl.java')
        LzFileDirImp(service_impl_path).write_content(JavaTableServiceImplTemplate)
        print(f'文件已生成在 {MYSQL_TABLE_BEAN_DIR}')
        return MYSQL_TABLE_BEAN_DIR

    def table_bean_controller(self, table_name: str, package_path: str, base_dir=None):
        if base_dir is None:
            MYSQL_TABLE_BEAN_DIR = LzFileDirImp.static_join(TEMP_DIR, 'table_bean')
        else:
            MYSQL_TABLE_BEAN_DIR = base_dir
        LzFileDirImp.static_make_dirs(MYSQL_TABLE_BEAN_DIR)

        CONTROLLER_DIR = LzFileDirImp.static_join(MYSQL_TABLE_BEAN_DIR, 'controller')
        LzFileDirImp.static_make_dirs(CONTROLLER_DIR)

        self.kwargs_dict['MYSQL_TABLE_CONTROLLER_DIR'] = CONTROLLER_DIR
        self.kwargs_dict['table_controller_package'] = f'{package_path}.controller'

        table_meta_info = self.table_meta_data(table_name)
        table_comment = table_meta_info[0]['tbcomment']
        table_name_title = table_name.title()
        self.kwargs_dict = {**self.kwargs_dict, **dict(
            table_comment=table_comment,
            table_name=table_name,
            table_name_title=table_name_title,
            table_name_lower=table_name.lower()
        )}

        JavaTableControllerTemplate = LzFileDirImp(
            LzFileDirImp.static_join(CODE_DATA_DIR, 'JavaTableControllerTemplate')).read_context()
        JavaTableControllerTemplate = JavaTableControllerTemplate.format(**self.kwargs_dict)
        service_path = LzFileDirImp.static_join(CONTROLLER_DIR, f'{table_name_title}Controller.java')
        LzFileDirImp(service_path).write_content(JavaTableControllerTemplate)

        print(f'文件已生成在 {MYSQL_TABLE_BEAN_DIR}')
        return MYSQL_TABLE_BEAN_DIR

    @staticmethod
    def java_bean_from_dict_data(class_name: str, package_path: str, data_dict: Dict[str, Any]):
        """
        python 字典转Java Bean
        :param class_name:
        :param package_path:
        :param data_dict:
        :return:
        """

        java_bean_template = LzFileDirImp(
            LzFileDirImp.static_join(CODE_DATA_DIR, 'JavaBeanTemplate')).read_context()

        field_str_list = []
        for k, v in data_dict.items():
            field_name = k
            field_type = LzDataTypeMap.python_to_java(v)

            field_str = f"""
                private {field_type} {field_name};
            """
            field_str_list.append(field_str)
        code_field_str = ''.join(field_str_list)
        code_field_str = LzMySQLJava.beautiful_string(code_field_str, '	')

        arg_dict = dict(
            package_path=package_path,
            class_name=class_name.title(),
            field_str=code_field_str,
        )
        java_bean_template = java_bean_template.format(**arg_dict)
        # 在 temp 目录下创建 java 文件
        LzFileDirImp(LzFileDirImp.static_join(TEMP_DIR, class_name.title() + '.java')).write_content(java_bean_template)
        return java_bean_template


# lz = LzMySQL(user='root', password='123456', db='ssm_db')
# # data_lines = lz.query_to_df(
# #     sql='select * from tbl_user',
# # )
# # print(data_lines.columns)
#
# print(pd.DataFrame(lz.table_meta_data()))

# table_field_list = [
#     TableFieldMetaInfo('field1', 'int', primary=True, field_comment='主键字段'),
#     TableFieldMetaInfo('field2', 'varchar(255)'),
#     TableFieldMetaInfo('field3', 'float(7,2)'),
#     TableFieldMetaInfo('field4', 'text'),
# ]
# ti = TableMetaInfo('temp_table', table_field_list, table_comment='临时测试表')
#
# print(LzMySQL.create_sql_table(ti, drop=True))
from pprint import pprint

# for table_name in ['bigtable', 'course', 'score', 'student', 'teacher']:
#     # # 数据转存到MySQL中
#     # table_name = 'bigtable'
#     package_path = 'lazy.cloud.services.vod'
#     # base_dir = r'C:\Users\测试\PycharmProjects\notebook-warehouse\Java\Java8Maven\LazySpringCloud\services\service-vod\src\main\java\lazy\cloud\services\vod'
#     base_dir = None
#     lz = LzMySQLJava(user='root', password='123456', db='datawarehouse')
#
#     code = lz.table_bean(table_name, 'lazy.cloud.common.model.datawarehouse', base_dir=base_dir)
#     lz.table_bean_mapper(table_name, package_path, base_dir=base_dir)
#     lz.table_bean_service(table_name, package_path, base_dir=base_dir)
#     lz.table_bean_controller(table_name, package_path, base_dir=base_dir)

# # 字典数据转 java bean
# LzMySQLJava.java_bean_from_dict_data('Temp', 'lazy.cloud.services.vod.bean', {
#     'field1': '',
#     'field2': [],
#     'field3': 3.14,
# })

# lz = LzMySQL(user='root', password='123456', db='datawarehouse')
# pprint(lz.table_meta_data(table_name))
