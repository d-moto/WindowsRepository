
resource "azurerm_virtual_network" "terraform-test-vnet" {
  name                = var.vnet-name
  address_space       = ["10.0.0.0/16"]
  location            = var.rg-location
  resource_group_name = var.rg-name
}
resource "azurerm_subnet" "terraform-test-subnet" {
  name                 = var.subnet-name
  resource_group_name  = var.rg-name
  virtual_network_name = azurerm_virtual_network.terraform-test-vnet.name
  address_prefixes     = ["10.0.2.0/24"]
}