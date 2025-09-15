import time

def puissance_rapide(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result


for n in [84, 168]:  # Test et mesure du temps
    start_time = time.time()
    result = puissance_rapide(42, n)
    end_time = time.time()
    print(f"42^{n} = {result}")
    print(f"Temps de calcul : {end_time - start_time:.10f} secondes\n")
