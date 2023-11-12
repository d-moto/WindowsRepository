module "nic1" {
    source                  = "./modules/nic"
    network_interface_name = "${var.network_interface_name1}"
    # rg_name                 = "${var.rg_name1}"
    # rg_location             = "${var.rg_location}"
    rg_name                 = module.rg1.terraform-rg-name
    rg_location             = module.rg1.terraform-rg-location
    private_ip_address      = "${var.private_ip_address1}"
    subnet_id               = module.subnet1.terraform-subnet_id
}