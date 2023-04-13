#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/delay.h>
#include <linux/kthread.h>

MODULE_LICENSE("GPL");

static struct task_struct *task;

static int thread_function(void *data)
{
    while (!kthread_should_stop()) {
        printk(KERN_INFO "Hello\n");
        msleep(10000);
    }

    return 0;
}

static int __init hello_init(void)
{
    printk(KERN_INFO "Hello module loaded.\n");

    task = kthread_create(thread_function, NULL, "hello");

    if (IS_ERR(task)) {
        printk(KERN_ERR "Failed to create hello thread.\n");
        return PTR_ERR(task);
    }

    wake_up_process(task);

    return 0;
}

static void __exit hello_exit(void)
{
    kthread_stop(task);
    printk(KERN_INFO "Hello module unloaded.\n");
}

module_init(hello_init);
module_exit(hello_exit);

