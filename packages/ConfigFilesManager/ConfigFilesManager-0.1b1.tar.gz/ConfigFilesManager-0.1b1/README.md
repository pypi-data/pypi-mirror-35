# ConfigFilesManager
A python module to a easy manage configs files for applications


# Why?
This module help you to manage configurations files of python applications.
So, you can check the value or type of a variable in configuration file, without to 
have write more code. You can check if a required variables is present or not. And then 
raise (or not) Exceptions.


# Sample
For example if we have a config file like this:

```ini
[CONFIG]
# Configuration file
IP = 127.0.0.1
PORT = 27017
DB_NAME = CoreDatabase
INSTALL_PATH = /home/eamanu/dev/test_coremanagement
; timeout on milliseconds. 5000 ms = 5 seconds
TIMEOUT_DB_MS = 5000
```

If we want all the variables to be obligatory, we have to mark the variable 
like 'required'. Then, we have to say what is the type is the variable.

Our code is the next: 

```python

from configFilesManager import configFilesManager

schema = {'CONFIG': {'IP': {'type': 'str', 'required': True},
                        'TIMEOUT_DB_MS': {'type': 'int', 'required': True},
                        'PORT': {'type': 'int', 'required': True},
                        'DB_NAME': {'type': 'str', 'required': True},
                        'INSTALL_PATH': {'type': 'str', 'required': True}}}

config = 'path/to/config.ini'

cfm = configFilesManager(config, schema)
cfm.run_check()

```

If whole it's ok, you don't have catch any exception, but if some is bad you 
will have a Exception raised. You could access to the values of the configs 
parsed on `cfm.parser_config_dict` dict


# Contribution

Please see [CONTRIBUTE.md](CONTRIBUTE.md)