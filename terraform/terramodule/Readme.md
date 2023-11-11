## Terraform moduleとは

- モジュールとは同一ディレクトリにあるTerraform構成ファイル一式
- 複数のモジュールで構成することができる
- ルートモジュールから子モジュールを呼び出して使うことができる。

## Terraform Moduleの使い方

## Azure仮想マシンをモジュール化してみる

リソースセクションで分ける

- リソースグループ
- 仮想ネットワーク・サブネット
- 仮想マシン・ネットワークインターフェース

これらを3つのモジュールに分解して各リソースごとにディレクトリを分ける。

- ルートディレクトリ
- モジュール関連
  - リソースグループ
  - 仮想マシン
  - 仮想ネットワーク
  
```
mokos@DESKTOP-NOUPOER MINGW64 ~/gittmp/WindowsRepository/terraform/terramodule (dev-terra)
$ ls -lR
.:
total 22
-rw-r--r-- 1 mokos 197609  953 Nov 11 13:00 Readme.md
-rw-r--r-- 1 mokos 197609    0 Nov 11 13:26 VM-01.tf
-rw-r--r-- 1 mokos 197609    0 Nov 11 13:26 VM-02.tf
-rw-r--r-- 1 mokos 197609 1887 Nov 11 13:12 VM.tf
-rw-r--r-- 1 mokos 197609  232 Nov 11 13:12 main.tf
drwxr-xr-x 1 mokos 197609    0 Nov 11 13:16 modules/
-rw-r--r-- 1 mokos 197609  601 Nov 11 13:12 provider.tf
-rw-r--r-- 1 mokos 197609 8889 Nov 11 13:12 terraform.xlsx
-rw-r--r-- 1 mokos 197609    0 Nov 11 13:12 variable.tf

./modules:
total 0
drwxr-xr-x 1 mokos 197609 0 Nov 11 13:16 rg/
drwxr-xr-x 1 mokos 197609 0 Nov 11 13:16 vm/
drwxr-xr-x 1 mokos 197609 0 Nov 11 13:16 vnet/

./modules/rg:
total 0
-rw-r--r-- 1 mokos 197609 0 Nov 11 13:12 output.tf
-rw-r--r-- 1 mokos 197609 0 Nov 11 13:12 rg.tf
-rw-r--r-- 1 mokos 197609 0 Nov 11 13:12 variable.tf

./modules/vm:
total 0
-rw-r--r-- 1 mokos 197609 0 Nov 11 13:12 VM.tf
-rw-r--r-- 1 mokos 197609 0 Nov 11 13:12 variable.tf

./modules/vnet:
total 0
-rw-r--r-- 1 mokos 197609 0 Nov 11 13:12 output.tf
-rw-r--r-- 1 mokos 197609 0 Nov 11 13:12 variable.tf
-rw-r--r-- 1 mokos 197609 0 Nov 11 13:12 vnet.tf

mokos@DESKTOP-NOUPOER MINGW64 ~/gittmp/WindowsRepository/terraform/terramodule (dev-terra)
$
```

※仮想マシン2台作成時のディレクトリ構成になります。ルートディレクトリにVM-01.tf、VM-02.tfの2つあるのはその為です。

## module化の進め方

- ルートモジュールにあった、vm.tfのリソースグループ部分をrg.tfとして分割

