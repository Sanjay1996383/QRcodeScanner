import qrcode 
qr=qrcode.QRCode(
    version=16,
    box_size=10,
    border=5
    
)
data ='https://github.com/Sanjay1996383'
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill_color='red',black_color='green')
image.save('sanjay.png')