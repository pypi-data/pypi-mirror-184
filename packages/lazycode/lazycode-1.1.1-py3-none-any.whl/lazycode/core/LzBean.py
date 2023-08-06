from pydantic import BaseModel, validator
from enum import Enum
from typing import AnyStr, List, Dict, Optional
import re


class LzBean(BaseModel):
    pass


class LzEnum(Enum):
    pass


class TempBean(LzBean):
    # 名称
    name: str
    # 年龄, 默认值
    age: int = 18
    # 性别, 可选参数
    sex: Optional[str]

    # 对 name 字段的输入进行检查是否合法
    @validator("name")
    def name_check(cls, name):
        # 名字只能是字母
        if re.compile(r'^[A-z]+$').search(name):
            return name
        else:
            raise ValueError("name 只能是由字母组成!")


# tb = TempBean(name='abc', age=12)
# print(tb)

# from enum import Enum
# from typing import List, Union
# from datetime import date
# from pydantic import BaseModel
#
#
# class Gender(str, Enum):
#     man = "man"
#     women = "women"
#
#
# class Person(BaseModel):
#     name: str
#     gender: Gender
#
#
# class Department(BaseModel):
#     name: str
#     lead: Person
#     cast: List[Person]
#
#
# class Group(BaseModel):
#     owner: Person
#     member_list: List[Person] = []
#
#
# class Company(BaseModel):
#     name: str
#     owner: Union[Person, Group]
#     regtime: date
#     department_list: List[Department] = []
#
# sales_department = {
#     "name": "sales",
#     "lead": {"name": "Sarah", "gender": "women"},
#     "cast": [
#         {"name": "Sarah", "gender": "women"},
#         {"name": "Bob", "gender": "man"},
#         {"name": "Mary", "gender": "women"}
#     ]
# }
#
# research_department = {
#     "name": "research",
#     "lead": {"name": "Allen", "gender": "man"},
#     "cast": [
#         {"name": "Jane", "gender": "women"},
#         {"name": "Tim", "gender": "man"}
#     ]
# }
#
# company = {
#     "name": "Fantasy",
#     "owner": {"name": "Victor", "gender": "man"},
#     "regtime": "2020-7-23",
#     "department_list": [
#         sales_department,
#         research_department
#     ]
# }
#
# company = Company(**company)
# print(company)