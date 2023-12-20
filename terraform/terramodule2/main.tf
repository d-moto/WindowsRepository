module "resource_group" {
  source              = "./modules/resource_group"
  resource_group_name = "moduleRG"
  location            = "japaneast"
}

module "vnet" {
  source              = "./modules/vnet"
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  vnet_name           = "moduleVnet"
  address_space       = [${var.address_space}]
}

module "subnets" {
  source              = "./modules/subnet"
  resource_group_name = module.resource_group.resource_group_name
  vnet_name           = module.vnet.vnet_name
  subnet_names        = var.subnet_names
  subnet_prefixes     = var.subnet_prefixes
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
