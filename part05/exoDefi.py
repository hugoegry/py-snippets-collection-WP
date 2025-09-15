import random
import time

start = time.time()
# V1
uneListe = []
for i in range(1000000):
    uneListe.append(random.randint(1, 1000000))
    uneListe = sorted(uneListe)

# V2
uneListe = [random.randint(1, 1000000) for _ in range(1000000)]
uneListe.sort()
print(uneListe)
print(time.time() - start)
