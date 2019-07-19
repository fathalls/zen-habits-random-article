import urllib2,bs4,webbrowser,random
# import bs4
# import webbrowser
# import random

request = urllib2.Request('https://zenhabits.net/archives/')
request.add_header('User-Agent', 'ScrapingAuthority (ScrapingAuthority.com')
open = urllib2.urlopen(request)
page = bs4.BeautifulSoup(open, 'html.parser')
link_tags = page.find_all('a')
size = len(link_tags)
number = random.randint(0, size+1)
url = link_tags[number].get('href')
webbrowser.open(url)




