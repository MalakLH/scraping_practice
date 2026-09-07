from bs4 import BeautifulSoup
import requests

def scrape_product_info(url):
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, 'lxml')
    charts = soup.find_all('div', class_='row')


    for chart in charts:

        try:
            produit = chart.find('h1').text.replace('  ','').replace('\n','')
            print(f'Produit: {produit}')
            break

        except AttributeError:
            pass


    for chart in charts:

        try:
            prix = chart.find('div', class_="product-prices").text.replace('  ','').replace('\n','').replace('\t','')
            print(f'Prix: {prix}')
            break

        except AttributeError:
            pass


    for chart in charts:
        
        try:
            description = chart.find('p').text.replace('  ','').replace('\n','').replace('\t','')
            print(f'Description: {description}')
            break

        except AttributeError:
            pass