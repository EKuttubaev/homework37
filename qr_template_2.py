import qrcode
from PIL import Image, ImageDraw, ImageFont

def make_qr(qr):
    img = Image.open("template_level2.png")
    qr_coord = (290, 120)
    point_1_coords = (40, 850)
    point_2_coords = (40, 900)
    point_3_coords = (40, 950)
    point_4_coords = (40, 1000)
    size = 430
    text_font = ImageFont.truetype("fonts/OpenSans-SemiBold.ttf", 50)
    qr_img = qrcode.make(qr[0], border=1)
    img.paste(qr_img, qr_coord)
    new_img = qr_img.resize((size, size), Image.ANTIALIAS)
    img.paste(new_img, qr_coord)
    draw = ImageDraw.Draw(img)
    # if len(qr[1])>7:
    #     n=qr[1][0:7]
    #     draw.text(name_point_coords, n, "#FF0", font=text_font)
    #     img.save(f"template_2_results/template_2{qr[1]}.png", "PNG")
    # else:
    #n=(f"Оплати {qr[1]}")
    draw.rectangle((40,860,300,910),fill="#FF0")
    draw.rectangle((40,915,350,960),fill="#FF0")
    draw.rectangle((40,965,200,1010),fill="#FF0")
    draw.rectangle((40,1015,300,1060),fill="#FF0")
    draw.text(point_1_coords, "Оплати в", "#000", font=text_font)
    draw.text(point_2_coords, qr[1], "#000", font=text_font)
    draw.text(point_3_coords, "через", "#000", font=text_font)
    draw.text(point_4_coords, "Balance!", "#000", font=text_font)
    img.save(f"template_2_results/template_2{qr[1]}.png", "PNG")


qr_data = [
    ["http://www.asos.com/", "asos"],
    ["https://www.missguided.co.uk/", "missquided"],
    ["https://www.net-a-porter.com/ua/en/", "ОNet a Porter"],
    ["https://www.simplybe.co.uk/", "Оsimplybe "],
    ["https://www.prettylittlething.com/", "Оprettylittlething"],
    ["http://www.rokit.co.uk/", "rokit"],
    ["http://www.boohoo.com/", "boohoo"],
    ["https://secretsales.com/", "secretsales"]

]
for qr in qr_data:
    make_qr(qr)
