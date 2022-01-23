from PIL import Image, ImageEnhance
import os

def main():
    image, format = get_photo(input("Image path: "))
    tempt_image = set_tempt_photo(image)
    gray_image = grayify_photo(tempt_image)

    converter = ImageEnhance.Color(gray_image)
    image = converter.enhance(2.0)

    out = os.path.join(os.getcwd(), 'out')
    generated_img = open(os.path.join(out, 'out.png'), 'wb')
    image.save(generated_img, format)

def get_photo(path):
    image_path = os.path.abspath(path)
    image = Image.open(image_path)
    format = image.format
    return image, format

def grayify_photo(image):
    gray_image = image.convert("L")
    return gray_image

def set_tempt_photo(image):
    r, g, b = (255,137,18)
    matrix = ( r / 255.0, 0.0, 0.0, 0.0,
               0.0, g / 255.0, 0.0, 0.0,
               0.0, 0.0, b / 255.0, 0.0 )
    return image.convert('RGB', matrix)

if __name__ == '__main__':
    main()