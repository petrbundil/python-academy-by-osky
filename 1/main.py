strana = float(input("Velikost strany čtverce? "))

if strana > 0:
    obvod = 4 * strana
# print("Obvod čtverce se stranou " + str(strana) + " je " + str(obvod))
    print("Obvod čtverce se stranou", strana, "je", obvod, "cm")
else:
    print("Ti jebe či co???")
