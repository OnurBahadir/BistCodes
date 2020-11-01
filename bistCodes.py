
import bs4 as bs
import requests 

def getBistCodes():
    req=requests.get("https://www.kap.org.tr/tr/bist-sirketler")
    soup=bs.BeautifulSoup(req.text,"html.parser")
    codes=soup.find_all("div",{"class":"comp-cell _04 vtable"})
    codes=[x.text[1:-1] for x in codes]
    return codes


print( getBistCodes() ) 
