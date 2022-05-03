#!/usr/bin/env python

import os

os.fork()
os.fork()

print(f"Called from process with ID {os.getpid()} whose parent is {os.getppid()}")
# Parent of initial process of this program is shell process (you can check with ps)
