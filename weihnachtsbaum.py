hoehe = int(input("Wie hoch ist der Weihnachtsbaum?: "))

for i in range(hoehe):
    print(" " * (hoehe - i - 1) + "*" * (2*i+1))

for y in range(hoehe // 3):
    print(" " * (hoehe - 2) + "| |")