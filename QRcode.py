import qrcode


# ?making a qr code
myqrcodecontent = 'https://www.collince.com'
qrcode_image_name = 'myQRcodeImage.png'

img = qrcode.make(myqrcodecontent)
img.save(qrcode_image_name)
print("QR code created successfully")