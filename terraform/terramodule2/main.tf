## call resource group module
module "resource_group" {
  source              = "./modules/resource_group"
  resource_group_name = "moduleRG"
  location            = "japaneast"
}

## call vnet module
module "vnet" {
  source              = "./modules/vnet"
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  vnet_name           = "moduleVnet"
  address_space       = [var.address_space]
}

## call subnet module
module "subnets" {
  source              = "./modules/subnet"
  resource_group_name = module.resource_group.resource_group_name
  vnet_name           = module.vnet.vnet_name
  subnet_names        = var.subnet_names
  subnet_prefixes     = var.subnet_prefixes
}

## call vm module
module "vm" {
  source              = "./modules/vm"
  instance_count      = 2  # 1または2に変更可能
  vm_name             = "myRHELVM"
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  network_interface_ids = module.network_interface.network_interface_ids
  ssh_public_key      = "/home/alma1/Git-win/WindowsRepository/terraform/terramodule2/id_rsa.pub"  # SSH公開キーのパスを指定
}

## call network interface module
module "network_interface" {
  source              = "./modules/network_interface"
  nic_name            = "myNic"
  subnet_ids          = module.subnets.subnet_ids
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
}

## variable
variable "address_space" {
    default = "172.30.0.0/16"
}

variable "subnet_names" {
  description = "List of subnet names"
  type        = list(string)
  default     = ["subnet1", "subnet2", "subnet3", "subnet4", "subnet5", "subnet6", "subnet7", "subnet8"]
}

variable "subnet_prefixes" {
  description = "List of subnet address prefixes"
  type        = list(string)
  default     = ["172.30.10.0/24", "172.30.20.0/24", "172.30.30.0/24", "172.30.40.0/24", "172.30.50.0/24", "172.30.60.0/24", "172.30.70.0/24", "172.30.80.0/24"]
}

variable "instance_count" {
  description = "Number of VM instances to create"
  default     = 2
}

variable "vm_name" {
  description = "Base name of the virtual machine"
  default     = "myRHELVM"
}


