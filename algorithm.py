import pytesseract
from PIL import Image
from autocorrect import Speller

#spell = Speller()

text = pytesseract.image_to_string(Image.open('Receipt2.JPG'))
#text = spell(text)
sorted_text = text.lower().split()

total = " "

f = open("total.json", "w")

for x in sorted_text:
    if x == 'total' or x == 'total:':
        total = sorted_text[sorted_text.index(x) + 1]
        break
    elif x == 'charge' or x == 'charge:':
        total = sorted_text[sorted_text.index(x) + 1]
        break
    elif x == 'subtotal' or x == 'subtotal:':
        for y in sorted_text:
            if y == 'tax' or y == 'tax':
                total = int(sorted_text[sorted_text.index(x) + 1]) + int(sorted_text[sorted_text.index(y) + 1])
                break
    else:
        total = "Price not found, please retake picture"

print(total)
f.write("{total: " + total + "}\n")

        