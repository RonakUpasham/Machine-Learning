#### Indian Express Sports News

import requests
from bs4 import BeautifulSoup
def Sports():
    for i in range(2,82):
        url = "https://indianexpress.com/section/sports/page/" +str(i)+'/'
        page_request = requests.get(url)
        data = page_request.content
        soup = BeautifulSoup(data,"html.parser")
        headlines=[]


        counter = 0
        for divtag in soup.find_all('div', {'class': 'articles'}):
            for h2tag in divtag.find_all('h2', {'class': 'title'}):
                if (counter <= 30):
                    counter = counter + 1
                    headlines.append(h2tag.find('a').contents[0]+'__'+'Sports'+'\n')


        f = open("DemoFile.txt", "a")
        f.writelines(headlines)
        f.close()

if __name__ == "__main__":
    Sports()

