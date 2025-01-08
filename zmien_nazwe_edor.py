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
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N', 'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z',
    }
    for pl_char, ascii_char in replacements.items():
        text = text.replace(pl_char, ascii_char)
    return text

def clean_filename(original_name: str) -> str:
    """
    1) Usuwa polskie diakrytyki.
    2) Zmienia spacje na plusa '+'.
    3) Usuwa następujące znaki: : ~ " # % & * < > ? ! / { | }
    """
    name = remove_polish_diacritics(original_name)
    # Zamiana spacji na +
    name = name.replace(' ', '+')
    # Usuwanie niedozwolonych znaków
    # Używamy pętli lub wyrażeń regularnych. Tutaj pętla "dla czytelności":
    forbidden_chars = [':', '~', '"', '#', '%', '&', '*', '<', '>', '?', '!', '/', '{', '|', '}']
    for ch in forbidden_chars:
        name = name.replace(ch, '')
    return name

def main():
    """
    Skrypt kopiuje plik(i) do nowej nazwy z oczyszczoną nazwą.
    Nazwy plików przyjmuje z sys.argv[1:].
    """
    # Jeśli nie podano żadnych plików:
    if len(sys.argv) < 2:
        print("Nie podano plików do przetworzenia (przeciągnij je na skrypt lub podaj w cmd).")
        input("Naciśnij Enter, aby zakończyć...")
        return

    # Przetwarzamy każdy plik z listy argumentów
    for file_path in sys.argv[1:]:
        if not os.path.isfile(file_path):
            print(f"\n[UWAGA] '{file_path}' nie jest plikiem lub nie istnieje.")
            continue
        
        print(f"\nPrzetwarzam plik: {file_path}")

        # Rozbicie ścieżki na katalog, nazwę, rozszerzenie
        dir_name = os.path.dirname(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]  # nazwa bez rozszerzenia
        extension = os.path.splitext(os.path.basename(file_path))[1]  # np. ".txt"

        # Oczyszczanie nazwy
        new_base = clean_filename(base_name)
        new_filename = new_base + extension
        new_path = os.path.join(dir_name, new_filename)

        if new_path == file_path:
            print(f"Nazwa po konwersji pozostaje bez zmian: {new_filename}")
        else:
            print(f"Nowa nazwa pliku: {new_filename}")
        
        # Kopiowanie do nowej nazwy (zostawiamy oryginał)
        try:
            shutil.copy2(file_path, new_path)
            print(f"Skopiowano do: {new_path}")
        except Exception as e:
            print(f"[BLAD] Nie udalo sie skopiowac pliku: {e}")

    print("\nKoniec. Wszystkie pliki zostały przetworzone.")
    input("Naciśnij Enter, aby zakończyć...")

if __name__ == "__main__":
    main()
