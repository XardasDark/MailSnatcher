#!/usr/bin/env python3

from crawler import config
import crawler.logging
import argparse
import logging
from crawler.core import MailCrawler

def main():
    parser = argparse.ArgumentParser(
        prog="MailSnatcher",
        description="Smart E-Mail Crawler - snatches emails from websites!"
    )
    
    parser.add_argument(
        "url",
        help="Start URL of the website to crawl"
    )
    
    parser.add_argument(
        "-d", "--depth",
        type=int,
        default=config.DEFAULT_DEPTH,
        help="Maximum crawl depth (default: 2)"
    )

    parser.add_argument(
        "-o", "--output",
        choices=["console"],
        default="console",
        help="Output format (default: console)"
    )
    
    parser.add_argument(
        "--loglevel", "-l",
        default=config.DEFAULT_LOG_LEVEL,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: INFO)"
    )
    
    args = parser.parse_args()
    
    logging.getLogger().setLevel(getattr(logging, args.loglevel.upper()))
    mail_crawler = MailCrawler(start_url=args.url, depth=args.depth)
    results = mail_crawler.run()

    if args.output == "console":
        for email in results:
            print(email)
    else:
        print(f"Export '{args.output}' not implemented yet.")

if __name__ == "__main__":
    main()
