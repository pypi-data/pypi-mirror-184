import ctypes
import os
from sys import platform
from pathlib import Path

if platform in ["linux", "linux2"]:
    # linux\
    p = os.path.dirname(os.path.abspath(__file__))   
    library = ctypes.cdll.LoadLibrary(p.split('/lib')[0]+"/etc/library.so")
    hello_world = library.helloWorld


elif platform == "darwin":
    # OS X
    pass
elif platform == "win32":
    # windows
    library = ctypes.cdll.LoadLibrary('./etc/library.dll')
    rg =  library.RandomGenerator