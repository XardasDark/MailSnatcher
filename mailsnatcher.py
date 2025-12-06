#!/usr/bin/env python3

import argparse
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
        default=2,
        help="Maximum crawl depth (default: 2)"
    )

    parser.add_argument(
        "-o", "--output",
        choices=["console"],
        default="console",
        help="Output format"
    )
    
    args = parser.parse_args()

    crawler = MailCrawler(start_url=args.url, depth=args.depth)
    results = crawler.run()

    if args.output == "console":
        for email in results:
            print(email)
    else:
        print(f"Export '{args.output}' not implemented yet.")

if __name__ == "__main__":
    main()