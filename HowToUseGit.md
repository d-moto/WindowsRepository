
# **How To Use Git**

**NOTE**

git repository location: 
- windowns11 --> /c/Users/mokos/git-ichiyasa
- Linux --> /home/alma1/Git

git config file location:
- windows11 --> /c/Users/mokos/.gitconfig
- Linux --> /root/.gitconfig

## **1. Set Up Git**
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

## **2. Set up and create local repository**
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


## **3. Check differences of git files**
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

## **4. Commit the files**
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

## **5. ローカルリポジトリでの操作を取り消す（checkout, reset）**
ワークツリーへの変更を取り消す方法(git checkout)とステージングエリアへの変更を取り消す方法(git reset)について

ワークツリーへの変更の取り消しは、ファイルの状態が直前のコミット（または直前のステージングエリアへの登録）に戻る。  
ステージングエリアへの変更の取り消しは、ファイルの状態はそのままでステージングエリアへの登録だけを取り消します。

***
[Work Tree]  --"git add"-->  [Staging area]  --"git commit"-->  [Git Directory]  
[Work Tree]  <--"git reset"--  [Staging area]  
[Work Tree]  <-----------------"git checkout"----------------- [Git Directory]
***

ファイルをいろいろ変更したが、やっぱり直前のコミット状態まで戻したい時に、"git checkout"コマンドで、ワークツリーの変更を取り消せる。

- **6. Work Treeの変更を取り消すコマンド（git checkout）**
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

## **7. Check the commit history**
- Check the commit history
```
$ git log
```
- Check the commit history with diffs
```
$ git log -p
```

## **8. Preparing to use git hub**

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

## **9. Clone the remote repository**
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
## **10. Create a dedicated branch and switch**
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

## **11. Edit file and commit**
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

## **12. Create the pull request**
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

## **13. Retrieve the contents of a remote repository to the local repository**

Reflect from remote repository to local repository.
- git pull command
```
$ git pull origin master 
```

- git fetch origin
```
$ git fetch origin
```

## **14. Use multiple branches**

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
[root@localhost63 ichiyasaGitSample]# git push origin speakers-info
Enter passphrase for key '/root/.ssh/id_rsa': d-motoi
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 756 bytes | 756.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'speakers-info' on GitHub by visiting:
remote:      https://github.com/d-moto/ichiyasaGitSample/pull/new/speakers-info
remote:
To github.com:d-moto/ichiyasaGitSample.git
 * [new branch]      speakers-info -> speakers-info
[root@localhost63 ichiyasaGitSample]#

8. Create new branch from master branch
```
$ git checkout master
$ git checkout -b sessions-info
```
```
[root@localhost63 ichiyasaGitSample]# git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
[root@localhost63 ichiyasaGitSample]# git branch
* master
  speakers-info
  update-venue
  update-venue2
[root@localhost63 ichiyasaGitSample]# git checkout -b sessions-info
Switched to a new branch 'sessions-info'
[root@localhost63 ichiyasaGitSample]# git branch
  master
* sessions-info
  speakers-info
  update-venue
  update-venue2
[root@localhost63 ichiyasaGitSample]#
```

**NOTE** :<br>
Look at the difference between speakers-info and sessions-info.  
At present, the sessions-info branch is a copy of the master branch. （Changes made in speakers-info are not reflected).
```
[root@localhost63 ichiyasaGitSample]# git diff sessions-info speakers-info
diff --git a/index.html b/index.html
index 35483fe..f53e6fc 100644
--- a/index.html
+++ b/index.html
@@ -60,17 +60,21 @@
                     <article>
                         <h3>スピーカー</h3>
                         <div class="speaker">
+                       <!--TODO : プロフィール画像を受け取ったら更新する-->
                             <img src="images/speaker1.png" alt="" class="image"/>
                             <div class="inner">
-                                <h4>1人目: 未定</h4>
-                                <p>1人目のプロフィール</p>
+                                <h4>いろふさん</h4>
+                               <p>大阪を中心に仕事をしている、ふつうのプログラマです。</p>
+                               <p>関西Javaエンジニア会の中の人。</p>
+                               <p>主に業務Webアプリの開発をしてきました。</p>
                             </div>
                         </div>
                         <div class="speaker">
                             <img src="images/speaker2.png" alt="" class="image"/>
                             <div class="inner">
-                                <h4>2人目: 未定</h4>
-                                <p>2人目のプロフィール</p>
+                                <h4>うらがみさん</h4>
+                                <p>大阪のプログラマーです。GitHubを日常的に利用しています。</p>
+                               <p>一年間毎日コミットをしてプロフィールページのcontributionsを緑一色にしたことがあります。</p>
                             </div>
                         </div>
                     </article>
@@ -159,4 +163,4 @@
 <script src="assets/js/main.js"></script>

 </body>
-</html>
\ No newline at end of file
+</html>
[root@localhost63 ichiyasaGitSample]#
```

9. Edit the file and proceed to merge

10. Execute commit
```
$ git status
$ git add index.html
$ git commit -m "セッション情報を記載した"
```
11. Push to remote repository and merge
```
$ git push origin sessions-info
```
Merge on Github.<br>
Contents of the index.html file at this time.<br>
```
<!DOCTYPE HTML>
<!--
	Read Only by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
<head>
    <title>Ichiyasa Git User Group</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <link rel="stylesheet" href="assets/css/main.css"/>
</head>
<body>

<!-- Header -->
<section id="header">
    <header>
        <span class="image avatar"><img src="images/avatar.png" alt=""/></span>
        <h1 id="logo"><a href="#">Ichiyasa Git User Group</a></h1>
    </header>
    <nav id="nav">
        <ul>
            <li><a href="#one" class="active">Japan Git User Groupとは</a></li>
            <li><a href="#two">イベントのお知らせ</a></li>
            <li><a href="#three">過去のイベント</a></li>
        </ul>
    </nav>
</section>

<!-- Wrapper -->
<div id="wrapper">

    <!-- Main -->
    <div id="main">

        <!-- One -->
        <section id="one">
            <div class="container">
                <header class="major">
                    <h2>Ichiyasa Git User Group</h2>
                </header>
                <p>Gitを利用する人々のコミュニティです。</p>
                <p>勉強会を企画・運営し、情報交換の場を提供しています。</p>
                <p>このコミュニティーは、非営利目的で活動しています。</p>
            </div>
        </section>

        <!-- Two -->
        <section id="two">
            <div class="container">
                <h2>第２回Git勉強会</h2>
                <div class="features">
                    <p>第２回Git勉強会を開催します。みなさま、是非ご参加ください！</p>
                    <article>
                        <h3>イベント日時・場所</h3>
                        <p>3月23日 19:00開始</p>
                        <p>株式会社インプレス イベントセミナー会場</p>
                    </article>
                    <article>
                        <h3>スピーカー</h3>
                        <div class="speaker">
                            <img src="images/speaker1.png" alt="" class="image"/>
                            <div class="inner">
                                ★<h4>1人目: 未定</h4>
                                ★<p>1人目のプロフィール</p>
                            </div>
                        </div>
                        <div class="speaker">
                            <img src="images/speaker2.png" alt="" class="image"/>
                            <div class="inner">
                                ★<h4>2人目: 未定</h4>
                                ★<p>2人目のプロフィール</p>
                            </div>
                        </div>
                    </article>
                    <article>
                        <h3>タイムテーブル</h3>
                        <div class="table-wrapper">
                            <table class="alt">
                                <thead>
                                <tr>
                                    <th>時間</th>
                                    <th>内容</th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr>
                                    <td>19:00〜19:05</td>
                                    <td>オープニング</td>
                                </tr>
                                <tr>
                                    <td>19:05〜19:50</td>
                                    ★<td>私のGitの使い方（いろふさん）</td>
                                </tr>
                                <tr>
                                    <td>19:50〜20:00</td>
                                    <td>休憩</td>
                                </tr>
                                <tr>
                                    <td>20:00〜20:45</td>
                                    ★<td>現場で使える！実践Git（うらがみさん）</td>
                                </tr>
                                <tr>
                                    <td>20:45〜21:00</td>
                                    <td>クロージング</td>
                                </tr>
                                <tr>
                                    <td>21:00〜</td>
                                    <td>懇親会</td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </article>
                </div>
            </div>
        </section>

        <!-- Three -->
        <section id="three">
            <div class="container">
                <h2>過去のイベント</h2>
                <h3>第１回Git勉強会</h3>
                <div class="features">
                    <article>
                        <h4>Gitはじめの一歩 (@ihcomegaさん)</h4>
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/RZizY7tGPn8?rel=0"
                                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                    </article>
                    <article>
                        <h4>Git実践入門 (@syobochimさん)</h4>
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/LocX863UA_w?rel=0"
                                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                    </article>
                </div>
            </div>
        </section>
    </div>

    <!-- Footer -->
    <section id="footer">
        <div class="container">
            <ul class="copyright">
                <li>&copy; Untitled. All rights reserved.</li>
                <li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
            </ul>
        </div>
    </section>

</div>

<!-- Scripts -->
<script src="assets/js/jquery.min.js"></script>
<script src="assets/js/jquery.scrollzer.min.js"></script>
<script src="assets/js/jquery.scrolly.min.js"></script>
<script src="assets/js/skel.min.js"></script>
<script src="assets/js/util.js"></script>
<script src="assets/js/main.js"></script>

</body>
</html>
```

12. Import the contents of the master branch into the topic branch. (Changes in the sessions-info branch are imported into the speakers-info branch.)

**NOTE** : <br>
In 11, the changes made in 11 are not reflected in the local repository because the branches were merged on the remote repository.<br>
Use the git pull command to update the master branch in the local repository to the latest state.

```
$ git checkout master
$ git pull origin master
```

13. Import the latest information from the master branch
```
$ git checkout speakers-info
$ git merge master
```
14. Execute commit
```
$ git status
$ git commit -am "いろふさんの画像を追加した。"
```
15. Create pull request and merge
```
$ git push origin speakers-info
```

## **Udemy**

## **git に push する**

1. ローカルレポジトリにリモートレポジトリを追加する。
```
# git remote add origin https://github.com/example/example.git
```
originというショートカットでURLのリモートレポジトリを登録する。

2. リモートレポジトリ（GitHub）へ送信する。
```
# git push <remote name> <branch name>
# git push origin master
```

3. tokenの作成
git のページ
--> 右上の丸いアイコン
--> developer settings
--> personal access tokens
から作成

4. 新規レポジトリの作成
git のページ
--> 右上の丸いアイコン
--> your profile
--> repositories
から作成

5. git に push する
```
# git remote add origin git@github.com:d-moto/for_study_git.git
# git push -u origin main
```

```
mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ git remote add origin git@github.com:d-moto/for_study_git.git

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ git remote -v
origin  git@github.com:d-moto/for_study_git.git (fetch)
origin  git@github.com:d-moto/for_study_git.git (push)

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ git push -u origin master
Enter passphrase for key '/c/Users/mokos/.ssh/id_rsa':d-motoi
Enumerating objects: 51, done.
Counting objects: 100% (51/51), done.
Delta compression using up to 16 threads
Compressing objects: 100% (47/47), done.
Writing objects: 100% (51/51), 12.82 KiB | 1010.00 KiB/s, done.
Total 51 (delta 15), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (15/15), done.
To github.com:d-moto/for_study_git.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$

```

## **コマンドにエイリアスをつける**

```
# git config --global alias.ci commit
# git config --global alias.st status
# git config --global alias.br branch
# git config --global alias.co checkout
```

## **バージョン管理しないファイルを指定する**

".gitignore"ファイルを作成する。
```

## **変更を元に戻す**

1. ファイルの変更を取り消す
```
# git checkout -- <file name>
-- ワークツリーの状態をステージの状態と同じにする。
# git checkout -- <directory name>
*全変更を取り消す
# git checkout -- .

2. ステージした変更を取り消す
```
# git reset HEAD <file name>
# git reset HEAD <directory name>
*全変更を取り消す
# git reset HEAD .
指定した変更をステージから取り消すだけなので、ワークツリーへの影響はない。

HEADとは
自分がいるブランチの最新のコミット状態（リモートレポジトリの最新のコミット状態）を表している。

3. 直前のコミットをやり直す
```
# git commit --amend
```
リモートレポジトリにPushしたコミットはやり直せない。

## **リモートレポジトリを表示する**
```
# git remote
URLも表示する。
# git remote -v
```

## **リモートレポジトリを登録する（複数可）**
```
# git remote add <remote name> <remote URL>

# git remote add origin https://......
# git remote add tutorial https://.....
```

## **リモートレポジトリから情報を取得する**
リモートレポジトリから情報を取得する方法は、2種類ある。
- fetch
- pull

1. fetch
```
# git fetch <remote name>
# git fetch origin
```
fetch はリモートレポジトリからローカルレポジトリへ情報を持ってくる。リモートのワークツリーへは反映されない。
ワークツリーへ反映させたい時は、git mergeコマンドを使用する。

```
# git fetch origin
# git branch -a
# git checkout remotes/origin/master
# ls -al
# git checkout master
# git branch -a
# git merge origin/master
```

2. pull
pullを使うのは、リモートから情報を取得してマージまでを一度にやりたい時。
ワークツリーへも変更が反映される。

```
# git pull <remote name> <branch name>
# git pull origin master

上記のコマンドは以下のコマンドと同値
# git fetch origin master
# git merge origin/master
```

**注意**
git pull は、それを実行すると、現在自分がいるブランチにマージが実行されてしまう。

例えば、[maste][sub-branch]という2つのブランチがあったとして、現在masterブランチにいるとき、
```
# git pull origin sub-branch
```
を実行すると、今いるmasterブランチに、sub-branchの内容がマージされてしまう。

## **リモートの詳細表示を知る**
```
# git remote show <remote name>
# git remote show origin
```
```
$ git remote show origin
Enter passphrase for key '/c/Users/mokos/.ssh/id_rsa':
* remote origin
  Fetch URL: git@github.com:d-moto/WindowsRepository.git
  Push  URL: git@github.com:d-moto/WindowsRepository.git
  HEAD branch: master
  Remote branch:
    master tracked
  Local ref configured for 'git push':
    master pushes to master (fast-forwardable)
```

## **リモートの変名、削除**
```
# git remote rename <old remote name> <new remote name>
# git remote rename origin origin2

# git remote rm <remote name>
# git remote rm origin2
```

## **ブランチとマージ**

1. branchとは
並行して複数機能を開発するための仕組み

Gitのデータの持ち方
リポジトリの中身
圧縮ファイル、ツリーファイル、コミットファイル
コミットはスナップショット

ブランチはコミットIDを指したポインタ
HEADは今作業しているブランチのポインタ

2. branchを新規に追加する
```
# git branch <branch name>
# git branch testbranch
```

```
# git branch
# すべてのブランチ
# git branch -a
```
HEADなどがどのブランチを指しているかを確認するときは、以下のコマンドを使用すると良い。
```
# git log --oneline --decorate
```

3. branchを切り替える
```
# git checkout <既存のbranch>
# git checkout -b <new branch>
```

4. 変更履歴をマージする
```
# git merge <branch name>
# git merge <remote name/branch name>
# git merge origin/master　# 作業中のブランチにマージする
```
- マージには3種類ある。
-- Fast Foward:早送りマージ（ポインタが前にずれるだけ）
-- Auto Merge:基本的なマージ（マージコミットという新しいコミットを作る。親コミットが2つ）
-- conflict

Fast Forwardの例：
masterブランチからbugfixブランチを作成し、bugfixブランチ上で、bugfix.txtを作成。
そのあとに、bugfixブランチの変更をmasterブランチへマージする。
この時、masterブランチでは、bugfixブランチ作成時点から、変更が一切ないため、masterブランチのポインタは、bugfixブランチの最新のコミットへずれるだけとなる。
これが、Fast Forward

```
[root@localhost63 Git]# git branch
  bugfix
* master
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]#
[root@localhost63 Git]# git checkout bugfix
Switched to branch 'bugfix'
[root@localhost63 Git]# git branch
* bugfix
  master
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]#
[root@localhost63 Git]# touch bugfix.txt
[root@localhost63 Git]# git add bugfix.txt
[root@localhost63 Git]# git commit -m "create bugfix.txt"
[bugfix 900dbde] create bugfix.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 bugfix.txt
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root   0 12月 14 21:52 bugfix.txt
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]# git checkout master
Switched to branch 'master'
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]# git merge bugfix
Updating 355969c..900dbde
Fast-forward
 bugfix.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 bugfix.txt
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root   0 12月 14 21:53 bugfix.txt
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]#
```

Auto Mergeの例：

```
[root@localhost63 Git]# git branch
  bugfix
* master
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root   0 12月 14 21:53 bugfix.txt
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]# touch master-fix
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root   0 12月 14 21:53 bugfix.txt
-rw-r--r-- 1 root root   0 12月 14 21:58 master-fix
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]#
[root@localhost63 Git]# git add master-fix
[root@localhost63 Git]# git commit -m "master-fix added"
[master 7fca0f9] master-fix added
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 master-fix
[root@localhost63 Git]#
[root@localhost63 Git]# git checkout bugfix
Switched to branch 'bugfix'
[root@localhost63 Git]#
[root@localhost63 Git]#
[root@localhost63 Git]# git branch
* bugfix
  master
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root   0 12月 14 21:53 bugfix.txt
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]# touch bugfix-fix
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root   0 12月 14 21:59 bugfix-fix
-rw-r--r-- 1 root root   0 12月 14 21:53 bugfix.txt
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]# git add .
[root@localhost63 Git]# git commit -m "bugfix-fix added"
[bugfix 4158baf] bugfix-fix added
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 bugfix-fix
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root   0 12月 14 21:59 bugfix-fix
-rw-r--r-- 1 root root   0 12月 14 21:53 bugfix.txt
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]#
[root@localhost63 Git]# git checkout master
Switched to branch 'master'
[root@localhost63 Git]# git branch
  bugfix
* master
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root   0 12月 14 21:53 bugfix.txt
-rw-r--r-- 1 root root   0 12月 14 21:59 master-fix
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]# git merge bugfix
hint: Waiting for your editor to close the file... code --wait: code: コマンドが見つかりません
error: There was a problem with the editor 'code --wait'.
Not committing merge; use 'git commit' to complete the merge.
[root@localhost63 Git]# git status
On branch master
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        new file:   bugfix-fix

[root@localhost63 Git]# git commit -m "merge bugfix-fix"
[master 4427fe3] merge bugfix-fix
[root@localhost63 Git]#
[root@localhost63 Git]# git log --oneline
4427fe3 (HEAD -> master) merge bugfix-fix
4158baf (bugfix) bugfix-fix added
7fca0f9 master-fix added
900dbde create bugfix.txt
355969c (origin/master) add emulater.c
2a9bccb rename sshkey file name
120da98 modify .gitignore
d2dd84c make ignore file
92b96cb modify readme
f9f75a3 modify readme
dc6a5dc 2022-12-11
d580a04 create readme.md file
5d51a5d 2022/11/12
6b4a5c8 add readme.md
f3c1df2 first commit
[root@localhost63 Git]# ls -l
合計 8
drwxr-xr-x 2 root root  95 12月 14 09:50 C
drwxr-xr-x 3 root root  43 11月 28 11:13 Python
-rw-r--r-- 1 root root   0 12月 14 22:00 bugfix-fix
-rw-r--r-- 1 root root   0 12月 14 21:53 bugfix.txt
-rw-r--r-- 1 root root   0 12月 14 21:59 master-fix
-rw-r--r-- 1 root root 413 12月 11 22:59 readme.md
-rw-r--r-- 1 root root  43 11月 11 23:50 test
[root@localhost63 Git]#
```