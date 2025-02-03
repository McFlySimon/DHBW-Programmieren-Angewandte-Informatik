zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gerade_zahlen = []

for zahl in zahlen:
    if zahl % 2 == 0:
        gerade_zahlen.append(zahl)

print("Gerade Zahlen:", gerade_zahlen)
