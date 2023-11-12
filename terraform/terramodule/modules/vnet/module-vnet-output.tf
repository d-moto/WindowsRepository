output "terraform-vnet_id" {
  value = azurerm_virtual_network.terraform-vnet.id
}

output "terraform-vnet-name" {
  value = azurerm_virtual_network.terraform-vnet.name
}

output "terraform-vnet-address-space" {
  value = azurerm_virtual_network.terraform-vnet.address_space
}

##mainの方で、この戻り値を使用するようにする。