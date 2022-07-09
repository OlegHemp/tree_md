from pathlib import Path
from colorama import init


class StructFileSystem:
    def __init__(self, folder="", files='D'):
        """
        ## Description: ##
        Класс формирует и отображает дерево файловой структуры.

        ## :param `folder`: str##
        RAW строка. Если в переменной `folder` указан путь, то, он становится рабочей директорией,
        если, нет, то по умолчанию, берётся текущая директория (см. метод `self.valid_work_folder(folder)`).
        ## :param `files`: str##
        По умолчанию, установлено значение 'D', что означает, что строим дерево без файлов.
        Если, значение 'F' - строим дерево с файлами.

        ## Конструктор: ##
        * `self.work_folder: Union[Path, str]` - рабочая директория. Объект класса Path.
        * `self.dict_path: dict` - словарь, в который будет формироваться файловая структура.
        * `self.sing: list` - список, для хранения отображений элементов дерева.
        * `self.files: str` - определяет, как отображать дерево, файловой системы ('F' - директории и файлы).
        * `self.relative_folder: str` - рабочая директория (относительный путь), преобразованный в строку.
        """
        self.work_folder = self.valid_work_folder(folder)
        self.dict_path = {}
        self.sing = ['.', '├──', '│', '└──', '    ']
        if files == 'F':
            self.files = files
        else:
            self.files = 'D'
        self.relative_folder = str(self.work_folder.relative_to(Path(self.work_folder.parent)))
        # Для colorama
        init()

    def valid_work_folder(self, f):
        """
        ## Description: ##
        ** Проверка** на существование введённого пути и отвечаем на вопрос, является ли указанный  путь директорией?

        Создаём объект класса Path: `p = Path(f)`

        Проверка существования указанного в `f` пути (`Path.exists()`, *True* - существует, *False* - не существует).
        Проверка, на, то, является ли указанный сетевой путь файлом (p.is_file(), если файл, то True).

        ## :param `f`: str##
        путь, вводимый для проверки.

        ## :return: str или Path##
        Если путь не существует или является файлом, возвращаем директорию по умолчанию ("."),
        иначе объект, класса `Path`.
        """
        p = Path(f)
        if p.exists():
            if p.is_file() == False:
                return p
            else:
                print('\033[31m' + f"Указанный путь {p} является файлом!!!" + '\033[39m')
        else:
            print('\033[31m' + f"Директория {p} не существует!!!" + '\033[39m')
        return '.'

    def create_dict_tree(self):
        """
        ## Description: ##
        Метод заполняет словарь `self.dict_path` используя алгоритм BFS - обход в ширину (поиск в ширину, англ. BFS,
        Breadth-first search) — один из простейших алгоритмов обхода графа, являющийся основой для многих важных
        алгоритмов для работы с графами.
        Словарь `self.dict_path` имеет следующую структуру:
        ```python3
        self.dict_path = {'Директория предок':
                                    {'child_dir': [Список потомков (подддиректорий)]},
                                    {'child_file': [Список файлов. содержащихся в дир. предка]}
                        }
        ```
        Пример словаря:
        ```python3
        {'test':
            {'child_dir': ['folder001', 'folder002', 'folder003', 'folder004', 'folder005'],
            'child_file': ['text000000_01.txt']},
         'folder001':
            {'child_dir': ['folder0011', 'folder0012', 'folder0013'],
            'child_file': []},
        ....}
        ```
        В списке `tmp_path`, храним экземпляры класса Path, изначально указываем рабочую директорию. Далее,  в
        бесконечном цикле
        извлекаем предка `parents` из списка `tmp_path` (FIFO). Выход из цикла `while` наступит, тогда, когда,
        при следующей итерации список  `tmp_path` окажется пустым.
        В цикле for, находим поддиректории, преобразуем их в тип данных str, обрезав абсолютный путь и записываем в
        список `child_dir`.
        Если в переменной self.files храниться символ 'F', тогда сохраняем файлы, расположенные в директории предка, в
        словарь `child_file`.
        ## :return: None ##
        """
        tmp_path = [self.work_folder]
        while True:
            if len(tmp_path) == 0:
                break
            parents = tmp_path.pop(0)
            parents_relative = str(parents.relative_to(Path(parents.parent)))
            self.dict_path[parents_relative] = {'child_dir': [], 'child_file': []}
            for child in parents.iterdir():
                if child.is_dir():
                    tmp_path.append(child)
                    self.dict_path[parents_relative]['child_dir'].append(str(child.relative_to(Path(parents))))
                elif child.is_file() and self.files == 'F':
                    self.dict_path[parents_relative]['child_file'].append(str(child.relative_to(Path(parents))))

    def dfs(self, parents, prefix):
        """
        ## Description: ##
        Метод рекурсивно обходит словарь `dict_path` (алгоритм DFS - поиск в глубину), выводя на терминал дерево ФС.
        Базой рекурсии (выход из рекурсии), является условие, когда у предка словарь `child_dir` окажется пустым.

        В цикле "рисуем" директории. Перед вызовом метода `self.dfs(elem, prefix)` сохраняем префикс во временную
        переменную `temp_prefix = prefix` после возврата рекурсии возвращаем значение префикса `prefix = temp_prefix`.
        Далее, осуществляем вывод файлов.

        ## :param parents: ##
        передаём очередного предка.
        ## :param prefix: ##
        передаём префикс.
        ## :return: 1 ##
        """
        temp_parents = self.dict_path.get(parents)
        if temp_parents.get('child_dir') == "":
            return 1
        child_dir_len = len(temp_parents.get('child_dir'))
        child_file_len = len(temp_parents.get('child_file'))
        for ind, elem in enumerate(temp_parents.get('child_dir')):
            if ind == (child_dir_len - 1) and child_file_len == 0 and child_dir_len != 0:
                print(f"{prefix}{self.sing[3]}{elem}  ")
            else:
                print(f"{prefix}{self.sing[1]}{elem}  ")
            temp_prefix = prefix
            if ind == child_dir_len - 1 and child_file_len == 0:
                prefix = prefix + f" {self.sing[4]}"
            else:
                prefix = prefix + f"{self.sing[2]}{self.sing[4]}"
            self.dfs(elem, prefix)
            prefix = temp_prefix
        for ind, elem in enumerate(temp_parents.get('child_file')):
            if ind == child_file_len - 1:
                print(f"{prefix}{self.sing[3]}{elem}  ")
            else:
                print(f"{prefix}{self.sing[1]}{elem}  ")

    def dict_view(self):
        """
        ## Description: ##
        Метод инициализирует построение дерева файловой системы и вывод на экран, предварительно подготовив переменную
        `prefix`.

        `prefix: str` - в переменной, хранятся символы, которые при выводе стоят перед наименованиями директорий  и
        файлов.
        `print(f"\033[34m.  ")` -  указываем цвет для модуля colorama и рисуем точку "." из которой начинаем вывод
        дерева ФС.

        ## :return: None ##
        """
        prefix = ""
        self.create_dict_tree()
        print(f"\033[34m.  ")
        self.dfs(self.relative_folder, prefix)

