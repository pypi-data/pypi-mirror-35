#!/usr/bin/env python3
from cs200.core import BASE_SEARCH_URL, BASE_DELIMITER
from summa.summarizer import summarize
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


# This is a function to properly create a url for searching wikipedia pages.
def build_url(url):

        final_url = ""

        spaces = re.split(" ", url)
        # Iterate over the spaces list but exclude the last item.
        for item in range(len(spaces)-1):

                # Add an underscore between spaces in the search query
                final_url += spaces[item] + BASE_DELIMITER

        # To avoid adding an extra underscore after the final search term in the
        # url, we only add the last item of the spaces list to the final_url
        # variable after breaking out of the loop.
        final_url += spaces[-1]

        return BASE_SEARCH_URL + final_url


def remove_tags(text):
    # Code snippet used from stack overflow, will replace with customized version
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)

def parse_url(url):
    """Function that separates the important text from the irrelevant wikipedia html/js/css code of a HTTP response."""

    # Variable that will eventually be equal to the relevant text of a wikipedia post.
    relevant_text = str()

    data = urlopen(url).read()


    # Instantiate beautifulsoup object and locate all p elements in the data variable.
    soup = BeautifulSoup(data, "html.parser")
    paragraphs = soup.find_all("p")

    # Loop over each paragraph in the paragraphs list. If it has a parent div element,
    # consider the element as relevant text in the summarization process and therefore append it to the
    # relevant_text variable.
    for paragraph in paragraphs:
        if paragraph.parent.name == "div":
            relevant_text += str(paragraph)

    # Remove all tags in the text for optimization of user experience and summarization
    return remove_tags(relevant_text)


def summarize_wiki(concept, limit):
        """ Function to automate summarizing and writing result to a file."""

        url = build_url(concept)

        parsed_text = parse_url(url)

        return summarize(parsed_text, words=limit)
