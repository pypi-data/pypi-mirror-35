import hashlib
import json
import multiprocessing
import random
# modules in standard library
import re
import sys
import threading
import time
from collections import Counter

from dnz import Engine

# external modules
import dns.resolver
import requests

# Python 2.x and 3.x compatiablity
if sys.version > '3':
    import urllib.parse as urlparse
    import urllib.parse as urllib
else:
    import urlparse
    import urllib

# In case you cannot install some of the required development packages
# there's also an option to disable the SSL warning:
# try:
#     import requests.packages.urllib3
#
#     requests.packages.urllib3.disable_warnings()
# except:
#     pass

# # Check if we are running this on windows platform
# is_windows = sys.platform.startswith('win')
#
#
# class enumratorBase(object):
#     def __init__(self, base_url, engine_name, domain, subdomains=None, silent=False, verbose=True):
#         subdomains = subdomains or []
#         self.domain = urlparse.urlparse(domain).netloc
#         self.session = requests.Session()
#         self.subdomains = []
#         self.timeout = 25
#         self.base_url = base_url
#         self.engine_name = engine_name
#         self.silent = silent
#         self.verbose = verbose
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#             'Accept-Language': 'en-US,en;q=0.8',
#             'Accept-Encoding': 'gzip',
#         }
#         self.print_banner()
#
#     def send_req(self, query, page_no=1):
#
#         url = self.base_url.format(query=query, page_no=page_no)
#         try:
#             resp = self.session.get(url, headers=self.headers, timeout=self.timeout)
#         except Exception:
#             resp = None
#         return self.get_response(resp)
#
#     def get_response(self, response):
#         if response is None:
#             return 0
#         return response.text if hasattr(response, "text") else response.content
#
#     def check_max_subdomains(self, count):
#         if self.MAX_DOMAINS == 0:
#             return False
#         return count >= self.MAX_DOMAINS
#
#     def check_max_pages(self, num):
#         if self.MAX_PAGES == 0:
#             return False
#         return num >= self.MAX_PAGES
#
#     # override
#     def extract_domains(self, resp):
#         """ chlid class should override this function """
#         return
#
#     # override
#     def check_response_errors(self, resp):
#         """ chlid class should override this function
#         The function should return True if there are no errors and False otherwise
#         """
#         return True
#
#     def should_sleep(self):
#         """Some enumrators require sleeping to avoid bot detections like Google enumerator"""
#         return
#
#     def generate_query(self):
#         """ chlid class should override this function """
#         return
#
#     def get_page(self, num):
#         """ chlid class that user different pagnation counter should override this function """
#         return num + 10
#
#     def enumerate(self, altquery=False):
#         flag = True
#         page_no = 0
#         prev_links = []
#         retries = 0
#
#         while flag:
#             query = self.generate_query()
#             count = query.count(self.domain)  # finding the number of subdomains found so far
#
#             # if they we reached the maximum number of subdomains in search query
#             # then we should go over the pages
#             if self.check_max_subdomains(count):
#                 page_no = self.get_page(page_no)
#
#             if self.check_max_pages(page_no):  # maximum pages for Google to avoid getting blocked
#                 return self.subdomains
#             resp = self.send_req(query, page_no)
#
#             # check if there is any error occured
#             if not self.check_response_errors(resp):
#                 return self.subdomains
#             links = self.extract_domains(resp)
#
#             # if the previous page hyperlinks was the similar to the current one, then maybe we have reached the last page
#             if links == prev_links:
#                 retries += 1
#                 page_no = self.get_page(page_no)
#
#                 # make another retry maybe it isn't the last page
#                 if retries >= 3:
#                     return self.subdomains
#
#             prev_links = links
#             self.should_sleep()
#
#         return self.subdomains
#
#
# class enumratorBaseThreaded(multiprocessing.Process, enumratorBase):
#     def __init__(self, base_url, engine_name, domain, subdomains=None, q=None, lock=threading.Lock(), silent=False,
#                  verbose=True):
#         subdomains = subdomains or []
#         enumratorBase.__init__(self, base_url, engine_name, domain, subdomains, silent=silent, verbose=verbose)
#         multiprocessing.Process.__init__(self)
#         self.lock = lock
#         self.q = q
#         return
#
#     def run(self):
#         domain_list = self.enumerate()
#         for domain in domain_list:
#             self.q.append(domain)
#
#
# # host,engine,date,ping,open_ports
#
# class GoogleSearchEngine(Engine):
#     name = 'google_search'
#     base_url = 'https://google.com/search?q={query}&btnG=Search&hl=en-US&biw=&bih=&gbv=1&start={page_no}&filter=0'
#     max_pages = 200
#
#     def extract_domains(self, resp):
#         links_list = list()
#         link_regx = re.compile('<cite.*?>(.*?)<\/cite>')
#         try:
#             links_list = link_regx.findall(resp)
#             for link in links_list:
#                 link = re.sub('<span.*>', '', link)
#                 if not link.startswith('http'):
#                     link = "http://" + link
#                 subdomain = urlparse.urlparse(link).netloc
#                 if subdomain and subdomain not in self.subdomains and subdomain != self.domain:
#                     if self.verbose:
#                         self.print_("%s%s: %s%s" % (R, self.engine_name, W, subdomain))
#                     self.subdomains.append(subdomain.strip())
#         except Exception:
#             pass
#         return links_list
#
#     def check_response_errors(self, resp):
#         if (type(resp) is str or type(resp) is unicode) and 'Our systems have detected unusual traffic' in resp:
#             self.print_(R + "[!] Error: Google probably now is blocking our requests" + W)
#             self.print_(R + "[~] Finished now the Google Enumeration ..." + W)
#             return False
#         return True
#
#     def generate_query(self):
#         if self.subdomains:
#             fmt = 'site:{domain} -www.{domain} -{found}'
#             found = ' -'.join(self.subdomains[:self.MAX_DOMAINS - 2])
#             query = fmt.format(domain=self.domain, found=found)
#         else:
#             query = "site:{domain} -www.{domain}".format(domain=self.domain)
#         return query
#
#
# class YahooSearchEngine(Engine):
#     name = 'yahoo_search'
#     base_url = 'https://search.yahoo.com/search?p={query}&b={page_no}'
#
#     def __init__(self, domain, subdomains=None, q=None, silent=False, verbose=True):
#         subdomains = subdomains or []
#
#         self.engine_name = "Yahoo"
#         self.MAX_DOMAINS = 10
#         self.MAX_PAGES = 0
#
#     def run(self):
#         pass
#
#     def extract_domains(self, resp):
#         link_regx2 = re.compile('<span class=" fz-.*? fw-m fc-12th wr-bw.*?">(.*?)</span>')
#         link_regx = re.compile('<span class="txt"><span class=" cite fw-xl fz-15px">(.*?)</span>')
#         links_list = []
#         try:
#             links = link_regx.findall(resp)
#             links2 = link_regx2.findall(resp)
#             links_list = links + links2
#             for link in links_list:
#                 link = re.sub("<(\/)?b>", "", link)
#                 if not link.startswith('http'):
#                     link = "http://" + link
#                 subdomain = urlparse.urlparse(link).netloc
#                 if not subdomain.endswith(self.domain):
#                     continue
#                 if subdomain and subdomain not in self.subdomains and subdomain != self.domain:
#                     if self.verbose:
#                         self.print_("%s%s: %s%s" % (R, self.engine_name, W, subdomain))
#                     self.subdomains.append(subdomain.strip())
#         except Exception:
#             pass
#
#         return links_list
#
#     def should_sleep(self):
#         return
#
#     def get_page(self, num):
#         return num + 10
#
#     def generate_query(self):
#         if self.subdomains:
#             fmt = 'site:{domain} -domain:www.{domain} -domain:{found}'
#             found = ' -domain:'.join(self.subdomains[:77])
#             query = fmt.format(domain=self.domain, found=found)
#         else:
#             query = "site:{domain}".format(domain=self.domain)
#         return query
#
#
# class AskSearchEngine(Engine):
#     name = 'ask_search'
#     base_url = 'http://www.ask.com/web?q={query}&page={page_no}&qid=8D6EE6BF52E0C04527E51F64F22C4534&o=0&l=dir&qsrc=998&qo=pagination'
#
#     def __init__(self, domain, subdomains=None, q=None):
#         subdomains = subdomains or []
#         self.MAX_DOMAINS = 11
#         self.MAX_PAGES = 0
#         enumratorBaseThreaded.__init__(self, base_url, self.engine_name, domain, subdomains, q=q, silent=silent,
#                                        verbose=verbose)
#         self.q = q
#         return
#
#     def run(self, domain: str):
#         pass
#
#     def extract_domains(self, resp):
#         links_list = list()
#         link_regx = re.compile('<p class="web-result-url">(.*?)</p>')
#         try:
#             links_list = link_regx.findall(resp)
#             for link in links_list:
#                 if not link.startswith('http'):
#                     link = "http://" + link
#                 subdomain = urlparse.urlparse(link).netloc
#                 if subdomain not in self.subdomains and subdomain != self.domain:
#                     if self.verbose:
#                         self.print_("%s%s: %s%s" % (R, self.engine_name, W, subdomain))
#                     self.subdomains.append(subdomain.strip())
#         except Exception:
#             pass
#
#         return links_list
#
#     def get_page(self, num):
#         return num + 1
#
#     def generate_query(self):
#         if self.subdomains:
#             fmt = 'site:{domain} -www.{domain} -{found}'
#             found = ' -'.join(self.subdomains[:self.MAX_DOMAINS])
#             query = fmt.format(domain=self.domain, found=found)
#         else:
#             query = "site:{domain} -www.{domain}".format(domain=self.domain)
#
#         return query
#
#
# class BingSearchEngine(Engine):
#     name = 'bing_search'
#     base_url = 'https://www.bing.com/search?q={query}&go=Submit&first={page_no}'
#
#     def __init__(self, domain, subdomains=None, q=None, silent=False, verbose=True):
#         subdomains = subdomains or []
#
#         self.engine_name = "Bing"
#         self.MAX_DOMAINS = 30
#         self.MAX_PAGES = 0
#         enumratorBaseThreaded.__init__(self, base_url, self.engine_name, domain, subdomains, q=q, silent=silent)
#         self.q = q
#         self.verbose = verbose
#         return
#
#     def run(self, domain: str):
#         pass
#
#     def extract_domains(self, resp):
#         links_list = list()
#         link_regx = re.compile('<li class="b_algo"><h2><a href="(.*?)"')
#         link_regx2 = re.compile('<div class="b_title"><h2><a href="(.*?)"')
#         try:
#             links = link_regx.findall(resp)
#             links2 = link_regx2.findall(resp)
#             links_list = links + links2
#
#             for link in links_list:
#                 link = re.sub('<(\/)?strong>|<span.*?>|<|>', '', link)
#                 if not link.startswith('http'):
#                     link = "http://" + link
#                 subdomain = urlparse.urlparse(link).netloc
#                 if subdomain not in self.subdomains and subdomain != self.domain:
#                     if self.verbose:
#                         self.print_("%s%s: %s%s" % (R, self.engine_name, W, subdomain))
#                     self.subdomains.append(subdomain.strip())
#         except Exception:
#             pass
#
#         return links_list
#
#     def generate_query(self):
#         if self.subdomains:
#             fmt = 'domain:{domain} -www.{domain} -{found}'
#             found = ' -'.join(self.subdomains[:self.MAX_DOMAINS])
#             query = fmt.format(domain=self.domain, found=found)
#         else:
#             query = "domain:{domain} -www.{domain}".format(domain=self.domain)
#         return query
#
#
# class BaiduSearchEngine(Engine):
#     name = 'baidu_search'
#     base_url = 'https://www.baidu.com/s?pn={page_no}&wd={query}&oq={query}'
#     MAX_PAGES = 760
#
#     def __init__(self, domain, subdomains=None, q=None, silent=False, verbose=True):
#         subdomains = subdomains or []
#
#         self.engine_name = "Baidu"
#         self.MAX_DOMAINS = 2
#         self.
#         enumratorBaseThreaded.__init__(self, base_url, self.engine_name, domain, subdomains, q=q, silent=silent,
#                                        verbose=verbose)
#         self.querydomain = self.domain
#         self.q = q
#         return
#
#     def run(self, domain: str):
#         pass
#
#     def extract_domains(self, resp):
#         links = list()
#         found_newdomain = False
#         subdomain_list = []
#         link_regx = re.compile('<a.*?class="c-showurl".*?>(.*?)</a>')
#         try:
#             links = link_regx.findall(resp)
#             for link in links:
#                 link = re.sub('<.*?>|>|<|&nbsp;', '', link)
#                 if not link.startswith('http'):
#                     link = "http://" + link
#                 subdomain = urlparse.urlparse(link).netloc
#                 if subdomain.endswith(self.domain):
#                     subdomain_list.append(subdomain)
#                     if subdomain not in self.subdomains and subdomain != self.domain:
#                         found_newdomain = True
#                         if self.verbose:
#                             self.print_("%s%s: %s%s" % (R, self.engine_name, W, subdomain))
#                         self.subdomains.append(subdomain.strip())
#         except Exception:
#             pass
#         if not found_newdomain and subdomain_list:
#             self.querydomain = self.findsubs(subdomain_list)
#         return links
#
#     def findsubs(self, subdomains):
#         count = Counter(subdomains)
#         subdomain1 = max(count, key=count.get)
#         count.pop(subdomain1, "None")
#         subdomain2 = max(count, key=count.get) if count else ''
#         return (subdomain1, subdomain2)
#
#     def check_response_errors(self, resp):
#         return True
#
#     def should_sleep(self):
#         time.sleep(random.randint(2, 5))
#         return
#
#     def generate_query(self):
#         if self.subdomains and self.querydomain != self.domain:
#             found = ' -site:'.join(self.querydomain)
#             query = "site:{domain} -site:www.{domain} -site:{found} ".format(domain=self.domain, found=found)
#         else:
#             query = "site:{domain} -site:www.{domain}".format(domain=self.domain)
#         return query
