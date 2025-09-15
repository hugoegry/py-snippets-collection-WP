n_bottles: int = 99
for n in range(n_bottles, 0, -1):
  print(f"{n} bottles of beer on the wall.")
  print(f"{n} bottles of beer.")
  print("Take one down, pass it around,")
  print(f"{n-1} bottles of beer on the wall\n")

print("No more bottles of beer on the wall,")
print("no more bottles of beer.")
print("Go to the store and buy some more,")
print("99 bottles of beer on the wall...")