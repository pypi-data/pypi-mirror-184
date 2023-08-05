from wora.file import (exists, read_file)

import toml

def load_toml_config(configfp: str) -> dict:
    ''' Reads the toml config file into a dictionary '''
    result = dict
    if (exists(configfp)):
        result = toml.loads(read_file(configfp))
    return result
