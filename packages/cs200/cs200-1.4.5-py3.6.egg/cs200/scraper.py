from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import re
from cs200.core import BASE_SEARCH_URL, BASE_DELIMITER

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


def get_url(concept, out, limit):
        """ Function to automate summarizing and writing result to a file."""
        url = build_url(concept)

        parser = HtmlParser.from_url(url, Tokenizer("english"))

        stemmer = Stemmer("english")

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words("english")

        # Loop over entire summarized structure and return sentences by writing them to output file of user's choice.
        for sentence in summarizer(parser.document, limit):
                with open(out, "a") as output:
                    output.write(str(sentence))
