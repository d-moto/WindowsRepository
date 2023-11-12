output "terraform-test-rg-name" {
    value = azurerm_resource_group.terraform-rg.name
}

output "terraform-test-rg-location" {
    value = azurerm_resource_group.terraform-rg.location  
}