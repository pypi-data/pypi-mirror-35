import datetime
import json
import logging
import concurrent.futures
from typing import Union

from .engine import Engine
from .host import Host
from .utils import generate_name

logging.basicConfig(level=logging.INFO)


class Scanner:
    """
    Scanner
    """
    def __init__(self, target: str, engines_paths: list = list('hi'), word_list_path: str = None,
                 output_file_path: str = None,
                 max_domains: int = None, max_levels: int = 5, engine_timeout: int = None, scan_ports: list = None,
                 workers: int = 1,
                 log_level: str = 'INFO'):
        self.target = Host(target)

        self.engines_paths = engines_paths

        self.max_domains = max_domains
        self.max_levels = max_levels
        self.scan_ports = scan_ports
        self.engine_timeout = engine_timeout
        self.engines = []
        self.domains = []
        self._target_set = set()

        self.log = logging.getLogger('dnz.Scanner')
        # self.log.setLevel(log_level)
        self.scanners = []

    def add_scanner(self, engine: Union[str, Engine]):
        """
        Add engine to list of engines to be run
        """
        if not isinstance(engine, Engine):
            raise TypeError('Engines must be instances of the Engine class')

        if engine not in self.engines:
            self.engines.append(engine)
            self.log.debug('Engine added to list of engines')
        else:
            self.log.debug('')

    def remove_engine(self, engine: Union[str, Engine]):
        """
        Remove engine from list of engines to be run
        """
        if not isinstance(engine, Engine):
            raise TypeError('Engines must be instances of the Engine class')

        if engine in self.engines:
            self.engines.remove(engine)
            self.log.debug('Engine removed from list of engines')
        else:
            self.log.debug('')

    def run(self, threaded: bool = False):
        if self.output_file_path:
            self.log.debug('Opening output path at %s', self.output_file_path)
            self.output_file_handler = open(self.output_file_path, 'w')

        # if self.workers > 0:
        #     with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        #         future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        #         for future in concurrent.futures.as_completed(future_to_url):
        #             url = future_to_url[future]
        #             try:
        #                 data = future.result()
        #             except Exception as exc:
        #                 print('%r generated an exception: %s' % (url, exc))
        #             else:
        #                 print('%r page is %d bytes' % (url, len(data)))

        for engine in self.engines:
            for host in engine.run():
                if isinstance(host, str):
                    valid_domain = True
                elif isinstance(host, list):
                    for item in host:
                        if isinstance(item, str):
                            valid_domain = True
                        else:
                            valid_domain = False
                else:
                    valid_domain = False

                if valid_domain:
                    self.target_set.add(host)
                    self.domains.append(host)
                    if self.output_file_path:
                        data = ''
                        json.dump(data, self.output_file_handler, indent=4)

        if self.scan_ports:
            for host in self.domains:
                host.scan_ports(self.scan_ports)

                if self.output_file_path:
                    data = ''
                    json.dump(data, self.output_file_handler, indent=4)

    def stop(self):
        if self.output_file_path:
            self.output_file_handler.close()
            self.log.debug('Close output file at %s', self.output_file_path)

    @property
    def targets(self):
        return list(self.target_set)

    def clear_targets(self):
        self.target_set = set()

    # def write_rows(self):
    #     fieldnames = ['first_name', 'last_name', 'Grade']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()
    #     writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
    #     writer.writerows([{'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'},
    #                       {'Grade': 'A', 'first_name': 'Rachael',
    #                        'last_name': 'Rodriguez'},
    #                       {'Grade': 'C', 'first_name': 'Tom', 'last_name': 'smith'},
    #                       {'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},
    #                       {'Grade': 'A', 'first_name': 'Kennzy', 'last_name': 'Tim'}])

    def __str__(self):
        return self.target.fqdn

    def __repr__(self):
        return '<Scanner: {}>'.format(self.target.fqdn)


class Scan:
    def __init__(self):
        self.name = generate_name()
        self.start_date = datetime.datetime.now(datetime.timezone.utc)
        self.file_name = ''

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Scan: {}>'.format(self.name)
