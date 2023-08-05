[![banner](doc/img/repo-banner@2x.png)](https://oceanprotocol.com)

<h1 align="center">oceandb-bigchaindb-driver</h1>

> 🐳 Ocean DB [BigchainDB](https://www.bigchaindb.com/) driver (Python).
> [oceanprotocol.com](https://oceanprotocol.com)

[![Travis (.com)](https://img.shields.io/travis/com/oceanprotocol/oceandb-bigchaindb-driver.svg)](https://travis-ci.com/oceanprotocol/oceandb-bigchaindb-driver)
[![Codacy coverage](https://img.shields.io/codacy/coverage/be42a51b898e46c7b7c2531d49a4e1ac.svg)](https://app.codacy.com/project/ocean-protocol/oceandb-bigchaindb-driver/dashboard)
[![PyPI](https://img.shields.io/pypi/v/oceandb-bigchaindb-driver.svg)](https://pypi.org/project/oceandb-bigchaindb-driver/)
[![GitHub contributors](https://img.shields.io/github/contributors/oceanprotocol/oceandb-bigchaindb-driver.svg)](https://github.com/oceanprotocol/oceandb-bigchaindb-driver/graphs/contributors)

---

## Table of Contents

  - [Features](#features)
  - [Quick-start](#quick-start)
  - [About BigchainDB plugin implementation](#about-bigchaindb-plugin-implementation)
  - [Code style](#code-style)
  - [Testing](#testing)
  - [License](#license)

---

## Features

BigchainDB driver to connect implementing OceanDB.

## Quick-start

First of all we have to specify where is allocated our config.
To do that we have to pass the following argument:

```

    --config=/path/of/my/config
```

If you do not provide a configuration path, by default the config is expected in the config folder.

In the configuration we are going to specify the following parameters to

```yaml
    [oceandb]

    enabled=true            # In order to enable or not the plugin
    module=bigchaindb       # You can use one the plugins already created. Currently we have mongodb and bigchaindb.
    module.path=            # You can specify the location of your custom plugin.
    db.hostname=localhost   # Address of your bigchaindb nodes.
    db.port=9985            # Port of your bigchaindb database.

    # Bigchaindb specific config:
    secret=                 # A secret that serves as a seed.
    db.namespace=namespace  # Namespace that you are going to use in bigchaindb
    db.app_id=              # App id of your bigchaindb application.
    db.app_key=             # App key of your bigchaindb application.
```

Once you have defined this the only thing that you have to do it is use it:

```python

    oceandb = OceanDb(confPath)
    tx_id = oceandb.write({"value": "test"})  #Write a new transaction in bdb.
    oceandb.read(tx_id)                       #Read the content of this transaction
    oceandb.update({"value": "update"},tx_id) #Update value of the transaction.
    oceandb.delete(tx_id)                     #Delete transaction
```


## About BigchainDB plugin implementation


CRAB is the CRUD model in databases applied to blockchains:

+--------------+----------------+
| Database     | Blockchain     |
+==============+================+
| **C**\ reate | **C**\ reate   |
+--------------+----------------+
| **R**\ ead   | **R**\ etrieve |
+--------------+----------------+
| **U**\ pdate | **A**\ ppend   |
+--------------+----------------+
| **D**\ elete | **B**\ urn     |
+--------------+----------------+

You can find `here <https://blog.bigchaindb.com/crab-create-retrieve-append-burn-b9f6d111f460>`_ a link talking about the CRAB model.

## Code style

The information about code style in python is documented in this two links [python-developer-guide](https://github.com/oceanprotocol/dev-ocean/blob/master/doc/development/python-developer-guide.md)
and [python-style-guide](https://github.com/oceanprotocol/dev-ocean/blob/master/doc/development/python-style-guide.md).
    
## Testing

Automatic tests are setup via Travis, executing `tox`.
Our test use pytest framework.


## License

```
Copyright 2018 Ocean Protocol Foundation Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.