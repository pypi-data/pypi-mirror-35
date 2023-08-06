import requests
from dnz import Engine
import re


class DNSdumpsterEngine(Engine):
    name = 'dns_dumpster'
    base_url = 'https://dnsdumpster.com/'

    def __init__(self):
        self.session = requests.Session()

    def run(self, domain: str):
        resp = self.req('GET', self.base_url)
        token = self.get_csrftoken(resp)
        params = {'csrfmiddlewaretoken': token, 'targetip': domain}
        post_resp = self.req('POST', self.base_url, params)
        return self.extract_domains(post_resp, domain)

    def req(self, req_method, url, params=None):
        params = params or {}
        headers = {}
        headers['Referer'] = 'https://dnsdumpster.com'
        try:
            if req_method == 'GET':
                resp = self.session.get(url, headers=headers, timeout=10)
            else:
                resp = self.session.post(url, data=params, headers=headers, timeout=10)
        except Exception as e:
            print(e)
            resp = None
        return resp

    def get_csrftoken(self, resp):
        csrf_regex = re.compile("<input type='hidden' name='csrfmiddlewaretoken' value='(.*?)' />", re.S)
        token = csrf_regex.findall(resp.text)[0]
        return token.strip()

    def extract_domains(self, resp, domain):
        extracted_domains = []
        tbl_regex = re.compile('<a name="hostanchor"><\/a>Host Records.*?<table.*?>(.*?)</table>', re.S)
        link_regex = re.compile('<td class="col-md-4">(.*?)<br>', re.S)
        try:
            results_tbl = tbl_regex.findall(resp.text)[0]
        except IndexError:
            results_tbl = ''
        links_list = link_regex.findall(results_tbl)
        links = list(set(links_list))
        for link in links:
            subdomain = link.strip()
            if not subdomain.endswith(domain):
                continue
            if subdomain and subdomain not in extracted_domains and subdomain != domain:
                extracted_domains.append(subdomain.strip())
        return extracted_domains


class VirusTotalEngine(Engine):
    name = 'virus_total'
    base_url = 'https://www.virustotal.com/en/domain/{domain}/information/'

    def run(self, domain: str):
        url = self.base_url.format(domain=domain)
        resp = requests.get(url)
        if not resp:
            return
        return self.extract_domains(resp, domain)

    def extract_domains(self, resp, domain):
        extracted_domains = []
        link_regx = re.compile('<div class="enum.*?">.*?<a target="_blank" href=".*?">(.*?)</a>', re.S)
        try:
            links = link_regx.findall(resp.text)
            for link in links:
                subdomain = link.strip()
                if not subdomain.endswith(domain):
                    continue
                if subdomain not in extracted_domains and subdomain != domain:
                    extracted_domains.append(subdomain.strip())
        except Exception:
            pass

        return extracted_domains


class ThreatCrowdEngine(Engine):
    name = 'threat_crowd'
    base_url = 'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}'

    def run(self, domain: str):
        url = self.base_url.format(domain=domain)
        resp = requests.get(url)
        if not resp:
            return
        return self.extract_domains(resp, domain)

    def extract_domains(self, resp, domain):
        extracted_domains = []

        try:
            links = resp.json()['subdomains']
            for link in links:
                subdomain = link.strip()
                if not subdomain.endswith(domain):
                    continue
                if subdomain not in extracted_domains and subdomain != domain:
                    extracted_domains.append(subdomain.strip())
        except Exception as e:
            print(e)

        return extracted_domains


class CRTSearchEngine(Engine):
    name = 'crt_search'
    base_url = 'https://crt.sh/?q=%25.{domain}'

    def run(self, domain: str):
        url = self.base_url.format(domain=domain)
        resp = requests.get(url)
        if not resp:
            return
        return self.extract_domains(resp, domain)

    def extract_domains(self, resp, domain):
        extracted_domains = []

        link_regx = re.compile('<TD>(.*?)</TD>')
        try:
            links = link_regx.findall(resp.text)
            for link in links:
                subdomain = link.strip()
                if not subdomain.endswith(domain) or '*' in subdomain:
                    continue

                if '@' in subdomain:
                    subdomain = subdomain[subdomain.find('@') + 1:]

                if subdomain not in extracted_domains and subdomain != domain:
                    extracted_domains.append(subdomain.strip())
        except Exception as e:
            print(e)

        return extracted_domains


class PassiveDNSEngine(Engine):
    name = 'passive_dns'
    base_url = 'https://api.sublist3r.com/search.php?domain={domain}'

    def run(self, domain: str):
        url = self.base_url.format(domain=domain)
        resp = requests.get(url)
        if not resp:
            return
        return self.extract_domains(resp, domain)

    def extract_domains(self, resp, domain):
        extracted_domains = []
        try:
            subdomains = resp.json()
            for subdomain in subdomains:
                if subdomain not in extracted_domains and subdomain != domain:
                    extracted_domains.append(subdomain.strip())
        except Exception as e:
            pass

        return extracted_domains
