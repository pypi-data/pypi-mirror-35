from cs200.scraper import summarize_wiki


class Controller:

    def __init__(self):
            self.headless_mode = False


    def write_summarization(self, concept="computer programming", limit=5, output="output.txt"):

        # Obtain text from wikipedia page in headless mode(with command line).
        if self.headless_mode:
            text = summarize_wiki(self.concept, self.limit)
            with open(self.output, "w") as out:
                out.write(text)

        # Obtain summarized text in normal mode.
        elif not self.headless_mode:
            text = summarize_wiki(concept, limit)
            with open(output, "w") as out:
                out.write(text)

    def init_args(self):
        """ Function to create argument interface with command line. """

        import argparse

        self.headless_mode = True

        parser = argparse.ArgumentParser()

        parser.add_argument("--c", "--concept", help="The concept to simplify", type=str, default="computers")
        parser.add_argument("--l", "--limit", help="The amount of results to be returned", type=int, default=3)
        parser.add_argument("--o", "--output", help="Output file to write results to", type=str, default="output.txt")

        args = parser.parse_args()

        self.concept = args.c
        self.limit = args.l
        self.output = args.o
