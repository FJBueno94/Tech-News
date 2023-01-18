import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, timeout=2, headers={"user-agent": "Fake user-agent"}
        )
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
    links = select.css("a.cs-overlay-link::attr(href)").getall()
    if links:
        return links
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    select = Selector(html_content)
    link = select.css("a.next::attr(href)").get()
    if link:
        return link
    else:
        return None


# Requisito 4
# https://www.tutorialspoint.com/python3/string_strip.htm
def scrape_news(html_content):
    select = Selector(html_content)
    url = select.css("link[rel=canonical]::attr(href)").get()
    title = select.css("h1.entry-title::text").get().strip()
    timestamp = select.css("li.meta-date::text").get()
    writer = select.css("span.author a::text").get()
    comements = select.css("ol.comment-list li").getall()
    comments_count = len(comements) if comements else 0
    summary = "".join(
        select.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    tags = select.css("section.post-tags a::text").getall()
    category = select.css("div.meta-category span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    page = fetch("https://blog.betrybe.com/")
    news_list = []
    while len(news_list) < amount:
        news_list += scrape_updates(page)
        page = fetch(scrape_next_page_link(page))

    db_news = [scrape_news(fetch(page)) for page in news_list[0:amount]]
    create_news(db_news)
    return db_news
