import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bin_exists(host):
    assert host.file('/usr/local/bin/withings-scale-pairing-wizard').is_file
    assert host.file('/usr/local/bin/withings-scale-pairing-wizard').is_executable


def test_sudoers_exists(host):
    assert host.file('/etc/sudoers.d/withings-scale-pairing-wizard').is_file
