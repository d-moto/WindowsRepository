module "nic1" {
    source                  = "./modules/nic"
    ## Interface Name
    # network_interface_name_eth0 = "${var.network_interface_name1_eth0}"
    # network_interface_name_eth1 = "${var.network_interface_name1_eth1}"
    # network_interface_name_eth2 = "${var.network_interface_name1_eth2}"
    # network_interface_name_eth3 = "${var.network_interface_name1_eth3}"
    network_interface_names = "${var.network_interface_names1}"
    ## IP Config Name
    # ip_config_eth0 = "${var.ip_config1_eth0}"
    # ip_config_eth1 = "${var.ip_config1_eth1}"
    # ip_config_eth2 = "${var.ip_config1_eth2}"
    # ip_config_eth3 = "${var.ip_config1_eth3}"
    ip_config_names = "${var.ip_config_names1}"
    ## RG name and location
    rg_name                 = module.rg1.terraform-rg-name
    rg_location             = module.rg1.terraform-rg-location
    ## Private IP Address
    # private_ip_address_eth0 = "${var.private_ip_address1_eth0}"
    # private_ip_address_eth1 = "${var.private_ip_address1_eth1}"
    # private_ip_address_eth2 = "${var.private_ip_address1_eth2}"
    # private_ip_address_eth3 = "${var.private_ip_address1_eth3}"
    private_ip_addresses = "${var.private_ip_addresses1}"
    ## Subnet Id
    # subnet_id_eth0               = module.subnet1.terraform-subnet_id_eth0
    # subnet_id_eth1               = module.subnet1.terraform-subnet_id_eth1
    # subnet_id_eth2               = module.subnet1.terraform-subnet_id_eth2
    # subnet_id_eth3               = module.subnet1.terraform-subnet_id_eth3
    subnet_ids = module.subnet1.terraform-subnet-ids
}