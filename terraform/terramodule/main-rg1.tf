module "rg1" {
  source      = "./modules/rg"
  rg_name     = "${var.rg_name1}"
  rg_location = "${var.rg_location}"
}

# module "rg2" {
#   source      = "./modules/rg"
#   rg_name     = "myRG2"
#   rg_location = "japaneast"
# }

