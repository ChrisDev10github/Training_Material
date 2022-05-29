from bs4 import BeautifulSoup
import requests

def getHTML(url):
    response = requests.get(url)
    return response.text

import requests
response = requests.get("http://books.toscrape.com/")
print(response)


html = getHTML("http://books.toscrape.com/")
soup = BeautifulSoup(html,'html.parser')

table = soup.find_all('h3',attrs = {'class':'main-table'})
books=[]

#showcase = html_soup.find_all(tag,class)       tag,attribute,class 
#use find_all  or could use select instead of find all
#for loop

for row in table.find_all_next('li'):
    cells = row.find_all_next('p')
    book = {}
    book['name'] = cells[0].string    
    #countrycodes = cells[2].string
    #book['iso-2'] = countrycodes.split('/')[0]
    #book['iso-3'] = countrycodes.split('/')[1]
    books.append(book)

#h3 tags

