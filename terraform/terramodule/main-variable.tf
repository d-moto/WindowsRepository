## Resource Group Name
variable "rg_name1" {
  default = "myRG1"
}

## Resouce Group Location 
variable "rg_location" {
  default = "japaneast"
}

## Vnet
variable "vnet_name1" {
  default = "myVnet1"
}
variable "vnet_address_space1" {
  default = "172.10.0.0/16"
}

## Subnet
variable "subnet_name1" {
  default = "mySubnet1"
}

variable "subnet_address_prefixes1" {
  default = "172.10.10.0/24"
}

## Network Interface
variable "network_interface_name1" {
  default = "eth0"
}
variable "private_ip_address1" {
  default = "172.10.10.100"
}

## Linux Virtual Machine
variable "vm_name1" {
  default = "myVM"
}

variable "vm_size1" {
  default = "Standard_F2"
}

variable "vm_adminuser1" {
  default = "adminuser"
}