from PIL import Image
import numpy as np

# 1. Funkcja rysująca pionowe pasy
def rysuj_pasy_pionowe(w, h, grub):
    obraz = np.ones((h, w), dtype=np.uint8)  # Tworzenie białego obrazu
    for j in range(0, w, 2 * grub):
        obraz[:, j:j+grub] = 0  # Rysowanie czarnych pionowych pasów
    return Image.fromarray(obraz.astype(bool))

# 2. Funkcja wstawiająca obraz w inny obraz w zadanych współrzędnych
def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    # Konwersja obrazów do tablic numpy
    tab_bazowy = np.asarray(obraz_bazowy).copy()
    tab_wstawiany = np.asarray(obraz_wstawiany)

    # Wymiary obrazów
    h_bazowy, w_bazowy = tab_bazowy.shape
    h_wstawiany, w_wstawiany = tab_wstawiany.shape

    # Wstawianie obrazu
    for i in range(h_wstawiany):
        for j in range(w_wstawiany):
            if m + i < h_bazowy and n + j < w_bazowy:
                tab_bazowy[m + i, n + j] = tab_wstawiany[i, j]

    # Zwracanie zmodyfikowanego obrazu
    return Image.fromarray(tab_bazowy)

# 3. Tworzenie obrazu bazowego
obraz_bazowy = rysuj_pasy_pionowe(300, 200, 15)

# 4. Wczytanie obrazu 'inicjaly.bmp' z komputera
inicjaly_image = Image.open('inicjaly.bmp')  # Wczytaj obraz z pliku na swoim komputerze

# 5. Wstawienie obrazu w dwóch różnych miejscach, tworząc dwa różne obrazy

# Pierwszy obraz: wstawienie przy m=250, n=100
obraz1 = wstaw_obraz_w_obraz(obraz_bazowy, inicjaly_image, 150, 100)
obraz1.show()  # Wyświetlenie pierwszego obrazu

# Drugi obraz: wstawienie przy m=0, n=50
obraz2 = wstaw_obraz_w_obraz(obraz_bazowy, inicjaly_image, 0, 50)
obraz2.show()  # Wyświetlenie drugiego obrazu
