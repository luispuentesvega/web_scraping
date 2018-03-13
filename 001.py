from bs4 import BeautifulSoup
import requests
page_link ='https://stackoverflow.com/questions/961632/converting-integer-to-string-in-python'
# fetch the content from url
page_response = requests.get(page_link, timeout=5)
print(page_response)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")

#Printing Head
print('-===========================>Printing Title of this page!')
print(page_content.title)

print('-===========================>Printing >a!')
print(str(page_content.a))


print('-===========================>Getting all a!')
#print(page_content.find_all('a'))

# extract all html elements where price is stored
#content = page_content.find_all(class_='main_price')
# prices has a form:
#[<div class="main_price">Price: $66.68</div>,
# <div class="main_price">Price: $56.68</div>]


f= open("amazon.txt","w+")
f.write(str(page_content.a))
f.close()