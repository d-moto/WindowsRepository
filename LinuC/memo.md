
# 1.3 ブートプロセスとsystemd
</br>

## 1.3.1 Linuxのブートプロセス
---
</br>

システムの電源を入れてからOSが起動するまでは、コンピューターのアーキテクチャーにより異なる。
一般的なPC(x86/x86_64)では以下のような順番。

1. BIOS/UEFIが起動
2. BIOS/UEFIがハードウェアのチェックや初期化を行う。
3. 起動デバイス（システムディスク）に書き込まれたブートローダー（boot loader)を読み出す。
4. ブートローダーに制御を移す。
5. ブートローダーは起動デバイス上のカーネルをメモリ上へ読み込む。
6. 読み込まれたカーネルはメモリの初期化、システムクロックの設定を行う。
7. カーネルは仮のルートファイルシステムをマウントする。（initramfs:初期RAMディスク）  
初期RAMディスクには、システムの起動に必要なデバイスドライバが組み込まれている。  
これにより、ハードディスクなどのデバイスへアクセスできるようになる。  
</br>
8. ルートファイルシステムが使えるようになると、カーネルは最初のプロセスであるinit(またはsystemd)プロセスを実行する。
9. initは必要なサービスを順次起動していき、最後にログインプロンプトを表示して起動処理を完了する。

</br>

## 1.3.2 ブートターゲット
---
</br>

システム起動時のターゲットを知るためには、以下のコマンドを用いる。
</br>
```
# systemctl get-default
```
multi-user.targetに設定されている場合。
```
[root@localhost63 ~]# systemctl get-default
multi-user.target
[root@localhost63 ~]#
```

</br>

「graphical.target」や「multi-user.target」は、systemdの処理単位(Unit)をまとめたターゲット。いくつかのターゲットがあらかじめ設定されている。

</br>

**主なターゲット**
ターゲット | 説明
---|---
multi-user.target | CUIログイン
graphical.target | グラフィカルログイン
poweroff.target | システム終了
rescue.target | レスキュー(シングルユーザー)モード
reboot.target | システム再起動

</br>

システム起動時のターゲットを変更するには、set-defaultサブコマンドを使用する。(root権限が必要)

```
# systemctl set-default <target name>

# systemctl set-default multi-user.target
```

</br>

ターゲットを指定して、システムを終了したり、再起動したりすることもできる。その場合はisolateサブコマンドを使用する。(root権限が必要)
```
# systemctl isolate <target name>

# 直ちにシステムを再起動する場合
# systemctl isolate reboot.target
```

</br>

メンテナンス用のシステム状態として、シングルユーザーモード(レスキューモード)が存在する。  
シングルユーザーモードに切り替える場合は以下のようにする。
```
# systemctl isolate rescue.target
```

</br>

## 1.3.3 シャットダウンおよび再起動
---
</br>

![](20221215190937_1.jpg)
