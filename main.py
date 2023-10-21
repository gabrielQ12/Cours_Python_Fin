#!/usr/bin/env python3
# coding: utf-8

import mechanize
from bs4 import BeautifulSoup


def view_page(url, proxy=None):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    user_agent = [("User-agent", "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0")]
    browser.addheaders = user_agent
    if proxy:
        browser.set_proxies(proxy)
    page = browser.open(url)
    for cookie in browser.cookiejar:
        print(cookie)
    print(page.read())


view_page('https://icanhazip.com') #{"https" : "212.34.250.14:3128"}
