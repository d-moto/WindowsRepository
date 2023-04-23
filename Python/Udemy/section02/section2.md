# Python環境の設定 4_7

## 4. Macにpythonをインストールする
略
## 5. MacにPycharmをインストールする
略
## 6. Windowsにpythonをインストールする

### anacondaからインストールする方法

1. python.org からインストールする or anaconda.com へ移動する。

2. 上記サイトへ移動し、ダウンロードボタンをクリックする。

3. exeファイルのダウンロードが始まるので、終わるまで待つ。

4. ダウンロードが終わったら、exeファイルを起動する。

5. インストールウィンドウの指示に従う。  
Destination Folder : C:\Users\mokos\anaconda3

6. ダウンロードができたら、アプリ検索で、「Anaconda Powershell Prompt」を探す。

7. 上記が起動すれば、インストールは正常にできている。

## 7. WindowsにPycharmをインストールする。(IDEをインストールする。)

1. https://www.jetbrains.com/ja-jp/pycharm/　に移動する。

2. 右上のダウンロードボタンをクリック。

3. FreeのCommunityをダウンロードする。

4. インストーラーが起動するので、指示に従う。  
インストール先：C:\Program Files\JetBrains\PyCharm Community Edition 2022.3

5. インストールが完了したら、Run PyCharm Community Edition にチェックを入れて、起動する。

6. Welcome to PyCharmの画面で、New Projectを押す。

7. Locationの最後のpythonProjectをpython_programmingに変更。

8. Previously configured interpreterにチェックを入れる。

9. Add Interpreterをクリック。(これにAnacondaを指定する。)

10. 左のSystem Interpreterをクリックする。

11. anacondaをインストールした、ディレクトリを指定する。（今回は、C:\Users\mokos\anaconda3）

12. PyCharmが起動し、右下にIndexing Python SDK 'Python3.9'が表示されているので、終わるまでしばらく待つ。

13. 終われば、PyCharmが使用できる。

### **NOTE : PyCharmのTerminal機能で以下のエラーが出た**

```
To initialize your shell, run
Import-Module : このシステムではスクリプトの実行が無効になっているため、ファイル C:\Users\mo
    $ conda init <SHELL_NAME>Conda.psm1 を読み込むことができません。詳細については、「about_
Execution_Policies」(https://go.microsoft.com/fwlink/?LinkID=135170) を参照してください。
Currently supported shells are:
  - bash-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentL ...
  - cmd.exe~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - fishtegoryInfo          : セキュリティ エラー: (: ) [Import-Module]、PSSecurityException
  - tcshllyQualifiedErrorId : UnauthorizedAccess,Microsoft.PowerShell.Commands.ImportModule 
  - xonshd
  - zsh
  - powershelldError: Your shell has not been properly configured to use 'conda activate'.
If using 'conda activate' from a batch script, change your
See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.



CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
If using 'conda activate' from a batch script, change your
invocation to 'CALL conda.bat activate'.

To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - cmd.exe
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.
```

windowsPowerShellで以下のようにした。
```
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

新機能と改善のために最新の PowerShell をインストールしてください!https://aka.ms/PSWindows

PS C:\WINDOWS\system32> Get-ExecutionPlicy
Get-ExecutionPlicy : 用語 'Get-ExecutionPlicy' は、コマンドレット、関数、スクリプト ファイル、または操作可能なプログラ
ムの名前として認識されません。名前が正しく記述されていることを確認し、パスが含まれている場合はそのパスが正しいことを確
認してから、再試行してください。
発生場所 行:1 文字:1
+ Get-ExecutionPlicy
+ ~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (Get-ExecutionPlicy:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\WINDOWS\system32> Get-ExecutionPolicy
Restricted
PS C:\WINDOWS\system32> Set-ExecutionPolicy RemoteSigned

実行ポリシーの変更
実行ポリシーは、信頼されていないスクリプトからの保護に役立ちます。実行ポリシーを変更すると、about_Execution_Policies
のヘルプ トピック (https://go.microsoft.com/fwlink/?LinkID=135170)
で説明されているセキュリティ上の危険にさらされる可能性があります。実行ポリシーを変更しますか?
[Y] はい(Y)  [A] すべて続行(A)  [N] いいえ(N)  [L] すべて無視(L)  [S] 中断(S)  [?] ヘルプ (既定値は "N"): Y
PS C:\WINDOWS\system32> Get-ExecutionPolicy
RemoteSigned
PS C:\WINDOWS\system32>
```

Terminalを再起動すると、入れた。
```
(base) PS C:\Users\mokos\PycharmProjects\python_programming> 
```