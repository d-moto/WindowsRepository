## define RG
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

## define variable
variable "resource_group_name" {
    description = "The name of the resource group"
}

variable "location" {
    desctiption = "The Azure Region in which all resources in this should be created.
}