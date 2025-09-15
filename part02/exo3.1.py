"""
📌 Instruction
Write a snippet of code that computes the result, as well as both the quotient and the remainder of the
euclidean division 42/4. 
It should output something like:
10.5
10
2
"""

a: int = 42
b: int = 4
quotient: float = a / b
quotient2: int = a // b
rest: int = a % b
print(quotient)
print(quotient2)
print(rest)
