#include <linux/module.h>
#include <linux/seq_file.h>
#include <linux/sysinfo.h>
#include <linux/vmstat.h>

MODULE_AUTHOR("Your Name");
MODULE_LICENSE("GPL");

static int thread_function(void *data)
{
    struct sysinfo info;
    struct timespec ts;
    struct seq_file *file;
    unsigned long totalram_pages;
    unsigned long total_swap_pages;
    unsigned long mem_usage;
    unsigned long slab;
    int i;

    while (!kthread_should_stop()) {
        si_meminfo(&info);
        totalram_pages = (info.totalram + PAGE_SIZE - 1) / PAGE_SIZE;
        total_swap_pages = info.totalswap / PAGE_SIZE;
        getnstimeofday(&ts);
        file = seq_open(NULL, &seq_operations);
        if (!file) {
            printk(KERN_ERR "Failed to open /proc file\n");
            return 0;
        }
        seq_printf(file, "%lld.%09ld %lu %lu %lu %lu ", (long long)ts.tv_sec, ts.tv_nsec,
                info.totalram, info.freeram, info.bufferram, global_node_page_state(NR_ACTIVE_FILE));
        for (i = 0; i <= MAX_NR_ZONES; i++)
            seq_printf(file, "%lu ", zone_page_state(totalram_pages, i));
        slab = zone_page_state(totalram_pages, NR_SLAB_RECLAIMABLE) + zone_page_state(totalram_pages, NR_SLAB_UNRECLAIMABLE);
        seq_printf(file, "%lu %lu ", slab, global_node_page_state(NR_FILE_PAGES));
        mem_usage = 100 - info.freeram * 100 / (totalram_pages - total_swap_pages);
        seq_printf(file, "%lu\n", mem_usage);
        seq_close(file);
        nanosleep(&(struct timespec){.tv_sec = 10, .tv_nsec = 0}, NULL);
    }

    return 0;
}

static struct task_struct *thread;

static int __init memorylog_init(void)
{
    thread = kthread_create(thread_function, NULL, "memorylog");
    if (IS_ERR(thread)) {
        printk(KERN_ERR "Failed to create kernel thread\n");
        return -ENOMEM;
    }
    wake_up_process(thread);
    return 0;
}

static void __exit memorylog_exit(void)
{
    kthread_stop(thread);
}

module_init(memorylog_init);
module_exit(memorylog_exit);

