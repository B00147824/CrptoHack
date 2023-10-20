ciphertext = bytearray.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

flag = ""

for num in range(256):  # Bruteforce all possible byte value 0-255
    
    results = [chr(n^num) for n in ciphertext]
    
    flag = "".join(results)
    
    if flag.startswith("crypto"):
        print(flag)
        print(num)  # So we'll know the magic "single byte"

