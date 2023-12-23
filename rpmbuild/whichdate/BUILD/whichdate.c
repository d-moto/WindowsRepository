#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main() {
    time_t t;
    struct tm *tm_info;

    time(&t);
    tm_info = localtime(&t);

    int seconds = tm_info->tm_sec;

    if (seconds % 2 == 0) {
        printf("INFO: pattern 2\n");
        return 2;
    } else {
        printf("INFO: pattern 1\n");
        return 1;
    }
}

