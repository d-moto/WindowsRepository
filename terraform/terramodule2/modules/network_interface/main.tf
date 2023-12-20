## define NETWORK INTERFACE
resource "azurerm_network_interface" "nic" {
  count               = length(var.subnet_ids)
  name                = "${var.nic_name}-${count.index + 1}"
  location            = var.location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "ipconfig${count.index + 1}"
    subnet_id                     = var.subnet_ids[count.index]
    private_ip_address_allocation = "Dynamic"
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

## define output
output "network_interface_ids" {
  value = azurerm_network_interface.nic.*.id
}

