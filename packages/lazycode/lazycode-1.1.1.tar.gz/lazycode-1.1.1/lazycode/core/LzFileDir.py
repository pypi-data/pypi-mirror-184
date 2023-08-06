import os
import shutil
import datetime
import inspect
import zipfile
import pathlib
from typing import Union, List, AnyStr, Dict
import json

from lazycode.decorator.decorator import SafeInfo, SafeOperationInClassMethod


class LzFileDirImp(SafeInfo):
    __path: str = None

    def __init__(self, path: str = None):
        self.init(path)

    def __str__(self) -> str:
        return self.to_string()

    def init(self, path: str):
        self.__path = path

    def to_string(self) -> str:
        return self.__path

    def copy(self):
        return LzFileDirImp(self.__path)

    def obj_class_file_path(self, obj: object):
        """
        获取对象类所在的文件路径
        :param obj:
        :return:
        """
        self.__path = inspect.getfile(obj.__class__)
        return self

    @staticmethod
    def dir_empty(path: str):
        return True if len(os.listdir(path)) == 0 else False

    def make_file(self) -> bool:
        """
        创建文件
        :param encoding:
        :return:
        """
        with open(self.__path, 'wb') as f:
            pass
        return True

    def read_context(self, mode='r', encoding='utf-8') -> Union[bytes, AnyStr]:
        """
        读取文件内容
        :param mode:
        :param encoding:
        :return:
        """
        content = None
        with open(file=self.__path, mode=mode, encoding=encoding) as f:
            content = f.read()
        return content

    @staticmethod
    def static_read_context(path: str, mode='r', encoding='utf-8') -> Union[bytes, AnyStr]:
        return LzFileDirImp(path).read_context(mode, encoding)

    def read_content_json(self, encoding='utf-8') -> Dict:
        return json.loads(self.read_context('r', encoding))

    def write_content(self, content, mode='w', encoding='utf-8') -> bool:
        """
        向文件内写入内容
        :param content:
        :param mode:
        :param encoding:
        :return:
        """
        with open(file=self.__path, mode=mode, encoding=encoding) as f:
            f.write(content)
        return True

    def make_dirs(self) -> bool:
        """
        创建多级目录
        :return:
        """
        if not self.exists():
            os.makedirs(self.__path)
        return True

    @staticmethod
    def static_make_dirs(path: str) -> bool:
        return LzFileDirImp(path).make_dirs()

    def exists(self) -> bool:
        """
        检查文件或目录是否存在
        :return:
        """
        return os.path.exists(self.__path)

    @staticmethod
    def static_exists(path: str) -> bool:
        return LzFileDirImp(path).exists()

    def is_file(self) -> bool:
        """
        是否为文件
        :return:
        """
        return os.path.isfile(self.__path)

    @staticmethod
    def static_is_file(path: str) -> bool:
        return LzFileDirImp(path).is_file()

    def is_dir(self) -> bool:
        """
        是否为目录
        :return:
        """
        return os.path.isdir(self.__path)

    @staticmethod
    def static_is_dir(path: str) -> bool:
        return LzFileDirImp(path).is_dir()

    def rename_file_or_dir(self, new_name: str) -> bool:
        """
        重命名文件或目录
        :param new_name:
        :return:
        """
        print(new_name)
        # new_name = os.path.join(os.path.dirname(self.__path), new_name)
        os.rename(self.__path, new_name)
        return True

    @staticmethod
    def rename_file_or_dir(path: str, new_name: str) -> bool:
        return LzFileDirImp(path).rename_file_or_dir(new_name)

    def remove_file_dir(self) -> bool:
        """
        删除文件或目录
        :return:
        """
        if self.exists():
            if os.path.isfile(self.__path):
                os.remove(self.__path)
            else:
                shutil.rmtree(self.__path)

        return True

    def move(self, new_dir: str) -> str:
        """
        移动文件或目录到指定目录
        :param new_dir:
        :return:
        """
        # if self.exists() and LzFileDirImp.static_exists(new_dir):
        return shutil.move(self.__path, new_dir)

    @staticmethod
    def static_move_files(files: Union[AnyStr, List], dst_dir: AnyStr) -> List:
        res = []
        for file in files:
            r = shutil.move(file, dst_dir)
            res.append(r)
        return res

    @staticmethod
    def static_remove_file_dir(path: str) -> bool:
        return LzFileDirImp(path).remove_file_dir()

    def abspath(self) -> str:
        """
        获取绝对路径
        :return:
        """
        return os.path.abspath(self.__path)

    @staticmethod
    def static_abspath(path: str) -> str:
        return LzFileDirImp(path).abspath()

    def join(self, *paths: str) -> str:
        """
        路径拼接
        :param path:
        :return:
        """
        path = self.__path
        for p in paths:
            path = os.path.join(path, p)
        return path

    @staticmethod
    def static_join(path: str, *paths: str) -> str:
        return LzFileDirImp(path).join(*paths)

    def split_dir_file(self) -> list:
        """
        切分父级目录和文件名
        :return:
        """
        return list(os.path.split(self.__path))

    def dir_path(self) -> str:
        """
        获取文件袋父级目录路径
        :return:
        """
        return os.path.dirname(self.__path)

    @staticmethod
    def static_dir_path(path: str) -> str:
        return LzFileDirImp(path).dir_path()

    def filename(self) -> str:
        """
        获取文件名
        :return:
        """
        return os.path.split(self.__path)[1]

    @staticmethod
    def static_filename(path: str) -> str:
        return LzFileDirImp(path).filename()

    def filename_not_suffix(self) -> str:
        """
        获取文件名, 去掉文件类型后缀
        :return:  file
        """
        return os.path.splitext(os.path.split(self.__path)[1])[0]

    @staticmethod
    def static_filename_not_suffix(path: str) -> str:
        return LzFileDirImp(path).filename_not_suffix()

    def get_drive(self) -> str:
        """
        获取路径盘符驱动名
        :return: D:
        """
        return os.path.splitdrive(self.__path)[0]

    def get_suffix(self) -> str:
        """
        获取文件类型后缀
        :return: .txt
        """
        return os.path.splitext(self.__path)[1]

    # 获取文件, 大小(字节)
    def file_info_filesize(self) -> int:
        return os.stat(self.__path).st_size

    # 文件最后访问 时间
    def file_info_lvtime(self) -> str:
        timestamp = os.stat(self.__path).st_atime
        return datetime.datetime.fromtimestamp(timestamp).strftime(fmt='%Y-%m-%d %H:%M:%S.%f')

    # 文件最后修改 时间
    def file_info_lmtime(self) -> str:
        timestamp = os.stat(self.__path).st_mtime
        return datetime.datetime.fromtimestamp(timestamp).strftime(fmt='%Y-%m-%d %H:%M:%S.%f')

    # 文集创建时间
    def file_info_lctime(self) -> str:
        timestamp = os.stat(self.__path).st_ctime
        return datetime.datetime.fromtimestamp(timestamp).strftime(fmt='%Y-%m-%d %H:%M:%S.%f')

    def deep_copy_file(self, to_path: str) -> str:
        """
        深度复制文件, 包括修改时间
        :param to_path:
        :return:
        """
        if self.is_dir():
            return shutil.copytree(self.__path, to_path)
        else:
            return shutil.copy2(self.__path, to_path)

    def list_dir_files(self) -> list:
        return os.listdir(self.__path)

    def walk(self) -> list:
        """
        递归获取目录下的文件和目录, 包含三个参数 (当前目录路径, 当前目录下的所有目录, 当前目录下的所有文件)
        :return:
        """
        return list(os.walk(self.__path))

    def deep_walk_all_file(self) -> list:
        """
        获取目录下所有的文件和目录
        :return:
        """
        all_file = []
        for path, dirs, files in os.walk(self.__path):
            all_file.append(self.static_abspath(path))
            all_file.extend([self.static_abspath(os.path.join(path, f)) for f in files])
        return all_file

    @staticmethod
    def static_deep_walk_all_file(path: str) -> list:
        return LzFileDirImp(path).deep_walk_all_file()

    @staticmethod
    def static_listdir_abs(dir_path: str):
        return [LzFileDirImp.static_abspath(LzFileDirImp.static_join(dir_path, file)) for file in os.listdir(dir_path)]


class LzFileTool(object):

    @staticmethod
    def unzip_file_deep(zip_file_path: str, unzip_dir_path: str = None):
        unzip_dir_path = LzFileTool.unzip_file(zip_file_path, unzip_dir_path)
        zip_files = [path for path in LzFileDirImp.static_deep_walk_all_file(unzip_dir_path) if
                     path.lower().endswith(".zip")]
        while len(zip_files) > 0:
            for zf in zip_files:
                LzFileTool.unzip_file(zf)
                LzFileDirImp.static_remove_file_dir(zf)
            zip_files = [path for path in LzFileDirImp.static_deep_walk_all_file(unzip_dir_path) if
                         path.lower().endswith(".zip")]
        return unzip_dir_path

    @staticmethod
    def unzip_file(zip_file_path: str, unzip_dir_path: str = None):
        """
        递归解压文件
        """

        zip_file_path = LzFileDirImp.static_abspath(zip_file_path)
        if unzip_dir_path is None:
            unzip_dir_path = LzFileDirImp.static_join(LzFileDirImp.static_dir_path(zip_file_path),
                                                      LzFileDirImp.static_filename_not_suffix(zip_file_path))
        unzip_dir_path = LzFileDirImp.static_abspath(unzip_dir_path)

        LzFileDirImp.static_remove_file_dir(unzip_dir_path)
        LzFileDirImp.static_make_dirs(unzip_dir_path)

        with zipfile.ZipFile(zip_file_path) as zf:
            zf = zipfile.ZipFile(zip_file_path)
            for name in zf.namelist():
                zf.extract(name, unzip_dir_path)
                # print(unzip_dir_path, name)

                # file_path = LzFileDirImp.static_join(unzip_dir_path)
                # zipfile 默认只能识别 cp437, utf-8 编码的路径, 而window默认为 gbk编码
                temp_name = name
                while len(temp_name) > 0:
                    d, f = os.path.split(temp_name)
                    try:
                        # 使用cp437对文件名进行解码还原
                        new_name = f.encode('cp437')
                        # win下一般使用的是gbk编码
                        new_name = new_name.decode("gbk")
                        # print(f,new_name, f != new_name)

                        # 需要转码
                        if f != new_name:
                            old_path = LzFileDirImp.static_join(unzip_dir_path, d, f)
                            new_path = LzFileDirImp.static_join(unzip_dir_path, d, new_name)
                            if LzFileDirImp.static_exists(new_path):
                                LzFileDirImp.static_move_files(LzFileDirImp.static_listdir_abs(old_path), new_path)
                                LzFileDirImp.static_remove_file_dir(old_path)
                            else:
                                os.rename(old_path, new_path)
                    except Exception as e:
                        print(e)
                    temp_name = d

        return unzip_dir_path

    @staticmethod
    def an_garcode(dir_path, curr_encoding, convert_encoding):
        """anti garbled code"""
        print(dir_path)
        dir_path = LzFileDirImp.static_abspath(dir_path)
        for file_name in os.listdir(dir_path):
            try:
                # 使用cp437对文件名进行解码还原
                new_name = file_name.encode(curr_encoding)
                # win下一般使用的是gbk编码
                new_name = new_name.decode(convert_encoding)

                # 重命名文件
                file_path_old = LzFileDirImp.static_join(dir_path, file_name)
                file_path_new = LzFileDirImp.static_join(dir_path, new_name)
                os.rename(file_path_old, file_path_new)
                file_name = new_name
            except:
                # 如果已被正确识别为utf8编码时则不需再编码
                print(f'{file_name} 转换失败')
                pass

            file_path = LzFileDirImp.static_join(dir_path, file_name)
            if os.path.isdir(file_path):
                # 对子文件夹进行递归调用
                LzFileTool.an_garcode(file_path, curr_encoding, convert_encoding)
        return dir_path

# lz = LzFileDirImp()
# print(LzFileDirImp.abspath())
