from dnz import Engine
from dnz.host import Host


class WordListEngine(Engine):
    name = 'word_list'

    def __init__(self, word_list_path):
        self.word_list_path = word_list_path
        self.word_list = []
        self.target_set = set()

        if self.word_list_path:
            with open(self.word_list_path, 'r'):
                self._open_word_list()

    def run(self, domain: str):
        self.generate_targets(domain)
        return list(self.target_set)

    def _open_word_list(self):
        with open(self.word_list_path, 'r') as fh:
            self.word_list = fh.read().splitlines()

    def reload_word_list(self):
        """
        Reload word list
        """
        self._open_word_list()

    def additional_sub_domains(self, domain: str, limit: int = None):
        for word in self.word_list[:limit]:
            new_target = Host(domain)
            new_target.add_sub_domain(word)
            self.target_set.add(new_target.fqdn)

    def numbered_sub_domains(self, domain: str, separator: str = '-', max_num: int = 10):
        if Host(domain).sub_domain:
            for num in range(1, max_num + 1):
                new_target = Host(domain)
                new_sub_domain = new_target.sub_domain + separator + str(num)
                new_target.replace_sub_domain(new_sub_domain)
                self.target_set.add(new_target.fqdn)

                new_target = Host(domain)
                new_sub_domain = new_target.sub_domain + str(num)
                new_target.replace_sub_domain(new_sub_domain)
                self.target_set.add(new_target.fqdn)

    def dashed_sub_domains(self, domain: str, separator: str = '-', limit: int = None):
        if Host(domain).sub_domain:
            for word in self.word_list[:limit]:
                new_target = Host(domain)
                new_sub_domain = new_target.sub_domain + separator + word
                new_target.replace_sub_domain(new_sub_domain)
                self.target_set.add(new_target.fqdn)

                new_target = Host(domain)
                new_sub_domain = word + separator + new_target.sub_domain
                new_target.replace_sub_domain(new_sub_domain)
                self.target_set.add(new_target.fqdn)

    def generate_targets(self, domain: str, target_types='all'):
        """
        Generate additional domain targets
        """
        if target_types == 'all':
            target_types = ['additional', 'numbered', 'dashed']
        else:
            target_types = [target_types]

        for method in target_types:
            if callable(getattr(self, f'{method}_sub_domains')):
                getattr(self, f'{method}_sub_domains')(domain)
