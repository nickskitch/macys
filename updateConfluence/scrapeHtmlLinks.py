__author__ = 'Nick'


from bs4 import BeautifulSoup
import urllib2
url = """
http://www.reddit.com/r/videos/comments/241eqc/comedian_ronny_chieng_breaks_down_kanye_west/
"""

data = urllib2.urlopen(url)


soup = BeautifulSoup(data)
for link in soup.findAll("a"):
    href = str(link.get("href"))
    if href.find("reddit")==-1:
        #print link.get("href")
        if href.find("http")>=0:
            print link.get("href")

