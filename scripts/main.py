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
        out[module.__module__] = module.out

    with open("nx-links.json", 'w') as out_file:
        json.dump(out, out_file, indent=4)
