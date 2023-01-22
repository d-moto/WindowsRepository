# Virtual Boxを使用していた際のメモ

## VirtualBoxをコマンドで操作したい場合
1. cmdを開く。
2. VBをインストールしたディレクトリに移動する。  
```shell
PS C:\Users\axppe> cd 'C:\Program Files\Oracle\VirtualBox\'
PS C:\Program Files\Oracle\VirtualBox>
```
3. コマンドを打ち込む。   
```shell
C:\Program Files\Oracle\VirtualBox>VBoxManage.exe startvm AlmaLinux9 --type headless

C:\Program Files\Oracle\VirtualBox>VBoxManage.exe list vms
"AlmaLinux9" {6ebc2119-de35-467b-a695-047eb2e424f5}

C:\Program Files\Oracle\VirtualBox>VBoxManage.exe list runningvms

C:\Program Files\Oracle\VirtualBox>
C:\Program Files\Oracle\VirtualBox>
C:\Program Files\Oracle\VirtualBox>VBoxManage.exe startvm "AlmaLinux9" --type headless
Waiting for VM "AlmaLinux9" to power on...
VM "AlmaLinux9" has been successfully started.

C:\Program Files\Oracle\VirtualBox>VBoxManage.exe list runningvms
"AlmaLinux9" {6ebc2119-de35-467b-a695-047eb2e424f5}

C:\Program Files\Oracle\VirtualBox>
C:\Program Files\Oracle\VirtualBox>VBoxManage.exe controlvm AlmaLinux9 poweroff
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%

C:\Program Files\Oracle\VirtualBox>VBoxManage.exe list runningvms

C:\Program Files\Oracle\VirtualBox>
```

## 参考
```
VirtualBoxをコマンドで操作する場合はVBoxManageというコマンドで操作を行います。
Windowsの場合、以下にあるため、パスを切りましょう。

パス
C:\Program Files\Oracle\VirtualBox
## 参照系コマンド一覧
説明	コマンド
全ての仮想マシン一覧の表示	VBoxManage list vms
起動中の仮想マシン一覧の表示	VBoxManage list runningvms
仮想マシンの詳細表示	VBoxManage showvminfo [UUID or VM名]
仮想マシンのスナップショット一覧表示	VBoxManage snapshot [UUID or VM名] list
指定したスナップショットの仮想マシン詳細表示	VBoxManage snapshot [UUID or VM名] showvminfo [スナップショット名]
操作系コマンド一覧
説明	コマンド
仮想マシンの起動（GUIあり）	VBoxManage startvm [UUID or VM名]
仮想マシンの起動（ボタン表示なし）	VBoxManage startvm [UUID or VM名] --type sdl
仮想マシンの起動（GUIなし）	VBoxManage startvm [UUID or VM名] --type headless
仮想マシンの起動（GUIなし変更可）	VBoxManage startvm [UUID or VM名] --type separate
仮想マシンの電源オフ	VBoxManage controlvm [UUID or VM名] poweroff
仮想マシンのACPIシャットダウン	VBoxManage controlvm [UUID or VM名] acpipowerbutton
仮想マシンの再起動	VBoxManage controlvm [UUID or VM名] reset
仮想マシンのサスペンド	VBoxManage controlvm [UUID or VM名] savestate
仮想マシンの一時停止	VBoxManage controlvm [UUID or VM名] pause
仮想マシンの再開	VBoxManage controlvm [UUID or VM名] resume
スナップショットの作成	VBoxManage snapshot [UUID or VM名] take [スナップショット名]
指定したスナップショットの削除	VBoxManage snapshot [UUID or VM名] delete [スナップショット名]
指定したスナップショット名の修正	VBoxManage snapshot [UUID or VM名] edit [スナップショット名] --name=[新しいスナップショット名]
直前のスナップショットへのリストア	VBoxManage snapshot [UUID or VM名] restorecurrent
指定したスナップショットへのリストア	VBoxManage snapshot [UUID or VM名] restore [スナップショット名]
ホストからゲストOSの操作	VBoxManage guestcontrol [UUID or VM名] run --exe "[コマンドフルパス]" --username [ゲストOSユーザ名] --password [ゲストOSパスワード]
```
