# 目次
1. [gitの初期設定](#anchor1)
2. [ローカルレポジトリを作る]
3. []

<a id="anchor1"></a>

# gitの初期設定
ログインしているユーザーで初めてGitを使用する場合は、以下の設定が必要。

1. Userの設定
```
$ git config --global user.name motoi
```
2. Emailの設定
```
$ git config --global user.email goodddd6@gmail.com
```
3. 設定の確認
```
$ git config --list
```
4. エディタの設定（VSコード）
```
$ git config --global core.editor "code --wait"
```
5. 設定の確認
```
$ git config core.editor
```

※"git config --globalコマンドを実行すると、そのユーザーのホームディレクトリ（今回の場合は、/c/User/mokos/.gitconfig）の.gitconfigファイルが作成され、そのファイル
に設定が書き込まれる。

# ローカルレポジトリを作る。

1. ローカルレポジトリを作成するディレクトリを作成
```
$ cd ~
$ mkdir Git_work
```
2. 作成したディレクトリに移動
```
$ cd Git_work
```
3. 初期化コマンドを実行する
```
$ git init
```
※この時、`.git`ファイルが作成される。

# ブランチの操作
## ブランチを切る。
```shell
# git branch <branch name>
```

## ブランチの一覧を表示
```shell
# git branch
```

## ブランチを切りかえる
```shell
# git checkoout <branch name>
```

## ブランチをmasterブランチにマージ
※tool-devブランチをmasterブランチに取り込む場合。

```shell
# git checkout master
```
```shell
# git merge tool-dev
```

# Gitの変更履歴の確認

`git diff`は、Gitリポジトリ内の変更を表示するためのコマンドです。以下に、その主なバリエーションと使用例を示します。

1. `git diff`: ワーキングディレクトリとインデックス（ステージングエリア）の差分を表示します。(`git add`してしまうと`git diff`で差分が見れなくなってしまう。)
このコマンドは、まだステージングエリアに追加されていない変更を確認するのに役立ちます。

    使用例:
    ```
    git diff
    ```

2. `git diff --staged`または`git diff --cached`: インデックスと最新のコミットの差分を表示します。これは、次のコミットで何が変更されるかを確認するのに役立ちます。

    使用例:
    ```
    git diff --staged
    ```

3. `git diff <commit>`: ワーキングディレクトリと指定したコミットの差分を表示します。

    使用例:
    ```
    git diff 9da6487
    ```

4. `git diff <commit1> <commit2>`: 2つのコミット間の差分を表示します。

    使用例:
    ```
    git diff 9da6487 5b7e7d6
    ```

5. `git diff <branch1>..<branch2>`: 2つのブランチ間の差分を表示します。

    使用例:
    ```
    git diff master..feature
    ```

6. `git diff --name-only`: 変更されたファイルの名前のみを表示します。

    使用例:
    ```
    git diff --name-only
    ```

7. `git diff --name-status`: 変更されたファイルの名前と、それらが追加された（A）、変更された（M）、または削除された（D）かを表示します。

    使用例:
    ```
    git diff --name-status
    ```

8. `git diff --stat`: 変更されたファイル、挿入行数、削除行数の統計を表示します。

    使用例:
    ```
    git diff --stat
    ```

9. `git diff --color-words`: 単語レベルでの変更を色分けして表示します。

    使用例:
    ```
    git diff --color-words
    ```

10. `git diff --ignore-space-change`または`git diff -b`: スペースの変更を無視して差分を表示します。

    使用例:
    ```
    git diff --ignore-space-change
    ```

以上が主な`git diff`コマンドのバリエーションとその使用例です。これらのコマンドは、リポジトリ内の変更を理解し、追跡するのに非常に役立ちます。


# Gitのtag機能
タグとは、コミットを参照しやすくするために、わかりやすい名前を付けるもの。
Gitでは軽量タグと注釈付きタグの2種類のタグが使用できる。
また、一度付けたタグはブランチのように位置が移動することはなく固定。

- 軽量タグ
    - 名前を付けられる
- 注釈付きタグ
    - 名前を付けられる
    - コメントを付けられる
    - 署名を付けられる

一般的にはリリースタグには注釈付きタグを使ってコメントや署名を追加する。
軽量タグはローカルで一時的に使用する使い捨てなどに使用する。

## 前準備
新しくディレクトリを作成する。
```
$ mkdir tutorial
$ cd tutorial
$ git init
```
tutorialディレクトリに以下の内容のmyfile.txtを作成し、コミットする。
```
This is myfile. tag tutorial.
```
```
$ echo "This is myfile. tag tutorial." >> myfile.txt
$ git add myfile.txt
$ git commit -m "first commit"
```
この時点での履歴は以下となる。

〇<-master<-HEAD

## 軽量タグを追加する
タグを追加するには、tagコマンドを使用する
<tagname>にはタグの名前を指定する。
```
$ git tag <tagname>
```
現在のHEADが指しているコミットにappleというタグを付けるには次のコマンドを使う。
```
$ git tag apple
```
パラメータなしでtagコマンドを実行するとタグの一覧を表示できる。
```
$ git tag
```
また、logコマンドに`--decorete`オプションを付けて実行すると、タグ情報を含めて履歴を表示できる。

〇<-master<-HEAD==apple

## 注釈付きタグを追加する
注釈付きタグを追加するには、tagコマンドに-aオプションを指定して実行する。
実行するとエディタが起動するので、タグに設定するコメントを入力する。
-mオプションでコメントを与えることもできる。
```
$ git tag -a <tagname>
```
現在のHEADが指しているコミットにbananaという注釈付きタグを付けるには、次のコマンドを実行する。
```
$ git tag -am "banana tag" banana
```
-nオプションを指定してtagコマンドを実行するとタグの一覧とコメントを表示できる。
```
$ git tag -n
```

〇<-master<-HEAD==banana(banana tag)

## タグを削除する
タグを削除するにはtagコマンドに-dオプションを指定して実行する
```
$ git tag -d <tagname>
```

# 付録
## git help
```
$ git
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
```