# get_info.py

import requests
from bs4 import BeautifulSoup
import whois
import sys

def get_subdomains(url):
    try:
        response = requests.get(f'http://dnsdumpster.com/?dns={url}')
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find_all('table')[0]
        rows = table.find_all('tr')[1:]

        subdomains = []
        for row in rows:
            cols = row.find_all('td')
            subdomain = cols[0].text.strip()
            subdomains.append(subdomain)

        return subdomains
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_whois_information(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except Exception as e:
        print(f"Error: {e}")
        return {}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_info.py <domain>")
        sys.exit(1)

    domain_name = sys.argv[1]

    # Find subdomains
    subdomains = get_subdomains(domain_name)
    print(f"Subdomains: {subdomains}")

    # Get WHOIS information
    whois_info = get_whois_information(domain_name)
    print(f"\nWHOIS Information:\n{whois_info}")
