import logging

logger = logging.getLogger(__name__)

class MailCrawler:
    def __init__(self, start_url, depth):
        self.start_url = start_url
        self.depth = depth
        self.results = set()

    def run(self):
        logger.info("Starting crawl at %s with depth %s", self.start_url, self.depth)
        return sorted(self.results)
    
# Download Website Content
