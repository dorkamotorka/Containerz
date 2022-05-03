#!/usr/bin/env python

import os

print("execvp() called from process with ID", os.getpid())

# execvp is execve without env (3rd argument)
command = ['python', 'print_my_pid.py']
os.execvp(command[0], command)

print("This should not execute, because print_my_pid program replaces the program in current process")
