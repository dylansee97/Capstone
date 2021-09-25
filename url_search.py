from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

root = "https://google.com/"
link = "https://www.google.com/search?q=donald+trump&sxsrf=ALeKk01K1bOuJFHjy4HBARo1cRpUYakYPg:1629640327633&source=lnms&tbm=nws&sa=X&sqi=2&ved=2ahUKEwiu29um48TyAhWGqpUCHYuoAlcQ_AUoAnoECAEQBA&biw=1441&bih=718&dpr=2"

req = Request(link, headers = {'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

links = []
with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'html5lib')
    #print(soup)
    for item in soup.find_all('div', attrs = {'class': "ZINbbc xpd O9g5cc uUPGi"}):
        #print(item)
        raw_link = (item.find('a', href = True)['href'])
        link = (raw_link.split("/url?q=")[1]).split('&sa=U&')[0]
        title = (item.find('div',attrs = {'class': 'BNeawe vvjwJb AP7Wnd'}))
        description  = (item.find('div',attrs = {'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())
        time = description.split(" · ")[0]
        #print(description)
        descript = description.split(" · ")[1]
        print(title)
        print(time)
        print(descript)
        links.append(link)
        print(link)
        print("\n")

        news_data = open("data.csv","a")
        news_data.write("{},{},{},{} \n".format(title,time,descript,link))
        news_data.close

"""     
print(links)

mainlink = links[0]

req = Request(mainlink, headers = {'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'html5lib')
    print(soup)
    """
        

