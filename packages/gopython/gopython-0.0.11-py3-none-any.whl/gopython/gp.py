import ctypes
import os
from sys import platform
from pathlib import Path

if platform in ["linux", "linux2"]:
    # linux\
    fp = os.path.dirname(os.path.abspath(__file__))   
    path = fp.split('/lib')[0]+"/etc/library.so"
    library = ctypes.cdll.LoadLibrary(path)
    hello_world = library.helloWorld

elif platform == "darwin":
    # OS X
    p = os.path.dirname(os.path.abspath(__file__))   
    path = p.split('/lib')[0]+"/etc/library.so"
    library = ctypes.cdll.LoadLibrary(path)
    hello_world = library.helloWorld


elif platform == "win32":
    # windows
    fp = os.path.dirname(os.path.abspath(__file__))   
    path = fp.split("\lib")[0]+"\etc\library.dll"
    lib = ctypes.cdll.LoadLibrary(path)
    hello_world =  lib.helloWorld
