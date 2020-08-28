from PIL import Image, ImageDraw, ImageFont
import qrcode
from PIL import Image, ImageDraw, ImageFont




def make_qr(qr):
    img = Image.open("template_level1.jpg")
    qr_coord = (338, 487)
    name_point_coords = (450, 1450)
    size = 571
    text_font = ImageFont.truetype("fonts/OpenSans-SemiBold.ttf", 100)
    qr_img = qrcode.make(qr[0], border=1)
    img.paste(qr_img, qr_coord)
    new_img = qr_img.resize((size, size), Image.ANTIALIAS)
    img.paste(new_img, qr_coord)
    draw = ImageDraw.Draw(img)
    if len(qr[1])>7:
        n=qr[1][0:7]
        draw.text(name_point_coords, n, "#FF0", font=text_font)
        img.save(f"results/new_qr{qr[1]}.png", "PNG")
    else:
        draw.text(name_point_coords, qr[1], "#FF0", font=text_font)
        img.save(f"results/new_qr{qr[1]}.png", "PNG")


qr_data = [
    ["http://www.asos.com/", "asos"],
    ["https://www.missguided.co.uk/", "missquided"],
    ["https://www.net-a-porter.com/ua/en/", "Net a Porter"],
    ["https://www.simplybe.co.uk/", "simplybe"],
    ["https://www.prettylittlething.com/", "prettylittlething"],
    ["http://www.rokit.co.uk/", "rokit"],
    ["http://www.boohoo.com/", "boohoo"],
    ["https://secretsales.com/", "secretsales"]

]
for qr in qr_data:
    make_qr(qr)
