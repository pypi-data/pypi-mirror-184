# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netauto_utils']

package_data = \
{'': ['*']}

install_requires = \
['netaddr>=0.8.0,<0.9.0',
 'netmiko>=4.1.2,<5.0.0',
 'paramiko>=2.12.0,<3.0.0',
 'rich>=13.0.1,<14.0.0']

setup_kwargs = {
    'name': 'netauto-utils',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Network Automation Utilities\n\nThis package contains a variety of modules. Some are for general Python tasks like file conversions, others are for aiding Network Engineering  Automation. I have and still use many of these utilities as an Automation Engineer. \n\n\n## Installation\n\nRun `pip install netauto_utils`poetry add netauto_utils`.\n\nIf you can *not* install, clone the repository & run `poetry install` to install the package. \n\n_NOTE:_ Other package managers such as `pip` can also be used for installation.\n\nYou can also clone and install the package locally with:\n\n```bash\n$ git clone https://github.com/ns03444/netauto_utils.git\n$ cd netauto_utils\n$ poetry install  # Use --no-dev if you don\'t want development dependencies\n```\n\n## Quick Start\n\nExample of using a utility in the `data_converter` module to convert a Python object to a YAML file:\n\nSee source code for more info on the utilities and their associated parameters.\n\n```python\n# Import module\n>>> \n>>> from netauto_utils import data_converter\n>>> \n>>> python_obj = {\n...     "Yaml Data": [\n...         {"a": 1, "b": 2},\n...         {"c": 3, "d": 4},\n...         {"e": 5, "f": 6},\n...     ]\n... }\n>>> \n>>> write_file = True\n>>> \n>>> filename = \'my_new_yaml_file.yml\'\n>>> \n>>> \n>>> print(data_converter.python_to_yaml(python_obj, write_file, filename))\nmy_new_yaml_file.yml has been created! 👍\n\nYaml Data:\n  - a: 1\n    b: 2\n  - c: 3\n    d: 4\n  - e: 5\n    f: 6\n\n>>>\n```\nThe new YAML file generated `my_new_yaml_file.yml`.\n```\n---\nYaml Data:\n  - a: 1\n    b: 2\n  - c: 3\n    d: 4\n  - e: 5\n    f: 6\n\n```\n\n## Modules\n\n\n### `cisco_show`\nThis is a Python module that contains functions that retrieve various information from a Cisco device. It uses the Netmiko library to establish a connection to the device and send commands to it. The information it retrieves includes IP interface brief information, the primary IP address for a given interface, the access control lists and prefix lists used in a given route map, and BGP peer information for the default VRF. The module also contains some other functions that are used to process and manipulate this data.\n\n### `command_sender`\nThis is a Python module that contains functions for sending show and configuration commands to a remote network device using the Netmiko library. It can be used to establish an SSH connection to the device, send commands to it, and retrieve the output. The module includes functions for opening and closing a connection to the device, sending configuration commands, and sending show commands. It also includes a function for parsing the output of show commands using TextFSM. The module also contains some error handling to catch and handle common exceptions that may occur when using Netmiko.\n\n### `data_converter`\nThis is a Python module that contains functions for performing various types of data formatting conversions. It includes functions for converting data between different formats, such as Python dictionaries and lists to YAML or JSON, and for reading and writing data to and from files in different formats. It also includes a function for reading data from a CSV file and returning it as a list of dictionaries. The module uses the json, yaml, and csv libraries to handle these conversions. It also includes some error handling to catch and handle exceptions that may occur when reading or writing data to files.\n\n### `ip_address`\n- The function ipwildcard_to_cidr() takes an IP address and a wildcard mask as input, and returns the IP address in CIDR notation.\n\n- The function ipnetmask_to_cidr() takes an IP address and a subnet mask as input, and returns the IP address in CIDR notation.\n\n- The function get_port_number() takes a transport protocol name as input, and returns the port number associated with the protocol. If the protocol name is not recognized, it returns the original protocol name.\n\n- The function cidr_to_ipnetmask() takes an IP address in CIDR notation as input, and returns the IP address and its corresponding subnet mask.\n\n- The function prefix_to_wildcard() takes a prefix length as input and returns the corresponding wildcard mask.\n\n- The function netmask_to_wildcard() takes a subnet mask as input and returns the corresponding wildcard mask.\n\n- The function wildcard_to_netmask() takes a wildcard mask as input and returns the corresponding subnet mask.\n\n\n\n## Cutting a New Release\n1. Checkout develop branch - ensure you have the latest commits by running git pull\n2. Create new branch - git checkout -b <new-branch>\n\nPerform the following operations:\n- Run poetry version <major/minor/patch> to update version in pyproject.toml\n- Edit CHANGELOG.md - Update for new version with changes included in new version\n- Run poetry update to update Python dependencies\n- Commit all changes - push branch to GitLab\n- Open new MR for your new branch into master\n- After the merge is completed, cut a new tag (Repository > Tags > Name: vX.X.X)\n- Open new MR from master into develop to sync branches (master will not be deleted).\n\n',
    'author': 'ns03444',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
