import os
import time as tm
os.system("cls")
print("-"*25+"oOo"+"-"*25)
def zsom():
    szmok = []
    while len(szmok) <= 5:
        szam = input("Adj egy szmot")
        try:
            szmok.append(float(szam))
        except ValueError:
            print("Hibás bemeneti adat")
    os.system("cls")
    return szmok

def nev_kb():
    nevek= []
    while len(nevek) <=5:
        nev = input("Adj egy nevet")
        try: 
            int(nev)
            print("Hibás bemeneti adat")
        except ValueError:
            nevek.append(nev)
    os.system("cls")
    return nevek
 
szamok = zsom()
print("-"*25+"oOo"+"-"*25)
nevek = nev_kb()

with open("jegyek", "w") as jegy:
    for nev,szam in zip(nevek,szamok):
        jegy.write(f"{nev} :: {str(szam)}\n")

print("File írás kész")
v_olv = input("Vissza szeretnéd olvasni a filet?\n('Y' h igen hibás bemeneti adatat esetén nem olvasható vissza)")
if v_olv.upper() == "Y":
    olv_fi = open("jegyek","r")
    olvd_fi = olv_fi.read()
    print(olvd_fi)  
    print("File írás elvégezve.")ű
    olv_fi.Close()
    tm.sleep(10)
    os.system("cls")
else:
    tm.sleep(10)
    os.system("cls")
    print("File írás elvégezve.")
    