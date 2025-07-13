# Project Title: VergeScraper

Author: Norman McCord  
Course: IS 3020 Application Development  
Semester: Summer 2025  

## Description

VergeScraper is a Python-based web scraper that extracts the latest article headlines from The Verge homepage. This is a proof-of-concept and is hard-coded to work with theverge.com website. My goal is to create the origins of a tool that can be used on any news feed site. The tool fetches live page data, filters for news article links, and stores the first 10 headlines and URLs in a timestamped CSV file.

## Features

- Connects to https://www.theverge.com
- Filters and extracts article headlines and links
- Saves output to a CSV file with a timestamp
- Handles duplicate and empty link filtering
- Simple command-line feedback for visibility

## How to Run

1. Clone the repository:
   git clone https://github.com/KSU-IS/verge-scraper.git

2. Navigate to the project folder:
   cd verge-scraper

3. Run the script:
   python .\VergeScraper.py (*PowerShell 7 syntax*)

## Files

- [VergeScraper](VergeScraper).py - main Python script
- README.md - project overview
- [Project Roadmap](projectroadmap.md) - sprint task tracking and updates

## Notes

- Output CSV files will be named like `theverge_headlines_YYYY-MM-DD_HH-MM.csv`.
- See [Project Roadmap](projectroadmap.md) for sprint task progress and planning.
- Ensure you have the required libraries installed: `requests`, `beautifulsoup4`.

## Web-Scraper-using-BeautifulSoup
Web Scraping done using python and beautifulsoup4

This is a fork of [mfakharealam's](https://github.com/mfakharealam/Web-Scraper-using-BeautifulSoup) project.  I'm working to remove the reliance on H2 headers or other CSS attributes as these methods of SEO are being used less on webpages.  This pulls heaadlines and URLs from theverge.com only.    
