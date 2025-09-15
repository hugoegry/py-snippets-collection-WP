"""
📌 Instruction
write a snippet of code that extracts the decimal part of the
following numbers:
- 12.24
- 424242.8
"""
a: int = 12.24
b: int = 424242.8

a = a - int(a)
b = b - int(b) 

print(a)
print(b)