import bs4 as bs
import requests 

def getBistCodes():
    req=requests.get("https://www.kap.org.tr/tr/Endeksler")
    soup=bs.BeautifulSoup(req.text,"html.parser")
    codes=soup.find_all("div",{"class":"comp-cell _02 vtable"})
    codes=[x.text[1:-1] for x in codes]
    return codes

if __name__=="__main__":
    print(getBistCodes())
