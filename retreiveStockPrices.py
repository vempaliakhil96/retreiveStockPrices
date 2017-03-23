# retreiveStockPrices.py
import urllib
import re
stockName = str(raw_input('Enter name of stock\n'))
stockNameUpper=stockName.upper()
print stockNameUpper
url = 'https://www.google.com/finance?q=NASDAQ:'+stockNameUpper
# print url
data = urllib.urlopen(url, 'lxml')
htmltext = data.read()
file = open('stockprice.xml', 'w')
file.write(htmltext)
regex = '<span class=\"pr\">\n<span id=\"(.+?)\">(.+?)</span>\n</span>'
pattern = re.compile(regex)
price = re.findall(pattern, htmltext)
print 'Current price of '+stockNameUpper+' is: '+ str(price[-1][-1])

	
