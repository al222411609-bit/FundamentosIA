valores = [True, False]

print("\nSelecciona la operación lógica:")
print("1. Negación (NO P)")
print("2. Conjunción (P Y Q)")
print("3. Disyunción (P O Q)")
print("4. Condicional (Si P entonces Q)")
print("5. Bicondicional (P si y solo si Q)")

opcion = int(input("\nOpción: "))


if opcion == 1:
    print("\n P | Resultado")
    print("=" * 23)
    for P in valores:
        resultado = not P
        print(P, "|", resultado)

else:
   # P y Q
    if opcion == 2:
        print("\n P | Q | P AND Q")
    elif opcion == 3:
        print("\n P | Q | P OR Q")
    elif opcion == 4:
        print("\n P | Q | P -> Q")
    elif opcion == 5:
        print("\n P | Q | P <-> Q")
    
    print("=" * 23)


    for P in valores:
        for Q in valores:
            
            if opcion == 2:
                resultado = P and Q
            elif opcion == 3:
                resultado = P or Q
            elif opcion == 4:
                resultado = (not P) or Q
            elif opcion == 5:
                resultado = P == Q

            print(P, "|", Q, "|", resultado)
