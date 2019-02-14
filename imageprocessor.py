import code
from PIL import Image

def rotate_box(an_image):
    box = (100,100,400,400)
    region = an_image.crop(box)
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed, box)
    return an_image


code.open_rotate_save("C:\\Users\\Joergson\\Desktop\\pictures")

print("---->  fertig  <----")


