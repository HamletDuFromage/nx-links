import json

import cfws
import firmwares
import sigpatches
import app

if __name__ == '__main__':

    json_file = "nx-links.json"
    try:
        with open(json_file, "r") as old_file:
            out = json.load(old_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        out = {}

    modules = [
        cfws.Cfws(),
        sigpatches.Sigpatches(),
        firmwares.Firmwares(),
        app.App()
    ]
    for module in modules:
        if module.out == {}:
            print(f"Module {module.__module__} returned an empty dict.")
        out[module.__module__] = module.out

    with open(json_file, 'w') as out_file:
        json.dump(out, out_file, indent=4)
