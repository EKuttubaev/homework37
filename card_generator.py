from PIL import Image, ImageFont, ImageDraw


def text_from_rigth(draw: ImageDraw, font: ImageFont, text, color, coords):
    text_width, text_height = font.getsize(text)
    coords = (coords[0] - text_width, coords[1])
    draw.text(coords, text, fill=color, font=font)


def text_from_left(draw: ImageDraw, font: ImageFont, text, color, coords):
    coords = (coords[0], coords[1])
    draw.text(coords, text, fill=color, font=font)


def make_and_save_card(person):
    template = Image.open("level0_template.jpg")
    name_font = ImageFont.truetype("fonts/OpenSans-Light.ttf", 50)
    surname_font = ImageFont.truetype("fonts/OpenSans-SemiBold.ttf", 50)
    position_font = ImageFont.truetype("fonts/OpenSans-SemiBold.ttf", 20)
    other_inf_font = ImageFont.truetype("fonts/OpenSans-semiBold.ttf", 25)
    name_coords = (555, 265)
    surname_coords = (555, 336)
    position_coords = (555, 413)
    mail_coords = (770, 240)
    phone_coords=(770,320)
    adress_coords=(770,410)
    web_page_coords=(770,495)
    draw = ImageDraw.Draw(template)

    text_from_rigth(draw, name_font, person[0].upper(), "#FFF", name_coords)
    text_from_rigth(draw, surname_font, person[1].upper(), "#FFF", surname_coords)
    text_from_rigth(draw, position_font, person[2].upper(), "#F00", position_coords)
    text_from_left(draw,other_inf_font,person[3].upper(),"#FFF",mail_coords)
    text_from_left(draw,other_inf_font,person[4].upper(),"#FFF",phone_coords)
    text_from_left(draw,other_inf_font,person[5].upper(),"#FFF",adress_coords)
    text_from_left(draw,other_inf_font,person[6].upper(),"#FFF",web_page_coords)

    template.save(f"results/card_{person[0]}_{person[1]}.png", "PNG")


persons = [
    ["Alisher", "Alikulov", "Software Developer", "masteraalish@gmail.com", "+996 776 900 413", "Kyrgyzstan, Bishkek",
     "www.master.com"],
    ["Isaac", "Asimov", "Writer", "isaacaazimov@gmail.com", "+996 706 900 413", "USA, Manhattan, New York city",
     "www.asimov.fb"],
    ["George", "Lucas", "Film producer", "gorge@lucasfilm.com", "+8 79938 38837", "USA, California", "lucasfilm.com"],
]

for person in persons:
    make_and_save_card(person)
