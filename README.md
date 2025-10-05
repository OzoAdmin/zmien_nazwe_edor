# zmien_nazwe_edor

Skrypt Python do oczyszczania nazw plików z polskich znaków diakrytycznych i specjalnych charakterów.

## Opis

Program kopiuje pliki z oczyszczonymi nazwami, usuwając problematyczne znaki, które mogą powodować problemy w różnych systemach operacyjnych i aplikacjach. Oryginalny plik pozostaje nienaruszony - tworzona jest kopia z nową nazwą.

## Funkcjonalność

Skrypt wykonuje następujące operacje na nazwach plików:

1. **Usuwa polskie znaki diakrytyczne** - zamienia znaki takie jak ą, ć, ę, ł, ń, ó, ś, ź, ż na ich odpowiedniki ASCII (a, c, e, l, n, o, s, z, z)
2. **Zamienia spacje na znaki plus (+)**
3. **Usuwa problematyczne znaki specjalne**: `: ~ " # % & * < > ? ! / { | }`

## Użycie

### Uruchomienie z linii poleceń

```bash
python zmien_nazwe_edor.py plik1.txt plik2.pdf "plik z polskimi znakami.doc"
```

### Przeciąganie plików na skrypt

Możesz przeciągnąć pliki bezpośrednio na plik skryptu w Eksploratorze Windows.

### Przykład

**Plik wejściowy:** `Ważny dokument z ąćęłńóśźż!.pdf`  
**Plik wyjściowy:** `Wazny+dokument+z+acelnoszz.pdf`

## Tworzenie pliku wykonywalnego (.exe)

Jeśli chcesz używać skryptu na komputerach bez zainstalowanego Pythona, możesz utworzyć plik wykonywalny (.exe) przy użyciu PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile zmien_nazwe_edor.py
```

Po wykonaniu tej komendy, w folderze `dist` zostanie utworzony plik `zmien_nazwe_edor.exe`, który można uruchamiać na dowolnym komputerze z Windows bez konieczności instalacji Pythona.

### Użycie pliku .exe

```cmd
zmien_nazwe_edor.exe plik1.txt plik2.pdf "plik z polskimi znakami.doc"
```

lub przeciągnięcie plików na `zmien_nazwe_edor.exe` w Eksploratorze Windows.

## Wymagania

### Dla skryptu Python
- Python 3.x
- Standardowe biblioteki Python (sys, os, shutil)

### Dla pliku wykonywalnego (.exe)
- Brak wymagań - działa na dowolnym systemie Windows

## Funkcje

### `remove_polish_diacritics(text: str) -> str`
Usuwa polskie znaki diakrytyczne z podanego tekstu, obsługując zarówno małe jak i wielkie litery.

### `clean_filename(original_name: str) -> str`
Kompleksowo oczyszcza nazwę pliku:
- Usuwa polskie diakrytyki
- Zamienia spacje na znaki plus
- Usuwa niedozwolone znaki specjalne

### `main()`
Główna funkcja programu, która:
- Przetwarza argumenty wiersza poleceń
- Sprawdza istnienie plików
- Wykonuje kopię z oczyszczoną nazwą
- Wyświetla informacje o postępie

## Charakterystyka

- **Bezpieczne operacje** - oryginalny plik pozostaje niezmieniony
- **Wsparcie dla wielu plików** - można przetwarzać kilka plików jednocześnie
- **Intuicyjny interfejs** - wyraźne komunikaty o statusie operacji
- **Obsługa błędów** - informuje o problemach z kopiowaniem plików
- **Przenośność** - możliwość utworzenia pliku wykonywalnego .exe

## Autor

**Michał Kowalski**  
informatykbudzetowy.pl  
michal@informatykbudzetowy.pl

## Wersja

0.0.2

## Licencja

Projekt udostępniony jako narzędzie pomocnicze dla administracji IT.
