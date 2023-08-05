import requests
from bs4 import BeautifulSoup

class PackOne:
    def __init__(self):
        self.name = 'PackOne'

    def do(self):
        return 'My name is {}'.format(self.name)



class NyT:
    def __init__(self):
        self.name='NyT'
    def news(self):
        r=requests.get('https://www.nytimes.com/section/science')
        soup=BeautifulSoup(r.text,'html.parser')
        results=soup.find_all('h2',attrs={'class':'headline'})
        i=0
        while i<3:
            print(results[i].text)
            i+=1
