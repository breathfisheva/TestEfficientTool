from PIL import Image
from PIL import ImageChops


def compare_image(image1_path, image2_path):
    image_one = Image.open(image1_path)
    image_two = Image.open(image2_path)

    try:
        diff = ImageChops.difference(image_one, image_two)
        if diff.getbbox() is None:
            print("we are same")
        else:
            diff.show()
            print("%s and %s is differnt value is %s" % (image1_path, image2_path, diff.getbbox()))
            diff.save(r'./different/diff.png')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    compare_image('./QA/IEstest140400center_socn.png', './UAT/IEstest56049center_socn.png')


