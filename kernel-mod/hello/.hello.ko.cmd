cmd_/root/kernel/hello/hello.ko := ld -r -m elf_x86_64  -z max-page-size=0x200000 -T ./scripts/module-common.lds  --build-id  -o /root/kernel/hello/hello.ko /root/kernel/hello/hello.o /root/kernel/hello/hello.mod.o ;  true
