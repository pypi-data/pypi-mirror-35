import os
import yaml

profiles_config = {}
config = {}

with open("config.yaml") as f:
    profiles_config = yaml.load(f.read())

def _read_config(key):
    return os.environ[key] if key in os.environ else None

ybc_profile = _read_config("YBC_PROFILE")
if ybc_profile is not None and ybc_profile in profiles_config:
    config = profiles_config[ybc_profile]
else:
    config = profiles_config["online"]