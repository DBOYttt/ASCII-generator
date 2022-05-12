from distutils.dep_util import newer_pairwise
from importlib.resources import path
import PIL.Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width = 100):
        width, height = image.size
        ratio = height / width
        new_height = int(new_width * ratio)
        resize_image = image.resize((new_width, new_height))
        return(resize_image)

def grayify(image):
    grayscale_image = image.convert('L')
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ASCII_CHARS[pixel//2] for pixel in pixels])
    return(characters)

def main(new_width = 100):
    path = input('Enter the path to the image fiel : \n')

    try:
        image = PIL.Image.open(path)
    except:
        print(path, 'Unable to find image')

    new_image_data = pixels_to_ascii(grayify(resize(image)))

    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count))

    print(ascii_image)
main()