
import re
import requests
from bs4 import BeautifulSoup

def extract_email_from_url(url):
    try:
        res = requests.get(url, timeout=5)
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", res.text)
        return emails[0] if emails else None
    except Exception:
        return None
