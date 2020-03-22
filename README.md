# Please note this is a work in progress. If you just want to use the script, [check this out](https://github.com/kaustubhd93/adstxt-crawler.git)

## A WEB app for crawling ads.txt of desired domains
- User will login with credentials, upload a file with a list of domains in a certain format and schedule a crawl.
- Once crawling is done. User can download the tar file which will have all ads.txt content in csv format.

### What is ads.txt?
- [Tell me](https://github.com/kaustubhd93/adstxt-crawler/wiki/Ads.txt-concepts)  

## Format for file with list of domains.
NOTE: List of domains should be written separately each on a new line.  
```
domain1.xyz  
domain2.xyz  
www.domain3.xyz  
```

## File structure

```
adstxt/           --- Helper scripts, spiders and other scrapy files.  
adstxtui/         --- All UI related files.  
archives/         --- Old archived code for reference.  
crawl.sh          --- script to run spiders.  
docs/             --- Required documents for reference.  
requirements.txt  --- List of python libraries required by this app.  
```
