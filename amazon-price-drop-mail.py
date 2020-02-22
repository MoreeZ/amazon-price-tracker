import requests
from bs4 import BeautifulSoup
import smtplib
import json
import time

# The amazon link of the item that you want to watch
URL = "https://www.amazon.co.uk/ASUS-GeForce-Enthusiast-Level-Technology-ROG-STRIX-RTX2080TI-O11G/dp/B07HNMT91C/ref=sr_1_2?crid=W4293JGO9S0M&keywords=gtx+2080ti&qid=1582286111&sprefix=gtx+2%2Caps%2C168&sr=8-2"

# Your browser user agent (varies)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
price = soup.find(id="priceblock_ourprice").get_text().strip()
title = soup.find(id="productTitle").get_text().strip()
formatedPrice = float(price.replace("£", "").replace(",", ""))


def sendMail():
    # password dgzegizxvcycespq
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YOUR_GMAIL', 'GMAIL_APP_PASSWORD')

    subject = "Price fell down!"
    body = f'check the amazon link {URL}\nItem "{title} now costs {price}"'
    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'YOUR_GMAIL',  # From
        'RECIPIENT_EMAIL',  # To
        msg  # message
    )


# Checks every 12 hours
while True:
    if(formatedPrice < 1000):
        sendMail()
        quit()
    time.sleep(43200)
