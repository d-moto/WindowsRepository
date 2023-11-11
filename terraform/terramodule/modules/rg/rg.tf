resource "azurerm_resource_group" "terraform-test-rg" {
    name     = var.rg-name
    location = var.rg-location  
}