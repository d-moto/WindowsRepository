/*リソースグループ*/

variable "rg-name" {}
variable "rg-location" {}
/*ネットワークIF*/
variable "nic-name" {}
variable "subnet_id" {}
/*仮想マシン*/
variable "vm-name" {}
variable "admin_username" {}
variable "admin_password" {
    sensitive = true
}