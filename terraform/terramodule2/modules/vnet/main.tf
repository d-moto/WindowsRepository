##########################################################################################
## Define VNET
##########################################################################################
resource "azurerm_virtual_network" "vnet" {
  name                = var.vnet_name
  address_space       = var.address_space
  location            = var.location
  resource_group_name = var.resource_group_name
}

##########################################################################################
## Define variable
##########################################################################################
variable "vnet_name" {
  description = "The name of the virtual network"
}

variable "address_space" {
  description = "The address space that is used the virtual network"
}

variable "location" {
  description = "The Azure Region in which to create the virtual network."
}

variable "resource_group_name" {
  description = "The name of the resource group in which to create the virtual network."
}

##########################################################################################
## Define output
##########################################################################################
output "vnet_name" {
  value = azurerm_virtual_network.vnet.name
}

