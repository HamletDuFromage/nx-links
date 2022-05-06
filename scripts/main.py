import argparse
import json

import bootloaders
import cfws
import firmwares
import hekate
import payloads
import sigpatches
import hekate_ipl


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Get links for AiO-Switch-Updater")
    requiredNamed = parser.add_argument_group('Require arguments')
    requiredNamed.add_argument(
        '-gt', '--githubToken', help='Github Token', required=True)
    args = parser.parse_args()

    json_file = "nx-links.json"
    try:
        with open(json_file, "r") as old_file:
            out = json.load(old_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        out = {}

    modules = [
        bootloaders.Bootloaders(),
        cfws.Cfws(),
        hekate.Hekate(),
        payloads.Payloads(),
        sigpatches.Sigpatches(),
        firmwares.Firmwares(),
        hekate_ipl.HekateIpl()
    ]
    for module in modules:
        if module.out == {}:
            print(f"Module {module.__module__} returned an empty dict. It will be skipped.")
        else:
            out[module.__module__] = module.out

    with open(json_file, 'w') as out_file:
        json.dump(out, out_file, indent=4)
