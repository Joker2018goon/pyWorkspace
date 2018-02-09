from urllib2 import urlopen,HTTPError,URLError
from bs4 import BeautifulSoup

def get_title(url):
    try:
        html=urlopen(url)
    except (HTTPError,URLError) as e:
        return None

    try:
        bsobj=BeautifulSoup(html.read(),'html.parser')
        title=bsobj.body.h1
    except AttributeError as e:
        return None
    return title

title=get_title('http://www.pythonscraping.com/pages/page1.html')
if title ==None:
    print('title could not be found')
else:
    print(title)