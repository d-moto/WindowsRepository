# output "terraform-nic-eth0_id" {
#   value = azurerm_network_interface.terraform-nic-eth0.id
# }

# output "terraform-nic-eth1_id" {
#   value = azurerm_network_interface.terraform-nic-eth1.id
# }

# output "terraform-nic-eth2_id" {
#   value = azurerm_network_interface.terraform-nic-eth2.id
# }

# output "terraform-nic-eth3_id" {
#   value = azurerm_network_interface.terraform-nic-eth3.id
# }

output "terraform-nic-ids" {
  value = [for s in azurerm_network_interface.terraform-nics : s.id]
}