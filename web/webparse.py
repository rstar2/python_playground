import requests, webbrowser, bs4

# this just opens the browser
webbrowser.open("http://abv.bg")

# get a page 
abvBg_res = requests.get('http://abv.bg')
#  check for valid status
abvBg_res.raise_for_status()

#  create a "soup" object - similar to jQuery
abvBg_Soup = bs4.BeautifulSoup(abvBg_res.text)

abvBg_Soup.select('div')
abvBg_Soup.select('#author')
abvBg_Soup.select('div > span')
abvBg_Soup.select('input[type="button"]')
