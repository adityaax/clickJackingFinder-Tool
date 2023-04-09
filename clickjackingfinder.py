import bs4
import urllib
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.request import Request

domain=input('enter target domain (eg. example.com): ')

req = Request(url='https://securityheaders.com/?q={}&followRedirects=on'.format(domain),headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = bs(webpage, 'html.parser').get_text()

def function(x):
    if x in soup.strip():
        print("{} is vulnerable to clickjacking attack ".format(domain))
    else:
        print("{} is not vulnerable to clickjacking attack ".format(domain))

function("X-Frame-OptionsX-Frame-Options tells the browser whether you want to allow your site to be framed or not.")
