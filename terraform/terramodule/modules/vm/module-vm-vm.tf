resource "azurerm_linux_virtual_machine" "terraform-linux-virtual-machine" {
  #count = length(var.vm_network_interface_ids)
  name                = "${var.vm_name}"
  resource_group_name = "${var.rg_name}"
  location            = "${var.rg_location}"
  size                = "${var.vm_size}"
  admin_username      = "${var.vm_adminuser}"
  # network_interface_ids = [
  #   # var.network_interface_eth0_id,
  #   # var.network_interface_eth1_id,
  #   # var.network_interface_eth2_id,
  #   # var.network_interface_eth3_id,
  # ]
  network_interface_ids = var.vm_network_interface_ids

  admin_ssh_key {
    username   = "${var.vm_adminuser}"
    public_key = file("~/.ssh/id_rsa_azure_nopass.pub")
  }
    os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "${var.vm_publisher}"
    offer     = "${var.vm_offer}"
    sku       = "${var.vm_sku}"
    version   = "${var.vm_version}"
  }
}