import bbc_link_scrapper as bls
from bs4 import BeautifulSoup
import requests
import os


def get_content():
    # if file is empty or does not exist
    if not os.path.exists("url.in"):
        print("Fetching URLs from BBC")
        bls.fill_url_in_file()
    elif os.stat("url.in").st_size == 0:
        print("Fetching URLs from BBC")
        bls.fill_url_in_file()

    print("Fetching Data from Urls")
    scrap_data = {}  # Dictionary to save Data of New(Heading,Content)
    file_count = 0

    # Reading from url.in file
    lines = ""
    with open("url.in", 'r') as file:
        lines = file.readlines()

    with open("url.in", 'w') as file:  # OPENED this file again to reWrite accessed URL in url.in
        for line in lines:             # Iterating as Each line of URL
            response = requests.get(line)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Finding Heading of News
            heading_list = soup.find(
                class_="story-headline gel-trafalgar-bold")
            scrap_data['heading'] = ""

            if(heading_list != None):
                # If more than one Heading exists
                for heading in heading_list:
                    scrap_data['heading'] += str(heading)

            # Selecting div containing Paragraph
            div = soup.find('div', {'id': "story-body"})

            if(div != None):
                p_in_div = div.find_all('p')
                # content = soup.find(id="story-body").contents

                # Gathering all text inside div into DICTIONARY
                scrap_data['content'] = ""
                for p in p_in_div:
                    temp = str(p.get_text())
                    scrap_data['content'] += "\n"+temp

                """Writing News Data in file"""
                # Creating 'data' folder if not exist
                if not os.path.exists('data'):
                    os.makedirs('data')

                file_count += 1
                with open("./data/news"+str(file_count)+".txt", 'w') as output:
                    output.write(scrap_data['heading'])
                    output.write(scrap_data['content'])
                    output.write('\n')
                    # print("news"+str(file_count)+".txt is written")

                    # Rewriting URL because some might be empty
                    file.write(line)
                if (file_count == 10):
                    break
