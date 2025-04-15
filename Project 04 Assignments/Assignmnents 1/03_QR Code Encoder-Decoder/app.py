import qrcode



#QR CODE 1
data = "Don\'t forget to subscribe to my channel!"

img = qrcode.make(data)

img.save('C:/Users/i Tech Computers/Pictures/Camera Roll/myqrcode.png')


#QR CODE 2
data1 = "Don\'t forget to subscribe to my channel!"

qr = qrcode.QRCode( version = 1, box_size= 10, border = 5)

qr.add_data(data1)

qr.make(fit=True)

img1 = qr.make_image(fill_color = 'red', back_color = 'white')

img1.save('C:/Users/i Tech Computers/Pictures/Camera Roll/myqrcode1.png')

