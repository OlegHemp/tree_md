<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>sfs API documentation</title>
<meta name="description" content="" />
<link rel="preload stylesheet" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/sanitize.min.css" integrity="sha256-PK9q560IAAa6WVRRh76LtCaI8pjTJ2z11v0miyNNjrs=" crossorigin>
<link rel="preload stylesheet" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/typography.min.css" integrity="sha256-7l/o7C8jubJiy74VsKTidCy1yBkRtiUGbVkYBylBqUg=" crossorigin>
<link rel="stylesheet preload" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/github.min.css" crossorigin>
<style>:root{--highlight-color:#fe9}.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}h1:target,h2:target,h3:target,h4:target,h5:target,h6:target{background:var(--highlight-color);padding:.2em 0}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}dt:target .name{background:var(--highlight-color)}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}td{padding:0 .5em}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js" integrity="sha256-Uv3H6lx7dJmRfRvH8TH6kJD1TSK1aFcwgx+mdg3epi8=" crossorigin></script>
<script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
</head>
<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>sfs</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from pathlib import Path
from colorama import init


class StructFileSystem:
    def __init__(self, folder=&#34;&#34;, files=&#39;D&#39;):
        &#34;&#34;&#34;
        ## Description: ##
        Класс формирует и отображает дерево файловой структуры.

        ## :param `folder`: str##
        RAW строка. Если в переменной `folder` указан путь, то, он становится рабочей директорией,
        если, нет, то по умолчанию, берётся текущая директория (см. метод `self.valid_work_folder(folder)`).
        ## :param `files`: str##
        По умолчанию, установлено значение &#39;D&#39;, что означает, что строим дерево без файлов.
        Если, значение &#39;F&#39; - строим дерево с файлами.

        ## Конструктор: ##
        * `self.work_folder: Union[Path, str]` - рабочая директория. Объект класса Path.
        * `self.dict_path: dict` - словарь, в который будет формироваться файловая структура.
        * `self.sing: list` - список, для хранения отображений элементов дерева.
        * `self.files: str` - определяет, как отображать дерево, файловой системы (&#39;F&#39; - директории и файлы).
        * `self.relative_folder: str` - рабочая директория (относительный путь), преобразованный в строку.
        &#34;&#34;&#34;
        self.work_folder = self.valid_work_folder(folder)
        self.dict_path = {}
        self.sing = [&#39;.&#39;, &#39;├──&#39;, &#39;│&#39;, &#39;└──&#39;, &#39;    &#39;]
        if files == &#39;F&#39;:
            self.files = files
        else:
            self.files = &#39;D&#39;
        self.relative_folder = str(self.work_folder.relative_to(Path(self.work_folder.parent)))
        # Для colorama
        init()

    def valid_work_folder(self, f):
        &#34;&#34;&#34;
        ## Description: ##
        ** Проверка** на существование введённого пути и отвечаем на вопрос, является ли указанный  путь директорией?

        Создаём объект класса Path: `p = Path(f)`

        Проверка существования указанного в `f` пути (`Path.exists()`, *True* - существует, *False* - не существует).
        Проверка, на, то, является ли указанный сетевой путь файлом (p.is_file(), если файл, то True).

        ## :param `f`: str##
        путь, вводимый для проверки.

        ## :return: str или Path##
        Если путь не существует или является файлом, возвращаем директорию по умолчанию (&#34;.&#34;),
        иначе объект, класса `Path`.
        &#34;&#34;&#34;
        p = Path(f)
        if p.exists():
            if p.is_file() == False:
                return p
            else:
                print(&#39;\033[31m&#39; + f&#34;Указанный путь {p} является файлом!!!&#34; + &#39;\033[39m&#39;)
        else:
            print(&#39;\033[31m&#39; + f&#34;Директория {p} не существует!!!&#34; + &#39;\033[39m&#39;)
        return &#39;.&#39;

    def create_dict_tree(self):
        &#34;&#34;&#34;
        ## Description: ##
        Метод заполняет словарь `self.dict_path` используя алгоритм BFS - обход в ширину (поиск в ширину, англ. BFS,
        Breadth-first search) — один из простейших алгоритмов обхода графа, являющийся основой для многих важных
        алгоритмов для работы с графами.
        Словарь `self.dict_path` имеет следующую структуру:
        ```python3
        self.dict_path = {&#39;Директория предок&#39;:
                                    {&#39;child_dir&#39;: [Список потомков (подддиректорий)]},
                                    {&#39;child_file&#39;: [Список файлов. содержащихся в дир. предка]}
                        }
        ```
        Пример словаря:
        ```python3
        {&#39;test&#39;:
            {&#39;child_dir&#39;: [&#39;folder001&#39;, &#39;folder002&#39;, &#39;folder003&#39;, &#39;folder004&#39;, &#39;folder005&#39;],
            &#39;child_file&#39;: [&#39;text000000_01.txt&#39;]},
         &#39;folder001&#39;:
            {&#39;child_dir&#39;: [&#39;folder0011&#39;, &#39;folder0012&#39;, &#39;folder0013&#39;],
            &#39;child_file&#39;: []},
        ....}
        ```
        В списке `tmp_path`, храним экземпляры класса Path, изначально указываем рабочую директорию. Далее,  в
        бесконечном цикле
        извлекаем предка `parents` из списка `tmp_path` (FIFO). Выход из цикла `while` наступит, тогда, когда,
        при следующей итерации список  `tmp_path` окажется пустым.
        В цикле for, находим поддиректории, преобразуем их в тип данных str, обрезав абсолютный путь и записываем в
        список `child_dir`.
        Если в переменной self.files храниться символ &#39;F&#39;, тогда сохраняем файлы, расположенные в директории предка, в
        словарь `child_file`.
        ## :return: None ##
        &#34;&#34;&#34;
        tmp_path = [self.work_folder]
        while True:
            if len(tmp_path) == 0:
                break
            parents = tmp_path.pop(0)
            parents_relative = str(parents.relative_to(Path(parents.parent)))
            self.dict_path[parents_relative] = {&#39;child_dir&#39;: [], &#39;child_file&#39;: []}
            for child in parents.iterdir():
                if child.is_dir():
                    tmp_path.append(child)
                    self.dict_path[parents_relative][&#39;child_dir&#39;].append(str(child.relative_to(Path(parents))))
                elif child.is_file() and self.files == &#39;F&#39;:
                    self.dict_path[parents_relative][&#39;child_file&#39;].append(str(child.relative_to(Path(parents))))

    def dfs(self, parents, prefix):
        &#34;&#34;&#34;
        ## Description: ##
        Метод рекурсивно обходит словарь `dict_path` (алгоритм DFS - поиск в глубину), выводя на терминал дерево ФС.
        Базой рекурсии (выход из рекурсии), является условие, когда у предка словарь `child_dir` окажется пустым.

        В цикле &#34;рисуем&#34; директории. Перед вызовом метода `self.dfs(elem, prefix)` сохраняем префикс во временную
        переменную `temp_prefix = prefix` после возврата рекурсии возвращаем значение префикса `prefix = temp_prefix`.
        Далее, осуществляем вывод файлов.

        ## :param parents: ##
        передаём очередного предка.
        ## :param prefix: ##
        передаём префикс.
        ## :return: 1 ##
        &#34;&#34;&#34;
        temp_parents = self.dict_path.get(parents)
        if temp_parents.get(&#39;child_dir&#39;) == &#34;&#34;:
            return 1
        child_dir_len = len(temp_parents.get(&#39;child_dir&#39;))
        child_file_len = len(temp_parents.get(&#39;child_file&#39;))
        for ind, elem in enumerate(temp_parents.get(&#39;child_dir&#39;)):
            if ind == (child_dir_len - 1) and child_file_len == 0 and child_dir_len != 0:
                print(f&#34;{prefix}{self.sing[3]}{elem}  &#34;)
            else:
                print(f&#34;{prefix}{self.sing[1]}{elem}  &#34;)
            temp_prefix = prefix
            if ind == child_dir_len - 1 and child_file_len == 0:
                prefix = prefix + f&#34; {self.sing[4]}&#34;
            else:
                prefix = prefix + f&#34;{self.sing[2]}{self.sing[4]}&#34;
            self.dfs(elem, prefix)
            prefix = temp_prefix
        for ind, elem in enumerate(temp_parents.get(&#39;child_file&#39;)):
            if ind == child_file_len - 1:
                print(f&#34;{prefix}{self.sing[3]}{elem}  &#34;)
            else:
                print(f&#34;{prefix}{self.sing[1]}{elem}  &#34;)

    def dict_view(self):
        &#34;&#34;&#34;
        ## Description: ##
        Метод инициализирует построение дерева файловой системы и вывод на экран, предварительно подготовив переменную
        `prefix`.

        `prefix: str` - в переменной, хранятся символы, которые при выводе стоят перед наименованиями директорий  и
        файлов.
        `print(f&#34;\033[34m.  &#34;)` -  указываем цвет для модуля colorama и рисуем точку &#34;.&#34; из которой начинаем вывод
        дерева ФС.

        ## :return: None ##
        &#34;&#34;&#34;
        prefix = &#34;&#34;
        self.create_dict_tree()
        print(f&#34;\033[34m.  &#34;)
        self.dfs(self.relative_folder, prefix)</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="sfs.StructFileSystem"><code class="flex name class">
<span>class <span class="ident">StructFileSystem</span></span>
<span>(</span><span>folder='', files='D')</span>
</code></dt>
<dd>
<div class="desc"><h2 id="description">Description:</h2>
<p>Класс формирует и отображает дерево файловой структуры.</p>
<h2 id="param-folder-str">:param <code>folder</code>: str</h2>
<p>RAW строка. Если в переменной <code>folder</code> указан путь, то, он становится рабочей директорией,
если, нет, то по умолчанию, берётся текущая директория (см. метод <code>self.valid_work_folder(folder)</code>).</p>
<h2 id="param-files-str">:param <code>files</code>: str</h2>
<p>По умолчанию, установлено значение 'D', что означает, что строим дерево без файлов.
Если, значение 'F' - строим дерево с файлами.</p>
<h2 id="_1">Конструктор:</h2>
<ul>
<li><code>self.work_folder: Union[Path, str]</code> - рабочая директория. Объект класса Path.</li>
<li><code>self.dict_path: dict</code> - словарь, в который будет формироваться файловая структура.</li>
<li><code>self.sing: list</code> - список, для хранения отображений элементов дерева.</li>
<li><code>self.files: str</code> - определяет, как отображать дерево, файловой системы ('F' - директории и файлы).</li>
<li><code>self.relative_folder: str</code> - рабочая директория (относительный путь), преобразованный в строку.</li>
</ul></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class StructFileSystem:
    def __init__(self, folder=&#34;&#34;, files=&#39;D&#39;):
        &#34;&#34;&#34;
        ## Description: ##
        Класс формирует и отображает дерево файловой структуры.

        ## :param `folder`: str##
        RAW строка. Если в переменной `folder` указан путь, то, он становится рабочей директорией,
        если, нет, то по умолчанию, берётся текущая директория (см. метод `self.valid_work_folder(folder)`).
        ## :param `files`: str##
        По умолчанию, установлено значение &#39;D&#39;, что означает, что строим дерево без файлов.
        Если, значение &#39;F&#39; - строим дерево с файлами.

        ## Конструктор: ##
        * `self.work_folder: Union[Path, str]` - рабочая директория. Объект класса Path.
        * `self.dict_path: dict` - словарь, в который будет формироваться файловая структура.
        * `self.sing: list` - список, для хранения отображений элементов дерева.
        * `self.files: str` - определяет, как отображать дерево, файловой системы (&#39;F&#39; - директории и файлы).
        * `self.relative_folder: str` - рабочая директория (относительный путь), преобразованный в строку.
        &#34;&#34;&#34;
        self.work_folder = self.valid_work_folder(folder)
        self.dict_path = {}
        self.sing = [&#39;.&#39;, &#39;├──&#39;, &#39;│&#39;, &#39;└──&#39;, &#39;    &#39;]
        if files == &#39;F&#39;:
            self.files = files
        else:
            self.files = &#39;D&#39;
        self.relative_folder = str(self.work_folder.relative_to(Path(self.work_folder.parent)))
        # Для colorama
        init()

    def valid_work_folder(self, f):
        &#34;&#34;&#34;
        ## Description: ##
        ** Проверка** на существование введённого пути и отвечаем на вопрос, является ли указанный  путь директорией?

        Создаём объект класса Path: `p = Path(f)`

        Проверка существования указанного в `f` пути (`Path.exists()`, *True* - существует, *False* - не существует).
        Проверка, на, то, является ли указанный сетевой путь файлом (p.is_file(), если файл, то True).

        ## :param `f`: str##
        путь, вводимый для проверки.

        ## :return: str или Path##
        Если путь не существует или является файлом, возвращаем директорию по умолчанию (&#34;.&#34;),
        иначе объект, класса `Path`.
        &#34;&#34;&#34;
        p = Path(f)
        if p.exists():
            if p.is_file() == False:
                return p
            else:
                print(&#39;\033[31m&#39; + f&#34;Указанный путь {p} является файлом!!!&#34; + &#39;\033[39m&#39;)
        else:
            print(&#39;\033[31m&#39; + f&#34;Директория {p} не существует!!!&#34; + &#39;\033[39m&#39;)
        return &#39;.&#39;

    def create_dict_tree(self):
        &#34;&#34;&#34;
        ## Description: ##
        Метод заполняет словарь `self.dict_path` используя алгоритм BFS - обход в ширину (поиск в ширину, англ. BFS,
        Breadth-first search) — один из простейших алгоритмов обхода графа, являющийся основой для многих важных
        алгоритмов для работы с графами.
        Словарь `self.dict_path` имеет следующую структуру:
        ```python3
        self.dict_path = {&#39;Директория предок&#39;:
                                    {&#39;child_dir&#39;: [Список потомков (подддиректорий)]},
                                    {&#39;child_file&#39;: [Список файлов. содержащихся в дир. предка]}
                        }
        ```
        Пример словаря:
        ```python3
        {&#39;test&#39;:
            {&#39;child_dir&#39;: [&#39;folder001&#39;, &#39;folder002&#39;, &#39;folder003&#39;, &#39;folder004&#39;, &#39;folder005&#39;],
            &#39;child_file&#39;: [&#39;text000000_01.txt&#39;]},
         &#39;folder001&#39;:
            {&#39;child_dir&#39;: [&#39;folder0011&#39;, &#39;folder0012&#39;, &#39;folder0013&#39;],
            &#39;child_file&#39;: []},
        ....}
        ```
        В списке `tmp_path`, храним экземпляры класса Path, изначально указываем рабочую директорию. Далее,  в
        бесконечном цикле
        извлекаем предка `parents` из списка `tmp_path` (FIFO). Выход из цикла `while` наступит, тогда, когда,
        при следующей итерации список  `tmp_path` окажется пустым.
        В цикле for, находим поддиректории, преобразуем их в тип данных str, обрезав абсолютный путь и записываем в
        список `child_dir`.
        Если в переменной self.files храниться символ &#39;F&#39;, тогда сохраняем файлы, расположенные в директории предка, в
        словарь `child_file`.
        ## :return: None ##
        &#34;&#34;&#34;
        tmp_path = [self.work_folder]
        while True:
            if len(tmp_path) == 0:
                break
            parents = tmp_path.pop(0)
            parents_relative = str(parents.relative_to(Path(parents.parent)))
            self.dict_path[parents_relative] = {&#39;child_dir&#39;: [], &#39;child_file&#39;: []}
            for child in parents.iterdir():
                if child.is_dir():
                    tmp_path.append(child)
                    self.dict_path[parents_relative][&#39;child_dir&#39;].append(str(child.relative_to(Path(parents))))
                elif child.is_file() and self.files == &#39;F&#39;:
                    self.dict_path[parents_relative][&#39;child_file&#39;].append(str(child.relative_to(Path(parents))))

    def dfs(self, parents, prefix):
        &#34;&#34;&#34;
        ## Description: ##
        Метод рекурсивно обходит словарь `dict_path` (алгоритм DFS - поиск в глубину), выводя на терминал дерево ФС.
        Базой рекурсии (выход из рекурсии), является условие, когда у предка словарь `child_dir` окажется пустым.

        В цикле &#34;рисуем&#34; директории. Перед вызовом метода `self.dfs(elem, prefix)` сохраняем префикс во временную
        переменную `temp_prefix = prefix` после возврата рекурсии возвращаем значение префикса `prefix = temp_prefix`.
        Далее, осуществляем вывод файлов.

        ## :param parents: ##
        передаём очередного предка.
        ## :param prefix: ##
        передаём префикс.
        ## :return: 1 ##
        &#34;&#34;&#34;
        temp_parents = self.dict_path.get(parents)
        if temp_parents.get(&#39;child_dir&#39;) == &#34;&#34;:
            return 1
        child_dir_len = len(temp_parents.get(&#39;child_dir&#39;))
        child_file_len = len(temp_parents.get(&#39;child_file&#39;))
        for ind, elem in enumerate(temp_parents.get(&#39;child_dir&#39;)):
            if ind == (child_dir_len - 1) and child_file_len == 0 and child_dir_len != 0:
                print(f&#34;{prefix}{self.sing[3]}{elem}  &#34;)
            else:
                print(f&#34;{prefix}{self.sing[1]}{elem}  &#34;)
            temp_prefix = prefix
            if ind == child_dir_len - 1 and child_file_len == 0:
                prefix = prefix + f&#34; {self.sing[4]}&#34;
            else:
                prefix = prefix + f&#34;{self.sing[2]}{self.sing[4]}&#34;
            self.dfs(elem, prefix)
            prefix = temp_prefix
        for ind, elem in enumerate(temp_parents.get(&#39;child_file&#39;)):
            if ind == child_file_len - 1:
                print(f&#34;{prefix}{self.sing[3]}{elem}  &#34;)
            else:
                print(f&#34;{prefix}{self.sing[1]}{elem}  &#34;)

    def dict_view(self):
        &#34;&#34;&#34;
        ## Description: ##
        Метод инициализирует построение дерева файловой системы и вывод на экран, предварительно подготовив переменную
        `prefix`.

        `prefix: str` - в переменной, хранятся символы, которые при выводе стоят перед наименованиями директорий  и
        файлов.
        `print(f&#34;\033[34m.  &#34;)` -  указываем цвет для модуля colorama и рисуем точку &#34;.&#34; из которой начинаем вывод
        дерева ФС.

        ## :return: None ##
        &#34;&#34;&#34;
        prefix = &#34;&#34;
        self.create_dict_tree()
        print(f&#34;\033[34m.  &#34;)
        self.dfs(self.relative_folder, prefix)</code></pre>
</details>
<h3>Methods</h3>
<dl>
<dt id="sfs.StructFileSystem.create_dict_tree"><code class="name flex">
<span>def <span class="ident">create_dict_tree</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"><h2 id="description">Description:</h2>
<p>Метод заполняет словарь <code>self.dict_path</code> используя алгоритм BFS - обход в ширину (поиск в ширину, англ. BFS,
Breadth-first search) — один из простейших алгоритмов обхода графа, являющийся основой для многих важных
алгоритмов для работы с графами.
Словарь <code>self.dict_path</code> имеет следующую структуру:</p>
<pre><code class="language-python3">self.dict_path = {'Директория предок':
                            {'child_dir': [Список потомков (подддиректорий)]},
                            {'child_file': [Список файлов. содержащихся в дир. предка]}
                }
</code></pre>
<p>Пример словаря:</p>
<pre><code class="language-python3">{'test':
    {'child_dir': ['folder001', 'folder002', 'folder003', 'folder004', 'folder005'],
    'child_file': ['text000000_01.txt']},
 'folder001':
    {'child_dir': ['folder0011', 'folder0012', 'folder0013'],
    'child_file': []},
....}
</code></pre>
<p>В списке <code>tmp_path</code>, храним экземпляры класса Path, изначально указываем рабочую директорию. Далее,
в
бесконечном цикле
извлекаем предка <code>parents</code> из списка <code>tmp_path</code> (FIFO). Выход из цикла <code>while</code> наступит, тогда, когда,
при следующей итерации список
<code>tmp_path</code> окажется пустым.
В цикле for, находим поддиректории, преобразуем их в тип данных str, обрезав абсолютный путь и записываем в
список <code>child_dir</code>.
Если в переменной self.files храниться символ 'F', тогда сохраняем файлы, расположенные в директории предка, в
словарь <code>child_file</code>.</p>
<h2 id="return-none">:return: None</h2></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def create_dict_tree(self):
    &#34;&#34;&#34;
    ## Description: ##
    Метод заполняет словарь `self.dict_path` используя алгоритм BFS - обход в ширину (поиск в ширину, англ. BFS,
    Breadth-first search) — один из простейших алгоритмов обхода графа, являющийся основой для многих важных
    алгоритмов для работы с графами.
    Словарь `self.dict_path` имеет следующую структуру:
    ```python3
    self.dict_path = {&#39;Директория предок&#39;:
                                {&#39;child_dir&#39;: [Список потомков (подддиректорий)]},
                                {&#39;child_file&#39;: [Список файлов. содержащихся в дир. предка]}
                    }
    ```
    Пример словаря:
    ```python3
    {&#39;test&#39;:
        {&#39;child_dir&#39;: [&#39;folder001&#39;, &#39;folder002&#39;, &#39;folder003&#39;, &#39;folder004&#39;, &#39;folder005&#39;],
        &#39;child_file&#39;: [&#39;text000000_01.txt&#39;]},
     &#39;folder001&#39;:
        {&#39;child_dir&#39;: [&#39;folder0011&#39;, &#39;folder0012&#39;, &#39;folder0013&#39;],
        &#39;child_file&#39;: []},
    ....}
    ```
    В списке `tmp_path`, храним экземпляры класса Path, изначально указываем рабочую директорию. Далее,  в
    бесконечном цикле
    извлекаем предка `parents` из списка `tmp_path` (FIFO). Выход из цикла `while` наступит, тогда, когда,
    при следующей итерации список  `tmp_path` окажется пустым.
    В цикле for, находим поддиректории, преобразуем их в тип данных str, обрезав абсолютный путь и записываем в
    список `child_dir`.
    Если в переменной self.files храниться символ &#39;F&#39;, тогда сохраняем файлы, расположенные в директории предка, в
    словарь `child_file`.
    ## :return: None ##
    &#34;&#34;&#34;
    tmp_path = [self.work_folder]
    while True:
        if len(tmp_path) == 0:
            break
        parents = tmp_path.pop(0)
        parents_relative = str(parents.relative_to(Path(parents.parent)))
        self.dict_path[parents_relative] = {&#39;child_dir&#39;: [], &#39;child_file&#39;: []}
        for child in parents.iterdir():
            if child.is_dir():
                tmp_path.append(child)
                self.dict_path[parents_relative][&#39;child_dir&#39;].append(str(child.relative_to(Path(parents))))
            elif child.is_file() and self.files == &#39;F&#39;:
                self.dict_path[parents_relative][&#39;child_file&#39;].append(str(child.relative_to(Path(parents))))</code></pre>
</details>
</dd>
<dt id="sfs.StructFileSystem.dfs"><code class="name flex">
<span>def <span class="ident">dfs</span></span>(<span>self, parents, prefix)</span>
</code></dt>
<dd>
<div class="desc"><h2 id="description">Description:</h2>
<p>Метод рекурсивно обходит словарь <code>dict_path</code> (алгоритм DFS - поиск в глубину), выводя на терминал дерево ФС.
Базой рекурсии (выход из рекурсии), является условие, когда у предка словарь <code>child_dir</code> окажется пустым.</p>
<p>В цикле "рисуем" директории. Перед вызовом метода <code>self.dfs(elem, prefix)</code> сохраняем префикс во временную
переменную <code>temp_prefix = prefix</code> после возврата рекурсии возвращаем значение префикса <code>prefix = temp_prefix</code>.
Далее, осуществляем вывод файлов.</p>
<h2 id="param-parents">:param parents:</h2>
<p>передаём очередного предка.</p>
<h2 id="param-prefix">:param prefix:</h2>
<p>передаём префикс.</p>
<h2 id="return-1">:return: 1</h2></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def dfs(self, parents, prefix):
    &#34;&#34;&#34;
    ## Description: ##
    Метод рекурсивно обходит словарь `dict_path` (алгоритм DFS - поиск в глубину), выводя на терминал дерево ФС.
    Базой рекурсии (выход из рекурсии), является условие, когда у предка словарь `child_dir` окажется пустым.

    В цикле &#34;рисуем&#34; директории. Перед вызовом метода `self.dfs(elem, prefix)` сохраняем префикс во временную
    переменную `temp_prefix = prefix` после возврата рекурсии возвращаем значение префикса `prefix = temp_prefix`.
    Далее, осуществляем вывод файлов.

    ## :param parents: ##
    передаём очередного предка.
    ## :param prefix: ##
    передаём префикс.
    ## :return: 1 ##
    &#34;&#34;&#34;
    temp_parents = self.dict_path.get(parents)
    if temp_parents.get(&#39;child_dir&#39;) == &#34;&#34;:
        return 1
    child_dir_len = len(temp_parents.get(&#39;child_dir&#39;))
    child_file_len = len(temp_parents.get(&#39;child_file&#39;))
    for ind, elem in enumerate(temp_parents.get(&#39;child_dir&#39;)):
        if ind == (child_dir_len - 1) and child_file_len == 0 and child_dir_len != 0:
            print(f&#34;{prefix}{self.sing[3]}{elem}  &#34;)
        else:
            print(f&#34;{prefix}{self.sing[1]}{elem}  &#34;)
        temp_prefix = prefix
        if ind == child_dir_len - 1 and child_file_len == 0:
            prefix = prefix + f&#34; {self.sing[4]}&#34;
        else:
            prefix = prefix + f&#34;{self.sing[2]}{self.sing[4]}&#34;
        self.dfs(elem, prefix)
        prefix = temp_prefix
    for ind, elem in enumerate(temp_parents.get(&#39;child_file&#39;)):
        if ind == child_file_len - 1:
            print(f&#34;{prefix}{self.sing[3]}{elem}  &#34;)
        else:
            print(f&#34;{prefix}{self.sing[1]}{elem}  &#34;)</code></pre>
</details>
</dd>
<dt id="sfs.StructFileSystem.dict_view"><code class="name flex">
<span>def <span class="ident">dict_view</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"><h2 id="description">Description:</h2>
<p>Метод инициализирует построение дерева файловой системы и вывод на экран, предварительно подготовив переменную
<code>prefix</code>.</p>
<p><code>prefix: str</code> - в переменной, хранятся символы, которые при выводе стоят перед наименованиями директорий
и
файлов.
<code>print(f"[34m.
")</code> -
указываем цвет для модуля colorama и рисуем точку "." из которой начинаем вывод
дерева ФС.</p>
<h2 id="return-none">:return: None</h2></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def dict_view(self):
    &#34;&#34;&#34;
    ## Description: ##
    Метод инициализирует построение дерева файловой системы и вывод на экран, предварительно подготовив переменную
    `prefix`.

    `prefix: str` - в переменной, хранятся символы, которые при выводе стоят перед наименованиями директорий  и
    файлов.
    `print(f&#34;\033[34m.  &#34;)` -  указываем цвет для модуля colorama и рисуем точку &#34;.&#34; из которой начинаем вывод
    дерева ФС.

    ## :return: None ##
    &#34;&#34;&#34;
    prefix = &#34;&#34;
    self.create_dict_tree()
    print(f&#34;\033[34m.  &#34;)
    self.dfs(self.relative_folder, prefix)</code></pre>
</details>
</dd>
<dt id="sfs.StructFileSystem.valid_work_folder"><code class="name flex">
<span>def <span class="ident">valid_work_folder</span></span>(<span>self, f)</span>
</code></dt>
<dd>
<div class="desc"><h2 id="description">Description:</h2>
<p><strong> Проверка</strong> на существование введённого пути и отвечаем на вопрос, является ли указанный
путь директорией?</p>
<p>Создаём объект класса Path: <code>p = Path(f)</code></p>
<p>Проверка существования указанного в <code>f</code> пути (<code>Path.exists()</code>, <em>True</em> - существует, <em>False</em> - не существует).
Проверка, на, то, является ли указанный сетевой путь файлом (p.is_file(), если файл, то True).</p>
<h2 id="param-f-str">:param <code>f</code>: str</h2>
<p>путь, вводимый для проверки.</p>
<h2 id="return-str-path">:return: str или Path</h2>
<p>Если путь не существует или является файлом, возвращаем директорию по умолчанию ("."),
иначе объект, класса <code>Path</code>.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def valid_work_folder(self, f):
    &#34;&#34;&#34;
    ## Description: ##
    ** Проверка** на существование введённого пути и отвечаем на вопрос, является ли указанный  путь директорией?

    Создаём объект класса Path: `p = Path(f)`

    Проверка существования указанного в `f` пути (`Path.exists()`, *True* - существует, *False* - не существует).
    Проверка, на, то, является ли указанный сетевой путь файлом (p.is_file(), если файл, то True).

    ## :param `f`: str##
    путь, вводимый для проверки.

    ## :return: str или Path##
    Если путь не существует или является файлом, возвращаем директорию по умолчанию (&#34;.&#34;),
    иначе объект, класса `Path`.
    &#34;&#34;&#34;
    p = Path(f)
    if p.exists():
        if p.is_file() == False:
            return p
        else:
            print(&#39;\033[31m&#39; + f&#34;Указанный путь {p} является файлом!!!&#34; + &#39;\033[39m&#39;)
    else:
        print(&#39;\033[31m&#39; + f&#34;Директория {p} не существует!!!&#34; + &#39;\033[39m&#39;)
    return &#39;.&#39;</code></pre>
</details>
</dd>
</dl>
</dd>
</dl>
</section>
</article>
<nav id="sidebar">
<h1>Index</h1>
<div class="toc">
<ul></ul>
</div>
<ul id="index">
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="sfs.StructFileSystem" href="#sfs.StructFileSystem">StructFileSystem</a></code></h4>
<ul class="">
<li><code><a title="sfs.StructFileSystem.create_dict_tree" href="#sfs.StructFileSystem.create_dict_tree">create_dict_tree</a></code></li>
<li><code><a title="sfs.StructFileSystem.dfs" href="#sfs.StructFileSystem.dfs">dfs</a></code></li>
<li><code><a title="sfs.StructFileSystem.dict_view" href="#sfs.StructFileSystem.dict_view">dict_view</a></code></li>
<li><code><a title="sfs.StructFileSystem.valid_work_folder" href="#sfs.StructFileSystem.valid_work_folder">valid_work_folder</a></code></li>
</ul>
</li>
</ul>
</li>
</ul>
</nav>
</main>
<footer id="footer">
<p>Generated by <a href="https://pdoc3.github.io/pdoc" title="pdoc: Python API documentation generator"><cite>pdoc</cite> 0.10.0</a>.</p>
</footer>
</body>
</html>