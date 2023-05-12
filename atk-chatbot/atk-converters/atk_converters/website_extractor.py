from langchain.document_loaders import WebBaseLoader
from typing import List
import re
import urllib.request
from collections import deque
from html.parser import HTMLParser
from urllib.parse import urlparse
from typing import Any, Set
import logging

logging.getLogger().setLevel(logging.INFO)

HTTP_URL_PATTERN = r'^http[s]{0,1}://.+$'

full_url = "https://aganitha.ai/"


class WebsiteExtractor:

    @staticmethod
    def website_loader(url: str) -> List:
        """Takes in a file with list of links and returns the contents of the
           websites as document objects"""
        # with open(web_input_file, "r") as f:
        #     urls = [line.strip() for line in f]
        urls = crawl(url)
        loader = WebBaseLoader(urls)
        docs = loader.load()
        return docs


class HyperlinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hyperlinks: List[str | Any] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.hyperlinks.append(attrs["href"])


def get_hyperlinks(url: str) -> List[None | str]:
    try:
        with urllib.request.urlopen(url) as response:
            if not response.info().get('Content-Type').startswith("text/html"):
                return []
            html = response.read().decode('utf-8')
    except Exception as e:
        logging.info(e)
        logging.info(f"page not found for {url}")
        return []

    parser = HyperlinkParser()
    parser.feed(html)
    return parser.hyperlinks


def get_domain_hyperlinks(local_domain: str, url: str) -> List[str]:
    clean_links: List[str] = []
    for link in set(get_hyperlinks(url)):
        clean_link: str | None = None
        if re.search(HTTP_URL_PATTERN, link):
            url_obj = urlparse(link)
            if url_obj.netloc == local_domain:
                clean_link = link

        else:
            if link.startswith("/"):
                link = link[1:]
            elif link.startswith("#") or link.startswith("mailto:"):
                continue
            clean_link = "https://" + local_domain + "/" + link

        if clean_link is not None:
            image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"]
            if clean_link.endswith("/"):
                clean_link = clean_link[:-1]
            if any(clean_link.endswith(ext) for ext in image_extensions):
                continue
            clean_links.append(clean_link)

    return list(set(clean_links))


def crawl(url: str) -> List[str]:
    logging.info(f"Extracting pages for domain: {url}")
    local_domain = urlparse(url).netloc
    queue = deque([url])
    seen = set([url])
    while queue:
        url = queue.pop()
        for link in get_domain_hyperlinks(local_domain, url):
            if link not in seen:
                queue.append(link)
                seen.add(link)
                logging.info(f"Visited {link}")
    return list(seen)
