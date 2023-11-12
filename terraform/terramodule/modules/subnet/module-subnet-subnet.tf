## Subnet
resource "azurerm_subnet" "terraform-subnet" {
  name                 = "${var.subnet_name}"
  resource_group_name  = "${var.rg_name}"
  virtual_network_name = "${var.vnet_name}"
  address_prefixes     = ["${var.subnet_address_prefixes}"]
}