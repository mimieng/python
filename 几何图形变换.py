from PIL import Image
img=Image.open('./OIP-C.jpg')
img.show()
transpose_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transpose_img.show()