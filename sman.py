from PIL import Image, ImageFont, ImageDraw
import os

class Generator:
    def __init__(self):
        self.ask_for_input()
        self.resize_img()

    def ask_for_input(self):
        self.name = input("What's ur name \n")
        self.position = input("What's ur position \n")
        self.branch = input("Your branch \n")

    def resize_img(self):
        img_path = os.path.join(os.path.realpath("."), "img.png")
        img_obj = Image.open(img_path)
        
        scalar = 3

        img_obj = img_obj.resize((int(img_obj.width / scalar), int(img_obj.height / scalar)))

        img_height, img_width = img_obj.size

        pic_path = os.path.join(os.path.realpath("."), "pic.jpg")
        pic_obj = Image.open(pic_path)

        pic_obj = pic_obj.resize((110 , 142))
        pic_width, pic_height = pic_obj.size 

        img_text = ImageDraw.Draw(img_obj)

        arialFont = ImageFont.truetype(os.path.join(os.path.realpath("."), 'ARLRDBD.ttf'), 12)

        gap = 25 

        img_text.text((130 - 2, (92 + (gap * 0))), f'{self.name}', fill='black', font=arialFont)
        img_text.text((145 - 2, (92 + (gap * 1))), f'{self.position}', fill='black', font=arialFont)
        img_text.text((140 - 2, (92 + (gap * 2))), f'{self.branch}', fill='black', font=arialFont)

        # Signature
        smallArialFont = ImageFont.truetype(os.path.join(os.path.realpath("."), 'ARLRDBD.ttf'), 7)
        img_text.text((10, (215)), f'Get your ID Card on africonn.com/sman ', fill='black', font=smallArialFont)
        img_obj.paste(pic_obj, (img_width - (pic_width - 127), img_height - (pic_height + 157)))
        img_obj.save(f"{self.name}'s_id_card.png")
        
# Instantiate the class
Generator()

