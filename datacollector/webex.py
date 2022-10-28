from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url="http://olympus.realpython.org/profiles/aphrodite"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
soup = BeautifulSoup(webpage, 'html.parser')

filee=open(r'gogohtml.txt','w')
tow=soup.prettify()
filee.write(tow)