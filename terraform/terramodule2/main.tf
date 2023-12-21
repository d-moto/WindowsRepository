## call resource group module
module "resource_group" {
  source              = "./modules/resource_group"
  resource_group_name = var.resource_group_name
  location            = var.location
}

## ★
## variable
variable "resource_group_name" {
  default = "moduleRG"
}
variable "location" {
  default = "japaneast"
}

## call vnet module
module "vnet" {
  source              = "./modules/vnet"
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  vnet_name           = var.vnet_name
  address_space       = [var.address_space]
}

## ★
## variable
variable "vnet_name" {
  default = "moduleVnet"
}

variable "address_space" {
    default = "172.30.0.0/16"
}

## ★
## call subnet module
module "subnets_node" {
  source              = "./modules/subnet"
  resource_group_name = module.resource_group.resource_group_name
  vnet_name           = module.vnet.vnet_name
  subnet_names        = var.subnet_names_node
  subnet_prefixes     = var.subnet_prefixes_node
  # subnet_ids          = module.subnets.subnet_ids
  # nsg_ids             = module.nsg.nsg_ids
}

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

## ★
## call subnet module
module "subnets_ansible" {
  source              = "./modules/subnet"
  resource_group_name = module.resource_group.resource_group_name
  vnet_name           = module.vnet.vnet_name
  subnet_names        = var.subnet_names_ansible
  subnet_prefixes     = var.subnet_prefixes_ansible
  # subnet_ids          = module.subnets.subnet_ids
  # nsg_ids             = module.nsg.nsg_ids
}

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

## ★
## call network interface module
# module "network_interface" {
#   source              = "./modules/network_interface"
#   nic_name            = "myNic"
#   subnet_ids          = module.subnets.subnet_ids
#   resource_group_name = module.resource_group.resource_group_name
#   location            = module.resource_group.location
#   private_ip_addresses  = var.private_ip_addresses
# }

## variable
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
    "172.30.50.10"
  ]
}

## ★
## call vm module
# module "vm" {
#   source              = "./modules/vm"
#   instance_count      = 2  # 1または2に変更可能
#   vm_name             = var.vm_name_node
#   resource_group_name = module.resource_group.resource_group_name
#   location            = module.resource_group.location
#   ssh_public_key      = "/home/alma1/Git-win/WindowsRepository/terraform/terramodule2/id_rsa.pub"  # SSH公開キーのパスを指定
#   network_interface_ids = [
#     slice(module.network_interface.network_interface_ids, 0, 4),
#     slice(module.network_interface.network_interface_ids, 4, 8)
#   ]
# }

# ## variable
# variable "vm_name_node" {
#   default = "cluster1"
# }



# ## call network security group module
# module "nsg" {
#   source              = "./modules/nsg"
#   nsg_names           = ["nsg1", "nsg2", "nsg3", "nsg4"]
#   resource_group_name = module.resource_group.resource_group_name
#   location            = module.resource_group.location
# }

## variable
variable "instance_count" {
  description = "Number of VM instances to create"
  default     = 2
}

variable "vm_name" {
  description = "Base name of the virtual machine"
  default     = "myRHELVM"
}


