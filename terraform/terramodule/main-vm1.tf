module "vm1" {
  source               = "./modules/vm"
  rg_name              = module.rg1.terraform-rg-name
  rg_location          = module.rg1.terraform-rg-location
  vm_name              = "${var.vm_name1}"
  vm_size              = "${var.vm_size1}"
  vm_adminuser         = "${var.vm_adminuser1}"
  network_interface_id = module.nic1.terraform-nic_id
}