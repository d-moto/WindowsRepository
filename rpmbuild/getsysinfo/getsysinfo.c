#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int get_cpu_usage() {
    // CPU使用率の計算方法にはさまざまなアプローチがあります。
    // ここでは簡単な例を示します。
    // 実際の実装にはより詳細なロジックが必要かもしれません。
        long double a[4], b[4], loadavg;
    FILE *fp;

    fp = fopen("/proc/stat","r");
    fscanf(fp, "%*s %Lf %Lf %Lf %Lf", &a[0], &a[1], &a[2], &a[3]);
    fclose(fp);
    sleep(1);

    fp = fopen("/proc/stat","r");
    fscanf(fp, "%*s %Lf %Lf %Lf %Lf", &b[0], &b[1], &b[2], &b[3]);
    fclose(fp);

    loadavg = ((b[0]+b[1]+b[2]) - (a[0]+a[1]+a[2])) / ((b[0]+b[1]+b[2]+b[3]) - (a[0]+a[1]+a[2]+a[3]));
    return (int)(loadavg * 100);
}

int get_core_count() {
    return sysconf(_SC_NPROCESSORS_ONLN);
}

int get_memory_usage() {
    // メモリ使用率の計算方法にはさまざまなアプローチがあります。
    // ここでは簡単な例を示します。
    // 実際の実装にはより詳細なロジックが必要かもしれません。
        FILE *fp = fopen("/proc/meminfo", "r");
    if(fp == NULL) {
        perror("Unable to open /proc/meminfo");
        return -1;
    }

    int total_memory = 0;
    int free_memory = 0;
    char buffer[256];

    while(fgets(buffer, sizeof(buffer), fp)) {
        sscanf(buffer, "MemTotal: %d kB", &total_memory);
        sscanf(buffer, "MemFree: %d kB", &free_memory);
    }

    fclose(fp);

    int used_memory = total_memory - free_memory;
    return (used_memory * 100) / total_memory;
}

int main() {
    int cpu_usage = get_cpu_usage();
    int core_count = get_core_count();
    int memory_usage = get_memory_usage();

    printf("CPU Usage: %d%%\n", cpu_usage);
    printf("CPU Cores: %d\n", core_count);
    printf("Memory Usage: %d%%\n", memory_usage);

    return 0;
}

