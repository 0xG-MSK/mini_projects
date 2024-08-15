#user input to search
print("""
NOTE: To retrieve data for domain and sub domain,
enter domain and sub-domain with whitespace
""")
user_input = input('Enter Web Domain: ')
print()
print('loading... ')
#modules
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import webbrowser as wb
import random as rd
import sys

# URL of the webpage to scrape
if ' ' in user_input:
    domain = user_input.split()
    url = f'https://{domain[0]}.com/{domain[1]}'
    hyperL = url
elif ' ' not in user_input:
    url = f'https://www.{user_input}.com'
    hyperL = url
print(url)
# Send a GET request to the webpage
try:
    response = requests.get(url)
except:
    print()
    sys.exit('No Such Address: NSA')

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the data on the webpage
    #text
    #element = soup.find('html')
    texts = soup.get_text()
    print('\n',texts)
    #links
    links = soup.find_all('a')
#   Convert relative URLs to absolute ones and print/save them
    #for link in links:
        #absolute_url = urljoin(url, link.get('href'))
        #print(absolute_url)
        
        # Save the absolute URLs to a file
    with open('/storage/emulated/0/Documents/data.txt', 'w') as f:
        f.write(texts + '\n')
else:
    print("Failed to retrieve the webpage")


open_site = input('Do want to open site? ').lower()
match open_site:
    case 'yes':
        wb.open_new(hyperL)
        print(url, '-->')
    case 'y':
        wb.open_new(hyperL)
    case 'no':
        pass
    case 'n':
        pass
#wb.open_new(hyperL) #opens the site after retrieving data
"""
```

This code uses `urljoin` to join the base URL (`url`) with the relative URL (`link.get('href')`) to form an absolute URL. The `urljoin` function takes care of handling different types of relative URLs.

Note that I've also changed the file mode to 'a' (append) instead of `'w'` (write) to avoid overwriting the file if you run the script multiple times.

"""