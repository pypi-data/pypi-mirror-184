# Network Automation Utilities

This package contains a variety of modules. Some are for general Python tasks like file conversions, others are for aiding Network Engineering  Automation. I have and still use many of these utilities as an Automation Engineer. 


## Installation

Run `pip install netauto_utils`poetry add netauto_utils`.

If you can *not* install, clone the repository & run `poetry install` to install the package. 

_NOTE:_ Other package managers such as `pip` can also be used for installation.

You can also clone and install the package locally with:

```bash
$ git clone https://github.com/ns03444/netauto_utils.git
$ cd netauto_utils
$ poetry install  # Use --no-dev if you don't want development dependencies
```

## Quick Start

Example of using a utility in the `data_converter` module to convert a Python object to a YAML file:

See source code for more info on the utilities and their associated parameters.

```python
# Import module
>>> 
>>> from netauto_utils import data_converter
>>> 
>>> python_obj = {
...     "Yaml Data": [
...         {"a": 1, "b": 2},
...         {"c": 3, "d": 4},
...         {"e": 5, "f": 6},
...     ]
... }
>>> 
>>> write_file = True
>>> 
>>> filename = 'my_new_yaml_file.yml'
>>> 
>>> 
>>> print(data_converter.python_to_yaml(python_obj, write_file, filename))
my_new_yaml_file.yml has been created! 👍

Yaml Data:
  - a: 1
    b: 2
  - c: 3
    d: 4
  - e: 5
    f: 6

>>>
```
The new YAML file generated `my_new_yaml_file.yml`.
```
---
Yaml Data:
  - a: 1
    b: 2
  - c: 3
    d: 4
  - e: 5
    f: 6

```

## Modules


### `cisco_show`
This is a Python module that contains functions that retrieve various information from a Cisco device. It uses the Netmiko library to establish a connection to the device and send commands to it. The information it retrieves includes IP interface brief information, the primary IP address for a given interface, the access control lists and prefix lists used in a given route map, and BGP peer information for the default VRF. The module also contains some other functions that are used to process and manipulate this data.

### `command_sender`
This is a Python module that contains functions for sending show and configuration commands to a remote network device using the Netmiko library. It can be used to establish an SSH connection to the device, send commands to it, and retrieve the output. The module includes functions for opening and closing a connection to the device, sending configuration commands, and sending show commands. It also includes a function for parsing the output of show commands using TextFSM. The module also contains some error handling to catch and handle common exceptions that may occur when using Netmiko.

### `data_converter`
This is a Python module that contains functions for performing various types of data formatting conversions. It includes functions for converting data between different formats, such as Python dictionaries and lists to YAML or JSON, and for reading and writing data to and from files in different formats. It also includes a function for reading data from a CSV file and returning it as a list of dictionaries. The module uses the json, yaml, and csv libraries to handle these conversions. It also includes some error handling to catch and handle exceptions that may occur when reading or writing data to files.

### `ip_address`
- The function ipwildcard_to_cidr() takes an IP address and a wildcard mask as input, and returns the IP address in CIDR notation.

- The function ipnetmask_to_cidr() takes an IP address and a subnet mask as input, and returns the IP address in CIDR notation.

- The function get_port_number() takes a transport protocol name as input, and returns the port number associated with the protocol. If the protocol name is not recognized, it returns the original protocol name.

- The function cidr_to_ipnetmask() takes an IP address in CIDR notation as input, and returns the IP address and its corresponding subnet mask.

- The function prefix_to_wildcard() takes a prefix length as input and returns the corresponding wildcard mask.

- The function netmask_to_wildcard() takes a subnet mask as input and returns the corresponding wildcard mask.

- The function wildcard_to_netmask() takes a wildcard mask as input and returns the corresponding subnet mask.



## Cutting a New Release
1. Checkout develop branch - ensure you have the latest commits by running git pull
2. Create new branch - git checkout -b <new-branch>

Perform the following operations:
- Run poetry version <major/minor/patch> to update version in pyproject.toml
- Edit CHANGELOG.md - Update for new version with changes included in new version
- Run poetry update to update Python dependencies
- Commit all changes - push branch to GitLab
- Open new MR for your new branch into master
- After the merge is completed, cut a new tag (Repository > Tags > Name: vX.X.X)
- Open new MR from master into develop to sync branches (master will not be deleted).

