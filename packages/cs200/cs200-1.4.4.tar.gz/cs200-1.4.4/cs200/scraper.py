import requests
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


