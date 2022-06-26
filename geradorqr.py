# import the pyqrcode  module after you install it
import pyqrcode

# take user input
# this is the text for which we want to generate a QR code
text = input("EDigite o texto para gera QR code: ")

# create a pyqrcode object by calling the create() method
# we will use our text as an argument
qr_code = pyqrcode.create(text)

# calling the svg() method of the qr_code object
# creates the file named qr_code.svg in svg format
# the scale argument sets how large to draw a single image
qr_code.svg('qr_code.svg', scale=8)
