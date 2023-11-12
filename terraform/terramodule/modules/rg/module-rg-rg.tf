resource "azurerm_resource_group" "terraform-rg" {
    name     = var.rg_name
    location = var.rg_location  
}