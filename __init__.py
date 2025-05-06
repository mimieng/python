import numpy as np
from PIL import Image
img=Image.open(r'./OIP-C.jpg')
print(img.size)
print(img.mode)
imgData=np.array(img)
print(imgData)
img.show()