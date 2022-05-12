from importlib.resources import path
import PIL.Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width = 100):
        width, height = image.size
        ratio = height / width
        new_height = int(new_width * ratio)
        resize_image = image.resize((new_width, new_height))
        return(resize_image)



def main():
    path = input('Enter the path to the image fiel : \n')

    try:
        image = PIL.Image.open(path)
    except:
        print(path, 'Unable to find image')




    image = resize(image);

    def to_greyscale(image):
        return image.convert("L")
    to_greyscale()

    greyscale_image = to_greyscale(image)

    def pixel_to_ascii(image):
        pixels = image.getdata()
        ascii_str = "";
        for pixel in pixels:
            ascii_str += ASCII_CHARS[pixel//25];
        return ascii_str
    pixel_to_ascii()

    ascii_str = pixel_to_ascii(greyscale_image)

    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img);
main()