from PIL import Image
import numpy as np


image1 = Image.open("inicjaly.bmp")
'''
print("Informacje o obrazie:")
print("tryb:", image1.mode)
print("format:", image1.format)
print("rozmiar:", image1.size)
'''

#image1.show()
image1Data = np.asarray(image1)
'''
print(image1Data.shape)
print(image1Data.dtype)
print(image1Data.size)
print(image1Data.ndim)
print(image1Data)
'''
image1DataCopy = image1Data.astype(np.int_)
#print(image1DataCopy)

t1_text = open('t1.txt', 'w')
for rows in image1DataCopy:
    for item in rows:
        t1_text.write(str(item) + ' ')
    t1_text.write('\n')

t1_text.close()