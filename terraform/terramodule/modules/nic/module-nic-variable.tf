## Resource Group
variable "rg_name" {}
variable "rg_location" {}

## Virtual Network Name
# variable "ip_config_eth0" {}
# variable "ip_config_eth1" {}
# variable "ip_config_eth2" {}
# variable "ip_config_eth3" {}

# variable "network_interface_name_eth0" {}
# variable "network_interface_name_eth1" {}
# variable "network_interface_name_eth2" {}
# variable "network_interface_name_eth3" {}

# variable "private_ip_address_eth0" {}
# variable "private_ip_address_eth1" {}
# variable "private_ip_address_eth2" {}
# variable "private_ip_address_eth3" {}

# variable "subnet_id_eth0" {}
# variable "subnet_id_eth1" {}
# variable "subnet_id_eth2" {}
# variable "subnet_id_eth3" {}

variable "network_interface_names" {
  description = "List of network interface names"
  type = list(string)
}

variable "ip_config_names" {
  description = "List of ip configuration names"
  type = list(string)
}

variable "subnet_ids" {
  description = "List of subnetids"
  type = list(string)
}

variable "private_ip_addresses" {
  description = "List of ip addresses"
  type = list(string)
}