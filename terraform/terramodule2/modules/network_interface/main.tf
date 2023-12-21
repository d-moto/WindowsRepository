## define NETWORK INTERFACE
resource "azurerm_network_interface" "nic" {
  count               = sum(var.nic_counts)
  name                = "${var.nic_name}"
  location            = var.location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "ipconfig${var.nic_name}"
    subnet_id                     = var.subnet_ids[count.index % length(var.subnet_ids)]
    private_ip_address_allocation = "Static"
    private_ip_address            = var.private_ip_addresses[count.index]
  }
}

## define variable
variable "nic_name" {
  description = "Base name for the network interfaces"
}

variable "subnet_ids" {
  description = "List of subnet IDs to attach to the network interfaces"
  type        = list(string)
}

variable "resource_group_name" {
  description = "Name of the resource group"
}

variable "location" {
  description = "Azure region for the network interfaces"
}

variable "private_ip_addresses" {
  description = "List of private IP addresses for each network interface"
  type        = list(string)
}

## define output
output "network_interface_ids" {
  value = azurerm_network_interface.nic.*.id
}

