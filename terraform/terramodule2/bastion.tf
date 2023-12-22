##########################################################################################
## Azure bastion
##########################################################################################
resource "azurerm_public_ip" "pubip" {
  name                = "pubip"
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  #allocation_method   = "Dynamic"
  allocation_method   = "Static"
  sku                 = "Standard"
}

resource "azurerm_bastion_host" "bashost" {
  name                = "bashost"
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.location
  
  file_copy_enabled   = true
  sku                 = "Standard"
  tunneling_enabled   = true
  

  ip_configuration {
    name                 = "configuration"
    subnet_id            = module.subnets_bastion.subnet_ids[0]
    public_ip_address_id = azurerm_public_ip.pubip.id
  }
}