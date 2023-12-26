※ここのファイルのパス
```
× C:\Users\mokos\03Git_work\git-master\WindowsRepository\Python\Udemy\PyCharmProjects
↓に変更
C:\Users\mokos\03Git_work\git-master\WindowsRepository\Python\Udemy\PyCharmProjects\Scripts\python.exe C:\Users\mokos\03Git_work\git-master\WindowsRepository\Python\Udemy\PyCharmProjects\PythonScripts\main.py 
Hi, PyCharm
This is python path: C:\Users\mokos\03Git_work\git-master\WindowsRepository\Python\Udemy\PyCharmProjects\Scripts\python.exe

Process finished with exit code 0
```

## pythonの実行環境

- 以下にPythonをダウンロードしている。
```
PS C:\Users\mokos> cd "python/env/mainenv/Scripts"
PS C:\Users\mokos\python\env\mainenv\Scripts> python.exe
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
PS C:\Users\mokos\python\env\mainenv\Scripts>
```
※大本は以下.
※仮想環境を構築して(mainenv)使用している。
```
C:\Users\mokos>python
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> print(sys.executable)
C:\Users\mokos\AppData\Local\Programs\Python\Python311\python.exe
>>>
```

## 仮想環境の作成

- 仮想環境は以下のコマンドで作成する。
```
PS C:\Users\mokos\python\env\mainenv\Scripts> python -m venv myenv
```

- 仮想環境のアクティベート
```
PS C:\Users\mokos\python\env\mainenv\Scripts> cd myenv
PS C:\Users\mokos\python\env\mainenv\Scripts\myenv> Scripts/activate
(myenv) PS C:\Users\mokos\python\env\mainenv\Scripts\myenv>
```

- 仮想環境のディアクティベーション
```
(myenv) PS C:\Users\mokos\python\env\mainenv\Scripts\myenv> deactivate
PS C:\Users\mokos\python\env\mainenv\Scripts\myenv>
```

- 仮想環境の削除
```
PS C:\Users\mokos\python\env\mainenv\Scripts>> Remove-Item -Path "myenv" -Recurse -Force
```

- パッケージの確認(mainenv)
```
(mainenv) C:\Users\mokos\python\env\mainenv\Scripts>pip list
Package                 Version
----------------------- ------------
aiohttp                 3.8.4
aiosignal               1.3.1
asttokens               2.2.1
async-generator         1.10
async-timeout           4.0.2
attrs                   23.1.0
Babel                   2.12.1
backcall                0.2.0
beautifulsoup4          4.12.2
bs4                     0.0.1
certifi                 2023.5.7
cffi                    1.15.1
charset-normalizer      3.1.0
click                   8.1.3
colorama                0.4.6
colour                  0.1.5
contourpy               1.1.0
cycler                  0.11.0
dataclasses-json        0.5.8
decorator               5.1.1
diffusers               0.17.1
dtreeviz                2.2.1
exceptiongroup          1.1.1
executing               1.2.0
faiss-cpu               1.7.4
filelock                3.12.2
fonttools               4.40.0
frozenlist              1.3.3
fsspec                  2023.6.0
futures                 3.0.5
goslate                 1.5.4
GPUtil                  1.4.0
graphviz                0.20.1
greenlet                2.0.2
h11                     0.14.0
huggingface-hub         0.15.1
idna                    3.4
importlib-metadata      6.7.0
iniconfig               2.0.0
ipython                 8.14.0
jedi                    0.18.2
Jinja2                  3.1.2
joblib                  1.2.0
kiwisolver              1.4.4
langchain               0.0.209
langchainplus-sdk       0.0.16
MarkupSafe              2.1.3
marshmallow             3.19.0
marshmallow-enum        1.5.1
matplotlib              3.7.1
matplotlib-inline       0.1.6
mauve-text              0.3.0
mpmath                  1.3.0
multidict               6.0.4
mypy-extensions         1.0.0
networkx                3.1
numexpr                 2.8.4
numpy                   1.25.0
openai                  0.27.8
openapi-schema-pydantic 1.2.4
outcome                 1.2.0
packaging               23.1
pandas                  2.0.3
parso                   0.8.3
pickleshare             0.7.5
Pillow                  9.5.0
pip                     23.1.2
pluggy                  1.2.0
prompt-toolkit          3.0.39
psutil                  5.9.5
pure-eval               0.2.2
pycparser               2.21
pydantic                1.10.9
PyDictionary            2.0.1
Pygments                2.15.1
pyparsing               3.1.0
pypng                   0.20220715.0
PySocks                 1.7.1
pytest                  7.4.0
python-dateutil         2.8.2
python-dotenv           1.0.0
pytube                  15.0.0
pytz                    2023.3
PyYAML                  6.0
qrcode                  7.4.2
regex                   2023.6.3
requests                2.31.0
safetensors             0.3.1
scikit-learn            1.2.2
scipy                   1.10.1
selenium                4.10.0
setuptools              65.5.0
six                     1.16.0
sniffio                 1.3.0
sortedcontainers        2.4.0
soupsieve               2.4.1
SQLAlchemy              2.0.16
stack-data              0.6.2
sympy                   1.12
tenacity                8.2.2
threadpoolctl           3.1.0
tkcalendar              1.6.1
tokenizers              0.13.3
torch                   2.0.1
tqdm                    4.65.0
traitlets               5.9.0
transformers            4.30.2
trio                    0.22.0
trio-websocket          0.10.3
typing_extensions       4.6.3
typing-inspect          0.9.0
tzdata                  2023.3
urllib3                 2.0.3
wcwidth                 0.2.6
webdriver-manager       3.8.6
webuiapi                0.9.3
wsproto                 1.2.0
yarl                    1.9.2
zipp                    3.15.0

[notice] A new release of pip is available: 23.1.2 -> 23.3.2
[notice] To update, run: python.exe -m pip install --upgrade pip

(mainenv) C:\Users\mokos\python\env\mainenv\Scripts>
```

- パッケージのインストール
```commandline
(mainenv) PS C:\Users\mokos\python\env\mainenv\Scripts> pip install psutil
```