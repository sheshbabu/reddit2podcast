import requests
from urllib.parse import urlparse, urlunparse
from typing import TypedDict


class Article(TypedDict):
    title: str
    id: str
    selftext: str
    is_self: bool
    num_comments: int


def get_json(url: str):
    new_url = construct_json_url(url)
    response = requests.get(new_url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def extract_articles(json_data: dict) -> list[Article]:
    articles = []
    for post in json_data["data"]["children"]:
        article: Article = {
            "title": post["data"]["title"],
            "id": post["data"]["name"],
            "selftext": post["data"]["selftext"],
            "is_self": post["data"]["is_self"],
            "num_comments": post["data"]["num_comments"],
        }
        articles.append(article)
    return articles


def extract_comments(json_data: dict) -> list[str]:
    comments = []
    for post in json_data[1]["data"]["children"]:
        if "body" in post["data"]:
            comments.append(post["data"]["body"])
    return comments


def construct_json_url(url: str) -> str:
    parsed_url = urlparse(url)
    path = parsed_url.path
    if not path.endswith(".json"):
        path += ".json"
    new_url = urlunparse(parsed_url._replace(path=path))
    if parsed_url.query:
        new_url += "?" + parsed_url.query
    return new_url
