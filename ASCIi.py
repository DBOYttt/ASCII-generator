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

def main():
    path = input('Enter the path to the image fiel : \n')

    try:
        image = PIL.Image.open(path)
    except:
        print(path, 'Unable to find image')
main()