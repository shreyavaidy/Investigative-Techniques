import requests #for http requests 
import re #for regular expressions
from bs4 import BeautifulSoup #to use Beautiful Soup

target_url = "https://www1.nyc.gov/site/nypd/stats/crime-statistics/borough-and-precinct-crime-stats.page"
# Susan prefers storing the contents of the URL locally in a cache rather than calling the website each time.
# This is because repeatedly scraping off a website could tip off the wesbsite. Plus, you can tinker with the local copy as much as you like until you have figured out your scrapper

#page_contents = requests.get(target_url)
#page_data = page_contents.text

#local_copy = open("NYPD_crime_states.html","w")
#local_copy.write(page_data)
#local_copy.close()

is_excel = re.compile(".*xlsx")

souped_data = BeautifulSoup(open("NYPD_crime_states.html","r"),"html.parser")

data_div = souped_data.find('div', class_="about-description")

all_links = data_div.find_all('a')

for link in all_links:
	if is_excel.match(link['href']):
		print(link['href'])
