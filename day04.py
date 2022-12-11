import hashlib

p = 1
while True:
    if hashlib.md5(('bgvyzdsv' + str(p)).encode()).hexdigest().startswith('000000'):
        print(p)
        break
    p += 1
