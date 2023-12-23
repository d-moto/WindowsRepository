resource "azurerm_network_security_group" "nsg-adm" {
  name                = "nsg-adm"
  location            = module.resource_group.location
  resource_group_name = module.resource_group.resource_group_name

  ## INBOUNT
  security_rule {
    name                       = "allow_ssh"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  security_rule {
    name                         = "allow_between_vm_in"
    priority                     = 101
    direction                    = "Inbound"
    access                       = "Allow"
    protocol                     = "Tcp"
    source_port_range            = "*"
    destination_port_range       = "*"
    source_address_prefixes      = [var.private_ip_addresses[0]]
    destination_address_prefixes = [var.private_ip_addresses[4]]
  }

  security_rule {
    name                         = "allow_http"
    priority                     = 103
    direction                    = "Inbound"
    access                       = "Allow"
    protocol                     = "Tcp"
    source_port_range            = "*"
    destination_port_range       = "61011"
    source_address_prefix       = "*"
    destination_address_prefixes = [
      var.private_ip_addresses[0],
      var.private_ip_addresses[4]
    ]
  }

  ## OUTBOUND
  security_rule {
    name                         = "allow_between_vm_out"
    priority                     = 102
    direction                    = "Outbound"
    access                       = "Allow"
    protocol                     = "Tcp"
    source_port_range            = "*"
    destination_port_range       = "*"
    source_address_prefixes      = [var.private_ip_addresses[4]]
    destination_address_prefixes = [var.private_ip_addresses[0]]
  }
}

resource "azurerm_subnet_network_security_group_association" "nsg_association" {
  subnet_id                 = module.subnets_node.subnet_ids[0]
  network_security_group_id = azurerm_network_security_group.nsg-adm.id
}

# variable "nsg_names" {
#   description = "The name of the network security group"
# }

# variable "resource_group_name" {
#   description = "The name of the resource group"
# }

# variable "location" {
#   description = "The Azure Region in which to create the network security group."
# }
