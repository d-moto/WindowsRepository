module "vnet1" {
    source                  = "./modules/vnet"
    #rg_name                 = "${var.rg_name1}"
    rg_name                 = module.rg1.terraform-rg-name
    #rg_location             = "${var.rg_location}"
    rg_location             = module.rg1.terraform-rg-location
    vnet_name               = "${var.vnet_name1}"
    vnet_address_space      = "${var.vnet_address_space1}"
}