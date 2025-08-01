#################################################################################################################
###QUESTO PEZZO FUNZIONA, TI PERMETTE DI SCRIVERE L'HTML DENTRO A samplehtml.html , una volta fatto commentalo###
#################################################################################################################
# Necessary imports
#import sys
#import urllib.request
#
## Save a reference to the original
## standard output
#original_stdout = sys.stdout
#
## as an example, taken my article list
## published link page and stored in local
##with urllib.request.urlopen('https://www.geeksforgeeks.org/user/priyarajtt/contributions/') as webPageResponse:
##with urllib.request.urlopen('https://dbuono.com/pizzeria-da-toni-pisa/prodotti/pizze/') as webPageResponse:
#with urllib.request.urlopen('https://dbuono.com/pizzeria-da-toni-pisa/prodotti/pizze/?products-per-page=all') as webPageResponse:
#    outputHtml = webPageResponse.read()
#
## Scraped contents are placed in 
## samplehtml.html file and getting
## used for next set of examples
#with open('samplehtml.html', 'w') as f:
#    
#    # Here the  standard output is 
#    # written to the file that we 
#    # used above
#    sys.stdout = f
#    print(outputHtml)
#    
#    # Reset the standard output to its 
#    # original value
#    sys.stdout = original_stdout

import requests
from bs4 import BeautifulSoup
import re

#Tutorial: https://realpython.com/beautiful-soup-web-scraper-python/

#Codice per tutorial 

#URL = "https://realpython.github.io/fake-jobs/"
#page = requests.get(URL)
#soup = BeautifulSoup(page.content, "html.parser")
#results = soup.find(id="ResultsContainer")
###print(results.prettify())
#job_cards = results.find_all("div", class_="card-content")
##for job_card in job_cards:
##    print(job_card, end="\n" * 2)
#for job_card in job_cards:
#    title_element = job_card.find("h2", class_="title")
#    company_element = job_card.find("h3", class_="company")
#    location_element = job_card.find("p", class_="location")
#    print(title_element.text)
#    print(company_element.text)
#    print(location_element.text)
#    print()



#Codice per Toni

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

for pizza in pizze_all:
    title_pizza = pizza.find("li", class_="title")
    price_pizza = pizza.find("span", class_="price")
    print("TITOLO:")
#    print(title_pizza)
    print(title_pizza.text)
    print("PREZZO:")
#    print(price_pizza)
    print(price_pizza.text)
    print()

#Fino a qua funziona, stampa tutte le pizze ed i relativi prezzi. Ora devi fare in modo che
#Le pizze con i prezzi vengano salvate in un file NEW e confrontate con quelle che sono già dentro ad un file OLD
#E poi mostri quali cambiano valore!! 