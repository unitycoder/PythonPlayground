# https://kazuar.github.io/scraping-tutorial/
# Login to website with CSRF token

import requests
from lxml import html

URL = 'http://yourtarget.url/login'

with requests.session() as client:
    loginpage = client.get(URL)
    
    tree = html.fromstring(loginpage.text)
    
    # parse hidden csrf field from login page (use view source to find its name first)
    csrftoken = list(set(tree.xpath("//input[@name='_csrf']/@value")))[0]
    
    login_data = {'username':'redtruck','password':'420', 'csrfmiddlewaretoken':csrftoken}
    loggedinpage=client.post(URL,data=login_data)

    print loggedinpage.text
