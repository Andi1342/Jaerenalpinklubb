# Tidtakning
import time

def getTotal(loper):
    return round(omgang1[loper] + omgang2[loper] + omgang3[loper], 3)

def printResultat(tider : dict, omgangNr : int):
    for startnummer,tid in tider.items():
        print (f"løper nummer {startnummer} i mål på {tid} i omgang {omgangNr}.") 

titel= ()
titel= input("løps dato + plass: ")

def kjaur ():
    loper = 1
    tider = {}

    print ("enter før start, q for quit")
    while True:

        
        s = input("neste løper")
        if s == "q":
            break
        start = time.perf_counter()

        input("tid startet, trykk enter for mål")
        slutt = time.perf_counter()

        print(f"løper nr {loper} i mål {slutt-start:.3F} sekunder")

        tider [loper] = round(slutt-start, 3)
        
        loper += 1
    return tider

def saveToFile(omganger):
    omgNr = 1
    with open(f"{titel}.csv", "w", encoding="UTF-8" ) as fil:

        for omgang in omganger:
            fil.write(f"\n Omgang nr{omgNr}:\n")
            for nr,tid in omgang.items():
                fil.write(f"Løper {nr}: omgang{omgNr}: {tid}, total: {getTotal(nr)}\n") 
            omgNr += 1
        fil.write(f"\n Takk for løpet")

omgang1 = kjaur()
input("omgang 2?")
omgang2 = kjaur()
input("Omgang 3?")
omgang3 = kjaur()

print("Snakkes på lan")

for i in omgang1.keys():
    print (f"totalt tid til løper {i}: {getTotal(i)}")

saveToFile([omgang1, omgang2, omgang3])

printResultat(omgang1, 1)
printResultat(omgang2, 2)
printResultat(omgang3, 3)
