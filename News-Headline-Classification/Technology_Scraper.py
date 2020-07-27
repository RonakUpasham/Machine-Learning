#### Gadgets Now Technology News

import requests
from bs4 import BeautifulSoup
def technology():
    for i in range(2,102):
        url = "https://www.gadgetsnow.com/tech-news/" +str(i)     
        page_request = requests.get(url)
        data = page_request.content
        soup = BeautifulSoup(data,"html.parser")
        headlines=[]


        counter = 0
        for divtag in soup.find_all('div', {'class': 'tech_list ctn_stories'}):
            for ultag in divtag.find_all('ul', {'class': 'cvs_wdt'}):
                for litag in ultag.find_all('li'):
                    if (counter <= 30):
                        counter = counter + 1
                        headlines.append(litag.find('a')['title']+'__'+'Technology'+'\n')


        f = open("DemoFile.txt", "a")
        f.writelines(headlines)
        f.close()

    
if __name__ == "__main__":
    technology()

