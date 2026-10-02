import requests
from bs4 import BeautifulSoup
import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

data=[]

for page in range(1,3):
    url=f"http://books.toscrape.com/catalogue/page-{page}.html"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')

    books_price=soup.find_all('article',class_="product_pod")
    for price in books_price:
        name_of_book=price.find('h3').get_text()
        prices=price.find(class_="price_color").get_text()
        cleaned_text=prices.replace("£","").replace(",","")
        flo_prices=float(cleaned_text)
        stock=price.find('p',class_="instock availability").get_text()
        if flo_prices<45:
           
            data.append({"names":name_of_book,"prices":flo_prices,"stock_availability":stock})
try:
    url2=" https://pointer-animating-garnet.ngrok-free.dev/webhook-test/6f728f31-ba17-4780-a9db-d4748b162a8b"
    payload=requests.post(url2,json=data)
    if payload.status_code==200:
        print("successful",payload.json())
    else:
        ("failed",payload.status_code)
except Exception as e:
    print("an error occur as",e)