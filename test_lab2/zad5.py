from PIL import Image
import numpy as np

# Funkcja do rysowania naprzemiennych czarnych i białych ramek
def rysuj_ramki(w, h, grub):
    obraz = np.ones((h, w), dtype=np.uint8)  # Tworzenie białego obrazu
    current_color = 0  # Zaczynamy od czarnego
    for i in range(0, min(h, w)//2, grub):
        obraz[i:h-i, i:w-i] = current_color
        current_color = 1 - current_color  # Przełączanie między czarnym (0) a białym (1)
    return Image.fromarray(obraz.astype(bool))

# Wykonanie funkcji
obraz_ramki = rysuj_ramki(80, 130, 5)

# Zapisanie obrazu w formacie BMP
bmp_path = 'obraz_ramki.bmp'
obraz_ramki.save(bmp_path)

# Otworzenie obrazu przekonwertowanego na 24-bitową mapę bitową
# (zakładam, że dokonasz konwersji samodzielnie, a plik będzie nazywał się 'obraz_ramki_24bit.bmp')
jpeg_path = 'obraz_ramki_24bit.bmp'  # Upewnij się, że plik JPEG o tej nazwie istnieje
obraz_24bit = Image.open(jpeg_path)

# Pobieranie informacji o trybie obrazu i jego tablicy
tryb_obrazu = obraz_24bit.mode
rozmiar_obrazu = obraz_24bit.size
tablica = np.asarray(obraz_24bit)
wymiar_tablicy = tablica.shape
liczba_elementow_tablicy = tablica.size

# Przygotowanie odpowiedzi
info = f"{tryb_obrazu}; {rozmiar_obrazu}; {wymiar_tablicy}; {liczba_elementow_tablicy}"
print(info)
