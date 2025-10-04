#!/usr/bin/env python3
from rune_gen import make_name, make_sigil, ascii_sigil
import sys
if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1]=="name":
        print(make_name(int(sys.argv[2]) if len(sys.argv)>2 else 2))
    else:
        print(ascii_sigil(make_sigil()))
