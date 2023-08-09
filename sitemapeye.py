import requests
from bs4 import BeautifulSoup
from termcolor import colored

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
        print(colored(f"{indentation}{page}", 'green'))
        for link in links:
            print(f"{indentation}  -> {link}")

banner = colored("""
 ____  _ _       __  __
/ ___|(_) |_ ___|  \/  | __ _ _ __
\___ \| | __/ _ \ |\/| |/ _` | '_ \\
 ___) | | ||  __/ |  | | (_| | |_) |
|____/|_|\__\___|_|  |_|\__,_| .__/
                             |_|

""", 'red')

url = input("Enter the URL to generate the site map: ")
sitemap = create_sitemap(url)

print(banner)
print("Welcome to SiteMap Eye!")
print("\nGenerated Site Map:")
print_sitemap(sitemap)

created_by = colored("\nCreated By ", 'red') + colored("xNovem", 'red') + colored("\n( ", 'red') + colored("https://github.com/xNovem", 'yellow') + colored(" )", 'red')
print(created_by)
