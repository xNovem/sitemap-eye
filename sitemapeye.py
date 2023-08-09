import requests
from bs4 import BeautifulSoup

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []

    for link in soup.find_all('a'):
        link_url = link.get('href')
        if link_url and link_url.startswith('http'):
            links.append(link_url)
    
    return links

def create_sitemap(start_url, max_depth=3):
    sitemap = {}
    visited = set()
    
    def crawl(url, depth):
        if depth > max_depth or url in visited:
            return
        visited.add(url)
        
        links = get_links(url)
        sitemap[url] = links
        
        for link in links:
            crawl(link, depth + 1)
    
    crawl(start_url, 0)
    return sitemap

def print_sitemap(sitemap, indentation='|=====> '):
    for page, links in sitemap.items():
        print(f"{indentation}{page}")
        for link in links:
            print(f"{indentation}  -> {link}")

banner = """
 _______  ___      _______  __   __  _______  __   __ 
|       ||   |    |   _   ||  | |  ||   _   ||  | |  |
|    _  ||   |    |  |_|  ||  |_|  ||  |_|  ||  |_|  |
|   |_| ||   |    |       ||       ||       ||       |
|    ___||   |___ |       ||       ||       ||       |
|   |    |       ||   _   ||   _   ||   _   | |     | 
|___|    |_______||__| |__||__| |__||__| |__|  |___|  
                                                     
"""

print(banner)
print("Welcome to SiteMap Eye!")
url = input("Enter the URL to generate the site map: ")
sitemap = create_sitemap(url)

print("\nGenerated Site Map:")
print_sitemap(sitemap)
