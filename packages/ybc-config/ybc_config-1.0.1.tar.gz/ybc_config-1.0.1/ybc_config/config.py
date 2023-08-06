import os

profiles_config = {"online": {"prefix": "https://www.yuanfudao.com"},
                   "test": {"prefix": "https://ke.yuanfudao.ws"},
                   "local": {"prefix": "https://ke.yuanfudao.ws"}
                   }
config = {}

uri = '/tutor-ybc-course-api-v2/api'

def _read_config(key):
    return os.environ[key] if key in os.environ else None


ybc_profile = _read_config("YBC_PROFILE")
if ybc_profile is not None and ybc_profile in profiles_config:
    config = profiles_config[ybc_profile]
else:
    config = profiles_config["online"]