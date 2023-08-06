from dnz import Engine
from dnz.utils import is_valid_hostname
from typing import List
import dns.resolver

DEFAULT_RECORDS = [
    'NONE',
    'A',
    'ALIAS',
    'NS',
    'MD',
    'MF',
    'CNAME',
    'SOA',
    'MB',
    'MG',
    'MR',
    'NULL',
    'WKS',
    'PTR',
    'HINFO',
    'MINFO',
    'MX',
    'TXT',
    'RP',
    'AFSDB',
    'X25',
    'ISDN',
    'RT',
    'NSAP',
    'NSAP-PTR',
    'SIG',
    'KEY',
    'PX',
    'GPOS',
    'AAAA',
    'LOC',
    'NXT',
    'SRV',
    'NAPTR',
    'KX',
    'CERT',
    'A6',
    'DNAME',
    'OPT',
    'APL',
    'DS',
    'SSHFP',
    'IPSECKEY',
    'RRSIG',
    'NSEC',
    'DNSKEY',
    'DHCID',
    'NSEC3',
    'NSEC3PARAM',
    'TLSA',
    'HIP',
    'CDS',
    'CDNSKEY',
    'CSYNC',
    'SPF',
    'UNSPEC',
    'EUI48',
    'EUI64',
    'TKEY',
    'TSIG',
    'IXFR',
    'AXFR',
    'MAILB',
    'MAILA',
    'ANY',
    'URI',
    'CAA',
    'TA',
    'DLV',
]


class DNSResolverEngine(Engine):
    name = 'dns_resolver'

    def __init__(self, records: List[str] = None):
        if not records:
            self.records = DEFAULT_RECORDS
        else:
            self.records = records

    def run(self, domain: str):
        """
        Get all the records associated to domain parameter.
        """
        data = []
        for record in self.records:
            try:
                answers = dns.resolver.query(domain, record)
                for rdata in answers:
                    if is_valid_hostname(rdata.to_text()):
                        data.append(rdata.to_text())
            except Exception as e:
                pass

        return data
