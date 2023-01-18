from tech_news.database import search_news


# https://stackoverflow.com/questions/26699885/how-can-i-use-a-regex-variable-in-a-query-for-mongodb
# Requisito 6
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    response = []
    for new in search:
        response.append((new["title"], new["url"]))
    return response


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    search = search_news({"tags": {"$regex": tag, "$options": "i"}})
    response = []
    for new in search:
        response.append((new["title"], new["url"]))
    return response


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
