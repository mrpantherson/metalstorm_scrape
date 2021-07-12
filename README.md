# Metal Storm Spider Scraper
A simple scraper for the website MetalStorm.net using scrapy. Some small improvements can be made to this that I might get around to, but for now just load up req.txt and it will scrape basic information from the site and store it in a csv/json.

## Usage: In terminal
scrapy crawl metalspider -O file.csv

## TODO
* don't hard code pages, follow links to the end
* scrape each band page individually for more information
* sort output after scraping
* clean req.txt
