
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

## **Check the commit history**
- Check the commit history
```
$ git log
```
- Check the commit history with diffs
```
$ git log -p
```

## **Preparing to use git hub**

- Set up a public key in git hub
1. Generate the SSH key
```
$ ssh-keygen -t rsa -b 4096 -C "goodddd6@gmail.com"
|
|
|
[root@localhost63 Git]# ssh-keygen -t rsa -b 4096 -C "goodddd6@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): /home/alma1/Git/sshkey/id_rsa
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/alma1/Git/sshkey/id_rsa.
Your public key has been saved in /home/alma1/Git/sshkey/id_rsa.pub.
The key fingerprint is:
SHA256:TZ6yluXlFJbcq1pj1cz+/FhjTr9nKMHAS5AeqUWm5qo goodddd6@gmail.com
The key's randomart image is:
+---[RSA 4096]----+
|       .oo       |
|       o*  . o   |
|      o+ +. = .  |
|     o. .++o . = |
|      . S.=+o o +|
|     .   *.+oo . |
|    .   + . *. =o|
|   .   .   +..=+*|
|  E       .  ..+O|
+----[SHA256]-----+
[root@localhost63 Git]#
```

2. Register the ssh public key to git hub

3. Enter the command to check the connection to the git hub
```
$ ssh -T git@github.commit
```

## **Clone the remote repository**
1. Get the URL of the remote repository
```
git@github.com:d-moto/ichiyasaGitSample.git
```

2. Execute clone
```
$ git clone git@github.com:d-moto/ichiyasaGitSample.git
```
**note**
新しくリモートレポジトリが作成されるので、現在操作しているレポジトリがあれば、<br>
その中から出てから、上記のコマンドを叩く。
```
[root@localhost63 Git]# cd ..
[root@localhost63 alma1]# mkdir ichiyasa-git-repository
[root@localhost63 alma1]# cd ichiyasa-git-repository/
[root@localhost63 ichiyasa-git-repository]# ls
[root@localhost63 ichiyasa-git-repository]#
[root@localhost63 ichiyasa-git-repository]#
[root@localhost63 ichiyasa-git-repository]# git status
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
[root@localhost63 ichiyasa-git-repository]#
[root@localhost63 ichiyasa-git-repository]#
[root@localhost63 ichiyasa-git-repository]# ls -al
合計 4
drwxr-xr-x  2 root  root     6 11月 15 22:49 .
drwx------ 34 alma1 alma1 4096 11月 15 22:49 ..
[root@localhost63 ichiyasa-git-repository]#
[root@localhost63 ichiyasa-git-repository]#
[root@localhost63 ichiyasa-git-repository]# git clone git@github.com:d-moto/ichiyasaGitSample.git
Cloning into 'ichiyasaGitSample'...
Enter passphrase for key '/root/.ssh/id_rsa':
remote: Enumerating objects: 33, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.

remote: Total 33 (delta 0), reused 2 (delta 0), pack-reused 28
Receiving objects: 100% (33/33), 1.36 MiB | 1.17 MiB/s, done.
Resolving deltas: 100% (2/2), done.
[root@localhost63 ichiyasa-git-repository]#
[root@localhost63 ichiyasa-git-repository]#
[root@localhost63 ichiyasa-git-repository]# ls
ichiyasaGitSample
[root@localhost63 ichiyasa-git-repository]# cd ichiyasaGitSample/
[root@localhost63 ichiyasaGitSample]# ls
README.md  assets  images  index.html
[root@localhost63 ichiyasaGitSample]# cd ..
[root@localhost63 ichiyasa-git-repository]# ls -al
合計 4
drwxr-xr-x  3 root  root    31 11月 15 22:49 .
drwx------ 34 alma1 alma1 4096 11月 15 22:49 ..
drwxr-xr-x  5 root  root    99 11月 15 22:52 ichiyasaGitSample
[root@localhost63 ichiyasa-git-repository]# cd ichiyasaGitSample/
[root@localhost63 ichiyasaGitSample]# ls
README.md  assets  images  index.html
[root@localhost63 ichiyasaGitSample]# ls -al
合計 16
drwxr-xr-x 5 root root   99 11月 15 22:52 .
drwxr-xr-x 3 root root   31 11月 15 22:49 ..
drwxr-xr-x 8 root root  163 11月 15 22:52 .git
-rw-r--r-- 1 root root   56 11月 15 22:52 .gitignore
-rw-r--r-- 1 root root  104 11月 15 22:52 README.md
drwxr-xr-x 5 root root   40 11月 15 22:52 assets
drwxr-xr-x 2 root root   42 11月 15 22:52 images
-rw-r--r-- 1 root root 6369 11月 15 22:52 index.html
[root@localhost63 ichiyasaGitSample]#
```
## **Create a dedicated branch and switch**
1. Create branch
```
$ git branch <new branch name>

$ git branch update-venue
```

2. Check the branch in use
```
$ git branch

[root@localhost63 ichiyasaGitSample]# git branch
* master
  update-venue
[root@localhost63 ichiyasaGitSample]#
```

A list of branches is displayed.
[*] is the branch currently in use.

3. Check out the branch (Switch the branch)
```
$ git checkout <branch-name>

$ git branch update-venue

[root@localhost63 ichiyasaGitSample]# git branch
  master
* update-venue
[root@localhost63 ichiyasaGitSample]#
```

4. Check the branch in use
```
$ git branch

or 

$ git status

[root@localhost63 ichiyasaGitSample]# git status
On branch ★update-venue
nothing to commit, working tree clean
[root@localhost63 ichiyasaGitSample]#

```

## **Edit file and commit**
On the branch you just created, edit the file and commit.

1. Edit "index.html"
```
 55                     <article>
 56                         <h3>イベント日時・場所</h3>
 57                         <p>3月23日 19:00開始</p>
 58                         <p>株式会社インプレス12345678 イベントセミナー会場</p>
 59                     </article>
 
 |

 55                     <article>
 56                         <h3>イベント日時・場所</h3>
 57                         <p>3月23日 19:00開始</p>
 58                         <p>株式会社インプレス イベントセミナー会場</p>
 59                     </article>
 ```

2. Check the status
```
[root@localhost63 ichiyasaGitSample]# git status
On branch update-venue
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
[root@localhost63 ichiyasaGitSample]#
```

3. Execute commit
```
[root@localhost63 ichiyasaGitSample]# git add index.html
[root@localhost63 ichiyasaGitSample]# git commit -m "Edit venue (delete 12345678)"
[update-venue 353b7df] Edit venue (delete 12345678)
 1 file changed, 2 insertions(+), 2 deletions(-)
[root@localhost63 ichiyasaGitSample]#
```

4. Compare operations on branches (Compare against the master branch)

```
[root@localhost63 ichiyasaGitSample]# git diff master
diff --git a/index.html b/index.html
index 35483fe..ced2022 100644
--- a/index.html
+++ b/index.html
@@ -55,7 +55,7 @@
                     <article>
                         <h3>イベント日時・場所</h3>
                         <p>3月23日 19:00開始</p>
-                        <p>株式会社インプレス12345678 イベントセミナー会場</p>
+                        <p>株式会社インプレス イベントセミナー会場</p>
                     </article>
                     <article>
                         <h3>スピーカー</h3>
@@ -159,4 +159,4 @@
 <script src="assets/js/main.js"></script>

 </body>
-</html>
\ No newline at end of file
+</html>
[root@localhost63 ichiyasaGitSample]#
```

## **Create the pull request**
Changes made in the local repository are reflected in the remote repository. <br>
Then, the operations in the newly created branch are merged into the master branch. <br>
The master branch will be the latest state.
The name of the remote repository to be pushed can be found with the "git remote -v" command.

```
$ git remote -v

[root@localhost63 ichiyasaGitSample]# git remote -v
origin  git@github.com:d-moto/ichiyasaGitSample.git (fetch)
origin  git@github.com:d-moto/ichiyasaGitSample.git (push)
[root@localhost63 ichiyasaGitSample]#
```

1. Push the branch

```
$ git push <Name of the remote repository to be pushed> <Branch name to push>

[root@localhost63 ichiyasaGitSample]# git push origin update-venue
Enter passphrase for key '/root/.ssh/id_rsa': d-motoi
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 297 bytes | 297.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:d-moto/ichiyasaGitSample.git
   a2373f9..353b7df  update-venue -> update-venue
[root@localhost63 ichiyasaGitSample]#


[root@localhost63 ichiyasaGitSample]# git branch
  master
* update-venue
[root@localhost63 ichiyasaGitSample]# git branch update-venue2
[root@localhost63 ichiyasaGitSample]# git branch
  master
* update-venue
  update-venue2
[root@localhost63 ichiyasaGitSample]# git checkout update-venue2
Switched to branch 'update-venue2'
[root@localhost63 ichiyasaGitSample]# git branch
  master
  update-venue
* update-venue2
[root@localhost63 ichiyasaGitSample]# git status
On branch update-venue2
nothing to commit, working tree clean
[root@localhost63 ichiyasaGitSample]#
[root@localhost63 ichiyasaGitSample]# ls
README.md  assets  images  index.html
[root@localhost63 ichiyasaGitSample]# vi README.md
[root@localhost63 ichiyasaGitSample]# git status
On branch update-venue2
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
[root@localhost63 ichiyasaGitSample]# git add README.md
[root@localhost63 ichiyasaGitSample]# git commit -m "edit README.md"
[update-venue2 2a37202] edit README.md
 1 file changed, 1 insertion(+), 1 deletion(-)
[root@localhost63 ichiyasaGitSample]# git status
On branch update-venue2
nothing to commit, working tree clean
[root@localhost63 ichiyasaGitSample]# git remote -v
origin  git@github.com:d-moto/ichiyasaGitSample.git (fetch)
origin  git@github.com:d-moto/ichiyasaGitSample.git (push)
[root@localhost63 ichiyasaGitSample]# git push origin update-venue2
Enter passphrase for key '/root/.ssh/id_rsa':
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 331 bytes | 331.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'update-venue2' on GitHub by visiting:
remote:      https://github.com/d-moto/ichiyasaGitSample/pull/new/update-venue2
remote:
To github.com:d-moto/ichiyasaGitSample.git
 * [new branch]      update-venue2 -> update-venue2
[root@localhost63 ichiyasaGitSample]#
```

## **Retrieve the contents of a remote repository to the local repository**

Reflect from remote repository to local repository.
- git pull command
```
$ git pull origin master 
```

- git fetch origin
```
$ git fetch origin
```

## **Use multiple branches**

1. Create and checkout branch
```
$ git checkout -b speakers-info
```

2. Modify HTML file

3. Add TODO comment

4. Prepare images

5. Check HTML file on browser

6. Execute commit
```
$ git status
$ git add -A #Add all changes to stage
$ git status
$ git commit -m "add speaker infomation"
```

7. Push remote repository
```
$ git push origin speaker-info
```
