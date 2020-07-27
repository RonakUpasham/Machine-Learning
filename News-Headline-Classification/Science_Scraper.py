#### India Today Science News

import requests
from bs4 import BeautifulSoup
def science():
    for i in range(1,169):
        url = "https://www.indiatoday.in/science?page="+str(i) 
        page_request = requests.get(url)
        data = page_request.content
        soup = BeautifulSoup(data,"html.parser")
        headlines=[]


        counter = 0
        for divtag in soup.find_all('div', {'class': 'catagory-listing'}):
            for divtag1 in divtag.find_all('div', {'class': 'detail'}):
                for h2tag in divtag1.find_all('h2'):
                    if (counter <= 30):
                        counter = counter + 1
                        headlines.append(h2tag.find('a').contents[0]+'__'+'Science'+'\n')


        f = open("DemoFile.txt", "a")
        f.writelines(headlines)
        f.close()
    
if __name__ == "__main__":
    science()

