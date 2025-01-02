# Skrypt do automatycznej zmiany nazw plików dla eDoręczeń

Ten skrypt służy do **automatycznego dostosowywania nazw plików** w taki sposób, aby spełniały wymogi systemu [eDoręczeń](https://www.gov.pl/web/cyfryzacja/edorzeczenia).  
Dzięki temu nie musisz ręcznie usuwać polskich znaków, spacji itp. Skrypt sam wykona to zadanie za Ciebie, co jest szczególnie przydatne przy wysyłaniu wielu plików naraz.

## Funkcjonalności

1. **Usuwanie polskich znaków diakrytycznych** (ą, ć, ę, ł, ń, ó, ś, ź, ż).  
2. **Zamiana spacji** na znak `+`.  
3. **Usuwanie niedozwolonych znaków** (np.: `: ~ " # % & * < > ? ! / { | }`).  
4. **Kopiowanie** pliku do nowej nazwy (oryginał pozostaje nienaruszony).  

Po wykonaniu skryptu nowy plik o poprawionej nazwie pojawi się w tym samym folderze co oryginał.

---

## Zawartość repozytorium

- **`README.md`** – Ten plik z opisem.  
- **`zmien_nazwe_edor.py`** – Główny skrypt w Pythonie.  
  - Skrypt można uruchomić bezpośrednio (wymagany zainstalowany Python),  
  - **lub** można go przekształcić w plik `.exe` (samodzielny, bez konieczności instalowania Pythona) za pomocą [PyInstaller](https://pyinstaller.org/).

---

## Kod skryptu: `zmien_nazwe_edor.py`

Poniższy kod możesz wkleić do pliku o nazwie `zmien_nazwe_edor.py`:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import shutil

def remove_polish_diacritics(text: str) -> str:
    """
    Usuwa polskie znaki diakrytyczne (małe i wielkie) z tekstu.
    """
    replacements = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z',
    }
    for pl_char, ascii_char in replacements.items():
        text = text.replace(pl_char, ascii_char)
    return text

def clean_filename(original_name: str) -> str:
    """
    1) Usuwa polskie diakrytyki
    2) Zmienia spacje na plus '+'
    3) Usuwa niedozwolone znaki: : ~ " # % & * < > ? ! / { | }
    """
    name = remove_polish_diacritics(original_name)
    # Zamiana spacji na +
    name = name.replace(' ', '+')
    # Usuwanie wybranych niedozwolonych znaków
    forbidden_chars = [':', '~', '"', '#', '%', '&', '*', '<', '>', '?', '!', '/', '{', '|', '}']
    for ch in forbidden_chars:
        name = name.replace(ch, '')
    return name

def main():
    """
    Skrypt kopiuje wskazane pliki do nowej nazwy akceptowanej przez eDoręczenia.
    Nazwy plików przyjmuje z sys.argv[1:].
    """
    # Brak argumentów -> wyświetlamy komunikat
    if len(sys.argv) < 2:
        print("Nie podano plików do przetworzenia. Przeciągnij je na skrypt lub podaj w CMD.")
        input("Naciśnij Enter, aby zakończyć...")
        return

    for file_path in sys.argv[1:]:
        if not os.path.isfile(file_path):
            print(f"\n[UWAGA] '{file_path}' nie jest plikiem lub nie istnieje.")
            continue
        
        print(f"\nPrzetwarzam plik: {file_path}")

        # Rozbicie ścieżki na katalog, nazwę, rozszerzenie
        dir_name = os.path.dirname(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        extension = os.path.splitext(os.path.basename(file_path))[1]

        # Oczyszczanie nazwy
        new_base = clean_filename(base_name)
        new_filename = new_base + extension
        new_path = os.path.join(dir_name, new_filename)

        if new_path == file_path:
            print(f"Nazwa po konwersji pozostaje bez zmian: {new_filename}")
        else:
            print(f"Nowa nazwa pliku: {new_filename}")
        
        # Kopiowanie (zostawienie oryginału)
        try:
            shutil.copy2(file_path, new_path)
            print(f"Skopiowano do: {new_path}")
        except Exception as e:
            print(f"[BŁĄD] Nie udało się skopiować: {e}")

    print("\nGotowe. Pliki zostały dostosowane do wymogów eDoręczeń.")
    input("Naciśnij Enter, aby zakończyć...")

if __name__ == "__main__":
    main()
