#!/usr/bin/env python

import os
import subprocess

print("Calling popen() from process with ID", os.getpid())
command = ['python', 'print_my_pid.py']

# os.popen is deprecated in Python3 in favor of subprocess.Popen
p1 = subprocess.Popen(command, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = p1.communicate()

print(out.decode("utf-8"))
