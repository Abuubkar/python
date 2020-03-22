from bs4 import BeautifulSoup
import requests
baseUrl = "https://www.bbc.com"
url = "https://www.bbc.com/sport"


def fill_url_in_file():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    news_url = []

    # heading = soup.select(
    #     ".gs-c-promo-heading gs-o-faux-block-link__overlay-link sp-o-link-split__anchor gel-pica-bold")

    # Finding all classes containing LINKS in MAIN PAGE
    heading = soup.find_all(
        class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link sp-o-link-split__anchor gel-pica-bold")

    # Accessing all LINKS within classes
    for ref in heading:
        temp = str(ref['href'])

        # Filtering & Saving in list URLs
        if(temp.find("live", 0, len(temp)-1) < 0
           and (temp.find("http", 0, len(temp)-1) < 0)
           and (temp.find("av", 0, len(temp)-1)) < 0):
            news_url.append(baseUrl+ref['href'])

    # Saving in File all Url
    with open("url.in", 'w') as file:
        for link in news_url:
            file.write(link)
            file.write('\n')
    print("Url found ", len(news_url)-1)
