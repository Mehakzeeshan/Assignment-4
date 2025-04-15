from pyzbar.pyzbar import  decode
from PIL import Image


#DECODING QR CODE

img = Image.open('C:/Users/i Tech Computers/Pictures/Camera Roll/myqrcode.png')

result = decode(img)

print(result)