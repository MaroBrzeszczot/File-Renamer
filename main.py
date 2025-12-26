import os
# ==========================================
# Zmienia nazwe wszstkich danych w folderze
# ==========================================

folder_path = input("Podaj sciezke do folderu : ")
nazwa = input("Podaj nazwę bazową: ")

pliki = os.listdir(folder_path)
licznik = 1
grupujPoExt = True
for plik in pliki:
    file_path = os.path.join(folder_path, plik)


    if os.path.isfile(file_path):
        # print("Plik: ",plik)
        rozszerzenie = os.path.splitext(plik)[1].replace(".", "")
        if rozszerzenie == "": rozszerzenie ="brak_rozszerzenia"
        nowa_nazwa = f"{nazwa}_{licznik}.{rozszerzenie}"
        if grupujPoExt:
            folder_docelowy = os.path.join(folder_path, rozszerzenie)
            os.makedirs(folder_docelowy, exist_ok=True)
            new_file_path = os.path.join(folder_docelowy, nowa_nazwa)
        else:
            new_file_path = os.path.join(folder_path, nowa_nazwa)

        os.rename(file_path, new_file_path)
        licznik +=1

print(f"Zmieniono {licznik-1} {'plik' if licznik == 1 else 'pliki' if 1 < licznik < 5 else 'plików'}")
input("Wcisnij Enter aby zakonczyc")


