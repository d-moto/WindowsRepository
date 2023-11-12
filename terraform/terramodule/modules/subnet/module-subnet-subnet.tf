## Subnet
resource "azurerm_subnet" "terraform-subnet_id_eth0" {
  name                 = "${var.subnet_name_eth0}"
  resource_group_name  = "${var.rg_name}"
  virtual_network_name = "${var.vnet_name}"
  address_prefixes     = ["${var.subnet_address_prefixes_eth0}"]
}

resource "azurerm_subnet" "terraform-subnet_id_eth1" {
  name                 = "${var.subnet_name_eth1}"
  resource_group_name  = "${var.rg_name}"
  virtual_network_name = "${var.vnet_name}"
  address_prefixes     = ["${var.subnet_address_prefixes_eth1}"]
}

resource "azurerm_subnet" "terraform-subnet_id_eth2" {
  name                 = "${var.subnet_name_eth2}"
  resource_group_name  = "${var.rg_name}"
  virtual_network_name = "${var.vnet_name}"
  address_prefixes     = ["${var.subnet_address_prefixes_eth2}"]
}

resource "azurerm_subnet" "terraform-subnet_id_eth3" {
  name                 = "${var.subnet_name_eth3}"
  resource_group_name  = "${var.rg_name}"
  virtual_network_name = "${var.vnet_name}"
  address_prefixes     = ["${var.subnet_address_prefixes_eth3}"]
}