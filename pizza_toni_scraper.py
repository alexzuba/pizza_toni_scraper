import requests
from bs4 import BeautifulSoup
import re

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

#Tutorial Beautiful Soup: https://realpython.com/beautiful-soup-web-scraper-python/


#Codice per Toni

GMAIL_USERNAME = "pizzeriatonitracker@gmail.com"
GMAIL_APP_PASSWORD = "vvxcqbaxfvklzxik"

URL = "https://dbuono.com/pizzeria-da-toni-pisa/prodotti/pizze/?products-per-page=all"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="content") #Funziona, ottengo la parte delle pizze
#print(results.prettify())
#print(results)
pizze_all = results.find_all("ul", class_="woo-product-info")

##FINO A QUA FUNZIONA
#for pizza in pizze_all:
#    print(pizza, end="\n" * 2)

#Scrivo i nuovi prezzi
#new_prices = open('new_prices.txt', 'w')
new_prices = open('new_prices.txt', 'w', encoding='utf-8')

for pizza in pizze_all:
    title_pizza = pizza.find("li", class_="title")
    price_pizza = pizza.find("span", class_="price")
#    print("TITOLO:")
#    print(title_pizza.text)
#    print("PREZZO:")
#    print(price_pizza.text)
#    print()
    #Scrivo i nuovi prezzi in new_prices.txt
    new_prices.write(title_pizza.text)
    #new_prices.write('\n')
    new_prices.write(': ')
    new_prices.write(price_pizza.text)
    new_prices.write('\n')

new_prices.close()

#Confronto con i vecchi prezzi
old_prices = open('old_prices.txt', 'r')
new_prices = open('new_prices.txt', 'r')
changed_prices = open('changed_prices.txt', 'w') #File in cui scrivo i prezzi cambiati, da inviare per mail

old_prices_data = old_prices.readlines()
new_prices_data  = new_prices.readlines()

i = 0
update = 0 #Se rimane a 0 non c'è bisogno di sovrascrivere old_prices, altrimenti devo sovrascriverlo con new_prices
for line1, line2 in zip(old_prices_data, new_prices_data):
    i += 1
    if line1 == line2:
        #print(f"Line {i}: IDENTICAL")
        i = i
    else:
        print(f"Line {i}:")
        print(f"\tVecchio prezzo: {line1.strip()}")
        print(f"\tNuovo prezzo: {line2.strip()}")
        changed_prices.write(line2)
        update = 1

old_prices.close()
new_prices.close()
changed_prices.close()

#Sovrascrivo old_prices se new_prices /= old_prices 
if update == 1:
    i = 0
    old_prices = open('old_prices.txt', 'w')
    new_prices = open('new_prices.txt', 'r')
    for line in new_prices:
        i += 1
        old_prices.write(line)

old_prices.close()
new_prices.close()


#Mandare email:
# https://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python

if update == 1: #Invio mail con il contenuto delle pizze cambiate di prezzo
    changed_prices_path = 'changed_prices.txt'

    with open(changed_prices_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_content = ''.join(lines)

#    print(file_content)

    recipients = ["loll77@hotmail.it"]
    msg = MIMEText(file_content)
    msg["Subject"] = "Prezzo delle pizze di Toni cambiato!!"
    msg["To"] = ", ".join(recipients)
    msg["From"] = f"{GMAIL_USERNAME}@gmail.com"

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
    smtp_server.sendmail(msg["From"], recipients, msg.as_string())
    smtp_server.quit()


#Miglioramenti: Quando invia la mail, non mandare soltanto il nuovo prezzo, ma anche quello vecchio



