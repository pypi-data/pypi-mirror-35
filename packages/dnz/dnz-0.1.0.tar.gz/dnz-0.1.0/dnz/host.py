import datetime
import logging
import socket
from typing import List

import tldextract
from .utils import is_valid_hostname, ping
import dns.resolver

log = logging.getLogger(__name__)


class Host:
    def __init__(self, url: str):
        """

        Args:
            url:
        """
        self.__parse_url(url)
        self.verified = False
        self.last_scan = ''
        self.ports_scanned = {}

    def __parse_url(self, url: str):
        self.parts = tldextract.extract(url)

    @property
    def is_valid(self):
        """
        Whether the host is a valid hostname

        Returns:
            bool
        """
        return is_valid_hostname(self.fqdn)

    @property
    def sub_domain(self):
        """
        Subdomain
        Returns:

        """
        return self.parts.subdomain

    @property
    def domain(self):
        """
        Domain
        Returns:

        """
        return self.parts.domain

    @property
    def suffix(self):
        """
        Suffix
        Returns:

        """
        return self.parts.suffix

    @property
    def fqdn(self):
        """
        fqdn
        Returns:

        """
        return self.parts.fqdn

    def add_sub_domain(self, sub_domain: str):
        current_sub_domain = self.sub_domain.split('.')
        current_sub_domain.insert(0, sub_domain)
        new_sub_domain = '.'.join([item for item in current_sub_domain if item])
        updated_url = '{}.{}.{}'.format(
            new_sub_domain, self.domain, self.suffix)
        self.__parse_url(updated_url)

    def replace_sub_domain(self, sub_domain: str):
        updated_url = '{}.{}.{}'.format(
            sub_domain, self.domain, self.suffix)
        self.__parse_url(updated_url)

    def to_dict(self):
        pass

    @property
    def source(self):
        return {
            'original': '',
            'all': []
        }

    @property
    def resolvers_processed(self):
        return []

    @property
    def resolvers_count(self):
        return []

    @property
    def resolvers_pct(self):
        return []

    @property
    def open_ports(self):
        """

        Returns:

        """
        return [port for port in self.ports_scanned.keys() if self.ports_scanned[port]['is_open']]

    @property
    def closed_ports(self):
        """

        Returns:

        """
        return [port for port in self.ports_scanned.keys() if not self.ports_scanned[port]['is_open']]

    def scan_ports(self, ports: List[int]):
        """
        Scan list of ports for TCP connection
        Args:
            ports:

        Returns:

        """
        log.debug('Performing port scan for host %s on %s ports', self.fqdn, len(ports))
        for port in ports:
            is_open = self.__check_port(port)
            self.ports_scanned[port] = {'is_open': is_open, 'checked_at': datetime.datetime.now(datetime.timezone.utc)}
        log.debug('Completed port scan for host %s on %s ports', self.fqdn, len(ports))
        return self.ports_scanned

    def __check_port(self, port: int, timeout: int = 2):
        log.debug('Checking open port for host %s on %s', self.fqdn, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            result = s.connect_ex((self.fqdn, port))
            s.close()
        except Exception as error:
            log.debug('Checking open port for host %s on %s', self.fqdn, port)
            return False
        if result == 0:
            log.debug('Checking open port for host %s on %s', self.fqdn, port)
            return True
        else:
            log.debug('Checking open port for host %s on %s', self.fqdn, port)
            return False

    def ping(self):
        return ping(self.fqdn)

    def check_port(self, port: int):
        """
        Verify that host is up using TCP connection
        """
        return self.__check_port(port)

    def scan_results(self):
        return {'host': self.fqdn, 'engines': []}

    def dns(self):
        is_valid = False
        Resolver = dns.resolver.Resolver()
        Resolver.nameservers = ['8.8.8.8', '8.8.4.4']
        self.lock.acquire()
        return Resolver.query(self.fqdn, 'A')[0].to_text()

    def __str__(self):
        return self.fqdn

    def __repr__(self):
        return '<Host: {}>'.format(self.fqdn)
