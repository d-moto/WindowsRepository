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
    description = "The Azure Region in which all resources in this should be created."
}

## define output
output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

output "location" {
  value = azurerm_resource_group.rg.location
}
