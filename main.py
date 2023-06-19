#Scraping the product page
import requests
url= "https://www.amazon.com/adidas-Inter-Miami-Authentic-Jersey/dp/B09WW3P26N/ref=sr_1_4?keywords=inter%2Bmiami%2Bjersey&qid=1687135902&sprefix=Inter%2Bmiami%2B%2Caps%2C252&sr=8-4&th=1&psc=1"
headers= {
    "User-Agent":"User-Agent:",
    "Accept-Language":"en-US,en;q=0.9,es;q=0.8"
}
response=requests.get(url,headers=headers)
html=response.text

#Creating a soup with the html to look for the price
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

prettified_html = soup.prettify()
with open("html.text","w", encoding='utf-8') as file:
    file.write(prettified_html)

price= soup.find(name="span", class_="a-offscreen").get_text()
price_float= float(price.split("$")[1])
print(price_float)


#Sending a mail when there is a good deal
import smtplib
my_email = "fake.mail123@gmail.com" #your email
# app password from gmail after 2-step vertification, category: Other(custom).
my_password = "abcd123"
#USE ENVIRONMENT VARIABLES when using public code.

product="Inter Miami's shirt"
target_price= 100

if price_float < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addrs=my_email,
            to_addrs=my_email,
            msg=f"Subject: {product} is at a really good price!\n\n Price today is {price_float}$ check it today in Amazon at {url}")
else:
    pass


