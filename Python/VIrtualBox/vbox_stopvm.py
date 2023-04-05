import subprocess

# Variable
vm_name1 = "alma9_node1"
cmd = 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe controlvm "{}" poweroff'.format(vm_name1)

# CommandLine
print("execute following command : " + cmd)

# execute command
subprocess.run(cmd)