# 📁 File Renamer – Python

Prosty i szybki program w Pythonie do **masowej zmiany nazw plików w folderze**.  
Idealny do porządkowania plików takich jak dokumenty, zdjęcia, CSV, EXE itd.

---

## 🔧 Funkcje

- ✅ Zmiana nazw wszystkich plików w wybranym folderze
- ✅ Automatyczna numeracja plików
- ✅ Zachowanie oryginalnych rozszerzeń (`.txt`, `.csv`, `.exe`, itd.)
- ✅ Obsługa dowolnej liczby plików
- ✅ Program działa lokalnie – **pliki nie są wysyłane nigdzie na zewnątrz**

---

## 📌 Jak działa

1. Podajesz ścieżkę do folderu z plikami  
2. Podajesz nazwę bazową (np. `raport`)  
3. Program zmienia nazwy plików według schematu:

raport_1.txt
raport_2.txt
raport_3.exe
raport_4.csv

yaml
Skopiuj kod

---

## ▶️ Uruchomienie

### Wymagania
- Python 3.8+

### Uruchomienie programu
```bash
python file_renamer.py
Po uruchomieniu program poprosi o:

ścieżkę do folderu

nazwę bazową plików

🖥️ Przykład
Przed:

arduino
Skopiuj kod
document.txt
image.png
program.exe
Po:

Skopiuj kod
file_1.txt
file_2.png
file_3.exe
⚠️ Uwagi
Program zmienia nazwy bez cofania (undo) – zalecane jest wykonanie kopii zapasowej

Zmieniane są tylko pliki, foldery są pomijane

📜 Licencja
Projekt udostępniony na licencji MIT – możesz go dowolnie używać, modyfikować i rozwijać.

👤 Autor
Autor: MaroBrzeszczot
Projekt stworzony jako część portfolio Python / automatyzacja.
