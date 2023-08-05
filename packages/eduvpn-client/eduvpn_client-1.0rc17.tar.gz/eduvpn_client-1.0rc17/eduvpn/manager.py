# python-eduvpn-client - The GNU/Linux eduVPN client and Python API
#
# Copyright: 2017, The Commons Conservancy eduVPN Programme
# SPDX-License-Identifier: GPL-3.0+

import json
import logging
import os

from eduvpn.util import have_dbus

if have_dbus():
    import eduvpn.other_nm as NetworkManager
    from dbus.exceptions import DBusException
    import dbus

from eduvpn.config import providers_path
from eduvpn.io import write_cert
from eduvpn.openvpn import parse_ovpn, ovpn_to_nm
from eduvpn.util import make_unique_id
from eduvpn.exceptions import EduvpnException
from eduvpn.metadata import Metadata

logger = logging.getLogger(__name__)


def insert_config(settings):
    """
    Add a configuration to the networkmanager

    args:
        settings (dict): a nm settings dict, typically generated by :meth:`ovpn_to_nm()`
    """
    if not have_dbus():
        return

    name = settings['connection']['id']
    logger.info("generating or updating OpenVPN configuration with name {}".format(name))
    connection = NetworkManager.Settings.AddConnection(settings)
    return connection


def list_providers():
    """
    List all OpenVPN connections.
    """
    if not have_dbus():
        # fall back to just listing the json files
        try:
            providers = [i for i in os.listdir(providers_path) if i.endswith('.json')]
        except (IOError, OSError) as e:
            logger.error("can't list configurations in {}".format(providers_path))
            raise StopIteration
        else:
            for p in providers:
                try:
                    yield Metadata.from_uuid(p[:-5])
                except IOError as e:
                    logger.error("cant open {}: {}".format(p, e))
    else:
        all_ = NetworkManager.Settings.ListConnections()
        vpn_connections = [c.GetSettings()['connection'] for c in all_ if c.GetSettings()['connection']['type'] == 'vpn']
        logger.info("There are {} VPN connections in networkmanager".format(len(vpn_connections)))
        for conn in vpn_connections:
            yield Metadata.from_uuid(conn['uuid'], display_name=conn['id'])


def store_provider(meta, config_dict):
    """Store the eduVPN configuration"""
    logger.info("storing profile with name {} using NetworkManager".format(meta.display_name))
    new = False
    if not meta.uuid:
        meta.uuid = make_unique_id()
        new = True
    cert_path = write_cert(meta.cert, 'cert', meta.uuid)
    key_path = write_cert(meta.key, 'key', meta.uuid)
    nm_config = ovpn_to_nm(config_dict, meta=meta, display_name=meta.display_name, username=meta.username)
    nm_config['vpn']['data'].update({'cert': cert_path, 'key': key_path})

    if new:
        insert_config(nm_config)
    else:
        update_config_provider(meta, config_dict)

    meta.write()
    return meta.uuid


def delete_provider(uuid):
    """
    Delete the network manager configuration by its UUID

    args:
        uuid (str): the unique ID of the configuration
    """
    metadata = os.path.join(providers_path, uuid + '.json')
    logger.info("deleting metadata file {}".format(metadata))
    try:
        os.remove(metadata)
    except Exception as e:
        logger.error("can't remove ovpn file: {}".format(str(e)))

    if not have_dbus():
        return

    logger.info("deleting profile with uuid {} using NetworkManager".format(uuid))
    all_connections = NetworkManager.Settings.ListConnections()
    conns = [c for c in all_connections if c.GetSettings()['connection']['uuid'] == uuid]
    if len(conns) != 1:
        logger.error("{} connections matching uid {}".format(len(conns), uuid))
        return

    conn = conns[0]
    logger.info("removing certificates for {}".format(uuid))
    for f in ['ca', 'cert', 'key', 'ta']:
        if f not in conn.GetSettings()['vpn']['data']:
            logger.error("key {} not in config for {}".format(f, uuid))
            continue
        path = conn.GetSettings()['vpn']['data'][f]
        logger.info("removing certificate {}".format(path))
        try:
            os.remove(path)
        except (IOError, OSError) as e:
            logger.error("can't remove certificate {}: {}".format(path, e))

    try:
        conn.Delete()
    except Exception as e:
        logger.error("can't remove networkmanager connection: {}".format(str(e)))
        raise


def connect_provider(uuid):
    """
    Enable the network manager configuration by its UUID

    args:
        uuid (str): the unique ID of the configuration
    """
    logger.info("connecting profile with uuid {} using NetworkManager".format(uuid))
    if not have_dbus():
        raise EduvpnException("No DBus daemon running")

    try:
        connection = NetworkManager.Settings.GetConnectionByUuid(uuid)
        return NetworkManager.NetworkManager.ActivateConnection(connection, "/", "/")
    except DBusException as e:
        raise EduvpnException(e)


def list_active():
    """
    List active connections

    returns:
        list: a list of NetworkManager.ActiveConnection objects
    """
    logger.info("getting list of active connections")
    if not have_dbus():
        return []

    try:
        active = NetworkManager.NetworkManager.ActiveConnections
        return [a for a in active if NetworkManager.Settings.GetConnectionByUuid(a.Uuid).GetSettings()['connection']['type'] == 'vpn']
    except DBusException:
        return []


def disconnect_all():
    """
    Disconnect all active VPN connections.
    """
    if not have_dbus():
        return []

    for active in NetworkManager.NetworkManager.ActiveConnections:
        conn = NetworkManager.Settings.GetConnectionByUuid(active.Uuid)
        if conn.GetSettings()['connection']['type'] == 'vpn':
            disconnect_provider(active.Uuid)


def disconnect_provider(uuid):
    """
    Disconnect the network manager configuration by its UUID

    args:
        uuid (str): the unique ID of the configuration
    """
    logger.info("Disconnecting profile with uuid {} using NetworkManager".format(uuid))
    if not have_dbus():
        raise EduvpnException("No DBus daemon running")

    conns = [i for i in NetworkManager.NetworkManager.ActiveConnections if i.Uuid == uuid]
    if len(conns) == 0:
        raise EduvpnException("no active connection found with uuid {}".format(uuid))
    for conn in conns:
        NetworkManager.NetworkManager.DeactivateConnection(conn)


def is_provider_connected(uuid):
    """
    checks if a provider is connected

    returns:
        tuple or None: returns ipv4 and ipv6 address if connected
    """
    for active in list_active():
        if uuid == active.Uuid:
            if active.State == 2:  # connected
                return active.Ip4Config.AddressData[0]['address'], active.Ip6Config.AddressData[0]['address']
            else:
                return "", ""


def update_config_provider(meta, config_dict):
    """
    Update an existing network manager configuration

    args:
        uuid (str): the unique ID of the network manager configuration
        display_name (str): The new display name of the configuration
        config (str): The new OpenVPN configuration
    """
    logger.info("updating config for {} ({})".format(meta.display_name, meta.uuid))
    nm_config = ovpn_to_nm(config_dict, meta=meta, display_name=meta.display_name, username=meta.username)

    if have_dbus():
        connection = NetworkManager.Settings.GetConnectionByUuid(meta.uuid)
        old_settings = connection.GetSettings()
        nm_config['vpn']['data'].update({'cert': old_settings['vpn']['data']['cert'],
                                         'key': old_settings['vpn']['data']['key']})
        connection.Update(nm_config)


def update_keys_provider(uuid, cert, key):
    """
    Update the key pare in the network manager configuration. Typically called when the keypair is expired.

    args:
        uuid (str): unique ID of the network manager connection
        cert (str):
        key (str):
    """
    logger.info("updating key pare for uuid {}".format(uuid))
    write_cert(cert, 'cert', uuid)
    write_cert(key, 'key', uuid)


def monitor_all_vpn(callback):
    """
    This installs a dbus callback which will be called every time the state of any VPN connection changes.

    args:
        callback (func): a callback function
    """
    if not have_dbus():
        return []

    bus = dbus.SystemBus()
    bus.add_signal_receiver(handler_function=callback, dbus_interface='org.freedesktop.NetworkManager.VPN.Connection',
                            signal_name='VpnStateChanged')


def monitor_vpn(uuid, callback):
    """
    This installs a dbus callback which will be called every time the state of a specific VPN changes

    args:
        callback (func): a callback function
    """
    if not have_dbus():
        return

    connection = NetworkManager.Settings.GetConnectionByUuid(uuid)
    connection.connect_to_signal('Updated', callback)