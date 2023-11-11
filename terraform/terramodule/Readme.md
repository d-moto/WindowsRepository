## Terraform module�Ƃ�

- ���W���[���Ƃ͓���f�B���N�g���ɂ���Terraform�\���t�@�C���ꎮ
- �����̃��W���[���ō\�����邱�Ƃ��ł���
- ���[�g���W���[������q���W���[�����Ăяo���Ďg�����Ƃ��ł���B

## Terraform Module�̎g����

## Azure���z�}�V�������W���[�������Ă݂�

���\�[�X�Z�N�V�����ŕ�����

- ���\�[�X�O���[�v
- ���z�l�b�g���[�N�E�T�u�l�b�g
- ���z�}�V���E�l�b�g���[�N�C���^�[�t�F�[�X

������3�̃��W���[���ɕ������Ċe���\�[�X���ƂɃf�B���N�g���𕪂���B

- ���[�g�f�B���N�g��
- ���W���[���֘A
  - ���\�[�X�O���[�v
  - ���z�}�V��
  - ���z�l�b�g���[�N
  
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

�����z�}�V��2��쐬���̃f�B���N�g���\���ɂȂ�܂��B���[�g�f�B���N�g����VM-01.tf�AVM-02.tf��2����̂͂��ׂ̈ł��B

## module���̐i�ߕ�

- ���[�g���W���[���ɂ������Avm.tf�̃��\�[�X�O���[�v������rg.tf�Ƃ��ĕ���



$ tree .
Folder PATH listing for volume Windows
Volume serial number is C201-CCFE
C:\USERS\MOKOS\GITTMP\WINDOWSREPOSITORY\TERRAFORM\TERRAMODULE
|   .terraform.lock.hcl
|   provider.tf
|   Readme.md
|   rg1.tf
|   terraform.tfstate
|   terraform.xlsx
|   variable.tf
|
+---.terraform
|   +---modules
|   |       modules.json
|   |
|   \---providers
|       \---registry.terraform.io
|           \---hashicorp
|               \---azurerm
|                   +---3.78.0
|                   |   \---windows_amd64
|                   |           terraform-provider-azurerm_v3.78.0_x5.exe
|                   |
|                   \---3.80.0
|                       \---windows_amd64
|                               terraform-provider-azurerm_v3.80.0_x5.exe
|
\---modules
    +---rg
    |       output.tf
    |       rg.tf
    |       variable.tf
    |
    +---vm
    |       variable.tf
    |       vm.tf
    |
    \---vnet
            output.tf
            variable.tf
            vnet.tf

