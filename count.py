import os


def count_lines_in_file(file):
    with open(file) as fp:
        count = 0
        line = fp.readline()
        while line:
            if not line.strip():
                # Empty line
                line = fp.readline()
                continue
            if not line.startswith('#'):
                count += 1
            line = fp.readline()
        return count


def count_if_py_file(file_path):
    if file_path.split('.')[-1] == 'py':
        print("Coutning", file_path)
        return count_lines_in_file(file_path)
    return 0


def get_all_files_in_folder(start_from, ignore=None):
    list_to_ret = []
    list_of_itmes = os.listdir(start_from)
    for item in list_of_itmes:
        if item in ignore:
            continue
        if os.path.isdir(os.path.join(start_from, item)):
            list_to_ret.extend(get_all_files_in_folder(os.path.join(start_from, item), []))
        else:
            list_to_ret.append(os.path.join(start_from, item))
    return list_to_ret


start_with = os.path.dirname(__file__)
all_files = get_all_files_in_folder(start_with, ignore=['venv'])
total_count = sum(count_if_py_file(file) for file in all_files)
print(total_count)
