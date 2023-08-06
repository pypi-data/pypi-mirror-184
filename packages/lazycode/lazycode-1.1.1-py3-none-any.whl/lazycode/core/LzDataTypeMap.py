from typing import Any, Callable, Tuple, AnyStr
from lazycode.core.LzDateTime import LzDateTimeImp

from enum import Enum

import datetime


class MySQLDataTypeEnum(Enum):
    VARCHAR = 'varchar'
    TEXT = 'text'

    INT = 'int'
    BIGINT = 'bigint'

    FLOAT = 'double'
    DOUBLE = 'double'
    DECIMAL = 'decimal'

    DATE = 'date'
    DATETIME = 'datetime'


class LzDataTypeMap(object):

    @staticmethod
    def __convert_data(data: Any, convert_fun: Callable):
        if data is None:
            return data
        else:
            return convert_fun(data)

    @staticmethod
    def mysql_to_python(dtype: str, data: Any = None, **kwargs) -> Tuple[AnyStr, Any]:
        """
        MySQL的数据类型转python
        """
        dtype = dtype.strip().lower()

        if dtype in [MySQLDataTypeEnum.VARCHAR.value, MySQLDataTypeEnum.TEXT.value]:
            return 'str', LzDataTypeMap.__convert_data(data, str)
        elif dtype in [MySQLDataTypeEnum.INT.value, MySQLDataTypeEnum.BIGINT.value]:
            return 'int', LzDataTypeMap.__convert_data(data, int)
        elif dtype in [MySQLDataTypeEnum.FLOAT.value, MySQLDataTypeEnum.DOUBLE.value, MySQLDataTypeEnum.DECIMAL.value]:
            return 'float', LzDataTypeMap.__convert_data(data, float)
        elif dtype in [MySQLDataTypeEnum.DATE.value, MySQLDataTypeEnum.DATETIME.value]:
            # 日期格式
            #  YYYY-MM-DD hh:mm:ss.mms -> %y-%m-%d %h:%mi:%s.%ms
            if data is not None:
                data = data.strip()
                date_format_list = kwargs.get('date_format_list', [])
                # 添加默认解析的日期格式
                date_format_list.extend([
                    '%y-%m-%d', '%y/%m/%d',
                    '%h:%mi:%s', '%h:%mi.%s',
                    '%y-%m-%d %h:%mi:%s', '%y/%m/%d %h:%mi.%s', '%y/%m/%d %h:%mi:%s',
                    '%y-%m-%d %h:%mi', '%y/%m/%d %h:%mi',
                    '%y-%m-%d %h:%mi:%s.%ms'
                ])
                for date_format in date_format_list:
                    try:
                        data = LzDateTimeImp().convert_datetime_string_format(data, format_str=date_format).base()
                        break
                    except:
                        pass
                else:
                    raise Exception(f'{data} 日期格式无法解析')
            else:
                return 'datetime', data
        else:
            raise Exception(f'无法识别的数据类型 {dtype}')

    @staticmethod
    def mysql_to_Java(dtype: str, **kwargs) -> AnyStr:
        java_type = None
        if dtype in [MySQLDataTypeEnum.VARCHAR.value, MySQLDataTypeEnum.TEXT.value, ]:
            java_type = 'String'
        elif dtype in [MySQLDataTypeEnum.INT.value, ]:
            java_type = 'Integer'
        elif dtype in [MySQLDataTypeEnum.BIGINT.value, ]:
            java_type = 'BigInteger'
        elif dtype in [MySQLDataTypeEnum.FLOAT.value, ]:
            java_type = 'Float'
        elif dtype in [MySQLDataTypeEnum.DOUBLE.value, ]:
            java_type = 'Double'
        elif dtype in [MySQLDataTypeEnum.DECIMAL.value, ]:
            java_type = 'BigDecimal'
        elif dtype in [MySQLDataTypeEnum.DATE.value, MySQLDataTypeEnum.DATETIME.value]:
            java_type = 'Date'
        else:
            raise Exception(f'无法识别的数据类型 {dtype}')

        return java_type

    @staticmethod
    def python_to_java(py_data: Any) -> str:
        """
        python 数据转 Java类型字符串
        :param py_data:
        :return:
        """

        java_type = None
        if isinstance(py_data, str):
            java_type = 'String'
        elif isinstance(py_data, int):
            java_type = 'Integer'
        elif isinstance(py_data, float):
            java_type = 'Double'
        elif isinstance(py_data, bool):
            java_type = 'Boolean'
        elif isinstance(py_data, dict):
            java_type = 'Map'
        elif isinstance(py_data, list):
            java_type = 'List'
        elif isinstance(py_data, datetime.datetime):
            java_type = 'Date'
        else:
            raise Exception(f'无法识别的数据类型 {py_data}')

        return java_type

# print(LzDataTypeMap.mysql_to_python('datetime'))
