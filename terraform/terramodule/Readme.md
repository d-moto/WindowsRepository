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
PS C:\Users\mokos\03Git_work\git-master\WindowsRepository\terraform\terramodule> tree /f /a 
フォルダー パスの一覧:  ボリューム Windows
ボリューム シリアル番号は C201-CCFE です
C:.
|   .terraform.lock.hcl
|   main-nic1.tf
|   main-provider.tf
|   main-rg1.tf
|   main-subnet1.tf
|   main-variable.tf
|   main-vm1.tf
|   main-vnet1.tf
|   Readme.md
|   terraform.tfstate
|   terraform.tfstate.backup
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
+---docs
|       terraform.xlsx
|
\---modules
    +---nic
    |       module-nic-nic.tf
    |       module-nic-output.tf
    |       module-nic-variable.tf
    |
    +---rg
    |       module-rg-output.tf
    |       module-rg-rg.tf
    |       module-rg-variable.tf
    |
    +---subnet
    |       module-subnet-output.tf
    |       module-subnet-subnet.tf
    |       module-subnet-variable.tf
    |
    +---vm
    |       module-vm-output.tf
    |       module-vm-variable.tf
    |       module-vm-vm.tf
    |
    \---vnet
            module-vnet-output.tf
            module-vnet-variable.tf
            module-vnet-vnet.tf

PS C:\Users\mokos\03Git_work\git-master\WindowsRepository\terraform\terramodule> 
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

