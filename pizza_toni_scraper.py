#Guarda questo video https://www.youtube.com/watch?v=PaGp7Vi5gfM&ab_channel=PatrickLoeber
#Cosi puoi runnare questo codice su GitHub, inoltra elimina la pw per app da google e creane una nuova
#usandola per questo script. In questo modo tutto sarà più sicuro 

#Parsing HTML
#Tutorial Beautiful Soup: https://realpython.com/beautiful-soup-web-scraper-python/
import requests
from bs4 import BeautifulSoup
#Sending Email
# https://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python
import smtplib
from email.mime.text import MIMEText
import os

#Debug constants
PRINT_DEBUG = False #False -> Niente print di debug
SEND_EMAIL = True #False -> Non mandare email
#Email constants
GMAIL_USERNAME = "pizzeriatonitracker@gmail.com"
try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available"
    print("Token not available")
GMAIL_APP_PASSWORD = SOME_SECRET

URL = "https://dbuono.com/pizzeria-da-toni-pisa/prodotti/pizze/?products-per-page=all"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="content") #Funziona, ottengo la parte delle pizze
pizze_all = results.find_all("ul", class_="woo-product-info")

#Printa tutto il codice html di interesse
if PRINT_DEBUG == True:
    for pizza in pizze_all:
        print(pizza, end="\n" * 2)

#Scrivo i nuovi prezzi
new_prices = open('new_prices.txt', 'w', encoding='utf-8')
for pizza in pizze_all:
    title_pizza = pizza.find("li", class_="title")
    price_pizza = pizza.find("span", class_="price")
    #Printa tutte le pizze ed i relativi prezzi
    if PRINT_DEBUG == True:
        print("TITOLO:")
        print(title_pizza.text)
        print("PREZZO:")
        print(price_pizza.text)
        print()
    #Scrivo i nuovi prezzi in new_prices.txt
    new_prices.write(title_pizza.text)
    new_prices.write(': ')
    new_prices.write(price_pizza.text)
    new_prices.write('\n')
new_prices.close()

#Confronto con i vecchi prezzi
old_prices = open('old_prices.txt', 'r')
new_prices = open('new_prices.txt', 'r')
changed_prices = open('changed_prices.txt', 'w', newline='') #File in cui scrivo i prezzi cambiati, da inviare per mail. Non c'è '\n' alla fine della riga scritta

old_prices_data = old_prices.readlines()
new_prices_data  = new_prices.readlines()
i = 0
update = 0 #Se rimane a 0 non c'è bisogno di sovrascrivere old_prices, altrimenti devo sovrascriverlo con new_prices
for line1, line2 in zip(old_prices_data, new_prices_data):
    i += 1
    if line1 == line2:
        i = i #Do nothing
    else:
        if PRINT_DEBUG == True:
            print(f"Line {i}:")
            print(f"\tVecchio prezzo: {line1.strip()}")
            print(f"\tNuovo prezzo: {line2.strip()}")
        changed_prices.write("Vecchio prezzo: ")
        changed_prices.write(line1)
        changed_prices.write("Nuovo prezzo: ")
        changed_prices.write(line2)
        changed_prices.write('\n')
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

#Mando email
if update == 1: #Invio mail con il contenuto delle pizze cambiate di prezzo
    changed_prices_path = 'changed_prices.txt'

    with open(changed_prices_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_content = ''.join(lines)

    if PRINT_DEBUG == True:
        print(file_content)

    if SEND_EMAIL == True:
        recipients = ["loll77@hotmail.it", "alessandrozubani98@gmail.com"]
        msg = MIMEText(file_content)
        msg["Subject"] = "Prezzo delle pizze di Toni cambiato!!"
        msg["To"] = ", ".join(recipients)
        msg["From"] = f"{GMAIL_USERNAME}@gmail.com"
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
        smtp_server.sendmail(msg["From"], recipients, msg.as_string())
        smtp_server.quit()



