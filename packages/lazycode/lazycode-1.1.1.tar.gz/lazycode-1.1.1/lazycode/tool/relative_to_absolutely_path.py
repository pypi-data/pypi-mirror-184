from lazycode.core.LzFileDir import LzFileDirImp
import re


def convert(base_dir: str, safe=False):
    """
    将 from ..common import xxx 导入方式变为 from python.common import xxx
    注意: 如果代码中的 字符串中出现这样的导入语句字符串也会被替换
    """
    base_dir = LzFileDirImp.static_abspath(base_dir)
    if safe:
        new_base_dir = f'{base_dir}_abs'
        LzFileDirImp.static_remove_file_dir(new_base_dir)
        LzFileDirImp(base_dir).deep_copy_file(new_base_dir)
        base_dir = new_base_dir
    base_dir = LzFileDirImp.static_abspath(base_dir)
    cat_base_dir = LzFileDirImp.static_dir_path(base_dir)

    py_files = LzFileDirImp.static_deep_walk_all_file(base_dir)

    import_line_reg = re.compile(r'from +\.+.+')
    import_reg = re.compile(r'from +(\.+)(.*) import')
    for file in py_files:
        if LzFileDirImp.static_is_file(file) and file.lower().endswith('.py'):
            pack_path = LzFileDirImp.static_dir_path(file).replace(cat_base_dir, '').strip('\\').replace('\\', '.')

            file_context = LzFileDirImp(file).read_context()

            import_line_list = import_line_reg.findall(file_context)
            if not import_line_list:
                continue

            for import_line in import_line_list:
                # print(import_line, file)
                import_reg_group = import_reg.search(import_line)
                relative = import_reg_group.group(1)
                relative_other = import_reg_group.group(2)

                pack_path_split = pack_path.split('.')
                end_index = len(pack_path_split) - (len(relative.split('.')) - 2)
                new_pack_path = '.'.join(pack_path_split[:end_index])
                relative_other = f'.{relative_other}' if new_pack_path != '' and relative_other != '' else relative_other

                if new_pack_path == '' and relative_other != '':
                    raise Exception(f'代码中包导入错误 {import_line} {file}')

                new_import_line = f'from {new_pack_path}{relative_other} import'
                new_import_line = import_line.replace(import_reg_group.group(0), new_import_line)

                # print(import_line)
                # print(new_import_line)

                file_context = file_context.replace(import_line, new_import_line)

            LzFileDirImp(file).write_content(file_context)
