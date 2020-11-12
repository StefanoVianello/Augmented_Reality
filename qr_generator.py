import pyqrcode
from PIL import Image
import png

# TODO make into a function with url and image strings + filename of finalprodut
# TODO add way of iterating over barcodes

# make QR code from custom string
qrobj = pyqrcode.QRCode('https://stefanovianello.github.io/Augmented_Reality/', error='H')
with open('output/test_qr.png', 'wb') as f:
    qrobj.png(f, scale=10)

# open the QR code to place the logo in the middle
img = Image.open('output/test_qr.png')
width, height = img.size

# open the logo image + white box image
logo = Image.open('barcodes/4.png')
square = Image.open('barcodes/white_square.png')

# place square, then logo on top
square_size = 150
xmin_square = ymin_square = int((width / 2) - (square_size / 2))
xmax_square = ymax_square = int((width / 2) + (square_size / 2))
square = square.resize((xmax_square - xmin_square, ymax_square - ymin_square))
img.paste(square, (xmin_square, ymin_square, xmax_square, ymax_square))

logo_size = 100
xmin = ymin = int((width / 2) - (logo_size / 2))
xmax = ymax = int((width / 2) + (logo_size / 2))
logo = logo.resize((xmax - xmin, ymax - ymin))
img.paste(logo, (xmin, ymin, xmax, ymax))

img.save('output/final_qr.png')
