# Program do automatycznej zmiany nazw plików dla eDoręczeń

Ten program służy do **automatycznego dostosowywania nazw plików** w taki sposób, aby spełniały wymogi systemu [eDoręczeń](https://www.gov.pl/web/cyfryzacja/edorzeczenia).  
Dzięki temu nie musisz ręcznie usuwać niedozwolonych znaków, spacji itp. Program sam wykona to zadanie za Ciebie, co jest szczególnie przydatne przy wysyłaniu wielu plików naraz.

## Funkcjonalności

1. **Zamiana spacji** na znak `_`.  
2. **Usuwanie niedozwolonych znaków** (np.: `: ~ " # % & * < > ? ! / { | }`).  
3. **Kopiowanie** pliku do nowej nazwy (oryginał pozostaje nienaruszony).  

Po wykonaniu programu nowy plik o poprawionej nazwie pojawi się w tym samym folderze co oryginał.

---

## Zawartość repozytorium

- **`README.md`** – Ten plik z opisem.  
- **`zmien_nazwe_edor.py`** – Główny program w Pythonie.  
  - Program można uruchomić bezpośrednio (wymagany zainstalowany Python),  
  - **lub** można go przekształcić w plik `.exe` (samodzielny, bez konieczności instalowania Pythona) za pomocą [PyInstaller](https://pyinstaller.org/).

---

## Kod programu: `zmien_nazwe_edor.py`

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import shutil

def clean_filename(original_name: str) -> str:
    """
    1) Zmienia spacje na podkreślnik '_'
    2) Usuwa niedozwolone znaki: : ~ " # % & * < > ? ! / { | }
    """
    name = original_name

    # (1) Zamiana spacji na podkreślnik '_'
    name = name.replace(' ', '_')

    # (2) Usuwanie wybranych niedozwolonych znaków
    forbidden_chars = [':', '~', '"', '#', '%', '&', '*', '<', '>', '?', '!', '/', '{', '|', '}']
    for ch in forbidden_chars:
        name = name.replace(ch, '')

    return name

def main():
    """
    Program kopiuje wskazane pliki do nowej nazwy, zamienia spacje na '_',
    a także usuwa pewne niedozwolone znaki. Nazwy plików pobiera z sys.argv[1:].
    """
    # Brak argumentów -> wyświetlamy komunikat
    if len(sys.argv) < 2:
        print("Nie podano plików do przetworzenia. Przeciągnij je na program lub podaj w CMD.")
        input("Naciśnij Enter, aby zakończyć...")
        return

    for file_path in sys.argv[1:]:
        if not os.path.isfile(file_path):
            print(f"\n[UWAGA] '{file_path}' nie jest plikiem lub nie istnieje.")
            continue
        
        print(f"\nPrzetwarzam plik: {file_path}")

        # Rozbicie ścieżki na katalog, nazwę i rozszerzenie
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
        
        # Kopiowanie (zachowanie oryginału)
        try:
            shutil.copy2(file_path, new_path)
            print(f"Skopiowano do: {new_path}")
        except Exception as e:
            print(f"[BŁĄD] Nie udało się skopiować: {e}")

    print("\nGotowe. Pliki zostały przetworzone.")
    input("Naciśnij Enter, aby zakończyć...")

if __name__ == "__main__":
    main()
