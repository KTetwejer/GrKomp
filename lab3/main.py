from PIL import Image
import numpy as np

#zadanie 1

def rysuj_ramki_szare(w, h, grub, kolor_zew, kolor_wew):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8) * kolor_zew
    tab[grub:h-grub, grub:w-grub] = kolor_wew
    return Image.fromarray(tab)

def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)

im_ramki_szare = rysuj_ramki_szare(300, 200, 5, 50, 150)
im_ramki_szare.save('ramki_szare.png')

im_pasy_szare = rysuj_pasy_pionowe_szare(300, 200, 5, 20)
im_pasy_szare.save('pasy_szare.png')

#zadanie 2

def negatyw(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape[:2]
    tab_neg = tab.copy()

    if obraz.mode == '1':
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = not tab[i, j]

    elif obraz.mode == 'L':
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab[i, j]

    elif obraz.mode == 'RGB':
        for i in range(h):
            for j in range(w):
                tab_neg[i, j, 0] = 255 - tab[i, j, 0]  # R
                tab_neg[i, j, 1] = 255 - tab[i, j, 1]  # G
                tab_neg[i, j, 2] = 255 - tab[i, j, 2]  # B

    return Image.fromarray(tab_neg)

gwiazdka = Image.open('gwiazdka.bmp')
negatyw_gwiazdka = negatyw(gwiazdka)
negatyw_gwiazdka.save('negatyw_gwiazdka.png')


def rysuj_ramki_kolorowe(w, kolor, a, b, c):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = kolor[0]
    kolor_g = kolor[1]
    kolor_b = kolor[2]
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - a) % 256
        kolor_g = (kolor_g - b) % 256
        kolor_b = (kolor_b - c) % 256
    return Image.fromarray(tab)

a = 6
b = 8
c = -a

obraz3 = rysuj_ramki_kolorowe(200, [20, 120, 220], a, b, c)
negatyw_kolorowe_ramki = negatyw(obraz3)
negatyw_kolorowe_ramki.save('negatyw_kolorowe_ramki.png')


def rysuj_po_skosie_szare(h, w, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a * i + b * j) % 256
    return Image.fromarray(tab)


im_skos = rysuj_po_skosie_szare(100, 300, a, b)
negatyw_skos = negatyw(im_skos)
negatyw_skos.save('negatyw_skos.png')


#zadanie 3

def koloruj_w_paski(obraz, grub, kolory):
    t_obraz = np.asarray(obraz.convert('1'))
    h, w = t_obraz.shape
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8) * 255
    ile_paskow = int(h / grub)
    for k in range(ile_paskow):
        kolor = kolory[k % len(kolory)]
        for i in range(k * grub, (k + 1) * grub):
            for j in range(w):
                if t_obraz[i, j] == 0:
                    tab[i, j] = kolor
    return Image.fromarray(tab)

inicjaly = Image.open('inicjaly.bmp')
kolory = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
obraz_kolorowy = koloruj_w_paski(inicjaly, 10, kolory)
obraz_kolorowy.save('kolorowe_inicjaly.png')

#zadanie 4

# Typ uint8 ma zakres od 0 do 255, więc musimy użyć operacji modulo, bez tej operacji dostajemy błąd
x = 328 % 256  # Zamiast bezpośredniej konwersji
y = -24 % 256  # Wynik dla wartości ujemnej

# Konwersja na typ uint8
x_uint8 = np.uint8(x)
y_uint8 = np.uint8(y)

print(f"328 jako uint8: {x_uint8}")  # Oczekiwany wynik: 72
print(f"-24 jako uint8: {y_uint8}")  # Oczekiwany wynik: 232