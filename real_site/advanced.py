from bs4 import BeautifulSoup
import requests

html_content = requests.get('https://www.panda.tn/index.php?id_product=126&id_product_attribute=0&rewrite=pack-creme-eclat-a-l-huile-de-sesame&controller=product').text

soup = BeautifulSoup(html_content, 'lxml')
charts = soup.find_all('div', class_='row')

for chart in charts:

    try:
        produit = chart.find('div', class_="product-prices").text.replace(' ','').replace('\n','').replace('\t','')
        print(produit)

    except AttributeError:
        print("No product prices found in this chart.")


