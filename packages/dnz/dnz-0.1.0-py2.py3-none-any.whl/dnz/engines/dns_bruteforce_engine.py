import random
import uuid
from dnz import Engine


class DNSResolver(Engine):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8',
        'Accept-Encoding': 'gzip',
    }

    def __init__(self, record_type: str = 'A'):
        super(DNSResolver).__init__()

    # This process cannot block forever,  it  needs to check if its time to die.
    def add_nameserver(self, nameserver: str):
        """
        Add nameserver
        """
        keep_trying = True
        while not self.time_to_die and keep_trying:
            try:
                self.resolver_q.put(nameserver, timeout=1)
                trace("Added nameserver:", nameserver)
                keep_trying = False
            except Exception as e:
                if type(e) == Queue.Full or str(type(e)) == "<class 'queue.Full'>":
                    keep_trying = True

    def verify(self, nameserver_list: list):
        """
        Verify DNS resolvers work
        """
        added_resolver = False
        for server in nameserver_list:
            if self.time_to_die:
                break
            server = server.strip()
            if server:
                self.resolver.nameservers = [server]
                try:
                    # test_result = self.resolver.query(self.most_popular_website, "A")
                    # should throw an exception before this line.
                    if True:  # test_result:
                        # Only add the nameserver to the queue if we can detect wildcards.
                        if (self.find_wildcards(self.target)):  # and self.find_wildcards(".com")
                            # wildcards have been added to the set, it is now safe to be added to the queue.
                            # blocking queue,  this process will halt on put() when the queue is full:
                            self.add_nameserver(server)
                            added_resolver = True
                        else:
                            trace("Rejected nameserver - wildcard:", server)
                except Exception as e:
                    # Rejected server :(
                    trace("Rejected nameserver - unreliable:", server, type(e))
        return added_resolver

    # Only add the nameserver to the queue if we can detect wildcards.
    # Returns False on error.
    def find_wildcards(self, host: str):
        """
        Find wildcards on DNS resolver
        """
        # We want sovle the following three problems:
        # 1)The target might have a wildcard DNS record.
        # 2)The target maybe using geolocaiton-aware DNS.
        # 3)The DNS server we are testing may respond to non-exsistant 'A' records with advertizements.
        # I have seen a CloudFlare Enterprise customer with the first two conditions.
        try:
            # This is case #3,  these spam nameservers seem to be more trouble then they are worth.
            wildtest = self.resolver.query(uuid.uuid4().hex + ".com", "A")
            if len(wildtest):
                trace("Spam DNS detected:", host)
                return False
        except:
            pass
        test_counter = 8
        looking_for_wildcards = True
        while looking_for_wildcards and test_counter >= 0:
            looking_for_wildcards = False
            # Don't get lost, this nameserver could be playing tricks.
            test_counter -= 1
            try:
                testdomain = "%s.%s" % (uuid.uuid4().hex, host)
                wildtest = self.resolver.query(testdomain, self.record_type)
                # This 'A' record may contain a list of wildcards.
                if wildtest:
                    for w in wildtest:
                        w = str(w)
                        if w not in self.wildcards:
                            # wildcards were detected.
                            self.wildcards[w] = None
                            # We found atleast one wildcard, look for more.
                            looking_for_wildcards = True
            except Exception as e:
                if type(e) == dns.resolver.NXDOMAIN or type(e) == dns.name.EmptyLabel:
                    # not found
                    return True
                else:
                    # This resolver maybe flakey, we don't want it for our tests.
                    trace("wildcard exception:", self.resolver.nameservers, type(e))
                    return False
        # If we hit the end of our depth counter and,
        # there are still wildcards, then reject this nameserver because it smells bad.
        return (test_counter >= 0)

    def run(self, domain: str):
        """
        Run the resolver
        """
        # Every user will get a different set of resovlers, this helps redistribute traffic.
        random.shuffle(self.resolver_list)
        if not self.verify(self.resolver_list):
            # This should never happen,  inform the user.
            sys.stderr.write('Warning: No nameservers found, trying fallback list.\n')
            # Try and fix it for the user:
            self.verify(self.backup_resolver)
        # End of the resolvers list.
        try:
            self.resolver_q.put(False, timeout=1)
        except:
            pass

    def stop(self):
        """
        Stop the resolver
        """
        self.time_to_die = True

    def get_cname(q, target: str, resolved_out):
        global progress
        global lock
        global starttime
        global found
        global resolverName
        lock.acquire()
        progress += 1
        lock.release()
        if progress % 500 == 0:
            lock.acquire()
            left = linecount - progress
            secondspassed = (int(time.time()) - starttime) + 1
            amountpersecond = progress / secondspassed
            lock.release()
            timeleft = str(datetime.timedelta(seconds=int(left / amountpersecond)))
            print(
                colored("[*] {0}/{1} completed, approx {2} left".format(progress, linecount, timeleft),
                        "blue"))
        final_hostname = target
        result = list()
        result.append(target)
        resolver = dns.resolver.Resolver()
        if (resolverName is not None):  # if a DNS server has been manually specified
            resolver.nameservers = [resolverName]
        try:
            for rdata in resolver.query(final_hostname, 'CNAME'):
                result.append(rdata.target)
        except:
            pass
        if len(result) is 1:
            try:
                A = resolver.query(final_hostname, "A")
                if len(A) > 0:
                    result = list()
                    result.append(final_hostname)
                    result.append(str(A[0]))
            except:
                pass
        if len(result) > 1:  # will always have 1 item (target)
            if str(result[1]) in found:
                if found[str(result[1])] > 3:
                    return
                else:
                    found[str(result[1])] = found[str(result[1])] + 1
            else:
                found[str(result[1])] = 1
            resolved_out.write(str(result[0]) + ":" + str(result[1]) + "\n")
            resolved_out.flush()
            ext = tldextract.extract(str(result[1]))
            if ext.domain == "amazonaws":
                try:
                    for rdata in resolver.query(result[1], 'CNAME'):
                        result.append(rdata.target)
                except:
                    pass
            print(
                colored(
                    result[0],
                    "red") +
                " : " +
                colored(
                    result[1],
                    "green"))
            if len(result) > 2 and result[2]:
                print(
                    colored(
                        result[0],
                        "red") +
                    " : " +
                    colored(
                        result[1],
                        "green") +
                    ": " +
                    colored(
                        result[2],
                        "blue"))
        q.put(result)
