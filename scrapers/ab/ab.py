from urllib.parse import urljoin
import re
import csv
import requests
from bs4 import BeautifulSoup

from config import minister_urls

SOCIAL_SELECTORS = {
    'twitter': "a[href*='twitter.com']",
    'facebook': "a[href*='facebook.com']",
    'youtube': "a[href*='youtube.com']",
    'instagram': "a[href*='instagram.com']"
}


def get_ministry_data(session, name, url):
    response = session.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    about = soup.select_one('p.goa-page-header--lede')
    socials = {
        key: (tag['href'] if (tag := soup.select_one(sel)) and tag.has_attr('href') else '')
        for key, sel in SOCIAL_SELECTORS.items()
    }
    return {
        'type': name,
        'about': about.get_text(strip=True) if about else '',
        'priorities': '',
        'website': url,
        **socials
    }


def parse_compound_name(tag):
    text = tag.get_text(' ', strip=True)
    parts = re.findall(r"[A-Za-z]+", text)
    return ' '.join(parts[:3])


def get_minister_data(session, url):
    response = session.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    name_tag = soup.select_one('div.goa-text h2')
    image_tag = soup.select_one('div.goa-thumb img')
    name = parse_compound_name(name_tag) if name_tag else ''
    photo = urljoin(url, image_tag['src']) if image_tag and image_tag.has_attr('src') else ''
    return {
        'name': name,
        'photo_url': photo,
        'minister_contact_number': '',
        'minister_url': url
    }


def scrape_ministries(output_file='output.csv'):
    session = requests.Session()
    headers = [
        'type', 'about', 'priorities', 'website',
        'twitter', 'facebook', 'youtube', 'instagram',
        'name', 'photo_url', 'minister_contact_number', 'minister_url'
    ]
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for ministry, (min_url, minister_url) in minister_urls.items():
            print(f"Scraping ministry: {ministry}")
            data = get_ministry_data(session, ministry, min_url)
            data.update(get_minister_data(session, minister_url))
            writer.writerow(data)


if __name__ == '__main__':
    scrape_ministries()
