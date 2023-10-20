input_string = "label"
key = 13
result = "".join(chr(ord(char) ^ key) for char in input_string)
print(result)
