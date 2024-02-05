
print("Aim- Water Jug Problem")

G4 = 0
G3 = 0
while G4 != 2:
    ruleno = int(input("Enter the rule number: "))
    if ruleno == 1:
        G4 = 4
        G3 = G3
        print("4 gallon jug = ",G4)
        print("3 gallon jug = ",G3)
    elif ruleno == 2:
        G3 = 3
        G4 = G4
        print("4 gallon jug = ",G4)
        print("3 gallon jug = ",G3)
    elif ruleno == 5:
        G4 = 0
        print("4 gallon jug = ",G4)
        print("3 gallon jug = ",G3)
    elif ruleno == 6:
        G3 = 0
        print("4 gallon jug = ",G4)
        print("3 gallon jug = ",G3)
    elif ruleno == 7:
        G3 = G3-(4-G4)
        G4 = 4
        print("4 gallon jug = ",G4)
        print("3 gallon jug = ",G3)
    elif ruleno == 8:
        G4 = G4-(3-G3)
        G3 = 3
        print("4 gallon jug = ",G4)
        print("3 gallon jug = ",G3)
    elif ruleno == 9:
        G4 = G4+G3
        G3 = 0
        print("4 gallon jug = ",G4)
        print("3 gallon jug = ",G3)
    elif ruleno == 10:
        G3 = G3+G4
        G4 = 0
        print("4 gallon jug = ",G4)
        print("3 gallon jug = ",G3)
    elif ruleno == 11:
        G4 = 2
        G3 = 0
        print("4 gallon jug = ",G4)
        print("3 gallon jug = ",G3)
    elif ruleno == 12:
        G4 = 0
        G3 = G3
        print("4 gallon jug = ",G4)
        print("3 gallon jug = ",G3)
        