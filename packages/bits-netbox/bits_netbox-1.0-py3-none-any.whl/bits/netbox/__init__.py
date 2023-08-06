"""Netbox class file."""

import pynetbox


class Netbox(object):
    """Netbox class."""

    def __init__(self, url, token, verbose=False):
        """Initialize the object."""
        self.token = token
        self.url = url
        self.verbose = verbose

        # connect
        self.netbox = pynetbox.api(self.url, token=self.token)

    def get_prefixes(self):
        """Return a dict of Prefixes in netbox."""
        prefixes = {}
        for prefix in self.netbox.ipam.prefixes.all():
            name = str(prefix)
            prefixes[name] = prefix.serialize()
        return prefixes

    def get_vlans(self):
        """Return a dict of VLANs in netbox."""
        vlans = {}
        for vlan in self.netbox.ipam.vlans.all():
            name = str(vlan)
            vlans[name] = vlan.serialize()
        return vlans
