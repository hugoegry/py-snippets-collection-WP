"""
📌 Instruction
Calculate the first 6 decimals of Pi using this amazing formula:
π − 3 = 1²
    6+ 3²
     6+ 5²
      6+ 7²
       6+...
"""

epsilon: int = 5e-7
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
