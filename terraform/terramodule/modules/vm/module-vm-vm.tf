resource "azurerm_linux_virtual_machine" "terraform-linux-virtual-machine" {
  name                = "${var.vm_name}"
  resource_group_name = "${var.rg_name}"
  location            = "${var.rg_location}"
  size                = "${var.vm_size}"
  admin_username      = "${var.vm_adminuser}"
  network_interface_ids = [
    var.network_interface_id,
  ]

  admin_ssh_key {
    username   = "${var.vm_adminuser}"
    public_key = file("~/.ssh/id_rsa.pub")
  }
    os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }
}