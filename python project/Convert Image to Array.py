from PIL import Image
image = Image.open('clock.png')
from numpy import asarray
data = asarray(image)
print(data)