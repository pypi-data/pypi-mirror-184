from lazycode.setting import random_data_file, TEMP_DIR, CODE_DATA_DIR
import json
import os
import re
import random
import datetime
from dateutil import relativedelta
from abc import abstractmethod
from copy import deepcopy
from collections import defaultdict
from pprint import pprint

from typing import List, Dict, Tuple
import pandas as pd
from lazycode.core.LzMySQL import LzMySQL, TableMetaInfo, TableFieldMetaInfo
from lazycode.core.LzDataTypeMap import LzDataTypeMap
from lazycode.core.LzFileDir import LzFileDirImp
from lazycode.core.LzDataFrame import LzDataFrameImp

with open(random_data_file, 'r', encoding='utf-8') as f:
    all_data_dict = json.loads(f.read())


class LzRandomData(object):

    @staticmethod
    def random_university():
        return random.choice(all_data_dict["universitys"])

    @staticmethod
    def random_number(bit_num: int = 10, start_is_zero=False) -> str:
        number = list(map(str, range(0, 10)))
        number_no = list(map(str, range(1, 10)))

        num = random.choice(number_no) if start_is_zero is False else random.choice(number)
        bit_num -= 1
        if bit_num > 0:
            num += ''.join(random.choices(number, k=bit_num))
        return num

    @staticmethod
    def random_name_sex() -> Tuple[str, str, str, str]:
        # 单姓
        firstName = all_data_dict["nameData"]["firstName"]
        # 双姓
        firstNameDouble = all_data_dict["nameData"]["firstNameDouble"]

        # 80% 的单姓
        name_first = random.choice(firstName) if random.randint(1, 100) <= 80 else random.choice(firstNameDouble)

        # 女名
        last_name_girl = all_data_dict["nameData"]["lastNameGirl"]
        last_name_girl_double = ''.join(random.choices(last_name_girl, k=2))

        last_name_boy = all_data_dict["nameData"]["lastNameBoy"]
        last_name_boy_double = ''.join(random.choices(last_name_boy, k=2))

        if random.randint(0, 1) > 0:
            # 80% 双字的名
            name_last = last_name_boy_double if random.randint(1, 100) <= 80 else random.choice(
                last_name_boy)
            sex = '男'
        else:
            name_last = last_name_girl_double if random.randint(1, 100) <= 80 else random.choice(
                last_name_girl)
            sex = '女'

        name = name_first + name_last
        return name_first, name_last, name, sex

    @staticmethod
    def random_city() -> tuple:
        cityList = all_data_dict["cityList"]
        city_level1, city_level2, city_level3 = random.choice(cityList).split("-")
        city_level1, city_level1_code = city_level1.split("_", 1)
        city_level1_code = "{:0<6}".format(city_level1_code)
        city_level2, city_level2_code = city_level2.split("_", 1)
        city_level2_code = "{:0<6}".format(city_level2_code)
        city_level3, city_level3_code = city_level3.split("_", 1)
        city_level3_code = "{:0<6}".format(city_level3_code)

        return city_level1, city_level1_code, city_level2, city_level2_code, city_level3, city_level3_code

    @staticmethod
    def random_datetime(start_datetime: datetime.datetime = None, end_datetime: datetime.datetime = None,
                        fmt='%Y-%m-%d %H:%M:%S.%f') -> datetime.datetime:
        """
        随机生成一个日期
        :param start_datetime: 默认 1940-01-01 00:00:00.00
        :param end_datetime: 默认 now()
        :param fmt:
        :return:
        """
        start_datetime_timestamp = 0 if start_datetime is None else start_datetime.timestamp()
        end_datetime_timestamp = datetime.datetime.now().timestamp() if end_datetime is None else end_datetime.timestamp()

        random_dt = datetime.datetime.fromtimestamp(random.uniform(start_datetime_timestamp, end_datetime_timestamp))

        # str_datetime = random_dt.strftime(fmt=fmt)
        return random_dt

    @staticmethod
    def random_department() -> str:
        return random.choice(all_data_dict["departments"])

    @staticmethod
    def random_phone() -> str:
        """
        随机生成一个11位数的手机号码
        :return:
        """
        phone_pre_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151",
                          "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(phone_pre_list) + "".join(random.choice("0123456789") for i in range(8))

    @staticmethod
    def random_email() -> str:
        emailEnd = random.choice(["@qq.com", "@163.com", "@126.com", "@139.com", "@sohu.com", "@aliyun.com", "@189.cn"])

        # 创建一个长度为[3,10)由 字母或数字组成的字符串
        headStr = LzRandomData.random_symbol(random.randint(5, 10), zztsFlag=False, wordFlag=True, numbersFlag=True,
                                             repeat=False)
        email = headStr + emailEnd
        return email

    @staticmethod
    def random_symbol(count=10, zztsFlag=True, wordFlag=True, numbersFlag=True,
                      repeat=True) -> str:
        """
        随机生成一个字符串
        :param count: 字符长度
        :param zztsFlag: 是否包含标点符号
        :param wordFlag: 是否包含单词
        :param numbersFlag: 是否包含数字
        :param repeat: 是否允许出现重复字符
        :return:
        """

        # 特殊字符ASCII码 `~@#...
        zzts = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

        # 字母ASCII码 abcd...
        words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # 数字ASCII码 012...
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        allSymbol = [zzts, words, numbers]
        allSymbolFlag = [zztsFlag, wordFlag, numbersFlag]
        symbols = []
        for i, e in enumerate(allSymbolFlag):
            if e:
                symbols.extend(allSymbol[i])

        if repeat:
            return "".join(random.choices(symbols, k=count))
        else:
            if count > len(symbols):
                print("非重复的数据过长!")
                return None
            else:
                return "".join(random.sample(symbols, k=count))

    @staticmethod
    def random_chinese_word(count=1, common=True) -> str:
        if common:
            return "".join(random.choices(all_data_dict["commonWords"], k=count))
        else:
            return "".join([chr(random.randint(0x4e00, 0x9fbf)) for i in range(count)])

    @staticmethod
    # 18位身份证号码
    def random_id(city_code: str = None, birth_datetime_code: str = None, sex=None) -> str:
        """
        随机生成一个身份证号码
        :param city_code: 省市县 编码
        :param birth_datetime_code: 出生日期
        :param sex: 性别
        :return:
        """
        sex = random.choice(['男', '女']) if sex is None else sex

        # 地址码6位, 省(2) 市(2) 县/区(2)
        city_code: str = LzRandomData.random_city()[-1] if city_code is None else city_code
        # 出生日期码8位, 年(4) 月(2) 日(2)
        birth_datetime_code: str = LzRandomData.random_datetime().strftime(
            '%Y%m%d') if birth_datetime_code is None else birth_datetime_code

        # 顺序码3位
        sort_code = random.randint(100, 300)
        if (sex == '男') and (sort_code % 2 != 1):
            sort_code += 1
        if (sex == '女') and (sort_code % 2 != 0):
            sort_code += 1
        sort_code = str(sort_code)

        # 校验码1位
        check_code = None

        temp_id = city_code + birth_datetime_code + sort_code
        # 前17位号码权重值
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        sum_weight = sum(list(map(lambda ele: ele[0] * ele[1], list(zip(list(map(int, list(temp_id))), weight)))))
        check_code_map = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        check_code = check_code_map[sum_weight % 11]

        user_id_code = temp_id + check_code
        return user_id_code

    @staticmethod
    def random_url() -> str:
        r_str1 = LzRandomData.random_symbol(zztsFlag=False)
        arg_str = '/'.join(
            [LzRandomData.random_symbol(zztsFlag=False, count=random.randint(2, 10)) for i in
             range(0, random.randint(1, 10))])

        URL = f"http://www.{r_str1}.com/{arg_str}"

        return URL


class LzRandomDataTableLine(object):
    @abstractmethod
    def random_data(self): ...

    @staticmethod
    def get_field_comment(): ...

    def to_dict(self) -> Dict:
        var_members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        member_dict = {var: getattr(self, var) for var in var_members}
        return member_dict

    def field_names(self) -> List:
        return list(self.to_dict().keys())

    def dict_fill(self, data_dict: dict):
        for k, v in data_dict.items():
            setattr(self, k, v)

    def __str__(self) -> str:
        return str(self.to_dict())


class LzRandomDataTable(object):
    field_comment: LzRandomDataTableLine = None
    table_comment: str = None
    table_data: List[LzRandomDataTableLine] = None

    line: LzRandomDataTableLine = None

    def __init__(self, table_len: int = 10) -> None:
        if table_len < 1:
            raise Exception("数据条数必须 > 0")
        self.random_data(table_len)

    def __str__(self):
        return str(self.to_dataframe())

    # 生成随机数据
    def random_data(self, num):
        self.table_data = []
        for i in range(num):
            line_data = deepcopy(self.line.random_data())
            self.table_data.append(line_data)
        return self

    def join_master_field(self, this_table_field: str, master_table: 'LzRandomDataTable', master_table_field: str, ):
        """
        设置当前表字段数据从其他表中获取
        :param master_table: 主表
        :param master_table_field: 主表中关联的字段
        :param this_table_field: 当前表达字段
        :return:
        """
        for line in self.table_data:
            m_line = random.choice(master_table.table_data)
            setattr(line, this_table_field, getattr(m_line, master_table_field))

    def to_dataframe(self, columns_as_comment=False) -> pd.DataFrame:
        """
        转换为DataFrame数据表
        :param columns_as_comment:
        :return:
        """
        df = None
        if columns_as_comment is True:
            columns_dict = self.field_comment.to_dict()
            df = pd.DataFrame([{columns_dict[k]: v for k, v in line.to_dict().items()} for line in self.table_data])
        else:
            df = pd.DataFrame([line.to_dict() for line in self.table_data])
        return df

    def to_list(self) -> List[Dict]:
        """
        将数据转换放在 list 中
        :return:
        """
        return [{k: v for k, v in line.to_dict().items()} for line in self.table_data]

    def create_table(self, lzmysql: LzMySQL, tablemetainfo: 'TableMetaInfo', drop_table=False):
        field_comment_dict = self.field_comment.to_dict()
        field_list = [
            TableFieldMetaInfo(field_name=k, field_type='varchar(255)', field_comment=field_comment_dict.get(k)) for k
            in self.line.field_names()]
        tablemetainfo.set_table_field_list(field_list)
        sql = lzmysql.create_sql_table(tablemetainfo, drop=drop_table)
        lzmysql.execute(sql)
        return True

    def insert_to_mysql_table(self, lzmysql: LzMySQL, tablemetainfo: 'TableMetaInfo'):
        table_name = tablemetainfo.table_name
        db_name = lzmysql.dbname

        fields = self.line.field_names()
        sql_fields = ",".join([f"`{field}`" for field in fields])
        sql_args = ",".join(["%s" for e in fields])
        sql = f'insert into {db_name}.{table_name}({sql_fields}) values ({sql_args})'
        args = [[line.get(field) for field in fields] for line in self.to_list()]

        sep = 10000
        for i in range(0, len(args), sep):
            print(f'向 {table_name} 插入 {i}-{i+sep}')
            lzmysql.executemany(sql, args[i:i + sep])
        return True


class TableLine(LzRandomDataTableLine):
    auto_id: str = None
    id_card: str = None
    name_first: str = None
    name_last: str = None
    name: str = None
    sex: str = None
    university: str = None
    education: str = None
    city_level1: str = None
    city_level1_code: str = None
    city_level2: str = None
    city_level2_code: str = None
    city_level3: str = None
    city_level3_code: str = None
    datetime_pre: str = None
    datetime: str = None
    datetime_last: str = None
    department: str = None
    phone_number: str = None
    email: str = None
    chinese_word: str = None
    symbol: str = None
    url: str = None
    age: str = None
    qq_number: str = None
    is_deleted: str = None
    status: str = None

    @staticmethod
    def get_field_comment() -> 'TableLine':
        field_comment = TableLine()

        field_comment.auto_id = '16位字符随机ID'
        field_comment.id_card = '身份证号'
        field_comment.name_first = '姓'
        field_comment.name_last = '名'
        field_comment.name = '姓名'
        field_comment.sex = '性别'
        field_comment.university = '大学'
        field_comment.education = '学历'
        field_comment.city_level1 = '省级名称'
        field_comment.city_level1_code = '省级编码'
        field_comment.city_level2 = '市级名称'
        field_comment.city_level2_code = '市级编码'
        field_comment.city_level3 = '县/区级名称'
        field_comment.city_level3_code = '县/区级编码'
        field_comment.datetime_pre = '日期前'
        field_comment.datetime = '日期'
        field_comment.datetime_last = '日期后'
        field_comment.department = '部门'
        field_comment.phone_number = '手机号码'
        field_comment.email = '邮箱'
        field_comment.chinese_word = '中文汉字'
        field_comment.symbol = '字符串'
        field_comment.url = '链接'
        field_comment.age = '年龄'
        field_comment.qq_number = 'QQ号码'
        field_comment.is_deleted = '逻辑删除(1:已删除，0:未删除)'
        field_comment.status = '状态'

        return field_comment

    def random_data(self):
        """
        字段随机数据
        :return:
        """

        def __random_add_datetime():
            return relativedelta.relativedelta(years=random.randint(0, 100),
                                               months=random.randint(1, 12),
                                               days=random.randint(1, 30),
                                               hours=random.randint(0, 23),
                                               minute=random.randint(1, 59),
                                               seconds=random.randint(0, 59))

        self.auto_id = LzRandomData.random_symbol(count=16, zztsFlag=False, wordFlag=True, numbersFlag=True)
        self.name_first, self.name_last, self.name, self.sex = LzRandomData.random_name_sex()
        fmt = '%Y-%m-%d %H:%M:%S.%f'
        r_dt = LzRandomData.random_datetime()
        p_dt = r_dt - __random_add_datetime()
        l_dt = r_dt + __random_add_datetime()
        self.datetime = r_dt.strftime(fmt)
        self.datetime_pre = p_dt.strftime(fmt)
        self.datetime_last = l_dt.strftime(fmt)
        self.city_level1, self.city_level1_code, self.city_level2, self.city_level2_code, self.city_level3, self.city_level3_code = LzRandomData.random_city()
        self.id_card = LzRandomData.random_id(city_code=self.city_level3_code,
                                              birth_datetime_code=r_dt.strftime('%Y%m%d'),
                                              sex=self.sex)
        self.university = LzRandomData.random_university()
        self.education = random.choice(['小学', '初中', '高中', '专科', '本科', '硕士', '博士'])
        self.department = LzRandomData.random_department()
        self.phone_number = LzRandomData.random_phone()
        self.email = LzRandomData.random_email()
        self.chinese_word = LzRandomData.random_chinese_word(count=random.randint(3, 15))
        self.symbol = LzRandomData.random_symbol(zztsFlag=False)
        self.url = LzRandomData.random_url()
        self.age = str(random.randint(0, 100))
        self.qq_number = LzRandomData.random_number()
        self.is_deleted = str(random.randint(0, 1))
        self.status = str(random.randint(1, 5))

        return self


class Table(LzRandomDataTable):
    field_comment = TableLine.get_field_comment()
    table_comment: str = '模板数据表'
    line: TableLine = TableLine()


class DefaultCode(LzMySQL):
    def create_default_code(self, table_like='%'):
        table_info = self.table_meta_data(table_like)
        table_dict = defaultdict(list)

        for dic in table_info:
            table_dict[dic['tbname']].append(dic)

        start_index = 0
        reg = re.compile(r'\nclass ')

        LzRandomDataTemplateCode = ''
        for i, (table_name, lis) in enumerate(table_dict.items()):
            table_name_title = table_name.title()
            table_comment = lis[0]['tbcomment']

            filed_default_str = []
            field_comment_str = []
            random_data_str = []

            for ele in lis:
                colname = ele['colname']
                colcomment = ele['colcomment']
                col_datatype = ele['col_datatype']

                filed_default_str.append(f'{colname}: {LzDataTypeMap.mysql_to_python(col_datatype)[0]} = None')
                field_comment_str.append(f'field_comment.{colname} = "{colcomment}"')
                random_data_str.append(f'self.{colname} = None')

            filed_default_str = '\n    '.join(filed_default_str)
            field_comment_str = '\n        '.join(field_comment_str)
            random_data_str = '\n        '.join(random_data_str)

            kwargs = dict(
                table_name_title=table_name_title,
                table_comment=table_comment,
                filed_default_str=filed_default_str,
                field_comment_str=field_comment_str,
                random_data_str=random_data_str,
                table_name=table_name
            )

            RandomDataCodeTemplate = LzFileDirImp(
                LzFileDirImp.static_join(CODE_DATA_DIR, 'RandomDataCodeTemplate')).read_context()
            RandomDataCodeTemplate = RandomDataCodeTemplate[start_index:]
            RandomDataCodeTemplate = RandomDataCodeTemplate.format(**kwargs)
            LzRandomDataTemplateCode += RandomDataCodeTemplate

            if start_index <= 0:
                start_index = reg.search(RandomDataCodeTemplate).span()[0]
        LzFileDirImp(LzFileDirImp.static_join(TEMP_DIR, 'LzRandomDataTemplateCode.py')).write_content(
            LzRandomDataTemplateCode)


# dc = DefaultCode('root', '123456', 'datawarehouse')
# dc.create_default_code()

# create_default_code('root', '123456', 'datawarehouse', 'Student')


# from lazycode.core.LzDataFrame import LzDataFrameImp
# import os
#
# lz = Table(10)
# lzdf = LzDataFrameImp(lz.to_dataframe())
# csv_txt = lzdf.to_text(have_header=True, column_sep='\t')
# with open(os.path.join(TEMP_DIR, 'random_data.csv'), 'w', encoding='utf-8') as f:
#     f.write(csv_txt)


# # 数据于列名称对其，不错行
# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)
# # 显示所有列
# pd.set_option('display.max_columns', None)
# # 限制最多显示10行数据, 设置None表示全部显示
# pd.set_option('display.max_rows', 10)
#
# # 产生数据 写入MySQL
# lz = LzMySQL('root', '123456', 'datawarehouse')
# tmi = TableMetaInfo(table_name='bigtable', table_comment='数据宽表', db_name='datawarehouse')
#
# tb = Table(200)
# tb.create_table(lz, tmi, drop_table=True)
# tb.insert_to_mysql_table(lz, tmi)
#
# print(tb)

import prettytable as pt
import wcwidth
from tabulate import tabulate

# tb = Table(10)
# df: pd.DataFrame = tb.to_dataframe().iloc[:, :4]
#
# print(LzDataFrameImp(df).to_format_text(tablefmt='pipe'))

# print(LzDataFrameImp(tb.to_dataframe().iloc[:, :4]).to_format_text(False))
