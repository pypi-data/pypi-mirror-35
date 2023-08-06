"""DNS class file."""

import json
import re
import sys
import yaml


class DNS(object):
    """DNS class."""

    def __init__(self, mhl=None, verbose=False):
        """Initialize the object."""
        self.mhl = mhl
        self.settings = self.get_settings()
        self.verbose = verbose

    def get_resource_records(self):
        """Return a list of all resource records from master.host.listing."""
        records = self.get_host_records()
        records += self.get_cname_records()
        records += self.get_mx_records()
        records += self.get_ns_records()
        records += self.get_additional_records()
        return records

    def get_additional_records(self):
        """Get additional resource records."""
        domain = 'broadinstitute.org-external'
        settings = self.settings[domain]

        records = []
        for key in settings:
            record = self.settings['defaults'][key]
            records.append(record)
        return records

    def get_cname_records(self):
        """Get cname resource records."""
        records = []
        if not self.mhl:
            return
        cnames = self.mhl.mhlfile.cnames
        for hostname in cnames:
            cname = cnames[hostname]
            hostname = '%s.broadinstitute.org.' % (hostname)
            record = {
                'kind': 'dns#resourceRecordSet',
                'name': hostname,
                'rrdatas': [cname.target],
                'ttl': cname.ttl.replace('-', ''),
                'type': 'CNAME',
            }
            records.append(record)
        return records

    def get_host_records(self):
        """Get host resource records."""
        records = []
        round_robins = {}
        if not self.mhl:
            return
        hosts = self.mhl.mhlfile.hosts
        for hostname in hosts:
            host = hosts[hostname]

            # skip dnsskip hosts
            if 'dnsskip' in host.tags:
                continue

            # skip netapps
            if host.hosttype in ['netapp']:
                continue

            # skip hosts with internal IPs
            if re.match(r'^(192\.168\.|10\.|172\.)', host.ip):
                continue

            hostname = '%s.broadinstitute.org.' % (hostname)

            # add the host A record
            record = {
                'kind': 'dns#resourceRecordSet',
                'name': hostname,
                'rrdatas': [host.ip],
                'ttl': host.ttl.replace('-', ''),
                'type': 'A',
            }
            records.append(record)

            # handle round robin records
            if host.round_robin:
                if host.round_robin in round_robins:
                    round_robins[host.round_robin]['rrdatas'].append(host.ip)
                else:
                    hostname = '%s.broadinstitute.org.' % (host.round_robin)
                    record = {
                        'kind': 'dns#resourceRecordSet',
                        'name': hostname,
                        'rrdatas': [host.ip],
                        'ttl': host.ttl.replace('-', ''),
                        'type': 'A',
                    }
                    records.append(record)

            # add cname records
            for cname in host.cnames:
                # skip ldap
                if cname in ['ldap']:
                    continue
                cname = '%s.broadinstitute.org.' % (cname)
                record = {
                    'kind': 'dns#resourceRecordSet',
                    'name': cname,
                    'rrdatas': [hostname],
                    'ttl': host.ttl.replace('-', ''),
                    'type': 'CNAME',
                }
                records.append(record)

        # add in the round robin records
        for name in round_robins:
            record = round_robins[name]
            records.append(record)

        return records

    def get_mx_records(self):
        """Get mx resource records."""
        records = []
        if not self.mhl:
            return
        mxs = self.mhl.mhlfile.mxs
        for hostname in mxs:
            # skip broadinstitute.org. and broad.mit.edu.
            if hostname in ['broad.mit.edu.', 'broadinstitute.org.']:
                continue
            mx = mxs[hostname]
            hostname = '%s.broadinstitute.org.' % (hostname)
            record = {
                'kind': 'dns#resourceRecordSet',
                'name': hostname,
                'rrdatas': mx.targets,
                'ttl': mx.ttl.replace('-', ''),
                'type': 'MX',
            }
            records.append(record)
        return records

    def get_ns_records(self):
        """Get ns resource records."""
        records = []
        if not self.mhl:
            return
        nss = self.mhl.mhlfile.nss
        for hostname in nss:
            ns = nss[hostname]
            hostname = '%s.broadinstitute.org.' % (hostname)
            record = {
                'kind': 'dns#resourceRecordSet',
                'name': hostname,
                'rrdatas': ns.targets,
                'ttl': ns.ttl.replace('-', ''),
                'type': 'NS',
            }
            records.append(record)
        return records

    def get_settings(self):
        """Get DNS settings from YAML file."""
        # read in dns yaml
        with open("bits/dns/dns.yaml", 'r') as stream:
            try:
                settings = yaml.load(stream)
            except yaml.YAMLError as e:
                print(e)
                sys.exit(1)
        return settings
