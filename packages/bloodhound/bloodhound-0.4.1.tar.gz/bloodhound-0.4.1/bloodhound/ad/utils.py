####################
#
# Copyright (c) 2018 Fox-IT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
####################

import logging
import socket
import threading
import re
import dns
from dns import resolver, reversename
from structures import LDAP_SID


"""
"""
class ADUtils(object):
    @staticmethod
    def domain2ldap(domain):
        return 'DC=' + ',DC='.join(str(domain).rstrip('.').split('.'))


    @staticmethod
    def ldap2domain(ldap):
        return re.sub(',DC=', '.', ldap[ldap.find('DC='):], flags=re.I)[3:]


    @staticmethod
    def tcp_ping(host, port, timeout=1.0):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((host, port))
            s.close()
            return True
        except KeyboardInterrupt:
            raise
        except:
            return False

    @staticmethod
    def ip2host(ip, resolver=resolver):
        result = ip
        try:
            addr = reversename.from_address(ip)
        except dns.exception.SyntaxError:
            logging.warning('DNS: invalid address: %s' % ip)
            return result

        try:
            answer = str(resolver.query(addr, 'PTR')[0])
            result = answer.rstrip('.')
        except (dns.resolver.NXDOMAIN, dns.resolver.Timeout) as e:
            pass
        except:
            logging.warning('DNS lookup failed: %s' % addr)
            pass

        return result

    # Translate the binary SID from LDAP into human-readable form
    @staticmethod
    def formatSid(siddata):
        return LDAP_SID(siddata).formatCanonical()

    # Translate SidType to strings accepted by BloodHound
    @staticmethod
    def translateSidType(sidType):
        if sidType == 1:
            return 'user'
        if sidType == 2:
            return 'group'
        # sidType 4 means "alias", this is actually a Domain Local Group
        if sidType == 4:
            return 'group'
        if sidType == 9:
            return 'computer'
        if sidType == 5:
            return 'wellknown'
        # Can be a (by BloudHound) unsupported type
        # must not be an empty string since this breaks our CSV files
        return 'unknown'

    @staticmethod
    def resolve_ad_entry(entry):
        """
        Translate an LDAP entry into a dictionary containing the
        information used by BloodHound
        """
        resolved = {}
        account = ''
        dn = ''
        domain = ''
        if entry['attributes']['sAMAccountName']:
            account = entry['attributes']['sAMAccountName']
        if entry['attributes']['distinguishedName']:
            dn = entry['attributes']['distinguishedName']
            domain = ADUtils.ldap2domain(dn)

        resolved['principal'] = unicode('%s@%s' % (account, domain)).upper()
        if not entry['attributes']['sAMAccountName']:
            # TODO: Fix foreign users
            # requires cross-forest resolving
            if 'ForeignSecurityPrincipals' in dn:
                resolved['principal'] = domain.upper()
                resolved['type'] = 'foreignsecurityprincipal'
            else:
                resolved['type'] = 'unknown'
        else:
            accountType = entry['attributes']['sAMAccountType']
            if accountType in [268435456, 268435457, 536870912, 536870913]:
                resolved['type'] = 'group'
            elif accountType in [805306369]:
                resolved['type'] = 'computer'
                short_name = account.rstrip('$')
                resolved['principal'] = unicode('%s.%s' % (short_name, domain)).upper()
            elif accountType in [805306368]:
                resolved['type'] = 'user'
            elif accountType in [805306370]:
                resolved['type'] = 'trustaccount'
            else:
                resolved['type'] = 'domain'

        return resolved

class DNSCache(object):
    """
    A cache used for caching forward and backward DNS at the same time.
    This cache is used to avoid PTR queries when forward lookups are already done
    """
    def __init__(self):
        self.lock = threading.Lock()
        self._cache = {}

    # Get an entry from the cache
    def get(self, entry):
        with self.lock:
            return self._cache[entry]

    # Put a forward lookup in the cache, this also
    # puts the reverse lookup in the cache
    def put(self, entry, value):
        with self.lock:
            self._cache[entry] = value
            self._cache[value] = entry

    # Put a reverse lookup in the cache. Forward lookup
    # is not added since reverse is considered less reliable
    def put_single(self, entry, value):
        with self.lock:
            self._cache[entry] = value

class SidCache(object):
    """
    Generic cache for caching SID lookups
    """
    def __init__(self):
        self.lock = threading.Lock()
        self._cache = {}

    # Get an entry from the cache
    def get(self, entry):
        with self.lock:
            return self._cache[entry]

    # Put a forward lookup in the cache, this also
    # puts the reverse lookup in the cache
    def put(self, entry, value):
        with self.lock:
            self._cache[entry] = value

class SamCache(SidCache):
    """
    Cache for mapping SAM names to principals.
    Identical to the SidCache in behaviour
    """
    pass
