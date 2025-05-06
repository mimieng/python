from PIL import Image
img = Image.open('./OIP-C.jpg')
w,h = img.size
img1=img.crop(box=(0,0,w//2,h))
img2=img.crop(box=(w//2,0,w,h))
img1.show()
img2.show()