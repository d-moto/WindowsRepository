#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0xf8cdd757, "module_layout" },
	{ 0x3e18c761, "kthread_stop" },
	{ 0xc00d5473, "wake_up_process" },
	{ 0xdc1e5ca7, "kthread_create_on_node" },
	{ 0xf9a482f9, "msleep" },
	{ 0x27e1a049, "printk" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0xb3f7646e, "kthread_should_stop" },
	{ 0xbdfb6dbb, "__fentry__" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "FD10C25E02694CC2EB633DB");
MODULE_INFO(rhelversion, "8.7");
