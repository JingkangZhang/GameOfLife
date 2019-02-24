import base64
f = open("one.py", "rb")
encoded = base64.b64encode(f.read())
f = open("encoded.py", "wb")
f.write(encoded)
f.close()
