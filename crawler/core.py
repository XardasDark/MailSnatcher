import crawler.config as config

class MailCrawler:
    def __init__(self, start_url, depth=None):
        self.start_url = start_url
        self.depth = depth if depth is not None else config.DEFAULT_DEPTH
        self.results = set()

    def run(self):
        # TODO: Everything
        print(f"Starting crawl at {self.start_url} with depth {self.depth}")

        return sorted(self.results)