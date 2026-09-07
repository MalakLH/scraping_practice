from bs4 import BeautifulSoup

with open('presentation.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

    soup = BeautifulSoup(html_content, 'lxml')

    h2_tags = soup.find_all('h2', class_='title reveal d1') # the class_ parameter is used to specify the class attribute of HTML

    h3_tags = soup.find_all('h3')

    for h2_tag in h2_tags:
        h2_text= h2_tag.text.strip() # Use strip() to remove any leading/trailing whitespace
        print(h2_text) # Print the text content of each <h2> tag

    for h3_tag in h3_tags:
        h3_text = h3_tag.text.strip()[-1] # Use strip() to remove any leading/trailing whitespace and get the last word
        print(h3_text) # Print the text content of each <h3> tag