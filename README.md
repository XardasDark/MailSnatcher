# MailSnatcher
A simple Email Crawler for training purposes, written in Python.

## Planned Features

#### 🔍 Crawler-Features
- Recursive crawling
  - Navigate through all linked pages – with configurable depth
- Crawl-History
  - Remember pages already visited → never crawl twice
- Domain limitation
  - Only crawl within the specified domain so that it does not crawl the entire internet
- Rate limiting / crawl delay
  - This prevents the server from becoming overloaded or blocking the crawler
- Parallel Crawler Threads
  - Faster collection through multi-threading / async
- Batch mode
  - Import list of websites → process automatically

#### 📧 Email detection
- Detection of 'hidden' emails
(e.g. name [at] domain [dot] com, info(at)example.com → automatically convert to normal format)
- Detection in JavaScript / obfuscated strings
  - Matching in \<script> blocks or base64-encoded strings
- Whitelist/blacklist filter
  - Include or exclude domains or TLDs (e.g. only .uk, .com)
- Duplicate filter
  - No multiple results

#### 🧠 Intelligence + Analysis
- Ranking / Confidence Score
  - Sort relevant emails higher, e.g. 'contact'/'info' < 'name@company'
- Semantic context analysis
  - Which email belongs to which name/department?
- Evaluation of social media links
  - Check LinkedIn/GitHub/imprint pages specifically

#### ⤵️ Export & Output
- Export to CSV / JSON / TXT
- Live display in the console
  - Progress bar, emails found, crawling statistics
- Option to save to an SQLite or MySQL database
- Output sorted by domain / page

#### 🔮 Maybe in future
- GUI
- API mode
- Keyword search
  - Not just emails, but also phone numbers, names, etc.
- Crawler scheduler
  - Run at specific times
- Deploy it as Docker-Container, Debian Package, etc.

## Installation
ToDo

## Usage
ToDo