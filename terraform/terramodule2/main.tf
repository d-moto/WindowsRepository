##########################################################################################
## Call resource group module
##########################################################################################
module "resource_group" {
  source              = "./modules/resource_group"
  resource_group_name = var.resource_group_name
  location            = var.location
}

## ★
## Resource Group variable
variable "resource_group_name" {
  default = "moduleRG"
}
variable "location" {
  default = "japaneast"
}

##########################################################################################
## Call vnet module
##########################################################################################
module "vnet" {
  source              = "./modules/vnet"
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  vnet_name           = var.vnet_name
  address_space       = [var.address_space]
}

## ★
## vnet variable
variable "vnet_name" {
  default = "moduleVnet"
}

variable "address_space" {
  default = "172.30.0.0/16"
}

##########################################################################################
## Call subnet module
##########################################################################################
module "subnets_node" {
  source              = "./modules/subnet"
  resource_group_name = module.resource_group.resource_group_name
  vnet_name           = module.vnet.vnet_name
  subnet_names        = var.subnet_names_node
  subnet_prefixes     = var.subnet_prefixes_node
  # subnet_ids          = module.subnets.subnet_ids
  # nsg_ids             = module.nsg.nsg_ids
}

## ★
## subnet variable
variable "subnet_names_node" {
  description = "List of subnet names"
  type        = list(string)
  default     = ["subnet-eth0", "subnet-eth1", "subnet-eth2", "subnet-eth3"]
}

variable "subnet_prefixes_node" {
  description = "List of subnet address prefixes"
  type        = list(string)
  default     = ["172.30.10.0/24", "172.30.20.0/24", "172.30.30.0/24", "172.30.40.0/24"]
}

##########################################################################################
## Call subnet module
##########################################################################################
module "subnets_ansible" {
  source              = "./modules/subnet"
  resource_group_name = module.resource_group.resource_group_name
  vnet_name           = module.vnet.vnet_name
  subnet_names        = var.subnet_names_ansible
  subnet_prefixes     = var.subnet_prefixes_ansible
  # subnet_ids          = module.subnets.subnet_ids
  # nsg_ids             = module.nsg.nsg_ids
}

## ★
## subnet variable
variable "subnet_names_ansible" {
  description = "List of subnet names"
  type        = list(string)
  default     = ["subnet-ansible-eth0"]
}

variable "subnet_prefixes_ansible" {
  description = "List of subnet address prefixes"
  type        = list(string)
  default     = ["172.30.50.0/24"]
}

##########################################################################################
## Call subnet module for Azure Bastion
##########################################################################################
module "subnets_bastion" {
  source              = "./modules/subnet"
  resource_group_name = module.resource_group.resource_group_name
  vnet_name           = module.vnet.vnet_name
  subnet_names        = var.subnet_names_bastion
  subnet_prefixes     = var.subnet_prefixes_bastion
  # subnet_ids          = module.subnets.subnet_ids
  # nsg_ids             = module.nsg.nsg_ids
}

## ★
## subnet variable for Azure Bastion
variable "subnet_names_bastion" {
  description = "List of subnet names"
  type        = list(string)
  default     = ["AzureBastionSubnet"]
}

variable "subnet_prefixes_bastion" {
  description = "List of subnet address prefixes"
  type        = list(string)
  default     = ["172.30.1.0/24"]
}

##########################################################################################
## Call subnet module for windows
##########################################################################################
module "subnets_win" {
  source              = "./modules/subnet"
  resource_group_name = module.resource_group.resource_group_name
  vnet_name           = module.vnet.vnet_name
  subnet_names        = var.subnet_names_win
  subnet_prefixes     = var.subnet_prefixes_win
  # subnet_ids          = module.subnets.subnet_ids
  # nsg_ids             = module.nsg.nsg_ids
}

## ★
## subnet variable
variable "subnet_names_win" {
  description = "List of subnet names"
  type        = list(string)
  default     = ["subnet-win-eth0"]
}

variable "subnet_prefixes_win" {
  description = "List of subnet address prefixes"
  type        = list(string)
  default     = ["172.30.100.0/24"]
}

##########################################################################################
## Call network interface module
##########################################################################################
module "network_interface" {
  source   = "./modules/network_interface"
  nic_name = var.nic_name
  subnet_ids = [
    module.subnets_node.subnet_ids[0],
    module.subnets_node.subnet_ids[1],
    module.subnets_node.subnet_ids[2],
    module.subnets_node.subnet_ids[3],
    module.subnets_node.subnet_ids[0],
    module.subnets_node.subnet_ids[1],
    module.subnets_node.subnet_ids[2],
    module.subnets_node.subnet_ids[3],
    module.subnets_ansible.subnet_ids[0],
    module.subnets_win.subnet_ids[0]
    ]
  nic_counts           = [2, 2, 2, 2, 1, 1]
  resource_group_name  = module.resource_group.resource_group_name
  location             = module.resource_group.location
  private_ip_addresses = var.private_ip_addresses
}

## ★
## network interface variable
variable "nic_name" {
  default = [
    "node1-eth0",
    "node1-eth1",
    "node1-eth2",
    "node1-eth3",
    "node2-eth0",
    "node2-eth1",
    "node2-eth2",
    "node2-eth3",
    "ansible-eth0",
    "win-eth0"

  ]
}
variable "private_ip_addresses" {
  default = [
    "172.30.10.10",
    "172.30.20.10",
    "172.30.30.10",
    "172.30.40.10",
    "172.30.10.20",
    "172.30.20.20",
    "172.30.30.20",
    "172.30.40.20",
    "172.30.50.10",
    "172.30.100.10"
  ]
}

##########################################################################################
## Call vm module for node
##########################################################################################
module "vm_node" {
  source              = "./modules/vm"
  instance_count      = 2 # 1または2に変更可能
  vm_name             = var.vm_name_node
  vm_size             = var.vm_size_node
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  ssh_public_key      = "/home/alma1/Git-win/WindowsRepository/terraform/terramodule2/id_rsa.pub" # SSH公開キーのパスを指定
  network_interface_ids = [
    slice(module.network_interface.network_interface_ids, 0, 4),
    slice(module.network_interface.network_interface_ids, 4, 8)
  ]
}

## ★
## vm variable
variable "vm_name_node" {
  default = [
    "cluster1",
    "cluster2"
  ]
}

variable "vm_size_node" {
  default = [
    "Standard_D3_v2",
    "Standard_D3_v2"
  ]
}

##########################################################################################
## Call vm module for ansible
##########################################################################################
module "vm_ansible" {
  source              = "./modules/vm"
  instance_count      = 1 # 1または2に変更可能
  vm_name             = var.vm_name_ansible
  vm_size             = var.vm_size_ansible
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  ssh_public_key      = "/home/alma1/Git-win/WindowsRepository/terraform/terramodule2/id_rsa.pub" # SSH公開キーのパスを指定
  network_interface_ids = [
    slice(module.network_interface.network_interface_ids, 8, 9)
  ]
  # user_data = var.user_data_ansible
}

## variable
variable "vm_name_ansible" {
  default = [
    "ansible"
  ]
}

variable "vm_size_ansible" {
  default = [
    "Standard_D1_v2"
  ]
}

## ★
## variable
variable "instance_count" {
  description = "Number of VM instances to create"
  default     = 2
}

variable "vm_name" {
  description = "Base name of the virtual machine"
  default     = "myRHELVM"
}

##########################################################################################
## Call vm module for win
##########################################################################################
module "vm_win" {
  source              = "./modules/vm-win"
  instance_count      = 1 # 1または2に変更可能
  vm_name             = var.vm_name_win
  vm_size             = var.vm_size_win
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  ssh_public_key      = "/home/alma1/Git-win/WindowsRepository/terraform/terramodule2/id_rsa.pub" # SSH公開キーのパスを指定
  network_interface_ids = [
    slice(module.network_interface.network_interface_ids, 9, 10),
  ]
}

## ★
## vm variable
variable "vm_name_win" {
  default = [
    "windows1"
  ]
}

variable "vm_size_win" {
  default = [
    "Standard_D2as_v4"
  ]
}

## Linux login with SSH
# az network bastion ssh --name "Bastion" --resource-group "Bastion" --target-resource-id "/subscriptions/<SubID>/resourceGroups/Bastion/providers/Microsoft.Compute/virtualMachines/Ubuntu" --auth-type password --user hiyama

## Linux scp
# az network bastion tunnel --name "Bastion" --resource-group "Bastion" --target-resource-id "/subscriptions/<SubID>/resourceGroups/Bastion/providers/Microsoft.Compute/virtualMachines/ubuntu" --resource-port "22" --port "60001"

## Windows login with RDP
# az network bastion rdp --name "Bastion" --resource-group "Bastion" --target-resource-id "/subscriptions/<SubID>/resourceGroups/Bastion/providers/Microsoft.Compute/virtualMachines/Windows"

## Windows SCP
# az network bastion tunnel --name "Bastion" --resource-group "Bastion" --target-resource-id "/subscriptions/<SUbID>/resourceGroups/Bastion/providers/Microsoft.Compute/virtualMachines/Windows" --resource-port "22" --port "60002"

## 


