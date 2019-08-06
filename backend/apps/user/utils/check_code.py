from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import randint, choice


def rnd_char():
    """get random digits, alphabets"""
    return chr(choice([randint(48, 57), randint(65, 90), randint(97, 122)]))


def rnd_color():
    """get random color"""
    return randint(64, 255), randint(64, 255), randint(64, 255)


def ran_color2():
    """get random color"""
    return randint(32, 127), randint(32, 127), randint(32, 127)


class CheckCode(object):

    @staticmethod
    def get_check_code_pict():
        num = 5  # number of check code
        width = 50 * num  # width of image
        height = 60  # height of image
        image = Image.new('RGB', (width, height), (255, 255, 255))

        # set Font instance, .tff is font file, can switch it
        font = ImageFont.truetype('arial.ttf', 50)
        # set Draw instance
        draw = ImageDraw.Draw(image)
        # pad every pixels
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=rnd_color())
        # generate code
        code = ""
        for k in range(num):
            temp = rnd_char()
            draw.text((50 * k + randint(1, 10), randint(0, 5)), temp, font=font, fill=ran_color2())
            code += temp
        # blur the image
        image = image.filter(ImageFilter.GaussianBlur)

        return image, code
