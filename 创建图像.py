import numpy as np
from PIL import Image
# image=Image.new('RGB', (100, 100), 'white')
# image.show()

image=np.array([[[255,0,0]]], dtype=np.uint8)
image=Image.fromarray(image)
image.show()
