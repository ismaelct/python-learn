#!/usr/bin/env python3
import os
if os.name == "posix":
    os.system("clear")
    print("unix")
elif os.name == "nt":
    os.system("cls")
    print("windows")
