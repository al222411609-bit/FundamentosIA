valores = [True, False]

print("p \t q \t p and q")
print("=" * 25)

for p in valores:
    for q in valores:
        resultado = p and q
        print(p, "\t", "q", "\t", resultado)
