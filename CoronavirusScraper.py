import requests
from bs4 import BeautifulSoup

"""
Eventually make this an args call maybe?
"""


def get_request():
    page = requests.get("https://www.buzzfeed.com/")
    return page.content


def parse_soup(content):
    soup = BeautifulSoup(content, "html.parser")
    return soup


def get_headlines(soup):
    headlines = soup.find_all("a", class_="js-card__link")
    coronaCount = 0
    covidCount = 0
    virusCount = 0
    for str in list(headlines):
        if "corona" in str.get_text().lower():
            coronaCount += 1
        if "covid" in str.get_text().lower():
            covidCount += 1
        if "virus" in str.get_text().lower():
            virusCount += 1
    print(
        "Count of Corona: %s \n Count of Covid: %s \n Count of Virus %s"
        % (coronaCount, covidCount, virusCount)
    )


content = get_request()
soup = parse_soup(content)
get_headlines(soup)
