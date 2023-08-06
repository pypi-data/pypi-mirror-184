"""This module performs various types of data formatting conversions."""
# pylint: disable=protected-access,too-many-arguments,wrong-import-order,unspecified-encoding,super-with-arguments,too-many-ancestors
from collections import OrderedDict
from csv import DictReader
import json
import yaml
from rich.console import Console

console = Console()


class NoAliasDumper(yaml.Dumper):
    """Supports indentation for yaml file generation."""

    def ignore_aliases(self, data):
        """Supports indentation for yaml file generation."""
        return True

    def increase_indent(self, flow=True, indentless=False):
        """Supports indentation for yaml file generation."""
        return super(NoAliasDumper, self).increase_indent(flow, False)


def ordered_dict_representer(self, value):
    """Supports indentation for yaml file generation."""
    return self.represent_mapping("tag:yaml.org,2002:map", value.items())


yaml.add_representer(OrderedDict, ordered_dict_representer)


def python_to_yaml(python_obj, write_file=False, filename=None):
    """Converts Python list or dictionary to YAML formatted data.

    Args:
        python_obj (list/dict, required): Python list or dictionary to be converted to YAML.
        write_file (bool, optional): Write YAML file.
        filename (str, optional): Name of new yaml file.

    Returns:
        (str): String representation of the YAML formatted data.
    """
    if dict(python_obj):
        yaml_obj = yaml.dump(
            OrderedDict(python_obj),
            Dumper=NoAliasDumper,
            default_flow_style=False,
            indent=2,
            sort_keys=False,
        )
        if write_file:
            store_file = f"{filename}"
            with open(store_file, "w") as file:
                file.write("---\n" + yaml_obj)
            console.print(f"[underline]{store_file}[/] has been created! :thumbs_up:\n", style="bold green")
        return yaml_obj

    yaml_obj = yaml.dump(python_obj)
    if write_file:
        store_file = f"{filename}"
        with open(store_file, "w") as file:
            file.write("---\n" + yaml_obj)
        console.print(f"[underline]{store_file}[/] has been created! :thumbs_up:\n", style="bold green")
    return yaml_obj


def json_to_dict(json_data):
    """Converts JSON data to python dictionary.

    Args:
        json_string (str, required): Name of new yaml file.

    Returns:
        (str): String representation of the YAML formatted data
    """
    py_dct = json.load(json_data)
    console.print("JSON string has been converted to Python Dictionary! :thumbs_up:\n", style="bold green")
    return py_dct


def python_to_json(python_obj):
    """Converts JSON data to python dictionary.

    Args:
        json_string (str, required): Name of new yaml file.

    Returns:
        (str): String representation of the YAML formatted data
    """
    return json.dumps(python_obj)


def txt_to_python(fhand):
    """Converts JSON data to python dictionary.

    Args:
        json_string (str, required): Name of new yaml file.

    Returns:
        (str): String representation of the YAML formatted data
    """
    with open(fhand) as file:
        lst = file.readlines()

    return lst


def get_json_data(fname):
    """Read file to get json data..

    Args:
        fname (str, required): Name of JSON file to be read.

    Returns:
        (Dict): Ordered dictionary read from file.
    """
    with open(fname, encoding="utf8") as data:
        json_data = data.read()
    json_dict = json.loads(json_data, object_pairs_hook=OrderedDict)
    return json_dict


def read_csv_as_dict(fname):
    """Read csv file to return each row in csv file as dictionary.

    Args:
        fname (str, required): Name of CSV file to be read (normally with .csv extension).

    Returns:
        (List): List of Dictionaries where each dictionary in list is row from csv file.
    """
    with open(fname, "r") as csv_fname:
        new_dict = DictReader(csv_fname)
        csv_dict = list(new_dict)
    return csv_dict