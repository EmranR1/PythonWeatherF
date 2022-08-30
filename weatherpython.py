#weather report
#importing BeautifulSoup library
from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def weather(city):
    city=city.replace(" ","+")
    res=requests.get(f'https://www.google.com/search?q={city}&oq={city}'
    f'&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid='
    f'chrome&ie=UTF-8',headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')