from PIL import Image
img = Image.open('./OIP-C.jpg')
rotate_img=img.rotate(angle=45,translate=(100,0),expand=False,fillcolor=(255,0,0))
rotate_img.show()