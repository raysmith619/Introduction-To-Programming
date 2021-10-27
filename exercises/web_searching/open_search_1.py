# open_search_1.py  26May2021  crs
"""
Automate The Boring Stuff with Python  Al Sweigart 2nd Ed
Chapter 12 - Web Scraping
Project: Opening All Search Results - A project to search
the Python Package Index and automatically open each
search result link.
Needed:
pip install --user beautifulsoup4
"""
import requests, sys, webbrowser, bs4
verbose = 0x05          # Larger more debugging info
print('Searching...')   # display text while downloading
                        #  the search result page
search_args = ['tom', 'brady' , 'nfl']  # Default  - for testing
if len(sys.argv[1:]) > 0:
    search_args = sys.argv[1:]  # Use actual cmd line args
print(f"search_args:{search_args}")
google_url = "https://google.com"
pypi_url = "https://pypi.org"
request = google_url + '/search?q=' # Stick to google
request += " ".join(search_args)
print(f"request:{request}")
res = requests.get(request)
res.raise_for_status()

if verbose >= 0x100:
    print(f"res: {res}")
    print(f"res.text:{res.text}")
"""
Step 2: Find All the Results
"""
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.content, 'html.parser')
if verbose >= 0x10:
    print("\n\nExperimenting with soup navigation")
    if verbose >= 0x100:
        print(f"\nsoup: {soup}")
    if verbose >= 0x010:
        try:
            print(f"\nsoup prettify: {soup.prettify()}")
        except:
            print("prettify - failed")

    print("\n\nsoup <b>")
    for tag in soup.find_all('b')[0:3]:
        print(tag)

    print("\n\nsoup <a>")
    for tag in soup.find_all('a')[0:5]:
        print(tag.prettify())
    
# Open a browser tab for each result.
linkElems = soup.select('a')
print(f"n links: {len(linkElems)}")

"""
Step 3: Open Web Browsers for Each Result
"""
numOpen = min(5, len(linkElems))
print(f"Opening the first {numOpen}")
for i in range(numOpen):
    urlToOpen = google_url + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

