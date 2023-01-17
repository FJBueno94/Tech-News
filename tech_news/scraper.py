import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=2, headers={
            "user-agent": "Fake user-agent"
        })
        status_code = response.status_code
        if status_code == 200:
            response = response.text
            return response
    except requests.ReadTimeout:
        return None
    else:
        return None


# Requisito 2
def scrape_updates(html_content):
    select = Selector(html_content)
    links = select.css('a.cs-overlay-link::attr(href)').getall()
    if links:
        return links
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    select = Selector(html_content)
    link = select.css('a.next::attr(href)').get()
    if link:
        return link
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
