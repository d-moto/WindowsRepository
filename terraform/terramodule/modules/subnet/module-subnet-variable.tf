## Resource Group
variable "rg_name" {}

## Virtual Network Name
variable "vnet_name" {}

## Subnet Name
# variable "subnet_name_eth0" {}
# variable "subnet_name_eth1" {}
# variable "subnet_name_eth2" {}
# variable "subnet_name_eth3" {}
variable "subnet_names" {
  description = "List of subnet names"
  type        = list(string)
}
# variable "subnet_address_prefixes_eth0" {}
# variable "subnet_address_prefixes_eth1" {}
# variable "subnet_address_prefixes_eth2" {}
# variable "subnet_address_prefixes_eth3" {}
variable "subnet_address_prefixes" {
  description = "List of subnet address prefixes"
  type        = list(string)
}