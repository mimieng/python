from PIL import Image
img = Image.open('./OIP-C.jpg')
# png轉jpg需要轉換格式
# img=img.convert('RGB')
img.save('景色.jpg')