import os
from BeautifulSoup import BeautifulSoup
import requests

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("""
  ____ ____ _  _ ____ _  _    _ _ _ ____ ___ ____ _ ____ _  _ 
  |    |  | |\/| |  | |\ |    | | | |  |  |  |  | |  | |  | 
  |___ |__| |  | |__| | \|    |_|_| |__|  |  |__| |__|  \/  
                                                            
    SiteMap EYE 
    """)

def get_site_map(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content)
        links = soup.findAll('a')
        return [link.get('href') for link in links if link.get('href') and not link.get('href').startswith('#')]
    else:
        print("Hata: Sayfa alınamadı.")

def print_site_map(site_map, depth=0):
    for link in site_map:
        print("|" + "=" * (4 * depth) + "> " + link)
        nested_links = get_site_map(link)
        if nested_links:
            print_site_map(nested_links, depth + 1)

def main():
    clear_screen()
    print_header()
    site_url = raw_input("\nSite URL'sini girin: ")
    site_map = get_site_map(site_url)
    print("\nSite Haritası:")
    print_site_map(site_map)

if __name__ == "__main__":
    main()
