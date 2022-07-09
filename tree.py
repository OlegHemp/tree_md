from sfs import StructFileSystem
#str_test = r"C:\python_file\tree_md\test"


def main():
    path = input("Введите директорию:")
    f = input("Введите F, если нужен вывод файлов:")
    ph = StructFileSystem(path, f)
    ph.dict_view()


if __name__ == '__main__':
    main()




