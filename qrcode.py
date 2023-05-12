#importing all the libraries
import png, pyqrcode

#link for my instagram account
link = input('Enter the link here: ')

#creatng qr code
code = pyqrcode.create(link)

#saving it to desktop
code.png('QR Code.png', scale = 8)
