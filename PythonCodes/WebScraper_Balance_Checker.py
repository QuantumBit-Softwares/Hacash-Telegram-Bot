#scrape.py
# 1. All websites are basically HTML/CSS and javascript
# 2. We can use python to find whatever tags we are looking for.
# 3. For pages that use a lot of javascript, we can  use web drivers instead to make the calls
#https://towardsdatascience.com/how-to-scrape-any-website-with-python-and-beautiful-soup-bc84e95a3483

import requests
from bs4 import BeautifulSoup

i=1
address_input = input("Enter your HAC address: ")
url = ("http://block.hacash.org/address/"+address_input)
result = requests.get(url)
#print(result.content)
src = result.content
soup = BeautifulSoup(src, 'lxml')
soup.find('p')

contents= soup.findAll('p')
for x in contents:
	if i == 1:
		hac_address = x.text
	if i == 2:
		hac_balance = x.text
	if i == 3:
		hacd_balance = x.text
	i = i+1
	if i==4:
		break
	
#string/s to be removed
r_items=["Index/Address"]
hac_address_real = [x for x in hac_address.split() if x not in r_items]
hac_address_real1 = ' '.join(hac_address_real)
hac_address_real2 = 'Address '+hac_address_real1

print(hac_address_real2)
print(hac_balance)
print(hacd_balance)

