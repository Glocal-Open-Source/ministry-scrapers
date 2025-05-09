# ministry-scrapers

This project will scrape the information of every provinces Ministries, Crown Corps, and other Authorities.

Each province has a config and scraper in its respective folder.

Config contains all urls neccessary for retrieving the following information:

```
                      fields
              -----------------------
             | Type              str |
             | Ministry          str |
             | Role              str |
             | Honorable         bool|
             | Name              str |
             | French            bool|
             | Biography         str |
             | Contact URL       str |
             | Contact Phone     str |
             | Office            str |
              -----------------------
```
Scrapers will be unique for each source url - in the case of BC, we will need no more than 2 scrapers to retrieve all of this info. 
