from tech_news.database import search_news
from datetime import datetime


def data_validation(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")


# https://stackoverflow.com/questions/26699885/how-can-i-use-a-regex-variable-in-a-query-for-mongodb
# Requisito 6
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    response = []
    for new in search:
        response.append((new["title"], new["url"]))
    return response


# https://stackoverflow.com/questions/969285/how-do-i-translate-an-iso-8601-datetime-string-into-a-python-datetime-object
# Requisito 7
def search_by_date(date):
    data_validation(date)
    search = search_news(
        {
            "timestamp": {
                "$eq": datetime.fromisoformat(date).strftime("%d/%m/%Y")
            }
        }
    )
    response = []
    for new in search:
        response.append((new["title"], new["url"]))
    return response


# Requisito 8
def search_by_tag(tag):
    search = search_news({"tags": {"$regex": tag, "$options": "i"}})
    response = []
    for new in search:
        response.append((new["title"], new["url"]))
    return response


# Requisito 9
def search_by_category(category):
    search = search_news({"category": {"$regex": category, "$options": "i"}})
    response = []
    for new in search:
        response.append((new["title"], new["url"]))
    return response
