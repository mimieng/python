from PIL import Image
img = Image.open('./OIP-C.jpg')
# img1=img.resize((100,100))
# 整体缩放
img1=img.resize(size=(100,100),box=(0,0,100,100))
# （0,0）->（100,100）
img1.save('图片缩放.jpg')
img1.show()