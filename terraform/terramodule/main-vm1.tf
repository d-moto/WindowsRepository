module "vm1" {
  source               = "./modules/vm"
  rg_name              = module.rg1.terraform-rg-name
  rg_location          = module.rg1.terraform-rg-location
  vm_name              = "${var.vm_name1}"
  vm_size              = "${var.vm_size1}"
  vm_publisher         = "${var.vm_publisher1}"
  vm_offer             = "${var.vm_offer1}"
  vm_sku               = "${var.vm_sku1}"
  vm_version           = "${var.vm_version1}"
  vm_adminuser         = "${var.vm_adminuser1}"
  # network_interface_eth0_id = module.nic1.terraform-nic-eth0_id
  # network_interface_eth1_id = module.nic1.terraform-nic-eth1_id
  # network_interface_eth2_id = module.nic1.terraform-nic-eth2_id
  # network_interface_eth3_id = module.nic1.terraform-nic-eth3_id
  vm_network_interface_ids = module.nic1.terraform-nic-ids
}