# import libraries
import requests
from lxml import html
from bs4 import BeautifulSoup

# specify url
address = 'https://swgoh.gg/u/smurkcity12/mods/'

# query website and return the html to the variable page
response = requests.get(address)
html = response.text
# tree = html.fromstring(page.content)


# collection_mod = tree.xpath()

# BS testing
soup = BeautifulSoup(html, "lxml")
head_tag = soup.head
body_tag = soup.body
# for child in head.descendents:
#     print(child)
content_container = soup.find("div",{"class": "content-container"})
mod_list = content_container.find("div",{"class": "content-container-primary mod-list"})
# print(mod_list)
last_update = mod_list.find("div", {"class": "user-last-updated text-muted"})
print(last_update)
print(last_update.contents)
print(last_update.contents[1])
for child in last_update.children:
    print(child)
# print(soup.prettify())
# print(soup.head)
# print(soup.title)


# Take out the div of name and get its value
# name_box = soup.find('h1', attrs={'class': 'collection-mod'})
# print(name_box.text)
# name = name_box.text.strip() # strip is used to remove starting and trailing
# print(name)