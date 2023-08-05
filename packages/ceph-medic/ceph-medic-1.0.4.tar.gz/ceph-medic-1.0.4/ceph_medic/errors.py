
could_not_connect_to_cluster = """
Failed to connect to cluster when running:

    {command}

This could be because the Ceph cluster name might not map correctly to
a configuration file or a keyring. If using custom cluster names, make sure
that the Ceph configuration file is named the same.

The default cluster name is 'ceph' and ceph-medic will infer the cluster name
if there is no /etc/ceph/ceph.conf by finding the first ".conf" file in that
directory.
"""
