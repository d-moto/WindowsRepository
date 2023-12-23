## buildディレクトリ配下の構成

```
# ls -lR

.:
合計 8
drwxr-xr-x 2 alma1 alma1  42 12月 17 09:32 BUILD
drwxr-xr-x 2 alma1 alma1   6 12月 17 09:32 BUILDROOT
-rw-r--r-- 1 root  root    0 12月 17 09:40 README.txt
drwxr-xr-x 3 alma1 alma1  20 12月 17 09:32 RPMS
drwxr-xr-x 2 alma1 alma1  25 12月 17 09:32 SOURCES
drwxr-xr-x 2 alma1 alma1   6 12月 17 01:09 SPECS
drwxr-xr-x 2 alma1 alma1  37 12月 17 09:32 SRPMS
-rw-r--r-- 1 root  root  350 12月 17 01:04 whichdate.c
-rw-r--r-- 1 root  root  706 12月 17 09:31 whichdate.spec

./BUILD:
合計 24
-rwxr-xr-x 1 root root 18128 12月 17 09:32 whichdate
-rw-r--r-- 1 root root   350 12月 17 09:32 whichdate.c

./BUILDROOT:
合計 0

./RPMS:
合計 0
drwxr-xr-x 2 root root 40 12月 17 09:32 x86_64

./RPMS/x86_64:
合計 12
-rw-r--r-- 1 root root 10040 12月 17 09:32 whichdate-1.0-1.x86_64.rpm

./SOURCES:
合計 4
-rw-r--r-- 1 root root 350 12月 17 09:32 whichdate.c

./SPECS:
合計 0

./SRPMS:
合計 8
-rw-r--r-- 1 root root 6610 12月 17 09:32 whichdate-1.0-1.src.rpm
```


## rpmbuildコマンドの実行
```
[root@localhost63 rpmbuild]# rpmbuild -v -ba --define "_topdir /home/alma1/rpmbuild" whichdate.spec
```
