## Resource Group Name
variable "rg_name1" {
  default = "myRG1"
}

## Resouce Group Location 
variable "rg_location" {
  default = "japaneast"
}

## Vnet
variable "vnet_name1" {
  default = "myVnet1"
}
variable "vnet_address_space1" {
  default = "172.10.0.0/16"
}

## Subnet
# variable "subnet_name1_eth0" {
#   default = "mySubnet1_eth0"
# }

# variable "subnet_name1_eth1" {
#   default = "mySubnet1_eth1"
# }

# variable "subnet_name1_eth2" {
#   default = "mySubnet1_eth2"
# }

# variable "subnet_name1_eth3" {
#   default = "mySubnet1_eth3"
# }

# variable "subnet_address_prefixes1_eth0" {
#   default = "172.10.10.0/24"
# }

# variable "subnet_address_prefixes1_eth1" {
#   default = "172.10.11.0/24"
# }

# variable "subnet_address_prefixes1_eth2" {
#   default = "172.10.12.0/24"
# }

# variable "subnet_address_prefixes1_eth3" {
#   default = "172.10.13.0/24"
# }

variable "subnet_names1" {
  default = [
    "mySubnet1_eth0",
    "mySubnet1_eth1",
    "mySubnet1_eth2",
    "mySubnet1_eth3"
    ]
}

variable "subnet_address_prefixes1" {
  default = [
    "172.10.10.0/24",
    "172.10.11.0/24",
    "172.10.12.0/24",
    "172.10.13.0/24",
    ]
}

## Network Interface
# variable "network_interface_name1_eth0" {
#   default = "eth0"
# }
# variable "network_interface_name1_eth1" {
#   default = "eth1"
# }
# variable "network_interface_name1_eth2" {
#   default = "eth2"
# }
# variable "network_interface_name1_eth3" {
#   default = "eth3"
# }

variable "network_interface_names1" {
  default = [
    "eth0",
    "eth1",
    "eth2",
    "eth3",
    ]
}

## IP Config Name
# variable "ip_config1_eth0" {
#   default = "ipconfig_eth0"
# }
# variable "ip_config1_eth1" {
#   default = "ipconfig_eth1"
# }
# variable "ip_config1_eth2" {
#   default = "ipconfig_eth2"
# }
# variable "ip_config1_eth3" {
#   default = "ipconfig_eth3"
# }

variable "ip_config_names1" {
  default = [
    "ipconfig_eth0",
    "ipconfig_eth1",
    "ipconfig_eth2",
    "ipconfig_eth3",
    ]
}

# variable "private_ip_address1_eth0" {
#   default = "172.10.10.100"
# }
# variable "private_ip_address1_eth1" {
#   default = "172.10.11.101"
# }
# variable "private_ip_address1_eth2" {
#   default = "172.10.12.102"
# }
# variable "private_ip_address1_eth3" {
#   default = "172.10.13.103"
# }

variable "private_ip_addresses1" {
  default = [
    "172.10.10.100",
    "172.10.11.101",
    "172.10.12.102",
    "172.10.13.103",
    ]
}


## Linux Virtual Machine
variable "vm_name1" {
  default = "myVM"
}

variable "vm_size1" {
  default = "Standard_D3_v2"
}

variable "vm_adminuser1" {
  default = "adminuser"
}

variable "vm_publisher1" {
  default = "RedHat"
}

variable "vm_offer1" {
  default = "RHEL"
}

variable "vm_sku1" {
  default = "9_2"
}

variable "vm_version1" {
  default = "latest"
}