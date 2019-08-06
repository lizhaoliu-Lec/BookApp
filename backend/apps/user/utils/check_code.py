from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import randint, choice


# 随机ASCII码生成数字或大小写字母
def rnd_char():
    return chr(choice([randint(48, 57), randint(65, 90), randint(97, 122)]))


# 背景颜色
def rnd_color():
    return randint(64, 255), randint(64, 255), randint(64, 255)


# 验证码颜色
def ran_color2():
    return randint(32, 127), randint(32, 127), randint(32, 127)


class CheckCode:

    # 生成验证码图片
    @staticmethod
    def getCheckCodePict():
        num = 5  # 生成num位的验证码
        width = 50 * num  # 图宽
        height = 60  # 图高
        image = Image.new('RGB', (width, height), (255, 255, 255))

        # 创建Font对象 .tff为字体文件 可自定义
        font = ImageFont.truetype('arial.ttf', 50)
        # 创建Draw对象
        draw = ImageDraw.Draw(image)
        # 填充每个像素
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=rnd_color())
        # 生成验证码
        code = ""
        for k in range(num):
            temp = rnd_char()
            draw.text((50 * k + randint(1, 10), randint(0, 5)), temp, font=font, fill=ran_color2())
            code += temp
        # 对图片进行模糊处理
        image = image.filter(ImageFilter.GaussianBlur)

        return image, code
