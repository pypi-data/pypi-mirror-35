from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import argparse
from cs200.scraper import build_url

    
class Controller:
            
    def __init__(self):
            self.headless_mode = True
        
    def return_summarization(self, concept="computer programming", limit=5, output="output.txt"):
        
        # Obtain text from wikipedia page in headless mode(without command line).
        if self.headless_mode:
            url = build_url(concept)
        
            parser = HtmlParser.from_url(url, Tokenizer("english"))

            stemmer = Stemmer("english")

            summarizer = Summarizer(stemmer)
            summarizer.stop_words = get_stop_words("english")

            # Loop over entire summarized structure and return sentences by writing them to output file of user's choice.
            for sentence in summarizer(parser.document, limit):
                with open(output, "a") as output:
                    output.write(str(sentence))
                
        # Obtain summarized text in cli mode.   
        elif not self.headless_mode:
            
            url = build_url(self.concept)
        
            parser = HtmlParser.from_url(url, Tokenizer("english"))

            stemmer = Stemmer("english")

            summarizer = Summarizer(stemmer)
            summarizer.stop_words = get_stop_words("english")

            # [CLI Mode] Loop over entire summarized structure and return sentences by writing them to output file of user's choice.
            for sentence in summarizer(parser.document, self.limit):
                with open(self.output, "a") as output:
                    output.write(str(sentence))
    
    
    def init_args(self):
        """ Function to create argument interface with command line. """
        self.headless_mode = False
        
        parser = argparse.ArgumentParser()

        parser.add_argument("--c", "--concept", help="The concept to simplify", type=str, default="computers")
        parser.add_argument("--l", "--limit", help="The amount of results to be returned", type=int, default=3)
        parser.add_argument("--o", "--output", help="Output file to write results to", type=str, default="output.txt")

        args = parser.parse_args()

        self.concept = args.c
        self.limit = args.l
        self.output = args.o
