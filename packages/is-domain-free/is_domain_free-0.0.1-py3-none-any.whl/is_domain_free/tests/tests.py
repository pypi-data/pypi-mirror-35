from pathlib import Path
from unittest import TestCase

import os

from is_domain_free import DomainNameAvailabilityChecker
from is_domain_free import get_tld_from_domain_name
from is_domain_free import WhoisParserBasic
from is_domain_free.exceptions import TldNotSupportedException


def get_domain_file_content(domain_name):
    """
    Simple utility for tests used to read a text file from a domain name
    :param domain_name: Domain name for which to read the corresponding file
    :return: Content of the text file
    """
    content = Path('%s/whois_results/%s.txt' % (os.path.dirname(__file__), domain_name)).read_text()
    return content


class WhoisContentGetterStub(object):
    """
    Whois content getter used for tests. It will get the
    text form the text file based on the domain name
    passed in parameter.

    For example, if you pass 'google.io', it will look for
    google.io.txt in the 'whois_results' folder.
    """

    def get_whois_content(self, domain):
        content = get_domain_file_content(domain)
        return content


class WhoisParserBasicTest(TestCase):
    """
    Tests that the basic whois parser returns the right availability
    statuses depending on string found in whois content
    """
    def _is_available(self, domain_name, whois_content):
        """
        Checks if a domain_name is available based on the
        content of a whois command

        :param domain_name: domain name to check
        :param whois_content: Text (content of a whois command)
        :return:
        """
        parser = WhoisParserBasic()
        is_available = parser.is_available(domain_name, whois_content)
        return is_available

    def test_parser_tld_com(self):
        """
        Tests that the parser stub finds the content of a file
        :return:
        """
        tld = get_tld_from_domain_name('google.com')
        self.assertTrue(tld, 'com')

    def test_get_tld_uk(self):
        """
        Tests that a tld from a .co.uk returns .uk
        :return:
        """
        tld = get_tld_from_domain_name('google.co.uk')
        self.assertTrue(tld, 'uk')

    def test_unsupported_tld(self):
        """
        Tests that an error is raised when an unsupported TLD is passed
        :return:
        """
        parser = WhoisParserBasic()
        self.assertRaises(TldNotSupportedException, parser.is_available, 'unsupportedtld.abc', 'NOT FOUND')

    def test_parse_com_unavail(self):
        """
        Test that we successfully say that a domain name is
        taken/not available when it's registered eg google.com
        """
        self.assertFalse(self._is_available('google.com', 'XXX'))

    def test_parse_com_avail(self):
        """
        Tests that the result of a .com returns that
        the domain is available when nobody registered it.
        """
        self.assertTrue(self._is_available('rewqwerty.com', WhoisParserBasic.COM_NET_AVAILABLE))

    def test_parse_net_unavail(self):
        """
        unavailability test for a .net domain
        """
        self.assertFalse(self._is_available('google.net', 'XXX'))

    def test_parse_net_avail(self):
        """
        availability test for a .net domain
        """
        self.assertTrue(self._is_available('rewqwerty.net', WhoisParserBasic.COM_NET_AVAILABLE))

    def test_parse_io_unavail(self):
        """
        Tests that if the specific text isn't find in the whois content,
        the domain name is returned as being taken.
        :return:
        """
        self.assertFalse(self._is_available('google.io', 'XXX'))

    def test_parse_io_avail(self):
        """
        Tests that a domain name is available if it contains the
        searched string indicating that a domain is not taken.
        :return:
        """
        self.assertTrue(self._is_available('rewqwerty.io', WhoisParserBasic.IO_AVAILABLE))


class WhoisContentGetterStubTest(TestCase):
    """
    Simply testing that the stub returns text file content
    """
    def test_get_file(self):
        """
        Testing that when getting the content of google.com, it reads
        the google.com.txt file and returns its content.
        :return:
        """
        whois_stub = WhoisContentGetterStub()
        content = whois_stub.get_whois_content('google.com')
        self.assertTrue(content.startswith('   Domain Name: GOOGLE.COM'))


class IntegrationTest(TestCase):
    """
    Test using both the whois getter and the whois parser.
    """
    def _get_domain_checker(self):
        whois_getter = WhoisContentGetterStub()
        whois_parser = WhoisParserBasic()

        domain_checker = DomainNameAvailabilityChecker(whois_getter, whois_parser)
        return domain_checker

    def _is_available(self, domain_name):
        domain_checker = self._get_domain_checker()
        return domain_checker.is_available(domain_name)

    def test_whois_getter(self):
        whois_getter = WhoisContentGetterStub()
        file_content = whois_getter.get_whois_content('google.io')
        self.assertTrue('Domain Name: GOOGLE.IO' in file_content)

    def test_available_domain_com(self):
        self.assertTrue(self._is_available('rewqwerty.com'))

    def test_unavailable_domain_com(self):
        self.assertFalse(self._is_available('google.com'))

    def test_available_domain_net(self):
        self.assertTrue(self._is_available('rewqwerty.net'))

    def test_unavailable_domain_net(self):
        self.assertFalse(self._is_available('google.net'))

    def test_available_domain_io(self):
        self.assertTrue(self._is_available('rewqwerty.io'))

    def test_unavailable_domain_io(self):
        self.assertFalse(self._is_available('google.io'))

    def test_multiple_domains(self):
        """
        Testing a batch of domain names for their availability

        :return:
        """
        domain_names = [
            'google.com',
            'rewqwerty.io',
            'google.io',
        ]

        domain_checker = self._get_domain_checker()

        result = domain_checker.is_available_batch(domain_names)

        self.assertEqual(len(result), 3)
        self.assertListEqual(sorted(result), sorted([
            ('google.com', False),
            ('rewqwerty.io', True),
            ('google.io', False),
        ]))
