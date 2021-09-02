import pyqrcode

data='www.youtube.com/ajaynair'

qrimage=pyqrcode.create(data)

qrimage.png('ytt.png', scale=10)