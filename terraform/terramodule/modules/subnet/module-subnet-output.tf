output "terraform-subnet_id" {
  value = azurerm_subnet.terraform-subnet.id
}

output "terraform-subnet-name" {
  value = azurerm_subnet.terraform-subnet.name
}

output "terraform-subnet-address-prefixes" {
  value = azurerm_subnet.terraform-subnet.address_prefixes
}