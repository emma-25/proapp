import pyqrcode
import png
from PIL import Image
s = "http://127.0.0.1:8000/visita/"
url = pyqrcode.create(s)
img = "visita.png"
url.png(img, scale=10)
#opening image
im=Image.open(img)
im.show()