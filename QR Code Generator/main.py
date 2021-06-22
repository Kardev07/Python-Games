import qrcode 

data = 'QR\ Code builder'

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('C:/Users/karth/OneDrive/Desktop/Karthik/Codes/QR Code Generator/qrcode.png')