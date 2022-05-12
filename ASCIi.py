import PIL.Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def main():
    x = input('Enter the path to the image fiel : \n')

    try:
        image = PIL.Image.open(x)
    except:
        print(x, 'Unable to find image')
main()

def resize(image, new_width = 100):
    width, height = image.size
    new_height = new_width * height / width
    return image.resize((new_width, new_height))
resize()

def to_greyscale(image):
    return image.convert("L")
to_greyscale()

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "";
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25];
    return ascii_str
pixel_to_ascii()