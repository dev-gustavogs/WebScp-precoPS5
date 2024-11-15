import requests
from bs4 import BeautifulSoup
import time

def fecht_page():
  url = "https://www.mercadolivre.com.br/console-playstation-5-digital-slim-branco-1tb-returnal-e-ratchet-e-clank-controle-sem-fio-dualsense-branco/p/MLB37494438#polycard_client=search-nordic&wid=MLB3885192251&sid=search&searchVariation=MLB37494438&position=1&search_layout=grid&type=product&tracking_id=33b3de9b-666c-44cc-9ced-d8d8cc8e11db"
  response = requests.get(url)
  return response.text

def parser_page(html):
  soup = BeautifulSoup(html, "html.parser")
  product_name = soup.find('h1', class_= 'ui-pdp-title').get_text()
  prices = soup.find_all('span', class_='andes-money-amount__fraction')
  old_price = int(prices[0].get_text(strip=True).replace('.', ''))
  new_price = int(prices[1].get_text(strip=True).replace('.', ''))
  installment_price = int(prices[2].get_text(strip=True).replace('.', ''))

  return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'installment_price': installment_price
  }
  
if __name__ == "__main__":
  while True:
        page_content = fecht_page()
        product_info = parser_page(page_content)
        print(product_info)
        time.sleep(10)