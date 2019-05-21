#!/usr/bin/python
import hashlib, base64

userInput = input("Input key: ").strip()

def secAccept(secKey):
    GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
    combine = (secKey+GUID).encode('ascii')
    keyId = hashlib.sha1(combine)
    #raw binary
    return base64.b64encode(keyId.digest())

print(str(secAccept(userInput)).split("'")[1])
