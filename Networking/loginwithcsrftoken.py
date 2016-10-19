# https://kazuar.github.io/scraping-tutorial/
# Login to website with CSRF token

import requests
from lxml import html

URL = 'http://yourtarget.url/login'

with requests.session() as client:
    # first grab the initial csfr token from login page
    loginpage = client.get(URL)
    # if you get SSL error (using self signed), then add verify=False
    # loginpage = client.get('URL', verify=False)

    # parse hidden csrf field from login page (use view source to find its name first)
    tree = html.fromstring(loginpage.text)
    csrftoken = list(set(tree.xpath("//input[@name='_csrf']/@value")))[0]
    
    # do actual login form submission, note csrfmiddlewaretoken could have different names like "csrfmiddlewaretoken"
    payload = {'username':'redtruck','password':'420', '_csrf':csrftoken}
    loggedinpage=client.post(URL,data=payload)

    # display logged in page
    #print loggedinpage.text
    
    # again parse hidden csrf field from logged-in page, its different from initial _csfr
    tree = html.fromstring(loggedinpage.text)
    csrftoken = list(set(tree.xpath("//input[@name='_csrf']/@value")))[0]
    
    # now can access sub pages as you are logged in and have the logged in csfr token
    URL = 'http://yourtarget.url/home'
    headers = dict(referer = URL)
    payload = {'something': 'benchman', '_csrf':csrftoken}
    response = client.post(URL, data=payload, headers=headers)
    
    print response.text

    
