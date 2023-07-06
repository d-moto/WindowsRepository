# Linux の概要

## システムコール発行の可視化
プロセスのシステムコールはstraceコマンドで確認できる

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println("hello world")
}
```

ビルドする

```shell
# go build hello.go
# ./hello
hello world
```

straceコマンドでシステムコールを確認する
-o オプションで出力先を指定できる。
```shell
# strace -o hello.log ./hello
hello world
```

ログを確認する。
```
[root@localhost63 sec1]# less hello.log | grep write
write(1, "hello world\n", 12)           = 12
[root@localhost63 sec1]#
```
write()システムコールが発行されていることがわかる。

## システムコールを処理している時間の割合
以下の無限ループのプログラムをバックグラウンドで処理する。
```python
while True:
    pass
```

tasksetコマンドで、バックグラウンドで実行する。
```
[root@localhost63 sec1]# taskset -c 0 ./inf-loop.py  &
[1] 65723
[root@localhost63 sec1]#
```
`taskset -c <論理CPU番号> <コマンド>`で使用する。
プロセス番号65723でバックグラウンドで実行されている。

sar コマンドで確認する。
```
[root@localhost63 sec1]# sar -P 0 1 1
Linux 4.18.0-425.19.2.el8_7.x86_64 (localhost63)        2023年06月08日  _x86_64_        (4 CPU)

20時30分20秒     CPU     %user     %nice   %system   %iowait    %steal     %idle
20時30分21秒       0    100.00      0.00      0.00      0.00      0.00      0.00
平均値:        0    100.00      0.00      0.00      0.00      0.00      0.00
[root@localhost63 sec1]#
```
`-P 0`が論理CPU0のデータを採取するという意味。
次の1が1sごとに情報を取得するという意味。
最後の1が1回情報を採取するという意味。

実験が終わったら、killコマンドでプログラムを終了させる。


