
# **How To Use Git**

## **Set Up Git**
1. set up user name
```
$ git config --global user.name motoi
```
2. set up email
```
$ git config --global user.email goodddd6@gmail.com
```
3. check the configuration
```
$ git config --list
```
4. set up Visual Studio Code
```
$ git config --global core.editor "code --wait"
```
5. check the configuration
```
$ git config core.editor
```
※When you execute this command "git config --global", the file "/c/Users/mokos/.gitconfig" is created and the configuration is written.

## **Set up and create local repository**
1. careate directory
```
$ cd ~
$ mkdir git-ichiyasa
```
2. create something
```
$ touch HowToUseGit.md
```
3. create local repository
```
$ cd git-ichiyasa
$ git init
```
4. check your directory
```
$ ls -al
```
5. check status of local repository
```
$ git status
```
6. register files by git add command
```
$ git add HowToUseGit.md
```
7. check status
```
$ git status
```
※Files that are not registered under git management are treated as "Untracked files" by the git status command.

<details>
<summary>
example
</summary>

```shell

$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        HowToUseGit.md

nothing added to commit but untracked files present (use "git add" to track)

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ git add HowToUseGit.md

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   HowToUseGit.md


mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$
```
</details>


## **Check differences of git files**
1. Check the difference between the work tree and the staging area
```
$ git diff
```
2. Check the difference between the staging area and the git directory
```
$ git diff --cached
```
```
$ git diff
diff --git a/HowToUseGit.md b/HowToUseGit.md
index 0a161d4..d0fd93c 100644
#--- a/HowToUseGit.md
#+++ b/HowToUseGit.md
@@ -95,4 +95,4 @@ $ git diff
 #```
 $ git diff --cached
 #```
#-
#+3.
#
#mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ git diff --cached
diff --git a/HowToUseGit.md b/HowToUseGit.md
new file mode 100644
index 0000000..0a161d4
#--- /dev/null
#+++ b/HowToUseGit.md
@@ -0,0 +1,98 @@
#+
#+# How To Use Git
#+
#+## Set Up Git
#+1. set up user name
................................
```

## **Commit the files**
1. check status of local repository
```
$ git statsu
```
2. execute commit
```
$ git commit
```
3. atom is opend
4. write commit message
5. check status
```
$ git status
```
```
$ git status
On branch master
nothing to commit, working tree clean
```

## **ローカルリポジトリでの操作を取り消す（checkout, reset）**
ワークツリーへの変更を取り消す方法(git checkout)とステージングエリアへの変更を取り消す方法(git reset)について

ワークツリーへの変更の取り消しは、ファイルの状態が直前のコミット（または直前のステージングエリアへの登録）に戻る。  
ステージングエリアへの変更の取り消しは、ファイルの状態はそのままでステージングエリアへの登録だけを取り消します。

***
[Work Tree]  --"git add"-->  [Staging area]  --"git commit"-->  [Git Directory]  
[Work Tree]  <--"git reset"--  [Staging area]  
[Work Tree]  <-----------------"git checkout"----------------- [Git Directory]
***

ファイルをいろいろ変更したが、やっぱり直前のコミット状態まで戻したい時に、"git checkout"コマンドで、ワークツリーの変更を取り消せる。

- **Work Treeの変更を取り消すコマンド（git checkout）**
```
$ git checkout -- sample.txt
```
```
#[Work Tree (added something)] [staging area (something added is not resistered)] [Git Derectory (newest)]  
#At this time,  
#[Work Tree]!=[Git Directory]  
#-->git checkout  
#[Work Tree (same as GIt Directory)] [Staging Area (something added is not resistered)] [Git Directory (newest)]  
#At this time,  
#[Work Tree]=[Git Directory]
```

<details>
<summary>
Example
</summary>

1. Create a new file, and commit  
```
$ touch GitCheckOut.txt
$ git add GitCheckOut.txt
$ git commit -m "File to check git checkout command"
```

2. Write to the file you just created.
```
$ echo "this is sample script" >> GitCheckOut.txt
```

3. Check the status of the work tree.
```
$ git status
```

4. Cancel changes to the work tree.
```
$ git checkout -- GitCheckOut.txt
```

5. Check the status of the GitCheckOut.txt
```
$ cat GitCheckOut.txt
```

It should be back to a blank slate.
Strictly speaking, the "git checkout" command reverts to the staging area state, not the last committed state.

</details>


<details>
<summary>
Execution example
</summary>

```shell

$ git status
On branch master
nothing to commit, working tree clean

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ touch GitCheckOut.txt

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ git add GitCheckOut.txt

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ git commit -m "File to check git checkout command"
[master 15c2ddc] File to check git checkout command
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 GitCheckOut.txt

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ cat GitCheckOut.txt

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ echo "this is sample script" >> GitCheckOut.txt

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   GitCheckOut.txt

no changes added to commit (use "git add" and/or "git commit -a")

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ cat GitCheckOut.txt
this is sample script

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ git checkout -- GitCheckOut.txt

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ cat GitCheckOut.txt

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$
```
</details>

<br>

- **ステージングエリアへの登録を取り消すコマンド（git reset）**<br><br>
間違ってファイルの状態をステージングエリアに登録してしまった時は、  
git resetコマンドで取り消せる。<br>
git checkoutコマンドとは異なり、ワークツリーの状態は変更されない。<br>
```shell
$ git reset HEAD GitCheckOut.txt
```
resetコマンドの後ろにHEADと指定している。<br>
HEADはこのローカルレポジトリで**最後にコミットした状態**を意味している。<br>
ステージングエリアの状態を最後のコミットと同じ状態にリセットするという意味になる。<br><br>

<details>
<summary>
Example
</summary>

1. Change file contents
```
[root@localhost63 Git]# pwd
/home/alma1/Git
[root@localhost63 Git]# ls
readme.md  test
[root@localhost63 Git]# cat test
[root@localhost63 Git]# echo "`date`" >> test
[root@localhost63 Git]# cat test
2022年 11月 11日 金曜日 23:50:52 JST
[root@localhost63 Git]#
```

2. Register the files to staging Area
```
[root@localhost63 Git]# git add test
```

3. Check the status of the local repository
```
# [root@localhost63 Git]# git status
# On branch master
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
        modified:   test
# [root@localhost63 Git]#
```

4. Reset the registration to staging area
```
[root@localhost63 Git]# git reset HEAD test
Unstaged changes after reset:
M       test
```

5. Check the status of the local repository
```
[root@localhost63 Git]# git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   test
no changes added to commit (use "git add" and/or "git commit -a")
[root@localhost63 Git]#
```

6. Check the contents of test file
```
[root@localhost63 Git]# cat test
2022年 11月 11日 金曜日 23:50:52 JST
[root@localhost63 Git]#
```
ワークツリーのファイルの内容は変更されていない。<br>
ファイルの内容も変更したければ、git checkoutを使う。
</details>

aiu
