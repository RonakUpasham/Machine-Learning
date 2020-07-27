#Business Standard Politics News

#https://www.business-standard.com/category/politics-news-north-1550102.htm/ - North Politcs
#https://www.business-standard.com/category/politics-news-south-1550103.htm/ - South Politics
#https://www.business-standard.com/category/politics-news-east-1550104.htm/  - East Politics
#https://www.business-standard.com/category/politics-news-west-1550105.htm/  - West Politics

import requests
from bs4 import BeautifulSoup
def politics():
    for i in range(2,27):
        url = "https://www.business-standard.com/category/politics-news-north-1550102.htm/"+str(i)
        page_request = requests.get(url)
        data = page_request.content
        soup = BeautifulSoup(data,"html.parser")
        headlines=[]


        counter = 0
        for litag in soup.find_all('li'):
            for h2tag in litag.find_all('h2'):
                if (counter <= 30):
                    counter = counter + 1
                    headlines.append(h2tag.find('a').contents[0]+'__'+'Politics'+'\n')


        f = open("DemoFile.txt", "a")
        f.writelines(headlines)
        f.close()
    
if __name__ == "__main__":
    politics()
