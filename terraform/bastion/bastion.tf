terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.85.0"
    }
  }
}

provider "azurerm" {
  # Configuration options
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "rg"
  location = "japaneast"
}

resource "azurerm_virtual_network" "vn" {
  name                = "vn"
  address_space       = ["172.30.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_subnet" "sbn" {
  name                 = "AzureBastionSubnet"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vn.name
  address_prefixes     = ["172.30.1.0/24"]
}

## for bastion
resource "azurerm_public_ip" "pubip" {
  name                = "pubip"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  #allocation_method   = "Dynamic"
  allocation_method   = "Static"
  sku                 = "Standard"
}

resource "azurerm_bastion_host" "bashost" {
  name                = "bashost"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  
  file_copy_enabled   = true
  sku                 = "Standard"
  tunneling_enabled   = true
  

  ip_configuration {
    name                 = "configuration"
    subnet_id            = azurerm_subnet.sbn.id
    public_ip_address_id = azurerm_public_ip.pubip.id
  }
}
