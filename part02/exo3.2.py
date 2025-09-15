"""
📌 Instruction
Write a snippet of code in order to check if a number is odd.
"""


def is_odd(n: int) -> bool:
    return n % 2 != 0


number: int = int(input("Entrez un nombre: "))
if is_odd(number):
    print("impair")
else:
    print("pair")
