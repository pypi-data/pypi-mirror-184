"""This module is will pull common cisco information from cisco device."""
# pylint: disable=protected-access,broad-except,too-many-arguments,wrong-import-order


from collections import defaultdict
from rich.console import Console
from netauto_utils import command_sender

console = Console()


def get_int_ip_brief(net_connect):
    """Get IP interface brief information from cisco.

    Args:
        net_connect (pointer, required): Netmiko point to device.

    Returns:
        (Dict): Interface name and status for each interface.
    """
    cisco_command = "show ip interface brief"
    int_data = command_sender.send_show_commands(net_connect, [cisco_command], "genie")
    int_data = int_data[cisco_command]["interface"]
    for int_details in int_data.values():
        del int_details["method"]
        del int_details["interface_is_ok"]
    return int_data


def get_int_ipaddr(net_connect, int_name):
    """Get Primary IP Address defined on interface.

    Args:
        int_name (str, required): Full Interface Name.
        net_connect (pointer, required): Netmiko point to device.

    Returns:
        (str): Primary IP address for interface.
    """
    cisco_command = "show interface " + int_name
    int_data = command_sender.send_show_commands(net_connect, [cisco_command], "genie")
    int_data = int_data[cisco_command]

    if "Invalid" in int_data:
        ip_addr = ["Interface not found"]
    elif "ipv4" in int_data[int_name]:
        ip_addr = list(int_data[int_name]["ipv4"].keys())
    else:
        ip_addr = ["IPv4 address not found"]
    return ip_addr[0]


def get_rm_list_name(net_connect, rm_name):
    """Return ACL and Prefix lists used within simple route map.

    Args:
        rm_name (str, required): Route Map Name.
        net_connect (pointer, required): Netmiko point to device.

    Returns:
        (List): acl and prefix names used in route map.
    """
    rm_acls = []
    rm_prefix_lists = []
    cisco_command = "show route-map " + rm_name
    rm_data = command_sender.send_show_commands(net_connect, [cisco_command], "genie")

    if "not found" in rm_data[cisco_command]:
        return rm_data[cisco_command]
    rm_statements = rm_data[cisco_command][rm_name]["statements"]
    # pprint.pprint(rm_statements)
    for rm_statement in rm_statements.values():
        rm_conditions = rm_statement["conditions"]
        if "match_access_list" in rm_conditions:
            rm_acls.append(rm_conditions["match_access_list"])
        elif "match_prefix_list" in rm_conditions:
            rm_prefix_lists.append(rm_conditions["match_prefix_list"])
    return rm_acls, rm_prefix_lists


def get_bgp_peers(net_connect):
    """Get list of BGP peers for default VRF.

    Args:
        net_connect (pointer, required): Netmiko point to device.

    Returns:
        (Tuple): List of BGP peer IP addresses and List of BGP peering data for each peer.
    """
    cisco_command = "show bgp all neighbor"
    output = command_sender.send_show_commands(net_connect, [cisco_command], "genie")
    output = output[cisco_command]
    # pprint.pprint(output)
    current_peers = output["list_of_neighbors"]
    default_vrf_bgpdata = output["vrf"]["default"]["neighbor"]
    return current_peers, default_vrf_bgpdata


def get_bgp_policy(net_connect, current_peers):
    """Create data structure for route policy locations and names."""
    print("build neighbor policy")
    bgp_policy_data = defaultdict()
    for bgp_peer_ip in current_peers:
        show_command = f"show bgp all neighbors {bgp_peer_ip} policy"
        output = command_sender.send_show_commands(net_connect, [show_command], "genie")
        output = output[show_command]
        if isinstance(output, str):
            policies = output.split("\n")
            policy_dict = {
                "prefix-list-in": "",
                "prefix-list-out": "",
                "distribute-list-in": "",
                "distribute-list-out": "",
            }
            for line in policies:
                words = line.split()
                if "Neighbor" in line:
                    neigh_ip = words[1][:-1]
                    if neigh_ip not in bgp_policy_data:
                        bgp_policy_data[neigh_ip] = {}
                if "prefix-list" in line or "distribute-list" in line:
                    key = words[0] + "-" + words[2]
                    policy_dict[key] = words[1]
            bgp_policy_data[neigh_ip].update(policy_dict)
        elif isinstance(output, dict):
            rm_dict = {"rm_in_name": "", "rm_out_name": ""}
            for key, value in output["vrf"]["default"]["neighbor"].items():
                rm_names = value["address_family"]["ipv4 unicast"]
                if "nbr_af_route_map_name_in" in rm_names:
                    rm_dict["rm_in_name"] = rm_names["nbr_af_route_map_name_in"]
                if "nbr_af_route_map_name_out" in rm_names:
                    rm_dict["rm_out_name"] = rm_names["nbr_af_route_map_name_out"]
                if key not in bgp_policy_data:
                    bgp_policy_data[key] = rm_dict
    return bgp_policy_data


def build_prefix_list_data(net_connect):
    """Create cisco prefix list data structure."""
    print("build prefix list data")
    prefix_list_dict = defaultdict()
    show_command = "show ip prefix-list"
    prefix_list_data = command_sender.send_show_commands(net_connect, [show_command], "textfsm")
    prefix_list_data = prefix_list_data[show_command]
    # print(f"prefix list data is {prefix_list_data}")
    if prefix_list_data:
        list_data = list(zip(*[dict_data.values() for dict_data in prefix_list_data]))
        prefix_names = list(set(list_data[0]))
        for pl_name in prefix_names:
            for item in prefix_list_data:
                if pl_name == item["name"]:
                    if item["name"] not in prefix_list_dict:
                        prefix_list_dict[pl_name] = []
                    prefix_list_dict[pl_name].append(item)
    return prefix_list_dict
