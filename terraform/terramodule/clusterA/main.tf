terraform {
  required_providers {
    azurerm   = {
      source  = "hashicorp/azurerm"
      version = "3.78.0"
    }
  }
}

provider "azurerm" {
  # Configuration options
  features {}
  skip_provider_registration = true
}

module "cluster1-rg1" {
  source      = "./../modules/rg"
  rg_name     = "${var.rg_name1}"
  rg_location = "${var.rg_location}"
}

module "cluster1-vnet1" {
    source                  = "./../modules/vnet"
    rg_name                 = module.cluster1-rg1.terraform-rg-name
    rg_location             = module.cluster1-rg1.terraform-rg-location
    vnet_name               = "${var.vnet_name1}"
    vnet_address_space      = "${var.vnet_address_space1}"
}

module "cluster1-subnet1" {
    source                    = "./../modules/subnet"
    rg_name                   = module.cluster1-rg1.terraform-rg-name
    vnet_name                 = module.cluster1-vnet1.terraform-vnet-name
    subnet_names              = "${var.subnet_names1}"
    subnet_address_prefixes   = "${var.subnet_address_prefixes1}"
}

module "cluster1-nic1" {
    source                  = "./../modules/nic"
    network_interface_names = "${var.network_interface_names1}"
    ip_config_names         = "${var.ip_config_names1}"
    rg_name                 = module.cluster1-rg1.terraform-rg-name
    rg_location             = module.cluster1-rg1.terraform-rg-location
    private_ip_addresses    = "${var.private_ip_addresses1}"
    subnet_ids              = module.cluster1-subnet1.terraform-subnet-ids
}

module "cluster1-nic2" {
    source                  = "./../modules/nic"
    network_interface_names = "${var.network_interface_names2}"
    ip_config_names         = "${var.ip_config_names2}"
    rg_name                 = module.cluster1-rg1.terraform-rg-name
    rg_location             = module.cluster1-rg1.terraform-rg-location
    private_ip_addresses    = "${var.private_ip_addresses2}"
    subnet_ids              = module.cluster1-subnet1.terraform-subnet-ids
}

module "cluster1-vm1" {
  source               = "./../modules/vm"
  rg_name              = module.cluster1-rg1.terraform-rg-name
  rg_location          = module.cluster1-rg1.terraform-rg-location
  vm_name              = "${var.vm_name1}"
  vm_size              = "${var.vm_size1}"
  vm_publisher         = "${var.vm_publisher1}"
  vm_offer             = "${var.vm_offer1}"
  vm_sku               = "${var.vm_sku1}"
  vm_version           = "${var.vm_version1}"
  vm_adminuser         = "${var.vm_adminuser1}"
  vm_network_interface_ids = module.cluster1-nic1.terraform-nic-ids
}

module "cluster1-vm2" {
  source               = "./../modules/vm"
  rg_name              = module.cluster1-rg1.terraform-rg-name
  rg_location          = module.cluster1-rg1.terraform-rg-location
  vm_name              = "${var.vm_name2}"
  vm_size              = "${var.vm_size1}"
  vm_publisher         = "${var.vm_publisher1}"
  vm_offer             = "${var.vm_offer1}"
  vm_sku               = "${var.vm_sku1}"
  vm_version           = "${var.vm_version1}"
  vm_adminuser         = "${var.vm_adminuser1}"
  vm_network_interface_ids = module.cluster1-nic2.terraform-nic-ids
}

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

variable "subnet_names1" {
  default = [
    "mySubnet1_eth0",
    "mySubnet1_eth1",
    "mySubnet1_eth2",
    "mySubnet1_eth3"
    ]
}

variable "subnet_address_prefixes1" {
  default = [
    "172.10.10.0/26",
    "172.10.11.0/26",
    "172.10.12.0/26",
    "172.10.13.0/26",
    ]
}

variable "network_interface_names1" {
  default = [
    "eth0",
    "eth1",
    "eth2",
    "eth3",
    ]
}

variable "network_interface_names2" {
  default = [
    "eth4",
    "eth5",
    # "eth6",
    # "eth7",
    ]
}

variable "ip_config_names1" {
  default = [
    "ipconfig_eth0",
    "ipconfig_eth1",
    "ipconfig_eth2",
    "ipconfig_eth3",
    ]
}

variable "ip_config_names2" {
  default = [
    "ipconfig_eth4",
    "ipconfig_eth5",
    # "ipconfig_eth6",
    # "ipconfig_eth7",
    ]
}

variable "private_ip_addresses1" {
  default = [
    "172.10.10.10",
    "172.10.11.11",
    "172.10.12.12",
    "172.10.13.13",
    ]
}

variable "private_ip_addresses2" {
  default = [
    "172.10.10.20",
    "172.10.11.21",
    # "172.10.12.202",
    # "172.10.13.203",
    ]
}

## Linux Virtual Machine
variable "vm_name1" {
  default = "myVM1"
}
variable "vm_name2" {
  default = "myVM2"
}

variable "vm_size1" {
  default = "Standard_D3_v2"
}

variable "vm_adminuser1" {
  default = "adminuser"
}

variable "vm_publisher1" {
  default = "RedHat"
}

variable "vm_offer1" {
  default = "RHEL"
}

variable "vm_sku1" {
  default = "9_2"
}

variable "vm_version1" {
  default = "latest"
}

## Azure Bastion
module "subnet_bastion" {
    source                    = "./../modules/subnet"
    rg_name                   = module.cluster1-rg1.terraform-rg-name
    vnet_name                 = module.cluster1-vnet1.terraform-vnet-name
    subnet_names              = "${var.subnet_bastion_names}"
    subnet_address_prefixes   = "${var.subnet_bastion_address_prefixes}"
}

resource "azurerm_public_ip" "bastion_pub_ip" {
  name                = "bastion_pub_ip"
  location            = module.cluster1-rg1.terraform-rg-location
  resource_group_name = module.cluster1-rg1.terraform-rg-name
  allocation_method   = "Static"
  sku                 = "Standard"
}

resource "azurerm_bastion_host" "azurerm_bastion_host" {
  name                = "azurerm_bastion_host"
  location            = module.cluster1-rg1.terraform-rg-location
  resource_group_name = module.cluster1-rg1.terraform-rg-name

  ip_configuration {
    name                 = "configuration"
    subnet_id            = module.subnet_bastion.terraform-subnet-ids[0]
    public_ip_address_id = azurerm_public_ip.bastion_pub_ip.id
  }
}
variable "subnet_bastion_names" {
  default = [
    "AzureBastionSubnet",
    ]
}
variable "subnet_bastion_address_prefixes" {
  default = [
    "172.10.20.0/26",
    ]
}