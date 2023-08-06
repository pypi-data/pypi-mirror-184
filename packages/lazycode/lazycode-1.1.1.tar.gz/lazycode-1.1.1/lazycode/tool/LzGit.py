from lazycode.core.LzFileDir import LzFileDirImp


def git_make_dir_keep(dir_path: str):
    """
    在所有空文件夹中添加一个 .gitkeep 文件
    :param dir_path:
    :return:
    """
    files = LzFileDirImp.static_deep_walk_all_file(dir_path)
    for file in files:
        if LzFileDirImp.static_is_dir(file) and LzFileDirImp.dir_empty(file):
            keep_file = LzFileDirImp.static_join(file, '.gitkeep')
            print(f'create {keep_file}')
            LzFileDirImp(keep_file).make_file()


def git_remove_dir_keep(dir_path: str):
    files = LzFileDirImp.static_deep_walk_all_file(dir_path)
    for file in files:
        if LzFileDirImp.static_filename(file) == '.gitkeep':
            print(f'remove {file}')
            LzFileDirImp.static_remove_file_dir(file)


# git_make_dir_keep(r'C:\Users\测试\PycharmProjects\notebook-warehouse\Java\Java8Maven')
# git_remove_dir_keep(r'C:\Users\测试\PycharmProjects\notebook-warehouse\Java\Java8Maven')
