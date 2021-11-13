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
    templateFront.paste(pic.convert('RGB'), (447, 572))
    draw = ImageDraw.Draw(templateFront)
    draw.text((602, 1371), str(data['Roll Number']), font=fonta, fill='black')
    draw.text((602, 1239), data['Name'], font=fonta, fill='black')
    draw.text((602, 1492), data['Specialization'], font=fonta, fill='black')
    draw.text((602, 1632), data['Batch(year)'], font=fonta, fill='black')
    return templateFront.convert('RGB')


def generate_card_back(data):
    templateBack = Image.open("template-back.png")
    draw = ImageDraw.Draw(templateBack)
    draw.text((564, 104), str(data['Parents Name']), font=fonta, fill='black')
    draw.text((564, 321), data['Date of Birth'], font=fonta, fill='black')
    draw.text((564, 447), str(data['Blood Group']), font=fonta, fill='black')
    draw.text((564, 573), str(data['Student Contact No.']), font=fonta, fill='black')
    draw.text((564, 633), str(data['Mobile Number']), font=fonta, fill='black')
    draw.text((564, 816), data['Email'], font=fonta, fill='black')
    draw.text((78, 1044), data['Home Address'], font=fonta, fill='black')
    draw.text((78, 1124), data['city'], font=fonta, fill='black')
    draw.text((78, 1204), data['state'], font=fonta, fill='black')
    draw.text((78, 1284), data['addr'], font=fonta, fill='black')
    return templateBack.convert('RGB')


for record in records:
    card_front = generate_card_front(record)
    card_back = generate_card_back(record)
    card_front.save(f"newcards/{record['Roll Number']}_f.jpg")
    card_back.save(f"newcards/{record['Roll Number']}_b.jpg")
    with open('abcs.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(roll)
