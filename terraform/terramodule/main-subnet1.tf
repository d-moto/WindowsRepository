module "subnet1" {
    source                  = "./modules/subnet"
    # rg_name                 = "${var.rg_name1}"
    # vnet_name               = "${var.vnet_name1}"
    # subnet_name             = "${var.subnet_name1}"
    # subnet_address_prefixes = "${var.subnet_address_prefixes1}"
    rg_name                   = module.rg1.terraform-rg-name
    vnet_name                 = module.vnet1.terraform-vnet-name
    subnet_name             = "${var.subnet_name1}"
    subnet_address_prefixes = "${var.subnet_address_prefixes1}"
}
