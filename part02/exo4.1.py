"""
📌 Instruction
Calculate the first 6 decimals of Pi using the formula:
π = 4*(1/1 - 1/3 + 1/5 - 1/7...)
"""

epsilon: float = 3.142006200273917 - 3.1419474389623643
N: int = 1
pi_prec: int = 0
max_N: int = 1000
while N < max_N:
    val: int = 2
    for k in range(N, 0, -1):
        n = 2 * k - 1
        val = n**2 / (6 + val)
    pi = 3 + val
    if abs(pi) < epsilon:
        break
    pi_prec = pi
    N += 1
print(pi)
