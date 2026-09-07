from bs4 import BeautifulSoup

with open('presentation.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()
    print(html_content) # Print the HTML content to verify it's read correctly

    soup = BeautifulSoup(html_content, 'lxml')
    print(soup.prettify()) # Print the prettified HTML to verify BeautifulSoup parsing

    tags = soup.find_all('h3')
    print(tags) # Print all <h3> tags found in the HTML, we get a list as a result that has all the <h3> tags in it. We can iterate over this list to get each tag individually.

    for tag in tags:
        print(tag.text) # Print the text content of each <h3> tag