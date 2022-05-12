import PIL.Image

def main():
    x = input('Enter the path to the image fiel : \n')

    try:
        image = PIL.Image.open(x)
    except:
        print(x, 'Unable to find image');
main()
