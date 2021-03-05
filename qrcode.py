import pyqrcode, colored

# Input Url for creating QR-code
url = input("Enter the URL :")

#creating QR 
qrcode_ = pyqrcode.create(url, error="L", version=4)
qrcode_.png("QR-code.png", scale=20, module_color=[0, 0, 0], background=[90, 255, 163])
qrcode_.show()