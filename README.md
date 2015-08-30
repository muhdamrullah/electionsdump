This file is a script that dumps data from a polling site.

To run code:

scrapy runspider properworu.py -s CONCURRENT_REQUESTS=1000 -s CONCURRENT_REQUESTS_PER_DOMAIN=1000 -s REDIRECT_MAX_TIMES=0 -o worunew.csv
