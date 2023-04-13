cmd_/root/kernel/hello.ko := ld -r -m elf_x86_64  -z max-page-size=0x200000 -T ./scripts/module-common.lds  --build-id  -o /root/kernel/hello.ko /root/kernel/hello.o /root/kernel/hello.mod.o ;  true
