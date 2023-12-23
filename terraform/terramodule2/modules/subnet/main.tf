##########################################################################################
## Define SUBNET
##########################################################################################
resource "azurerm_subnet" "subnet" {
  count                = length(var.subnet_names)
  name                 = var.subnet_names[count.index]
  resource_group_name  = var.resource_group_name
  virtual_network_name = var.vnet_name
  address_prefixes     = [var.subnet_prefixes[count.index]]
}

# resource "azurerm_subnet_network_security_group_association" "nsg_association" {
#   count                     = length(var.subnet_ids)
#   subnet_id                 = var.subnet_ids[count.index]
#   network_security_group_id = var.nsg_ids[count.index]
# }

##########################################################################################
## Define varialbe
##########################################################################################
variable "subnet_names" {
  description = "The names of the subnets"
  type        = list(string)
}

variable "subnet_prefixes" {
  description = "The address prefixes for the subnets"
  type        = list(string)
}

variable "resource_group_name" {
  description = "The name of the resource group"
}

variable "vnet_name" {
  description = "The name of the virtual network"
}

# variable "subnet_ids" {
#   description = "List of subnet IDs to attach the NSG"
#   type        = list(string)
# }

# variable "nsg_ids" {
#   description = "The ID of the network security group to associate"
#   type        = list(string)
# }

##########################################################################################
## Define output
##########################################################################################
output "subnet_ids" {
  value = azurerm_subnet.subnet.*.id
}

