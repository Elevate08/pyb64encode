#!/bin/sh python3

import sys
import base64

def encode(data):
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")

    return encodedStr

if __name__ == "__main__":
    for arg in sys.argv:
        if "main.py" not in arg:
            encoded = encode(arg)
            print(f'{arg}: {encoded}')
