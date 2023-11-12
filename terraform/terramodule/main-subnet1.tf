module "subnet1" {
    source                  = "./modules/subnet"
    rg_name                   = module.rg1.terraform-rg-name
    vnet_name                 = module.vnet1.terraform-vnet-name
    subnet_name_eth0             = "${var.subnet_name1_eth0}"
    subnet_name_eth1             = "${var.subnet_name1_eth1}"
    subnet_name_eth2             = "${var.subnet_name1_eth2}"
    subnet_name_eth3             = "${var.subnet_name1_eth3}"
    subnet_address_prefixes_eth0 = "${var.subnet_address_prefixes1_eth0}"
    subnet_address_prefixes_eth1 = "${var.subnet_address_prefixes1_eth1}"
    subnet_address_prefixes_eth2 = "${var.subnet_address_prefixes1_eth2}"
    subnet_address_prefixes_eth3 = "${var.subnet_address_prefixes1_eth3}"
}
