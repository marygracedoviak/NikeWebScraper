import time
import datetime
import requests
import smtplib
from bs4 import BeautifulSoup
import csv
import pandas as pd


def price_check():
    url = 'https://www.nike.com/t/dunk-high-womens-shoes-L3Tqlr/DD1869-103?nikemt=true&cp=38647199687_search_%7CPRODUCT_GROUP%7CGOOGLE%7C71700000101429394%7CGG_Evergreen_Shopping_Shoes_AllShoes%7C%7Cc&exp=2011&gclid=CjwKCAjwp6CkBhB_EiwAlQVyxXfFXjmymed9WWW2BC6PvU-fqa9_ycDBXt7Juz3fO39eV9mVTVvs8RoCKtgQAvD_BwE&gclsrc=aw.ds'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0"
    }

    page = requests.get(url, headers=headers)

    content = BeautifulSoup(page.content, 'html.parser')
    prettyContent = BeautifulSoup(content.prettify(), 'html.parser')

    title = prettyContent.find(id='pdp_product_title').get_text()
    price = prettyContent.find("div", {"data-test": "product-price"}).get_text()

    today = datetime.date.today()

    price = price.strip()[1:]
    title = title.strip()

    data = [title, price, today]

    with open('NikeScraper.csv', 'a+', newline='', encoding='UTF8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)

    if int(price) < 130:
        send_gmail()


def create_file():
    header = ['Title', 'Price', 'Date']

    with open('NikeScraper.csv', 'w', newline='', encoding='UTF8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)


def send_gmail():
    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    # info changed for privacy reasons
    s.login("sender_email", "password")

    subject = 'Price dropped!'

    body = 'You should buy now!'

    msg = f"Subject: {subject}\n\n{body}"

    # info changed for privacy reasons
    s.sendmail("sender_email", "receiver_email", msg)

    s.quit()


def check_file():
    df = pd.read_csv(r'C:\Users\maryg\NikeScraper.csv')
    print(df)


if __name__ == '__main__':
    # comment this out if you need to run the program more than once
    # otherwise it will create a new csv and overwrite the existing one
    create_file()

    # use if you need to check what the file currently looks like
    # otherwise can be commented out
    check_file()

    while True:
        price_check()
        time.sleep(86400)
