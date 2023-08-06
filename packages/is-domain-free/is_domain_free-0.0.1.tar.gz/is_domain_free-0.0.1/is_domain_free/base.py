import multiprocessing as mp
import subprocess
import sys

from .exceptions import TldNotSupportedException


name = "is_domain_free"


def get_tld_from_domain_name(domain_name):
    """
    :param domain_name: the domain name from which to get the TLD from
    :return: Returns the TLD from a domain name (google.com would return 'com')
    """
    return domain_name.split('.')[-1]


class DomainNameAvailabilityChecker(object):
    """
    Main object that checks the availability of a domain name.

    The whois getter is the object that will return the content of a
    whois command on a specific domain name.

    The whois parser is the object that will parse the whois
    content.
    """
    def __init__(self, whois_getter, whois_parser):
        """
        :param whois_getter: Object that gets the whois content
        :param whois_parser: Object that parses the whois content
        """
        self._whois_getter = whois_getter
        self._whois_parser = whois_parser

    def is_available(self, domain_name):
        """
        Determine if a domain name is available (not taken) or
        unavailable (taken).

        :param domain_name: The domain name to check
        :return: True if the domain name is available (not taken)
        """
        whois_content = self._whois_getter.get_whois_content(domain_name)
        return self._whois_parser.is_available(domain_name, whois_content)

    def _is_available_batch(self, domain_name, output):
        """
        Used internally with is_available batch running parallel
        tasks. Output is used to append results.

        :param domain_name: domain name to check
        :param output: Results are added in output
        :return:
        """
        return output.put((domain_name, self.is_available(domain_name)))

    def is_available_batch(self, domain_names):
        """
        Multiple domain names checking, running in parellel. Since there's
        a lot of wait time with the 'whois' command, 100 domain name
        checks can take 10 seconds if ran sequentially. It goes down to
        about 1 second if we run the code with parallel processes.

        :param domain_names: Iterable conaintain the list of domains to
        check

        :return: A list of tuples with the domain names and a boolean
          indicating if they are available or not.
        """
        output = mp.Queue()
        processes = [
            mp.Process(
                target=self._is_available_batch, args=(domain_name, output)
            ) for domain_name in domain_names
        ]

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        results = [output.get() for p in processes]
        return results


class WhoisParserBasic(object):
    """
    Basic WHOIS content result parser. It simply checks
    in the whois content if a specific string appears at the
    beginning for .com, .net and .io domain names.
    """

    COM = 'com'
    NET = 'net'
    IO = 'io'

    supported_tlds = (COM, NET, IO)

    # String that means a domain name is available
    COM_NET_AVAILABLE = "No match for \""
    IO_AVAILABLE = "NOT FOUND"

    def is_available(self, domain_name, whois_content):
        if not whois_content:
            raise ValueError("whois_content parameter shouldn't be empty")

        tld = get_tld_from_domain_name(domain_name)

        if tld not in self.supported_tlds:
            raise TldNotSupportedException("tld must be one of: %s" % str(self.supported_tlds))

        if tld == self.COM or tld == self.NET:
            if whois_content.startswith(WhoisParserBasic.COM_NET_AVAILABLE):
                return True

        if tld == self.IO:
            if whois_content.startswith(WhoisParserBasic.IO_AVAILABLE):
                return True

        return False


class WhoisGetterBasic(object):
    """
    Simple basic whois content getter from the command line
    running whois abc.com. It will grab the whole text
    and return it back.
    """

    def get_whois_content(self, domain):
        """
        Returns the content of a whois 'domain-name.com' command

        Will simply run the 'whois' command on the current system and return
        the string (based on default local encoding).

        :param domain: Domain to check
        :return: The content of the whois command
        """
        result = subprocess.run(['whois', domain], stdout=subprocess.PIPE)
        return result.stdout.decode(sys.getdefaultencoding())


def is_free(domain_name):
    """
    Simple shortcut command that will instantiate a DomainNameAvailabilityChecker
     with the basic whois content grabber and whois parser.

    :param domain_name: Single domain name to check
    :return: List of tuples ie [(domainabc.com, True), ...]
     indicating if the domain names are free or not.
    """
    checker = DomainNameAvailabilityChecker(WhoisGetterBasic(), WhoisParserBasic())
    return checker.is_available(domain_name)


def are_free(domain_names):
    """
    Simple shortcut command that will instantiate a DomainNameAvailabilityChecker
     with the basic whois content grabber and whois parser and check a list
     of domain names for their availability.

    :param domain_names: List of domain names to check
    :return: List of tuples ie [(domainabc.com, True), ...]
     indicating if the domain names are free or not.
    """
    checker = DomainNameAvailabilityChecker(WhoisGetterBasic(), WhoisParserBasic())
    return checker.is_available_batch(domain_names)
