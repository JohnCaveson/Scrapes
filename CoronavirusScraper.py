import requests
from bs4 import BeautifulSoup

"""
Eventually make this an args call maybe?
"""


def parse_soup(pages=[]):
    pageContents = b''
    for page in pages:
        pageContents += page.content
    soup = BeautifulSoup(pageContents, "html.parser")
    return soup


def get_request():
    requestUrls = ["https://www.buzzfeed.com/", "https://www.yahoo.com/"]
    pages = []
    for url in requestUrls:
        pages.append(requests.get(url))

    return parse_soup(pages)


"""
TODO: Create individual headline functions per website or find a way to get all
"""


def get_headlines(soup):
    headlines = soup.find_all("a")
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
get_headlines(content)
