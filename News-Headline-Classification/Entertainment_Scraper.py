#### Indian Express Entertainment News

import requests
from bs4 import BeautifulSoup
def entertainment():
    for i in range(2,82):
        url = "https://indianexpress.com/section/entertainment/page/" +str(i)+'/' 
        page_request = requests.get(url)
        data = page_request.content
        soup = BeautifulSoup(data,"html.parser")
        headlines=[]


        counter = 0
        for divtag in soup.find_all('div', {'class': 'title'}):
            if (counter <= 30):
                counter = counter + 1
                headlines.append(divtag.find('a').contents[0]+'__'+'Entertainment'+'\n')


        f = open("DemoFile.txt", "a")
        f.writelines(headlines)
        f.close()
    
if __name__ == "__main__":
    entertainment()
