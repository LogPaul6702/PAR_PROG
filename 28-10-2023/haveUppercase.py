def sprawdz_wielkie_litery(ciąg):
    if any(znak.isupper() for znak in ciąg):
        print("W podanym ciągu znajdują się wielkie litery.")
    else:
        print("W podanym ciągu nie ma żadnych wielkich liter.")

tekst = input("Podaj ciąg znaków: ")
sprawdz_wielkie_litery(tekst)