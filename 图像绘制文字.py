from PIL import Image, ImageFont
from PIL import  ImageDraw
img=Image.open('./OIP-C.jpg')
draw = ImageDraw.Draw(img)
font=ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc",40)
draw.text((100,100),'你好',fill='red',font=font)
img.show()