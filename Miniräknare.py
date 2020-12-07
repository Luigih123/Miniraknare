

print("Välkommen till miniräknaren.")
print("[1] Räkna med +")
print("[2] Räkna med -")
print("[3] Räkna med *")
print("[4] Valfritt arbete, om du vill")
print("[5] Avsluta")
while True:
    alternativ = int(input("Välj ett alternativ :"))
    if alternativ == 1:
        num1 = float(input("skriv ett tal :"))
        num2 = float(input("skriv ett tal :"))
        num3 = num1 + num2 
        print(f'{num1} + {num2} = {num3}')
    elif alternativ == 2:
        print("")
    elif alternativ == 3:
        print("")
    elif alternativ == 4:
        print("")
    elif alternativ == 5:
        print("")
    break