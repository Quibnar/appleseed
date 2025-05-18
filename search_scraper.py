from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import urllib.parse
import time

def search_yelp(industry, location):
    query = f"site:yelp.com/biz {industry} in {location}".replace(" ", "+")
    url = f"https://duckduckgo.com/?q={query}&t=h_&ia=web"

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)

    # Wait for dynamic content to render
    time.sleep(5)

    # Scroll to bottom to trigger any lazy loading
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    print("\n🔍 Rendered DuckDuckGo HTML preview (first 500 chars):")
    print(soup.prettify()[:500])

    results = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "yelp.com/biz/" in href or "duckduckgo.com/l/?uddg=" in href:
            name = a.get_text(strip=True)

            # Unwrap redirect link if needed
            if "duckduckgo.com/l/?uddg=" in href:
                href = urllib.parse.parse_qs(urllib.parse.urlparse(href).query).get("uddg", [href])[0]
                href = urllib.parse.unquote(href)

            results.append({"name": name or "Yelp Business", "url": href})

    return results
