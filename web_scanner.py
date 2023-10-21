#!/usr/bin/env python3
# coding: utf-8

import threading
import urllib
import urllib.request
import urllib.response
import sys
import mechanize
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib3


class WebScanner:

    def __init__(self, url, proxy=None, user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0"):
        if not url.endswith("/")and not url.endswith(".php") and not url.endswith(".html"):
            self.url = url + "/"
        else:
            self.url = url
            self.proxy = proxy
            self.user_agent = user_agent
            self.browser = mechanize.Browser()
            self.link_list = []
            self.stopped = False


    def print_link_list(self):
        """
        Displays the links list to the terminal
        :return:
        """
        for link in self.link_list:
            print(link)


    def get_page_source(self, page=None):
        """
        Get a page source code
        :param page: optional : the requested page, if not set the default instance url is used
        :return: HTML source code of page
        """

        if page is None:
            page = self.url
        self.browser.set_handle_robots(False)
        user_agent = [("User-agent", self.user_agent)]
        self.browser.addheaders = user_agent
        if self.proxy:
            self.browser.set_proxies(self.proxy)
        page = page.strip()
        try:
            res = self.browser.open(page)
        except Exception as e:
            print("Erreur pour la page : " + page + " " + str(e))
            return None
        return res


    def get_page_links(self, page=None):
        """
        Get the links available in a page (href)
        :param page: the requested page, if not set the default instance url is used
        :return: a list containing the urls of the page,  or an empty list
        """

        link_list = []
        if page is None:
            page = self.url
            source =self.get_page_source(page)
        if source is not None:
            soup= BeautifulSoup(source, "html.parser")
            uparse = urlparse(page)
            for link in soup.find_all("a"):
                if not link.get("href") is None:
                    href = link.get("href")
                    if "#" in href:
                        href = href.split("#")[0]
                    new_link = urllib3.parse.urljoin()
                    if uparse.hostname in new_link and new_link not in link_list:
                        link_list.append(new_link)
                return link_list
            else:
                return []


    def print_cookies(self):
        """
        Display the cookies from the browser object
        :return:
        """
        for cookie in self.browser.cookiejar:
            print(cookie)


    def get_cookies(self):
        """
        Returns the cookies from the browser object
        :return: a list of all the cookies
        """

        cookies_list = []
        for cookies in self.browser.cookiejar:
            cookies_list.append(cookies)
        return cookies_list


    def _do_crawl(self, queue, page=None):
        try:
            page_links = self.get_page_links(page)
            for link in page_links:
                if self.stopped:
                    break
                if link not in self.link_list:
                    self.link_list.append(link)
                    queue.put(link)
                    self._do_crawl(queue, link)
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            sys.exit(1)
        except Exception as e:
            print("Error :" + str(e))
            sys.exit(1)


    def _crawl_end_callback(self, crawl_thread, crawl_queue):
        crawl_thread.join()
        crawl_queue.put("END")


    def crawl(self, crawl_queue, page=None):
        crawl_thread = threading.Thread(target=self._do_crawl, args=(crawl_queue,page))
        crawl_thread.start()
        thread2 = threading.Thread(target=self._crawl_end_callback, args=(crawl_thread, crawl_queue))
        thread2.start()

    # def crawl(self,page=None):
    #     """
    #     Crawl a page recursively, adding the links to the url list
    #     :param page: the requested page, if not set the default instance url is used
    #     :return:
    #     """

    #     try:
    #         page_links = self.get_page_links(page)
    #         for link in page_links:
    #             if self.stopped:
    #                 break
    #             if link not in self.link_list:
    #                 self.link_list.append(link)
    #                 print("Link addeed to the list : " + link)
    #                 self.crawl(link)
    #     except KeyboardInterrupt:
    #         print("\nProgram interrupted by user.")
    #         sys.exit(1)
    #     except Exception as e:
    #         print("Error :" + str(e))
    #         sys.exit(1)