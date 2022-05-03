#!/usr/bin/env python

import os

print(f"Called from process with ID {os.getpid()} spawned from parent process with ID {os.getppid()}")
