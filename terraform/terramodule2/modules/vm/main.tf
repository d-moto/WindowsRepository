## define VM
resource "azurerm_linux_virtual_machine" "vm" {
  count               = var.instance_count
  name                = var.vm_name[count.index]
  resource_group_name = var.resource_group_name
  location            = var.location
  size                = var.vm_size[count.index]#"Standard_D3_v2"
  admin_username      = "adminuser"
  network_interface_ids = var.network_interface_ids[count.index]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "RedHat"
    offer     = "RHEL"
    sku       = "9_0"
    version   = "latest"
  }

    admin_ssh_key {
    username   = "adminuser"
    public_key = file(var.ssh_public_key)
  }

  disable_password_authentication = true
}

## define variable
variable "instance_count" {
  description = "Number of instances to create"
  type        = number
}

variable "network_interface_ids" {
  description = "Nested list of network interface IDs for each VM"
  type        = list(list(string))
}

variable "vm_name" {
  description = "Base name of the virtual machine"
  type = list(string)
}

variable "vm_size" {
  description = "VM size"
  type = list(string)
}

variable "resource_group_name" {
  description = "Name of the resource group"
}

variable "location" {
  description = "Azure region for the virtual machine"
}

variable "ssh_public_key" {
  description = "Path to the public key to be used for SSH access to the VM"
}