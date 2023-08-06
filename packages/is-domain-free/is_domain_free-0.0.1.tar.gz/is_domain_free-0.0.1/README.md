Simple package to check if a domain name is available or not.

The program uses the `whois` system command, which works by default on Mac and Linux.

For Windows, you need to install the command from here: https://docs.microsoft.com/en-ca/sysinternals/downloads/whois

The program mostly interpret the WHOIS command's results (which is a string) to see if the domain is available or not.

*Note:* The results from the WHOIS command are different for different TLDs, so the support for TLDs is limited (io, net, com), but can be extended easily.