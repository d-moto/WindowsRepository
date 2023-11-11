module "rg1" {
  source      = "./modules/rg"
  rg-name     = "myRG1"
  rg-location = "japaneast"
}

module "rg2" {
  source = "./modules/rg"
  rg-name = "myRG2"
  rg-location = "japaneast"
}

