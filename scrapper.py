import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/MSI-GS65-Stealth-005-i7-8750H-Diamond/dp/B07M64JB6D/ref=sr_1_2_sspa?crid=32UUB0TTS8QE6&keywords=msi+laptop+2080&qid=1567481843&s=electronics&sprefix=MSI+lap%2Celectronics%2C155&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE5Vk0yUTNBNlRGQ1kmZW5jcnlwdGVkSWQ9QTA4OTc4MDkyRk9CS09QOVo3NE0mZW5jcnlwdGVkQWRJZD1BMDA2OTc2OTFRRjhVWjRDTFZSSTImd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="producTitle")
    title = title.get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if (converted_price > 1.700):
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server = ehlo()
    server.starttls()
    server.ehlo()

    server.login('metayer.jhonston@gmail.com', 'weyhrufuwwclrlde')

    subject = 'price went down!'
    body = 'Check the amazon link https://www.amazon.com/MSI-GS65-Stealth-005-i7-8750H-Diamond/dp/B07M64JB6D/ref=sr_1_2_sspa?crid=32UUB0TTS8QE6&keywords=msi+laptop+2080&qid=1567486039&s=electronics&sprefix=MSI+lap%2Celectronics%2C155&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMzNLQkk0SlBFUjYxJmVuY3J5cHRlZElkPUEwNTU0NDE0U1QwSFBSWFRBOEE1JmVuY3J5cHRlZEFkSWQ9QTAwNjk3NjkxUUY4VVo0Q0xWUkkyJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ== '

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'bruce.leeroy@gmail.com',
        'leeroy.bruce@gmail.com',
        msg
    )

    print('HEY CHECK YOUR EMAIL!')

    server.quit()


check_price()
