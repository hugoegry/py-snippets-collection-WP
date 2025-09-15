maList = ["a", 2, "a", 2, "A"]
# V1
m = set()
malist2 = [e for e in maList if e not in m and not m.append(e)]
print(malist2)
# V2
print(set(maList))
