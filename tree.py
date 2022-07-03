import os
from pathlib import Path
from colorama import init
init() # Для colorama
str1 = r"C:\python_file\Skillbox\town_db"
str1_1 = r"C:\python_file\Skillbox\town_db\myapp.py"
str2 = r"/etc/source/kdd"


class StructFileSystem:
    def __init__(self, folder=""):
        """
        work_folder - рабочая директория. Если в переменной folder указан путь, то, он становится рабочей директорией,
        если, нет, то по умолчанию, методом cwd, берётся текущая директория.
        :param folder:
        """
        self.work_folder = self.valid_work_folder(folder)
        self.dict_path = {}
        self.sing = ['.', '├──', '│', '└──', '  ']
        
    def valid_work_folder(self, f):
        """
        Проверка существования указанного в f пути (Path.exists(), True - существует, False - не существует) и проверка,
         на, то, является ли указанный сетевой путь файлом (p.is_file(), если файл, то True). Если путь не существует
         или является строкой, возвращаем директорию по умолчанию (".").
        :param f:
        :return:
        """
        p = Path(f)
        if p.exists():
            if p.is_file()==False:
                return p
            else:
                print('\033[31m' + f"Указанный путь {p} является файлом!!!" + '\033[39m')
        else:
            print('\033[31m' + f"Директория {p} не существует!!!" + '\033[39m')
        return '.'

    def creat_dict(self):
        """

        Формируем список self.dict_path, вида  {'предок': ['потомок1', 'потомок2', ...]}
        tmp_path - список (по сути очередь FIFO), хранящий путь к не обработанным потомкам, текущего предка.
        Изначально, в tmp_path храниться, только путь к рабочей директории.
        Далее в цикле переменной parents будет присваиваться значение нулевого элемента в списке tmp_path, при этом
        нулевой элемент будет удалён из списка.
        С помощью метода iterdir(), перебираем все поддиректории и файлы  и записываем поддиректории текущего предка
        в список subdirs.
        Бесконечный цикл while, будет выполняться, пока в списке tmp_path не останется ни одного элемента.

        :return: None

        """
        #relative_work_folder = self.work_folder.relative_to(Path(self.work_folder.parent))
        #parent_folder = self.work_folder.parent
        self.dict_path = {}
        tmp_path =[self.work_folder]
        #print('\033[34m' + "relative_work_folder =", relative_work_folder, "\nparent_folder =", parent_folder, '\033[39m')
        while True:
            if len(tmp_path) == 0:
                break
            parents = tmp_path.pop(0)
            subdirs = sorted([child for child in parents.iterdir() if child.is_dir()])
            if len(subdirs)>0:
                self.dict_path[str(parents.relative_to(Path(parents.parent)))] = [str(i.relative_to(Path(parents))) for i in subdirs]
                tmp_path = tmp_path + subdirs
            else:
                self.dict_path[str(parents.relative_to(Path(parents.parent)))] = None
        #print("dict_path =", self.dict_path, sep='\n')

    def dict_view(self):
        print("1", self.dict_path)
        self.creat_dict()
        print("2", self.dict_path)


if __name__ == '__main__':
    ph = StructFileSystem(str1)
    print("p.work_folder =", ph.work_folder, type(ph.work_folder))
    #s = input("Введите директорию:")
    #ph.creat_dict()
    ph.dict_view()


