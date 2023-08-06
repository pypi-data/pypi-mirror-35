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

        # prefixes
        self.prefixes = self.get_prefixes()
        self.descriptions = self.get_prefix_descriptions()

        # vlans
        self.vlans = self.get_vlans()

        # groupings
        self.groupings = {}
        self.grouping_ids = {}

        # collection all grouping labels/values from all prefixes
        for pid in self.prefixes:
            prefix = self.prefixes[pid]
            grouping = prefix.custom_fields['grouping']
            if not grouping:
                continue
            value = grouping['value']
            label = grouping['label']
            self.groupings[label] = value
            self.grouping_ids[value] = label

    def get_prefix_descriptions(self):
        """Return a dict of Prefixes by their description."""
        descriptions = {}
        for pid in self.prefixes:
            prefix = self.prefixes[pid]
            description = prefix['description']
            descriptions[description] = prefix
        return descriptions

    def get_prefixes(self):
        """Return a dict of Prefixes in netbox."""
        prefixes = {}
        for prefix in self.netbox.ipam.prefixes.all():
            pid = prefix.id
            prefixes[pid] = prefix
        return prefixes

    def get_sheet_prefix(self, prefix):
        """Return a prefix in the format that Google Sheets creates."""
        custom_fields = prefix.custom_fields

        # grouping
        grouping = ''
        if custom_fields['grouping']:
            # gid = custom_fields['grouping']['value']
            grouping = custom_fields['grouping']['label']

        # description
        description = prefix.description

        # network_type
        network_type = ''

        # building
        building = ''

        # floor
        floor = ''

        # servicenow_tag
        if custom_fields['servicenow_tag']:
                network_type, building, floor = custom_fields['servicenow_tag'].split(':')

        # vlan
        vlan = ''
        if prefix.vlan:
            vlan = prefix.vlan.vid

        # vmps_tag
        vmps_tag = prefix.custom_fields['mab_tag']

        # cidr
        cidr = prefix.prefix

        # gateway
        gateway = custom_fields['gateway']

        # netmask
        netmask = custom_fields['netmask']

        # usable_start
        usable_start = custom_fields['usable_start_ip']
        if not usable_start:
            usable_start = '-'

        # usable_end
        usable_end = custom_fields['usable_end_ip']
        if not usable_end:
            usable_end = '-'

        # notes
        notes = custom_fields['notes']

        data = {
            'grouping': grouping,
            'description': description,
            'network_type': network_type,
            'building': building,
            'floor': floor,
            'vlan': vlan,
            'vmps_tag': vmps_tag,
            'cidr': cidr,
            'gateway': gateway,
            'netmask': netmask,
            'usable_start': usable_start,
            'usable_end': usable_end,
            'notes': notes,
        }
        return data

    def get_vlans(self):
        """Return a dict of VLANs in netbox."""
        vlans = {}
        for vlan in self.netbox.ipam.vlans.all():
            vid = vlan.id
            vlans[vid] = vlan
        return vlans
