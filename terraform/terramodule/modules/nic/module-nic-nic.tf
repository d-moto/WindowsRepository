resource "azurerm_network_interface" "terraform-nic" {
  name                = "${var.network_interface_name}"
  location            = "${var.rg_location}"
  resource_group_name = "${var.rg_name}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Static"
    private_ip_address            = "${var.private_ip_address}"
  }
}