import pandas as pd
import os.path
import csv
from PIL import Image, ImageDraw, ImageFont

df = pd.read_csv("info.csv")
records = df.to_dict('records')

font = ImageFont.truetype("OpenSans-Semibold.ttf", size=45)
fonta = ImageFont.truetype("OpenSans-Semibold.ttf", size=40)
roll = ["Roll Numbers"]


def generate_card_front(data):
    templateFront = Image.open("template-front.png")
    if(os.path.exists(f"images/{data['Roll Number']}.jpg")):
        pic = Image.open(f"images/{data['Roll Number']}.jpg").resize((457, 571), Image.ANTIALIAS)
    else:
        pic = Image.open("209120007.jpg").resize((457, 571), Image.ANTIALIAS)
        roll.append(f"{data['Roll Number']}")

    #pic = Image.open(f"{data['Roll Number']}.jpg").resize((457, 571), Image.ANTIALIAS)
    templateFront.paste(pic.convert('RGB'), (2315, 297))
    draw = ImageDraw.Draw(templateFront)
    draw.text((410, 1400), str(data['rollnumber']), font=font, fill='black')
    draw.text((410, 1200), data['name'], font=font, fill='black')
    draw.text((410, 1550), data['branch'], font=font, fill='black')
    draw.text((410, 1700), data['batch'], font=font, fill='black')
    return templateFront.convert('RGB')


def generate_card_back(data):
    templateBack = Image.open("template-back.png")
    draw = ImageDraw.Draw(templateBack)
    draw.text((409, 104), str(data['Parents Name']), font=font, fill='black')
    draw.text((564, 321), data['Date of Birth'], font=font, fill='black')
    draw.text((564, 447), str(data['Blood Group']), font=font, fill='black')
    draw.text((564, 573), str(data['Student Contact No.']), font=font, fill='black')
    draw.text((564, 633), str(data['Mobile Number']), font=font, fill='black')
    draw.text((564, 816), data['Email'], font=font, fill='black')
    # draw.text((78, 1044), data['Home Address'], font=fonta, fill='black')
    # draw.text((78, 1124), data['city'], font=fonta, fill='black')
    # draw.text((78, 1204), data['state'], font=fonta, fill='black')
    # draw.text((78, 1284), data['addr'], font=fonta, fill='black')
    x = str(data['Home Adress']).split()
    draw.text((384, 989), x[0] + x[1] + x[2], font=font, fill='black')
    draw.text((384, 1089), x[3] + x[4] + x[5] + x[6], font=font, fill='black')
    draw.text((384, 1189), x[7] + x[8] + x[9] + x[10], font=font, fill='black')
    draw.text((384, 1289), x[11] + x[12] + x[13], font=font, fill='black')
    return templateBack.convert('RGB')


for record in records:
    card_front = generate_card_front(record)
    card_back = generate_card_back(record)
    card_front.save(f"newcards/{record['Roll Number']}_f.jpg")
    card_back.save(f"newcards/{record['Roll Number']}_b.jpg")
    with open('abcs.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(roll)
