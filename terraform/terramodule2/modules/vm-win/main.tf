##########################################################################################
## Define VM
##########################################################################################
resource "azurerm_windows_virtual_machine" "vm" {
  count                           = var.instance_count
  name                            = var.vm_name[count.index]
  resource_group_name             = var.resource_group_name
  location                        = var.location
  size                            = var.vm_size[count.index] #"Standard_D3_v2"
  admin_username                  = "adminuser"
  admin_password                  = "adminuser00!"
  network_interface_ids           = var.network_interface_ids[count.index]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "microsoftwindowsdesktop"#"MicrosoftWindowsServer"
    offer     = "windows-11"#"WindowsServer"
    sku       = "win11-21h2-pro"#"2016-Datacenter"
    version   = "latest"
  }

  #user_data = (base64encode(var.user_data))
  #user_data = (base64encode(replace(var.user_data, "systemctl_list-unit-files.txt", "systemctl_list-unit-files_${each.value}.txt")))
  # user_data = (
  #   base64encode(
  #     #replace(var.user_data, ".txt", "${var.vm_name[count.index]}.txt")
  #     <<-EOT
  #     #!/bin/bash
  #     systemctl list-unit-files > /home/adminuser/systemctl_list-unit-files-${var.vm_name[count.index]}.txt
  #     yum -y install policycoreutils-python-utils
  #     yum -y install traceroute httpd
  #     timedatectl set-timezone Asia/Tokyo
  #     curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash
  #     EXTERNAL_URL="http://172.30.10.10:61011" dnf install -y gitlab-ee
  #     cp -p /etc/gitlab/instial_root_password /home/adminuser/
  #     grep 'EXTERNAL_URL' /etc/gitlab/gitlab.rb > /home/adminuser/gitlab-url
  #     gitlab-ctl reconfigure
  #     EOT
  #   )
  # )
}

##########################################################################################
## Define variable
##########################################################################################
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
  type        = list(string)
}

variable "vm_size" {
  description = "VM size"
  type        = list(string)
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

# variable "user_data" {
#   description = "User date script"
# }
