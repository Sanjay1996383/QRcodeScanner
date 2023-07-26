import QRcode as qr
image= qr.make("https://www.youtube.com/watch?v=RFAQ1YmJz-k")
image.save('Text.png')