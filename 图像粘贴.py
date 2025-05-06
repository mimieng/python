from PIL import Image

img=Image.open('./OIP-C.jpg')
img1=Image.open('./景色.jpg')
s=img.resize((200,200))
img.paste(s,box=(100,100,300,300))
img.show()
