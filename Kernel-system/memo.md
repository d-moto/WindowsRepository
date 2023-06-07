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

