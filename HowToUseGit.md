
# How To Use Git 

## Set Up Git
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
> When you execute this command "git config --global", the file "/c/Users/mokos/.gitconfig" is created and the configuration is written.

## Set up and create local repository
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
**Files that are not registered under git management are treated as "Untracked files" by the git status command.**
```
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

## check differences of git files
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
--- a/HowToUseGit.md
+++ b/HowToUseGit.md
@@ -95,4 +95,4 @@ $ git diff
 ```
 $ git diff --cached
 ```
-
+3.

mokos@DESKTOP-NOUPOER MINGW64 ~/git-ichiyasa (master)
$ git diff --cached
diff --git a/HowToUseGit.md b/HowToUseGit.md
new file mode 100644
index 0000000..0a161d4
--- /dev/null
+++ b/HowToUseGit.md
@@ -0,0 +1,98 @@
+
+# How To Use Git
+
+## Set Up Git
+1. set up user name
................................
```

## commit the files
1. check status of local repository
```
$ git statsu
```
2. execute commit
```
$ git commit
```

