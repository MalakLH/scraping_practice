from bs4 import BeautifulSoup
import requests
import time

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

    with open(f'product_info.txt', 'a', encoding='utf-8') as file:
        file.write(f'Produit: {produit}\n')
        file.write(f'Prix: {prix}\n')
        file.write(f'Description: {description}\n')
        file.write('------------------------\n')

if __name__ == "__main__":

    while True:
        url = input("Enter the product URL: ")
        scrape_product_info(url)
        """
        time.sleep(5)  # Wait for 5 seconds before the next iteration
        """
