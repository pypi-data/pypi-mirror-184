from lazycode.core.LzFileDir import LzFileDirImp
import re


def convert_tree_context(context):
    """
dir1
    sub1
        sub1_1
            sub1_1_1
            .gitkeep
    sub2
        sub2_2
        abc.txt
    sub3

dir2
dir3
    """
    paths = []
    level_tree = list(['' for e in range(20)])
    for line in context.split('\n'):
        if len(line.strip()) == 0:
            continue
        line = line.replace('    ', '\t').split('\t')
        for i, ele in enumerate(line):
            if ele.strip() == '':
                continue
            level_tree[i] = ele

        path = '/'.join(level_tree[0: len(line)])
        paths.append(path)

    return paths


def make_file_dir(paths: list):
    file_reg = re.compile(r'\..*?$')
    for path in paths:
        # 创建空文件
        if file_reg.search(path) is not None:
            LzFileDirImp(path).make_file()
        else:
            LzFileDirImp.static_make_dirs(path)


# context = """
# dir1
#     sub1
#         sub1_1
#             sub1_1_1
#             .gitkeep
#     sub2
#         sub2_2
#         abc.txt
#     sub3
#
# dir2
# dir3
# """
# paths = convert_tree_context(context)
# make_file_dir(paths)
