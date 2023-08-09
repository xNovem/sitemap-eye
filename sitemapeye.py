# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import requests
from colorama import Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(Fore.CYAN + """
  ____ ____ _  _ ____ _  _    _ _ _ ____ ___ ____ _ ____ _  _ 
  |    |  | |\/| |  | |\ |    | | | |  |  |  |  | |  | |  | 
  |___ |__| |  | |__| | \|    |_|_| |__|  |  |__| |__|  \/  
                                                            
    Site Haritası Çıkartma Aracı
    """ + Style.RESET_ALL)

def get_site_map(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
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
    site_url = input("\nSite URL'sini girin: ")
    site_map = get_site_map(site_url)
    print("\nSite Haritası:")
    print_site_map(site_map)

if __name__ == "__main__":
    main()
