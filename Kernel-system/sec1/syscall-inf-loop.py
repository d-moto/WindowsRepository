#!/usr/bin/python3

import os
import time

while True:
    a = os.getppid()
    print(a)
    b = os.write(1, 12)
    print(b)
    time.sleep(1)
