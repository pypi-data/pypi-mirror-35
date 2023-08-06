"""MHL entry type classes."""

import netaddr
import re

HOSTRE = re.compile(r'^([0-9a-z])+([0-9a-z-])*([0-9a-z])*(\.rac)*$')
TTLRE = re.compile('^[0-9]+(m|h|d|w){0,1}$')

# Base classes
class BaseType(object):
    """BaseType class."""

    def __init__(self, line):
        """Initialize the object."""
        self.hosttype = None
        self.ip = None
        self.line = line
        self.linenum = line.linenum
        self.mac = None

    def check(self):
        """Check a line."""

    def check_ip(self):
        """Check IP."""
        # check if this is a valid ip address
        try:
            netaddr.IPAddress(self.ip)
        except netaddr.core.AddrFormatError:
            error = 'Invalid IP Address: %s' % (self.ip)
            self.line.errors.append(error)
            return

        # check if this ip address is in one of our known ranges
        if self.ip not in self.line.broad_hosts and self.hosttype != 'external':
            error = 'Unknown Network: %s' % (self.ip)
            self.line.errors.append(error)

class Owner(object):
    """"Owner class."""

    def __init__(self, comments, username):
        """Initialize the object."""
        self.emplid = None
        self.name = comments.split('(')[0].strip()
        self.username = username


class BaseRecord(BaseType):
    """BaseRecord class."""

    def __init__(self, line):
        """Initialize the object."""
        BaseType.__init__(self, line)
        self.data = line.to_json()
        self.line = line
        self.linenum = line.linenum
        self.type = self.data['hosttype']

        self.comments = None
        self.hostname = None
        self.hosttype = None
        self.ip = None
        self.ttl = None

    def check_comments(self):
        """Check Comments."""
        if not self.comments:
            error = 'Comments required: %s' % (self.comments)
            self.line.errors.append(error)

    def check_hostname(self, hostname=None):
        """Check Hostname."""
        # regexp to check that all host names have lowercase letters and numbers and
        # that they don't start or end with a hyphen
        hostre = HOSTRE
        if not hostname:
            hostname = self.hostname
        if self.type in ['mx']:
            if ' ' in hostname:
                _, hostname = hostname.split(' ')
        if self.type in ['cname', 'mx', 'ns']:
            hostname = hostname.replace('.', '')
        if not hostre.match(hostname):
            error = 'Hostname syntax: %s' % (hostname)
            self.line.errors.append(error)

    def check_hosttype(self):
        """Check hosttype."""
        if self.hosttype not in self.line.hosttypes:
            error = 'Invalid Type: %s' % (self.hosttype)
            self.line.errors.append(error)

    def check_ttl(self):
        """Check TTL."""
        # regexp to check that TTLs are in the proper format
        ttlre = TTLRE
        if not ttlre.match(self.ttl):
            if self.ttl != '-':
                error = 'TTL syntax: %s' % (self.ttl)
                self.line.errors.append(error)


class DnsRecord(BaseRecord):
    """DnsRecord class."""

    def __init__(self, line):
        """Initialize the object."""
        BaseRecord.__init__(self, line)
        # dns data
        self.comments = self.data['comments']
        self.hostname = self.data['hostnames']
        self.ttl = self.data['ttl']

    def check(self):
        """Check DNS record."""
        self.check_comments()
        self.check_hostname()
        self.check_ttl()


class CnameRecord(DnsRecord):
    """"CnameRecord class."""

    def __init__(self, line):
        """Initialize the object."""
        DnsRecord.__init__(self, line)
        self.target = self.data['target']

    def check(self):
        """Check DNS record."""
        self.check_comments()
        self.check_hostname()
        self.check_hostname(self.target)
        self.check_ttl()


class Comment(BaseType):
    """"Comment class."""

    def __init__(self, line):
        """Initialize the object."""
        BaseType.__init__(self, line)
        self.type = 'comment'
        self.comment_type = self.get_comment_type()
        self.hosttype = 'device'

    def check(self):
        """Run checks for a commented entry."""
        self.check_comments()

    def check_comments(self):
        """Check the comments in a commented entry."""
        if self.comment_type == 'entry':
            """Check this as if it were a real entry."""

        elif self.comment_type == 'reserved_ip':
            self.check_ip()
            comment = self.line.fields[1]
            if not re.match('RESERVED - ', comment):
                error = 'Invalid Comment: %s' % (comment)
                self.line.warnings.append(error)

        elif self.comment_type == 'available_ip':
            self.check_ip()

        elif self.comment_type == 'error':
            error = 'Invalid Comment: %s' % (comment)
            self.line.warnings.append(error)

    def get_comment_type(self):
        """Check the comment."""
        comment_type = 'error'
        # check for full entries
        if len(self.line.fields) == len(self.line.fieldnames):
            comment_type = 'entry'
            self.ip = self.line.fields[0].lstrip('#')
        # check for reserved IPs
        elif len(self.line.fields) == 2:
            comment_type = 'reserved_ip'
            self.ip = self.line.fields[0].lstrip('#')
        # check for available IPs
        elif len(self.line.fields) == 1:
            if re.match(r'#[0-9]+(\.[0-9]+){3}', self.line.line):
                comment_type = 'available_ip'
                self.ip = self.line.fields[0].lstrip('#')
            else:
                comment_type = 'comment'
        return comment_type

class Host(BaseRecord):
    """"Host class."""

    def __init__(self, line):
        """Initialize the object."""
        BaseRecord.__init__(self, line)
        self.type = 'host'
        self.hosttype = self.data['hosttype']

        # host data
        self.cnames = self.data['hostnames'].split(',')[1: ]
        self.comments = self.data['comments']
        self.hostname = self.data['hostnames'].split(',')[0]
        self.ip = self.data['target']
        self.location = self.data['location']
        self.mac = self.data['mac']
        self.tags = self.data['tags'].split(',')
        self.ttl = self.data['ttl']
        self.username = self.data['username']

        self.round_robin = None
        # round robin records
        if self.hosttype == 'round_robin':
            # for round_robin hosts, hostnames is handled slightly differently
            # the first hostname listed is the "round_robin" hostname
            # the second one is the "hostname"
            # the rest are the cnames
            self.round_robin = self.hostname
            self.hostname = self.cnames[0]
            self.cnames = self.cnames[1:]

        self.model = None
        self.owner = None

        # get model and owner from comments
        if self.hosttype in ['chrome', 'dhcpdevice', 'mac', 'pc']:
            # model
            if re.search(r'^.+\(.+\).*$', self.comments):
                self.model = self.comments.split('(')[1].split(')')[0].strip()
            # owner
            self.owner = Owner(self.comments, self.username)

    def check(self):
        """Check a Host."""
        self.check_cnames()
        self.check_comments()
        self.check_hostname()
        self.check_hosttype()
        self.check_ip()
        self.check_location()
        self.check_mac()
        self.check_tags()
        self.check_ttl()
        self.check_username()

        # desktops and laptops
        if self.hosttype in ['chrome', 'mac', 'pc']:
            self.check_computed_hostname()
            self.check_owner()

        # round robin
        if self.round_robin:
            self.check_hostname(self.round_robin)

    def check_cnames(self):
        """Check CNAMES for a host."""
        for hostname in self.cnames:
            self.check_hostname(hostname)

    def check_comments(self):
        """Check Comments."""
        BaseRecord.check_comments(self)

        if self.hosttype in ['chrome', 'mac', 'pc']:

            # check format of comment
            if not re.match(r"[a-zA-Z-'\. ]+ \(.*\).*$", self.comments):
                error = 'Invalid Comments format: %s' % (self.comments)
                self.line.errors.append(error)
                return

    def check_computed_hostname(self):
        """Check to make sure computed hostname exists."""
        hostname = self.get_computed_hostname()
        if hostname != self.hostname and hostname not in self.cnames:
            error = 'Computed Hostname not found: %s' % (hostname)
            self.line.errors.append(error)

    def check_location(self):
        """Check Location."""
        # define the list of valid locations

        required = False
        if self.hosttype not in [
            'device',
            'dhcpdevice',
            'external',
            'ip_alias',
            'round_robin'
        ]:
            required = True

        if self.location == '-':
            if not required:
                return
            else:
                error = 'Location required: %s' % (self.location)
                self.line.errors.append(error)
                return

        if self.location not in self.line.locations:
            error = 'Unknown Location: %s' % (self.location)
            self.line.errors.append(error)

    def check_mac(self):
        """Check MAC."""
        required = False
        if self.hosttype not in [
            'device',
            'external',
            'ip_alias',
            'netapp',
            'round_robin',
        ]:
            required = True

        if self.mac == '-':
            if not required:
                return
            else:
                error = 'MAC Address required: %s' % (self.mac)
                self.line.errors.append(error)
                return

        try:
            netaddr.EUI(self.mac)
        except netaddr.core.AddrFormatError:
            error = 'Invalid MAC address: %s' % (self.mac)
            self.line.errors.append(error)

    def check_owner(self):
        """Check Owner."""
        # exclude special owners
        # special_owners = self.line.special_owners
        # check the username to make sure it exists
        # check the owner name to make sure it exist
        # check to make sure username matches owner

    def check_tags(self):
        """Check Tags."""
        # check the tags to make sure they match a known set
        required = False
        if self.hosttype in ['mac_svr', 'netapp', 'unix_svr']:
            required = True

    def check_username(self):
        """Check username."""
        # check username to make sure it exists and is not terminated

    def get_computed_hostname(self):
        """Return the computed hostname."""
        type_char = self.hosttype[0]
        mac_name = self.get_mac_name()
        site_name = self.get_site_name()
        return '%s%s%s' % (site_name, type_char, mac_name)

    def get_mac_name(self):
        """Return MAC address portion of the computed hostname."""
        try:
            (mac4, mac5, mac6) = self.mac.split(':')[3:]
            return '%s%s-%s%s' % (mac4, mac5[0], mac5[1], mac6)
        except Exception as e:
            error = 'ERROR generating mac name: %s' % (self.mac)
            self.line.errors.append(error)

    def get_site_name(self):
        """Return the site name."""
        # check if the IP address is valid
        try:
            ip = netaddr.IPAddress(self.ip)
        except Exception as e:
            return self.location

        # regular hosts get no special character:
        if ip in self.line.regular_hosts:
            return self.location

        # cellario hosts get the "c"
        elif ip in self.line.cellario_hosts:
            return '%sc' % (self.location)

        # lab hosts get the "l"
        elif ip in self.line.lab_hosts:
            return '%sl' % (self.location)

        # qa hosts get the "q"
        elif ip in self.line.qa_hosts:
            return '%sq' % (self.location)

        # restricted vlan hosts get an "x"
        elif ip in self.line.restricted_hosts:
            return '%sx' % (self.location)

        # other known hosts get no tag
        else:
            return 'x'

        return self.location

class MxRecord(DnsRecord):
    """"MxRecord class."""

    def __init__(self, line):
        """Initialize the object."""
        DnsRecord.__init__(self, line)
        self.priority = self.data['mac']
        target = self.data['target']
        if self.priority:
            target = '%s %s' % (self.priority, target)
        self.targets = [target]

    def check(self):
        """Check MxRecord."""
        self.check_comments()
        self.check_hostname()
        for hostname in self.targets:
            self.check_hostname(hostname)
        self.check_ttl()

    def check_priority(self):
        """Check Priority."""
        try:
            int(self.priority)
        except Exception as e:
            error = 'Invalid MX Priority: %s [%s]' % (self.priority, e)
            self.line.errors.append(error)

class NsRecord(DnsRecord):
    """"NsRecord class."""

    def __init__(self, line):
        """Initialize the object."""
        DnsRecord.__init__(self, line)
        self.targets = [self.data['target']]

    def check(self):
        """Check NsRecord."""
        self.check_comments()
        self.check_hostname()
        for hostname in self.targets:
            self.check_hostname(hostname)
        self.check_ttl()
