a = {
    "dalmatians" : 101,
    "pi" : 3.14,
    "beast" : 3*2*111,
    "life" : 42,
    "googol" : 10**100
}

print(max(a, key=a.get))