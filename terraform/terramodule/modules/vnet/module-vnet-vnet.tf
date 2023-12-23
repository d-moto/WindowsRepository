## Virtual Network
resource "azurerm_virtual_network" "terraform-vnet" {
  name                = "${var.vnet_name}"
  address_space       = ["${var.vnet_address_space}"]
  location            = var.rg_location
  resource_group_name = var.rg_name
}

# ## Network Interface
# resource "azurerm_network_interface" "terraform-nif" {
#   name                = "${var.network_interface_name}"
#   location            = var.rg_location
#   resource_group_name = var.rg_name
#   ip_configuration {
#     name                          = "internal"
#     subnet_id                     = azurerm_subnet.terraform-subnet.id
#     private_ip_address_allocation = "Static"
#     private_ip_address            = "${var.private_ip_address}"
#   }
# }