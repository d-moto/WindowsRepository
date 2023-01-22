# Virtual Boxを使用していた際のメモ

## VirtualBoxをコマンドで操作したい場合
1. cmdを開く。
2. VBをインストールしたディレクトリに移動する。  
```shell
PS C:\Users\axppe> cd 'C:\Program Files\Oracle\VirtualBox\'
PS C:\Program Files\Oracle\VirtualBox>
```
3. コマンドを打ち込む。   
```shell
C:\Program Files\Oracle\VirtualBox>VBoxManage.exe startvm AlmaLinux9 --type headless

C:\Program Files\Oracle\VirtualBox>VBoxManage.exe list vms
"AlmaLinux9" {6ebc2119-de35-467b-a695-047eb2e424f5}

C:\Program Files\Oracle\VirtualBox>VBoxManage.exe list runningvms

C:\Program Files\Oracle\VirtualBox>
C:\Program Files\Oracle\VirtualBox>
C:\Program Files\Oracle\VirtualBox>VBoxManage.exe startvm "AlmaLinux9" --type headless
Waiting for VM "AlmaLinux9" to power on...
VM "AlmaLinux9" has been successfully started.

C:\Program Files\Oracle\VirtualBox>VBoxManage.exe list runningvms
"AlmaLinux9" {6ebc2119-de35-467b-a695-047eb2e424f5}

C:\Program Files\Oracle\VirtualBox>
C:\Program Files\Oracle\VirtualBox>VBoxManage.exe controlvm AlmaLinux9 poweroff
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%

C:\Program Files\Oracle\VirtualBox>VBoxManage.exe list runningvms

C:\Program Files\Oracle\VirtualBox>
```

## 参考
```
VirtualBoxをコマンドで操作する場合はVBoxManageというコマンドで操作を行います。
Windowsの場合、以下にあるため、パスを切りましょう。

パス
C:\Program Files\Oracle\VirtualBox
## 参照系コマンド一覧
説明	コマンド
全ての仮想マシン一覧の表示	VBoxManage list vms
起動中の仮想マシン一覧の表示	VBoxManage list runningvms
仮想マシンの詳細表示	VBoxManage showvminfo [UUID or VM名]
仮想マシンのスナップショット一覧表示	VBoxManage snapshot [UUID or VM名] list
指定したスナップショットの仮想マシン詳細表示	VBoxManage snapshot [UUID or VM名] showvminfo [スナップショット名]
操作系コマンド一覧
説明	コマンド
仮想マシンの起動（GUIあり）	VBoxManage startvm [UUID or VM名]
仮想マシンの起動（ボタン表示なし）	VBoxManage startvm [UUID or VM名] --type sdl
仮想マシンの起動（GUIなし）	VBoxManage startvm [UUID or VM名] --type headless
仮想マシンの起動（GUIなし変更可）	VBoxManage startvm [UUID or VM名] --type separate
仮想マシンの電源オフ	VBoxManage controlvm [UUID or VM名] poweroff
仮想マシンのACPIシャットダウン	VBoxManage controlvm [UUID or VM名] acpipowerbutton
仮想マシンの再起動	VBoxManage controlvm [UUID or VM名] reset
仮想マシンのサスペンド	VBoxManage controlvm [UUID or VM名] savestate
仮想マシンの一時停止	VBoxManage controlvm [UUID or VM名] pause
仮想マシンの再開	VBoxManage controlvm [UUID or VM名] resume
スナップショットの作成	VBoxManage snapshot [UUID or VM名] take [スナップショット名]
指定したスナップショットの削除	VBoxManage snapshot [UUID or VM名] delete [スナップショット名]
指定したスナップショット名の修正	VBoxManage snapshot [UUID or VM名] edit [スナップショット名] --name=[新しいスナップショット名]
直前のスナップショットへのリストア	VBoxManage snapshot [UUID or VM名] restorecurrent
指定したスナップショットへのリストア	VBoxManage snapshot [UUID or VM名] restore [スナップショット名]
ホストからゲストOSの操作	VBoxManage guestcontrol [UUID or VM名] run --exe "[コマンドフルパス]" --username [ゲストOSユーザ名] --password [ゲストOSパスワード]
```

## Linuxにrpmからvirtualboxをインストールする方法
```
[root@localhost63 alma1]# scp -i sshkeys/local63secret /var/tmp/VirtualBox-7.0-7.0.6_155176_el8-1.x86_64.rpm alma2@192.168.10.2:/home/alma2/
VirtualBox-7.0-7.0.6_155176_el8-1.x86_64.rpm                                                                                                 100%   93MB  32.7MB/s   00:02
[root@localhost63 alma1]#


[root@localhost66 alma2]# ls -l | grep Virtual
-rw-r--r-- 1 alma2 alma1 97952224  1月 22 15:02 VirtualBox-7.0-7.0.6_155176_el8-1.x86_64.rpm
[root@localhost66 alma2]#
[root@localhost66 alma2]# rpm -ihv VirtualBox-7.0-7.0.6_155176_el8-1.x86_64.rpm
警告: VirtualBox-7.0-7.0.6_155176_el8-1.x86_64.rpm: ヘッダー V4 DSA/SHA1 Signature、鍵 ID 98ab5139: NOKEY
エラー: 依存性の欠如:
        libGL.so.1()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5Core.so.5()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5Core.so.5(Qt_5)(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5Core.so.5(Qt_5.12)(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5DBus.so.5()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5DBus.so.5(Qt_5)(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5Gui.so.5()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5Gui.so.5(Qt_5)(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5Help.so.5()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5Help.so.5(Qt_5)(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5OpenGL.so.5()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5OpenGL.so.5(Qt_5)(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5PrintSupport.so.5()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5PrintSupport.so.5(Qt_5)(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5Widgets.so.5()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5Widgets.so.5(Qt_5)(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5X11Extras.so.5()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5X11Extras.so.5(Qt_5)(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5Xml.so.5()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libQt5Xml.so.5(Qt_5)(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libXcursor.so.1()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libXt.so.6()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libasound.so.2()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        libvpx.so.5()(64bit) は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
        vulkan-loader は VirtualBox-7.0-7.0.6_155176_el8-1.x86_64 に必要とされています
[root@localhost66 alma2]#
[root@localhost66 alma2]# yum install libGL libXt libvpx libXcursor vulkan-loader qt5-qtbase-* qt5-qttools-* qt5-qtx11extras* alsa-lib

[root@localhost66 alma2]# rpm -ihv VirtualBox-7.0-7.0.6_155176_el8-1.x86_64.rpm
警告: VirtualBox-7.0-7.0.6_155176_el8-1.x86_64.rpm: ヘッダー V4 DSA/SHA1 Signature、鍵 ID 98ab5139: NOKEY
Verifying...                          ################################# [100%]
準備しています...              ################################# [100%]
更新中 / インストール中...
   1:VirtualBox-7.0-7.0.6_155176_el8-1################################# [100%]

Creating group 'vboxusers'. VM users must be member of that group!

vboxdrv.sh: failed: Look at /var/log/vbox-setup.log to find out what went wrong.

There were problems setting up VirtualBox.  To re-start the set-up process, run
  /sbin/vboxconfig
as root.  If your system is using EFI Secure Boot you may need to sign the
kernel modules (vboxdrv, vboxnetflt, vboxnetadp, vboxpci) before you can load
them. Please see your Linux system's documentation for more information.
[root@localhost66 alma2]#
[root@localhost66 alma2]# /sbin/vboxconfig
vboxdrv.sh: Stopping VirtualBox services.
vboxdrv.sh: Starting VirtualBox services.
vboxdrv.sh: Building VirtualBox kernel modules.
vboxdrv.sh: failed: Look at /var/log/vbox-setup.log to find out what went wrong.

There were problems setting up VirtualBox.  To re-start the set-up process, run
  /sbin/vboxconfig
as root.  If your system is using EFI Secure Boot you may need to sign the
kernel modules (vboxdrv, vboxnetflt, vboxnetadp, vboxpci) before you can load
them. Please see your Linux system's documentation for more information.
[root@localhost66 alma2]#
[root@localhost66 alma2]# yum install elfutils-libelf-devel


[root@localhost66 alma2]# /sbin/vboxconfig
vboxdrv.sh: Stopping VirtualBox services.
vboxdrv.sh: Starting VirtualBox services.
vboxdrv.sh: Building VirtualBox kernel modules.
[root@localhost66 alma2]#

[root@localhost66 alma2]# mkdir VBoxHome
[root@localhost66 alma2]# cd VBoxHome/
[root@localhost66 VBoxHome]# pwd
/home/alma2/VBoxHome
[root@localhost66 VBoxHome]#

[root@localhost66 VBoxHome]# mkdir iso
[root@localhost66 VBoxHome]# mv ../AlmaLinux-9-latest-x86_64-dvd.iso iso/
[root@localhost66 VBoxHome]# mkdir rpms
[root@localhost66 VBoxHome]# mv ../VirtualBox-7.0-7.0.6_155176_el8-1.x86_64.rpm rpms/
[root@localhost66 VBoxHome]# ls -l
合計 0
drwxr-xr-x 2 root root 47  1月 22 15:31 iso
drwxr-xr-x 2 root root 58  1月 22 15:31 rpms
[root@localhost66 VBoxHome]#

[root@localhost66 VBoxHome]# mkdir vm
[root@localhost66 VBoxHome]# cd vm/
[root@localhost66 vm]# pwd
/home/alma2/VBoxHome/vm
[root@localhost66 vm]# vboxmanage createvm --name "rh9-node1" --register --basefolder $(pwd)
Virtual machine 'rh9-node1' is created and registered.
UUID: 253cc2ba-935b-482c-83d3-14bc4ed72c22
Settings file: '/home/alma2/VBoxHome/vm/rh9-node1/rh9-node1.vbox'
[root@localhost66 vm]#
[root@localhost66 vm]# vboxmanage createmedium --filename rh9-node1 disk -size 102400 --format vdi
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Medium created. UUID: 4973af85-5e20-43c2-b630-73084cc5191f
[root@localhost66 vm]#
[root@localhost66 vm]# vboxmanage list ostypes | grep RedHat8
ID:          RedHat8_64
[root@localhost66 vm]# vboxmanage modifyvm rh9-node1 --ostype RedHat9_64
[root@localhost66 vm]# vboxmanage modifyvm rh9-node1 --cpus 2 --memory 2048
[root@localhost66 vm]#
[root@localhost66 vm]# vboxmanage modifyvm rh9-node1 --nic1 bridged --bridgeadapter1 eno1
VBoxManage: warning: Interface "eth0" doesn't seem to exist
[root@localhost66 vm]#
[root@localhost66 vm]# vboxmanage storagectl rh9-node1 --name "SATA Controller" --add sata --bootable on
[root@localhost66 vm]#
[root@localhost66 vm]# vboxmanage storageattach rh9-node1 --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium rh9-node1.vdi
[root@localhost66 vm]#
[root@localhost66 vm]# vboxmanage storagectl rh9-node1 --name "IDE Controller" --add ide
[root@localhost66 vm]#
[root@localhost66 vm]# vboxmanage storageattach rh9-node1 --storagectl "IDE Controller" --port 0 --device 0 --type dvddrive --medium /ho
me/alma2/VBoxHome/iso/AlmaLinux-9-latest-x86_64-dvd.iso
[root@localhost66 vm]#
[root@localhost66 vm]# vboxmanage showvminfo rh9-node1
Name:                        rh9-node1
Encryption:     disabled
Groups:                      /
Guest OS:                    Red Hat 9.x (64-bit)
UUID:                        253cc2ba-935b-482c-83d3-14bc4ed72c22
Config file:                 /home/alma2/VBoxHome/vm/rh9-node1/rh9-node1.vbox
Snapshot folder:             /home/alma2/VBoxHome/vm/rh9-node1/Snapshots
Log folder:                  /home/alma2/VBoxHome/vm/rh9-node1/Logs
Hardware UUID:               253cc2ba-935b-482c-83d3-14bc4ed72c22
Memory size:                 2048MB
Page Fusion:                 disabled
VRAM size:                   8MB
CPU exec cap:                100%
HPET:                        disabled
CPUProfile:                  host
Chipset:                     piix3
Firmware:                    BIOS
Number of CPUs:              2
PAE:                         enabled
Long Mode:                   enabled
Triple Fault Reset:          disabled
APIC:                        enabled
X2APIC:                      disabled
Nested VT-x/AMD-V:           disabled
CPUID Portability Level:     0
CPUID overrides:             None
Boot menu mode:              message and menu
Boot Device 1:               Floppy
Boot Device 2:               DVD
Boot Device 3:               HardDisk
Boot Device 4:               Not Assigned
ACPI:                        enabled
IOAPIC:                      enabled
BIOS APIC mode:              APIC
Time offset:                 0ms
BIOS NVRAM File:             /home/alma2/VBoxHome/vm/rh9-node1/rh9-node1.nvram
RTC:                         local time
Hardware Virtualization:     enabled
Nested Paging:               enabled
Large Pages:                 enabled
VT-x VPID:                   enabled
VT-x Unrestricted Exec.:     enabled
AMD-V Virt. Vmsave/Vmload:   enabled
IOMMU:                       None
Paravirt. Provider:          Default
Effective Paravirt. Prov.:   KVM
State:                       powered off (since 2023-01-22T06:34:24.000000000)
Graphics Controller:         VBoxVGA
Monitor count:               1
3D Acceleration:             disabled
2D Video Acceleration:       disabled
Teleporter Enabled:          disabled
Teleporter Port:             0
Teleporter Address:
Teleporter Password:
Tracing Enabled:             disabled
Allow Tracing to Access VM:  disabled
Tracing Configuration:
Autostart Enabled:           disabled
Autostart Delay:             0
Default Frontend:
VM process priority:         default
Storage Controllers:
#0: 'SATA Controller', Type: IntelAhci, Instance: 0, Ports: 30 (max 30), Bootable
  Port 0, Unit 0: UUID: 4973af85-5e20-43c2-b630-73084cc5191f
    Location: "/home/alma2/VBoxHome/vm/rh9-node1.vdi"
#1: 'IDE Controller', Type: PIIX4, Instance: 0, Ports: 2 (max 2), Bootable
  Port 0, Unit 0: UUID: 539a2d14-2403-4f93-b39a-861dfeefb7fe
    Location: "/home/alma2/VBoxHome/iso/AlmaLinux-9-latest-x86_64-dvd.iso"
NIC 1:                       MAC: 080027B9DDCA, Attachment: Bridged Interface 'eth0', Cable connected: on, Trace: off (file: none), Type: 82540EM, Reported speed: 0 Mbps, Boot priority: 0, Promisc Policy: deny, Bandwidth group: none
NIC 2:                       disabled
NIC 3:                       disabled
NIC 4:                       disabled
NIC 5:                       disabled
NIC 6:                       disabled
NIC 7:                       disabled
NIC 8:                       disabled
Pointing Device:             PS/2 Mouse
Keyboard Device:             PS/2 Keyboard
UART 1:                      disabled
UART 2:                      disabled
UART 3:                      disabled
UART 4:                      disabled
LPT 1:                       disabled
LPT 2:                       disabled
Audio:                       enabled (Driver: Default, Controller: AC97, Codec: STAC9700)
Audio playback:              disabled
Audio capture:               disabled
Clipboard Mode:              disabled
Drag and drop Mode:          disabled
VRDE:                        disabled
OHCI USB:                    disabled
EHCI USB:                    disabled
xHCI USB:                    disabled
USB Device Filters:          <none>
Bandwidth groups:            <none>
Shared folders:              <none>
Recording enabled:           no
Recording screens:           1
 Screen 0:
    Enabled:                 yes
    ID:                      0
    Record video:            yes
    Destination:             File
    File:                    /home/alma2/VBoxHome/vm/rh9-node1/rh9-node1-screen0.webm
    Options:                 vc_enabled=true,ac_enabled=false,ac_profile=med
    Video dimensions:        1024x768
    Video rate:              512kbps
    Video FPS:               25fps
* Guest:
Configured memory balloon:   0MB

[root@localhost66 vm]#
[root@localhost66 vm]# export DISPLAY="192.168.1.10:0.0"
[root@localhost66 vm]# vboxmanage startvm rh9-node1
```

```
[root@localhost66 alma2]# vboxmanage
Oracle VM VirtualBox Command Line Management Interface Version 7.0.6
Copyright (C) 2005-2023 Oracle and/or its affiliates

Usage - Oracle VM VirtualBox command-line interface:

  VBoxManage [-V | --version] [--dump-build-type] [-q | --nologo] [--settingspw=password] [--settingspwfile=pw-file] [@response-file]
      [[help] subcommand]


  VBoxManage list [--long] [--sorted] [bridgedifs | cloudnets | cloudprofiles | cloudproviders | cpu-profiles | dhcpservers | dvds |
      extpacks | floppies | groups | hddbackends | hdds | hostcpuids | hostdrives | hostdvds | hostfloppies | hostinfo | hostonlyifs |
      hostonlynets | intnets | natnets | ostypes | runningvms | screenshotformats | systemproperties | usbfilters | usbhost | vms |
      webcams]


  VBoxManage showvminfo <uuid | vmname> [--details] [--machinereadable] [--password-id] [--password]

  VBoxManage showvminfo <uuid | vmname> <--log=index> [--password-idid] [--passwordfile|-]


  VBoxManage registervm <filename> --passwordfile


  VBoxManage unregistervm <uuid | vmname> [--delete] [--delete-all]


  VBoxManage createvm <--name=name> [--basefolder=basefolder] [--default] [--group=group-ID,...] [--ostype=ostype] [--register]
      [--uuid=uuid] [--ciphercipher] [--password-idpassword-id] [--passwordfile]


  VBoxManage modifyvm <uuid | vmname> [--name=name] [--groups= group[,group...] ] [--description=description] [--os-type=OS-type]
      [--icon-file=filename] [--memory=size-in-MB] [--page-fusion= on | off ] [--vram=size-in-MB] [--acpi= on | off ] [--ioapic= on |
      off ] [--hardware-uuid=UUID] [--cpus=CPU-count] [--cpu-hotplug= on | off ] [--plug-cpu=CPU-ID] [--unplug-cpu=CPU-ID]
      [--cpu-execution-cap=number] [--pae= on | off ] [--long-mode= on | off ] [--ibpb-on-vm-exit= on | off ] [--ibpb-on-vm-entry= on |
      off ] [--spec-ctrl= on | off ] [--l1d-flush-on-sched= on | off ] [--l1d-flush-on-vm-entry= on | off ] [--mds-clear-on-sched= on |
      off ] [--mds-clear-on-vm-entry= on | off ] [--cpu-profile= host | Intel 8086 | Intel 80286 | Intel 80386 ] [--hpet= on | off ]
      [--hwvirtex= on | off ] [--triple-fault-reset= on | off ] [--apic= on | off ] [--x2apic= on | off ] [--paravirt-provider= none |
      default | legacy | minimal | hyperv | kvm ] [--paravirt-debug= key=value[,key=value...] ] [--nested-paging= on | off ]
      [--large-pages= on | off ] [--vtx-vpid= on | off ] [--vtx-ux= on | off ] [--nested-hw-virt= on | off ] [--virt-vmsave-vmload= on |
      off ] [--accelerate-3d= on | off ] [--accelerate-2d-video= on | off ] [--chipset= ich9 | piix3 ] [--iommu= none | automatic | amd
      | intel ] [--tpm-type= none | 1.2 | 2.0 | host | swtpm ] [--tpm-location= location ] [--bios-logo-fade-in= on | off ]
      [--bios-logo-fade-out= on | off ] [--bios-logo-display-time=msec] [--bios-logo-image-path=pathname] [--bios-boot-menu= disabled |
      menuonly | messageandmenu ] [--bios-apic= disabled | apic | x2apic ] [--bios-system-time-offset=msec] [--bios-pxe-debug= on | off
      ] [--system-uuid-le= on | off ] [--bootX= none | floppy | dvd | disk | net ] [--rtc-use-utc= on | off ] [--graphicscontroller=
      none | vboxvga | vmsvga | vboxsvga ] [--snapshot-folder= default | pathname ] [--firmware= bios | efi | efi32 | efi64 ]
      [--guest-memory-balloon=size-in-MB] [--default-frontend= default | name ] [--vm-process-priority= default | flat | low | normal |
      high ]

  VBoxManage modifyvm <uuid | vmname> [--nicN= none | null | nat | bridged | intnet | hostonly | hostonlynet | generic | natnetwork |
      cloud ] [--nic-typeN= Am79C970A | Am79C973 | 82540EM | 82543GC | 82545EM | virtio ] [--cable-connectedN= on | off ] [--nic-traceN=
      on | off ] [--nic-trace-fileN=filename] [--nic-propertyN=name= [value] ] [--nic-speedN=kbps] [--nic-boot-prioN=priority]
      [--nic-promiscN= deny | allow-vms | allow-all ] [--nic-bandwidth-groupN= none | name ] [--bridge-adapterN= none | device-name ]
      [--cloud-networkN=network-name] [--host-only-adapterN= none | device-name ] [--host-only-netN=network-name]
      [--intnetN=network-name] [--nat-networkN=network-name] [--nic-generic-drvN=driver-name] [--mac-addressN= auto | MAC-address ]

  VBoxManage modifyvm <uuid | vmname> [--nat-netN= network | default ] [--nat-pfN= [rule-name],tcp |
      udp,[host-IP],hostport,[guest-IP],guestport ] [--nat-pfN=delete=rule-name] [--nat-tftp-prefixN=prefix] [--nat-tftp-fileN=filename]
      [--nat-tftp-serverN=IP-address] [--nat-bind-ipN=IP-address] [--nat-dns-pass-domainN= on | off ] [--nat-dns-proxyN= on | off ]
      [--nat-dns-host-resolverN= on | off ] [--nat-localhostreachableN= on | off ]
      [--nat-settingsN=[mtu],[socksnd],[sockrcv],[tcpsnd],[tcprcv]] [--nat-alias-modeN= default | [log],[proxyonly],[sameports] ]

  VBoxManage modifyvm <uuid | vmname> [--mouse= ps2 | usb | usbtablet | usbmultitouch | usbmtscreenpluspad ] [--keyboard= ps2 | usb ]
      [--uartN= off | IO-baseIRQ ] [--uart-modeN= disconnected | serverpipe | clientpipe | tcpserverport | tcpclienthostname:port |
      filefilename | device-name ] [--uart-typeN= 16450 | 16550A | 16750 ] [--lpt-modeN=device-name] [--lptN= off | IO-baseIRQ ]
      [--audio-controller= ac97 | hda | sb16 ] [--audio-codec= stac9700 | ad1980 | stac9221 | sb16 ] [--audio-driver= none | default |
      null | dsound | was | oss | alsa | pulse | coreaudio ] [--audio-enabled= on | off ] [--audio-in= on | off ] [--audio-out= on | off
      ] [--clipboard-mode= disabled | hosttoguest | guesttohost | bidirectional ] [--drag-and-drop= disabled | hosttoguest | guesttohost
      | bidirectional ] [--monitor-count=number] [--usb-ehci= on | off ] [--usb-ohci= on | off ] [--usb-xhci= on | off ]
      [--usb-rename=old-namenew-name]

  VBoxManage modifyvm <uuid | vmname> [--recording= on | off ] [--recording-screens= all | none | screen-ID[,screen-ID...] ]
      [--recording-file=filename] [--recording-max-size=MB] [--recording-max-time=msec] [--recording-opts= key=value[,key=value...] ]
      [--recording-video-fps=fps] [--recording-video-rate=rate] [--recording-video-res=widthheight]

  VBoxManage modifyvm <uuid | vmname> [--vrde= on | off ] [--vrde-property=property-name= [property-value] ] [--vrde-extpack= default |
      name ] [--vrde-port=port] [--vrde-address=hostip] [--vrde-auth-type= null | external | guest ] [--vrde-auth-library= default |
      name ] [--vrde-multi-con= on | off ] [--vrde-reuse-con= on | off ] [--vrde-video-channel= on | off ]
      [--vrde-video-channel-quality=percent]

  VBoxManage modifyvm <uuid | vmname> [--teleporter= on | off ] [--teleporter-port=port] [--teleporter-address= address | empty ]
      [--teleporter-password=password] [--teleporter-password-file= filename | stdin ] [--cpuid-portability-level=level]
      [--cpuid-set=leaf [:subleaf] eax?ebx?ecx?edx] [--cpuid-remove=leaf [:subleaf] ] [--cpuid-remove-all]

  VBoxManage modifyvm <uuid | vmname> [--tracing-enabled= on | off ] [--tracing-config=string] [--tracing-allow-vm-access= on | off ]

  VBoxManage modifyvm <uuid | vmname> [--usb-card-reader= on | off ]

  VBoxManage modifyvm <uuid | vmname> [--autostart-enabled= on | off ] [--autostart-delay=seconds]

  VBoxManage modifyvm <uuid | vmname> [--guest-debug-provider= none | native | gdb | kd ] [--guest-debug-io-provider= none | tcp | udp |
      ipc ] [--guest-debug-address= IP-Address | path ] [--guest-debug-port=port]

  VBoxManage modifyvm <uuid | vmname> [--pci-attach=host-PCI-address [@guest-PCI-bus-address] ] [--pci-detach=host-PCI-address]

  VBoxManage modifyvm <uuid | vmname> [--testing-enabled= on | off ] [--testing-mmio= on | off ] [--testing-cfg-dwordidx=value]


  VBoxManage snapshot <uuid|vmname>

  VBoxManage snapshot <uuid|vmname> take <snapshot-name> [--description=description] [--live]
      [--uniquename Number,Timestamp,Space,Force]

  VBoxManage snapshot <uuid|vmname> delete <snapshot-name>

  VBoxManage snapshot <uuid|vmname> restore <snapshot-name>

  VBoxManage snapshot <uuid|vmname> restorecurrent

  VBoxManage snapshot <uuid|vmname> edit <snapshot-name | --current> [--description=description] [--name=new-name]

  VBoxManage snapshot <uuid|vmname> list [--details | --machinereadable]

  VBoxManage snapshot <uuid|vmname> showvminfo <snapshot-name>


  VBoxManage clonevm <vmname|uuid> [--basefolder=basefolder] [--groups=group,...] [--mode=machine | --mode=machinechildren | --mode=all]
      [--name=name] [--options=option,...] [--register] [--snapshot=snapshot-name] [--uuid=uuid]


  VBoxManage movevm <uuid | vmname> [--type=basic] [--folder=folder-name]


  VBoxManage encryptvm <uuid | vmname> setencryption --old-passwordfile --ciphercipher-identifier --new-passwordfile
      --new-password-idpassword-identifier --force

  VBoxManage encryptvm <uuid | vmname> checkpassword <file>

  VBoxManage encryptvm <uuid | vmname> addpassword --passwordfile --password-idpassword-identifier

  VBoxManage encryptvm <uuid | vmname> removepassword <password-identifier>


  VBoxManage startvm <uuid | vmname...> [--putenv=name[=value]] [--type= [gui | headless | sdl | separate] ] --passwordfile
      --password-idpassword identifier


  VBoxManage controlvm <uuid | vmname> pause

  VBoxManage controlvm <uuid | vmname> resume

  VBoxManage controlvm <uuid | vmname> reset

  VBoxManage controlvm <uuid | vmname> poweroff

  VBoxManage controlvm <uuid | vmname> savestate

  VBoxManage controlvm <uuid | vmname> acpipowerbutton

  VBoxManage controlvm <uuid | vmname> acpisleepbutton

  VBoxManage controlvm <uuid | vmname> reboot

  VBoxManage controlvm <uuid | vmname> shutdown [--force]

  VBoxManage controlvm <uuid | vmname> keyboardputscancode <hex> [hex...]

  VBoxManage controlvm <uuid | vmname> keyboardputstring <string> [string...]

  VBoxManage controlvm <uuid | vmname> keyboardputfile <filename>

  VBoxManage controlvm <uuid | vmname> setlinkstateN <on | off>

  VBoxManage controlvm <uuid | vmname> nicN <null | nat | bridged | intnet | hostonly | generic | natnetwork> [device-name]

  VBoxManage controlvm <uuid | vmname> nictraceN <on | off>

  VBoxManage controlvm <uuid | vmname> nictracefileN <filename>

  VBoxManage controlvm <uuid | vmname> nicpropertyN <prop-name=prop-value>

  VBoxManage controlvm <uuid | vmname> nicpromiscN <deny | allow-vms | allow-all>

  VBoxManage controlvm <uuid | vmname> natpfN <[rulename] ,tcp | udp, host-IP, hostport, guest-IP, guestport>

  VBoxManage controlvm <uuid | vmname> natpfNdelete <rulename>

  VBoxManage controlvm <uuid | vmname> guestmemoryballoon <balloon-size>

  VBoxManage controlvm <uuid | vmname> usbattach <uuid | address> [--capturefile=filename]

  VBoxManage controlvm <uuid | vmname> usbdetach <uuid | address>

  VBoxManage controlvm <uuid | vmname> audioin <on | off>

  VBoxManage controlvm <uuid | vmname> audioout <on | off>

  VBoxManage controlvm <uuid | vmname> clipboard mode <disabled | hosttoguest | guesttohost | bidirectional>

  VBoxManage controlvm <uuid | vmname> clipboard filetransfers <on | off>

  VBoxManage controlvm <uuid | vmname> draganddrop <disabled | hosttoguest | guesttohost | bidirectional>

  VBoxManage controlvm <uuid | vmname> vrde <on | off>

  VBoxManage controlvm <uuid | vmname> vrdeport <port>

  VBoxManage controlvm <uuid | vmname> vrdeproperty <prop-name=prop-value>

  VBoxManage controlvm <uuid | vmname> vrdevideochannelquality <percentage>

  VBoxManage controlvm <uuid | vmname> setvideomodehint <xres> <yres> <bpp> [[display]  [enabled:yes | no | x-origin?y-origin] ]

  VBoxManage controlvm <uuid | vmname> setscreenlayout <display> <on | primaryx-origin?y-origin?x-resolution?y-resolution?bpp | off>

  VBoxManage controlvm <uuid | vmname> screenshotpng <filename> [display]

  VBoxManage controlvm <uuid | vmname> recording <on | off>

  VBoxManage controlvm <uuid | vmname> recording screens <all | none | screen-ID[,screen-ID...]>

  VBoxManage controlvm <uuid | vmname> recording filename <filename>

  VBoxManage controlvm <uuid | vmname> recording videores <widthxheight>

  VBoxManage controlvm <uuid | vmname> recording videorate <rate>

  VBoxManage controlvm <uuid | vmname> recording videofps <fps>

  VBoxManage controlvm <uuid | vmname> recording maxtime <sec>

  VBoxManage controlvm <uuid | vmname> recording maxfilesize <MB>

  VBoxManage controlvm <uuid | vmname> setcredentials <username> --passwordfile= <filename | password>  <domain-name> --allowlocallogon=
      <yes | no>

  VBoxManage controlvm <uuid | vmname> teleport <--host=host-name> <--port=port-name> [--maxdowntime=msec] [--passwordfile=filename |
      --password=password]

  VBoxManage controlvm <uuid | vmname> plugcpu <ID>

  VBoxManage controlvm <uuid | vmname> unplugcpu <ID>

  VBoxManage controlvm <uuid | vmname> cpuexecutioncap <num>

  VBoxManage controlvm <uuid | vmname> vm-process-priority <default | flat | low | normal | high>

  VBoxManage controlvm <uuid | vmname> webcam attach [pathname [settings] ]

  VBoxManage controlvm <uuid | vmname> webcam detach [pathname]

  VBoxManage controlvm <uuid | vmname> webcam list

  VBoxManage controlvm <uuid | vmname> addencpassword <ID> <password-file | -> [--removeonsuspend= yes | no ]

  VBoxManage controlvm <uuid | vmname> removeencpassword <ID>

  VBoxManage controlvm <uuid | vmname> removeallencpasswords

  VBoxManage controlvm <uuid | vmname> changeuartmodeN disconnected | serverpipe-name | clientpipe-name | tcpserverport |
      tcpclienthostname:port | filefilename | device-name

  VBoxManage controlvm <uuid | vmname> autostart-enabledN on | off

  VBoxManage controlvm <uuid | vmname> autostart-delayseconds


  VBoxManage import <ovfname | ovaname> [--dry-run] [--options= keepallmacs | keepnatmacs | importtovdi ] [--vsys=n] [--ostype=ostype]
      [--vmname=name] [--settingsfile=file] [--basefolder=folder] [--group=group] [--memory=MB] [--cpus=n] [--description=text] [--eula=
      show | accept ] [--unit=n] [--ignore] [--scsitype= BusLogic | LsiLogic ] [--disk=path] [--controller=index] [--port=n]

  VBoxManage import OCI:// --cloud [--ostype=ostype] [--vmname=name] [--basefolder=folder] [--memory=MB] [--cpus=n] [--description=text]
      <--cloudprofile=profile> <--cloudinstanceid=id> [--cloudbucket=bucket]


  VBoxManage export <machines> <--output=name> [--legacy09 | --ovf09 | --ovf10 | --ovf20] [--manifest] [--options= manifest | iso |
      nomacs | nomacsbutnat... ] [--vsys=virtual-system-number] [--description=description-info] [--eula=license-text]
      [--eulafile=filename] [--product=product-name] [--producturl=product-URL] [--vendor=vendor-name] [--vendorurl=vendor-URL]
      [--version=version-info] [--vmname=vmname]

  VBoxManage export <machine> <--output=cloud-service-provider> [--opc10] [--vmname=vmname] [--cloud=virtual-system-number]
      [--cloudprofile=cloud-profile-name] [--cloudshape=cloud-shape-name] [--clouddomain=cloud-domain] [--clouddisksize=disk-size-in-GB]
      [--cloudbucket=bucket-name] [--cloudocivcn=OCI-VCN-ID] [--cloudocisubnet=OCI-subnet-ID] [--cloudkeepobject= true | false ]
      [--cloudlaunchinstance= true | false ] [--cloudlaunchmode= EMULATED | PARAVIRTUALIZED ] [--cloudpublicip= true | false ]


  VBoxManage mediumio <--disk=uuid|filename | --dvd=uuid|filename | --floppy=uuid|filename> [--password-file=-|filename] formatfat
      [--quick]

  VBoxManage mediumio <--disk=uuid|filename | --dvd=uuid|filename | --floppy=uuid|filename> [--password-file=-|filename] cat [--hex]
      [--offset=byte-offset] [--size=bytes] [--output=-|filename]

  VBoxManage mediumio <--disk=uuid|filename | --dvd=uuid|filename | --floppy=uuid|filename> [--password-file=-|filename] stream
      [--format=image-format] [--variant=image-variant] [--output=-|filename]


  VBoxManage sharedfolder add <uuid | vmname> <--name=name> <--hostpath=hostpath> [--readonly] [--transient] [--automount]
      [--auto-mount-point=path]

  VBoxManage sharedfolder remove <uuid | vmname> <--name=name> [--transient]


  VBoxManage dhcpserver add <--network=netname | --interface=ifname> <--server-ip=address> <--netmask=mask> <--lower-ip=address>
      <--upper-ip=address> <--enable | --disable>
       [--global | --set-opt=dhcp-opt-no value... | --set-opt-hex=dhcp-opt-no hexstring... | --force-opt=dhcp-opt-no... |
           --supress-opt=dhcp-opt-no... | --min-lease-time=seconds | --default-lease-time=seconds | --max-lease-time=seconds...]
       [--group=name | --set-opt=dhcp-opt-no value... | --set-opt-hex=dhcp-opt-no hexstring... | --force-opt=dhcp-opt-no... |
           --supress-opt=dhcp-opt-no... | --incl-mac=address... | --excl-mac=address... | --incl-mac-wild=pattern... |
           --excl-mac-wild=pattern... | --incl-vendor=string... | --excl-vendor=string... | --incl-vendor-wild=pattern... |
           --excl-vendor-wild=pattern... | --incl-user=string... | --excl-user=string... | --incl-user-wild=pattern... |
           --excl-user-wild=pattern... | --min-lease-time=seconds | --default-lease-time=seconds | --max-lease-time=seconds...]
       [--vm=name|uuid | --nic=1-N | --set-opt=dhcp-opt-no value... | --set-opt-hex=dhcp-opt-no hexstring... |
           --force-opt=dhcp-opt-no... | --supress-opt=dhcp-opt-no... | --min-lease-time=seconds | --default-lease-time=seconds |
           --max-lease-time=seconds | --fixed-address=address...]
       [--mac-address=address | --set-opt=dhcp-opt-no value... | --set-opt-hex=dhcp-opt-no hexstring... | --force-opt=dhcp-opt-no... |
           --supress-opt=dhcp-opt-no... | --min-lease-time=seconds | --default-lease-time=seconds | --max-lease-time=seconds |
           --fixed-address=address...]

  VBoxManage dhcpserver modify <--network=netname | --interface=ifname> [--server-ip=address] [--lower-ip=address] [--upper-ip=address]
      [--netmask=mask] [--enable | --disable]
       [--global | --del-opt=dhcp-opt-no... | --set-opt=dhcp-opt-no value... | --set-opt-hex=dhcp-opt-no hexstring... |
           --force-opt=dhcp-opt-no... | --unforce-opt=dhcp-opt-no... | --supress-opt=dhcp-opt-no... | --unsupress-opt=dhcp-opt-no... |
           --min-lease-time=seconds | --default-lease-time=seconds | --max-lease-time=seconds | --remove-config...]
       [--group=name | --set-opt=dhcp-opt-no value... | --set-opt-hex=dhcp-opt-no hexstring... | --force-opt=dhcp-opt-no... |
           --unforce-opt=dhcp-opt-no... | --supress-opt=dhcp-opt-no... | --unsupress-opt=dhcp-opt-no... | --del-mac=address... |
           --incl-mac=address... | --excl-mac=address... | --del-mac-wild=pattern... | --incl-mac-wild=pattern... |
           --excl-mac-wild=pattern... | --del-vendor=string... | --incl-vendor=string... | --excl-vendor=string... |
           --del-vendor-wild=pattern... | --incl-vendor-wild=pattern... | --excl-vendor-wild=pattern... | --del-user=string... |
           --incl-user=string... | --excl-user=string... | --del-user-wild=pattern... | --incl-user-wild=pattern... |
           --excl-user-wild=pattern... | --zap-conditions | --min-lease-time=seconds | --default-lease-time=seconds |
           --max-lease-time=seconds | --remove-config...]
       [--vm=name|uuid | --nic=1-N | --del-opt=dhcp-opt-no... | --set-opt=dhcp-opt-no value... | --set-opt-hex=dhcp-opt-no hexstring...
           | --force-opt=dhcp-opt-no... | --unforce-opt=dhcp-opt-no... | --supress-opt=dhcp-opt-no... | --unsupress-opt=dhcp-opt-no... |
           --min-lease-time=seconds | --default-lease-time=seconds | --max-lease-time=seconds | --fixed-address=address |
           --remove-config...]
       [--mac-address=address | --del-opt=dhcp-opt-no... | --set-opt=dhcp-opt-no value... | --set-opt-hex=dhcp-opt-no hexstring... |
           --force-opt=dhcp-opt-no... | --unforce-opt=dhcp-opt-no... | --supress-opt=dhcp-opt-no... | --unsupress-opt=dhcp-opt-no... |
           --min-lease-time=seconds | --default-lease-time=seconds | --max-lease-time=seconds | --fixed-address=address |
           --remove-config...]

  VBoxManage dhcpserver remove <--network=netname | --interface=ifname>

  VBoxManage dhcpserver start <--network=netname | --interface=ifname>

  VBoxManage dhcpserver restart <--network=netname | --interface=ifname>

  VBoxManage dhcpserver stop <--network=netname | --interface=ifname>

  VBoxManage dhcpserver findlease <--network=netname | --interface=ifname> <--mac-address=mac>


  VBoxManage debugvm <uuid|vmname> dumpvmcore [--filename=name]

  VBoxManage debugvm <uuid|vmname> info <item> [args...]

  VBoxManage debugvm <uuid|vmname> injectnmi

  VBoxManage debugvm <uuid|vmname> log [--release | --debug] [group-settings...]

  VBoxManage debugvm <uuid|vmname> logdest [--release | --debug] [destinations...]

  VBoxManage debugvm <uuid|vmname> logflags [--release | --debug] [flags...]

  VBoxManage debugvm <uuid|vmname> osdetect

  VBoxManage debugvm <uuid|vmname> osinfo

  VBoxManage debugvm <uuid|vmname> osdmesg [--lines=lines]

  VBoxManage debugvm <uuid|vmname> getregisters [--cpu=id] [reg-set.reg-name...]

  VBoxManage debugvm <uuid|vmname> setregisters [--cpu=id] [reg-set.reg-name=value...]

  VBoxManage debugvm <uuid|vmname> show [--human-readable | --sh-export | --sh-eval | --cmd-set] [settings-item...]

  VBoxManage debugvm <uuid|vmname> stack [--cpu=id]

  VBoxManage debugvm <uuid|vmname> statistics [--reset] [--descriptions] [--pattern=pattern]

  VBoxManage debugvm <uuid|vmname> guestsample [--filename=filename] [--sample-interval-us=interval] [--sample-time-us=time]


  VBoxManage extpack install [--replace] [--accept-license=sha256] <tarball>

  VBoxManage extpack uninstall [--force] <name>

  VBoxManage extpack cleanup


  VBoxManage unattended detect <--iso=install-iso> [--machine-readable]

  VBoxManage unattended install <uuid|vmname> <--iso=install-iso> [--user=login] [--password=password] [--password-file=file]
      [--full-user-name=name] [--key=product-key] [--install-additions] [--no-install-additions] [--additions-iso=add-iso]
      [--install-txs] [--no-install-txs] [--validation-kit-iso=testing-iso] [--locale=ll_CC] [--country=CC] [--time-zone=tz]
      [--hostname=fqdn] [--package-selection-adjustment=keyword] [--dry-run] [--auxiliary-base-path=path] [--image-index=number]
      [--script-template=file] [--post-install-template=file] [--post-install-command=command]
      [--extra-install-kernel-parameters=params] [--language=lang] [--start-vm=session-type]


  VBoxManage cloud <--provider=name> <--profile=name>
       list instances [--state=string] [--compartment-id=string]

  VBoxManage cloud <--provider=name> <--profile=name>
       list images <--compartment-id=string> [--state=string]

  VBoxManage cloud <--provider=name> <--profile=name>
       instance create <--domain-name=name> <--image-id=id | --boot-volume-id=id> <--display-name=name> <--shape=type> <--subnet=id>
           [--boot-disk-size=size in GB] [--publicip=true/false] [--privateip=IP address] [--public-ssh-key=key string...]
           [--launch-mode=NATIVE/EMULATED/PARAVIRTUALIZED] [--cloud-init-script-path=path to a script]

  VBoxManage cloud <--provider=name> <--profile=name>
       instance info <--id=unique id>

  VBoxManage cloud <--provider=name> <--profile=name>
       instance terminate <--id=unique id>

  VBoxManage cloud <--provider=name> <--profile=name>
       instance start <--id=unique id>

  VBoxManage cloud <--provider=name> <--profile=name>
       instance pause <--id=unique id>

  VBoxManage cloud <--provider=name> <--profile=name>
       image create <--display-name=name> [--bucket-name=name] [--object-name=name] [--instance-id=unique id]

  VBoxManage cloud <--provider=name> <--profile=name>
       image info <--id=unique id>

  VBoxManage cloud <--provider=name> <--profile=name>
       image delete <--id=unique id>

  VBoxManage cloud <--provider=name> <--profile=name>
       image import <--id=unique id> [--bucket-name=name] [--object-name=name]

  VBoxManage cloud <--provider=name> <--profile=name>
       image export <--id=unique id> <--display-name=name> [--bucket-name=name] [--object-name=name]

  VBoxManage cloud <--provider=name> <--profile=name>
       network setup [--gateway-os-name=string] [--gateway-os-version=string] [--gateway-shape=string] [--tunnel-network-name=string]
           [--tunnel-network-range=string] [--proxy=string] [--compartment-id=string]

  VBoxManage cloud <--provider=name> <--profile=name>
       network create <--name=string> <--network-id=string> [--enable | --disable]

  VBoxManage cloud network update <--name=string> [--network-id=string] [--enable | --disable]

  VBoxManage cloud network delete <--name=string>

  VBoxManage cloud network info <--name=string>


  VBoxManage cloudprofile <--provider=name> <--profile=name> add [--clouduser=unique id] [--fingerprint=MD5 string] [--keyfile=path]
      [--passphrase=string] [--tenancy=unique id] [--compartment=unique id] [--region=string]

  VBoxManage cloudprofile <--provider=name> <--profile=name> update [--clouduser=unique id] [--fingerprint=MD5 string] [--keyfile=path]
      [--passphrase=string] [--tenancy=unique id] [--compartment=unique id] [--region=string]

  VBoxManage cloudprofile <--provider=name> <--profile=name> delete

  VBoxManage cloudprofile <--provider=name> <--profile=name> show


  VBoxManage signova <ova> <--certificate=file> <--private-key=file> [--private-key-password-file=password-file |
      --private-key-password=password] [--digest-type=type] [--pkcs7 | --no-pkcs7] [--intermediate-cert=file] [--force] [--verbose]
      [--quiet] [--dry-run]


  VBoxManage modifynvram <uuid|vmname> inituefivarstore

  VBoxManage modifynvram <uuid|vmname> enrollmssignatures

  VBoxManage modifynvram <uuid|vmname> enrollorclpk

  VBoxManage modifynvram <uuid|vmname> enrollpk [--platform-key=filename] [--owner-uuid=uuid]

  VBoxManage modifynvram <uuid|vmname> listvars

  VBoxManage modifynvram <uuid|vmname> queryvar [--name=name] [--filename=filename]

  VBoxManage modifynvram <uuid|vmname> deletevar [--name=name] [--owner-uuid=uuid]

  VBoxManage modifynvram <uuid|vmname> changevar [--name=name] [--filename=filename]


  VBoxManage hostonlynet add <--name=netname> [--id=netid] <--netmask=mask> <--lower-ip=address> <--upper-ip=address> [--enable |
      --disable]

  VBoxManage hostonlynet modify <--name=netname | --id=netid> [--lower-ip=address] [--upper-ip=address] [--netmask=mask] [--enable |
      --disable]

  VBoxManage hostonlynet remove <--name=netname | --id=netid>


  VBoxManage updatecheck perform [--machine-readable]

  VBoxManage updatecheck list [--machine-readable]

  VBoxManage updatecheck modify [--disable | --enable] [--channel=stable | withbetas | all] [--frequency=days]


  VBoxManage discardstate <uuid | vmname>


  VBoxManage adoptstate <uuid | vmname> <state-filename>


  VBoxManage closemedium [disk | dvd | floppy] <uuid | filename> [--delete]


  VBoxManage storageattach <uuid | vmname> <--storagectl=name> [--bandwidthgroup= name | none ] [--comment=text] [--device=number]
      [--discard= on | off ] [--encodedlun=lun] [--forceunmount] [--hotpluggable= on | off ] [--initiator=initiator] [--intnet]
      [--lun=lun] [--medium= none | emptydrive | additions | uuid | filename | host:drive | iscsi ] [--mtype= normal | writethrough |
      immutable | shareable | readonly | multiattach ] [--nonrotational= on | off ] [--passthrough= on | off ] [--passwordfile=file]
      [--password=password] [--port=number] [--server= name | ip ] [--setparentuuid=uuid] [--setuuid=uuid] [--target=target]
      [--tempeject= on | off ] [--tport=port] [--type= dvddrive | fdd | hdd ] [--username=username]


  VBoxManage storagectl <uuid | vmname> <--name=controller-name> [--add= floppy | ide | pcie | sas | sata | scsi | usb ] [--controller=
      BusLogic | I82078 | ICH6 | IntelAhci | LSILogic | LSILogicSAS | NVMe | PIIX3 | PIIX4 | USB | VirtIO ] [--bootable= on | off ]
      [--hostiocache= on | off ] [--portcount=count] [--remove] [--rename=new-controller-name]


  VBoxManage bandwidthctl <uuid | vmname> add <bandwidth-group-name> <--limit=bandwidth-limit[k|m|g|K|M|G]> <--type=disk|network>

  VBoxManage bandwidthctl <uuid | vmname> list [--machinereadable]

  VBoxManage bandwidthctl <uuid | vmname> remove <bandwidth-group-name>

  VBoxManage bandwidthctl <uuid | vmname> set <bandwidth-group-name> <--limit=bandwidth-limit[k|m|g|K|M|G]>


  VBoxManage showmediuminfo [disk | dvd | floppy] <uuid | filename>


  VBoxManage createmedium [disk | dvd | floppy] <--filename=filename> [--size=megabytes | --sizebyte=bytes] [--diffparent= UUID |
      filename ] [--format= VDI | VMDK | VHD ] [--variant Standard,Fixed,Split2G,Stream,ESX,Formatted,RawDisk] --propertyname=value...
      --property-filename=/path/to/file/with/value...


  VBoxManage modifymedium [disk | dvd | floppy] <uuid | filename> [--autoreset=on | off] [--compact] [--description=description]
      [--move=pathname] [--property=name=[value]] [--resize=megabytes| --resizebyte=bytes] [--setlocation=pathname]
      [--type=normal | writethrough | immutable | shareable | readonly | multiattach]


  VBoxManage clonemedium <uuid | source-medium> <uuid | target-medium> [disk | dvd | floppy] [--existing] [--format= VDI | VMDK | VHD |
      RAW | other ] [--variant=Standard,Fixed,Split2G,Stream,ESX]


  VBoxManage mediumproperty [disk | dvd | floppy] set <uuid | filename> <property-name> <property-value>

  VBoxManage mediumproperty [disk | dvd | floppy] get <uuid | filename> <property-name>

  VBoxManage mediumproperty [disk | dvd | floppy] delete <uuid | filename> <property-name>


  VBoxManage encryptmedium <uuid | filename> [--cipher=cipher-ID] [--newpassword=password] [--newpasswordid=password-ID]
      [--oldpassword=password]


  VBoxManage checkmediumpwd <uuid | filename> <password-file>


  VBoxManage convertfromraw <inputfile> <outputfile> [--format= VDI | VMDK | VHD ] [--uuid=uuid]
      [--variant=Standard,Fixed,Split2G,Stream,ESX]

  VBoxManage convertfromraw stdin <outputfile> [--format= VDI | VMDK | VHD ] [--uuid=uuid] [--variant=Standard,Fixed,Split2G,Stream,ESX]


  VBoxManage setextradata <global | uuid | vmname> <keyword> [value]


  VBoxManage getextradata <global | uuid | vmname> keyword | enumerate


  VBoxManage setproperty <property-name> <property-value>


  VBoxManage usbfilter add <index,0-N> <--target= <uuid | vmname | global> > <--name=string> <--action=ignore | hold>
      [--active=yes | no] [--vendorid=XXXX] [--productid=XXXX] [--revision=IIFF] [--manufacturer=string] [--product=string] [--port=hex]
      [--remote=yes | no] [--serialnumber=string] [--maskedinterfaces=XXXXXXXX]

  VBoxManage usbfilter modify <index,0-N> <--target= <uuid | vmname | global> > [--name=string] [--action=ignore | hold]
      [--active=yes | no] [--vendorid=XXXX| ""] [--productid=XXXX| ""] [--revision=IIFF| ""] [--manufacturer=string| ""]
      [--product=string| ""] [--port=hex] [--remote=yes | no] [--serialnumber=string| ""] [--maskedinterfaces=XXXXXXXX]

  VBoxManage usbfilter remove <index,0-N> <--target= <uuid | vmname | global> >


  VBoxManage guestproperty get <uuid | vmname> <property-name> [--verbose]

  VBoxManage guestproperty enumerate <uuid | vmname> [--no-timestamp] [--no-flags] [--relative] [--old-format] [patterns...]

  VBoxManage guestproperty set <uuid | vmname> <property-name> [property-value [--flags=flags] ]

  VBoxManage guestproperty unset <uuid | vmname> <property-name>

  VBoxManage guestproperty wait <uuid | vmname> <patterns> [--timeout=msec] [--fail-on-timeout]


  VBoxManage guestcontrol <uuid | vmname> run [--domain=domainname] [--dos2unix] [--exe=filename] [--ignore-orphaned-processes]
      [--no-wait-stderr | --wait-stderr] [--no-wait-stdout | --wait-stdout] [--passwordfile=password-file | --password=password]
      [--profile] [--putenv=var-name=[value]] [--quiet] [--timeout=msec] [--unix2dos] [--unquoted-args] [--username=username]
      [--verbose] <--program/arg0 [argument...] >

  VBoxManage guestcontrol <uuid | vmname> start [--domain=domainname] [--exe=filename] [--ignore-orphaned-processes]
      [--passwordfile=password-file | --password=password] [--profile] [--putenv=var-name=[value]] [--quiet] [--timeout=msec]
      [--unquoted-args] [--username=username] [--verbose] <--program/arg0 [argument...] >

  VBoxManage guestcontrol <uuid | vmname> copyfrom [--dereference] [--domain=domainname] [--passwordfile=password-file |
      --password=password] [--quiet] [--no-replace] [--recursive] [--target-directory=host-destination-dir] [--update]
      [--username=username] [--verbose] <guest-source0> guest-source1[...] <host-destination>

  VBoxManage guestcontrol <uuid | vmname> copyto [--dereference] [--domain=domainname] [--passwordfile=password-file |
      --password=password] [--quiet] [--no-replace] [--recursive] [--target-directory=guest-destination-dir] [--update]
      [--username=username] [--verbose] <host-source0> host-source1[...]

  VBoxManage guestcontrol <uuid | vmname> mkdir [--domain=domainname] [--mode=mode] [--parents] [--passwordfile=password-file |
      --password=password] [--quiet] [--username=username] [--verbose] <guest-directory...>

  VBoxManage guestcontrol <uuid | vmname> rmdir [--domain=domainname] [--passwordfile=password-file | --password=password] [--quiet]
      [--recursive] [--username=username] [--verbose] <guest-directory...>

  VBoxManage guestcontrol <uuid | vmname> rm [--domain=domainname] [--force] [--passwordfile=password-file | --password=password]
      [--quiet] [--username=username] [--verbose] <guest-directory...>

  VBoxManage guestcontrol <uuid | vmname> mv [--domain=domainname] [--passwordfile=password-file | --password=password] [--quiet]
      [--username=username] [--verbose] <source...> <destination-directory>

  VBoxManage guestcontrol <uuid | vmname> mktemp [--directory] [--domain=domainname] [--mode=mode] [--passwordfile=password-file |
      --password=password] [--quiet] [--secure] [--tmpdir=directory-name] [--username=username] [--verbose] <template-name>

  VBoxManage guestcontrol <uuid | vmname> stat [--domain=domainname] [--passwordfile=password-file | --password=password] [--quiet]
      [--username=username] [--verbose] <filename>

  VBoxManage guestcontrol <uuid | vmname> list <all | files | processes | sessions> [--quiet] [--verbose]

  VBoxManage guestcontrol <uuid | vmname> closeprocess [--session-id=ID | --session-name=name-or-pattern] [--quiet] [--verbose] <PID...>

  VBoxManage guestcontrol <uuid | vmname> closesession [--all | --session-id=ID | --session-name=name-or-pattern] [--quiet] [--verbose]

  VBoxManage guestcontrol <uuid | vmname> updatega [--quiet] [--verbose] [--source=guest-additions.ISO] [--wait-start] [-- [argument...]
      ]

  VBoxManage guestcontrol <uuid | vmname> watch [--quiet] [--verbose]


  VBoxManage metrics collect [--detach] [--list] [--period=seconds] [--samples=count] [* | host | vmname metric-list]

  VBoxManage metrics disable [--list] [* | host | vmname metric-list]

  VBoxManage metrics enable [--list] [* | host | vmname metric-list]

  VBoxManage metrics list [* | host | vmname metric-list]

  VBoxManage metrics query [* | host | vmname metric-list]

  VBoxManage metrics setup [--list] [--periodseconds] [--samplescount] [* | host | vmname metric-list]


  VBoxManage natnetwork add [--disable | --enable] <--netname=name> <--network=network> [--dhcp=on|off] [--ipv6=on|off]
      [--loopback-4=rule] [--loopback-6=rule] [--port-forward-4=rule] [--port-forward-6=rule]

  VBoxManage natnetwork list [filter-pattern]

  VBoxManage natnetwork modify [--dhcp=on|off] [--disable | --enable] <--netname=name> <--network=network> [--ipv6=on|off]
      [--loopback-4=rule] [--loopback-6=rule] [--port-forward-4=rule] [--port-forward-6=rule]

  VBoxManage natnetwork remove <--netname=name>

  VBoxManage natnetwork start <--netname=name>

  VBoxManage natnetwork stop <--netname=name>


  VBoxManage hostonlyif ipconfig <ifname> [--dhcp | --ip=IPv4-address --netmask=IPv4-netmask | --ipv6=IPv6-address
      --netmasklengthv6=length]

  VBoxManage hostonlyif create

  VBoxManage hostonlyif remove <ifname>


  VBoxManage usbdevsource add <source-name> <--backend=backend> <--address=address>

  VBoxManage usbdevsource remove <source-name>
[root@localhost66 alma2]#
```