module "vnet1" {
    source                  = "./modules/vnet"
    rg_name                 = "${var.rg_name1}"
    rg_location             = "${var.rg_location}"
    vnet_name               = "${var.vnet_name1}"
    vnet_address_space      = "${var.vnet_address_space1}"
    subnet_name             = "${var.subnet_name1}"
    subnet_address_prefixes = "${var.subnet_address_prefixes1}"
    network_interface_name  = "${var.network_interface_name1}"
    private_ip_address      = "${var.private_ip_address1}"
}