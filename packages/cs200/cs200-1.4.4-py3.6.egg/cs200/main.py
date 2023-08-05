import argparse
from cs200.scraper import build_url, get_url

    
class Controller:
            
    def __init__(self):
            self.headless_mode = True
        
    def return_summarization(self, concept="computer programming", limit=5, output="output.txt"):
        
        # Obtain text from wikipedia page in headless mode(without command line).
        if self.headless_mode:
            get_url(concept, output, limit)
                
        # Obtain summarized text in cli mode.   
        elif not self.headless_mode:
            get_url(self.concept, self.output, self.limit)
    
    
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
