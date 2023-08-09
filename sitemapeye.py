import os
import requests
from bs4 import BeautifulSoup
from termcolor import colored

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def print_sitemap_to_file(sitemap, filename, indentation=''):
    with open(filename, 'w') as f:
        for page, links in sitemap.items():
            f.write(f"{indentation}{page}\n")
            for link in links:
                f.write(f"{indentation}  -> {link}\n")

def main():
    banner = colored("""
     ____  _ _       __  __
    / ___|(_) |_ ___|  \/  | __ _ _ __
    \___ \| | __/ _ \ |\/| |/ _` | '_ \\
     ___) | | ||  __/ |  | | (_| | |_) |
    |____/|_|\__\___|_|  |_|\__,_| .__/
                                 |_|

    """, 'red')

    created_by = colored("Created By ", 'red') + colored("xNovem", 'red') + colored("\n( ", 'red') + colored("https://github.com/xNovem", 'yellow') + colored(" )", 'red')

    print(banner)
    print(created_by)
    print("Welcome to SiteMap Eye!")

    url = input("Enter the URL to generate the site map: ")
    clear_screen()
    print(colored("Generating sitemap...", 'red'))
    sitemap = create_sitemap(url)

    output_filename = 'sitemap.txt'
    print(colored(f"Generated Site Map saved to '{output_filename}':", 'red'))
    print_sitemap_to_file(sitemap, output_filename)
    print_sitemap(sitemap)
    print(created_by)

if __name__ == "__main__":
    main()
