# resource "azurerm_network_security_group" "nsg" {
#   count               = length(var.nsg_names)
#   name                = var.nsg_names[count.index]
#   location            = var.location
#   resource_group_name = var.resource_group_name
# }

# resource "azurerm_network_security_rule" "allow_ssh" {
#   name                        = "allow_ssh"
#   priority                    = 100
#   direction                   = "Inbound"
#   access                      = "Allow"
#   protocol                    = "Tcp"
#   source_port_range           = "*"
#   destination_port_range      = "22"
#   source_address_prefix       = "*"
#   destination_address_prefix  = "*"
#   resource_group_name         = var.resource_group_name
#   network_security_group_name = azurerm_network_security_group.nsg[0].name
# }

# resource "azurerm_network_security_rule" "allow_vm_communication" {
#   count                       = length(var.nsg_names)
#   name                        = "allow_vm_comm_${count.index}"
#   priority                    = 110
#   direction                   = "Inbound"
#   access                      = "Allow"
#   protocol                    = "Tcp"
#   source_port_range           = "*"
#   destination_port_range      = "*"
#   source_address_prefix       = "172.30.${count.index * 10 + 10}.10"
#   destination_address_prefix  = "172.30.${count.index * 10 + 50}.50"
#   resource_group_name         = var.resource_group_name
#   network_security_group_name = azurerm_network_security_group.nsg[count.index].name
# }

# variable "nsg_names" {
#   description = "The name of the network security group"
# }

# variable "resource_group_name" {
#   description = "The name of the resource group"
# }

# variable "location" {
#   description = "The Azure Region in which to create the network security group."
# }

# ## define output
# output "nsg_ids" {
#     value = azurerm_network_security_group.nsg.*.id
# }