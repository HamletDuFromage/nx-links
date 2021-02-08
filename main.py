import importlib
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get links for AiO-Switch-Updater")
    requiredNamed = parser.add_argument_group('Require arguments')
    requiredNamed.add_argument('-gt', '--githubToken', help='Github Token', required=True)
    args = parser.parse_args()
    importlib.import_module("atmosphere")
    importlib.import_module("cfw")
    importlib.import_module("sigpatches")
    importlib.import_module("firmwares")
    importlib.import_module("sxos")
    importlib.import_module("payloads")