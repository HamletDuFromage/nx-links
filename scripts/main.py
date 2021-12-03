import importlib
import argparse
import json


def compileMasterFile(modules):
    out = {}
    for module in modules:
        with open(f"{module}.json", 'r') as module_file:
            out[module] = json.load(module_file)
    with open("nx-links.json", 'w') as out_file:
        json.dump(out, out_file, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Get links for AiO-Switch-Updater")
    requiredNamed = parser.add_argument_group('Require arguments')
    requiredNamed.add_argument(
        '-gt', '--githubToken', help='Github Token', required=True)
    args = parser.parse_args()
    """ modules = ["cfws", "bootloaders", "sigpatches",
               "firmwares", "payloads", "hekate"] """
    modules = ["firmwares"]
    for module in modules:
        importlib.import_module(module)

    compileMasterFile(modules)
