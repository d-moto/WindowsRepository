resource "azurerm_resource_group" "terraform-rg" {
    name     = var.rg-name
    location = var.rg-location  
}