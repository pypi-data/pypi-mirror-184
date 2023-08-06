"""This module performs various types IP address utilities."""
# pylint: disable=protected-access,broad-except,too-many-arguments,wrong-import-order
import ipaddress
from functools import reduce
from ipaddress import IPv4Address, IPv4Network
from socket import getservbyname
from typing import List
from netaddr import IPAddress


def ipwildcard_to_cidr(ip_address, wildcard):
    """Takes ip address, wildcard mask as input & returns CIDR notation.

    Args:
        ip_address (str, required): ipv4 address.
        wildcard (str, required): ipv4 address's wildcard mask.


    Returns:
        (str): CIDR notated IP address.
    """
    try:
        prefix_length = str(
            IPv4Address._prefix_from_ip_int(int(IPv4Address(wildcard)) ^ (2**32 - 1))
        )  # pylint: disable=W0212
    except ipaddress.NetmaskValueError:
        print(f"Wildcard mask: {wildcard} is non-contiguous and cannot be processed!")
        prefix_length = "Error"
    ipv4 = ip_address + "/" + prefix_length

    return ipv4


def ipnetmask_to_cidr(ip_address, subnet_mask):
    """Takes ip address, subnet mask as input & returns CIDR notation.

    Args:
        ip_address (str, required): ipv4 address.
        netmask (str, required): ipv4 address's subnet mask.


    Returns:
        (str): CIDR notated IP address.
    """
    try:
        prefix_length = str(IPAddress(subnet_mask).netmask_bits())
    except Exception:
        prefix_length = "Error"
    ipv4 = ip_address + "/" + prefix_length

    return ipv4


def get_port_number(port_name):
    """Converts port protocol name to port service number.

    Args:
        port_name (str, required): Transport protocol name

    Returns:
        (str): The port number associated with the given protocol
    """
    try:
        if port_name == "non500-isakmp":
            port_name = "4500"
        else:
            port_name = getservbyname(port_name)
        return str(port_name)
    except Exception:
        return str(port_name)


def cidr_to_ipnetmask(ip_address):
    """Converts ip address in CIDR notation to ipv4 address & subnet mask.

    Args:
        ip_address (str, required): ipv4 address.

    Returns:
        (str): ipv4 address & subnet mask.
    """
    address = IPv4Network(ip_address).network_address
    netmask = IPv4Network(ip_address).netmask
    return str(address) + " " + str(netmask)


def prefix_to_wildcard(prefix):
    """Converts prefix length to wildcard mask.

    Args:
        prefix (str, required): prefix length value as a string.

    Returns:
        (str): wildcard mask.
    """
    return str(IPv4Address(int(IPv4Address._make_netmask(prefix)[0]) ^ (2**32 - 1)))


def netmask_to_wildcard(netmask):
    """Converts subnet mask to wildcard mask.

    Args:
        prefix (str, required): ipv4 address.

    Returns:
        (str): wildcard mask.
    """
    return str(IPv4Address(int(IPv4Address(netmask)) ^ (2**32 - 1)))


def wildcard_to_netmask(wildcard):
    """Converts wildcard mask to subnet mask.

    Args:
        wildcard (str, required): wildcard mask.

    Returns:
        (str): subnet mask.
    """
    return str(IPv4Address(int(IPv4Address(wildcard)) ^ (2**32 - 1)))
