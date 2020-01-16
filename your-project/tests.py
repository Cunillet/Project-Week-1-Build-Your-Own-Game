import base64
import os
import random

data = "abc123!?$*&()'-=@~"

# Standard Base64 Encoding in bytes
encodedBytes = base64.b64encode(data.encode("utf-8"))
# encoded to string
encodedStr = str(encodedBytes, "utf-8")
# save the encripted string in a file
enc = open('./files/enc_f', 'w+')
enc.write(encodedStr)
print('encoded bytes', encodedBytes)
print(data)
print(encodedStr)
# save the decripted value in a new file
# dec = os.open('./files/dec_f', os.O_RDWR|os.O_CREAT)
dec = open('./files/dec_f', 'w+')
base64.decode(enc, dec)

decodedBytes = base64.b64decode(encodedStr)
decodedStr = str(decodedBytes, "utf-8")

print(decodedBytes)
print(decodedStr)

dec.close()
enc.close()
