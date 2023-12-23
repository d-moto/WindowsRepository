# resource "azurerm_network_interface" "terraform-nic-eth0" {
#   name                = "${var.network_interface_name_eth0}"
#   location            = "${var.rg_location}"
#   resource_group_name = "${var.rg_name}"

#   ip_configuration {
#     name                          = "${var.ip_config_eth0}"
#     subnet_id                     = "${var.subnet_id_eth0}"
#     private_ip_address_allocation = "Static"
#     private_ip_address            = "${var.private_ip_address_eth0}"
#   }
# }

# resource "azurerm_network_interface" "terraform-nic-eth1" {
#   name                = "${var.network_interface_name_eth1}"
#   location            = "${var.rg_location}"
#   resource_group_name = "${var.rg_name}"

#   ip_configuration {
#     name                          = "${var.ip_config_eth1}"
#     subnet_id                     = "${var.subnet_id_eth1}"
#     private_ip_address_allocation = "Static"
#     private_ip_address            = "${var.private_ip_address_eth1}"
#   }
# }

# resource "azurerm_network_interface" "terraform-nic-eth2" {
#   name                = "${var.network_interface_name_eth2}"
#   location            = "${var.rg_location}"
#   resource_group_name = "${var.rg_name}"

#   ip_configuration {
#     name                          = "${var.ip_config_eth2}"
#     subnet_id                     = "${var.subnet_id_eth2}"
#     private_ip_address_allocation = "Static"
#     private_ip_address            = "${var.private_ip_address_eth2}"
#   }
# }

# resource "azurerm_network_interface" "terraform-nic-eth3" {
#   name                = "${var.network_interface_name_eth3}"
#   location            = "${var.rg_location}"
#   resource_group_name = "${var.rg_name}"

#   ip_configuration {
#     name                          = "${var.ip_config_eth3}"
#     subnet_id                     = "${var.subnet_id_eth3}"
#     private_ip_address_allocation = "Static"
#     private_ip_address            = "${var.private_ip_address_eth3}"
#   }
# }

resource "azurerm_network_interface" "terraform-nics" {
  count               = length(var.network_interface_names)
  name                = var.network_interface_names[count.index]
  location            = "${var.rg_location}"
  resource_group_name = "${var.rg_name}"

  ip_configuration {
    name                          = var.ip_config_names[count.index]
    subnet_id                     = var.subnet_ids[count.index]
    private_ip_address_allocation = "Static"
    private_ip_address            = var.private_ip_addresses[count.index]
  }
}