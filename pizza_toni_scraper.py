#import requests
#from bs4 import BeautifulSoup
#from urllib.request import urlopen
#import re
#
#
#HEADERS = {
#    "User-Agent": (
#        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#        "AppleWebKit/537.36 (KHTML, like Gecko) "
#        "Chrome/114.0.0.0 Safari/537.36"
#    ),
#    "Accept-Language": "it-IT,it;q=0.9"
#}
#
#product_url = "https://dbuono.com/pizzeria-da-toni-pisa/prodotti/pizze/"
#response = requests.get(product_url, headers=HEADERS, timeout=10)
#soup = BeautifulSoup(response.content, "html.parser")

# Necessary imports
import sys
import urllib.request

# Save a reference to the original
# standard output
original_stdout = sys.stdout

# as an example, taken my article list
# published link page and stored in local
#with urllib.request.urlopen('https://www.geeksforgeeks.org/user/priyarajtt/contributions/') as webPageResponse:
#with urllib.request.urlopen('https://dbuono.com/pizzeria-da-toni-pisa/prodotti/pizze/') as webPageResponse:
with urllib.request.urlopen('https://dbuono.com/pizzeria-da-toni-pisa/prodotti/pizze/?products-per-page=all') as webPageResponse:
    outputHtml = webPageResponse.read()

# Scraped contents are placed in 
# samplehtml.html file and getting
# used for next set of examples
with open('samplehtml.html', 'w') as f:
    
    # Here the  standard output is 
    # written to the file that we 
    # used above
    sys.stdout = f
    print(outputHtml)
    
    # Reset the standard output to its 
    # original value
    sys.stdout = original_stdout