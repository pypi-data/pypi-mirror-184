"""This module is for sending show or configuration commands to a remote network device."""
# pylint: disable=protected-access,broad-except,too-many-arguments,too-many-branches,wrong-import-order

import sys
import textfsm

from rich.console import Console
from paramiko import SSHException
from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException
from netmiko import NetMikoAuthenticationException
from netmiko import exceptions

console = Console()


def open_connection(device_type, device_ip, username, password):
    """Opens a connection to a device for use with NetMiko.

    Args:
        device_type (str, required): Type of device being configured.
        device_ip (str, required): Device's management IP.
        username (str, required): Username for ssh connection authentication.
        password (str, required): Password for ssh connection authentication.

    Returns:
        (list): pointer to network connection to device and current prompt.
    """
    device = {
        "device_type": device_type,
        "host": device_ip,
        "username": username,
        "password": password,
        "global_delay_factor": 4,
    }
    try:
        ssh_link = ConnectHandler(**device)
        ssh_link.enable()
        output = ssh_link.find_prompt()
        if "% Invalid" in output:
            return (
                console.print(output),
                console.print("Something went wrong. Please check your commands", style="bold red"),
            )
        return ssh_link, output
    except exceptions.NetmikoAuthenticationException:
        console.print(f"Authentication Failure!\n{device_type}", style="bold red")
        sys.exit()
    except exceptions.NetMikoTimeoutException:
        console.print("\n" + f"Timeout to device!\n{device_type}", style="bold red")
        sys.exit()
    except exceptions.SSHException:
        console.print(f"SSH might not be enabled!\n{device_type}", style="bold red")
        sys.exit()
    except EOFError:
        console.print("\n" + f"End of attempting device!\n{device_type}", style="bold red")
        sys.exit()


def close_connection(ssh_link):
    """Closes a Netmiko link to a device."""
    ssh_link.disconnect()


def send_config_commands(ssh_link, commands):
    """Sends a set of configuration commands using Netmiko.

    Args:
        ssh_link (ptr, required): Pointer to device being configured.
        commands (list, required): list of configuration commands.

    Returns:
        (str): router cli output
    """
    # Establish SSH Connection
    # Push configuration changes to remote device
    try:
        ssh_link.enable()
        output = ssh_link.send_config_set(commands)
        if "% Invalid" in output:
            return (
                console.print(output),
                console.print("Something went wrong. Please check your commands", style="bold red"),
            )
        console.print("Command completed!\n:thumbs_up:", style="bold green")
        return output
    except exceptions.NetmikoAuthenticationException:
        console.print("Authentication Failure!\n", style="bold red")
        sys.exit()
    except exceptions.NetMikoTimeoutException:
        console.print("\n" + "Timeout to device!\n", style="bold red")
        sys.exit()
    except exceptions.SSHException:
        console.print("SSH might not be enabled!\n", style="bold red")
        sys.exit()
    except EOFError:
        console.print("\n" + "End of attempting device!\n", style="bold red")
        sys.exit()


def send_show_commands(ssh_link, commands, parsing_tool):
    """Sends a single show command or a list of show commands using Netmiko.

    Args:
        ssh_link (ptr, required): Pointer to device being configured.
        commands (list, required): list of one or more show commands.
        parse_tool (optional): either genie or textfsm

    Returns:
        (str): Display configuration terminal changes
    """
    show_output = {}
    # Establish SSH Connection
    ssh_link.enable()
    if isinstance(commands, list):
        cmd_output = ""
        if not parsing_tool:
            for cmd in commands:
                cmd_output = ssh_link.send_command(cmd)
                new_dict = {cmd: cmd_output}
                show_output.update(new_dict)
            return show_output
        for cmd in commands:
            try:
                if "genie" in parsing_tool:
                    cmd_output = ssh_link.send_command(cmd, use_genie="True")
                elif "textfsm" in parsing_tool:
                    cmd_output = ssh_link.send_command(cmd, use_textfsm="True")
                new_dict = {cmd: cmd_output}
                show_output.update(new_dict)
            except NetMikoAuthenticationException:
                print("Authentication Failure: ")
                sys.exit()
            except NetMikoTimeoutException:
                print("\n" + "Timeout to device: ")
                sys.exit()
            except SSHException:
                print("SSH might not be enabled: ")
                sys.exit()
            except EOFError:
                print("\n" + "End of attempting device: ")
                sys.exit()
            except textfsm.TextFSMTemplateError:
                print(f"\n Text FSM unable to parse command: {cmd}")
                sys.exit()
            except textfsm.TextFSMError:
                print(f"\n Text FSM unable to parse command: {cmd}")
                sys.exit()
    else:
        print(f"Show commands must be of type python list.  Currently it is of type {type(commands)}")
    return show_output
